---
title: "2025-results-A Novel Deep Learning Framework with - PDF Extract"
source_pdf: "2025-results-A Novel Deep Learning Framework with.pdf"
pages: 13
extracted_at: "2026-02-13T10:43:55.895792"
---

# PDF Extract: 2025-results-A Novel Deep Learning Framework with

**Source PDF:** 2025-results-A Novel Deep Learning Framework with.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

1
SigNet: A Novel Deep Learning Framework for
Radio Signal Classiﬁcation
Zhuangzhi Chen*, Hui Cui*, Jingyang Xiang, Kunfeng Qiu, Liang Huang, Member, IEEE,
Shilian Zheng, Member, IEEE, Shichuan Chen, Qi Xuan, Senior Member, IEEE, and Xiaoniu Yang
Abstract—Deep learning methods achieve great success in
many areas due to their powerful feature extraction capabilities
and end-to-end training mechanism, and recently they are also
introduced for radio signal modulation classiﬁcation. In this
paper, we propose a novel deep learning framework called SigNet,
where a signal-to-matrix (S2M) operator is adopted to convert
the original signal into a square matrix ﬁrst and is co-trained
with a follow-up CNN architecture for classiﬁcation. This model
is further accelerated by integrating 1D convolution operators,
leading to the upgraded model SigNet2.0. The simulations on two
signal datasets show that both SigNet and SigNet2.0 outperform
a number of well-known baselines. More interestingly, our
proposed models behave extremely well in small-sample learning
when only a small training dataset is provided. They can achieve
a relatively high accuracy even when 1% training data are kept,
while other baseline models may lose their effectiveness much
more quickly as the datasets get smaller. Such result suggests
that SigNet/SigNet2.0 could be extremely useful in the situations
where labeled signal data are difﬁcult to obtain. The visualization
of the output features of our models demonstrates that our model
can well divide different modulation types of signals in the feature
hyper-space.
Index Terms—Deep learning, Modulation recognition, Convo-
lutional neural network.
I. INTRODUCTION
Q
UICK and accurate classiﬁcation of radio signals has
become an important issue in intelligent signal process-
ing, due to the wide usage of radio technology in numerous
*: The ﬁrst two authors contributed equally.
This work was supported in part by the National Natural Science Foundation
of China under Grant 61973273 and Grant 62072410, and by the Zhejiang
Provincial Natural Science Foundation of China under Grant LR19F030001
and LY19F020033. (Corresponding author: Qi Xuan.)
Z.
Chen,
H.
Cui,
J.
Xiang,
and
K.
Qiu
are
with
the
Insti-
tute of Cyberspace Security, and also with the College of Informa-
tion Engineering, Zhejiang University of Technology, Hangzhou 310023,
China (e-mail: zhuangzhichen@foxmail.com; huicuizjut@qq.com; xiangxi-
angjingyang@gmail.com; yexijoe@163.com).
L.
Huang
is
with
the
College
of
Computer
Science
and
Tech-
nology, Zhejiang University of Technology, Hangzhou, China (email:
lianghuang@zjut.edu.cn)
S. Zheng and S. Chen are with the Science and Technology on Communica-
tion Information Security Control Laboratory, Jiaxing 314033, China (e-mail:
lianshizheng@126.com; sicanier@sina.com).
Q. Xuan is with the Institute of Cyberspace Security, College of Information
Engineering, Zhejiang University of Technology, Hangzhou 310023, China,
with the PCL Research Center of Networks and Communications, Peng Cheng
Laboratory, Shenzhen 518000, China, and also with the Utron Technology
Co., Ltd. (as Hangzhou Qianjiang Distinguished Expert), Hangzhou 310056,
China (e-mail: xuanqi@zjut.edu.cn).
X. Yang is with the Institute of Cyberspace Security, Zhejiang University
of Technology, Hangzhou 310023, China, and also with the Science and
Technology on Communication Information Security Control Laboratory,
Jiaxing 314033, China (e-mail: yxn2117@126.com).
ﬁelds. In the open electromagnetic space, there are various
radio signal classiﬁcation tasks according to different stan-
dards and applications, such as modulation recognition [38],
Aircraft Communications Addressing and Reporting System
(ACARS) signal classiﬁcation [5], [40], technology recogni-
tion [3], [26] etc. With the massive use of mobile devices
and the development of 5G technology [9], the demand for
limited electromagnetic spectrum resources in modern society
is growing rapidly, which increases the difﬁculty of managing
radio signals in open electromagnetic space. Improving the
accuracy of modulation recognition can quickly manage the
effective range of electromagnetic spectrum, and ensure the
safety and reliability of communication system [37]. Radio
signal classiﬁcation and modulation recognition have drawn
the attention of many researchers. Recently, Kulin et al. [12],
Mendis et al. [16], Dobre [7] and Zheng et al. [39] have
proposed their respective radio signal recognition methods.
Signal classiﬁcation has generally been accomplished by
feature extraction and classiﬁcation. Feature extraction fo-
cuses on extracting the important characteristics from the
target signals, such as instantaneous amplitude, frequency and
phase, constellation diagram, higher-order moment, and time-
frequency diagram etc., which then are fed into machine learn-
ing methods for classiﬁcation. For example, Walenczykowska
et al. [29] used wavelet transform and neural network for
modulation identiﬁcation. Li et al. [13] mapped the signal to
a high-dimensional feature space by using wavelet transform
and then used Support Vector Machine (SVM) to automati-
cally recognize multiple types of digitally modulated signals.
Triantafyllakis et al. [27] adopted random forest algorithm to
identify pulse-time-frequency image characteristics of intra-
pulse modulation. Vuˇci´c et al. [28] introduced a theory based
on cyclic stationary signal classiﬁcation method. While Ab-
delmutalab et al. [1] used high order cumulants as features to
classify M-PSK and M-QAM signals. Most of these methods
require extensive expertise and meanwhile may be lack of high
precision, which greatly limit their application, especially in
complex scenes.
Recently, with the successful application of deep learning
in image classiﬁcation [33], [34], textural analysis [6], speech
recognition [24], and graph mining [4], [35], deep neural
networks are also becoming a preferable way for signal
classiﬁcation. Deep learning models, especially Convolutional
Neural Networks (CNNs), can automatically extract features
from various datasets based on task goals, which have been
proved to be signiﬁcantly superior to manual feature extraction
arXiv:2011.03525v2  [eess.SP]  18 Oct 2021

--- Page 2 ---

