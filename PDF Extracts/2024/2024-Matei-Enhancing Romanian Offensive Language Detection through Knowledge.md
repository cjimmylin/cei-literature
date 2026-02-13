---
title: "2024-Matei-Enhancing Romanian Offensive Language Detection through Knowledge - PDF Extract"
source_pdf: "2024-Matei-Enhancing Romanian Offensive Language Detection through Knowledge.pdf"
pages: 15
extracted_at: "2026-02-13T13:13:46.702265"
---

# PDF Extract: 2024-Matei-Enhancing Romanian Offensive Language Detection through Knowledge

**Source PDF:** 2024-Matei-Enhancing Romanian Offensive Language Detection through Knowledge.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

Enhancing Romanian Offensive Language
Detection through Knowledge Distillation,
Multi-Task Learning, and Data Augmentation
Vlad-Cristian Matei, Iulian-Marius T˘aiatu, R˘azvan-Alexandru Sm˘adu, and
Dumitru-Clementin Cercel*
Faculty of Automatic Control and Computers, National University of Science and
Technology POLITEHNICA Bucharest, Romania
Abstract. This paper highlights the significance of natural language
processing (NLP) within artificial intelligence, underscoring its pivotal
role in comprehending and modeling human language. Recent advance-
ments in NLP, particularly in conversational bots, have garnered sub-
stantial attention and adoption among developers. This paper explores
advanced methodologies for attaining smaller and more efficient NLP
models. Specifically, we employ three key approaches: (1) training a
Transformer-based neural network to detect offensive language, (2) em-
ploying data augmentation and knowledge distillation techniques to in-
crease performance, and (3) incorporating multi-task learning with knowl-
edge distillation and teacher annealing using diverse datasets to enhance
efficiency. The culmination of these methods has yielded demonstrably
improved outcomes.
Keywords: Offensive Language · Knowledge Distillation · Multi-Task
Learning · Data Augmentation
1
Introduction
In recent years, there has been a remarkable rise in the prominence of natural
language processing, primarily attributable to the success of conversational bots
like ChatGPT1. These models have achieved impressive performance through
extensive training on massive datasets. However, the battle against fake news,
offensive language, and abusive content on social networks remains challenging
due to the overwhelming volume of user-generated data, necessitating the de-
velopment of automatic detection systems [9]. Moreover, the intricate nature of
identifying offensive language stems from the nuanced considerations of contex-
tual factors, multiple meanings, and emerging expressions [11]. Further advance-
ments in this field are still required to tackle these challenges effectively.
Exploiting offensive language has garnered significant global attention, with
trained models demonstrating notable performance achievements [30]. However,
* Corresponding author: dumitru.cercel@upb.ro.
1 https://www.openai.com/chatgpt
arXiv:2409.20498v1  [cs.CL]  30 Sep 2024

--- Page 2 ---

2
V.-C. Matei et al.
when considering the specific context of the Romanian language analysis, the
existing datasets are constrained in size and availability [8]. To understand cru-
cial and intricate characteristics comprehensively, models require a diverse and
well-balanced collection of qualitative examples. Additionally, the architectures
underlying these models comprise millions of parameters, resulting in substantial
computational and resource requirements [3]. Consequently, although automatic
detection of offensive language remains relevant, challenges arise in adapting
these models for mobile devices or embedded systems due to limitations in speed,
space, and resource constraints [1].
The primary objective of this study is to develop an automatic offensive
language detection model encompassing three distinct offensive categories (i.e.,
Insult, Profanity, and Abuse) and a neutral class Other. Initially, we employ
the knowledge distillation (KD) method [13] to transfer information [26] from
a high-parameter model to a more compact architecture [3]. Subsequently, the
obtained results undergo meticulous analysis, complemented by an exploration of
various data augmentation strategies: generative text [28] by employing RoGPT-
2 [25], ASDA [19], MixUp [38], and noisy student [22]. These techniques enhance
the model’s performance by introducing nuanced variations or controlled noise
injection.
In addition, this study prioritizes performance optimization rather than model
size reduction. Accordingly, knowledge distillation is employed on an architec-
ture with an equivalent number of parameters [1]. Furthermore, a multi-task
learning (MTL) approach [4,21,15] integrates information from three auxiliary
tasks associated with sentiment analysis [31], emotions analysis [6], and sexist
language [14]. We comprehensively evaluate the effectiveness of this architecture
in efficiently assimilating and integrating the acquired information. Furthermore,
our study assesses how these auxiliary datasets contribute to a more comprehen-
sive understanding of the Romanian language, particularly in the context of the
initial problem. To summarize, the contributions of this work are: (i) evaluating
the knowledge distillation method to obtain a more compact and faster model
and showing that utilizing diverse data augmentation techniques improves per-
formance, and (ii) performance enhancement by applying multi-task learning
with knowledge distillation and teacher annealing [16], integrating information
from three additional datasets.
2
Related Work
Automatic offensive language detection poses a challenge of global interest [9,11],
with attempts to address the issue using various means, both classic machine
learning methods and deep learning approaches [37]. Offensive language de-
tection was proposed at several workshops, including SemEval-2019 [37] and
GermEval-2019 [30]. Baseline models such as support vector machines have been
evaluated on offensive and sexist tweets [14]. In addition, [5] explored neural
network approaches such as long short-term memory and convolutional neural

