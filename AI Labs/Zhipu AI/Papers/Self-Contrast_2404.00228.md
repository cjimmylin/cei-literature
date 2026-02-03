---
title: "Self Contrast 2404.00228"
source_pdf: "AI Labs/Zhipu AI/Papers/Self-Contrast_2404.00228.pdf"
company: "Zhipu AI"
pages: 15
extracted_at: "2026-01-25T04:43:51.353182"
type: "ai_lab_paper"
---

# Self Contrast 2404.00228

**Company/Lab:** Zhipu AI
**Source PDF:** AI Labs/Zhipu AI/Papers/Self-Contrast_2404.00228.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

InfLoRA: Interference-Free Low-Rank Adaptation for Continual Learning
Yan-Shuo Liang and Wu-Jun Li*
National Key Laboratory for Novel Software Technology,
Department of Computer Science and Technology, Nanjing University, P. R. China
liangys@smail.nju.edu.cn,liwujun@nju.edu.cn
Abstract
Continual learning requires the model to learn multi-
ple tasks sequentially.
In continual learning, the model
should possess the ability to maintain its performance on
old tasks (stability) and the ability to adapt to new tasks
continuously (plasticity). Recently, parameter-efficient fine-
tuning (PEFT), which involves freezing a pre-trained model
and injecting a small number of learnable parameters to
adapt to downstream tasks, has gained increasing popular-
ity in continual learning. Although existing continual learn-
ing methods based on PEFT have demonstrated superior
performance compared to those not based on PEFT, most
of them do not consider how to eliminate the interference
of the new task on the old tasks, which inhibits the model
from making a good trade-off between stability and plastic-
ity. In this work, we propose a new PEFT method, called
interference-free low-rank adaptation (InfLoRA), for con-
tinual learning. InfLoRA injects a small number of param-
eters to reparameterize the pre-trained weights and shows
that fine-tuning these injected parameters is equivalent to
fine-tuning the pre-trained weights within a subspace. Fur-
thermore, InfLoRA designs this subspace to eliminate the
interference of the new task on the old tasks, making a good
trade-off between stability and plasticity. Experimental re-
sults show that InfLoRA outperforms existing state-of-the-
art continual learning methods on multiple datasets. Code
is available at https://github.com/liangyanshuo/
InfLoRA.
1. Introduction
Continual learning requires the model to learn multiple
tasks sequentially [33].
To achieve continual learning,
the model should possess two essential abilities, including
the ability to keep its performance on the old tasks (sta-
bility) and the ability to adapt to the new tasks continu-
ously (plasticity) [33]. Furthermore, two different scenar-
*Wu-Jun Li is the corresponding author.
ios are often considered in continual learning, including
task-incremental scenario [32] and class-incremental sce-
nario [41]. Task-incremental scenario allows the model to
get task identities during inference. On the contrary, class-
incremental scenario does not allow the model to get task
identities during inference, making the model learn to dis-
tinguish all the classes across all the tasks.
Recently, parameter-efficient fine-tuning (PEFT) [15, 16,
18], which involves freezing a pre-trained model and in-
jecting a small number of learnable parameters to adapt
to downstream tasks, has gained increasing popularity in
continual learning [12, 38, 44], especially in the class-
incremental scenario.
More specifically, existing contin-
ual learning methods based on PEFT [21, 43] inject the
learnable parameters into a pre-trained model using some
popular PEFT methods such as prompt-tuning [25] or low-
rank adaptation (LoRA) [16]. Subsequently, these methods
freeze the pre-trained weights and sequentially fine-tune the
injected parameters on multiple tasks throughout the contin-
ual learning process.
Although continual learning methods based on PEFT
have demonstrated superior performance compared to those
not based on PEFT [44], most of them do not consider how
to eliminate the interference of the new task on the old tasks,
which inhibits the model from making a good trade-off
between stability and plasticity. Specifically, when learn-
ing a new task, existing continual learning methods based
on PEFT either reuse the previously learned parameters to
adapt to the new task [12, 44] or randomly expand some pa-
rameters first and then adapt to the new task [38, 42, 43].
During this process, the interference of the new task on the
old tasks exists due to the shared parameters between new
and old tasks, which means fine-tuning a pre-trained model
on a new task may interfere with the model’s performance
on the old tasks. As a result, it is hard for the model to make
a good trade-off between stability and plasticity.
In this work, we propose a new PEFT method, called
interference-free low-rank adaptation (InfLoRA), for con-
tinual learning. The contributions of this work are listed as
follows:
1
arXiv:2404.00228v3  [cs.LG]  3 Apr 2024

--- Page 2 ---

• InfLoRA injects a small number of parameters to repa-
rameterize the pre-trained weights and shows that fine-
tuning these injected parameters is equivalent to fine-
tuning the pre-trained weights within a subspace.
• InfLoRA designs this subspace to eliminate the interfer-
ence of the new task on the old tasks, making a good
trade-off between stability and plasticity.
• Experimental results show that InfLoRA outperforms ex-
isting state-of-the-art continual learning methods on mul-
tiple datasets.
2. Related Work and Preliminaries
2.1. Related Work
Parameter-Efficient
Fine-Tuning
Parameter-efficient
fine-tuning (PEFT) methods freeze a pre-trained model and
inject a small number of learnable parameters to adapt to
downstream tasks. In this way, PEFT methods reduce the
inefficiency of full fine-tuning methods which fine-tune all
the parameters of a pre-trained model to learn downstream
tasks. For example, Adapter [15] adds small modules in
different layers of Transformers and only tunes these added
modules to adapt to downstream tasks. Prompt-tuning [25]
and Prefix-tuning [27] insert a set of learnable tokens into
the input of the Transformer layers and only tune these
tokens to adapt to downstream tasks.
Low-rank adapta-
tion (LoRA) [16] reparameterizes the pre-trained weights
with low-rank branches and only tunes these branches to
adapt to the downstream tasks. Although these methods
tune much fewer learnable parameters than full fine-tuning,
they always show comparable or even superior performance
compared with full fine-tuning [11, 16, 31, 45].
Early
PEFT methods focus on natural language processing (NLP).
Recently, PEFT methods have also been proposed for
computer vision (CV). For example, visual prompt tun-
ing (VPT) [18] and AdapterFormer [6] apply prompt-tuning
and Adapter techniques to CV tasks, respectively. Both of
them exhibit comparable performance to full fine-tuning.
Continual Learning Early continual learning was usually
considered in the context of learning from scratch. Three
types of continual learning methods are proposed, includ-
ing regularization-based methods [1, 20, 23, 46], memory-
based methods [2, 3, 7, 28, 39], and expansion-based meth-
ods [17, 26, 35]. Regularization-based methods employ a
penalty loss (regularization) to prevent important parame-
ters of old tasks from changing too much. Memory-based
methods maintain a memory buffer to store information
about old tasks. Expansion-based methods dynamically ex-
pand the model’s architecture for each new task.
Recently, with the advancements of pre-trained mod-
els [9, 10, 13], using pre-trained models for continual learn-
ing has gained increasing popularity. Some continual learn-
ing methods fully fine-tune the pre-trained models [4, 49],
which has been shown to be inefficient. Other methods ex-
plore PEFT methods in continual learning. For instance,
some existing continual learning methods [21, 38, 43, 44]
introduce prompt-tuning in continual learning, achieving
much higher performance than previous methods that learn
from scratch, especially in the class-incremental scenario.
The method in [12] introduces a framework in continual
learning that can be combined with many existing PEFT
methods, such as prompt-tuning, LoRA and Adapter. How-
ever, all these methods do not consider how to eliminate the
interference of the new task on the old tasks, which inhibits
the model from making a good trade-off between stability
and plasticity.
2.2. Preliminaries
We first introduce low-rank adaptation (LoRA) [16], a pop-
ular PEFT method related to our method. Then, we give the
problem definition for continual learning.
Low-Rank Adaptation LoRA [16] is one of the most pop-
ular PEFT methods.
It assumes that the changes of pa-
rameters lie in a low-rank space when the model is fully
fine-tuned on a downstream task. Specifically, for a linear
layer with the input dimension dI and the output dimension
dO, we represent its weight with W dO×dI. Then, LoRA
reparametrizes the pre-trained weight W by expanding a
branch with two matrices, A ∈RdO×r and B ∈Rr×dI.
Typically, r is much smaller than the input dimension dI
and output dimension dO, making A a dimensionality in-
creasing matrix and B a dimensionality reduction matrix.
Finally, LoRA modifies the forward propagation in this lin-
ear layer as e = W h + ABh. Here, h and e denote the
input and output of this layer, respectively. LoRA initializes
A as 0 and initializes B using Gaussian distribution. Dur-
ing the learning of the downstream tasks, LoRA freezes the
pre-trained weight W and only fine-tunes the parameters A
and B.
Problem Definition In continual learning, there is a se-
quence of tasks with different distributions. We define the
task sequence as D = {D1, ..., DT }, where the t-th task
Dt = {(xi,t, yi,t)}nt
i=1. Here, xi,t denotes an input sample
and yi,t denotes its label. The objective of continual learn-
ing is to train a model sequentially on these tasks and ensure
that the model performs well on all of them.
We follow existing continual learning methods [43, 44]
based on PEFT and assume the model is a pre-trained
Vision Transformer (ViT) [10].
Specifically, assume the
model is hΦ(fΘ(·)) where hΦ(·) is the classifier with pa-
rameters Φ and fΘ(·) is the pre-trained ViT backbone with
pre-trained parameters Θ. Similar to existing work [43],
our focus is primarily on the class-incremental scenario,
where task identities are unknown during inference. Fur-
thermore, we concentrate on the exemplar-free setting [43,
51], where no historical data can be fetched for rehearsal.
2

