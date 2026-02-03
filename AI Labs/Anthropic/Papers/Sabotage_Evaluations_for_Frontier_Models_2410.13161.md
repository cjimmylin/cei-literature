--- Page 1 ---

Non-Perturbative Trivializing Flows for Lattice Gauge Theories
Mathis Gerdes∗
Institute of Physics, University of Amsterdam
Pim de Haan
CuspAI
Roberto Bondesan
Department of Computing, Imperial College London
Miranda C. N. Cheng†
Institute of Physics, University of Amsterdam
Institute for Mathematics, Academia Sinica, Taiwan and
Korteweg-de Vries Institute for Mathematics, University of Amsterdam
Continuous normalizing flows are known to be highly expressive and flexible, which allows for
easier incorporation of large symmetries and makes them a powerful computational tool for lattice
field theories. Building on previous work, we present a general continuous normalizing flow architec-
ture for matrix Lie groups that is equivariant under group transformations. We apply this to lattice
gauge theories in two dimensions as a proof of principle and demonstrate competitive performance,
showing its potential as a tool for future lattice computations.
CONTENTS
I. Introduction
1
II. Gauge Equivariant Continuous Flows
2
A. Ordinary Differential Equations on Lie
Groups
3
B. Adjoint Sensitivity Method
3
C. Numerical Integration
4
D. Lattice Gauge Theory Flow
4
III. Numerical Experiments
5
A. Single-Variable Conjugation Equivariant
Flows
5
B. Pure Gauge Theory in Two Dimensions
6
1. Flows on SU(2) lattices
6
2. Flows on SU(3) lattices
7
IV. Outlook
7
Acknowledgments
7
A. Adjoint Sensitivity Method
7
1. Lie-Algebra Valued Adjoint State
8
B. Gradient Implementation
9
1. Gradients and Divergence of Loops
9
C. Computational Cost of the Divergence
10
D. Implementation of the Crouch-Grossman Runge
Kutta integration method
10
∗m.gerdes@uva.nl
† On leave from CNRS, France.
E. Haar Measure and Sampling
11
1. Haar Measure for Matrix Lie Groups
11
2. Sampling from the Haar Distribution
11
3. Haar Measure for SU(3)
11
F. Markov Chain Monte Carlo & Observables
11
References
13
I.
INTRODUCTION
Lattice gauge theory is a cornerstone of theoretical
physics, providing non-perturbative insights into quan-
tum field theories such as Quantum Chromodynamics
(QCD). Traditional computational methods like Markov
Chain Monte Carlo (MCMC) [1] suffer from critical slow-
ing down near phase transitions and in the continuum
limit, leading to significant computational challenges [2].
Normalizing flows are machine learning models that
produce samples from a target distribution by learning a
bijective transformation between an easy-to-sample dis-
tribution and the target [3].
They have emerged as a
fundamental approach to computing observables in lat-
tice field theory, promising to accelerate computations by
improving sampling efficiency and reducing autocorrela-
tion times [4]. See [5, 6] for an overview.
Explicitly preserving symmetries is crucial in design-
ing efficient samplers based on normalizing flows. This
is because symmetries allow one to restrict the class of
possible bijective transformations to be learned, thereby
reducing the sample complexity of the task.
The im-
portance of symmetries is especially pronounced when
simulating lattice gauge theories, where the size of the
gauge symmetry group grows rapidly with the lattice size.
arXiv:2410.13161v2  [hep-lat]  19 Dec 2025


--- Page 2 ---

2
Given their high design flexibility, continuous-time nor-
malizing flows [7] are a promising framework. This is to
be contrasted with discrete flows [4, 8], where a partition
of the lattice, with a partial breaking of the translation
symmetry as a result, is required. For instance, in [9, 10]
continuous-time flows equivariant to spatial symmetries
have been developed for scalar field theories with ϕ4 cou-
pling, reaching higher performance than their discrete-
time counterpart.
Other contexts in which continuous
normalizing flows play a role in physics sampling include
[11]. In the following, we shall simply refer to continuous-
time flows as continuous flows and discrete-time flows as
discrete flows.
For gauge theories, discrete normalizing flows, such
as those employing residual networks [12–14] and cou-
pling layers [8], have been developed to respect gauge
symmetries.
In view of the above-mentioned benefits,
it is desirable to explore continuous realizations of nor-
malizing flows for lattice gauge theories. Exactly such
a method was theoretically proposed by L¨uscher in the
name of “trivializing maps” for gauge theories in the
foundational work [15], before the advent of the modern
machine learning technology. In particular, the L¨uscher
flow is driven by a potential that is assumed to admit a
perturbative expansion in flow time. The specific Ansatz
of the L¨uscher flow then dictates that this perturbative
expansion in flow time is also a perturbative expansion in
the inverse coupling constant β (see (15)). In particular,
it has the form ˜S = β P
k( βt
6 )k ˜S(k), where ˜S(k) is inde-
pendent of β. Following this idea, a machine learning-
enhanced implementation of such a trivializing flow was
recently reported in [16], showing promising results in
sampling quality. While effective, this approach did not
make full use of the general expressive power of neural
networks, constraining itself instead to a specific form of
expansion closely following L¨uscher’s original idea.
Building on these developments, we present a flexible
and fully equivariant framework for continuous normaliz-
ing flows for lattice gauge theories. The goal of continu-
ous flows is to learn the vector field driving the field trans-
formation such that the endpoint of the flow gives a good
approximation of the target density, in this case given in
terms of the action. In contrast to the original Ansatz
of L¨uscher’s, the time dependence of the vector field in
our flow is not constrained to be polynomial. Moreover,
while retaining equivariance, we do not constrain the vec-
tor field to be given by the gradient of a scalar potential.
Most importantly, our framework allows for general neu-
ral network architectures parameterizing the vector field,
leading to more expressive machine-learning models. As
a result, the vector field can in principle be an arbitrary
function of the field configuration, limited only by the
particular choice of architecture which has to be made in
consideration of computational efficiency.
In particular, our framework includes the flow of
L¨uscher [15] and its machine learning implementation
[16] as special cases.
The additional flexibility of our
framework gives us the freedom to choose a more or less
complex neural network, as appropriate for the given ap-
plication, balancing the trade-off between expressiveness
and computational cost.
A feature of neural ODE allowing for efficient gradient
computations is the adjoint sensitivity method, which we
implemented in a general way. This approach allows for
automatic differentiation and memory-efficient gradient
computation for an arbitrary neural network architec-
ture. This is combined with Crouch-Grossman Runge-
Kutta integration schemes that can simultaneously pro-
cess scalar and matrix group-valued degrees of freedom,
ensuring numerical stability. Our implementation can be
straightforwardly applied to any related integration prob-
lem involving real numbers and matrix groups, and any
loss functions.
We used this framework to construct a novel contin-
uous normalizing flow model for lattice gauge theories.
Our method achieves state-of-the-art effective sample size
– a metric quantifying the efficiency of the sampler –
when benchmarked on sampling two-dimensional SU(2)
and SU(3) lattice gauge theories. The integration and
Lie group infrastructure developed for this study forms
part of the broader flow library bijx [17]. Numerical data
for the figures can be found at [18].
II.
GAUGE EQUIVARIANT CONTINUOUS
FLOWS
The aim of normalizing flows is to approximate samples
from a target distribution, which in the present context
is given in terms of the actions S as
p(U) = e−S(U)
Z
,
(1)
where the partition function Z is a normalization con-
stant. U is a random variable that for lattice gauge the-
ories takes value in SU(N)|E| with the number of edges is
given by |E| = Ldd for a periodic square lattice with side
length L in each of the d dimensions. To sample from
p, we initially draw samples U ∼ρ(U) from an easy-to-
sample distribution, which we choose that associated to
be the Haar measure DU. One then applies a bijective
map U 7→U ′ = Φ(U) to obtain the output samples.
This change of variables induces a probability distribu-
tion q(U ′) on the proposed samples U ′.
To train the
normalizing flow, crucially without having reliable sam-
ples from the target distribution, we minimize the reverse
Kullback-Leibler (KL) divergence
Z
DU q(U) log
q(U)
p(U)