--- Page 3 ---

Enhancing Romanian Offensive Language Detection
3
networks on hate speech, showing there is room for improvement in these sys-
tems.
To optimize recent models, transfer learning techniques [26] have been pro-
posed, including multi-task learning [4,21] and knowledge distillation [13,3], with
applications extending to the domain of offensive language [32]. AngryBERT
[2] combined MTL with the Bidirectional Encoder Representations from Trans-
former (BERT) model [17] to jointly learn hate speech detection along with emo-
tion classification and target identification as secondary tasks, enhancing overall
performance. In [33], the authors investigate bridging differences in annotation
and data collection of hate speech and abusive language in tweets, including
various annotation schemes, labels, and geographic and cultural influences. To
harness the benefits of both methods, models combining multi-task learning with
knowledge distillation [18,7,27,20] or teacher annealing have been proposed [16].
This framework was also employed alongside the teacher annealing option, al-
beit for empathy detection [15]. In contrast to other works, we combine all these
methods to address the automatic detection of offensive language, particularly in
the Romanian language, and compare them individually and through an ablation
study.
3
Method
3.1
Fine-tuning BERT
In this work, we base our models on the BERT architecture [17]. The baseline
involves fine-tuning BERT for automatic offensive language detection. It adjusts
the weights obtained from a pre-trained BERT to identify and classify different
subtypes of offensive language accurately.
The initial step establishes a manually annotated dataset D =

(xi, yi)
	
i=1:N
with N examples, namely RO-Offense2, that assigns labels yi (i.e., Insult, Abuse,
Profanity, and Other) to each text comment xi. These labels enable a more nu-
anced understanding of the offensive language, moving beyond a simplistic bi-
nary classification. To accommodate the classification task with K = 4 possible
classes, we add a fully connected layer on top of the last layer of BERT’s ar-
chitecture. This fully connected layer consists of K neurons, each corresponding
to one of the predicted classes. Then, a softmax layer computes the probability
distribution pi over predicted classes for the given input text xi.
During the training process, the weights are updated to minimize the predic-
tion error by employing the cross-entropy loss function LCE. This loss quantifies
the dissimilarities between the predicted and true labels as follows:
LCE = −1
N
N
X
i=1
K
X
k=1
yi,k log (pi,k)
(1)
where yi,k is the kth class label from the one-hot encoding for the ground truth
yi, and pi,k is the kth class probability from the model’s softmax output pi.
2 https://huggingface.co/datasets/readerbench/ro-offense

--- Page 4 ---

4
V.-C. Matei et al.
3.2
Data Augmentation
Data augmentation is a technique employed to enrich the diversity of features
in the dataset without the need for additional data collection [10]. Its objec-
tive is to introduce changes in input data to enhance the models’ capacity for
generalization. This approach offers several benefits, including improved model
performance, acting as a regularization technique, enhancing model robustness,
and addressing class imbalance [12,19,10]. Our work employs several data aug-
mentation techniques.
RoGPT-2. Generative Pre-trained Transformer (GPT) models [28] leverage
the linguistic knowledge and comprehensive understanding of language struc-
tures to produce varied texts that encompass the intricacies and diversity ob-
served in real-world texts. While existing methods like Easy Data Augmentation
[34] focus on simple transformations applied to the existing text, GPT models
offer the advantage of generating creative and meaningful texts, enhancing the
model’s robustness through variety. However, the generated texts may signifi-
cantly alter the original meaning. To mitigate this risk, we employ the RoGPT-2
[25] model. RoGPT-2 is the Romanian version of the GPT-2 model [29], pre-
trained on a large 17 GB Romanian text dataset. We provide 70% of the context
to control the level of text augmentation, allowing the model to generate a sequel
and encouraging controlled and coherent text generation.
ASDA. Auxiliary Sentence-based Data Augmentation (ASDA) [19] utilizes
conditional masked language modeling [35] to generate augmented examples.
First, it works by selecting an example E1 from the training dataset and then
choosing another example E2 with the same class [LABEL] as E1. Next, we con-
struct the context using the following template: “The next two sentences are
[LABEL]. The first sentence is: E1. The second sentence is: E2.”. We
apply random masking of a set of words within the final sentence, E2. The mask-
ing process occurs with a predefined probability and depends on the sentence
length.
MixUp. MixUp [38] is a data augmentation method intended to boost diver-
sity while lowering the possibility of generating incorrect examples. It creates a
more robust generalization by linearly interpolating between various dataset ex-
amples. The technique randomly selects two examples (i.e., (xi, yi) and (xj, yj))
from the dataset, where xi and xj represent the encoded inputs, whereas yi and
yj are the one-hot encoded labels. New examples (ˆx, ˆy) are generated using the
following formulas:
ˆx = λxi + (1 −λ)xj,
(2)
ˆy = λyi + (1 −λ)yj,
(3)
where λ ∈[0, 1] is a hyperparameter that controls the interpolation process. In
this work, we employ the MixUp technique at two distinct levels3 [12]:
3 https://github.com/xashru/mixup-text

