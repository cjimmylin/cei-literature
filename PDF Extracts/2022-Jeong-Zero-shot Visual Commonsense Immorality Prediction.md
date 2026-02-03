---
title: "Zero-shot Visual Commonsense Immorality Prediction - PDF Extract"
source_pdf: "2022-Jeong-Zero-shot Visual Commonsense Immorality Prediction.pdf"
pages: 22
extracted_at: "2026-01-24T17:05:10.511419"
---

# PDF Extract: Zero-shot Visual Commonsense Immorality Prediction

**Source PDF:** 2022-Jeong-Zero-shot Visual Commonsense Immorality Prediction.pdf
**Total Pages:** 22

---

## Content

```
--- Page 1 ---

arXiv:2211.05521v1  [cs.CV]  10 Nov 2022
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
1
Zero-shot Visual Commonsense
Immorality Prediction
Yujin Jeong1
eugene6923@korea.ac.kr
Seongbeom Park1
psb485@korea.ac.kr
Suhong Moon2
suhong.moon@berkeley.edu
Jinkyu Kim1
jinkyukim@korea.ac.kr
1 Computer Science and Engineering
Korea University
Seoul 02841, Korea
2 Electrical Engineering and Computer
Sciences
University of California, Berkeley
CA 94720, USA
Abstract
Artiﬁcial intelligence is currently powering diverse real-world applications. These
applications have shown promising performance, but raise complicated ethical issues,
i.e. how to embed ethics to make AI applications behave morally. One way toward
moral AI systems is by imitating human prosocial behavior and encouraging some form
of good behavior in systems. However, learning such normative ethics (especially from
images) is challenging mainly due to a lack of data and labeling complexity. Here, we
propose a model that predicts visual commonsense immorality in a zero-shot manner. We
train our model with an ETHICS dataset (a pair of text and immorality annotation) via
a CLIP-based image-text joint embedding. Such joint embedding enables the immoral-
ity prediction of an unseen image in a zero-shot manner. We evaluate our model with
existing moral/immoral image datasets and show fair prediction performance consistent
with human intuitions, which is conﬁrmed by our human study. Further, we create a
visual commonsense immorality benchmark with more general and extensive immoral
visual content. Codes and dataset are available at https://github.com/ku-vai/
Zero-shot-Visual-Commonsense-Immorality-Prediction. Note that
this paper might contain offensive images and descriptions.
1
Introduction
Despite the explosive developments of Artiﬁcial Intelligence, AI ethics research has been
overlooked from many researchers. The previous research on ethical artiﬁcial intelligence
has been analyzed solely from the philosophical view, but not from the computational per-
spective [3, 29, 48]. Philosophers kept speculating that if computer scientists had focused
only on optimization or problem solving, artiﬁcial intelligence will encounter catastrophes
of immorality [4, 9, 41]. Fortunately, the demand for ethical machine learning has been
increasing and resulted in narrow ethical applications in Artiﬁcial Intelligence.
© 2022. The copyright of this document resides with its authors.
It may be distributed unchanged freely in print or electronic forms.

--- Page 2 ---

2
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
Figure 1: Examples found by our model from ImageNet [14] dataset. Note that we make
some images blurry due to their inappropriate content.
With ETHICS dataset [19], we are now able to evaluate how much a machine learning
system understands human’s ethical judgment for the open-world settings. This dataset con-
sists of some scenarios of justice, deontology, virtue ethics, utilitarianism, and commonsense
moral intuitions. The modality that this dataset covers, however, is only natural language. In
other words, in computer vision ﬁeld, this research is still limited to some speciﬁc tasks such
as detecting gun in the CCTV image [6, 17, 31], violent scene in the movies [10, 18, 46, 49]
and sexual contents in social networks [7, 16, 53].
Despite the fact that visual commonsense immorality prediction task is necessary for the
content moderation, it has not been taken into consideration since supervising a model with
proper visual inputs is challenging. This mainly resulted from two reasons: First, existing
immorality datasets are limited to speciﬁc sub-categories of commonsense immorality (e.g.
NSFW as known as "Not Safe For Work" for sexual contents), where models (trained on
them) are prone to overﬁt and do not generalize well. Second, collecting a wide range of
images that can fully cover commonsense immorality is difﬁcult. Judging the immorality of
a given image is also not an intuitive task, making it hard to create reliable visual datasets.
Thus, we advocate for leveraging a text-image joint embedding space with a large-scale
textual commonsense immorality dataset; we used ETHICS dataset in this paper.
To extend ETHICS dataset to ethical judgement of vision tasks for open-world settings,
we bring the recent advances of large vision-language pretrained models (VLMs) such as
CLIP [35] and DALL-E [36]. For VLMs, language supervision permits zero-shot transfer
for various computer vision tasks. Also, researchers have recently reported that we can re-
trieve toxic image from CLIP with only soft prompt tuning and without additional training
for the vision encoder [42]. This is a promising report in that CLIP model can detect offen-
sive features from the given image. However, the extension of CLIP for predicting ethical
judgements in open-ended settings is not trivial as these retrieved images are not easily gen-
eralized to other ethical scenarios.
To address this issue, we propose a zero-shot visual immorality prediction method. As
shown in Figure 2, our model consists of two main modules: (i) CLIP-based textual and
visual encoders and (ii) a commonsense immorality predictor (described as a classiﬁer in
the Figure 2). We train commonsense immorality predictor only with the ETHICS dataset
by mapping a text (e.g. “I painted the entire school with a nude lady”) to a binary class
(immoral vs. moral). Immorality of an unseen image is then predicted through the CLIP-
based visual encoder and the trained immorality predictor in a zero-shot manner.
To the best of our knowledge, there are only a limited number of image datasets to eval-
uate the performance of visual immorality prediction. Thus, we create a visual immorality
prediction benchmark, which provides more generalized domains suitable for our task. Over-
all 2,172 immoral images are collected through Google Image queries followed by a manual

--- Page 3 ---

JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
3
ﬁltering of irrelevant images. Our contributions are summarized as follows:
• We propose a novel zero-shot visual immorality prediction method. Based on CLIP-
based visual and textual joint embedders, we train an immorality prediction head with
a large-scale ETHICS commonsense dataset. Such a prediction head is then reused for
predicting immorality of an unseen image.
• We evaluate our method with the following ﬁve existing moral and immoral image
datasets: MS-COCO [26], Socio-Moral Image Dataset [12], Sexual Intent Detection
Images [16], NSFW [1], and Real-life Violence Situation Dataset [45]. Further, we
create a more generalized version of immoral image benchmark.
• Our human study with 172 participants from Amazon Mechanical Turk conﬁrms that
our model’s behavior aligns well with human intuition and validates our created dataset’s
effectiveness for the visual commonsense immorality classiﬁcation task.
2
Related Work
AI Ethics. There has been a great deal of effort in the ﬁeld of philosophy towards the concept
of ethical machine learning. A Turing test was developed by Alan Turing to determine if a
machine could act like a human being [48]. Asimov suggested the three laws of robotics as
the underlying principle of machine behavior, but simple rules are unable to make machines
moral due to the complexity of ethics and conﬂict between rules [3]. Moreover, Bostrom et
al. [9] argued that morality cannot be assured if machines are focused solely on problem
solving and may result in serious catastrophes such as paperclip maximizers [8]. In addition,
some existing studies in the philosophical literature have examined AI ethics dilemmas [4,
41].
It has become apparent that machine ethics is of paramount importance; yet, this has
been previously assessed only to a very limited extent due to the fact that machine learn-
ing engineers have focused solely on problem solving. Natural Language ﬁeld have exam-
ined four ethical categories in general so far: Fairness [22], Safety [38], Prosocial [37, 39]
and Utility [11, 23]. In addition to four categories, Commonsense Morality is newly dis-
cussed by Hendrycks et al. [19] Computer Vision has, however, focused primarily on Safety,
since surveillance video (CCTV) and visual content review have been the main tasks in the
area. [51]. In recent computer vision studies, the domain has been broaden to Fairness for
preventing discrimination caused by the dataset bias [2, 32, 44]. As part of this domain
expansion in Computer Vision, we focused on the Commonsense Morality by proposing a
novel visual immorality prediction model which utilizes the power of the generality of natu-
ral language.
Visual Immorality Benchmarks. As the importance of AI ethics has been highlighted,
datasets that provide value judgments as labels become required, which is a new perspective
since conventional datasets provided factual judgments. In the Natural Language ﬁeld, large
datasets have been released to detect aggressive languages [34, 40], and some studies have
also been conducted to collect tweets to judge moral values in SNS conversations [21, 30].
Especially, the recently released ETHICS dataset [19] is a comprehensive dataset, which
combines ﬁve strands of morality values that have been studied individually.
In comparison, visual datasets have dealt with solely speciﬁc domains. In terms of vio-
lence, images and videos from CCTV are collected for weapon detection [6, 17] and brutal
scene detection [33, 47]. Similarly, movies [5, 13, 46], sports [5, 51], and Youtube [45]

--- Page 4 ---

4
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
Figure 2: An overview of our visual commonsense immorality prediction model. In the train-
ing phase, we train our classiﬁer fmorality to predict the degree of commonsense immorality
from a given text prompt, e.g. “I punched my friend”. To train such a module, we use the
ETHICS dataset [19], which contains over 13,000 pairs of sentences or paragraphs and the
corresponding binary annotations of morality for training. We utilize a frozen CLIP [35]-
based image-text joint embedding space, which learns to map pairs of an image and a text to
have the same latent vector. This allows us to predict the degree of morality from an unseen
image in a zero-shot manner.
video datasets are constructed for a violence detection. NSFW [1] and Sexual Intent De-
tection [16] datasets consist of images concerning sexuality. To the best of our knowledge,
Socio-Moral Image Database (SMID) [12] is the only dataset that does not deal with a spe-
ciﬁc domain. However, this dataset, which provides only the morality score of the image
through the human study, does not explain why the image is immoral. Therefore, we cre-
ate a more general and explainable visual commonsense immorality benchmark, providing
images from 25 immoral keywords in 3 categories.
Large Vision-Language Pretrained Models. A large-scale pretraining of vision and lan-
guage modality has signiﬁcantly improved performancein several downstream tasks. CLIP [35]
and ALIGN [20] demonstrate that the pretrained models are able to learn strong multi-modal
representations for crossmodal alignment tasks and zero-shot image classiﬁcation using dual-
encoder model. FLAVA [43] and BLIP [25] have explored image-text uniﬁcation with the
pretraining of multiple unimodal and multimodal modules. CoCa [52] is a latest model that
is trained from scratch in a single pretraining stage. CLIP is jointly trained to associate
joint embeddings of texts and images that share the similar semantics with a 400M image-
caption pair dataset. Vision Transformers (ViT) or ResNets are used for a vision encoder
and Transformer is used for a text encoder. As a result, CLIP generates the robust image and
text features. This model can perform various downstream tasks such as image search and
zero-shot image classiﬁcation. With the help of such pretrained model’s remarkable trans-
ferability, we deliver vast quantities of information about morality embedded in ETHICS
dataset to image modality.
3
Visual Commonsense Immorality Prediction
Learning Visual Commonsense Immorality from ETHICS dataset. In this work, we rely
on the ETHICS dataset [19], which contains over 130,000 text ethical examples of 5 ethical
perspectives: justice, virtue, deontology, utilitarianism, and commonsense. Among them,
we utilize the commonsense morality dataset, which consists of more than 21,000 examples

--- Page 5 ---

JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
5
and corresponding binary labels of the commonsense immorality. This dataset is ideal for
the commonsense immorality prediction task: (i) they provide diverse open-world scenarios
(see the supplemental material for details), (ii) they collect over 21,000 text examples from
four different countries, and (iii) it is designed to evaluate machine understanding about ev-
eryday situations, not ambiguous moral dilemmas. There are two reasons for utilizing text
data rather than visual data: (i) there is no such large-scale dataset for the visual common-
sense immorality prediction task, (ii) collecting such a high-quality and large-scale dataset
is challenging regarding volume, quality, and consistency.
Thus, we advocate for utilizing a pre-trained image-text joint embedding space, which
maps a pair of a text prompt and an image into the same embedding. Given this joint em-
bedding space, we ﬁrst train a text-based commonsense immorality predictor, which learns
to predict the degree of the immorality of a given text prompt (e.g. “I punched my friend”).
Such an immorality predictor can be reused for an image-based commonsense immorality
predictor. Our image encoder maps an input image to a joint text-image embedding space,
and the learned immorality predictor predicts the degree of visual commonsense immoral-
ity. In Figure 2, we visualize an overview of our proposed visual commonsense immorality
prediction model. In the following sections, we explain it in detail.
CLIP-based Image-Text Joint Embedding. Our model depends on a text-image joint em-
bedder, which maps a pair of an image xv ∈I (e.g. a photo of people punching each other)
and a text xt ∈T (e.g. “I punched my friend”) into the same embedding space by minimizing
the (cosine) distance between a mini-batch of n image and text representation pairs {vi,ti}
for i ∈{1,2,...,n}. We use two different encoders fv and ft to obtain a set of d-dimensional
latent representations, i.e. v = fv(xv) ∈Rd and t = ft(xt) ∈Rd. CLIP learns these latent
representations via a typical contrastive learning approach by mapping a positive pair close
together in the embedding space, while that of negative pair samples further away. How-
ever, learning such a joint embedding from scratch is generally challenging due to the lack
of multi-modal datasets and computing resources. Thus, we leverage the pretrained CLIP
model, which optimized a visual-textual joint representation by contrastive learning.
Learning Textual Commonsense Immorality Predictor. Given a feature t = ft(xt) in the
joint embedding space, we further train an immorality classiﬁer fmorality that outputs as a
binary whether the input xt is moral or immoral. Following Hendrycks et al. [19], we use a
MLP for this classiﬁer. To train our classiﬁer, we rely on the ETHICS commonsense morality
dataset [35], which contains a combination of (i) over 6K short scenarios (1-2 sentences)
and (ii) over 7K detailed scenarios (1-8 paragraphs). Note that these short scenarios are from
Amazon Mechanical Turk, while long scenarios are from Reddit followed by multiple ﬁlters.
Given a frozen CLIP-based visual-textual joint encoder and a trained immorality classiﬁer
fmorality, our model is capable of predicting visual commonsense immorality given an unseen
image xv, i.e., ˆy = fmorality(v) = fmorality(fv(xv)).
Loss Function. We use the following Binary Cross-Entropy loss (BCELoss) Lc between
the target yi ∈{0,1} and the classiﬁcation output ˆyi = fmorality(ti) = fmorality(ft(xi
t)) for i ∈
{1,2,...,n}:
Lc = −1
n
n
∑
i=1
[yi logσ(ˆyi)+ (1 −yi)log(1 −σ(ˆyi))]
(1)
where σ represents a sigmoid function.

--- Page 6 ---

6
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
(a) Socio-Moral (SMID)
(b) Sexual Intent
Detection
(c) Real Life 
Violence Situation
(d) Visual Commonsense Immorality (ours)
Figure 3: Examples from different visual immorality datasets: (a) Socio-Moral (SMID) [12],
(b) Sexual Intent Detection [16], (c) Real Life Violence Situation [45], and (d) Visual Com-
monsense Immorality (ours).
4
Visual Immorality Benchmark
To effectively evaluate the ability of our proposed model to predict immorality, a benchmark
consisting of immoral images is generally required. However, as we summarized in Table 1
and Figure 3, existing benchmarks often focus on particular domains (e.g. sexual intent and
violence) and would not be generalized well toward commonsense immorality. Thus, in this
paper, we create a Visual Commonsense Immorality benchmark. We collect 2,172 immoral
images to proceed with more general and extensive immoral image detection. Inspired by
ImageNet-Sketch data [50], all images are collected through Google Image queries and man-
ually ﬁltered by removing the irrelevant images (see examples in the supplemental material).
Air Pollution
Fly-tipping
Garbage Throwing
Land Pollution
Space Junk
Water Pollution
Affair
Bad Parking
Drowsy Driving
Exam Cheating
Fare Evasion
Jaywalking
Manspreading
Middle Finger
Public Urination
School Bullying
School Fight
Secondhand Smoking
Slapping
Smartphone While Driving
Armed Robbery
Burglary
Car Vandalism
Kidnapping
Drunk Driving
# of instances
0
50
100
150
200
250
Sub-categories
Figure 4: Class distribution of our benchmark.
Design Criteria.
In line with
the previous research that deals
with commonsense [19], we deﬁne
the terminology “commonsense im-
morality” as the following: action
that clearly should not have been
done. We apply the following two
criteria to collect and ﬁlter images
based on the deﬁnition. First, all immoral keywords are selected based on commonsense.
Since morality is an area of value judgment, it can vary given the speciﬁcity of culture or sit-
uation. However, it is generally clear that crime or violence is a value to be rejected. Second,
images are intuitive in terms of morality. This is because, unlike text, which can take into
account the context, the greatest difﬁculty of the image is that it is necessary to judge moral-
ity with limited information (i.e., static situation) only. Entire processes are constructed on
human consensus because ethics is the domain of humanity.
Categories. Our benchmark consists of three categories: felony, antisocial behavior, and
environmental pollution.
• Felony is based on title 18 of the United States Code (U.S.C. Title 18), which is the
main criminal code of the federal government of the United States. For example, as
18 U.S.C. §2113. deﬁnes terminology and sentence about a bank robbery and inci-
dental crimes, the keyword “armed robbery” is selected based on this statute. The
most apparent immoral keywords are included in this category, such as “kidnapping”,
“burglary”, and “vandalism”.
• Antisocial behavior contains misdemeanors, social problems, and other unethical ac-
tions. As an example of driving, Driving Under the Inﬂuence (DUI) is a misdemeanor
unless it leads to other accidents. In comparison, whether drowsy driving can be con-
sidered a misdemeanor might be vague and disputable. However, drowsy driving can

--- Page 7 ---

JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
7
also be a latent cause of a tragic accident. Therefore, we classify these antisocial be-
haviors based on its dictionary deﬁnition: harmful to society. Social problems exist
in this category in the same vein. “smartphone while driving”, “exam cheating”, and
“secondhand smoking” are some examples of antisocial behavior.
• Environmental pollution is an another social domain of increasing importance re-
cently. It has been underestimated so far because it is tacit and long-term change
compared to other social problems. However, as sustainable development has become
a principal challenge for the present era, global movements such as carbon emission
regulations continue. It is no exaggeration to say that environmental pollution is one
of the most important issues in the world at this point in time. In this context, we
compose this category with some environmental keywords such as “ﬂy-tipping”, “air
pollution”, and “water pollution”.
5
Experiments
Datasets. We use ETHICS [19] dataset to train our commonsense immorality assessment
classiﬁer. This dataset is based on natural language scenarios, which involves interpersonal
events in an open-world setting (see details in the supplemental material). Note that we
focus on contextualized scenarios with commonsense moral intuitions. To further evaluate
the model’s ability to judge commonsense morality, we use the following eight datasets: (1)
MS-COCO [26], (2) ImageNet [14], (3) Socio-Moral Image [12], (4) Sexual Intent Detec-
tion [16], (5) Real Life Violence Situations [45], (6) NSFW [1], (7) XD-Violence [51], and
(8) our Visual Commonsense Immorality. In detail, MS-COCO [26] and ImageNet [14] are
widely-used image datasets throughout computer vision ﬁeld. Especially, MS-COCO [26]
contains highly-curated images (though contain some images with immoral intents), which
is thus ideal to be used as moral images. Socio-Moral Image Database [12] (SMID) contains
photographic images, representing a wide range of morally positive, negative, and neutral.
Sexual Intent Detection dataset [16] contains celebrity images with sexual and non-sexual
content. In addition, Real Life Violence Situations dataset [45] contains 1,000 violence (e.g.
street ﬁghts) and 1,000 non-violence videos collected from youtube videos. Lastly, similar
to Sexual Intent Detection dataset, NSFW [1] as known as the word for not safe for work
contains neutral, drawing, sexy and porn graphics. Further, validation datasets from Ima-
geNet [14] are also used to examine whether our model may detect images with immoral
intents from large scale dataset for profound discussions. Lastly, we use test video dataset
of XD-Violence [51] to see if our model can classify immoral scenes with high immorality
probability in long sequence video.
Textual Commonsense Immorality Classiﬁcation Performance. Given the joint embed-
ding space, we train an immorality predictor that outputs as a binary whether the input is
moral or immoral. To train such a classiﬁer, we use the ETHICS commonsense morality
dataset [19] as supervision. It is proven that CLIP based on Vision transformer has a supe-
rior performance in downstream tasks than ResNet models. [35], which means text-image
embedding space from the encoders are aligned more closely. Therefore, we conduct an
experiment by using pre-trained CLIP text encoders which are Transformers that have been
jointly trained with CLIP image encoders based on Vision Transformer. (see implementation
details in the supplemental material) In supplemental material, we compare the classiﬁcation
performance on test data with variants of the CLIP-based model and uni-modal NLP-based
baselines [15, 24, 28]. We observe that our model achieves an accuracy of 74.4%–79.2%,

--- Page 8 ---

8
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
Table 1: We report zero-shot visual commonsense immorality classiﬁcation performance
of variants of our model in terms of F-measure. Six image benchmarks are used: MS-
COCO [27], Socio-Moral Image [12], Sexual Intent Detection Images [16], Real Life Vio-
lence Situation [45], NSFW [1], and our Visual Commonsense Immorality. Note that we set
alpha to 0.2 to emphasize on recall.
Dataset
Contents
# of Immoral
Examples
F-measure (α = 0.2)
ViT-B/32 ViT-B/16
ViT-L/14
MS-COCO [27]
(mostly) non-immoral images
-
0.668
0.681
0.632
Socio-Moral Image [12]
photographic images of morally positive, negative, and neutral
962
0.591
0.552
0.511
Sexual Intent Detection Images [16]
sexual and non-sexual
466
0.434
0.724
0.431
Real Life Violence Situation [45]
violence and non-violence
1,000
0.807
0.645
0.743
NSFW [1]
sexy and porn graphics
16,103
0.243
0.837
0.243
Visual Commonsense Immorality (ours) felony, antisocial behavior, environmental pollution
2.172
0.962
0.776
0.720
which is comparable to or lower than uni-modal NLP-based baselines (62.9%–90.4%). This
would be reasonable as CLIP text encoder is trained with simple and short image description
as training input, while others are trained with text data that are more structured and complex.
Further, as ETHICS dataset provides two types of textual scenarios: (i) short (1-2 sentences,
focusing on actions, e.g. “I trashed his essay”) and (ii) long (4-5 paragraphs, focusing on de-
scribing situations). Models with the longer descriptive texts as an input perform better than
those with shorter action-centric texts (see detailed analysis in the supplemental material)
Zero-shot Visual Commonsense Immorality Analysis. Based on the CLIP-based joint
embedding space and the above-mentioned immorality predictor, we further evaluate our
model’s ability to determine visual commonsense immorality from unseen input images.
First, we evaluate our model with ﬁve existing datasets whose contents are similar with sub-
categories of ETHICS dataset, and we provide randomly-chosen examples in supplemental
material. In Table 1, clearly, we can see all CLIP backbones outperforms in predicting im-
moral images in our Visual Commonsense Immorality dataset. This implies that there are
some domain gaps between datasets: Compared to other dataset, our dataset is composed of
images that shows the ﬁrst-person character should not have done that action which is aligned
with ETHICS dataset. In the same vein, our model performs well on predicting violent im-
ages in Real Life Violence Situation [45] dataset, because violent images are action-centric
images compared to other existing dataset images (e.g. nude images in NSFW [1]).
Even though the classiﬁer with ViT-L/14 got much higher accuracy in ETHICS com-
monsense morality dataset, the classiﬁer did not completely surpassed the other backbones
in zero-shot classiﬁcation of image datasets. According to the table 1, we set our ﬁnal model
which used pre-trained CLIP (ViT-B/32) image encoder since it is effective for the zero-shot
prediction. Our analysis by using pre-trained CLIP (ViT-B/32) on our newly created dataset,
which contains more diverse immoral scenarios, further conﬁrms this. As shown in Table 2,
similar to human intuition, images of felony produce higher immorality score (85.8%) than
those of antisocial behavior (80.9%) and environment (76.2%).
Analysis with ImageNet. Further, we apply our model to ImageNet [14] – a large-scale
widely used image classiﬁcation dataset, which is thus required to ensure a generally high
level of morality. As shown in Figure 1, we observe that (i) our model is indeed able to
predict immoral images, which is consistent with human intuitions. (ii) We found that Im-
ageNet dataset contains substantial number of immoral images that can potentially provide
negative social impact without a proper image ﬁltering. Furthermore, as shown in Figure 6,
the immoral images are detected properly regardless of their original classes.

--- Page 9 ---

JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
9
Table 2: We report an average visual commonsense immorality for each category (e.g.
Armed Robbery) of our newly created dataset.
Felony (0.858)
Antisocial Behavior (0.809)
Environment (0.762)
Armed Robbery
0.895
Drowsy Driving
0.865
Manspreading
0.837
Smartphone while Driving
0.763
Fly-tipping
0.835
Burglary
0.865
Slapping
0.862
Fare Evasion
0.826
Jaywalking
0.760
Garbage Throwing
0.834
Kidnapping
0.862
School Fight
0.856
Bad Parking
0.786
Public Urination
0.743
Land Pollution
0.805
Car Vandalism
0.811
Secondhand Smoking
0.844
Exam Cheating
0.784
Air Pollution
0.762
Drunk Driving
0.842
Affair
0.766
Water Pollution
0.792
School Bullying
0.839
Middle Finger
0.766
Space Junk
0.545
Plastic Bag
Classified as
Immoral
Classified as
Moral
Hammer
Whiskey J ug
Syringe
Notebook
Seat Belt
Mountain Bike
Banana
Book J acket
Figure 6: Examples of the same class but differently classiﬁed by our model. E.g., our model
classiﬁes an image of a hammer as moral, but a person striking with it as immoral.
Figure 5: Performance compar-
ison with baseline.
Zero-shot Visual Supervision Baseline. Figure 5 shows
a performance comparison with ResNet50 model that is
trained with Sexual Intent Detection Images dataset and
tested (in a zero-shot manner) with SMID (random pho-
tographic images), NSFW (sexy and porn graphics), Real
Life Violence Situation, and our Viusal Commonsense Im-
morality. We observe that such classiﬁer trained on a spe-
ciﬁc category of commonsense immorality often results
in overﬁtting and does not generalize well. In Real Life
Violence Situation and Visual Commonsense Immorality
dataset, there are large domain gaps between Sexual Intent Detection compared to SMID
and NSFW. This leads to the poor performance of ResNet50 and results in the dramatic
accuracy gap with our model in our Visual Commonsense Immorality dataset.
Not at all
MS-COCO (non-immoral)
Immoral ImageNet Examples
by Schramowski et al.
Immoral ImageNet Examples
by Ours
Visual Immorality
Benchmark
Slightly
Moderately
“How immoral is the image below?”
Very Much
Extremely
Figure 7: Box plots from our human evaluations.
Human
Evaluations.
Since
ethics is humanity’s domain, align-
ing the model’s behavior with hu-
man intuition is essential. There-
fore, we conduct a human evalu-
ation to quantify the effectiveness
of our model.
We use Amazon
Mechanical Turk (AMT) to secure
diverse cultural backgrounds in our human study. Overall, 172 respondents (from more
than six different ethnic groups) were recruited and asked to evaluate the immorality of the
given 100 images on the 5-point Likert Scale. Those images were randomly sampled from
four different sources: (a) Visual Commonsense Immorality Benchmark, Immoral ImageNet
examples found by (b) our model, and (c) existing work by Schramowski et al., and (d)
MS-COCO validation dataset [26]. Note that we set a threshold to 0.9 for all experiments.
In Figure 7, we visualize box plots for each image sources. We observe that participants
answered that images from our created benchmark are immoral (median score was 4.10),
while images from MS-COCO (mostly moral) received 1.91. This may conﬁrm the validity
of our created dataset for the visual commonsense immorality classiﬁcation task. Further,

--- Page 10 ---

10
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
1.0
(a)
(c)
(b)
0.0
1
3
5
7
9
11
13
15
0.2
0.4
0.6
0.8
Immorality
1.0
0.0
0.2
0.4
0.6
0.8
Immorality
1.0
0.0
0.2
0.4
0.6
0.8
Immorality
Index of Frames
1
11
21
31
41
51
61
71
Index of Frames
1
6
11
16
21
Index of Frames
0
0
2
4
6
8
0
0
2
4
6
8
Figure 8: We visualize examples (e.g. (a) using a gun, (b) drinking or a person passed
out, and (c) ﬁghting) of the predicted level of visual commonsense immorality on XD-
violence [51] video frames. Corresponding video frames are provided on top of each plot.
Note that we apply a Savitzky-Golay smoothing ﬁlter (with the window size set to 5).
our study shows that our model can detect visual immorality better than existing work by
Schramowski et al. [42] (3.14 vs. 2.82 in the median, compare 2nd and 3rd box-plots). This
conﬁrms that leveraging textual information as supervision with a text-image embedding
space has better generalization compared to optimizing the model with small image dataset.
Analysis with Video. We conduct an experiment to test if our model truly capture the
immoral scenes in the video. Therefore, we use violent dataset of XD-Violence [51] which
have various violent scenes in long sequences. In randomly chosen videos, we extract a
frame uniformly every second. Figure 8 represents that our model correctly predict the
immoral scenes with higher probabilities compared to other non-immoral scenes. It leads us
to the next experiment of classifying the short video clips. We classify to violent video if the
average probability of all frames is higher than 0.7. We achieve 72.7% accuracy and 75.7%
F-measure (α=0.2) in Real Life Violence Situation dataset [45], which means our model is
reasonably able to determine visual immorality in short videos.
6
Conclusion
Predicting immorality from images is of paramount importance regarding social safety. In
this work, we ﬁrst utilized CLIP-based text-image joint embedding space and trained a (text-
based) commonsense immorality classiﬁer. Given these, we then predicted visual common-
sense immorality from an unseen image in a zero-shot manner. Using seven benchmarks in
image classiﬁcation, we demonstrated that our model successfully estimates visual common-
sense immorality. Our analysis with the XD-Violence dataset also showed consistency in its
prediction. In fact, we observed that widely-used image classiﬁcation benchmarks, such
as ImageNet, contain immoral visual scenes, potentially negatively impacting the trained
model’s behavior. Further, we created a new Visual Commonsense Immorality benchmark, a
more general image benchmark toward commonsense immorality. We hope our paper could
be an initial point in discussing the importance of visual commonsense immorality towards
ethical AI.
Acknowledgements. This work was supported by Institute of Information & communica-
tions Technology Planning & Evaluation (2022-0-00043,Adaptive Personality for Intelligent
Agents) and ICT Creative Consilience program (IITP-2022-2022-0-01819).

--- Page 11 ---

JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
11
References
[1] https://github.com/alex000kim/nsfw_data_scraper.
[2] Shervin Ardeshir, Cristina Segalin, and Nathan Kallus. Estimating structural disparities
for face models. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 10358–10367, 2022.
[3] Isaac Asimov. Three laws of robotics. Asimov, I. Runaround, 1941.
[4] Edmond Awad, Sohan Dsouza, Richard Kim, Jonathan Schulz, Joseph Henrich, Azim
Shariff, Jean-François Bonnefon, and Iyad Rahwan. The moral machine experiment.
Nature, 563(7729):59–64, 2018.
[5] Enrique Bermejo Nievas, Oscar Deniz Suarez, Gloria Bueno García, and Rahul Suk-
thankar. Violence detection in video using computer vision techniques. In International
conference on Computer analysis of images and patterns, pages 332–339. Springer,
2011.
[6] Muhammad Tahir Bhatti, Muhammad Gufran Khan, Masood Aslam, and Muham-
mad Junaid Fiaz. Weapon detection in real-time cctv videos using deep learning. IEEE
Access, 9:34366–34382, 2021.
[7] Daniel Bicho, Artur J Ferreira, and Nuno Datia. A deep learning approach to identify
not suitable for work images. i-ETC: ISEL Academic Journal of Electronics, Telecom-
munications and Computers, 6(1):1–11, 2020.
[8] Nick Bostrom. Ethical issues in advanced artiﬁcial intelligence. Science ﬁction and
philosophy: from time travel to superintelligence, 277:284, 2003.
[9] Nick Bostrom. The superintelligent will: Motivation and instrumental rationality in
advanced artiﬁcial agents. Minds and Machines, 22(2):71–85, 2012.
[10] Liang-Hua Chen, Hsi-Wen Hsu, Li-Yun Wang, and Chih-Wen Su. Violence detection
in movies. In 2011 Eighth International Conference Computer Graphics, Imaging and
Visualization, pages 119–124. IEEE, 2011.
[11] Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario
Amodei. Deep reinforcement learning from human preferences. Advances in neural
information processing systems, 30, 2017.
[12] Damien L. Crone, Stefan Bode, Carsten Murawski, and Simon M. Laham. The socio-
moral image database (smid): A novel stimulus set for the study of social, moral and af-
fective processes. PLOS ONE, 13:1–34, 01 2018. doi: 10.1371/journal.pone.0190954.
URL https://doi.org/10.1371/journal.pone.0190954.
[13] Claire-Hélène Demarty, Cédric Penet, Mohammad Soleymani, and Guillaume Gravier.
Vsd, a public dataset for the detection of violent scenes in movies: design, annotation,
analysis and evaluation. Multimedia Tools and Applications, 74(17):7379–7404, 2015.
[14] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A
large-scale hierarchical image database. In 2009 IEEE conference on computer vision
and pattern recognition, pages 248–255. Ieee, 2009.

--- Page 12 ---

12
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
[15] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-
training of deep bidirectional transformers for language understanding. In Proceedings
of the 2019 Conference of the North American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota, June 2019. Association for Computational
Linguistics. doi: 10.18653/v1/N19-1423. URL https://aclanthology.org/
N19-1423.
[16] Debashis Ganguly, Mohammad H Mofrad, and Adriana Kovashka. Detecting sexually
provocative images. In WACV, pages 660–668. IEEE, 2017.
[17] Jose L Salazar González, Carlos Zaccaro, Juan A Álvarez-García, Luis M Soria Mo-
rillo, and Fernando Sancho Caparrini. Real-time gun detection in cctv: An open prob-
lem. Neural networks, 132:297–308, 2020.
[18] Ismael Serrano Gracia, Oscar Deniz Suarez, Gloria Bueno Garcia, and Tae-Kyun Kim.
Fast ﬁght detection. PloS one, 10(4), 2015.
[19] Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song,
and Jacob Steinhardt. Aligning ai with shared human values. ICLR, 2021.
[20] Chao Jia, Yinfei Yang, Ye Xia, Yi-Ting Chen, Zarana Parekh, Hieu Pham, Quoc Le,
Yun-Hsuan Sung, Zhen Li, and Tom Duerig. Scaling up visual and vision-language
representation learning with noisy text supervision. In International Conference on
Machine Learning, pages 4904–4916. PMLR, 2021.
[21] Rishemjit Kaur and Kazutoshi Sasahara. Quantifying moral foundations from various
topics on twitter conversations. In 2016 IEEE International Conference on Big Data
(Big Data), pages 2505–2512. IEEE, 2016.
[22] Jon Kleinberg, Sendhil Mullainathan, and Manish Raghavan. Inherent trade-offs in the
fair determination of risk scores. arXiv preprint arXiv:1609.05807, 2016.
[23] Yehuda Koren. Factorization meets the neighborhood: a multifaceted collaborative
ﬁltering model. In Proceedings of the 14th ACM SIGKDD international conference on
Knowledge discovery and data mining, pages 426–434, 2008.
[24] Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma,
and Radu Soricut.
Albert:
A lite bert for self-supervised learning of language
representations.
In ICLR, 2020.
URL https://openreview.net/forum?
id=H1eA7AEtvS.
[25] Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. Blip: Bootstrapping language-
image pre-training for uniﬁed vision-language understanding and generation. arXiv
preprint arXiv:2201.12086, 2022.
[26] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ra-
manan, Piotr Dollár, and C Lawrence Zitnick. Microsoft coco: Common objects in
context. In European conference on computer vision, pages 740–755. Springer, 2014.
[27] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ra-
manan, Piotr Dollár, and C Lawrence Zitnick. Microsoft coco: Common objects in
context. In European conference on computer vision, pages 740–755. Springer, 2014.

--- Page 13 ---

JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
13
[28] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer
Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly
optimized bert pretraining approach. arXiv preprint arXiv:1907.11692, 2019.
[29] James H Moor. The nature, importance, and difﬁculty of machine ethics. IEEE intelli-
gent systems, 21(4):18–21, 2006.
[30] Hamdy Mubarak, Ammar Rashed, Kareem Darwish, Younes Samih, and Ahmed Ab-
delali. Arabic offensive language on twitter: Analysis and experiments. arXiv preprint
arXiv:2004.02192, 2020.
[31] Sanam Narejo, Bishwajeet Pandey, Ciro Rodriguez, M Rizwan Anjum, et al. Weapon
detection using yolo v3 for smart surveillance system. Mathematical Problems in En-
gineering, 2021, 2021.
[32] Sungho Park, Jewook Lee, Pilhyeon Lee, Sunhee Hwang, Dohyung Kim, and Hyeran
Byun. Fair contrastive learning for facial attribute classiﬁcation. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 10389–
10398, 2022.
[33] Mauricio Perez, Alex C Kot, and Anderson Rocha. Detection of real-world ﬁghts in
surveillance videos. In ICASSP 2019-2019 IEEE International Conference on Acous-
tics, Speech and Signal Processing (ICASSP), pages 2662–2666. IEEE, 2019.
[34] Zeses Pitenis, Marcos Zampieri, and Tharindu Ranasinghe. Offensive language identi-
ﬁcation in greek. arXiv preprint arXiv:2003.07459, 2020.
[35] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini
Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning
transferable visual models from natural language supervision. In International Confer-
ence on Machine Learning, pages 8748–8763. PMLR, 2021.
[36] Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford,
Mark Chen, and Ilya Sutskever. Zero-shot text-to-image generation. In International
Conference on Machine Learning, pages 8821–8831. PMLR, 2021.
[37] Hannah Rashkin, Eric Michael Smith, Margaret Li, and Y-Lan Boureau.
Towards
empathetic open-domain conversation models: A new benchmark and dataset. arXiv
preprint arXiv:1811.00207, 2018.
[38] Alex Ray, Joshua Achiam, and Dario Amodei. Benchmarking safe exploration in deep
reinforcement learning. arXiv preprint arXiv:1910.01708, 7:1, 2019.
[39] Stephen Roller, Emily Dinan, Naman Goyal, Da Ju, Mary Williamson, Yinhan Liu, Jing
Xu, Myle Ott, Kurt Shuster, Eric M Smith, et al. Recipes for building an open-domain
chatbot. arXiv preprint arXiv:2004.13637, 2020.
[40] Sara Rosenthal, Pepa Atanasova, Georgi Karadzhov, Marcos Zampieri, and Preslav
Nakov. Solid: A large-scale semi-supervised dataset for offensive language identiﬁca-
tion. arXiv preprint arXiv:2004.14454, 2020.
[41] Michael J Sandel. Justice: What’s the right thing to do. BUL Rev., 91:1303, 2011.

--- Page 14 ---

14
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
[42] Patrick Schramowski and Kristian Kersting. Inferring offensiveness in images from
natural language supervision. arXiv preprint arXiv:2110.04222, 2021.
[43] Amanpreet Singh, Ronghang Hu, Vedanuj Goswami, Guillaume Couairon, Wojciech
Galuba, Marcus Rohrbach, and Douwe Kiela. Flava: A foundational language and
vision alignment model. arXiv preprint arXiv:2112.04482, 2021.
[44] Kirill Sirotkin, Pablo Carballeira, and Marcos Escudero-Viñolo. A study on the dis-
tribution of social biases in self-supervised learning visual models. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 10442–
10451, 2022.
[45] Mohamed Mostafa Soliman, Mohamed Hussein Kamal, Mina Abd El-Massih Nashed,
Youssef Mohamed Mostafa, Bassel Safwat Chawky, and Dina Khattab. Violence recog-
nition from videos using deep learning techniques. In 2019 Ninth International Confer-
ence on Intelligent Computing and Information Systems (ICICIS), pages 80–85. IEEE,
2019.
[46] Swathikiran Sudhakaran and Oswald Lanz. Learning to detect violent videos using
convolutional long short-term memory. In 2017 14th IEEE International Conference
on Advanced Video and Signal Based Surveillance (AVSS), pages 1–6. IEEE, 2017.
[47] Waqas Sultani, Chen Chen, and Mubarak Shah.
Real-world anomaly detection in
surveillance videos. In Proceedings of the IEEE conference on computer vision and
pattern recognition, pages 6479–6488, 2018.
[48] Alan M Turing and J Haugeland. Computing machinery and intelligence. The Turing
Test: Verbal Behavior as the Hallmark of Intelligence, pages 29–56, 1950.
[49] Fath U Min Ullah, Amin Ullah, Khan Muhammad, Ijaz Ul Haq, and Sung Wook Baik.
Violence detection using spatiotemporal features with 3d convolutional neural network.
Sensors, 19(11):2472, 2019.
[50] Haohan Wang, Songwei Ge, Zachary Lipton, and Eric P Xing. Learning robust global
representations by penalizing local predictive power. Advances in Neural Information
Processing Systems, 32, 2019.
[51] Peng Wu, Jing Liu, Yujia Shi, Yujia Sun, Fangtao Shao, Zhaoyang Wu, and Zhiwei
Yang. Not only look, but also listen: Learning multimodal violence detection un-
der weak supervision. In European conference on computer vision, pages 322–339.
Springer, 2020.
[52] Jiahui Yu, Zirui Wang, Vijay Vasudevan, Legg Yeung, Mojtaba Seyedhosseini, and
Yonghui Wu. Coca: Contrastive captioners are image-text foundation models. arXiv
preprint arXiv:2205.01917, 2022.
[53] Dmirty Zhelonkin and Nikolay Karpov. Training effective model for real-time detection
of nsfw photos and drawings.
In International Conference on Analysis of Images,
Social Networks and Texts, pages 301–312. Springer, 2019.

--- Page 15 ---

arXiv:2211.05521v1  [cs.CV]  10 Nov 2022
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
1
Supplementary Material:
Zero-shot Visual Commonsense
Immorality Prediction
Yujin Jeong1
eugene6923@korea.ac.kr
Seongbeom Park1
psb485@korea.ac.kr
Suhong Moon2
suhong.moon@berkeley.edu
Jinkyu Kim1
jinkyukim@korea.ac.kr
1 Computer Science and Engineering
Korea University
Seoul 02841, Korea
2 Electrical Engineering and Computer
Sciences
University of California, Berkeley
CA 94720, USA
A
Implementation Details
Training Details. We implement our Commonsense Immorality predictor upon architecture
by Hendrycks et al. [6]. We use an MLP for this classiﬁer, which consists of Dropout-Linear-
Tanh-Dropout-Projection layers. Our model is trained end-to-end using AdamW [9] as an
optimizer with the learning rate shown in Table 1. The whole model is trained for 100 epochs
on 4 NVIDIA GeForce RTX 3090 GPUs, distributing inputs evenly per GPU. We utilize
the ETHICS commonsense morality dataset to train such a model. Other hyperparameters
(e.g., learning rate, batch size, epochs, weight decaying parameter, AdamW epsilon, and a
parameter for dropout layers) used to train our models are summarized in Table 1.
CLIP Backbone Input size
Learning rate Batch size Epochs Weight decay AdamW epsilon
Dropout
ViT-B/32
512
0.002
64
100
0.01
1e-8
0.5
ViT-B/16
512
0.002
64
100
0.01
1e-10
0.5
ViT-L/14
768
0.001
64
100
0.01
1e-8
0.5
Table 1: Details of Hyperparameters for training our morality classiﬁer.
Video Preprocessing. Real Life Violence Situations dataset [10] contains 2000 violence
and non-violence videos collected from YouTube. Each clip is approximately 5-seconds
long, and we extract a single 75-percentile frame from sorted video frames, where the most
important scenes are commonly observed.
Labeling Moral vs. Immoral Images. Socio-Moral Image dataset [3] provides an average
moral rate voted by multiple human judges, and we convert it into moral (1 for images where
© 2022. The copyright of this document resides with its authors.
It may be distributed unchanged freely in print or electronic forms.

--- Page 16 ---

2
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
the moral rate is above 2.4) and immoral (0 for images where the moral rate is below 2.4).
Sexual Intent Detection dataset [5] provides three label types: (i) sexually provocative im-
ages, (ii) images with implicit or hidden sexual intents, and (iii) images without any explicit
sexual intentions. In our experiment, we only use (i) as immoral images. Similarly, we use
sexual and porn images as immoral for the NSFW [1] dataset, whereas drawings and neutral
images are moral.
B
Dataset Details
Additional Examples of Existing Datasets. In Figure 1, we provide additional examples of
four different datasets: Socio-Moral Image dataset (SMID, [3]), Sexual Intent Detection [5],
Real Life Violence Situations [10], and NSFW [1].
Figure 1: Examples randomly sampled from four different datasets: Socio-Moral Image
dataset (SMID, [3]), Sexual Intent Detection [5], Real Life Violence Situations [10], and
NSFW [1]. Some images are blurred as they contain highly immoral (or sexually provoca-
tive) content.
Examples of ETHICS Commonsense Morality Dataset. ETHICS Commonsense Morality
Dataset, which we used to train our model, provides two types of text prompt: (1) long and
(2) short sentences. In Table 2, we provide statistics of the ETHICS dataset. Further, we
provide examples of such texts in Figure 2.

--- Page 17 ---

JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
3
Number of Examples
Avg. Length
(in words)
Train
Test
Test (Hard)
Total
13,910 3,885
3,964
224
Long sentences
7,249
1,776
2,260
417
Short sentences
6,661
2,109
1,704
15.9
Table 2: Number of examples in terms of data splits. As the ETHICS dataset provides two
types of text prompts (long and short sentences), we also provide statistics for both cases.

--- Page 18 ---

4
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
Figure 2: Examples of moral and immoral scenarios from the ETHICS commonsense moral-
ity dataset.

--- Page 19 ---

JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
5
Additional Examples of our Visual Commonsense Immorality. In Figure 3, we provide
additional random examples of our Visual Commonsense Immorality dataset along with dif-
ferent query keywords.
Figure 3: All keywords and corresponding (randomly sampled) images from our Visual
Commonsense Immorality Dataset.

--- Page 20 ---

6
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
C
Additional Experiments
Textual Commonsense Immorality Classiﬁcation Performance. In Table 3, we provide
scores of textual commonsense immorality classiﬁcation for a variant of our model with
different NLP models and different CLIP backbones.
NLP Model
Test Acc. (%) Test (Hard) Acc. (%) AUC (%)
Word Averaging
62.9
44.0
-
GPT-3 (few-shot) [2]
73.3
66.0
-
BERT-base [4]
86.5
48.7
-
BERT-large [4]
88.5
51.1
58.0
RoBERTa-large [8]
90.4
63.4
69.0
ALBERT-xxlarge [7]
85.1
59.0
56.0
CLIP Backbone
Test Acc. (%) Test (Hard) Acc. (%)
AUC
ViT-B/32
74.4
49.2
54.4
ViT-B/16
75.0
47.4
53.5
ViT-L/14
79.2
49.7
59.2
Table 3: Textual commonsense immorality prediction accuracy (in %) for variants of CLIP-
based backbones and uni-modal NLP-based models.
Details of Human Study. In Figure, we provide a pie chart to show the diversity of partici-
pants in our human study. Overall, 170 participants with different ethical backgrounds were
recruited through Amazon Mechanical Turk.
Figure 4: We ask an additional question “which of the following best describes you?” to see
the ethical diversity of participants in our human study.
Effect of Text Input Length. The CLIP-based text encoder was pre-trained with external
data, with texts of length 77 in max. This can pose a potential issue if text inputs have
more than 77 words. To see its effect, we further experiment with datasets of different
lengths (short vs. long). As shown in Table 4, we observe a degradation when we train
only with short sentences from the ETHICS dataset (compare 1st and 2nd rows), which
might be due to these short sentences often conveying a short description of actions (e.g.,
“I trashed his essay”). In contrast, long sentences (that were collected from Reddit) provide
better contextual cues to judge immorality (compare short vs. long sentences in Figure 2).

--- Page 21 ---

JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
7
Additionally, we experiment with long sentences as input but reverted to see the effect of
cutting sentences by 77 words for a CLIP-based text encoder. As shown in Table 4 (compare
2nd vs. 3rd rows), we observe a slight degradation, which indicates that the beginning of
sentences conveys better contexts to determine immorality.
Input
Test Acc. (%) Test (Hard) Acc. (%) AUC (%)
Short sentences
70.5
57.1
49.5
Long sentences
79.4
42.1
57.5
Long sentences (reverted)
73.8
41.9
55.3
Table 4: Textual commonsense immorality prediction accuracy (in %) with different subsets
of input texts.
References
[1] https://github.com/alex000kim/nsfw_data_scraper.
[2] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sand-
hini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark
Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christo-
pher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. In
H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin, editors, NeurIPS,
volume 33, pages 1877–1901, 2020.
[3] Damien L. Crone, Stefan Bode, Carsten Murawski, and Simon M. Laham. The socio-
moral image database (smid): A novel stimulus set for the study of social, moral and af-
fective processes. PLOS ONE, 13:1–34, 01 2018. doi: 10.1371/journal.pone.0190954.
URL https://doi.org/10.1371/journal.pone.0190954.
[4] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-
training of deep bidirectional transformers for language understanding. In Proceedings
of the 2019 Conference of the North American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota, June 2019. Association for Computational
Linguistics. doi: 10.18653/v1/N19-1423. URL https://aclanthology.org/
N19-1423.
[5] Debashis Ganguly, Mohammad H Mofrad, and Adriana Kovashka. Detecting sexually
provocative images. In WACV, pages 660–668. IEEE, 2017.
[6] Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song,
and Jacob Steinhardt. Aligning ai with shared human values. ICLR, 2021.
[7] Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma,
and Radu Soricut.
Albert:
A lite bert for self-supervised learning of language
representations.
In ICLR, 2020.
URL https://openreview.net/forum?
id=H1eA7AEtvS.

--- Page 22 ---

8
JEONG ET AL.: ZERO-SHOT VISUAL COMMONSENSE IMMORALITY
[8] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer
Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly
optimized bert pretraining approach. arXiv preprint arXiv:1907.11692, 2019.
[9] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. ICLR, 2019.
[10] Mohamed Mostafa Soliman, Mohamed Hussein Kamal, Mina Abd El-Massih Nashed,
Youssef Mohamed Mostafa, Bassel Safwat Chawky, and Dina Khattab. Violence recog-
nition from videos using deep learning techniques. In 2019 Ninth International Confer-
ence on Intelligent Computing and Information Systems (ICICIS), pages 80–85. IEEE,
2019.

```