= log Z + EU∼qL(U) ,
(2)
where
L(U) = log q(U) + S(U)
(3)
which we refer to as our loss function.
Note that the
partition function is a constant, and therefore drops out


--- Page 3 ---

3
when computing the gradient with respect to the network
parameters, and that we only need to generate samples
from the model q and not the target distribution p. In
practice, we will not be able to obtain a global minimum
of the loss. We use the flow as the proposal distribution in
a Metropolis-Hasting algorithm that guarantees asymp-
totic exactness of the sampling process[4], in importance
sampling [19], or in conjunction with Hamiltonian Monte
Carlo [20].
Continuous normalizing flows define the map Φ as
the solution to an ordinary differential equation (ODE),
whose vector field is given by a neural network. In con-
trast to discrete flows, any sufficiently regular ODE is
always invertible, and the change of density can be easily
computed if the divergence of the vector field is numeri-
cally tractable. This approach leads to highly expressive
architectures that can be made to manifestly respect the
symmetries of the target theory, leading to higher param-
eter efficiency.
In the following, we will present architectures for gauge
equivariant normalizing flows that achieve state-of-the-
art performance on two-dimensional pure gauge theory
for both SU(2) and SU(3). We will first introduce the
necessary notations and background in the following sec-
tion. For simplicity, we will initially suppress the edge
index and consider a single copy of SU(N) (or a matrix
Lie group G more generally), as the statements can be
easily generalized to the lattice setup.
A.
Ordinary Differential Equations on Lie Groups
Let G be a matrix Lie group and g the corresponding
Lie algebra. In the following, we will focus on the case
G = SU(N), but most of the results straightforwardly
apply to any matrix Lie group.
Any tangent vector V ∈TUG at the point U ∈G
can be decomposed in terms of a Lie algebra element
Z ∈g as V = ZU. Consequently, a neural ODE on G
is defined in terms of a neural network Zθ : G × R →g,
with parameters θ, as
˙U(t) = Zθ(U, t)U(t) .
(4)
The Lie algebra g = su(N) is spanned by a set of basis
vectors {Ta}N 2−1
a=1 , as SU(N) has dimensionality N 2 −1.
For instance, for G = SU(2) we use Ta = iσa, where σa
are the Pauli matrices, while for G = SU(3) we use Ta =
iλa, where λa are the Gell-Mann matrices.
Requiring
these vectors to form an orthonormal basis, the metric is
fixed to have the normalization
⟨A, B⟩= −tr(AB)/2 .
(5)
Correspondingly, a basis for tangent space TUG at the
point U is given by {TaU}a.
We can define the directional derivative of a function
f : G →R as
∂af(U) = d
dt

t=0 f
 etTaU

.
(6)
The gradient of f, which yields a tangent vector at U, is
then given as
∇f(U) =
X
a
∂af(U) TaU .
(7)
Consider now the situation when the initial point
U(0) ∈G is sampled from a certain distribution q0 on
G, and evolves following the ODE of equation (4) up to
time T.
The resulting distribution qT of U(T), incor-
porating the change of density induced by the flow, also
solves an ODE.
Denoting the log-likelihood as L(t, U) = log qt(U)
and writing the right-hand side of the ODE (4) as
Zθ(U, t)U(t) = P
a Za
θ (t, U)TaU(t), we have [21, 22]
L(T, U) = L(0, U) −
Z T
0
∇· ˙U(t, U) dt ,
(8)
where the divergence can be computed using the Lie al-
gebra basis as
∇· ˙U(t, U) =
X
a
∂aZa
θ (t, U) .
(9)
In the form of an ODE, this is
˙L = −∇· ˙U(t, U) .
(10)
In the application in lattice gauge theories, U will be
replaced by a collection of group elements {Ue}e, one for
each edge of the lattice.
B.
Adjoint Sensitivity Method
The adjoint sensitivity method is a way of comput-
ing gradients through the solution of an ODE. Below
we will give a general version of the adjoint sensitivity
method. The generality of the mathematical equations
(11) and (12) here is reflected in our implementation
of the method, which can be used for any loss and on
any manifold as long as it can be embedded in Cn. We
also record the explicit form this takes in equations (13)
and (14) for the special case of integrating on matrix Lie
groups with the KL divergence loss, as they are relevant
for the lattice gauge theory application in the context of
normalizing flows. Further details and explanations as
well as the derivation of the specialized expressions can
be found in the Appendix A, and alternative treatments
can be found in [16, 23, 24].
For a general flow on a manifold M given by the ODE
˙z = fθ(z), z ∈M, the gradient of the loss L(z(T)) given
a fixed initial value z(0) can be computed using
dθL(z(T)) = −
Z 0
T
a(t) ◦dθfθ(t, z(t)) dt ,
(11)
by integrating backwards from T. This uses the auxiliary
adjoint state a(t), which is formally a cotangent vector


--- Page 4 ---

4
(0)
(1)
(2)
(3)
(4)
(5)
(6)
(7)
FIG. 1. Loops used in the ODE architecture. The first two loops, highlighted in red, are used for the non-linear superposition
function. The anchor in the dual lattice is displayed as a dot.
of M. It is initialized as a(T) = dzL

z(T ) and solved for
simultaneously using
˙a(t) = −a(t) ◦dzfθ

z(t) .
(12)
Here, we have used the more abstract notation from dif-
ferential geometry. See for instance [25] for an introduc-
tion for physicists. In particular, for φ : M →M′, dφ
denotes the corresponding differential map dφx : TxM →
Tφ(x)M′ on the tangent spaces, “◦” denotes the compo-
sition of maps, and we routinely treat a cotangent vector
v ∈T ∗
xM as a map v ∈TxM →R.
For our particular problem, the adjoint state can be
reduced to an element of the Lie algebra (i.e. for SU(N)
embedded in Cn as a skew-symmetric traceless matrix),
that follows the ODE
˙A = [Z, A] + ∇(∇· ˙U)U −1 −
X
a
Aa(∇Za)U −1 .
(13)
Again, it is initialized as Aa(T) = ∂aL(U(T)), where we
have specified to the loss L from (3), with q = qT the
distribution at time T. After solving the ODE for A, the
gradient of the loss is computed as
∂θL(U(T)) = −
Z 0
T
 