--- Page 3 ---

Pre-trained 
Weights 
! ∈ℝ$%×$'
()
(a) Architecture
(b) Designing Dimensionality Reduc;on Matrix *+
,
❄
❄
-
: Element-Wise Addi;on
❄: Frozen
": Learnable
(+.)
(+
❄
"
……
ℳ+
ℳ+
0
1+
ℳ+
0
1+
ℳ+
0 ∩1+
: Gradient space of new tasks (1+)
: Gradient space of old tasks (ℳ+)
: Residual gradient space (ℳ+0)
*)
❄
*3.)
❄
*+
❄
*+
Figure 1. (a) The architecture of our InfLoRA in a certain linear layer of a Transformer. During the learning of the t-th task, the pre-trained
weight and all the old branches are frozen, and only At is fine-tuned. (b) The pipeline of designing dimensionality reduction matrix Bt.
3. Methodology
Figure 1 (a) illustrates the architecture of our InfLoRA
within a linear layer. Before learning the t-th new task, our
InfLoRA expands a LoRA-like branch, which includes a
dimensionality reduction matrix Bt ∈Rr×dI and a dimen-
sionality increasing matrix At ∈RdO×r. Then, the forward
propagation of this linear layer is modified as
e =W h +
t
X
j=1
AjBjh = Wt−1h + AtBth = Wth.
(1)
Here, Wt = Wt−1+AtBt = W +Pt
i=1 AiBi. Similar to
LoRA, our InfLoRA also initializes dimensionality increas-
ing matrix At as 0. However, different from LoRA, which
employs Gaussian distribution to initialize the dimension-
ality reduction matrix B, our InfLoRA designs the dimen-
sionality reduction matrix Bt before learning the t-th task.
During the learning of the t-th task, InfLoRA fine-tunes At
to learn the new task while keeping the pre-trained weight
W , all the old branches and the matrix Bt frozen. After
learning the t-th tasks, for any given test sample belong-
ing to the learned tasks, the model uses Wt and (1) to infer
its label. This design ensures that our method is compatible
with the class-incremental scenario where task identities are
unknown during inference.
In the following subsections, we first build the relation-
ship between our InfLoRA and the method that fine-tunes
the pre-trained weight.
Specifically, we show that fine-
tuning parameters At is equivalent to fine-tuning the pre-
trained weights W within a subspace spanned by the rows
of Bt. Note that Bt is designed before learning the t-th
task, making this subspace pre-designed. Then, building
upon this relationship, we introduce how our InfLoRA de-
signs this subspace to eliminate the interference of the new
task on the old tasks and make a good trade-off between
stability and plasticity.
3.1. Relationship between InfLoRA and Fine-
Tuning the Pre-Trained Weight
When the t-th task arrives and our method has expanded a
new branch, the forward propagation in this layer can be
represented by (1). At this time, we can prove the following
proposition:
Proposition 1. When learning the t-th task with forward
propagation represented by (1), fine-tuning At is equivalent
to fine-tuning the pre-trained weight W within the subspace
span{bt
1, ..., bt
r}. Here, bt
i (1 ≤i ≤r) denotes the i-th row
vector of Bt.
Proof. When tuning the pre-trained weight W to learn the
t-th task, we can compute the gradient of W based on the
chain rule:
∂L
∂W = ∂L
∂e
∂e
∂W = ∂L
∂e hT .
(2)
Here, L denotes the loss function. At this time, the change
of W can be denoted as ∆W = −α ∂L
∂W , where α is the
learning rate. Then, we can compute the change of the com-
posed matrix Wt = W + Pt
j=1 AjBj:
∆W Wt =[W + ∆W +
t
X
j=1
AjBj] −(W +
t
X
j=1
AjBj)
=∆W = −α ∂L
∂Wt
= −α∂L
∂e hT
(3)
Here, we use ∆W Wt to denote the change of the composed
matrix Wt causing by the change of W .
3

--- Page 4 ---

Similarly, when tuning the expanded weight At, we can
get the gradient of At based on the chain rule:
∂L
∂At
= ∂L
∂e
∂e
∂At
= ∂L
∂e hT BT
t .
(4)
At this time, the change of At can be denoted as ∆At =
−α ∂L
∂At . Then, we can compute the change of the composed
matrix Wt = Wt−1 + AtBt:
∆AtWt =[Wt−1 + (At + ∆At)Bt] −(Wt−1 + AtBt)
=∆AtBt = −α ∂L
∂At
Bt = −α∂L
∂e hT BT
t Bt
=∆W WtBT
t Bt
(5)
Here, we use ∆AtWt to denote the change of the com-
posed matrix Wt causing by the change of At. The fourth
equation in (5) holds because of (4). The fifth equation
in (5) holds because of (2). (5) shows that ∆AtWt is equal
to ∆W Wt multiplying a projection matrix BT
t Bt. Since
BT
t Bt projects each row vector of ∆W Wt into the sub-
space span{bt
1, ..., bt
r}, Proposition 1 holds.
Proposition 1 has demonstrated that using our InfLoRA
to
train
the
model
is
equivalent
to
directly
fine-
tuning the pre-trained weight W within the subspace
span{bt
1, ..., bt
r}. Therefore, before learning the t-th task,
we can design matrix Bt such that learning the t-th task
in the subspace span{bt
1, ..., bt
r} will not interfere with the
performance of the model on the old tasks.
3.2. Eliminating the Interference of the New Task
on the Old Tasks
We first introduce the desired characteristics that InfLoRA
aims to let the subspace span{bt
1, ..., bt
r} have. With these
characteristics, InfLoRA can eliminate the interference of
the new task on the old tasks and make a good trade-off
between stability and plasticity. Then, we introduce how to
design dimensionality reduction matrix Bt so that subspace
span{bt
1, ..., bt
r} has these characteristics.
3.2.1
Desired Characteristics
First, InfLoRA aims to make the subspace span{bt
1, ..., bt
r}
orthogonal to the gradients of all the old tasks. In this way,
according to Proposition 1, the update of InfLoRA, which
can be represented as ∆AtWt, will also be orthogonal to
the gradient of the old tasks. Note that the idea of making
the update for the new task orthogonal to the gradient of
the old tasks to eliminate the interference of the new task
on the old tasks has been proposed in many existing contin-
ual learning methods [30, 36]. However, all these existing
methods are designed for continual learning from scratch,
involving updating all parameters of the model, which is in-
compatible with the setting in PEFT. On the contrary, our
method is a PEFT method, which only tunes the parameters
in At.
Besides eliminating the interference of new tasks on
old tasks,
our InfLoRA further makes the subspace
span{bt
1, ..., bt
r} lie in a subspace that the gradient of the
new task lies in to make a good trade-off between stability
and plasticity. Specifically, existing work [19] has shown
that during fine-tuning, the weight increments of pre-trained
ViT exhibit redundancy in terms of weight rank. There-
fore, the gradients of the new task lie in a low-dimensional
subspace. Our method makes span{bt
1, ..., bt
r} not only or-
thogonal to the gradient of the old tasks but also lie in the
subspace in which the gradients of the new task t lie. By
doing so, our method makes the model’s focus on the new
task when eliminating the interference of the new task on
the old tasks, thereby making a good trade-off between sta-
bility and plasticity. Section 4.2 verifies the effectiveness of
these two characteristics.
3.2.2
Designing Dimensionality Reduction Matrix
InfLoRA first approximates the gradient space of the new
task and old tasks. Here, we use Nt to represent the gradient
space of the new task approximated by InfLoRA. Similarly,
we use Mt to represent the gradient space of previous t −1
old tasks approximated by InfLoRA. We also use M⊥
t to
denote the residual gradient space, which is orthogonal to
the space Mt. Then, in order to meet the characteristics
described in Section 3.2.1, InfLoRA ensures that each row
of Bt lies in Nt ∩M⊥
t . In other words, InfLoRA makes
span{bt
1, ..., bt
r} ⊆Nt ∩M⊥
t .
Existing works [29, 36] have shown that the gradient up-
date of the linear layer lies in the span of the inputs. Please
refer to supplementary material for a detailed explanation of
this proposition. Therefore, InfLoRA uses the input matrix
of the new task t to approximate the gradient space of the
new task. Specifically, InfLoRA computes the input matrix
Ht = [ht
1, ..., ht
n], with each column of Ht representing an
input vector of the t-th task. Then, InfLoRA considers Nt
as the subspace spanned by the columns of matrix Ht.
However, InfLoRA cannot use the input matrix of the
old tasks to approximate the gradient space of the old tasks
since the data from the old tasks is not available when the
model learns the new tasks. Instead, existing methods such
as gradient projection memory (GPM) [36] and dual gra-
dient projection memory (DualGPM) [29] can learn a ma-
trix to preserve information about the gradients of the old
tasks.
InfLoRA incorporates DualGPM to preserve gra-
dient information. With the assistance of DualGPM, the
model can learn either a matrix Mt ∈RdI×kt or a matrix
M ⊥
t
∈RdI×(dI−kt). Here, the columns of Mt contribute
to the orthonormal bases of Mt and the columns of M ⊥
t
contribute to the orthonormal bases of M⊥
t . kt denotes the
4