--- Page 5 ---

Enhancing Romanian Offensive Language Detection
5
– MixUp Encoder: Interpolates the representations of the two input exam-
ples before passing them through the classification layer.
– MixUp Sentence: Interpolates the representations of the two inputs after
the classification layer but before the softmax activation function.
Noisy Student. Noisy student [22] is employed in noisy student training
[36], where a teacher model generates pseudo-labels for unlabeled data, and a
student model is trained on these pseudo-labels. The objective is to introduce
natural noise and enhance the robustness of the model. In this research, we apply
two non-aggressive methods [22]:
– Word Drop: We choose, with a probability α, that every word in a sentence
has a fixed chance of 30% to be removed. It is guaranteed that at least one
word will be deleted, but no more than ten words in total.
– Sentence Drop: In cases where the example contains at least two sentences,
we remove one sentence from the text with the same probability α.
3.3
Multi-Task Learning Model
MTL [21,4] is a method that learns several related tasks simultaneously within a
single framework to enhance target task performance. The fundamental concept
behind MTL is based on the observation that learning similar tasks in parallel
can facilitate quicker adaptation, leveraging common principle knowledge [4].
Building upon this intuition, MTL learns shared representations that encap-
sulate the underlying essence of the information while capturing the specific
characteristics of each task up to a level beneficial for the main task [21]. This
approach can be viewed as a subcategory of TL, as both leverage the knowl-
edge from related tasks [26]. However, MTL offers several advantages, including
leveraging information learned from different tasks and transferring knowledge
across diverse datasets [21]. It also helps mitigate overfitting by regularizing the
network and preventing single tasks from dominating the learning process [21].
Inspired by [21,15], our MTL architecture consists of shared lower layers
derived from BERT common to all tasks and task-specific layers added to this
backbone. A softmax activation function follows each task-specific layer to obtain
the probability distribution for the corresponding task. In this work, the primary
task of offensive language detection is supported by three auxiliary tasks, namely
emotion classification, sentiment analysis, and sexist language detection. These
additional tasks are considered to be correlated with the target domain, as pre-
vious research [11,5,23] has demonstrated their relevance to offensive language
detection. Therefore, let Dτ =

(xτ
i , yτ
i )
	
be the training dataset for a task τ.
The multi-task loss LMT L, calculated for a model θ, is defined as follows [15]:
LMT L(θ) =
4
X
τ=1
X
(xτ
i ,yτ
i )∈Dτ
ℓ(yτ
i , f τ(xτ
i ; θ))
(4)
where ℓis either the binary cross-entropy or the cross-entropy loss depending
on the task, and f τ(xτ
i , θ) denotes the output of the model θ for the task τ.

--- Page 6 ---

6
V.-C. Matei et al.
We employ cross-entropy loss LCE for offensive language detection, sentiment
classification, and sexist language detection. For the emotion analysis dataset,
which comprises seven classes, we use the one-hot encoding representation for
the labels, and thus, the loss function ℓis the binary cross-entropy loss defined
as:
LBCE = −1
NK
N
X
i=1
K
X
k=1
[yi,k · log(pi,k) + (1 −yi,k) · log(1 −pi,k)]
(5)
where yi,k denotes the kth class label from the one-hot ground truth label, and
pi,k is the model’s prediction for the kth class.
3.4
Knowledge Distillation Models
KD. KD [13] aims to reduce the size of a larger model, referred to as the teacher,
by transferring its knowledge to a smaller, faster, and similarly performing model
known as the student. The fundamental principle behind this approach revolves
around compressing the knowledge contained within the teacher model, with the
student learning to mimic his predictions [3].
The temperature parameter T is critical in the knowledge distillation process.
It serves as a mechanism to control the level of confidence in the predictions
made by the teacher model. A higher temperature leads to a more uniform
probability distribution, allowing the student to explore diverse options, while a
lower temperature accentuates the differences between classes, focusing on the
information deemed more relevant by the teacher (i.e., exploitation) [13,20]. The
temperature adjustment is applied at the softmax function, which computes the
probability distribution over classes. Given the input xi, the probability pi,k for
class k is computed based on the network logits zi as follows [13]:
pi,k =
exp(zi,k/T)
P
j exp(zi,j/T)
(6)
The knowledge distillation architecture involves training the teacher and the
student neural networks on the same dataset. A hyperparameter α controls the
interpolation of partial losses, considering the teacher’s soft predictions and the
ground truth labels. The distillation loss is calculated using the cross-entropy
loss (LCE) between the ground truth and the hard predictions and the Kullback-
Leibler (KL) divergence loss (LKL−KD) between the soft labels and soft predic-
tions [20,16]:
LKL−KD = T 2
N
N
X
i=1
KL(pt(xi, T)||ps(xi, T))
(7)
LKD = αLCE + (1 −α)LKL−KD
(8)
where pt(xi, T) represents the softmax outputs of the teacher model, and ps(xi, T)
represents the student’s softmax output, both computed using Eq. 6.

--- Page 7 ---