⟨A(t), ∂θZ⟩−
X
a
∂θ∂aZa
!
dt .
(14)
A derivation of this from the general statement above can
be found in the appendix.
C.
Numerical Integration
Central to implementing the continuous flows for gauge
theories is to define an integration scheme that works si-
multaneously for Lie group and scalar-valued degrees of
freedom. The former is required for the field configura-
tions themselves, while the latter arises for the proba-
bility densities as well as the gradients with respect to
parameters in the adjoint sensitivity method. In princi-
ple, the adjoint state additionally introduces the tangent
space, which we could identify as a Lie algebra element
and treat separately. However, for our implementation
we treat it simply as an element of the ambient complex
space.
In principle, the Lie group elements themselves could
also be treated as elements of the ambient space. How-
ever, a discrete integration scheme would inevitably re-
sult in paths leaving the target manifold. Including pro-
jection steps could address this, but the need to reli-
ably estimate the change of density makes this naive ap-
proach unwieldy.
We, therefore, implement a Crouch-
Grossmann Runge-Kutta method [26, 27], which can be
defined for any matrix group and result in paths that re-
main in the desired submanifold up to numerical error.
The algorithm is briefly outlined with further technical
details in section D of the appendix.
D.
Lattice Gauge Theory Flow
In this section, we describe in some detail our choice for
the neural vector field. In pure gauge theories on the lat-
tice with gauge group G and square lattice VL ∼= (Z/LZ)d
with oriented edges connecting the adjacent vertices, the
field configuration consists of Ue ∈G for each edge e.
Reversing the direction of the edge gives U−e = U −1
e
.
The target probability density is given by the Wilson
action
S(U) = −β
N
X
x∈VL
X
µ<ν
Re[tr Pµν(x)] ,
(15)
where Pµν(x) are the plaquettes, namely the product of
U along edges forming the smallest closed loops. Here,
x denotes the initial vertex, and µ and ν are the two
directions that the loop spans. We only include one ori-
entation by requiring µ < ν with both µ and ν pointing in
the positive direction. An illustration is given in FIG. 1
(0).
For any given Ω: V →G we denote the corresponding
gauge transformation as Ω· U. For instance, we have
Ue 7→(Ω· U)e = ΩxiUe Ω−1
xf
(16)
where xi/f represent the starting/end-point of the edge
e. Note that the traces of Wilson loops, and hence the
Wilson action, are invariant under the above gauge trans-
formation.
The guiding idea for constructing our continuous flow
architecture is that the gradients of gauge-invariant


--- Page 5 ---

5
quantities, such as traces of loops W, are gauge equivari-
ant:
∇eW
U7→Ω·U
7−−−−−→Ωxi(∇eW)Ω−1
xf .
(17)
which is the precisely property we require of the vector
field Zθ(U, t)U(t) defining the ODE (4) for our continuous
normalizing flows.
In terms of the directional derivatives, i.e. transporting
the above back by right multiplication to the Lie algebra,
this is equivalent to
∂e
aW 7→Ωxi(∂e
aW)Ω−1
xi .
(18)
If the ODE is gauge equivariant, then transformation
commutes with the normalizing flow map.
Since the
prior we choose (the Haar measure) is by definition
gauge-invariant, the generated probability distribution
will automatically be gauge-invariant, namely qT (U) =
qT (Ω· U), just like the target Wilson action.
We will now use the Wilson loops as building blocks of
our vector field. To build a sufficiently expressive ODE,
we must use a larger set of loops than just the plaquettes.
We denote the traces of loops of some (to be specified be-
low) class (k) as W(k). FIG. 1 shows the specific classes
of loops we consider for our experiments in two dimen-
sions. Instead of the lattice vertices, we will use elements
of the dual lattice as anchor points of the Wilson loops,
denoted as ¯x and shown in the figure as dots, as this
better reflects the symmetries of the loops. In W(k) we
include all spatial alignments and shifts that keep the
original anchor point enclosed in the loop and leave the
orientation of the loop invariant. For instance, for each
anchor point ¯x in two dimensions, W(0) gives rise to one
trace value, namely the plaquette W1
(0) = tr P01, while
W(1) and W(3) each gives rise to four (corresponding to
up, down, left, right).
Concretely, we build the neural ODE by taking a su-
perposition of the vectors ∂e
aW with coefficients depend-
ing on gauge invariant quantities, which in particular in-
clude any element of W(k). To allow for efficient compu-
tation of the divergence, which is needed to compute the
change of density, we use a shallow architecture that first
applies a neural network locally in ¯x to a subset of W, fol-
lowed by a convolution in ¯x that introduces non-local cor-
relations. This way the divergence computation can be
done in O(|E|) time, while for general gauge invariant co-
efficients, it would take O(|E|2) time. See section C of the
appendix. Writing, as before, ˙Ue = P
a Za
e (t, U)TaUe, we
define
Za
e (t, U) =
X
k,¯x
 ∂e
aWk(¯x)

Λk
¯x(t, W) ,
(19)
with Λ(t, W) a time-dependent convolution of features
obtained from W by locally applying a neural network
at each anchor point ¯y:
Λk
¯x = ˆΛk(t) +
X
j,¯y
Ckj
¯x¯y(t) gj
¯y(t, W(¯y)) ,
(20)
where C(t) is a time-dependent convolution kernel, ˆΛk(t)
are field-independent learnable parameters, and g repre-
sents a neural network.
We found that this parametrization is expressive while
still allowing for a tractable divergence computation, as
required for the change of density computation.
Fur-
ther details of the architecture used in our experiments
can be found in section III B, where it is applied to two-
dimensional pure gauge theories.
III.
NUMERICAL EXPERIMENTS
A.
Single-Variable Conjugation Equivariant Flows
0
Flow
0
0
Target
0
0
10
5
10
4
10
3
10
2
10
1
100
FIG. 2. Comparison of the SU(3) densities at β = 9 in terms
of angular coordinates for the three conjugation equivariant
targets listed in table I and the respectively trained continu-
ous normalizing flows.
To highlight the flexibility of continuous flows and their
expressive power, we first repeat the experiment in [8]
and use flows to learn a conjugation-invariant density on
a single copy of SU(N). Specifically, we use three different
families of target actions of the form
S(i)(U) = −β
N Re tr

c(i)
n U n
(21)
with the sets of values c(i) as shown in table I.
TABLE I. Table of coefficients c(i) for the conjugation equiv-
ariant target actions of equation (21). These are the same
values as used in [8].
Target (i)
c(i)
1
c(i)
2
c(i)
3
0
1
0
0
1
0.17
-0.65
1.22
2
0.98
-0.63
-0.21


--- Page 6 ---