--- Page 5 ---

dimension of Mt. For detailed information of how Dual-
GPM maintains orthonormal bases Mt or M ⊥
t , please refer
to supplementary material or the original paper [29].
After approximating the gradient space of the new task
and old tasks, InfLoRA gets the component of Nt which
lies in M⊥
t . Specifically, when the model maintains Mt,
InfLoRA performs the operation
ˆ
Ht = Ht −MtM T
t Ht.
(6)
Similarly, when the model maintains M⊥
t , InfLoRA per-
forms the operation
ˆ
Ht = M ⊥
t (M ⊥
t )T Ht.
(7)
Note that when t = 1, Mt is a null space and ˆ
Ht = Ht.
Obviously, each column of ˆ
Ht lies in Nt ∩M⊥
t . How-
ever, since ( ˆ
Ht)T ∈Rn×dI and Bt ∈Rr×dI have differ-
ent shapes, InfLoRA can not directly define Bt as ( ˆ
Ht)T .
Note that n ≫r, InfLoRA uses the principal components
of ( ˆ
Ht)T to set Bt. Specifically, singular value decom-
posotion (SVD) is performed on ( ˆ
Ht)T = VtΣtUt. Then,
InfLoRA designs Bt by
Bt = (Ut)r.
(8)
Here, (Ut)r denotes the rows of Ut corresponding to the
top-r singular values. Figure 1 (b) illustrates the pipeline of
designing matrix Bt.
Note that DualGPM expands subspace Mt and reduces
subspace M⊥
t when the number of tasks increases. Since
InfLoRA constrains the update of the model within the sub-
space Nt ∩M⊥
t
⊆M⊥
t , the space for learning the new
task reduces when the number of tasks increases. How-
ever, by adjusting the approximation error of the gradient
for the old tasks, DualGPM can expand Mt slowly and re-
duce M⊥
t slowly. Therefore, the constraints imposed by
InfLoRA do not excessively affect the model’s learning of
new tasks. Please refer to supplementary material for a de-
tailed explanation.
3.3. Whole Process of InfLoRA
Algorithm 1 outlines the whole process of InfLoRA in con-
tinual learning. When the t-th new task arrives, InfLoRA
first designs Bt through (8) and expands a new branch.
Then, InfLoRA learns the t-th task by fine-tuning the newly
expanded branch. Please note that, based on empirical find-
ings from existing methods [12, 38], we employ the local
cross-entropy (CE) loss as the learning objective, as it usu-
ally performs better than the global CE loss in continual
learning methods based on PEFT. The local CE is the CE
loss constrained to the classes of the current new task, which
can be denoted as
L(Dt) =
1
|Dt|
X
(x,y)∈Dt
Lce(mask(hΦ(fΘ(x))), y).
(9)
Algorithm 1 InfLoRA for Continual Learning
1: Input: The data of different tasks {Dt}T
t=1, a pre-trained ViT
model fΘ(·).
2: Output: Network fΘ(·) with learned parameters Wt.
3: for t in 1 : T do
4:
Design Bt through (8);
5:
Expand a new branch for the t-th task;
6:
for Bt sampled from Dt do
7:
Compute the loss L(fΘ(Bt)) through (9) and update the
parameters;
8:
end for
9:
Preserve the information about the gradient of the t-th task
through DualGPM;
10: end for
Here, mask(·) is a function that filters out the logits of the
old classes and Lce denotes the standard CE loss. After
learning the t-th new task, InfLoRA follows the DualGPM
to preserve the information about the gradient of the t-th
task.
Note that the branch corresponding to the t-th task will
be frozen once the model has learned the t-th task. Since
the expanded branches are linear transformations, we can
integrate the old branches into the pre-trained weight to re-
duce the expanded parameters. Specifically, after learning
the first task, InfLoRA integrates the first branch into the
pre-trained weight and obtains the weight W1 = W +
A1B1. Before learning the t-th new task (t > 1), InfLoRA
maintains the weight Wt−1. After learning the t-th task,
InfLoRA integrates the t-th branch into Wt−1 and obtains
Wt = Wt−1+AtBt. In this way, the parameters in At and
Bt do not need to be maintained in the learning of subse-
quent tasks. Therefore, during the whole learning process,
the number of parameters expanded by InfLoRA equals the
number of parameters in a single branch. Since a single
branch contains (dI + dO)r parameters, the number of pa-
rameters expanded by InfLoRA is (dI + dO)r all the time.
4. Experiments
4.1. Experimental Settings
Datasets and Evaluation Metric Similar to existing con-
tinual learning methods [12, 44] based on PEFT, we use
ImageNet-R [14], CIFAR100 [24], and DomainNet [34]
to train and evaluate the models.
Imagenet-R is gener-
ated through artistic processing of 200 classes from Ima-
geNet [8]. This dataset is introduced to continual learning
by existing work [43] and has become a standard bench-
mark for continual learning methods based on PEFT. CI-
FAR100 is a dataset commonly used in existing continual
learning works.
DomainNet contains 345 classes and is
introduced by some existing works [38, 42] for continual
learning. Following existing continual learning work [38],
5

--- Page 6 ---

Table 1. Results (%) on ImageNet-R. Results are included for 5 tasks, 10 tasks, and 20 tasks. We report results averaged over 5 trials.
Tasks
5
10
20
Method
ACC5 (↑)
ACC5 (↑)
ACC10 (↑)
ACC10 (↑)
ACC20 (↑)
ACC20 (↑)
joint
81.14 ± 0.34
-
81.14 ± 0.34
-
81.14 ± 0.34
-
sequential
58.74 ± 1.28
72.91 ± 0.28
46.07 ± 1.15
62.91 ± 0.68
34.62 ± 0.85
51.15 ± 1.50
L2P [44]
64.13 ± 0.78
68.66 ± 0.41
62.54 ± 0.24
67.98 ± 0.27
57.92 ± 0.28
64.57 ± 0.29
DualPrompt [43]
67.88 ± 0.17
71.16 ± 0.31
65.41 ± 0.52
69.39 ± 0.43
61.00 ± 0.72
65.80 ± 0.67
CODA-P [38]
73.09 ± 0.21
76.91 ± 0.21
71.47 ± 0.35
75.82 ± 0.29
67.28 ± 0.30
72.34 ± 0.17
C-LoRA [37]
75.85 ± 0.31
78.85 ± 0.34
71.89 ± 0.45
75.33 ± 0.28
65.71 ± 0.60
70.63 ± 0.85
LAE [12]
73.84 ± 0.14
77.29 ± 0.45
71.70 ± 0.39
76.71 ± 0.10
66.98 ± 0.35
73.72 ± 0.05
InfLoRA-b5
75.28 ± 0.01
78.95 ± 0.08
74.13 ± 0.18
78.54 ± 0.14
68.41 ± 0.29
74.00 ± 0.50
InfLoRA
77.52 ± 0.37
82.01 ± 0.12
75.65 ± 0.14
80.82 ± 0.24
71.01 ± 0.45
77.28 ± 0.45
we split ImageNet-R into 5, 10, and 20 tasks, with each task
containing 40, 20, and 10 classes. We split CIFAR100 into
10 tasks, and each task constrains 10 classes. We split Do-
mainNet into 5 tasks, and each task contains 69 classes.
Following existing continual learning methods [12, 44],
we evaluate the performance of the model through two pop-
ular metrics, including the final accuracy ACCT and the
averaged accuracy ACCT = 1
T
PT
i=1 ACCi, where T de-
notes the total number of tasks and ACCi is defined as
ACCi = 1
i
i
X
j=1
ai,j.
(10)
Here, ai,j denotes the accuracy of the j-th task once the
model has learned the i-th task.
Baselines We compare our InfLoRA with state-of-the-art
continual learning methods based on PEFT, including learn
to prompt (L2P) [44], DualPrompt [43], continual decom-
posed attention-based prompt (CODA-P) [38], learning ac-
cumulation ensemble (LAE) [12], continual low-rank adap-
tation (C-LoRA) [37].
For LAE, we implement it with
LoRA [16]. Following existing works [12, 38], we also in-
clude two methods without continual learning, joint and se-
quential, in the comparison. Here, joint denotes the method
that learns all the tasks jointly, while sequential denotes the
method that learns all the tasks sequentially without any op-
eration to overcome the forgetting of the model. The accu-
racy of joint can be treated as the accuracy upper-bound and
the accuracy of sequential can be treated as the accuracy
lower-bound.
Architecture and Training Details
We follow existing
works [12, 43] to perform experiments. Specifically, we
use the ViT-B/16 backbone [10] supervised pre-trained on
ImageNet 21K as the pre-trained model.
For all the methods, we follow existing works [12, 38,
44] and use the Adam [22] optimizer with running averages
of gradient and its square (β1 = 0.9, β2 = 0.999). Each
task is trained for 50 epochs on ImageNet-R, 20 epochs on
CIFAR100 and 5 epochs on DomainNet. The batch size
is set to 128 for all the experiments. Since our InfLoRA
shares a similar architecture to LoRA, we follow existing
work [12] and insert the architecture of our InfLoRA in the
key and value of the attention module. Furthermore, ex-
isting method DualPrompt [43] treats the inserted blocks
as hyperparameters and searches for the best positions for
their prompts. On the contrary, we insert the architecture of
InfLoRA for all the Transformer blocks to avoid searching.
We also implement a variant of our method, which inserts
the bottom 5 Transformer blocks like existing methods Du-
alPrompt and CODA-P. We call this variant InfLoRA-b5.
As for the hyperparameter r, we determine its value through
a grid search on a validation dataset.
4.2. Experimental Results
Accuracy Table 1 shows the results of different methods
on ImageNet-R with a different number of tasks. Table 2
shows the results of different methods on CIFAR100 and
DomainNet. We can find that our methods InfLoRA and
InfLoRA-b5 outperform existing continual learning meth-
ods.
Figure 2 shows the variation of the accuracy of different
continual learning methods on ImageNet-R and CIFAR100.
We can find that our method outperforms existing methods
not only at the end of the learning but also throughout the
whole learning process. This indicates that our InfLoRA
eliminates the interference of the new task on the old tasks
and thus the accuracy of our method decreases slower com-
pared to other methods.
Analysis of Expanded Parameters Figure 3 shows the
number of expanded parameters and the accuracy of dif-
ferent methods on ImageNet-R and CIFAR100. For L2P,
DualPrompt and CODA-P, their expanded parameters are
included in the added prompts and corresponding key. For
LAE, its expanded parameters are the inserted LoRA mod-
ules and an additional copy. For C-LoRA, its expanded pa-
rameters are inserted LoRA modules. For our method, the
expanded parameters are Bt and At. The details of comput-
ing the number of expanded parameters for different meth-
6