Enhancing Romanian Offensive Language Detection
7
Fig. 1. Multi-task learning with knowledge distillation and teacher annealing.
MTKD. In natural language processing, the simultaneous learning of mul-
tiple tasks presents a considerable challenge. MTL addresses this challenge by
training a single model to solve numerous tasks concurrently. However, optimiz-
ing a model for various tasks with different complexities can result in perfor-
mance imbalances, where specific tasks dominate while others suffer [18].
To tackle the performance imbalance problem in MTL scenarios, multi-task
learning with knowledge distillation (MTKD) has been proposed by [7]. This
approach leverages the benefits of both techniques to overcome the performance
imbalance problem in MTL scenarios. The core idea is to use specialized mod-
els, called single-task teacher models, to teach a multi-task student model. The
teacher models provide rich information beyond simple one-hot encodings, and
this knowledge is transferred to the student model through distillation.
Based on the findings in [15], let Dτ = {(xτ
i , yτ
i )} with N τ examples repre-
sent the training dataset for the task τ, θ represents student’s parameters being
updated, and θτ represents teacher’s parameters. We denote f τ(xτ
i , θτ) the out-
put computed using Eq. 6 of each task-specific teacher model specialized in task
τ, trained using fine-tuned BERT, and f τ(xτ
i , θ) the output according to Eq. 6
of the student model on task τ. The loss is described as follows [15,20,16]:
LKL−MT KD(θ) =
4
X
τ=1
T 2
N τ
X
(xτ
i ,yτ
i )∈Dτ
KL(f τ(xτ
i ; θτ)||f τ(xτ
i ; θ))
(9)
LMT KD = αLCE + (1 −α)LKL−MT KD
(10)
MTKD-TA. Teacher annealing (TA) [16] is an optimization technique em-
ployed in conjunction with the knowledge distillation method to handle better
the discrepancies between the student and the teacher models. While tempera-
ture is typically used to alleviate this issue, [24] highlights that as the capacity

--- Page 8 ---

8
V.-C. Matei et al.
of the teacher model increases, thereby accentuating the differences with the
student model, the student’s performance improves only up to a certain point,
after which it decreases.
The TA method addresses the capacity difference problem in knowledge dis-
tillation by gradually reducing the influence of the teacher model. In contrast
to the teacher-assistant knowledge distillation approach, which introduces an in-
termediate network, teacher annealing relies on increasing linearly a parameter
during training [15,7], called λ, from 0 to 1. It controls the balance between
the distillation loss and the supervised loss, which measures the discrepancies
between the student’s predictions and the teacher’s predictions and between the
student’s predictions and the ground truth labels, respectively [16]. By gradually
decreasing the teacher’s influence and increasing reliance on the original labels,
the student model becomes more independent and capable of achieving improved
performance [7]. Thus, we modify the multi-task learning with knowledge distil-
lation and teacher annealing (MTKD-TA) loss function as follows:
LMT KD−T A = λLCE + (1 −λ)LKL−MT KD
(11)
As depicted in Fig. 1, the final architecture incorporates four task-specific
datasets to obtain individual teacher models by fine-tuning BERT. Each teacher
model is specialized for one of the four tasks. The student model adopts an MTL
architecture with a modified weight updating scheme in its network, accounting
for the newly introduced loss calculation formula.
4
Experiments
4.1
Datasets
The target dataset used in this research was the RO-Offense dataset4, consisting
of relevant examples curated explicitly for the proposed task. Additionally, three
auxiliary datasets were included to enhance the model’s performance in achieving
the main objective. By incorporating these additional datasets, the aim is to
improve the accuracy and generalization capability of the model in effectively
identifying and classifying offensive language.
RO-Offense. RO-Offense is the largest publicly available dataset for analyz-
ing offensive discourse in the Romanian language. It comprises 12,447 annotated
records, classified into four distinct classes: Profanity (13%), Insult (23%), Abuse
(28%), and Other (36%). To ensure privacy, the dataset has anonymized names
of individuals and organizations, replacing them with generic labels.
REDv2. The Romanian Emotions Dataset (REDv2) [6] is a publicly avail-
able dataset, hosted on GitHub5, that provides 5,449 manually verified tweets for
analyzing emotions in the Romanian language. Each example in the dataset is
classified into one of seven possible classes: Anger, Fear, Joy, Sadness, Surprise,
4 https://huggingface.co/datasets/readerbench/ro-offense
5 https://github.com/Alegzandra/RED-Romanian-Emotions-Dataset

--- Page 9 ---