6
We parametrize the ODE using a time-dependent po-
tential denoted Pθ, which we learn as a neural network:
˙U = ∇Pθ(t, U) .
(22)
The gradient and the Laplacian, needed for the change of
density computation following (10), are both computed
using automatic differentiation, which is feasible as we
only consider a single SU(N) matrix here.
To ensure that the defined flow is conjugation equiv-
ariant, we define the potential exclusively in terms of
conjugation invariant quantities. First, we construct 64
time features by applying the sin-function with individ-
ually learnable frequencies to t, followed by a dense layer
with 64 features. For U-dependent features, we use ab-
solute, real, and imaginary parts of tr(U n) for powers
n = 1 . . . nmax. Specifically, we use
| tr(U n)|, Re tr(U n), (Re tr(U n))2,
Im tr(U n), (Im tr(U n))2 .
(23)
The time and U-dependent features are then concate-
nated and processed by a ResNet of width 512 and ac-
tivation function gelu before being projected to a single
real value representing the potential Pθ.
For target c(1) we used ResNet depth 3 and nmax =
2, while for the other two targets we used depth 3 and
nmax = 4.
Leveraging the continuous nature of our normalizing
flows, we train a single potential for each type of target
and match the flow time t with the target inverse temper-
ature β as β(t) = 9 · t. For training, we use 4 randomly
drawn end times T and corresponding betas uniformly in
T ∈[0.1, 1] and evaluate the KL loss on 1024 samples for
each.
The densities evaluated in angular coordinates (see ap-
pendix E for details) of the flow shown in FIG. 2 match
the target densities visually to high accuracy. Similarly,
FIG. 3 shows that the flows are able to approximate the
target density for the whole range of target β values to
high accuracy as measured by effective sample size (ESS).
2
4
6
8
0.6
0.8
1.0
ESS
c(1) Contin.
c(1) Discrete
c(2) Contin.
c(2) Discrete
c(3) Contin.
c(3) Discrete
FIG. 3. Effective sample size along the flow time of trained
normalizing flows for each of the three families of target dis-
tributions listed in table I in comparison to the ESS achieved
by the individual discrete flows from [8].
B.
Pure Gauge Theory in Two Dimensions
To demonstrate the feasibility of the model, and in
particular the model architecture described in equation
(19), we performed experiments on two-dimensional pure
gauge theory (15) for SU(2) and SU(3), achieving state-
of-the-art or better effective sample sizes. Table II shows
the result of training for a 16 × 16 lattice, comparing
to previous discrete [8] and continuous [16] architectures.
Table III shows results for SU(3) on a smaller 8×8 lattice
but for larger values of β.
In contrast to previous work [8, 16], we have found that
initially using a smaller batch size of 32 and increasing
this after some steps helps to speed up training. Con-
cretely, we train using a second-order Crouch-Grossmann
integrator with 40 steps in 32-bit mode until training ap-
proximately converged, then switching to 64-bit mode
and a batch size of 128. ESS evaluation was done in each
case in 64-bit mode and using 40 steps of a third-order
Crouch-Grossmann method.
We will now outline in more detail the architectures
used for SU(2) and SU(3) flows, respectively.
TABLE II. Effective sample sizes for normalizing flows for
SU(2) and SU(3) on 16 × 16 lattice compared to previous
work. Best values in bold.
SU(2)
SU(3)
ESS [%]
β = 2.2
β = 2.7
β = 5
β = 6
β = 8
Continuous flow
87
68
86
76
23
Bacchio et al [16]
–
–
88
70
–
Boyda et al [8]
80
56
75
48
–
TABLE III. Effective sample sizes for normalizing flows for
SU(3) on 8×8 lattice compared to previous work. Best values
in bold.
ESS [%]
β = 8
β = 12
Continuous flow
64
27
Multiscale + flow [28]
35
13
Haar + flow [28]
25
3
1.
Flows on SU(2) lattices
When applying the general form of the architecture
in (19) above to the specific experiments described here,
we only used the first two classes of loops, shown in red
in FIG. 1, as input to the neural network that defines
the superposition coefficients Λ. Moreover, as we sum
over the anchor points ¯x, to avoid redundancy we do
not include all shifted copies of the Wilson loops in the
gradients ∇eW. We therefore denote by ˜
W(i) the subset
of traces W(i) where we pick one representative of each


--- Page 7 ---

7
set of shifted loops. For example, ˜
W(1)(¯x) contains two
instead of four values for each anchor point.
Let W(i1:i2) denote the union of W(i1), . . . , W(i2). The
architecture of the neural ODE used in our experiments
is then given by
Za
e (t, U) =
X
k,¯x

∂e
a ˜
Wk
(0:7)(¯x)

Λk
¯x
 t, W(0:1)

,
(24)
where the superposition coefficients are
Λk
¯x = ˆΛk(t) +
X
j,¯y
Ckj
¯x¯y(t) gj
¯y
 t, W(0:1)(¯y)

.
(25)
Note that for SU(2) all traces W are real numbers, and
can be directly input into conventional dense neural net-
works.
We parametrize g as a ResNet of depth 3, width 128,
and with gelu activation function.
The time depen-
dence is introduced by first applying a set of 16 uniformly
shifted Gaussian density functions to t followed by a sin-
gle dense layer with output size 16 to generate a set of
features Kl
g(t) with l = 1, . . . , 16.
The convolution kernel is chosen to be of size 5 × 5.
The time dependence is introduced by having 16 copies
of parameters and contracting them with Kl
C(t) which
is constructed as above but with independently trainable
parameters in the dense layer.
The number of output
features of g and thus input features of C, indexed by j
in equation (25), are chosen to be 24.
2.
Flows on SU(3) lattices
The architecture for SU(3) is qualitatively the same as
for SU(2). However, in this case, the traces of loops are
generally complex. For the input of the network g we use
Re W(0:1) and
 Im W(0:1)
2. The latter is chosen to reflect
the parity symmetry of the theory. Similarly, We have
two output channels in the convolution corresponding to
the imaginary and real parts of the gradients ∂W. The
final form of the architecture is then
Za
e (t, U) =
X
k,¯x
Re

∂e
a ˜
Wk
(0:7)(¯x)

Λ(R)k
¯x
 t, W(0:1)

+
Im

∂e
a ˜
Wk
(0:7)(¯x)

Dkj Im Wj
(0:1)

Λ(I)k
¯x
 t, W(0:1)

,
(26)
where we ensure parity symmetry by introducing a dense
matrix D, and with the two superposition factors similar
to the above:
Λ(∗)k
¯x
= ˆΛ(∗)k(t) +
X
j,¯y
C(∗)kj
¯x¯y
(t) gj
¯y
 t, W(0:1)(¯y)

.
(27)
The time dependence and network architecture are the
same as those specified above for SU(2).
IV.
OUTLOOK
In this work, we introduced a gauge-equivariant con-
tinuous normalizing flow framework for lattice gauge
theories.
Our method demonstrates competitive effec-
tive sample sizes (ESS) when applied to two-dimensional
SU(2) and SU(3) pure gauge theories, outperforming pre-
vious discrete and continuous approaches.
In machine learning literature, the idea of guiding the
continuous flow to achieve more stability and accuracy
has been discussed in various works [29, 30]. In our exper-
iment on a single Lie group flow, we have briefly explored
the method matching the flow time to a predetermined
evolution of target density and obtained encouraging pre-
liminary results. It would be extended to lattice gauge
theories, connecting to related work of stochastic normal-
izing flows [31] that have shown promising results also in
higher spatial dimensions [32, 33].
Scaling up normalizing flows to larger lattice sizes re-
mains a challenge [34, 35]. We believe that the broad
class of continuous equivariant normalizing flows devel-
oped in this paper constitutes a promising tool for achiev-
ing large-scale flow-based lattice simulations. To facili-
tate scaling, the incorporation of methods such as multi-
scale sampling [28], transfer learning [10] and other hier-
archical generation and transfer learning ideas should be
further explored.
In this work, we have limited ourselves to simple dense
networks when designing neural networks employed to
construct the neural ODE. It would be interesting to ex-
plore other network architectures, including the recently
proposed gauge equivariant convolutional networks [36],
in the future.
Finally, it will be useful to extend the
present work to include field theories with fermions.
ACKNOWLEDGMENTS
We thank Niki Stratikopoulou for helpful discussions.
The research of MG and MC is supported by the Vidi
grant (number 016.Vidi.189.182) from the Dutch Re-
search Council (NWO). MG was partially supported by
a project that has received funding from the European
Research Council (ERC) under the European Union’s
Horizon 2020 research and innovation programme (Grant
agreement No. 864035).
Appendix A: Adjoint Sensitivity Method
For a smooth manifold M, we consider the ODE ˙z =
fθ(t, z) ∈TzM where θ represents some set of trainable
parameters. Let Φ be the associated flow map with the
properties
d
dsΦt,s(z)

s=0 = fθ(t, z)
(A1a)
Φt+s,s′ ◦Φt,s = Φt,s+s′ ,
(A1b)


--- Page 8 ---

8
and with the boundary condition Φt,0(z) = z. From the
above, it is clear that the map Φ depends on the trainable
parameters θ through the form of the ODE.
Given a loss function L : M →R, we are interested
in computing ∂θL(z(T)) where z(T) = Φ0,T (z(0)) given
a fixed initial z(0).
At the final time T, the deriva-
tive dL|z(T ) measures the sensitivity of the loss to small
changes in the final value z(T). Formally, it is a cotan-
gent vector dL|z(T ) ∈T ∗
z(T )M which linearly maps vec-
tors in Tz(T )M to a real number. To compute it, one
needs to take into account the effect of changing the ODE
at all earlier times t < T. To this end, we define an aux-
iliary adjoint state a(t) ∈T ∗
z(t)M defined as follows:
a(t) := d(L ◦Φt,T −t)