--- Page 7 ---

Table 2. Results (%) on CIFAR100 and DomainNet. We report results over 5 trials.
Tasks
CIFAR100
DomainNet
Method
ACC10 (↑)
ACC10 (↑)
ACC5 (↑)
ACC5 (↑)
joint
91.92 ± 0.05
-
77.72 ± 0.04
-
sequential
62.18 ± 3.59
80.42 ± 0.23
53.44 ± 1.21
69.09 ± 0.33
L2P [44]
82.48 ± 0.20
87.64 ± 0.25
70.16 ± 0.05
75.60 ± 0.03
DualPrompt [43]
84.42 ± 0.30
90.06 ± 0.07
72.14 ± 0.05
77.71 ± 0.06
CODA-P [38]
86.62 ± 0.11
91.08 ± 0.28
73.23 ± 0.13
78.72 ± 0.07
C-LoRA [37]
82.97 ± 0.47
88.81 ± 0.34
69.34 ± 0.13
75.25 ± 0.11
LAE [12]
84.15 ± 0.10
89.84 ± 0.03
66.85 ± 0.40
75.01 ± 0.17
InfLoRA-b5
87.06 ± 0.25
91.59 ± 0.13
73.26 ± 0.50
78.82 ± 0.34
InfLoRA
86.51 ± 0.73
91.70 ± 0.32
74.53 ± 0.23
79.57 ± 0.57
1
3
5
Number of Tasks
50
60
70
80
90
Accuracy (%)
(a) ImageNet-R (5 Tasks)
L2P
DualPrompt
CODA-P
LAE
C-LoRA
InfLoRA-b5
InfLoRA
1
5
10
Number of Tasks
60
70
80
90
100
Accuracy (%)
(b) ImageNet-R (10 Tasks)
L2P
DualPrompt
CODA-P
LAE
C-LoRA
InfLoRA-b5
InfLoRA
1
10
20
Number of Tasks
60
70
80
90
100
Accuracy (%)
(c) ImageNet-R (20 Tasks)
L2P
DualPrompt
CODA-P
LAE
C-LoRA
InfLoRA-b5
InfLoRA
1
5
10
Number of Tasks
85
90
95
100
Accuracy (%)
(d) CIFAR100
L2P
DualPrompt
CODA-P
LAE
C-LoRA
InfLoRA-b5
InfLoRA
Figure 2. Variation of the performance of different methods during the learning of ImageNet-R and CIFAR100.
ods are given in supplementary material. We can find that
CODA-P and C-LoRA expand much more parameters than
other methods.
Furthermore, our methods InfLoRA and
InfLoRA-b5 expand comparable parameters to L2P, Dual-
Prompt and LAE but perform better than these methods.
Ablation Study We perform experiment to verify the effec-
tiveness of designing dimensionality reduction matrix Bt
by (8). Specifically, we explore three different variants for
designing Bt. The first variant designs Bt randomly us-
ing Gaussian distribution. We call this variant ‘Random
→Bt’. The second variant discards the operation in (6)
or (7) and directly sets ˆ
Ht = Ht. Through this way, this
variant ensures that each row of Bt lies in Nt while ig-
noring M⊥
t . We call this variant ‘Nt →Bt’. The third
variant does not compute the input matrix but initializes Ht
using a Gaussian distribution before applying the operation
in (6) or (7). In this way, this variant ensures that each row
of Bt lies in M⊥
t while ignoring Nt. We call this variant
‘M⊥
t →Bt’. Since our method focuses both M⊥
t and Nt,
we use Nt ∩M⊥
t →Bt to represent our method.
Table 3 shows the results of our method and its variants.
We can find that all these variants fail to perform as well
as our method. To further demonstrate the performance of
different variants, we show the relative accuracy of differ-
ent tasks after the model learns them all in Figure 4. Here,
relative accuracy is the accuracy of different variants mi-
nus the accuracy of our InfLoRA. Note that the last task is
the new task, and the other tasks are old tasks in Figure 4.
As we can see, ‘Random →Bt’ and ‘Nt →Bt’ outper-
0
2
4
Expanded Param (M)
60
70
80
ACC10 (%)
(a) ImageNet-R (10 Tasks)
L2P
DualPrompt
CODA-P
LAE
C-LoRA
InfLoRA-b5
InfLoRA
0
2
4
Expanded Param (M)
85
90
ACC10 (%)
(b) CIFAR100
L2P
DualPrompt
CODA-P
LAE
C-LoRA
InfLoRA-b5
InfLoRA
Figure 3. Variation of the performance of different methods during
the learning of ImageNet-R and CIFAR100.
form ‘M⊥
t →Bt’ on the new task but shows much lower
accuracy than ‘M⊥
t
→Bt’ and our InfLoRA on the old
tasks. This means these two variants fail to eliminate the in-
ference of the new task on the old tasks, making the model
suffer from low stability. On the contrary, ‘M⊥
t
→Bt’
shows the lowest performance on the new task. This means
‘M⊥
t
→Bt’ ignores the plasticity of the model.
Our
method outperforms all the variants on most of the tasks.
This shows that our method can eliminate the interference
of the new task on the old tasks and make a better trade-off
between stability and plasticity than these variants.
Varying the Pre-Trained Model We also follow the exist-
ing method [40] and perform experiments using a ViT-B/16
pre-trained with two different self-supervised methods, in-
cluding DINO [5] and iBOT [50]. All experimental settings,
except for the choice of the pre-trained model, are kept con-
sistent with the details outlined in Section 4.1.
7

--- Page 8 ---