Enhancing Romanian Offensive Language Detection
9
Trust, and Neutral. Additionally, all tweets have been anonymized by removing
usernames and proper nouns from the dataset.
CoRoSeOf.
The Corpus of Romanian Sexist and Offensive language
(CoRoSeOf) [14] is a publicly available dataset that is a valuable resource for
studying sexist and offensive language in the Romanian context. The dataset,
which can be found on GitHub6, contains 39,245 tweets with labels assigned
by multiple annotators for the classification of sexist and offensive language in
Romanian. Initially, each instance in the dataset was assigned to one of the
five possible classes: Direct Sexism, Descriptive Sexism, Reportive Sexism, Non-
Sexist Offensive, and Non-Sexist. However, for this research, the data has been
transformed into a binary classification format, where all sexist subtypes are
included in the sexist class, while the remaining instances are included in the
non-sexist class.
LaRoSeDa. The Large Romanian Sentiment Data Set (LaRoSeDa) [31] is
a publicly available resource, accessible on GitHub7, that consists of 15,000 re-
views collected from one of the largest e-commerce platforms in Romania. Each
instance in the dataset is labeled as either positive or negative, allowing for
sentiment analysis and contributing to a better understanding of the sentiment
patterns in the Romanian language.
4.2
Experimental Settings
The REDv2 dataset was split into 75% for training, 10% for validation, and
15% for testing. For Ro-Offense, CoRoSeOf, and LaRoSeDa datasets, we use the
80%/10%/10% split. All the trained models used the Transformer library8 as
their base architecture, and their versions are managed using the HuggingFace
platform9. The base architecture used for the distilled student model is Distil-
BERT-base-ro10, while the other models utilize BERT-base-ro-cased11 (BERT-
ro). The main difference between these two architectures is the number of lay-
ers [1]. Distil-BERT-base-ro consists of 6 layers, 81M parameters, and requires
312MB of memory, whereas BERT-ro comprises 12 layers, 124M parameters,
and occupies 477MB of memory. The configuration includes a starting learning
rate of 2e-5, AdamW optimizer, weight decay of 0.01, and batch size 16. The
number of fine-tuning epochs varies between 2 and 7, depending on the dataset
size and the architecture on which the model was trained. The probability α
used in noisy student takes values from the set {15, 20, 25}. The interpolation
parameter λ used in MixUp is set to either 15 or 30. For model evaluation, we
use accuracy (Acc), precision (P), recall (R), and weighted F1-score (F1).
6 https://github.com/DianaHoefels/CoRoSeOf
7 https://github.com/ancatache/LaRoSeDa
8 https://github.com/huggingface/transformers
9 https://huggingface.co/
10 https://huggingface.co/racai/distilbert-base-romanian-cased
11 https://huggingface.co/dumitrescustefan/bert-base-romanian-cased-v1

--- Page 10 ---

10
V.-C. Matei et al.
5
Results
5.1
Results for Knowledge Distillation Models
We focus on the distillation technique combined with multi-task learning, which
enables the transfer of information into a model of the same size but benefits
from diverse inputs from multiple sources of knowledge. This approach allows for
the development of a compact model that can maintain the high performance
of its teacher. The results are presented in Table 1. For the multi-task learn-
ing experiments, we employ the REDv2, LaRoSeDa, and CoRoSeOf datasets as
auxiliary tasks.
Fine-Tuning BERT. During experiments, we noticed that the offensive
language detection model based on the BERT-ro architecture, specifically trained
for offensive language detection and its subtypes, achieves commendable results
with an accuracy of 78.63% and an F1-score of 78.83%. However, BERT-ro is
not easily saturable, and there is room for further enhancement. These scores
indicate the potential for optimizing the model to achieve even better results.
KD. The results obtained by the student using the KD technique on the
main dataset are lower than those achieved by the BERT-ro model. There is
an approximate 1.5% drop in all evaluated metrics, which can be intuitively
explained by the fact that although the student benefits from both the soft
probabilities from the teacher and the direct information from the dataset, it
fails to reach the same performance due to the reduced size of the architecture
of Distil-BERT-base-ro, which consists of only 6 layers instead of 12.
MTL. The MTL model combines all datasets and relies on the larger archi-
tecture, BERT-ro. According to Table 1, the results obtained by the MTL model
are superior to those of the KD model, as the larger architecture allows for more
complex learning. However, the MTL model still falls short of the performance
achieved by the teacher model. This can be attributed to the inherent chal-
lenge of simultaneously learning multiple tasks, mainly when dealing with larger
datasets. Managing each task’s contribution and finding a learning balance is
crucial to improving overall performance.
MTKD. The MTKD model significantly improves over prior experiments. It
surpasses the performance of the teacher model by ∼2.3%, the distilled student
by ∼3.9%, and the MTL model by ∼3.3%. This improvement is achieved by
Table 1. Results on the RO-Offense dataset for knowledge distillation approaches.
Model
Acc
F1
P
R
base model
BERT-ro
78.63
78.83
79.15
78.63
MTL
77.99
77.85
77.80
77.99
distilled student
KD
77.10
77.23
77.44
77.10
MTKD
81.36
81.19
81.12
81.36
MTKD-TA
82.40
82.34
82.29
82.40

--- Page 11 ---