z(t) = dL

z(T ) ◦dΦt,T −t

z(t) . (A2)
Like dL|z(T ), the cotangent vector a(t) is a linear map
from a tangent vector in Tz(t)M to a real number. It
captures the sensitivity of the loss to (infinitesimally)
perturbing z(t) in the direction of the tangent vector,
then flowing with the ODE to time T, and evaluating
the loss. More explicitly, this means
a(t)(X) = dL

z(T )(dΦt,T −t(X))
(A3)
for all X ∈Tz(t)M, where
dΦt,T −t

z(t) : Tz(t)M →Tz(T )M
(A4)
is the differential map associated to Φt,T −t. Formally,
a(t) is the pullback of dL under the flow map Φ:
a(t) = Φ∗
t,T −t dL .
To obtain an equation for a(t), we take the derivative
with respect to t. First, observe that
a(t −s) = d(L ◦Φt,T −t ◦Φt−s,s) = a(t) ◦dΦt−s,s (A5)
which follows from the composition property (A1b) and
the chain rule.
Then, using that the derivatives with
respect to z and t commute and property (A1a) we can
take the time derivative to get:
˙a(t) = −d
dsa(t −s)

s=0
= −a(t) ◦d
 d
dsΦt−s,s

z(t−s)

s=0
= −a(t) ◦dfθ

z(t)
(A6)
Note that we also use here that the tangent space is a
vector space, and as such its tangent space can be iden-
tified with itself. If we let z(t) vary in M and consider
a as a section of the cotangent bundle, ˙a then lies in its
vertical bundle.
Using this, we can solve for the adjoint state by inte-
grating the ODE (A6) backwards in time, starting from
z(T) and the initial value a(T) = dL

z(T ). Given the ad-
joint state, the derivative with respect to parameters is
computed simultaneously as
dθL(z(T)) = −
Z 0
T
a(t) ◦dθfθ(t, z(t)) dt ,
(A7)
as explained in [21].
1.
Lie-Algebra Valued Adjoint State
We will show how the explicit equation of (13) for the
adjoint state, represented as a Lie algebra element, fol-
lows from the general expression in equation (12).
We consider an ODE on M = G × R whose elements
we denote z = (z(1), z(2)) = (U, L) where L ∈R rep-
resents the log-likelihood.
In particular we may have
G = SU(N)|E|, but to improve legibility we will suppress
the lattice index on U ∈G below.
The ODE ˙z = fθ is given by fθ = ( ˙U, ˙L), and using
the ODE for L of equation (10) we have:
˙U = Z(t, U)U =
X
a
Za(t, U)TaU ,
(A8a)
˙L = −∇U · ˙U= −
X
a
∂aZa(t, U) .
(A8b)
We integrate this forward in time from t = 0 to t = T
with the initial U(0) drawn from the Haar prior q0(U) =
ρ(U) and L(0) = log ρ(U(0)). Our loss function has the
specific form
L(U, L) = S(U) + L ,
(A9)
which we evaluate at z(T) = (U(T), L(T)). Note that as
our manifold M is a product space, its cotangent space
at any given point z can be split into an element in T ∗
z(1)G
and T ∗
z(2)R ∼= R, and we can use the notation dU and dL
to indicate the corresponding operators in the two spaces.
Thus, we have
a(T) = a(1)(T) + a(2)(T)
a(1)(T) = dUS,
a(2)(T) = dLL = 1.
(A10)
We have dfθ = (d ˙U, d ˙L) and both vector fields only
have explicit dependence on U, so we have dfθ = dUfθ.
To obtain the specific form of ˙a(t) from the genral form
of equation (A6) we compute
dU ˙Ue = dU(ZU) = (dUZ)U + ZdUU ,
(A11a)
dU ˙L = −dU(∇U · ˙U) .
(A11b)
This implies that the adjoint state satisfies
˙a = −a ◦dzfθ
= −a ◦(dU(ZU), 0) + a ◦(0, dU(∇U · ˙U))
= ˙a(1) + ˙a(2) ,
(A12)


--- Page 9 ---

9
where we split ˙a into
˙a(1) = −a(1) ◦dU(ZU) + a(2) ◦dU(∇U · ˙U) ,
(A13a)
˙a(2) = 0 ,
(A13b)
as the component in the vertical bundle of T ∗G and T ∗R
respectively. Thus, given the initial condition a(2)(T) = 1
we have a(2)(t) = 1 for all times, and we are left with
˙a(1) = −a(1) ◦dU(ZU) + dU(∇U · ˙U) .
(A14)
Recall that a(1)(t) ∈T ∗
U(t)G. In view of the decompo-
sition mentioned above (4) and given U(t), we can equiv-
alently define ˜a(1) ∈g∗such that for all v ∈g we have
˜a(1)(v) = a(1)(vU), namely ˜a(1) = a(1) ◦rU where rU
denotes right-multiplication by U = U(t). We thus have
d
dt˜a(1) = ˙a(1) ◦rU + a(1) ◦rZU ,
(A15)
where we have used ˙U = ZU. Using the scalar product
which gives an isomorphism g∗→g, we can represent
˜a(1)(t) as a Lie algebra element A(t) such that
˜a(1)(t)(v) = a(1)(t)(vU) = ⟨A(t), v⟩∀v ∈g .
(A16)
Similarly, defining the gradient ∇Uh ∈TUG of a scalar
function h as
dUh(vU) = ⟨∇UhU −1, v⟩,
(A17)
the initial condition is then given by A(T) = ∇US. In
terms of the explicit orthonormal basis {Ta}, we have
A(T) = P
a(∂aS)TaU.
Following a straightforward calculation using the above
relations and expressing the bilinear form as trace (5), we
finally obtain the adjoint state ODE
˙A = [Z, A]+∇U(∇U · ˙U)U −1−
X
a
Aa∇UZaU −1 , (A18)
where [Z, A] is the commutator and the a index is the
component with respect to the Lie algebra basis. In terms
of explicit basis {Ta}a for g and the dual basis {T a}a for
g∗, we have ˜a(1)(t) = P
a AaT a and A(t) = P
a AaTa.
Then (A15) acting on v ∈g gives
X
a
va ˙Aa =
X
a,b
(−Aavb∂bZa + ∂a∂bZb) −
X
a
Aa⟨Ta, [v, Z]⟩,
which becomes, upon using the cyclic property of the
trace,
˙Aa =
X
b
(−Ab∂aZb + ∂a∂bZb) + ⟨Ta, [Z, A]⟩
(A19)
which is precisely (A18). To translate the general loss
integral (11) , repeated here:
dθL(z(T)) = −
Z 0
T
a(t) ◦dθfθ(t, z(t)) dt ,
(A20)
into the specialized expression (14), we simply specialize
to the case dfθ = (d ˙U, d ˙L). With ˙U = ZU we get
a(1) ◦dθ ˙U = ⟨A(t), ∂θZ⟩
a(2) ◦dθ ˙L = −
X
a
∂θ∂aZa
(A21)
and thus the loss is computed as
∂θL(z(T)) =
Z 0
T
 