Table 3. Results of different variants on ImageNet-R with a different number of tasks.
Tasks
5
10
20
ACC5 (↑)
ACC5 (↑)
ACC10 (↑)
ACC10 (↑)
ACC20 (↑)
ACC20 (↑)
Random →Bt
72.49 ± 0.38 79.40 ± 0.29
67.38 ± 0.41 76.62 ± 0.06
56.17 ± 0.29 69.24 ± 0.35
Nt →Bt
67.01 ± 0.11 76.09 ± 0.04
57.91 ± 0.30 70.23 ± 0.59
40.73 ± 0.29 59.68 ± 0.52
M⊥
t →Bt
75.94 ± 0.53 80.69 ± 0.27
74.61 ± 0.62 79.67 ± 0.27
68.79 ± 0.42 75.74 ± 0.26
Nt ∩M⊥
t →Bt (InfLoRA)
77.52 ± 0.37 82.01 ± 0.12
75.65 ± 0.14 80.82 ± 0.24
71.01 ± 0.45 77.28 ± 0.45
1
4
7
10
Tasks
−30
−20
−10
0
Relative Accuracy (%)
(a) ImageNet-R (10 Tasks)
Random→Bt
M⊥
t →Bt
Nt →Bt
1
10
19
Tasks
−40
−20
0
Relative Accuracy (%)
(b) ImageNet-R (20 Tasks)
Random→Bt
M⊥
t →Bt
Nt →Bt
Figure 4. Relative accuracy of different tasks. Relative accuracy is
the accuracy of different variants minus the accuracy of InfLoRA.
Table 4. Results (%) of different methods on ImageNet-R (10
tasks) using various self-supervised pre-trained models.
Here,
DINO-1k and iBOT-1k indicate that the ViT is pre-trained on
ImageNet-1k using these respective methods.
Method
ACC10 (↑)
ACC10 (↑)
DINO-1k
L2P [44]
56.71 ± 0.12 63.59 ± 0.21
DualPrompt [43] 60.23 ± 0.42 66.57 ± 0.25
CODA-P [38]
64.02 ± 0.68 71.50 ± 0.42
C-LoRA [37]
63.07 ± 0.36 68.09 ± 0.41
LAE [12]
61.03 ± 0.27 69.89 ± 0.15
InfLoRA-b5
66.16 ± 0.14 73.01 ± 0.17
InfLoRA
68.31 ± 0.28 76.15 ± 0.05
iBOT-1k
L2P [44]
60.80 ± 0.35 66.58 ± 0.28
DualPrompt [43] 63.78 ± 0.38 68.88 ± 0.16
CODA-P [38]
68.02 ± 0.48 74.28 ± 0.47
C-LoRA [37]
68.60 ± 0.07 73.47 ± 0.28
LAE [12]
64.14 ± 0.29 72.59 ± 0.22
InfLoRA-b5
69.72 ± 0.44 76.11 ± 0.13
InfLoRA
71.84 ± 0.09 78.29 ± 0.09
Table 4 shows the results of different methods on
ImageNet-R when using various pre-trained models. Com-
paring these results to those in Table 1, we can find that the
performance of all methods utilizing self-supervised pre-
trained models is lower than the performance of the cor-
responding methods using supervised pre-trained models.
However, our methods still outperform all other methods.
Combining with Classifier Alignment Slow learner with
classifier alignment (SLCA) [48] utilizes feature statistics to
align classifiers, demonstrating superior performance com-
pared to methods without aligned classifiers. Our InfLoRA
can be combined with classifier alignment (CA) to get bet-
ter performance. Specifically, after learning the t-th task
Table 5. Results (%) of different methods on ImageNet-R (10
tasks) and CIFAR100 using classifier alignment (CA) technique.
Method
ACC10 (↑)
ACC10 (↑)
CIFAR100
SLCA [48]
91.06 ± 0.24 93.65 ± 0.19
InfLoRA+CA
91.59 ± 0.08 94.39 ± 0.05
ImageNet-R SLCA [48]
77.34 ± 0.25 81.35 ± 0.16
InfLoRA+CA
79.78 ± 0.25 83.38 ± 0.19
with parameters At and Bt and loss (9), we collect features
Ft = {ri,t}nt
i=1 of the t-th task. Here, ri,t = f(xi,t) de-
notes the features extracted by backbone fΘ(·). Then, mean
and covariance of features for each class are computed and
saved. After that, for each class c the model has seen during
continual learning, S samples are sampled from Gaussian
distribution N(µc, Σc). Here, µc and covariance Σc de-
note the mean and covariance of the class c. Finally, we
align the classifier using standard cross-entropy and these
samples. The details of this experiment are given in supple-
mentary material.
Table 5 shows that our method InfLoRA+CA outper-
forms SLCA. Note that SLCA tunes all the parameters of
the model while our method InfLoRA only tunes the pa-
rameters in At. Therefore, our InfLoRA+CA is much more
efficient than SLCA.
5. Conclusion
In this work, we propose a new method, called interference-
free low-rank adaptation (InfLoRA), for continual learn-
ing.
InfLoRA injects a small number of parameters to
reparameterize the pre-trained weights and shows that fine-
tuning these injected parameters is equivalent to fine-tuning
the pre-trained weights within a subspace.
Furthermore,
InfLoRA designs this subspace to eliminate the interference
of the new task on the old tasks, making a good trade-off
between stability and plasticity. Experimental results show
that InfLoRA outperforms existing state-of-the-art contin-
ual learning methods on multiple datasets.
Acknowledgment
This work is supported by NSFC (No.62192783), Na-
tional Key R&D Program of China (No.2020YFA0713901),
and Fundamental Research Funds for the Central Universi-
ties (No.020214380108).
8

--- Page 9 ---

References
[1] Rahaf Aljundi, Francesca Babiloni, Mohamed Elhoseiny,
Marcus Rohrbach, and Tinne Tuytelaars.
Memory aware
synapses: Learning what (not) to forget. In Proceedings of
the European Conference on Computer Vision, pages 139–
154, 2018. 2
[2] Rahaf Aljundi, Eugene Belilovsky, Tinne Tuytelaars, Lau-
rent Charlin, Massimo Caccia, Min Lin, and Lucas Page-
Caccia. Online continual learning with maximal interfered
retrieval. In Advances in Neural Information Processing Sys-
tems, pages 11849–11860, 2019. 2
[3] Rahaf Aljundi, Min Lin, Baptiste Goujaud, and Yoshua Ben-
gio. Gradient based sample selection for online continual
learning. In Advances in Neural Information Processing Sys-
tems, pages 11816–11825, 2019. 2
[4] Matteo Boschini, Lorenzo Bonicelli, Angelo Porrello, Gio-
vanni Bellitto, Matteo Pennisi, Simone Palazzo, Concetto
Spampinato, and Simone Calderara. Transfer without forget-
ting. In Proceedings of the European Conference on Com-
puter Vision, pages 692–709, 2022. 2
[5] Mathilde Caron, Hugo Touvron, Ishan Misra, Herv´e J´egou,
Julien Mairal, Piotr Bojanowski, and Armand Joulin. Emerg-
ing properties in self-supervised vision transformers.
In
Proceedings of the IEEE/CVF International Conference on
Computer Vision, pages 9650–9660, 2021. 7
[6] Shoufa Chen, Chongjian Ge, Zhan Tong, Jiangliu Wang,
Yibing Song, Jue Wang, and Ping Luo. Adaptformer: Adapt-
ing vision transformers for scalable visual recognition. Ad-
vances in Neural Information Processing Systems, pages
16664–16678, 2022. 2
[7] Aristotelis Chrysakis and Marie-Francine Moens.
Online
continual learning from imbalanced data. In Proceedings of
the International Conference on Machine Learning, pages
1952–1961, 2020. 2
[8] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,
and Li Fei-Fei. Imagenet: A large-scale hierarchical image
database. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, pages 248–255,
2009. 5
[9] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina
Toutanova. BERT: pre-training of deep bidirectional trans-
formers for language understanding. In Proceedings of the
Conference of the North American Chapter of the Associa-
tion for Computational Linguistics, pages 4171–4186, 2019.
2
[10] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,
Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,
Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-
vain Gelly, et al. An image is worth 16x16 words: Trans-
formers for image recognition at scale. In International Con-
ference on Learning Representations, 2021. 2, 6
[11] Chin-Lun Fu, Zih-Ching Chen, Yun-Ru Lee, and Hung-Yi
Lee. Adapterbias: Parameter-efficient token-dependent rep-
resentation shift for adapters in nlp tasks.
In Findings of
the Association for Computational Linguistics, pages 2608–
2621, 2022. 2
[12] Qiankun Gao, Chen Zhao, Yifan Sun, Teng Xi, Gang Zhang,
Bernard Ghanem, and Jian Zhang. A unified continual learn-
ing framework with general parameter-efficient tuning. In
Proceedings of the IEEE/CVF International Conference on
Computer Vision, pages 11449–11459, 2023. 1, 2, 5, 6, 7, 8
[13] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr
Doll´ar, and Ross Girshick. Masked autoencoders are scalable
vision learners. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 16000–
16009, 2022. 2
[14] Dan Hendrycks, Steven Basart, Norman Mu, Saurav Kada-
vath, Frank Wang, Evan Dorundo, Rahul Desai, Tyler Zhu,
Samyak Parajuli, Mike Guo, et al. The many faces of robust-
ness: A critical analysis of out-of-distribution generalization.
In Proceedings of the IEEE/CVF International Conference
on Computer Vision, pages 8340–8349, 2021. 5
[15] Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna
Morrone, Quentin De Laroussilhe, Andrea Gesmundo, Mona
Attariyan, and Sylvain Gelly.
Parameter-efficient transfer
learning for nlp. In Proceedings of the International Con-
ference on Machine Learning, pages 2790–2799, 2019. 1,
2
[16] Edward J Hu, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li,
Shean Wang, Lu Wang, Weizhu Chen, et al. Lora: Low-
rank adaptation of large language models. In International
Conference on Learning Representations, 2022. 1, 2, 6
[17] Steven C. Y. Hung, Cheng-Hao Tu, Cheng-En Wu, Chien-
Hung Chen, Yi-Ming Chan, and Chu-Song Chen. Compact-
ing, picking and growing for unforgetting continual learn-
ing. In Advances in Neural Information Processing Systems,
pages 13647–13657, 2019. 2
[18] Menglin Jia, Luming Tang, Bor-Chun Chen, Claire Cardie,
Serge J. Belongie, Bharath Hariharan, and Ser-Nam Lim. Vi-
sual prompt tuning. In Proceedings of the European Confer-
ence on Computer Vision, pages 709–727, 2022. 1, 2
[19] Shibo Jie and Zhi-Hong Deng.
Fact: Factor-tuning for
lightweight adaptation on vision transformer. In Proceed-
ings of the AAAI Conference on Artificial Intelligence, pages
1060–1068, 2023. 4
[20] Sangwon Jung, Hongjoon Ahn, Sungmin Cha, and Taesup
Moon. Continual learning with node-importance based adap-
tive group sparse regularization. Advances in Neural Infor-
mation Processing Systems, pages 3647–3658, 2020. 2
[21] Muhammad Gul Zain Ali Khan, Muhammad Ferjad Naeem,
Luc Van Gool, Didier Stricker, Federico Tombari, and
Muhammad Zeshan Afzal. Introducing language guidance
in prompt-based continual learning. In Proceedings of the
IEEE/CVF International Conference on Computer Vision,
pages 11463–11473, 2023. 1, 2
[22] Diederik P Kingma and Jimmy Ba. Adam: A method for
stochastic optimization.
arXiv preprint arXiv:1412.6980,
2014. 6
[23] James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel
Veness, Guillaume Desjardins, Andrei A Rusu, Kieran
Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-
Barwinska, et al. Overcoming catastrophic forgetting in neu-
ral networks. Proceedings of the National Academy of Sci-
ences, pages 3521–3526, 2017. 2
9