Enhancing Romanian Offensive Language Detection
11
Table 2. Results of student data augmentations on the RO-Offense dataset.
Model
Acc
F1
P
R
KD
77.10 77.23 77.44 77.10
+MixUp Encoder
77.02 77.21 77.53 77.02
+MixUp Sent.-30%
77.51 77.63 77.83 77.51
+RoGPT-2
77.51 77.71 78.10 77.51
+ASDA
77.75 77.73 77.81 77.75
+Noisy-25%
78.07 78.08 78.18 78.07
+ASDA+RoGPT-2
77.67 77.81 78.14 77.67
+ASDA+RoGPT-2+Noisy-15%
77.91 78.11 78.54 77.91
+ASDA+RoGPT-2+Noisy-20%
78.55 78.68 78.90 78.55
+ASDA+RoGPT-2+Noisy-20%+MixUp Sent.-30% 78.07 78.30 78.74 78.07
+ASDA+RoGPT-2+Noisy-20%+MixUp Sent.-15% 78.71 78.81 79.06 78.71
leveraging the transfer of knowledge from the teacher through a processing step
at a temperature T = 4 and utilizing the ground truth information. The balance
between these two sources of information is achieved through α = 0.6 controlling
the partial interpolation of losses.
MTKD-TA. The MTKD-TA model showcases two significant aspects based
on the results obtained. First, as we showed in the previous experiments, the
difference in architecture size led to a loss of information transferred from the
teacher to the student, which was partially regained in this experiment. Second,
we can achieve better results by dynamically scaling the λ coefficient. For most
tasks, the coefficient λ is increased incrementally between 0 and 1, with the
temperature fixed at T = 2. For the emotion detection task, the temperature T =
7 is more effective. The MTKD-TA model outperforms MTKD by approximately
1%, the distilled student by around 5%, and BERT-ro by roughly 3.5%.
5.2
Impact of Data Augmentation
We first explore distilling the base model into a smaller and faster model, which
also benefits from various data augmentation techniques to enhance its perfor-
mance. By employing these techniques, the aim is to strike a balance between
efficiency and accuracy. We present the results of applying data augmentation
techniques to the model obtained through distillation on the smaller architec-
ture, Distil-BERT-base-ro. The results are summarized in Table 2.
MixUp Encoder. This method does not show better results in our results.
The evaluation metrics do not exhibit significant differences that warrant con-
sidering this method in combination with other data augmentation techniques.
MixUp Sentence. Applying the MixUp Sentence technique with interpola-
tion 30% (i.e., MixUp Sent.-30%) at a higher level led to an accuracy improve-
ment of approximately 0.41% compared to the distilled student model alone.
This significant difference justifies combining this method with other augmenta-
tion techniques.

--- Page 12 ---

12
V.-C. Matei et al.
RoGPT-2. We employ RoGPT-2 to replace 30% of the end of the texts.
This augmentation technique results in a performance improvement of approx-
imately 0.5% compared to the reference model, similar to the MixUp Sentence
technique. The metrics indicate the potential benefits of combining it with other
augmentation methods. However, although more diverse, the augmentation is
riskier, completing the sentences more creatively.
ASDA. The utilization of the ASDA method results in an improvement of at
least 0.5% in evaluation metrics. This approach is considered safe and provides
a richer learning context.
Noisy Student. As observed in Table 2, the noisy student (i.e., Noisy)
augmentation technique proves to be the most effective. This method achieves
a significant increase in results of at least 0.8% compared to the distilled stu-
dent alone. Despite its simplicity, the method’s performance underscores the
significance of obtaining controlled noise. In this case, the constraint involves in-
troducing a 25% probability of change, both for word elimination and potential
sentence completion.
Combining augmentation techniques. After analyzing each augmen-
tation technique individually, we combined ASDA and RoGPT-2 to balance
context and creativity, resulting in a 0.6% increase over the student model.
Then, noise was added with a 15% probability initially, but a 20% probabil-
ity yielded a 1.4% increase. Ultimately, the best-performing approach combines
ASDA, RoGPT-2, Noisy Student, and MixUp Sentence. Regarding the MixUp
Sentence method, much better outcomes are obtained by reducing the proba-
bility of interpolating examples from 30% to 15%. In the end, we achieve an
advantage improvement of 1.58% over the distilled student alone, equalizing the
performance of the BERT-ro teacher, which has 53% more parameters.
5.3
Impact of Auxiliary Tasks
Through the lens of the ablation study, we analyze the behavior of MTL models
on offensive language detection by removing different combinations of tasks. The
results presented in Table 3 pertain to the evaluation using the F1-score. The
proposed model refers to the models that employ all three auxiliary tasks, namely
emotions detection, sentiment classification, and sexist language detection. Then,
we present the results obtained after removing the specified tasks, enumerated
after w/o (i.e., without). Note that the proposed model without any auxiliary
tasks in the MTL setting is equivalent to the BERT-ro model.
Sexist language. We notice a significant variation in the impact of the sexist
language task on the final outcome. In the case of the MTL model, the exclusion
of this task leads to very poor results, while for the MTKD-TA model, the results
are quite good even without considering this task. One possible explanation could
be the difficulty of accommodating a larger dataset within the MTL environment.
Combining dataset exclusions. We notice the combinations {emotions,
sexist language} and {sentiment, sexist language} yield similar results, indicating
that the model can successfully learn even without one of the tasks that analyze

--- Page 13 ---