−⟨A(t), ∂θZ⟩+
X
a
∂θ∂aZa
!
dt
=
X
a
Z 0
T
(−Aa(t)∂θZa + ∂θ∂aZa) dt .
(A22)
Appendix B: Gradient Implementation
In practice,
we implement the adjoint sensitivity
method under the assumption that M is embedded in
Cn for some integer n, and that we represent the values
as elements of this ambient space. This is in particular
the case for matrix Lie groups such as SU(N), product
manifolds thereof, and the real numbers that represent
the log-density of samples. The implementation makes
heavy use of JAX’s [37] Jacobian-vector product (JVP,
also known as forward mode) and vector-Jacobian prod-
ucts (VJP, also known as reverse mode). Given a function
f : Cm 7→Cn, these generate new functions
JVP(f) : TCm →TCn,
v 7→df(v)
VJP(f) : T ∗Cn →T ∗Cm,
c 7→c ◦df .
(B1)
Numerically T ∗Cm →∼= TCm ∼= Cm, and the action of a
dual space element c ∈T ∗Cm on v ∈TCm is simply the
inner product c · v ∈C on Cm. In particular, for a real
function h : Cm 7→R, the cotangent dh can be obtained
via VJP with cotangent 1 ∈C ∼= T ∗C as input. With
these operations, the adjoint sensitivity method can thus
be implemented in full generality.
1.
Gradients and Divergence of Loops
For traces of loops, the gradient and second derivatives
needed to compute the neural ODE and its divergence
can be efficiently computed by inserting Lie group gen-
erators into the product of group elements Ue labeled by
the edges e.


--- Page 10 ---

10
If a loop has the form
W = tr(Ue1 . . . Uei . . . Uen) ,
(B2)
the directional derivative ∂ei
a
acts on Uei as ∂ei
a Uei =
TaUei and ∂ei
a Uej = 0 for i ̸= j. Then for the loop we
have
∂ei
a W = tr(Ue1 . . . TaUei . . . Uen) ,
(B3)
with a sum over all occurrences if Uei appears in more
than one place.
For U −1
ei
= U †
ei, using the fact that
the generators are skew-symmetric, we have ∂ei
a U †
ei =
(TaUei)† = −U †
eiTa.
Once these directional deriva-
tives are computed, they can be propagated through the
derivative of the neural network as described above. For
the divergence, one has to trace over e and a. The pri-
mary challenge in the implementation is to efficiently
keep track of the combinatorics of where edge elements
appear and to avoid redundant computations for the sec-
ond derivatives arising from the divergence calculation.
Appendix C: Computational Cost of the Divergence
To understand the role of architecture in relation to
the computational cost of the divergence, first consider a
simpler scalar vector field
˙ϕx = fx(ϕ, t) .
(C1)
Computing the divergence
∂
∂ϕx
fx(ϕ, t)
(C2)
for a generic f would require one automatic differenti-
ation call per lattice site value x, regardless of whether
forward or backward mode is used. Let N be the number
of such sites (i.e. the size of the vectors ϕ and f(ϕ)). As
f is a function of N variables, its computational cost will
scale as O(N) in the best case. A single backward or
forward pass would thus also scale linearly in N. Since
the full divergence computation requires N backward or
forward passes, this leads to a total computational cost
for the divergence of O(N 2).
If the analytic form of f is known and chosen appro-
priately, it may be used to reduce this computational
cost.
Before considering our gauge field architecture,
we can illustrate this in the following toy example. Let
fx(ϕ) = P
y,i M i
xy sin(ωiϕy). It is clear the divergence
is in fact cheaper to evaluate than the vector field it-
self: ∂fx/∂ϕx = P
i M i
xxωi cos(ωiϕx).
This simplifica-
tion arises from the linear map M and the “locally” ap-
plied function sin. However, a black-box application of
automatic differentiation for the divergence would not
be able to exploit this fact, leading to a large amount of
redundant computations.
Now, recall the general architecture of equation (19):
Za
e (t, U) =
X
k,¯x
 ∂e
aWk(¯x)

Λk
¯x(t, W) .
(C3)
Applying the chain rule, after differentiating with respect
to the same link and Lie algebra component (i.e. applying
∂e
a), the divergence becomes:
∂e
aZa
e (t, U) =
X
k,¯x
 ∂e
a∂e
aWk(¯x)

Λk
¯x(t, W) +
X
k,¯x
X
j,¯y
 ∂e
aWk(¯x)
 ∂e
aWj(¯y)

∂
∂Wj(¯y)Λk
¯x(t, W) .
(C4)
The cost of taking the second derivative of the Wilson
loops for a given edge e does not increase with the lat-
tice size, at least when the choice of included loops is
held constant. We can thus focus on the second term.
Since not all Wilson loops contain the link Ue, the sums
over ¯x and ¯y do not scale with |E|.
Thus, the num-
ber of derivatives ∂Λ/∂W that need to be taken for any
given edge remains O(1). However, if the network Λ is
a black box, these derivatives still have to be computed
with automatic-differentiation for each lattice site. Since
Λ is generically a function of all field variables, this may
still scale as O(|E|2) – a function of |E| variables evalu-
ated |E| times.
The final simplification arises from the shallow form
Λk
¯x = ˆΛk(t) +
X
l,¯z
Ckl
¯x¯z(t) gl
¯z(t, W(¯z)) .
(C5)
Applying the derivative:
∂
∂Wj(¯y)Λk
¯x =
X
l
Ckl
¯x¯y(t)
∂
∂Wj(¯y)gl
¯y(t, W(¯y)) .
(C6)
Because the non-linearity g is applied “locally”, i.e. its
output at ¯z only depends on the Wilson loop stack at ¯z
(which does not scale with |E|), the sum over ¯z above is
removed and the convolution reduces to a simple point-
wise multiplication. Thus, computing g and its deriva-
tives with respect to W does not itself scale with |E|. We
still have to compute this once for each link, of course,
leading to a computational cost that grows linearly with
|E|. In contrast to a black-box vector field, however, this
shows that computing the divergence for our shallow vec-
tor field architecture does not add an additional factor of
|E| relative to the vector field itself.
Appendix D: Implementation of the
Crouch-Grossman Runge Kutta integration method
We consider ODEs on G×Rd, where we simultaneously
evolve both real degrees of freedom x ∈Rd and matrix


--- Page 11 ---

11
Lie group degrees of freedom Y ∈G. To achieve this, we
apply a Runge-Kutta method for the former and simul-
taneously a Crouch-Grossmann method [26, 27] for the
latter ensuring that the group structure of Y is preserved
during the simultaneous time evolution of both variables.
In the Crouch-Grossman method, the Lie group ele-
ment evolves according to:
Yn+1 = exp

hbsZ(n)
s

· · · · · exp

hb1Z(n)
1

Yn,
where h is the time step size, bi are the coefficients
from the Butcher tableau (Runge-Kutta coefficients) and
Z(n)
i
= Z(x(n)
i
, Y (n)
i
) ∈g is the Lie algebra-valued vector
field at the internal stage i that generally may depend on
both x(n)
i
and Y (n)
i
.
The internal stages Y (n)
i
∈G are computed using:
Y (n)
i
= exp

hai,i−1Z(n)
i−1

· · · · · exp

hai,1Z(n)
1