2
in many situations. Due to their powerful feature learning
capabilities, CNNs are widely applied for signal classiﬁcation.
For instance, O’Shea et al. [21] adopted VGG architecture
principals to design a 1D-CNN model, making it suitable
for small radio signal classiﬁcation tasks; meanwhile they
also adopted a 1 × 1 convolutional layer for ResNet unit
input, achieving comparable results. O’Shea et al. [19] also
used a narrow 2D-CNN for radio modulation recognition by
simply considering both in-phase (I) and quadrature (Q) signal
sequences in the time domain at the same time. A more
complex model in their paper was called CNN2, based on
which Liu et al. [14] and West et al. [31] designed their
own deep learning models for the respective signal modulation
classiﬁcation tasks. Using such kind of 1D convolution and
narrow 2D convolution, Xu et al. [32] proposed a multi-
channel CNN, named MCLDNN, to do modulation classi-
ﬁcation with different convolution features. However, these
existing models have extremely simple structures and may not
take advantage of the deep architecture of neural networks
to deal with more complex scenes. And for narrow 2D CNN
technique (using a narrow width input), it may not adequately
utilize the power of CNNs, since when the pooling layers
or stride > 1, feature maps in hidden layers will shrink to
one-dimensional vectors soon, and thus they can only extract
features in this one direction.
An alternative way is to preprocess the signals, so as to
change them into matrices, which are then fed into CNNs
to get classiﬁcation results. For instance, Peng et al. [23]
proposed a modulation classiﬁcation algorithm based on the
signal constellation diagram and deep learning models. Zeng
et al. [36] transformed signals into spectrogram images as the
input of CNN. There are also some related algorithms in the
area of time series analysis. For example, Wang et al. [30]
proposed a novel framework for encoding time series, where
the Gramian Angular Fields (GAF) and Markov Transition
Fields (MTF) are used to convert time series into different
types of images. However, these conversion methods are based
on speciﬁc mathematical formulas, like some speciﬁc feature
transformation (transform the original data to a more complex
but speciﬁc space), and thus are lack of ﬂexibility and may
lose some useful features.
On the other hand, radio signals are also a kind of time-
series, therefore, instead of losing their time information in
CNNs, long short term memory (LSTM) [8] can be a good
candidate to capture the time related features of signals. In
fact, LSTM has been adopted in multiple signal ﬁelds [17],
[41]. For instance, O’Shea et al. [18] applied deep recurrent
neural networks (RNN) for end-to-end radio trafﬁc sequence
recognition. Yildirim et al. [41] proposed a deep bidirectional
LSTM network for wavelet sequences and realized electro-
cardiogram signal classiﬁcation. Mostayed et al. [17] used
a bidirectional LSTM network to detect pathologies in ECG
signals. Rajendran et al. [25] adopted an LSTM based model
for modulation classiﬁcation in a distributed wireless spectrum
sensing network. Huang et al. [11] did three kinds of signal
data augmentations and evaluated them through an LSTM
model. LSTM models are able to capture the time information
due to its gate structure and memory cells and thus are
considered to be more suitable for signal classiﬁcation, leading
to higher accuracy in general. However, they are always time-
consuming and are also difﬁcult to train especially for long
signals in complex tasks.
To fully utilize the powerful feature extraction capability
of CNNs and meanwhile overcome the shortage of above
methods, in this paper, we ﬁrst focus on transforming signal
to a two-dimensional matrix as input so as to make it easy
for CNN to extract features. In particular, we design a ﬂexible
deep learning framework SigNet based on sliding trainable
operators which are used to adaptively extract the characteris-
tics of signals. Since different operators can capture the signal
properties in different aspects and scales and further automat-
ically transfer a signal into different matrices, integration of
which by typical CNN architecture thus can largely improve
the classiﬁcation performance. Moreover, to further accelerate
the training of SigNet, we replace some of the 2D convolution
operators by 1D convolution operators, and propose SigNet2.0.
Interestingly, SigNet2.0 is not only faster than SigNet, but may
also have slightly higher classiﬁcation accuracy, indicating its
outstanding performance in practice. The main contributions
of this paper are as follows.
1) We develop SigNet as a novel deep learning framework
for signal classiﬁcation by introducing a sliding square
operator S2M, with which the input signal can be
automatically transformed into a square feature matrix.
This S2M is trainable by connecting to a CNN structure
and can adaptively extract important features, avoiding
tedious preprocessing of the original signals.
2) We accelerate SigNet by integrating 1D and 2D convo-
lution operators, and propose SigNet2.0. This upgraded
model reduces the complexity of signals through 1D
convolution operators and then converts the simpliﬁed
signals into feature matrices through S2M, thereby im-
proving both classiﬁcation accuracy and efﬁciency.
3) We perform comprehensive simulations on two signal
datasets, and validate the outstanding performance of
our models. Speciﬁcally, SigNet performs signiﬁcantly
better than other models, and is close to the latest model
MCLDNN on RML2016.10a dataset (The accuracy of
SigNet on the entire test set is 61.35%, while that of
MCLDNN is 61.16%). And for dataset Sig2019-12,
SigNet performs signiﬁcantly better than all the other
models, especilly when the SNR is below 0dB. (The
accuracy of SigNet on the entire test set is 72.69%, while
the second best model MCLDNN is 67.52%), SigNet2.0
performs even better on two datasets (achieving the
accuracy of 62.30% and 72.87%, respectively). The
visualizations of the output features for various models
shows that our proposed models have a strong ability to
distinguish features of modulation categories.
4) We ﬁnd that SigNet and SigNet2.0 perform extremely
well in small-sample learning. Both of them keep a
relatively high accuracy when using a much smaller
training dataset, while other methods may lose their
effectiveness quickly. This phenomenon suggests that
our proposed models could be more practical since

--- Page 3 ---

3
labeling signals are always expensive.
The rest of paper is organized as follows. In Sec. II, we
present the details of our technique and the principal and
advantages. After that, we show the simulation setup and
results with analysis and discussion in Sec. III. And we further
visualize the model output features in Sec. IV to explain how
SigNet and SigNet2.0 behave better than other models. Finally,
we conclude the paper and give possible directions for the
future work in Sec. V.
II. METHOD
In this section, we introduce our method in detail. Speciﬁ-
cally, for the IQ signal, we ﬁrst design a series of parameter-
trainable matrix operations, transform them into matrices, and
then classify them with some typical deep learning model.
The overall framework of SigNet is shown in Fig. 1. We
mainly focus on the trainable signal-to-matrix method and the
work-ﬂow of the entire framework. Finally, based on our basic
model SigNet, we also introduce the accelerated version, i.e.,
SigNet2.0, by integrating 1D and 2D convolution operators,
whose structure is shown in Fig. 2.
A. S2M operator
The received radio signal can be seen as a function of time,
it is usually represented by its in-phase and the quadrature
(IQ) components as
x(t) = xI(t) + jxQ(t).
(1)
The real and imaginary parts of x(t) represent the I and Q
components, respectively. Usually, the signal is sampled at a
certain frequency, and the length of each signal sample is ﬁxed
to form a dataset.
For an IQ signal sample, we ﬁrst treat I channel and Q
channel separately, and transfer them into matrices by using
different signal-to-matrix (denoted by S2M brieﬂy) operators.
Speciﬁcally, to facilitate the implementation of the algorithm,
an IQ signal can be represented by:
I
=
[i1, i2, i3, ..., iN],
(2)
Q
=
[q1, q2, q3, ..., qN],
(3)
where N is the signal length of each channel. Without loss
of any generalization, here we focus on I channel, and the
operation for Q channel is exactly the same as I channel.
Firstly, we use a sliding window to sample the signal of I
channel, where the length of the window, denoted by k, is
adjustable. By the sliding window, we get a slice of signal
with length k. The window moves from [i1, i2, ..., ik] to the
end of the signal [iN−k+1, iN−k+2, ..., iN], with the default
stride set to h = 1. From the start to the end, putting all the
slices together, we thus get a slice matrix as follows:
SI =


i1
i2
· · ·
ik
i2
i3
· · ·
ik+1
...
...
...
...
iN−k+1
iN−k+2
· · ·
iN

,
(4)
with the matrix size (N −k+1)×k, meaning there are totally
N −k + 1 slices of length k.
Now, we deﬁne a ﬁlter FI as our trainable operator, which
is represented by a square matrix:
FI =


α11
α12
· · ·
α1k
α21
α22
· · ·
α2k
...
...
...
...
αk1
αk2
· · ·
αkk