--- Page 10 ---

[24] A Krizhevsky. Learning multiple layers of features from tiny
images. Master’s thesis, University of Tront, 2009. 5
[25] Brian Lester, Rami Al-Rfou, and Noah Constant. The power
of scale for parameter-efficient prompt tuning. In Proceed-
ings of the Conference on Empirical Methods in Natural
Language Processing, pages 3045–3059, 2021. 1, 2
[26] Xilai Li, Yingbo Zhou, Tianfu Wu, Richard Socher, and
Caiming Xiong. Learn to grow: A continual structure learn-
ing framework for overcoming catastrophic forgetting.
In
Proceedings of the International Conference on Machine
Learning, pages 3925–3934, 2019. 2
[27] Xiang Lisa Li and Percy Liang. Prefix-tuning: Optimizing
continuous prompts for generation. In Proceedings of the
Annual Meeting of the Association for Computational Lin-
guistics, pages 4582–4597, 2021. 2
[28] Yan-Shuo Liang and Wu-Jun Li. Loss decoupling for task-
agnostic continual learning. In Advances in Neural Informa-
tion Processing Systems, 2023. 2
[29] Yan-Shuo Liang and Wu-Jun Li.
Adaptive plasticity im-
provement for continual learning.
In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 7816–7825, 2023. 4, 5, 1, 2
[30] Sen Lin, Li Yang, Deliang Fan, and Junshan Zhang. Trgp:
Trust region gradient projection for continual learning. In In-
ternational Conference on Learning Representations, 2022.
4
[31] Rabeeh Karimi Mahabadi, James Henderson, and Sebastian
Ruder. Compacter: Efficient low-rank hypercomplex adapter
layers. In Advances in Neural Information Processing Sys-
tems, pages 1022–1035, 2021. 2
[32] Marc Masana, Joost Van de Weijer, Bartłomiej Twardowski,
et al.
On the importance of cross-task features for class-
incremental learning.
arXiv preprint arXiv:2106.11930,
2021. 1
[33] German I Parisi, Ronald Kemker, Jose L Part, Christopher
Kanan, and Stefan Wermter. Continual lifelong learning with
neural networks: A review. Neural Networks, pages 54–71,
2019. 1
[34] Xingchao Peng, Qinxun Bai, Xide Xia, Zijun Huang, Kate
Saenko, and Bo Wang. Moment matching for multi-source
domain adaptation. In Proceedings of the IEEE/CVF Inter-
national Conference on Computer Vision, pages 1406–1415,
2019. 5
[35] Andrei A Rusu, Neil C Rabinowitz, Guillaume Desjardins,
Hubert Soyer, James Kirkpatrick, Koray Kavukcuoglu, Raz-
van Pascanu, and Raia Hadsell. Progressive neural networks.
arXiv preprint arXiv:1606.04671, 2016. 2
[36] Gobinda Saha, Isha Garg, and Kaushik Roy. Gradient pro-
jection memory for continual learning. In International Con-
ference on Learning Representations, 2021. 4
[37] James Seale Smith, Yen-Chang Hsu, Lingyu Zhang, Ting
Hua, Zsolt Kira, Yilin Shen, and Hongxia Jin. Continual dif-
fusion: Continual customization of text-to-image diffusion
with c-lora. CoRR, 2023. 6, 7, 8, 2, 4
[38] James Seale Smith, Leonid Karlinsky, Vyshnavi Gutta, Paola
Cascante-Bonilla, Donghyun Kim, Assaf Arbelle, Rameswar
Panda, Rogerio Feris, and Zsolt Kira. Coda-prompt: Contin-
ual decomposed attention-based prompting for rehearsal-free
continual learning. In Proceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition, pages
11909–11919, 2023. 1, 2, 5, 6, 7, 8, 4
[39] Qing Sun, Fan Lyu, Fanhua Shang, Wei Feng, and Liang
Wan.
Exploring example influence in continual learning.
Advances in Neural Information Processing Systems, pages
27075–27086, 2022. 2
[40] Liyuan Wang, Jingyi Xie, Xingxing Zhang, Mingyi Huang,
Hang Su, and Jun Zhu.
Hierarchical decomposition of
prompt-based continual learning: Rethinking obscured sub-
optimality. arXiv preprint arXiv:2310.07234, 2023. 7, 2, 3,
4
[41] Liyuan Wang, Xingxing Zhang, Hang Su, and Jun Zhu. A
comprehensive survey of continual learning: Theory, method
and application. arXiv preprint arXiv:2302.00487, 2023. 1
[42] Yabin Wang, Zhiwu Huang, and Xiaopeng Hong. S-prompts
learning with pre-trained transformers: An occam’s razor for
domain incremental learning. Advances in Neural Informa-
tion Processing Systems, pages 5682–5695, 2022. 1, 5
[43] Zifeng Wang, Zizhao Zhang, Sayna Ebrahimi, Ruoxi Sun,
Han Zhang, Chen-Yu Lee, Xiaoqi Ren, Guolong Su, Vincent
Perot, Jennifer G. Dy, and Tomas Pfister. Dualprompt: Com-
plementary prompting for rehearsal-free continual learning.
In Proceedings of the European Conference on Computer Vi-
sion, pages 631–648, 2022. 1, 2, 5, 6, 7, 8, 4
[44] Zifeng Wang, Zizhao Zhang, Chen-Yu Lee, Han Zhang,
Ruoxi Sun, Xiaoqi Ren, Guolong Su, Vincent Perot, Jennifer
Dy, and Tomas Pfister.
Learning to prompt for continual
learning. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, pages 139–149,
2022. 1, 2, 5, 6, 7, 8, 4
[45] Elad Ben Zaken, Yoav Goldberg, and Shauli Ravfogel. Bit-
fit: Simple parameter-efficient fine-tuning for transformer-
based masked language-models. In Proceedings of the An-
nual Meeting of the Association for Computational Linguis-
tics (Short Papers), pages 1–9, 2022. 2
[46] Friedemann Zenke, Ben Poole, and Surya Ganguli. Contin-
ual learning through synaptic intelligence. In Proceedings
of the International Conference on Machine Learning, pages
3987–3995, 2017. 2
[47] Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin
Recht, and Oriol Vinyals. Understanding deep learning (still)
requires rethinking generalization. Communications of the
ACM, pages 107–115, 2021. 1
[48] Gengwei Zhang, Liyuan Wang, Guoliang Kang, Ling Chen,
and Yunchao Wei. SLCA: slow learner with classifier align-
ment for continual learning on a pre-trained model.
In
Proceedings of the IEEE/CVF International Conference on
Computer Vision, pages 19091–19101, 2023. 8
[49] Zangwei Zheng, Mingyuan Ma, Kai Wang, Ziheng Qin, Xi-
angyu Yue, and Yang You.
Preventing zero-shot transfer
degradation in continual learning of vision-language models.
In Proceedings of the IEEE/CVF International Conference
on Computer Vision, pages 19068–19079, 2023. 2
[50] Jinghao Zhou, Chen Wei, Huiyu Wang, Wei Shen, Cihang
Xie, Alan Yuille, and Tao Kong. Image bert pre-training with
online tokenizer. In International Conference on Learning
Representations, 2022. 7
10

--- Page 11 ---

[51] Fei Zhu, Xu-Yao Zhang, Chuang Wang, Fei Yin, and Cheng-
Lin Liu.
Prototype augmentation and self-supervision for
incremental learning. In Proceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition, pages
5871–5880, 2021. 2
11

--- Page 12 ---