Yn ,
where ai,j are given by the chosen Butcher tableau.
While we have suppressed the explicit time-dependence
in the equations above, we note that in evaluating Z(n)
i
,
we set the time to be t(n)
i
= tn + cih with ci = P
j ai,j.
For the real degrees of freedom x ∈Rd, we use a stan-
dard Runge-Kutta method with the same time step h
and the same Butcher-tableau coefficients ai,j, bi as for
the Lie group variables. The real degrees of freedom are
updated as:
xn+1 = xn + h
s
X
i=1
bif(x(n)
i
, Y (n)
i
) ,
where f(x(n)
i
, Y (n)
i
) ∈Rd is the vector field in the ODE
˙x = f(x, Y ), governing the evolution of x and xi are the
internal stages computed similarly:
x(n)
i
= xn + h
i−1
X
j=1
ai,jf(x(n)
j
, Y (n)
j
) .
Note that both internal stages x(n)
i
and Y (n)
i
are updated
in parallel using their respective methods.
Appendix E: Haar Measure and Sampling
1.
Haar Measure for Matrix Lie Groups
The Haar measure defines a unique invariant mea-
sure on compact Lie groups G such as SU(N) [38]. The
measure, denoted dU, is invariant under left- and right-
multiplications:
d(V U) = d(UV ) = dU
∀V, U ∈G.
This invariance ensures that the measure is uniform
across the group. With respect to this measure, the Haar
prior distribution is uniform and (up to volume normal-
ization) given as q0(U) = 1.
2.
Sampling from the Haar Distribution
Sampling from the Haar distribution on SU(N) can be
achieved through the construction of random unitary ma-
trices. The method involves generating random matrices
with independent complex entries, followed by an orthog-
onalization procedure that ensures the sampled matrix
lies within the SU(N) group [39].
We start with a random complex matrix X ∈CN×N,
whose elements are drawn from a standard normal dis-
tribution. We then apply a QR decomposition:
X = QR,
where Q ∈CN×N is a unitary matrix, and R ∈CN×N
is upper triangular. We then extract and normalize the
diagonal part of R by dividing each element by its abso-
lute value: R′ = diag(R)/|diag(R)|, i.e. R′
ii = Rii/|Rii|,
which ensures that all elements are pure phases thus mak-
ing it unitary. We then need to divide by
κ =
Np
det(Q) det(R′) ,
(E1)
to ensure that the matrix X′ = QR′/κ has a determinant
of 1, so finally we have X′ ∈SU(N).
The resulting
matrix X′ is then uniformly distributed according to the
Haar measure on SU(N).
3.
Haar Measure for SU(3)
For the specific case of SU(3), the Haar measure
can be expressed in terms of angular coordinates that
parametrize the eigenvalues of the matrix. The maximal
torus of SU(3) corresponds to diagonal matrices with
phases θ1, θ2, and θ3, satisfying P3
i=1 θi = 0 and ensur-
ing the unit determinant condition.
The Haar measure on SU(3) in terms of these angular
variables is given by [40]:
dU = dθ1 dθ2
Y
i<j
eiθi −eiθj2 .
(E2)
Appendix F: Markov Chain Monte Carlo &
Observables
To verify the implementation and successful training
of normalizing flows, we generated asymptotically unbi-
ased samples using an independent Metropolis-Hastings
Markov chain with the trained normalizing flows as in-
dependent proposal distributions. Denoting the learned
flow distribution as q(U) and the target distribution as
p(U), one samples proposals U ′ ∼q which are accepted,
U (i) = U ′, with probability
min

1, q(U (i−1))p(U ′)
q(U ′)p(U (i−1))

(F1)


--- Page 12 ---

12
and otherwise rejected, leading to a repeat of the previous
sample U (i) = U (i−1).
The acceptance rates over a sequence of this Markov
chain gives an alternative quality of fit measure for the
generative models to the ESS used in the main text. Ta-
ble IV gives an overview of these values, which are gen-
erally in agreement with the ESS.
TABLE IV. Acceptance rates (in %) for the continuous nor-
malizing flows trained for different gauge groups and lattice
sizes using an independent Metropolis-Hastings Markov chain
of length 20480 for all configurations of tables II and III.
SU(2), L=16
SU(3), L=16
SU(3), L=8
β = 2.2
β = 2.7
β = 5
β = 6
β = 8
β = 8
β = 12
84
82
78
71
38
65
32
Figures 4 and 5 show the ratios of observables esti-
mated using the same Markov chains compared to ana-
lytically known values [41, 42] for SU(2) and SU(3), re-
spectively. Here, Wl1l2 denote the expectation values of
the real parts of the traces of rectangular Wilson loops
with edge lengths l1 and l2. In addition, |ℓ|2 is the zero-
separation two-point function of Polyakov loops
ℓ(x2) = tr
Y
t
U1(x = (t, x2)) ,
(F2)
identifying axis-1 of the lattice with Euclidean time.
Then |ℓ|2 = l∗(x)l(x) is independent of x due to transla-
tional symmetry.
0.95
1.00
1.05
W11 W12 W21 W22 W13 W31 W14 W41 | |2
0.95
1.00
1.05
= 2.2
= 2.7
Ratio of MC estimate to true value
FIG. 4.
Ratio of Monte Carlo estimates of observables to
analytic values for flows on SU(2) on a 16 × 16 lattice. The
trained flows of table II are used as proposal distribution for
an independent Metropolis-Hastings Markov chain of length
20480, and errors shown as vertical bars are estimated using
a bootstrap method.
0.95
1.00
1.05
0.95
1.00
1.05
W11 W12 W21 W22 W13 W31 W14 W41 | |2
Loop type
0.95
1.00
1.05
= 5.0
= 6.0
= 8.0
Ratio of MC estimate to true value
FIG. 5.
Ratio of Monte Carlo estimates of observables to
analytic values for flows on SU(3) on a 16 × 16 lattice. The
trained flows of table II are used as proposal distribution for
an independent Metropolis-Hastings Markov chain of length
20480, and errors shown as vertical bars are estimated using
a bootstrap method.


--- Page 13 ---