,
(5)
with the matrix size k × k. The values of elements in FI
are randomly set by standard Gaussian distribution initially,
and can be update by optimization algorithms in the training
process of the whole deep learning framework.
Based on the slicing matrix SI and the ﬁlter FI, we can
transform a signal of I channel into a feature matrix by
MI = SI · FI · ST
I ,
(6)
with the matrix size (N −k + 1) × (N −k + 1).
Note that the elements in matrix MI can be considered as a
kind of dot product of two signal slices at different positions
with the operator FI:
mI(h, l) = [ih, ih+1, · · · , ih+k]·FI·[il, il+1, · · · , il+k]T, (7)
where mI(h, l) represents the element of matrix MI at
position (h, l). Since dot product of two vectors generally
represents the correlation between them, feature matrix MI
can capture the local auto-correlation of the signal under
appropriate transformation, to certain extent.
Similarly, we can get the feature matrix of the Q-channel
signal:
MQ = SQ · FQ · ST
Q,
(8)
where SQ, FQ represent the signal slice matrix and ﬁlter ma-
trix of the Q-channel signal, denoted as follows, respectively.
SQ =


q1
q2
· · ·
qk
q2
q3
· · ·
qk+1
...
...
...
...
qN−k+1
qN−k+2
· · ·
qN

,
(9)
FQ =


β11
β12
· · ·
β1k
β21
β22
· · ·
β2k
...
...
...
...
βk1
βk2
· · ·
βkk


(10)
In this way, we convert the IQ signal into two matrices MI
and MQ, which can be summarized as Algorithm 1.
B. Work-ﬂow of SigNet
Through S2M operator, we can get two feature matrices MI
and MQ corresponding to I and Q channels, respectively. Then,
to do signal classiﬁcation, we concatenate the two matrices in
the channel dimension to form a two-channel image, which is
then fed into a CNN for training and classiﬁcation, as shown
in Fig 1. Here, the CNN structure could be any typical one,
such as Alexnet, VGG and ResNet etc.
The training of the overall deep learning framework can
be divided into two parts: the ﬁrst is training for the signal

--- Page 4 ---

4
Matrix
(N-K+1)x(N-K+1)
Matri
Transpose


Input-I
1xN
Slice
1xK
Filter-I
KxK
Transposed
slice
Kx1
Value
1x1


Input-Q
1xN
Slice
1xK
Filter-Q
KxK
Transposed
slice
Kx1
Value
1x1
Matrix
(N-K+1)x(N-K+1)
Matrix
2x(N-K+1)x(N-K+1)
ZERO
PAD
CONV
Batch Norm
ReLU
MAX POOL
CONV
Batch Norm
ReLU
x3
Ă
AVG
POOL
Flatten
Output
ResNet50
CONV
Batch Norm
ReLU
Å
S2M
Fig. 1. The framework of SigNet. A signal-to-matrix operation S2M is implemented by matrix multiplication of signal slices and trainable ﬁlters and then a
typical CNN (ResNet50) is used for classiﬁcation. They are trained together by neural network optimization algorithms.
Algorithm 1 S2M operation
Input: IQ signal: I = [i1, i2, ..., iN], Q = [q1, q2, ..., qN];
Parameters: ﬁlter size k.
Output: Matrices MI and MQ.
1: Get slice matrices SI and SQ by Eq. (4) and Eq. (9),
respectively.
2: Get trainable ﬁlters FI and FQ:
If initialization: FI ∼N(0, 1), FQ ∼N(0, 1);
If training: FI = FI −η∇L(FI), FQ = FQ −η∇L(FQ),
where L is the classiﬁcation loss of entire deep learning
framework, and η is the learning rate.
3: Obtain the feature matrices:
MI = SI · FI · ST
I ;
MQ = SQ · FQ · ST
Q.
4: Return MI, MQ.
ﬁlters (FI and FQ) and the second is training for CNN. The
ﬁlter training is to ﬁnd better matrix representations of signals,
and the CNN training is to ﬁnd higher feature representations
from these matrices. Note that the whole framework is end-to-
end, while the ﬁlters and CNN can be either trained together
or alternately. Also, we can set different training parameters
for them, such as different learning rate or different weight
decay proposals. In this paper, for convenience, we train them
together with the same training parameters.
In this way, we can make full use of the capacity of
CNN in processing images (or matrices) without destroy the
inherent structure of the signals. Simulation results conﬁrm
the performance of our method.
C. Principal and advantages
The core of SigNet is to develop a new operator for signal
processing, which can be adaptively trained when naturally
integrated into the framework of CNN. And the motivation of
using a sliding window and a trainable ﬁlter to transfer 1D
signal into 2D matrix is that we believe, with the end-to-end
training, the trained operator can better convert the signal into
a two-dimensional representation. Just as the automatic image
classiﬁcation of CNN has surpassed the image classiﬁcation of
artiﬁcially designed features, an automatic image representa-
tion of signal may be better than deterministic signal-analysis-
based and speciﬁc-mathematical-formulas-based approaches.
Signals are typical time series, with the key information
to distinguish each other hidden in the correlation between
segments. The information at each point is simple, while that
of the whole signal is complex. We thus ﬁrst get continuous
slices of signal by a sliding window with length k, denoted by
xh, h = 1, 2, · · · , xN−k+1, with xh = [ih, ih+1, · · · , ih+k−1]
for I channel and xh = [qh, qh+1, · · · , qh+k−1] for Q channel;
then we calculate the correlation between each pair of them
after a linear mapping function g(xh) = G · xh′, with G the
square matrix with size k, to get the feature matrix:
mhl = g(xh)Tg(xl) = xhGTGx′
l,
(11)
which will be equivalent to Eq. (7) when we simply set FI =
GTG. Interestingly, when FI or G is set to identity matrix,
we will get
mhl = xhx′
l,
(12)
which degenerates to Gram matrix and characterizes the cor-
relation between two slices of the signal at different positions.
In this sense, the feature matrix of S2M is actually a
transformed correlation matrix of all the signal slices (or
namely a transformed local auto-correlation matrix for the
whole signal). Note that, in a previous work [30], Wang et al.
used the Gramian Angular Fields to convert time series into
different types of images for signal classiﬁcation. The main
difference is that we don’t use the Angular Field to transfer
the values to some angles, instead, we use a trainable ﬁlter to
transform the representational space of signal slices ﬁrst and
then calculate their inner products. The obtained feature matrix
could be considered as a generalized version of Gram matrix
based on signal slices. And SigNet thus has the following
advantages: First, through training with the CNN, a more
suitable representational space can be automatically found for
classiﬁcation; Second, the original Gram matrix is a symmetric
matrix, which is big but of huge information redundancy. By
breaking such symmetry, more information could be utilized,
since it could be different for exchanging two slices when
multiply by a transformation matrix between them.

--- Page 5 ---