InfLoRA: Interference-Free Low-Rank Adaptation for Continual Learning
Supplementary Material
A. Details of GPM and DualGPM
GPM and DualGPM are established on the fact that the gra-
dient updates lie in the span of input data points [47].
For a linear layer, we denote its forward propagation as
e = W h + b,
(11)
W ∈RdI×dO, h ∈RdI, and e ∈RdO. dI and dO denote
input and output dimension, respectively. We further denote
the loss function as L. Through the chain rule, we can get
the gradient of W :
∂L
∂W = ∂L
∂e
∂e
W = ∂L
∂e hT =


a1hT ,
a2hT ,
...,
adOhT

.
(12)
[a1, a2, ..., adO]T denotes the vector ∂L
∂e . Through (12), we
can find that each column of
∂L
∂W can be represented as in-
put h multiplied by a real value ak (1 ≤k ≤dO). There-
fore, in the linear layer, each column of the gradient
∂L
∂W
lies in the span of input.
A.1. Gradient Projection Memory
GPM learns a subspace Mt with orthogonal bases Mt to
approximate the gradient space of the old tasks. Here, the
columns of Mt contribute a set of orthogonal bases in Mt.
GPM expands the bases of Mt to the bases of Mt+1 after
learning the t-th new task. Specifically, GPM computes the
inputs matrix Ht such that each column of Ht represents
an input of this layer. Then, the part of Ht that has already
in Mt is removed by
ˆ
Ht = Ht −Mt(Mt)T Ht = Ht −Ht,proj.
(13)
Please note that when t = 1, dim(Mt) = 0 and hence
Ht,proj is a zero matrix. After that, singular value decom-
position (SVD) is performed on ˆ
Ht = ˆU ˆΣ ˆV T . Then, u
new orthogonal bases are chosen from the columns of ˆU for
a minimum of u satisfying the following criteria for given
threshold ϵth:
||( ˆ
Ht)u||2
F + ||Ht,proj||2
F ≥ϵth||Ht||2
F .
(14)
Here, ( ˆ
Ht)u = [u1, ..., uu] denotes the components of ˆ
Ht
that correspond to top-u singular values. Then, subspace
Mt+1 is obtained with the bases Mt+1 = [Mt, u1, ..., uu].
A.2. Dual Gradient Projection Memory
Different from GPM that learns a subspace Mt with orthog-
onal bases Mt to approximate the gradient space of the old
tasks, DualGPM either learns a subspace Mt with orthog-
onal bases Mt to approximate the gradient of the old tasks,
or learns a subspace M⊥
t with orthogonal bases M ⊥
t to ap-
proximate orthogonal complement of the gradient space of
the old tasks.
DualGPM decides whether to keep Mt or M ⊥
t in mem-
ory according to dim(Mt) and dim(M⊥
t ). Specifically,
during the learning of the first several tasks, dim(Mt) ≤
dim(M⊥
t ).
At this time, DualGPM maintains Mt, and
expands Mt to Mt+1 after each task.
When dim(Mt)
increases and exceeds dim(M⊥
t ), DualGPM obtains M ⊥
t
through some transformations on Mt. After that, DualGPM
only maintains M ⊥
t in memory, and reduces M ⊥
t to M ⊥
t+1
after each task. Through this way, the number of bases kept
for each layer is min{dim(Mt), dim(M⊥
t )}.
There are three key problems in DualGPM: expanding
the bases of Mt, obtaining the bases of M⊥
t through the
bases of Mt, and reducing the bases of M⊥
t .
Expanding the Bases of Mt
The expansion of Mt is the
same as that in GPM.
Transforming Mt to M⊥
t
DualGPM transforms Mt to
M⊥
t by performing SVD to the matrix Mt. Specifically, let
Mt = UΣV T , the column vectors of U which correspond
to the zero singular values form a set of orthogonal bases
of M⊥
t . Please refer to the paper of DualGPM [29] for this
explanation.
Reducing the Bases of M⊥
t
DualGPM reduces space
M⊥
t by removing the part of M⊥
t which contains the gra-
dient of the t-th task. Specifically, DualGPM first computes
the input matrix Rt. Then, the part of Rt which lies in M⊥
t
can be computed through
ˆR⊥
t = M ⊥
t (M ⊥
t )T Rt = R⊥
t,proj.
(15)
After that, SVD is performed on ˆR⊥
t
= ˆU ⊥ˆΣ⊥( ˆV ⊥)T .
Then, k new orthogonal bases are chosen from the columns
of ˆU ⊥for a maximum of k satisfying the following criteria
for the given threshold ϵth (the same as ϵth in (14)):
||( ˆR⊥
t )k||2
F ≤(1 −ϵth)||Rt||2
F .
(16)
Let Z = ( ˆR⊥
t )k = [u⊥
1 , ..., u⊥
k ], Z = span{u⊥
1 , ..., u⊥
k }.
Here, Z is the subspace of M⊥
t that contains the gradient of
1

--- Page 13 ---

1
5
10
Number of Tasks
0
300
768
dim(M⊥
t )
Variation of the Dimension in Different Layers
layer 1
layer 2
layer 3
layer 4
layer 5
layer 6
layer 7
layer 8
layer 9
layer 10
layer 11
layer 12
Figure 5. Change of the dimension of subspace M⊥
t throughout
the whole learning process.
the t-th task. DualGPM removes Z from M⊥
t to get M⊥
t+1.
Specifically, let
ˆ
M ⊥
t
= M ⊥
t −Z(ZT )M ⊥
t . DualGPM
performs the second SVD on ˆ
M ⊥
t
= eU ⊥eΣ⊥( eV ⊥)T . The
columns of eU ⊥which correspond to the non-zero singular
values form the bases M ⊥
t+1. Please refer to the paper of
DualGPM [29] for this explanation.
A.3. Approximation Error in DualGPM
DualGPM either learns a subspace Mt to approximate the
gradient space of the old tasks or learns a subspace M⊥
t to
represent the orthogonal complement of the gradient of the
old tasks. From Seciton A.2, we can find that the approx-
imation error is related to the hyperparameter ϵth in (14)
and (16). Specifically, when the value of ϵth in (14) and (16)
increases, the approximation error decreases. As a result,
the dimension of subspace Mt becomes larger, while the
dimension of M⊥
t becomes smaller. Note that our InfLoRA
constrains the update of the model to lie within the subspace
Nt ∩M⊥
t ⊆M⊥
t . Therefore, we can adjust the value of
ϵth to adjust the space for learning the new task. Here, for
all the experiments, we set
ϵth = ϵ + (1 −ϵ) ∗t
T
,
(17)
where t denotes the task id and T denotes the total number
of tasks. In other words, we gradually increase the value of
ϵth as the number of tasks increases throughout the whole
learning process. Table 6 shows the setting of ϵ in our In-
fLoRA.
Figure 5 illustrates the variation of the dimension of the
subspace M⊥
t in different Transformer layers of ViT-B/16.
We can find that the dimension of the subspace M⊥
t in
different Transformer layers of ViT-B/16 is always much
larger than zero, which means the space for learning the new
task always exists throughout the whole learning process.
B. More Experimental Details
B.1. Training Details
For all the methods in all the experiments except for the
comparison with SLCA, the batch size is set to 128 to fol-
low many existing continual learning methods based on
PEFT [38, 40].
Hyperparameters for different methods
are selected based on the experimental settings in existing
works [12, 38, 44] or through hyperparameter search. For
example, Adam is used as the optimizer with running av-
erages of gradient and its square (β1 = 0.9, β2 = 0.999).
The learning rate is searched among [5e-4, 1e-3, 2e-3, 1e-2]
for all the methods through the validation sets we split from
the training sets. For the hyperparameter r in our InfLoRA,
we search it among [1, 5, 10, 20, 30] through the valida-
tion sets we split from the training sets. Table 6 shows the
hyperparameters of different methods.
When compared with SLCA, our method is combined
with classifier alignment (CA). At this time, we follow
SLCA to train the expanded LoRA branches and classifiers
using the SGD optimizer. Each task is trained for 50 epochs
on ImageNet-R, 20 epochs on CIFAR100 and 5 epochs on
DomainNet. The batch size is set to 128.
B.2. Expanded Parameters
For L2P [44], the expanded parameters consist of the in-
serted prompts and their corresponding keys. Let d denote
the embedding dimension, e denote the prompt length, p
denote the number of prompts, and l denote the number
of layers in which prompts are inserted. To compute the
total number of expanded parameters, the formula used is
dlp(e + 1).
For DualPrompt [43], the expanded parameters also
consist of the inserted prompts and corresponding keys.
However, DualPrompt contains expert prompts and shared
prompts. Let d denote the embedding dimension, T denote
the number of tasks, eE denote the expert prompt length, eS
denote the shared prompt length, lE denote the number of
layers in which expert prompts are inserted and lS denote
the number of layers in which shared prompts are inserted.
To compute the total number of expanded parameters, the
formula used is d[TlE(eE + 1) + eSlS].
For CODA-Prompt [38], the expanded parameters con-
sist of the inserted prompts, corresponding keys and atten-
tion parameters. Let d denote the embedding dimension, e
denote the prompt length, p denote the number of prompts,
and l denote the number of layers in which prompts are in-
serted. To compute the total number of expanded parame-
ters, the formula used is dlp(e + 2).
For LAE [12], we implement it with LoRA. There-
fore, the expanded parameters in this method consist of the
inserted LoRA modules and the corresponding ensemble
modules. Let d denote the embedding dimension, r denote
the rank, and l denote the number of layers in which LoRA
modules are inserted. Since LAE inserts LoRA modules
into key and value projection in multi-head attention, the
number of expanded parameters is 8ldr.
For C-LoRA [37], the expanded parameters in this
2