13
[1] C. Morningstar, The Monte Carlo method in quantum
field theory (2007), arXiv:hep-lat/0702020.
[2] A. Sokal, Monte carlo methods in statistical mechanics:
foundations and new algorithms, in Functional integra-
tion: Basics and applications (Springer, 1997) pp. 131–
192.
[3] G. Papamakarios, E. Nalisnick, D. J. Rezende, S. Mo-
hamed, and B. Lakshminarayanan, Normalizing flows for
probabilistic modeling and inference, Journal of Machine
Learning Research 22, 1 (2021).
[4] M. S. Albergo, G. Kanwar, and P. E. Shanahan, Flow-
based generative models for Markov chain Monte Carlo
in lattice field theory, Phys. Rev. D 100, 034515 (2019),
arXiv:1904.12072 [hep-lat].
[5] M. S. Albergo, D. Boyda, D. C. Hackett, G. Kanwar,
K. Cranmer, S. Racani`ere, D. J. Rezende, and P. E.
Shanahan, Introduction to Normalizing Flows for Lattice
Field Theory (2021), arXiv:2101.08176 [hep-lat].
[6] M. C. N. Cheng and N. Stratikopoulou, Lecture Notes on
Normalizing Flows for Lattice Quantum Field Theories ,
to appear (2024).
[7] R. T. Q. Chen, Y. Rubanova, J. Bettencourt, and D. Du-
venaud, Neural ordinary differential equations (2019),
arXiv:1806.07366 [cs.LG].
[8] D. Boyda, G. Kanwar, S. Racani`ere, D. J. Rezende, M. S.
Albergo, K. Cranmer, D. C. Hackett, and P. E. Shana-
han, Sampling using $SU(N)$ gauge equivariant flows,
Phys. Rev. D 103, 074504 (2021), arXiv:2008.05456 [hep-
lat].
[9] P.
de
Haan,
C.
Rainone,
M.
C.
N.
Cheng,
and
R. Bondesan, Scaling up machine learning for quantum
field theory with equivariant continuous flows (2021),
arXiv:2110.02673 [cs.LG].
[10] M. Gerdes, P. de Haan, C. Rainone, R. Bondesan, and
M. C. N. Cheng, Learning Lattice Quantum Field The-
ories with Equivariant Continuous Flows, SciPost Phys.
15, 238 (2023), arXiv:2207.00283 [hep-lat].
[11] M. Caselle, E. Cellini, and A. Nada, Sampling the
lattice nambu-goto string using continuous normal-
izing flows, Journal of High Energy Physics 2024,
10.1007/jhep02(2024)048 (2024).
[12] Y. Nagai and A. Tomiya, Gauge covariant neural network
for quarks and gluons, Phys. Rev. D 111, 074501 (2025),
arXiv:2103.11965 [hep-lat].
[13] R. Abbott, M. S. Albergo, A. Botev, D. Boyda, K. Cran-
mer, D. C. Hackett, G. Kanwar, A. G. D. G. Matthews,
S. Racani`ere, A. Razavi, D. J. Rezende, F. Romero-
L´opez, P. E. Shanahan, and J. M. Urban, Normalizing
flows for lattice gauge theory in arbitrary space-time di-
mension (2023), arXiv:2305.02402 [hep-lat].
[14] R. Abbott, A. Botev, D. Boyda, D. C. Hackett, G. Kan-
war, S. Racani`ere, D. J. Rezende, F. Romero-L´opez, P. E.
Shanahan, and J. M. Urban, Applications of flow mod-
els to the generation of correlated lattice qcd ensembles,
Phys. Rev. D 109, 094514 (2024).
[15] M. L¨uscher, Trivializing maps, the Wilson flow and the
HMC algorithm, Commun. Math. Phys. 293, 899 (2010),
arXiv:0907.5491 [hep-lat].
[16] S. Bacchio, P. Kessel, S. Schaefer, and L. Vaitl, Learning
Trivializing Gradient Flows for Lattice Gauge Theories,
Phys. Rev. D 107, L051504 (2023), arXiv:2212.08469
[hep-lat].
[17] M. Gerdes and M. C. N. Cheng, Bijx: Bijections and
normalizing flows with jax/nnx, Journal of Open Source
Software 10, 9521 (2025).
[18] M. Gerdes, P. de Haan, R. Bondesan, and M. C. N.
Cheng, Non-perturbative trivializing flows for lattice
gauge theories, 10.5281/zenodo.15576712 (2025).
[19] K. A. Nicoli, C. J. Anders, L. Funcke, T. Hartung,
K. Jansen, P. Kessel, S. Nakajima, and P. Stornati, Esti-
mation of Thermodynamic Observables in Lattice Field
Theories with Deep Generative Models, Phys. Rev. Lett.
126, 032001 (2021), arXiv:2007.07115 [hep-lat].
[20] D. Albandea, L. Del Debbio, P. Hern´andez, R. Kenway,
J. Marsh Rossney, and A. Ramos, Learning trivializing
flows, Eur. Phys. J. C 83, 676 (2023), arXiv:2302.08408
[hep-lat].
[21] R. T. Q. Chen, Y. Rubanova, J. Bettencourt, and
D. K. Duvenaud, Neural Ordinary Differential Equations,
in Advances in Neural Information Processing Systems,
Vol. 31 (Curran Associates, Inc., 2018).
[22] L. Falorsi, Continuous normalizing flows on manifolds
(2021), arXiv:2104.14959 [cs, stat].
[23] A. Lou, D. Lim, I. Katsman, L. Huang, Q. Jiang, S.-N.
Lim, and C. De Sa, Neural Manifold Ordinary Differen-
tial Equations (2020), arXiv:2006.10254 [cs, math, stat].
[24] L. Falorsi and P. Forr´e, Neural ordinary differential equa-
tions on manifolds (2020), arXiv:2006.06663 [stat.ML].
[25] M. Nakahara, Geometry, Topology and Physics, 2nd ed.
(CRC Press, Bristol, 2003).
[26] P. E. Crouch and R. Grossman, Numerical integration of
ordinary differential equations on manifolds, Journal of
Nonlinear Science 3, 1 (1993).
[27] M. Wandelt, Geometric Integration on Lie Groups and
its Applications in Lattice QCD, Ph.D. thesis, Univer-
sit¨atsbibliothek Wuppertal (2021).
[28] R. Abbott, M. S. Albergo, D. Boyda, D. C. Hackett,
G. Kanwar, F. Romero-L´opez, P. E. Shanahan, and J. M.
Urban, Multiscale Normalizing Flows for Gauge Theo-
ries, PoS LATTICE2023, 035 (2024), arXiv:2404.10819
[hep-lat].
[29] H. Wu, J. K¨ohler, and F. No´e, Stochastic Normalizing
Flows (2020), arXiv:2002.06707 [physics, stat].
[30] L. I. Midgley, V. Stimper, G. N. C. Simm, B. Sch¨olkopf,
and J. M. Hern´andez-Lobato, Flow Annealed Importance
Sampling Bootstrap (2023), arXiv:2208.01893 [cs.LG].
[31] M. Caselle, E. Cellini, A. Nada, and M. Panero, Stochas-
tic normalizing flows as non-equilibrium transformations,
Journal of High Energy Physics 2022, 15 (2022).
[32] A. Bulgarelli, E. Cellini, and A. Nada, Sampling su(3)
pure gauge theory with stochastic normalizing flows
(2024), arXiv:2409.18861 [hep-lat].
[33] A. Bulgarelli, E. Cellini, and A. Nada, Scaling of stochas-
tic normalizing flows in SU(3) lattice gauge theory, Phys.
Rev. D 111, 074517 (2025), arXiv:2412.00200 [hep-lat].
[34] R. Abbott, M. S. Albergo, A. Botev, D. Boyda, K. Cran-
mer, D. C. Hackett, A. G. D. G. Matthews, S. Racani`ere,
A. Razavi, D. J. Rezende, F. Romero-L´opez, P. E. Shana-
han, and J. M. Urban, Aspects of scaling and scalability
for flow-based sampling of lattice QCD, Eur. Phys. J. A
59, 257 (2023), arXiv:2211.07541 [hep-lat].
[35] L. Del Debbio, J. M. Rossney, and M. Wilson, Efficient


--- Page 14 ---

14
Modelling of Trivializing Maps for Lattice $\phiˆ4$ The-
ory Using Normalizing Flows: A First Look at Scalabil-
ity, Phys. Rev. D 104, 094507 (2021), arXiv:2105.12481
[hep-lat].
[36] M. Favoni, A. Ipp, D. I. M¨uller, and D. Schuh, Lattice
gauge equivariant convolutional neural networks, Phys.
Rev. Lett. 128, 032003 (2022).
[37] J. Bradbury, R. Frostig, P. Hawkins, M. J. Johnson,
C. Leary, D. Maclaurin, G. Necula, A. Paszke, J. Van-
derPlas, S. Wanderman-Milne, and Q. Zhang, JAX: com-
posable transformations of Python+NumPy programs
(2018).
[38] J. J. Duistermaat and J. A. C. Kolk, Lie Groups, Uni-
versitext (Springer, Berlin, Heidelberg, 2000).
[39] F. Mezzadri, How to generate random matrices from the
classical compact groups, Notices of the American Math-
ematical Society 54, 592 (2007).
[40] D. Bump, The Weyl Integration Formula, in Lie Groups,
Graduate Texts in Mathematics, edited by D. Bump
(Springer, New York, NY, 2004) pp. 112–116.
[41] A. A. Migdal, Recursion Equations in Gauge Theories,
Sov. Phys. JETP 42, 413 (1975).
[42] D. J. Gross and W. Taylor, Two-dimensional QCD is a
string theory, Nucl. Phys. B 400, 181 (1993), arXiv:hep-
th/9301068.