Enhancing Romanian Offensive Language Detection
13
Table 3. Results on RO-Offense after removing auxiliary tasks.
Model
MTL MTKD MTKD-TA
Proposed model
77.85
81.19
82.34
w/o emotions & sentiment & sexist language 78.83
77.23
-
w/o emotions & sentiment
80.08
81.35
80.69
w/o emotions & sexist language
78.97 81.74
82.26
w/o sentiment & sexist language
78.25
81.67
82.39
w/o emotions
80.82 81.47
81.53
w/o sentiment
79.17
81.14
81.69
w/o sexist language
78.71
80.97
81.97
emotions and sentiments. Additionally, a notably lower performance is observed
for the MTKD-TA model when both tasks are excluded from the analysis.
6
Conclusion
This paper developed neural network models to detect Romanian offensive lan-
guage and investigated various techniques to enhance their performance. Inte-
grating additional related tasks (i.e., emotion analysis, sentiment analysis, and
sexist language detection) through MTL demonstrated improved performance.
However, achieving an optimal balance between the contributions of different
tasks in the MTL environment proved challenging. To address this, we em-
ployed KD and TA, resulting in ∼3.5% performance improvement compared
to the BERT-ro model. Additionally, efforts were made to reduce the model size
and utilize data augmentation techniques, leading to an additional performance
increase of ∼1.6%.
Future research directions involve exploring more diverse datasets, optimiz-
ing the MTL setup, fine-tuning hyperparameter combinations, and considering
alternative base architectures. These advancements aim to strengthen the detec-
tion and effective management of Romanian offensive language, contributing to
content filtering, and establishing a safer virtual environment.
Acknowledgements
This work was supported by the NUST POLITEHNICA Bucharest through the
PubArt program, and a grant from the National Program for Research of the
National Association of Technical Universities - GNAC ARUT 2023.
References
1. Avram, A.M., Catrina, D., Cercel, D.C., Dascalu, M., Rebedea, T., P˘ais,, V., Tufi¸s,
D.: Distilling the knowledge of romanian berts using multiple teachers. In: Pro-
ceedings of the thirteenth LREC. pp. 374–384 (2022)

--- Page 14 ---

14
V.-C. Matei et al.
2. Awal, M.R., Cao, R., Lee, R.K.W., Mitrovi´c, S.: Angrybert: Joint learning target
and emotion for hate speech detection. In: Pacific-Asia conference on knowledge
discovery and data mining. pp. 701–713. Springer (2021)
3. Buciluˇa, Cristian anrofbd Caruana, R., Niculescu-Mizil, A.: Model compression.
In: Proceedings of the 12th ACM SIGKDD. pp. 535–541 (2006)
4. Caruana, R.: Multitask learning. Machine learning 28, 41–75 (1997)
5. Chiril, P., Pamungkas, E.W., Benamara, F., Moriceau, V., Patti, V.: Emotionally
informed hate speech detection: a multi-target perspective. Cognitive Computation
pp. 1–31 (2022)
6. Ciobotaru, A., Constantinescu, M.V., Dinu, L.P., Dumitrescu, S.: Red v2: enhanc-
ing red dataset for multi-label emotion detection. In: Proceedings of the Thirteenth
Language Resources and Evaluation Conference. pp. 1392–1399 (2022)
7. Clark, K., Luong, M.T., Khandelwal, U., Manning, C.D., Le, Q.: Bam! born-again
multi-task networks for natural language understanding. In: Proceedings of the
57th ACL. pp. 5931–5937 (2019)
8. Cojocaru, A., Paraschiv, A., Dascalu, M.: News-ro-offense-a romanian offensive lan-
guage dataset and baseline models centered on news article comments. In: RoCHI.
pp. 65–72 (2022)
9. Council, E.: Framework decision on combating certain forms and expressions
of racism and xenophobia. https://eur-lex.europa.eu/legal-content/EN/TXT/
?uri=LEGISSUM%3Al33178 (2008), online, last accesed 16 June 2023
10. Feng, S.Y., Gangal, V., Wei, J., Chandar, S., Vosoughi, S., Mitamura, T., Hovy, E.:
A survey of data augmentation approaches for nlp. In: Findings of the Association
for Computational Linguistics: ACL-IJCNLP 2021. pp. 968–988 (2021)
11. Fortuna, P., Nunes, S.: A survey on automatic detection of hate speech in text.
ACM Computing Surveys (CSUR) 51(4), 1–30 (2018)
12. Guo, H., Mao, Y., Zhang, R.: Augmenting data with mixup for sentence classifi-
cation: An empirical study. CoRR abs/1905.08941 (2019)
13. Hinton, G., Vinyals, O., Dean, J.: Distilling the knowledge in a neural network.
arXiv preprint arXiv:1503.02531 (2015)
14. Hoefels, D.C., C¸¨oltekin, C¸., M˘adroane, I.D.: Coroseof-an annotated corpus of ro-
manian sexist and offensive tweets. In: Proceedings of the Thirteenth Language
Resources and Evaluation Conference. pp. 2269–2281 (2022)
15. Hosseini, M., Caragea, C.: Distilling knowledge for empathy detection. In: Findings
of EMNLP 2021. pp. 3713–3724 (2021)
16. Jafari, A., Rezagholizadeh, M., Sharma, P., Ghodsi, A.: Annealing knowledge dis-
tillation. In: Proceedings of the 16th Conference of the European Chapter of the
Association for Computational Linguistics: Main Volume. pp. 2493–2504 (2021)
17. Kenton, J.D.M.W.C., Toutanova, L.K.: Bert: Pre-training of deep bidirectional
transformers for language understanding. In: Proceedings of NAACL-HLT. pp.
4171–4186 (2019)
18. Li, W.H., Bilen, H.: Knowledge distillation for multi-task learning. In: Computer
Vision–ECCV 2020 Workshops: Glasgow, UK, August 23–28, 2020, Proceedings,
Part VI 16. pp. 163–176. Springer (2020)
19. Li, Y., Caragea, C.: Target-aware data augmentation for stance detection. In: Pro-
ceedings of the Conference of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies. pp. 1850–1860 (2021)
20. Li, Y., Zhao, C., Caragea, C.: Improving stance detection with multi-dataset learn-
ing and knowledge distillation. In: Proceedings of the 2021 Conference on Empirical
Methods in Natural Language Processing. pp. 6332–6345 (2021)