--- Page 14 ---

Table 6. List of hyper-parameters for different methods. The meaning of different hyperparameters is given in Section B.2. The hyperpa-
rameter ϵ in InfLoRA is explained in Section A.3
Methods
Hyper-Parameters
L2P
lr: 0.001 (ImageNet-R, DomainNet, CIFAR100)
l: 1 (ImageNet-R, DomainNet, CIFAR100)
p: 30 (ImageNet-R, DomainNet, CIFAR100)
e: 20 (ImageNet-R, DomainNet, CIFAR100)
DualPrompt
lr: 0.001 (ImageNet-R, DomainNet, CIFAR100)
lE: 3 (ImageNet-R, DomainNet, CIFAR100)
lS: 2 (ImageNet-R, DomainNet, CIFAR100)
eE: 20 (ImageNet-R, DomainNet, CIFAR100)
eS: 6 (ImageNet-R, DomainNet, CIFAR100)
CODA-P
lr: 0.001 (ImageNet-R, DomainNet, CIFAR100)
l: 5 (ImageNet-R, DomainNet, CIFAR100)
p: 100 (ImageNet-R, DomainNet, CIFAR100)
e: 8 (ImageNet-R, DomainNet, CIFAR100)
LAE
lr: 0.001 (ImageNet-R, DomainNet, CIFAR100)
r: 5 (ImageNet-R, DomainNet, CIFAR100)
C-LoRA
lr: 0.001 (ImageNet-R, DomainNet, CIFAR100)
r: 64 (ImageNet-R, DomainNet, CIFAR100)
λ: 0.5 (ImageNet-R, DomainNet, CIFAR100)
InfLoRA-b5
lr: 0.001 (CIFAR100), 0.0005 (ImageNet-R, DomainNet)
r: 10 (ImageNet-R, CIFAR100), 20 (DomainNet)
ϵ: 0.99 (ImageNet-R), 0.95 (CIFAR100, DomainNet)
InfLoRA
lr: 0.0005 (ImageNet-R, DomainNet, CIFAR100)
r: 10 (ImageNet-R, DomainNet, CIFAR100)
ϵ: 0.98 (ImageNet-R), 0.95 (CIFAR100, DomainNet)
method consist of the inserted LoRA modules. Let d denote
the embedding dimension, r denote the rank, and l denote
the number of layers in which LoRA modules are inserted.
Since C-LoRA inserts LoRA modules into query, key and
value projection in multi-head attention, the number of ex-
panded parameters is 6ldr.
For our methods, since we integrate the branches of the
old tasks when the model learns a new task, the number of
expanded parameters equals the number of parameters in a
single branch. Let d denote the embedding dimension, r
denote the rank, and l denote the number of layers in which
our InfLoRA modules are inserted. Since we also insert
InfLoRA modules into key and value projection in multi-
head attention, the number of expanded parameters is 4ldr.
C. More Experimental Results
C.1. Compare with More Methods
We compare with SeqLoRA, which initials LoRA modules
and finetunes these modules on multiple tasks sequentially
without any operation to overcome forgetting. The results
are given in Table 7, Table 8 and Table 9. We can find that
our method outperforms this method.
A recent continual learning PEFT method hierarchical
decomposition prompt (HiDe-Prompt) [40] proposes to per-
form continual learning hierarchically. This method main-
tains a set of task-specific prompts for each task and con-
tains two stages during training and inference. Specifically,
given an input sample, Hide-Prompt infers the prompt in-
dex and then uses the corresponding prompt to infer its la-
bel. We also compare our method with this method, and the
results are also given in Table 7, Table 8 and Table 9. We
can find that our method outperforms this method. Further-
more, this method shows comparable performance to our
method in terms of final accuracy ACCT on ImageNet-R.
However, there is a notable gap between this method and
our method in terms of averaged accuracy ACCT . Note
that averaged accuracy ACCT is more important than final
accuracy ACCT since ACCT represents the performance
of the model over the whole learning process.
C.2. Hyperparameter Analysis
We perform the hyperparameter analysis for our method
InfLoRA. There are two specific hyperparameters in our
3

--- Page 15 ---

Table 7. The comparison between our InfLoRA and more methods on ImageNet-R.
Tasks
5
10
20
Method
ACC5 (↑)
ACC5 (↑)
ACC10 (↑)
ACC10 (↑)
ACC20 (↑)
ACC20 (↑)
SeqLoRA
70.96 ± 0.25
79.14 ± 0.32
64.32 ± 0.09
74.78 ± 0.29
56.98 ± 0.29
69.29 ± 0.26
HiDe-Prompt [40]
76.82 ± 0.91
77.19 ± 0.34
75.06 ± 0.12
76.60 ± 0.01
66.88 ± 1.29
76.71 ± 0.23
InfLoRA
77.52 ± 0.37
82.01 ± 0.12
75.65 ± 0.14
80.82 ± 0.24
71.01 ± 0.45
77.28 ± 0.45
Table 8. The comparison between our InfLoRA and more methods
on DomainNet.
ACC5 (↑)
ACC5 (↑)
SeqLoRA
71.69 ± 0.13
78.68 ± 0.12
HiDe-Prompt [40]
71.48 ± 0.10
76.15 ± 0.05
InfLoRA
74.53 ± 0.23
79.57 ± 0.57
Table 9. Results (%) of different methods on ImageNet-R (10
tasks) using various self-supervised pre-trained models.
Here,
DINO-1k and iBOT-1k indicate that the ViT is pre-trained on
ImageNet-1k using these respective methods.
Method
ACC10 (↑)
ACC10 (↑)
DINO-1k
SeqLoRA
60.67 ± 0.11 66.29 ± 0.21
HiDe-Prompt [40] 68.11 ± 0.18 71.70 ± 0.01
InfLoRA
68.31 ± 0.28 76.15 ± 0.05
iBOT-1k
SeqLoRA
66.87 ± 0.40 71.80 ± 0.28
HiDe-Prompt [40] 71.33 ± 0.21 73.62 ± 0.13
InfLoRA
71.84 ± 0.09 78.29 ± 0.09
0
20
r
70.0
72.5
75.0
77.5
80.0
A10 (%)
(a) ImageNet-R
InfLoRA-b5
InfLoRA
0.90
0.95
ϵ
72
74
A10 (%)
(b) ImageNet-R
InfLoRA-b5
InfLoRA
Figure 6. (a) Analysis of the hyperparameter r. (b) Analysis of the
hyperparameter ϵ.
method InfLoRA. The first hyperparameter is r, which con-
trols the expanded parameters in InfLoRA. The second hy-
perparameter is ϵ, which is not the specific hyperparameter
of our InfLoRA but the hyperparameter introduced by Du-
alGPM. This hyperparameter controls the component main-
tained in the matrix Mt.
Figure 6 shows the results of our method with different
values of r or ϵ. We can find that the performance of In-
fLoRA increases first and then decreases with the increase
of r and ϵ.
Table 10. Results of DomainNet for domain incremental setting.
Method
ACC6 (↑)
ACC6 (↑)
L2P [44]
34.15 ± 0.10
49.84 ± 0.03
DualPrompt [43]
35.24 ± 0.12
48.44 ± 0.13
CODA-P [38]
56.89 ± 0.04
57.56 ± 0.03
C-LoRA [37]
44.96 ± 0.01
52.95 ± 0.08
InfLoRA
68.44 ± 0.04
67.46 ± 0.03
ImageNet-R (10 Tasks)
CIFAR100
DomainNet
Datasets
0.2
0.4
0.6
0.8
1.0
Time (s)
Inference Time
L2P
DualPrompt
CODA-P
LAE
InfLoRA-b5
InfLoRA
Figure 7. The time of inferring one task for different methods.
C.3. Domain Incremental Setting
InfLoRA can be extended to the domain incremental set-
ting. Specifically, DomainNet contains six domains and In-
fLoRA can learn on these domains sequentially. Table 10
shows that InfLoRA outperforms other baselines.
C.4. Inference Efficiency
Existing methods often involve multiple forward propa-
gations through the pre-trained backbone.
Specifically,
prompt-based continual learning methods, including L2P,
DualPrompt, and CODA-P, require an extra forward propa-
gation to generate instance-specific prompts. LAE requires
an extra forward propagation for ensembling. In contrast,
our InfLoRA only requires a single forward propagation
through the pre-trained backbone. Figure 7 provides a com-
parison of the time consumed by different methods during
inference. We can find that our method consistently outper-
forms existing methods in terms of time efficiency.
4

```