5
Input
ZERO
PAD
CONV
Batch Norm
ReLU
MAX POOL
˄Stage1˅
CONV
Batch Norm
ReLU
(ID Block)x2
(Stage2)
AVG
POOL
Flatten
Output
CONV
Batch Norm
ReLU
Å
CONV
Batch Norm
ReLU
(ID Block)x3
(Stage3)
CONV
Batch Norm
ReLU
CONV
Batch Norm
ReLU
(ID Block)x5
(Stage4)
CONV
Batch Norm
ReLU
CONV
Batch Norm
ReLU
(ID Block)x2
(Stage5)
CONV
Batch Norm
ReLU
Å
Å
Å
Using Conv1D
(Conv Block)
(Conv Block)
(Conv Block)
(Conv Block)
Using Conv2D
Fig. 2. One kind of structure of SigNet2.0, which is based on ResNet50. We try to use 1D convolution to replace some of the 2D convolution of SigNet to
accelerate the model. Here we choose replacing 1D convolution with 2D convolution on stage1 and stage2, for it’s highest classiﬁcation accuracy.
Compared with those methods that directly utilize signals,
such as reshape, narrow 2D-CNN and 1D-CNN, our SigNet
makes full use of feature extraction capabilities of CNNs
without destroying the structural information of original sig-
nals, leading to the ﬂuent learning of the whole framework.
SigNet is such a ﬂexible framework, one can adjust the size of
ﬁlter to ﬁnd the information-unit on a longer or shorter slice,
and change the stride to reduce the input size when signal
is especially long. We will continue to explore these hyper-
parameter sensitivities and researchers can also adjust them
according to their own tasks to get a better performance.
D. Acceleration and upgrade by integrating 1D convolution
SigNet converts the original signal sequence into a matrix,
which can enrich the hidden features of the signal. However,
this conversion greatly increases the size of the input data,
and the model will occupy a lot of computing resources,
especially for a long input sequence. On the other hand,
1D-CNN is naturally adopted to classify signals, which has
the following advantages: Firstly, it directly uses the signal
sequence without destroying its inherent structure; Secondly,
it is fast and effective. O’Shea et al. [21] designed a 1D-CNN
model and made it suitable for small radio signal classiﬁcation
tasks. Therefore, here, we consider to integrate 1D-CNN into
our framework so as the accelerate and upgrade our model.
We try to use 1D convolution operators to replace some
of the 2D convolution of SigNet to accelerate the framework,
and the speciﬁc number of replacement layers depends on the
structure of the CNN. As shown in Fig. 2, for example, we use
ResNet50 [10] as the basic CNN structure for classiﬁcation,
which consists of 5 stages each with a convolution block and
several identity blocks, each convolution block has 3 convo-
lution layers and each identity block also has 3 convolution
layers. For the original SigNet, the signal sequence will be
converted into a matrix ﬁrst by S2M and then input into
ResNet50 for classiﬁcation, but now we consider to use 1D
convolution ﬁrst to reduce the length of the signal sequence
and thus reduce the size of the transformed matrix. Begin
from the input layer, we replace some of 2D convolutional
layers of ResNet50 with 1D convolutional layers (we repalced
stage1 and stage2, actually), these 1D convolution structure
can be seen as the part of 1D ResNet50, it will output the
feature sequence of the input signal, which is much shorter
than the input signal but could contain most of the useful
information. Then, an S2M operation will be deployed to
convert the feature sequence to a matrix and the rest of the
structure of ResNet50 will do the ﬁnal classiﬁcation. We
name the upgraded model SigNet2.0 which mixes the 1D
structure and 2D structure of the CNN for signal classiﬁcation.
Simulation results show that SigNet2.0.0 can greatly improve
the efﬁciency of model training without loss of classiﬁcation
accuracy. Impressively, when the ratio of 1D structure and
2D structure is set appropriately, it can even improve the
classiﬁcation accuracy of the model to a certain extent.
III. SIMULATIONS
In this section, we perform the simulations to validate the
effectiveness of our models. All the deep learning models are
trained on NVIDIA Tesla V100-PCIE.
A. Modulation dataset
We evaluate our methods on the following two datasets for
signal modulation classiﬁcation.
• RML2016.10a This dataset is public for signal modu-
lation classiﬁcation [19], [20]. It uses GNU Radio [2]
to synthesize IQ signal samples. The dataset contains
11 modulation categories consisting of BPSK, QPSK,
8PSK, 16QAM, 64QAM, BFSK, CPFSK, and PAM4 for
digital modulations, and WB-FM, AM-SSB, and AM-
DSB for analog modulations. The signal to noise ratio
(SNR) ranges from -20dB to 18dB, the length of each
sample is 128, and the total size of the dataset is 220,000.
We divide the dataset into training set, validation set and
test set according to the ratio of 6:2:2, the size of training
set is 132000 (600 samples per modulation type of each
SNR), the size of validation set and test set are both
44000 (200 samples per modulation type of each SNR).
• Sig2019-12 This dataset contains longer signals simulated
by ourselves. The simulation considers several nonideal
effects of a real communication system, including carrier

--- Page 6 ---

6
phase, pulse shaping, frequency offsets and noise. It
contains 12 modulation categories consisting of BPSK,
QPSK, 8PSK, OQPSK, 2FSK, 4FSK, 8FSK, 16QAM,
32QAM, 64QAM, 4PAM, and 8PAM. The original data
is generated in a random manner, so as to guarantee equal
probability of transmitted symbols. The pulse shaping
ﬁlter is a raised cosine ﬁlter, and the roll-off factor
is a random value within the range 0.2 to 0.7. The
phase offset is randomly selected within the range −π
to π, and the carrier frequency offset (normalized to
the sampling frequency) is randomly selected within the
range -0.1 to 0.1. The SNR of each modulation type is
evenly distributed from -20dB to 30dB. Each data sample
contains 64 symbols, and the oversampling rate is 8, so
the number of sampling points for each sample is 512.
The total size of the dataset is 468000 (1500 samples per
modulation type of each SNR), and we divide dataset into
training set, validation set and test set according to the
ratio of 6:2:2, just the same as the division strategy of
RML2016.10a dataset.
In the following signal modulation classiﬁcation tasks, all
simulations are based on these two datasets, for RML2016.10a,
because all examples were scaled to unit energy [20], we use
the raw data as input; for Sig2019-12, we use the maximum-
minimum normalization to normalize each sample, which can
be formulated as x′
i = (xi −min)/(max −min) × 2 −1,
where xi is the original value of each sampling point in a
signal channel (I or Q), max and min are the maximum and
minimum values of the sampling points in a signal channel, re-
spectively. Without special instructions, we use entire training
set for training, entire validation set for validation and entire
test set for testing.
B. Models’ setup and baselines
To do signal classiﬁcation, we set our SigNet with 2 ﬁlters
of shape 3×3 and 1 stride in S2M operation, so it can transfer
an IQ signal to a 2-channel matrix, each 128-length signal
will be converted into a 126 × 126 × 2 image and each 512-
length signal will be converted into a 510 × 510 × 2 image.
Such image then will be imported into a default ResNet50 [10]
model implemented by Pytorch [22].
There are several kinds of baselines to be compared so as
to validate the effectiveness of our models. The ﬁrst kind
is to directly transfer the signal as 2D input, speciﬁcally,
we reshape each signal sample into a square matrix, a 128
(or 512) length IQ signal can be concatenated into a 256
(1024) length sequence, and then it can be further reshaped
as a 16 × 16 (or 32 × 32) matrix, which is then fed into
the ResNet50. In the ﬁeld of time-series analysis, there are
also methods to convert a time-series to a matrix ﬁrst using
some theories, such as GAF and MTF, and then connect to
typical CNN models to get classiﬁcation results. The brief
introduction of these methods are provided in Sec. II, and
there is also a method that uses signal constellation diagram
and deep learning models for classiﬁcation [23]. Here we use
these methods as the second kind of baselines which mainly
use some speciﬁc mathematical method to convert signal to
matrix. There are also several existing researches that using
deep learning methods to do signal classiﬁcation, such as
narrow 2D-CNN [19], 1D-ResNet [21], MCLDNN [32], and
LSTM [25]. We use them as the third kind of baselines. We
re-implemented the above-mentioned methods in the same
programming environment based on Python3, implemented
all the deep learning models for simulation based on the
deep learning framework Pytorch, and performed simulations
based on our datasets division. For dataset RML2016.10a, the
architecture description of these models are shown in Table I,
the layers of the model from input to output are described in
order. And for dataset SigNet2019-12, there is no changes but
the number of output neurons will be 12.
TABLE I
ARCHITECTURE DESCRIPTION OF DIFFERENT MODELS FOR
RML2016.10A DATASET.
Models
Architecture description
1D-ResNet
6 ResidualStack each contains 5 Conv1D
of kernel size 3 and pool size 2, Dense(128),
Dropout(0.3), Dense(11)
2D-CNN
Conv2D(256x1x3), ReLU, Dropout(0.5),
Conv2D(80x2x3), ReLU, Dropout(0.5), Dense(256),
ReLU, Dropout(0.5), Dense(11), softmax(11)
LSTM
LSTM(128), LSTM(64), Dense(11)
MCLDNN
Conv1D(50x7) concats with (Conv1D(100x7),
Conv1D(50x7)), ReLU, Conv1D(100x5),
LSTM(128), LSTM(128), Dense(128),
Dropout(0.5), Dense(128), Dropout(0.5),
Dense(11)
SigNet
S2M with a typical 2D ResNet50
SigNet2.0
S2M with a 1D-2D Fusion ResNet50
For each model training, ﬁrstly, we set an epoch number
to ensure the model’s testing accuracy reaches convergence
after training. Then, after each epoch of training, the model
will be validated on the validation set. Finally, the epoch of
training with the highest validation accuracy will be the last
epoch of training. We select all the models with the highest
validation accuracy, save them and use them for testing and
performance comparison. We use a warm-up cosine annealing
strategy for learning rate decay with an Adam optimizer, and
for each model, we used the initial learning rate 0.001 and
0.1 for RML2016.10a and Sig2019-12 datasets, respectively,
to ensure that it can be effectively trained. We set batch size
of 128 and 32 for each model with RML2016.10a dataset and
Sig2019-12 dataset, respectively.
C. Effectiveness of S2M operator
We ﬁrst compare the classiﬁcation results obtained by
SigNet with those obtained by the ﬁrst and second kinds
of baselines, by simply reshaping input (Reshape) or us-
ing speciﬁc mathematical input conversion (GAF, MTF, and
constellation diagram), to validate the effectiveness of our
trainable S2M operator.
We train the models by using the whole training set, and
then give the classiﬁcation accuracy on test samples of each
SNR. The results are shown in Fig. 3, where we can see that,
on both datasets, SigNet has a higher accuracy than the others.