--- Page 15 ---

Enhancing Romanian Offensive Language Detection
15
21. Liu, X., He, P., Chen, W., Gao, J.: Multi-task deep neural networks for natu-
ral language understanding. In: Proceedings of the 57th Annual Meeting of the
Association for Computational Linguistics. pp. 4487–4496 (2019)
22. Liu, Y., Shen, S., Lapata, M.: Noisy self-knowledge distillation for text summariza-
tion. In: Proceedings of the 2021 Conference of the NAACL. pp. 692–703 (2021)
23. Martins, R., Gomes, M., Almeida, J.J., Novais, P., Henriques, P.: Hate speech
classification in social media using emotional analysis. In: 2018 7th Brazilian Con-
ference on Intelligent Systems (BRACIS). pp. 61–66. IEEE (2018)
24. Mirzadeh, S.I., Farajtabar, M., Li, A., Levine, N., Matsukawa, A., Ghasemzadeh,
H.: Improved knowledge distillation via teacher assistant. In: Proceedings of the
AAAI conference on artificial intelligence. vol. 34, pp. 5191–5198 (2020)
25. Niculescu, M.A., Ruseti, S., Dascalu, M.: Rogpt2: Romanian gpt2 for text gener-
ation. In: 2021 IEEE 33rd International Conference on Tools with Artificial Intel-
ligence (ICTAI). pp. 1154–1161. IEEE (2021)
26. Pan, S.J., Yang, Q.: A survey on transfer learning. IEEE Transactions on knowledge
and data engineering 22(10), 1345–1359 (2009)
27. Park, S., Caragea, C.: Multi-task knowledge distillation with embedding con-
straints for scholarly keyphrase boundary classification. In: Proceedings of the 2023
Conference on EMNLP. pp. 13026–13042 (2023)
28. Radford, A., Narasimhan, K., Salimans, T., Sutskever, I., et al.: Improving lan-
guage understanding by generative pre-training (2018)
29. Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al.: Language
models are unsupervised multitask learners. OpenAI blog 1(8), 9 (2019)
30. Struß, J.M., Siegel, M., Ruppenhofer, J., Wiegand, M., Klenner, M., et al.:
Overview of germeval task 2 (2019)
31. Tache, A., Mihaela, G., Ionescu, R.T.: Clustering word embeddings with self-
organizing maps. application on laroseda-a large romanian sentiment data set. In:
Proceedings of the 16th Conference of the European Chapter of the Association
for Computational Linguistics: Main Volume. pp. 949–956 (2021)
32. Vlad, G.A., Tanase, M.A., Onose, C., Cercel, D.C.: Sentence-level propaganda
detection in news articles with transfer learning and bert-bilstm-capsule model. In:
Proceedings of the Second Workshop on Natural Language Processing for Internet
Freedom: Censorship, Disinformation, and Propaganda. pp. 148–154 (2019)
33. Waseem, Z., Thorne, J., Bingel, J.: Bridging the gaps: Multi task learning for
domain transfer of hate speech detection. Online harassment pp. 29–55 (2018)
34. Wei, J., Zou, K.: Eda: Easy data augmentation techniques for boosting performance
on text classification tasks. In: Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the 9th International Joint Confer-
ence on Natural Language Processing (EMNLP-IJCNLP). pp. 6382–6388 (2019)
35. Wu, X., Lv, S., Zang, L., Han, J., Hu, S.: Conditional bert contextual augmenta-
tion. In: Computational Science–ICCS 2019: 19th International Conference, Faro,
Portugal, June 12–14, 2019, Proceedings, Part IV 19. pp. 84–95. Springer (2019)
36. Xie, Q., Luong, M.T., Hovy, E., Le, Q.V.: Self-training with noisy student improves
imagenet classification. In: Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition. pp. 10687–10698 (2020)
37. Zampieri, M., Malmasi, S., Nakov, P., Rosenthal, S., Farra, N., Kumar, R.:
SemEval-2019 task 6: Identifying and categorizing offensive language in social me-
dia (OffensEval). In: Proceedings of the 13th International Workshop on Semantic
Evaluation. pp. 75–86. Minneapolis, Minnesota, USA (2019)
38. Zhang, H., Cisse, M., Dauphin, Y.N., Lopez-Paz, D.: mixup: Beyond empirical risk
minimization. arXiv preprint arXiv:1710.09412 (2017)

```