--- Page 7 ---

7
Some signal conversion methods, such as GAF and MTF,
perform quite differently on different datasets, which may
suggest that these methods lack good generalization ability.
All of these indicate that trainable S2M operators can indeed
match better with CNN classiﬁer, i.e., it can adaptively capture
the better features of signals for classiﬁcation.
D. Comparison with other deep learning models
In this part, we compare SigNet with several state-of-
the-art deep learning models applying in signal modulation
classiﬁcation. In particular, we choose three CNN models,
narrow 2D-CNN [19], 1D-ResNet [21] and MCLDNN [32],
and a 2-layer LSTM model [25] as the baselines. The ﬁrst three
are the most advanced CNN models for signal modulation
classiﬁcation, while the last one is a commonly used sequence
deep learning model. The results are shown in Fig. 4, as we can
see, for dataset RML2016.10a, SigNet performs signiﬁcantly
better than other models, except the state-of-the-art model
MCLDNN, the performance of these two models is very close
(the accuracy of SigNet on the entire test set is 61.35%, while
that of MCLDNN is 61.16%). And for dataset Sig2019-12,
SigNet performs signiﬁcantly better than all the other models,
especilly when the SNR is below 0dB (the accuracy of SigNet
on the entire test set is 72.69%, while the second best model
MCLDNN is 67.52%). These results indicate that our model
has a better generalization than MCLDNN and has a stable
performance on more datasets.
To compare the classiﬁcation performance of these models
more comprehensively, we visualize the confusion matrices of
the entire test sets in Fig. 5, for the two datasets RML2016.10a
and Sig2019-12, respectively. As we can see, on the dataset
RML2016.10a, 1D-ResNet is more likely to misclassify the
modulation category WBFM as AM-DSB; both 1D-ResNet
and 2D-CNN are more likely to confuse QAM64 and QAM16,
while it seems that both LSTM and SigNet are able to
reduce such confusion to certain extent. All the models may
misclassify WBFM as AM-SSB or AM-DSB and misclassify
all modulation categories as AM-SSB. On the dataset Sig2019-
12, 2D-CNN behaves the worst in many categories, especially
for 2FSK and 4FSK, while the others perform well. The
diagonal of SigNet and MCLDNN’s confusion matrices are
more distinct than the others, especially for OQPSK, 2FSK,
4FSK and 8FSK. LSTM seems close to SigNet, but the latter
has a much higher training efﬁciency, i.e., comparing with
LSTM, SigNet saves 49.58% and 32.40% training time on the
two datasets RML2016.10a and Sig2019-12, respectively.
E. The performance of SigNet2.0
To further accelerate our model, we replace some of the 2D-
convolutional layers with 1D-convolutional layers, and found
that it can slightly increase the classiﬁcation accuracy when the
ratio of 1D-convolutional layers and 2D-convolutional layers
is set appropriately. We tried to replace different numbers
of 2D-convolutional layers with 1D-convolutional layers and
tested the accuracy on the same dataset. For the ResNet50,
we found that when the 2D-convolutional layers of stage1 and
stage2 were replaced with 1D-convolutional layers (as shown
in Fig. 2), the model has the highest accuracy with a certain
acceleration effect, and we call this model SigNet2.0. Com-
paring with SigNet, SigNet2.0 improves 0.95% and 0.18%
accuracy, meanwhile saving 30.65% and 12.46% training time,
on RML2016.10a and Sig2019-12 datasets, respectively.
We conducted a comprehensive evaluation and comparison
of the models mentioned above, including model classiﬁcation
performance, training time and parameter quantity, as shown in
TABLE II. We also used the machine learning toolkit sklearn
to draw the ROC curves of all methods on the multi-class
classiﬁcation results and calculate the AUC value, as shown in
Fig. 6. We can see that some models, such as 1D-ResNet and
2D-CNN, are fast but of relatively low classiﬁcation accuracy;
MCLDNN also has a sightly lower accuracy than SigNet on
the RML2016.10a dataset, although it is lighter and more
efﬁcient. On Sig2019-12 dataset, it performs much poorer
than our SigNet, indicating that our method has the better
generalization ability when the data sample becomes longer.
Among these methods, GAF, MTF and Constellation have
the same amount of trained parameters, but they show great
difference in training time. The ﬁrst reason is that the input size
of Constellation is smaller than GAF and MTF and another
reason is that, for GAF and MTF, due to the storage space
limitation, we use an end-to-end framework to include the
processing of signal samples to matrix and subsequent CNN-
based classiﬁcation in one framework, while for Constellation,
we ﬁrst use the counting method to directly convert the entire
datasets into density matrices, and then input them into CNNs
for classiﬁcation. So, for the training time measurement, there
are two training time measurements for different models. For
GAF and MTF, because the processed training set requires
huge storage space, we choose to perform preprocessing
together with subsequent CNN training, so their training
time includes the time of preprocessing and subsequent CNN
training. For other models, the training time only includes
the training time of the model parameters. Since the training
time of GAF and MTF also includes the time of converting
signals into matrices, they are more time-consuming than other
methods, but their training time is only listed as a reference
and is not used for comparison with that of other methods.
In general, GAF and MTF methods are not ﬂexible enough
in implementation, and the accuracy is worse than that of
SigNet. Compared with other models, our SigNet model has
more parameters, since it is based on ResNet50, which has
a total of 50 convolutional layers. However, our model can
be trained efﬁciently due to the residual structure. Among
all the methods, SigNet2.0 performs the best in classiﬁcation
performance, obtaining the state-of-the-art results, reaching a
good balance between accuracy and efﬁciency.
F. Learning with small samples
There are always real situations that we cannot get enough
signal samples with labels. In reality, collecting labels for
signals may be more expensive than for images, since they
are relatively abstract and thus need a large amount of expert
labors. To validate the effectiveness of our method in such
situations, we also compare SigNet/SigNet2.0 with other state-
of-the-art deep learning models by using only a small fraction

--- Page 8 ---

8
Fig. 3. The comparison results of SigNet/SigNet2.0 and other signal-to-matrix methods. All the methods do the signal classiﬁcation by converting signal to
matrix ﬁrst and then using a typical ResNet50 for classiﬁcation.
Fig. 4. The comparison results of SigNet/SigNet2.0 and other deep learning models.
TABLE II
THE PERFORMANCES OF ALL THE MODELS WE USED.
Dataset
Method
Accuracy
F1 Score
Recall
Training Time
Parameter quantity
RML2016.10a
GAF
49.43%
0.5154
0.4943
3h18m
23.53M
MTF
48.17%
0.5162
0.4818
2h52m
23.53M
Constellation
44.92%
0.4507
0.4493
21m
23.53M
1D-ResNet
57.74%
0.5930
0.5774
26m
0.1M
2D-CNN
54.02%
0.5504
0.5402
21m
2.71M
LSTM
57.20%
0.5877
0.5720
1h56m
0.2M
MCLDNN
61.16%
0.6335
0.6117
53m
0.37M
SigNet
61.35%
0.6354
0.6135
62m
23.53M
SigNet2.0
62.30%
0.6487
0.6226
43m
23.52M
Sig2019-12
GAF
67.31%
0.6714
0.6732
33h24m
23.53M
MTF
65.21%
0.6561
0.6521
43h52m
23.53M
Constellation
41.78%
0.4193
0.4178
1h15m
23.53M
1D-ResNet
64.47%
0.6427
0.6447
50m
0.13M
2D-CNN
41.95%
0.4201
0.4196
1h15m
10.57M
LSTM
66.90%
0.6675
0.6682
19h49m
0.2M
MCLDNN
67.52%
0.6731
0.6738
1h42m
0.37M
SigNet
72.69%
0.7230
0.7228
15h23m
23.53M
SigNet2.0
72.87%
0.7265
0.7228
13h28m
23.52M

--- Page 9 ---

9
Fig. 5. The confusion matrices of ﬁve deep learning models, including 1D-ResNet, 2D-CNN, LSTM, MCLDNN and SigNet, on RML2016.10a (top) and
Sig2019-12 (bottom).
Fig. 6. The ROC curves and AUC values of all methods in RML2016.10a
test set (top) and Sig2019-12 test set (bottom).
η of training set. In particular, for RML2016.10a, we vary
η from 1/600 to 80/600 (about 0.167% to 13.333%), which
means that in the least case, each modulation category’s each
level of SNR only has one sample participates in training,
similarly, for Sig2019-12, the η is from 1/900 to 100/900
(about 0.111% to 11.111%), the classiﬁcation results are show
in Fig. 7.
We ﬁnd that, in general, our SigNet and SigNet2.0 can keep
relatively high accuracy when a small fraction of training set
is adopted: e.g., they achieve 56.94% and 56.63%, respec-
tively for RML2016.10a, and achieve 67.67% and 68.10%,
respectively for Sig2019-12 when less than 15% training set
is adopted; and these numbers are 36.35% and 41.47% for
RML2016.10a, and 44.49% and 44.88% for Sig2019-12 even
when about 1% training set is adopted. By comparison, the
accuracy of the other deep learning models drops very quickly
as the training set gets smaller. Both MCLDNN and LSTM use
the features of sequential neural networks (part of the features
used by MCLDNN is based on LSTM), which may be the
reason for their poor performance in small sample learning on
Sig2019-12. Such results are quite impressive by considering
that these three models have comparable results when the full
training set is adopted. More remarkably, for RML2016.10a,
when each modulation category’s each level of SNR only has
one sample participates in training, SigNet and SigNet2.0 still
have the accuracy above 20% for the both datasets, much
higher than the other three models. These results suggest that
our SigNet and SigNet2.0 have powerful feature extraction
capacity and could be very useful in the situations where the
labeled data are difﬁcult to obtain.
G. A brief ablation study of SigNet
We also conducted a brief ablation study of SigNet’s hyper-
parameters, including batch size, ﬁlter size of S2M and
optimizer. Since we use the learning rate decay strategy of
warm-up cosine annealing, the ablation study of learning rate
has not been taken. The results are shown in Table III. For

--- Page 10 ---

10
Fig. 7. The comparison results of our proposed SigNet/SigNet2.0 and those deep learning models as baselines on small sample learning.
dataset RML2016.10a, when the batch size is set to 128, the
accuracy of the model is the highest, and when the ﬁlter size
changes within a certain range (3, 5, 7, 9), the accuracy is
almost unaffected. For dataset Sig2019-12, within a certain
range, batch size (32, 64, 128) and ﬁlter size (3, 5, 7) have
little effect on the accuracy of the model.
TABLE III
A BRIEF ABLATION STUDY OF SIGNET WITH TEST ACCURACY.
Dataset
BatchSize
FilterSize
Optimizer
Accuracy
RML2016.10a
32
3x3
Adam
60.60%
RML2016.10a
64
3x3
Adam
60.29%
RML2016.10a
128
3x3
Adam
61.35%
RML2016.10a
256
3x3
Adam
59.53%
RML2016.10a
128
3x3
SGD
61.44%
RML2016.10a
128
3x3
Adagrad
60.99%
RML2016.10a
128
3x3
Adadelta
60.98%
RML2016.10a
128
5x5
Adam
60.83%
RML2016.10a
128
7x7
Adam
61.18%
RML2016.10a
128
9x9
Adam
61.20%
Sig2019-12
32
3x3
Adam
72.69%
Sig2019-12
64
3x3
Adam
72.14%
Sig2019-12
128
3x3
Adam
71.93%
Sig2019-12
32
3x3
SGD
69.13%
Sig2019-12
32
3x3
Adagrad
70.12%
Sig2019-12
32
3x3
Adadelta
70.01%
Sig2019-12
32
5x5
Adam
72.20%
Sig2019-12
32
7x7
Adam
72.58%
Sig2019-12
32
9x9
Adam
71.98%
What’s more, we also studied the impact of using different
ResNet structures on the performance of our framework. We
use the hyperparameter settings described in Section III-B
and replace the subsequent ResNet50 structure of S2M with
ResNet18, ResNet34 and ResNet101 respectively, and the
classiﬁcation accuracy is shown in Table IV. We can see
that in general, the changes in the ResNet structure do not
have much impact on the classiﬁcation performance of the
SigNet framework. For RML2016.10a, ResNet50 is better than
other structures, and for Sig2019-12, the simpler structure
ResNet34 performs better than others. And no matter which
ResNet structure is used with S2M, the signal classiﬁcation
performance is much better than other frameworks that use
ResNet, such as GAF, MTF, etc.
TABLE IV
A BRIEF ABLATION STUDY OF SIGNET WITH TEST ACCURACY.
Dataset
Architecture
Accuracy
Parameter
quantity
RML2016.10a
S2M+ResNet18
60.38%
11.17M
RML2016.10a
S2M+ResNet34
60.48%
21.28M
RML2016.10a
S2M+ResNet50
61.35%
23.52M
RML2016.10a
S2M+ResNet101
60.85%
42.52M
Sig2019-12
S2M+ResNet18
72.13%
11.17M
Sig2019-12
S2M+ResNet34
72.52%
21.28M
Sig2019-12
S2M+ResNet50
72.14%
23.52M
Sig2019-12
S2M+ResNet101
72.26%
42.52M
IV. EXPLANATORY VISUALIZATION OF MODELS
In this section, we will visualize the output features of the
six deep learning models proposed by other literature, to see
how these models distinguish signals of different modulations.
In particular, we use t-SNE (t-distributed Stochastic Neigh-
bor Embedding) [15] to map the output features extracted by
the trained model into a two-dimensional space for visual-
ization. Speciﬁcally, we ﬁrst remove the last softmax layer
of the trained deep learning models, and then input the test
dataset to obtain the corresponding output features. After that,
we use the t-SNE technique to reduce the dimension of the
output features for visualization. For the t-SNE technique, the
number of iterations is set to 300, the learning rate is 1000,
the perplexity is 30, and the momentum changes from 0.5 to
0.8.
We compare SigNet/SigNet2.0 with other deep learning
modulation classiﬁcation models through the output feature
visualization. Since the entire test set is too large and compli-
cated for visualization, we only select the data with maximum
SNR (18dB for RML2016.10a and 30dB for Sig2019-12), as
shown in Fig. 8. Note that we also display the classiﬁcation
results by placing confusion matrices on the left side.

--- Page 11 ---

11
Fig. 8. The visualization of test samples of the maximum SNR in the two datasets, i.e., 18dB for RML2016.10a (left) and 30dB for Sig2019-12 (right), by
using the six deep learning models, including 1D-ResNet, 2D-CNN, LSTM, MCLDNN, SigNet, and SigNet2.0 (from top to bottom).
As we can see, the classiﬁcation results are well reﬂected in
the visualization of the output features. When two categories
of data are misclassiﬁed with each other by a model, the
corresponding data points in t-SNE visualization will also
overlap, e.g., the data points of WBFM and AM-DSB in
RML2016.10a. It can be observed that the signals of different
modulation categories have much clearer boundaries by adopt-
ing SigNet/SigNet2.0 and MCLDNN than those by adopting
1D-ResNet, 2D-CNN or LSTM, leading to their much higher
classiﬁcation accuracy, which is consistent with the results
presented in TABLE II.

--- Page 12 ---

12
V. CONCLUSION
In this paper, we proposed a deep learning framework for
signal modulation classiﬁcation, namely SigNet, which ﬁrst
uses a trainable S2M operator to convert the original signal to
a square matrix and then use a typical CNN for classiﬁcation.
Moreover, we integrate 1D convolution operators into SigNet,
so as to propose SigNet2.0 to further improve the classiﬁcation
accuracy and efﬁciency. Comprehensive simulation results
validate the outstanding performance of our models. Quite
impressively, both SigNet and SigNet2.0 give comparable ac-
curacy even when very small training set is adopted, showing
their strong feature extraction capacity. Such results indicate
that our framework could be especially useful in the situations
where labeled signals are difﬁcult to obtain.
In the future, we may try other CNN architectures to further
improve the performance of SigNet. Moreover, we will also
apply our framework to other kinds of signal datasets to
validate its effectiveness in more general cases. We will also
consider that single channel sample may contain multiple
modulations and further adjust our model to single-input
multiple-output to adapt to such a more complex but practical
situation.
REFERENCES
[1] A.
Abdelmutalab,
K.
Assaleh,
and
M.
El-Tarhuni,
“Automatic
modulation classiﬁcation based on high order cumulants and hierarchical
polynomial classiﬁers,” Physical Communication, vol. 21, pp. 10–
18, 2016. [Online]. Available: https://www.sciencedirect.com/science/
article/pii/S1874490716301094
[2] E. Blossom, “Gnu radio: tools for exploring the radio frequency spec-
trum,” Linux journal, vol. 2004, no. 122, p. 4, 2004.
[3] M. Camelo, A. Shahid, J. Fontaine, F. A. P. de Figueiredo, E. De Poorter,
I. Moerman, and S. Latre, “A semi-supervised learning approach towards
automatic wireless technology recognition,” in 2019 IEEE International
Symposium on Dynamic Spectrum Access Networks (DySPAN), 2019,
pp. 1–10.
[4] J. Chen, J. Zhang, X. Xu, C. Fu, D. Zhang, Q. Zhang, and Q. Xuan,
“E-lstm-d: A deep learning framework for dynamic network link predic-
tion,” IEEE Transactions on Systems, Man, and Cybernetics: Systems,
pp. 1–14, 2019.
[5] S. Chen, S. Zheng, L. Yang, and X. Yang, “Deep learning for large-scale
real-world acars and ads-b radio signal classiﬁcation,” IEEE Access,
vol. 7, pp. 89 256–89 264, 2019.
[6] D. Chevitarese, D. Szwarcman, R. M. D. Silva, and E. V. Brazil,
“Seismic facies segmentation using deep learning,” AAPG Annual and
Exhibition, 2018.
[7] O. A. Dobre, “Signal identiﬁcation for emerging intelligent radios: clas-
sical problems and new challenges,” IEEE Instrumentation Measurement
Magazine, vol. 18, no. 2, pp. 11–18, 2015.
[8] K. Greff, R. K. Srivastava, J. Koutn´ık, B. R. Steunebrink, and J. Schmid-
huber, “Lstm: A search space odyssey,” IEEE Transactions on Neural
Networks and Learning Systems, vol. 28, no. 10, pp. 2222–2232, 2017.
[9] A. Gupta and R. K. Jha, “A survey of 5g network: Architecture and
emerging technologies,” IEEE Access, vol. 3, pp. 1206–1232, 2015.
[10] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
recognition,” in Proceedings of the IEEE Conference on Computer Vision
and Pattern Recognition (CVPR), June 2016.
[11] L. Huang, W. Pan, Y. Zhang, L. Qian, N. Gao, and Y. Wu, “Data
augmentation for deep learning-based radio modulation classiﬁcation,”
IEEE Access, vol. 8, pp. 1498–1506, 2020.
[12] M. Kulin, T. Kazaz, I. Moerman, and E. De Poorter, “End-to-end
learning from spectrum data: A deep learning approach for wireless
signal identiﬁcation in spectrum monitoring applications,” IEEE Access,
vol. 6, pp. 18 484–18 501, 2018.
[13] W. Li, Z. Dou, L. Qi, and C. Shi, “Wavelet transform based modula-
tion classiﬁcation for 5g and uav communication in multipath fading
channel,” Physical Communication, vol. 34, pp. 272–282, 2019.
[14] X. Liu, D. Yang, and A. E. Gamal, “Deep neural network architectures
for modulation classiﬁcation,” in 2017 51st Asilomar Conference on
Signals, Systems, and Computers, 2017, pp. 915–919.
[15] L. v. d. Maaten and G. Hinton, “Visualizing data using t-sne,” Journal
of machine learning research, vol. 9, no. Nov, pp. 2579–2605, 2008.
[16] G. J. Mendis, J. Wei-Kocsis, and A. Madanayake, “Deep learning based
radio-signal identiﬁcation with hardware design,” IEEE Transactions on
Aerospace and Electronic Systems, vol. 55, no. 5, pp. 2516–2531, 2019.
[17] A. Mostayed, J. Luo, X. Shu, and W. Wee, “Classiﬁcation of 12-
lead ecg signals with bi-directional lstm network,” arXiv preprint
arXiv:1811.02090, 2018.
[18] T. J. O’Shea, S. Hiteﬁeld, and J. Corgan, “End-to-end radio trafﬁc
sequence recognition with recurrent neural networks,” in 2016 IEEE
Global Conference on Signal and Information Processing (GlobalSIP),
2016, pp. 277–281.
[19] T. J. O’Shea, J. Corgan, and T. C. Clancy, “Convolutional radio mod-
ulation recognition networks,” in Engineering Applications of Neural
Networks, C. Jayne and L. Iliadis, Eds.
Cham: Springer International
Publishing, 2016, pp. 213–226.
[20] T. J. O’shea and N. West, “Radio machine learning dataset generation
with gnu radio,” in Proceedings of the GNU Radio Conference, vol. 1,
no. 1, 2016.
[21] T. J. O’Shea, T. Roy, and T. C. Clancy, “Over-the-air deep learning
based radio signal classiﬁcation,” IEEE Journal of Selected Topics in
Signal Processing, vol. 12, no. 1, pp. 168–179, 2018.
[22] A. Paszke, S. Gross, S. Chintala, G. Chanan, E. Yang, Z. DeVito, Z. Lin,
A. Desmaison, L. Antiga, and A. Lerer, “Automatic differentiation in
pytorch,” 2017.
[23] S. Peng, H. Jiang, H. Wang, H. Alwageed, Y. Zhou, M. M. Sebdani,
and Y. Yao, “Modulation classiﬁcation based on signal constellation
diagrams and deep learning,” IEEE Transactions on Neural Networks
and Learning Systems, vol. 30, no. 3, pp. 718–727, 2019.
[24] Y. Qian, M. Bi, T. Tan, and K. Yu, “Very deep convolutional neural
networks for noise robust speech recognition,” IEEE/ACM Transactions
on Audio, Speech, and Language Processing, vol. 24, no. 12, pp. 2263–
2276, 2016.
[25] S. Rajendran, W. Meert, D. Giustiniano, V. Lenders, and S. Pollin, “Deep
learning models for wireless signal classiﬁcation with distributed low-
cost spectrum sensors,” IEEE Transactions on Cognitive Communica-
tions and Networking, vol. 4, no. 3, pp. 433–445, 2018.
[26] A. Shahid, J. Fontaine, M. Camelo, J. Haxhibeqiri, M. Saelens, Z. Khan,
I. Moerman, and E. D. Poorter, “A convolutional neural network
approach for classiﬁcation of lpwan technologies: Sigfox, lora and ieee
802.15.4g,” in 2019 16th Annual IEEE International Conference on
Sensing, Communication, and Networking (SECON), 2019, pp. 1–8.
[27] K. Triantafyllakis, M. Surligas, G. Vardakis, and S. Papadakis, “Phasma:
An automatic modulation classiﬁcation system based on random forest,”
in 2017 IEEE International Symposium on Dynamic Spectrum Access
Networks (DySPAN), 2017, pp. 1–3.
[28] D. Vuˇci´c, S. Vukoti´c, and M. Eri´c, “Cyclic spectral analysis of
ofdm/oqam signals,” AEU-International Journal of Electronics and
Communications, vol. 73, pp. 139–143, 2017.
[29] M. Walenczykowska and A. Kawalec, “Type of modulation identiﬁcation
using wavelet transform and neural network,” Bulletin of the Polish
Academy of Sciences Technical Sciences, vol. 64, no. 1, pp. 257–261,
2016.
[30] Z. Wang and T. Oates, “Imaging time-series to improve classiﬁcation
and imputation,” arXiv preprint arXiv:1506.00327, 2015.
[31] N. E. West and T. O’Shea, “Deep architectures for modulation recog-
nition,” in 2017 IEEE International Symposium on Dynamic Spectrum
Access Networks (DySPAN), 2017, pp. 1–6.
[32] J. Xu, C. Luo, G. Parr, and Y. Luo, “A spatiotemporal multi-channel
learning framework for automatic modulation recognition,” IEEE Wire-
less Communications Letters, vol. 9, no. 10, pp. 1629–1632, 2020.
[33] Q. Xuan, Z. Chen, Y. Liu, H. Huang, G. Bao, and D. Zhang, “Multiview
generative adversarial network and its application in pearl classiﬁcation,”
IEEE Transactions on Industrial Electronics, vol. 66, no. 10, pp. 8244–
8252, 2019.
[34] Q. Xuan, B. Fang, Y. Liu, J. Wang, J. Zhang, Y. Zheng, and G. Bao,
“Automatic pearl classiﬁcation machine based on a multistream convo-
lutional neural network,” IEEE Transactions on Industrial Electronics,
vol. 65, no. 8, pp. 6538–6547, 2018.
[35] Q. Xuan, J. Wang, M. Zhao, J. Yuan, C. Fu, Z. Ruan, and G. Chen,
“Subgraph networks with application to structural feature space expan-
sion,” IEEE Transactions on Knowledge and Data Engineering, pp. 1–1,
2019.

--- Page 13 ---

13
[36] Y. Zeng, M. Zhang, F. Han, Y. Gong, and J. Zhang, “Spectrum analysis
and convolutional neural network for automatic modulation recognition,”
IEEE Wireless Communications Letters, vol. 8, no. 3, pp. 929–932, 2019.
[37] S. Zheng, S. Chen, L. Yang, J. Zhu, Z. Luo, J. Hu, and X. Yang,
“Big data processing architecture for radio signals empowered by
deep learning: Concept, experiment, applications and challenges,” IEEE
Access, vol. 6, pp. 55 907–55 922, 2018.
[38] S. Zheng, P. Qi, S. Chen, and X. Yang, “Fusion methods for cnn-based
automatic modulation classiﬁcation,” IEEE Access, vol. 7, pp. 66 496–
66 504, 2019.
[39] S. Zheng, S. Chen, and X. Yang, “Deep learning for cooperative radio
signal classiﬁcation,” arXiv preprint arXiv:1909.06031, 2019.
[40] H. Zhou, L. Jiao, S. Zheng, S. Chen, L. Yang, W. Shen, and X. Yang,
“Weight-variable scattering convolution networks and its application in
electromagnetic signal classiﬁcation,” IEEE Access, vol. 7, pp. 175 889–
175 896, 2019.
[41]
¨Ozal Yildirim, “A novel wavelet sequence based on deep bidirectional
lstm network model for ecg signal classiﬁcation,” Computers in
Biology and Medicine, vol. 96, pp. 189–202, 2018. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0010482518300738

```
