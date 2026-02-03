---
title: "Qwen2 VL 2410.00520"
source_pdf: "AI Labs/Alibaba (Qwen)/Qwen2-VL/Qwen2-VL_2410.00520.pdf"
company: "Alibaba (Qwen)"
pages: 57
extracted_at: "2026-01-25T04:43:50.900777"
type: "ai_lab_paper"
---

# Qwen2 VL 2410.00520

**Company/Lab:** Alibaba (Qwen)
**Model:** Qwen2-VL
**Source PDF:** AI Labs/Alibaba (Qwen)/Qwen2-VL/Qwen2-VL_2410.00520.pdf
**Total Pages:** 57

---

## Content

```
--- Page 1 ---

arXiv:2410.00520v3  [math.PR]  21 Nov 2024
STRETCHING OF POLYMERS AND TURBULENCE: FOKKER PLANCK
EQUATION, SPECIAL STOCHASTIC SCALING LIMIT AND STATIONARY
LAW
FRANCO FLANDOLI AND YASSINE TAHRAOUI
Abstract. The aim of this work is understanding the stretching mechanism of stochastic models
of turbulence acting on a simple model of dilute polymers. We consider a turbulent model that
is white noise in time and activates frequencies in a shell N ≤|k| ≤2N and investigate the
scaling limit as N →∞, under suitable intensity assumption, such that the stretching term has
a ﬁnite limit covariance. The polymer density equation, initially an SPDE, converges weakly to
a limit deterministic equation with a new term. Stationary solutions can be computed and show
power law decay in the polymer length.
Contents
1.
Introduction
2
1.1.
Sketch of the main results
3
1.2.
Literature review
4
2.
Notations, deﬁnitions and problem formulation
8
3.
Itˆo-Stratonovich correctors
11
4.
Main results
15
4.1.
Stationary solutions and power-law tail
18
5.
About proofs and mathematical challenges
19
6.
Existence and uniqueness of solutions to (12)
22
6.1.
A priori estimates
25
6.2.
Existence of solution to (12)
30
6.3.
Uniqueness of quasi-regular weak solution
34
7.
Diﬀusion scaling limit as N →+∞
45
7.1.
Time regularity and tightness of laws
45
7.2.
Passage to the limit as N →+∞
49
7.3.
Uniqueness of the limit problem (13)
53
7.4.
About the 3D case
53
References
54
Scuola Normale Superiore, Piazza dei Cavalieri, 7, 56126 Pisa, Italia
Scuola Normale Superiore, Piazza dei Cavalieri, 7, 56126 Pisa, Italia
E-mail addresses: franco.flandoli at sns.it, yassine.tahraoui at sns.it.
Date: November 22, 2024.
2020 Mathematics Subject Classiﬁcation. 35Q84, 60H15, 60H30, 76F25.
Key words and phrases. Fokker-Planck equation, Turbulence,Transport Noise, Stretching Noise, Polymer ﬂow.
1

--- Page 2 ---

2
F. FLANDOLI AND Y. TAHRAOUI
1. Introduction
Polymers are complex molecular systems, that can be vaguely thought as a chain of springs.
In a turbulent ﬂuid they are usually found in two states called coil and stretched. The coil state
is like a spherical or ellipsoidal rolled chain, which may be more or less elongated, but still in
roll position. The stretched state is when the chain is elongated, more similar to a stright line
than a sphere. Turbulence with small stretching intensity produces only a small perturbation
of the coil state, while strongly stretching turbulence may lead to the stretched state; when the
polymer pass from one state to the other we speak of coil-stretch transition.
In this work, we consider in dimension 2 or 3 the following Hookean model:



dRt
= ∇u(Xt, t)Rtdt −1
β Rtdt +
√
2σdWt,
dXt
= u(Xt, t)dt,
(1)
where Xt is the polymer position (the center of mass) and Rt is the end-to-end vector, repre-
senting the orientation and elongation of the chain, see e.g. [5, Section 4.2]. The polymer is
embedded into a ﬂuid having velocity u(t, x), which stretches Rt by ∇u(x, t). The equation for
Rt contains also a damping (restoring) term with relaxation time β and Brownian ﬂuctuations
√
2σdWt where, to simplify the notations we have denoted by σ2 the product kT
β , k being Boltz-
mann constant and T being the temperature.
The statistics of the polymer length r, say the diameter, have been investigated by several
authors in the physical literature, see for instance [4, 17, 38, 58] and other references mentioned
below. In the coil state, the distribution of r is found to be power law
(2)
f (r) ∼r−1−α
for relatively large r
with the exponent α positive (so that f is normalizable).
The exponent α depends on the
stretching properties of the turbulent ﬂow: the highest is the stretching intensity, the lowest is
α. At α = 0 one has the coil-stretch transition. In the stretched state, the precise mathematics
depends on the idealizations of the model. If we had introduced a superlinear damping instead
of the linear damping −1
βRt, this would produce a sort of cut-oﬀat very high lengths ( e.g.
FENE model, see Remark 12), so that the behavior (2) would be true only in a range
r0 << r << r1
and globally the function f would still be a pdf. In our idealization of linear damping, the
stretching may overcome the damping and lead to inﬁnite length in the asymptotic regime,
which is the idealized signature of strech state, see subsection 4.1.
Clearly, one would like to predict the exponent α based on turbulence features. The theory
developed on physical grounds by [4] and [10] tells us that α is related to the Lyapunov exponents
of the turbulent ﬂow. Precisely, if φt (x) is the Lagrangian ﬂow associated to the turbulent ﬂuid,
and we deﬁne
L (q) = lim
t→∞
1
t log E [|Dφt (x)|q]
then α satisﬁes
α
2β = L (α) . However, the computation of L (α) is not trivial in general.
The theory just mentioned does not make use of scale separation (and not even delta correla-
tion in time of the turbulent ﬂuid), hence it is quite general (much more than ours). In our paper

--- Page 3 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
3
we consider a special class of turbulent ﬂows, delta-correlated in time, having a precise dyadic
scale ℓ, namely based on Fourier components of modes |k| ∈[ℓ−1, 2ℓ−1]. When ℓis very small,
precisely in the scaling limit as ℓ→0, we discover a power law of the form (2). This provides
another proof (or a more rigorous proof, although in a particular regime) of the emergence of
power law in polymer length r. In addition, we ﬁnd a very direct relation between α and the
turbulent ﬂow characteristics, thanks essentially to the special structure of the ﬂow and the
separation of scales intrinsic in the scaling limit; the non-trivial informations on the Lyapunov
exponents are not needed anymore.
For the convenience of the reader, let us explain heuristically the main result of this work then
precise results (see section 4 ) and rigorous proofs are provided in the main body of the paper.
1.1. Sketch of the main results. We consider a dilute (non-interacting) family of polymers
subject to equations (1), thus described by the kinetic equation for the density f N (x, r, t) of
polymers with position x and length r at time t



∂tf N(x, r, t)
+divx(uN(x, t)f N(x, r, t)) + divr((∇uN(x, t)r −1
βr)f N(x, r, t)) = σ2∆rf N(x, r, t)
f N|t=0
= f0.
(3)
Here uN (x, t) is the ﬂuid velocity. We assume that uN (x, t) is made of two components, a
deterministic large-scale one uL (x, t) and a stochastic one, modeling small-scale turbulence, of
the form P
k∈K σN
k (x) ∂tW k
t , acting in Stratonovich form, that will be described below in detail;
hence
uN (x, t) = uL (x, t) + ◦
X
k∈K
σN
k (x) ∂tW k
t .
Here we just stress the fact that the coeﬃcients σN
k (x) of the turbulent part depend on a pa-
rameter N so that, when N increases, they represent smaller and smaller space scales, precisely
Fourier frequencies N ≤|k| ≤2N, providing a separation of scale regime essential for our analy-
sis. The noise acts on f N (x, r, t) in transport form, but incorporating also the stretching action
by the term ∇uN (x, t) r.
Our aim in this work is twofold. Firstly, present a rigorous mathematical framework and
proofs to study a stochastic Fokker-Planck equations with transport noise and general class of
initial data. These equations has an hyperbolic nature with respect to the space variable x ∈T2
and polymer length vector variable r ∈R2. Thus, we should combine techniques for weighted
spaces to handle the r-variable, spatial homogeneity and mirror symmetry of the covariance
operator to handle the stochastic part and prove existence of ”quasi-regular weak solution”,
see Deﬁnition 5. Then, combine commutators techniques to handle the space variable, using a
density result based on Wiener chaos decomposition to prove uniqueness in this class of solution,
see Theorem 8. We refer to section 5 for discussion about the mathematical challenges related
to these equations.
Secondly, understand the stretching power on the polymer, in the limit as N →∞when the noise
activates frequencies in a shell N ≤|k| ≤2N. The ﬁnal result is a limit model, of Fokker-Planck
type, with a new diﬀusion term in the radial variable of the polymer, with non-homogeneous and
degenerate coeﬃcients. Its radially symmetric stationary solutions are explicit and have power-
law tails. Let us describe quickly the scaling limit result, see Theorem 9 for the precise result.
Under the assumptions described in section 2, we prove that f N(x, r, t) weakly converges to the

--- Page 4 ---

4
F. FLANDOLI AND Y. TAHRAOUI
solution of a deterministic equation of the form (the results below contain also a deterministic
term in the velocity, which is omitted here in the Introduction for notational simplicity)



∂tf(x, r, t)
−divr( 1
β rf(x, r, t)) = σ2∆rf(x, r, t) + 1
2divr(A(r)∇f(x, r, t))
f|t=0
= f0
(4)
where A(r) = kT(3 |r|2 I −2r ⊗r) and kT = π log(2)
8
a2 where a is an intensity parameter of
the noise. The new diﬀusion term in the r-variable is one of the most important novelty of
this work. It captures the statistical properties of the stretching mechanism. We compute the
explicit rotation-invariant solution of the associated stationary equation and ﬁnd it has a power
law decay for large |r|:
f (|r|) ∼|r|
−
2
kT β
indicating large values with high probability. The constants in the power are directly associated
to those of the stochastic model of uN. This fact was predicted in the physical literature based
on other models and assumptions, see e.g. [4]. In our model we identify a simple link between
the power of the tail and parameters of the turbulence model, see subsection 4.1.
We wish to draw the reader’s attention to the following: introduce the mean of the structure
tensor T(t, x) :=
R
R2 r ⊗rf N(t, x, r)dr then TN 1 satisﬁes the following closed system of PDEs



∂tTN + uN · ∇TN = (∇uN)TN + TN(∇uN)t −2
β (TN −kTI)
TN|t=0 = T0,
(5)
The last equation (5) is a macroscopic Oldroyd-B model (see e.g. [11, Section 2.8]) and the
tensor T characterize the viscoelastic (non-Newtonian part) of the ﬂow (1). Many rheological
behavior can be detected such as shear viscosity, normal stress diﬀerence and overshoot phe-
nomenon in contrast with Newtonian ﬂows, see e.g. [5] and we refer e.g. to [11, 60, 61] for other
types of non-Newtonian ﬂows. As we discuss in subsection 4.1, the explicit rotation-invariant
solution of the stationary equation associated with the limit equation has a power-law density
and therefore it is not suﬃcient to study the system (5) only, this is another reason we base our
analysis on FP equation (3). We will comment about the limit equation associated with (5) in
Remark 11. Finally, Although the results and proofs are presented in 2D, similar results hold
in 3D after some cosmetic changes and mostly the form of the stochastic turbulent velocity, see
subsection 7.4.
This work is a key step in a research project on the eﬀects of small-scale turbulence on
large-scale motion, started a few years ago after the development of a new technique. In order
to understand the novelties it may be useful to review these recent developments and stress
similarities and diﬀerences.
1.2. Literature review. We divide the presentation in two subsections, the scalar and the
vector case. The second one is characterized by a peculiar issue, the presence of stretching,
which is by no means an incremental detail over the scalar case; and the present work aims to
give relevant information on the stretching case.
1The subscript N to stress the dependence on N because of the presence of uN.

--- Page 5 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
5
1.2.1. The scalar case. The foundational work [36] investigated a problem that, to some extent,
could be considered as a variant of diﬀusion approximation results in stochastic homogenization
theory: a stochastic ﬁrst order diﬀerential operator in Stratonovich form gives rise, in a suitable
scaling limit, to a deterministic diﬀusion term. The stochastic equation had the form (we do not
describe in detail the spatial domain, the ﬁnite or countable set where the index k varies and
other details which have no relevance for the purpose of this section, see [36])
(
dρN
t
= P
k θN
k ek · ∇ρN
t ◦dW k
t
ρN|t=0
= ρ0 ∈L2
with suitable vector ﬁelds ek (a suitable subset of a complete orthonormal system in L2) and the
family of real valued coeﬃcients θN :=
 θN
k

. Under the assumptions
lim
N→∞
θN2
ℓ2 = κ,
lim
N→∞
θN
ℓ∞= 0,
it has been proved that, in a weak sense (namely against test functions or in suitable negative
order Sobolev spaces) the solution ρN converges in mean square to the unique deterministic
solution ρt of the heat equation
(
∂tρt
= κ∆ρt
ρ|t=0
= ρ0
(possibly with the constant κ modiﬁed by a constant related to space dimension and the choice of
the orthonormal system). The technical assumption mentioned above on θN can be reformulated
in terms of the noise covariance function:
QN (x, y) =
X
k
 θN
k
2 ek (x) ⊗ek (y) = E [W (x, 1) ⊗W (y, 1)]
where W (x, t) = P
k θN
k ek (x) W k
t and the associated linear operator on L2 vector ﬁelds v (x)
(QNv) (x) =
Z
QN (x, y) v (y) dy.
The assumption is that the trace of QN converges to κ and the operator norm to zero. Heuris-
tically, it means that the function QN (x, y) tends to a non zero value along the diagonal and to
zero outside, in other words
(
limN→0 QN (x, x)
= κ
limN→0 QN (x, y)
= 0 for x ̸= y
(6)
namely the variance of the noise remains constant at the limit but the space correlation goes to
zero.
We have said that this is related to results in homogenization theory [50], but it is important
to notice that the model and strategy are diﬀerent from classical homogenization and especially
they are very eﬃcient for Generalizations to nonlinear problems. The result of [36] has been
extended, indeed, to 2D Euler equations, 2D Navier-Stokes equations, and other nonlinear mod-
els like Keller-Siegel and nonlinear heat equations, see [21] and [23] for the basic results in this
direction, obtained both with compactness methods and more quantitatively with estimates on
stochastic convolutions. The results have been supplemented by the analysis of Gaussian ﬂuctua-
tions and Large Deviations [37]. Mixing and dissipation enhancement results can also be obtained
by this approach, see [3, 14, 28, 22], [23, section 9] and [46, 48]. The fact that the limit equation

--- Page 6 ---

6
F. FLANDOLI AND Y. TAHRAOUI
contains an additional strongly elliptic term sometimes has a feedback eﬀect of regularization on
the approximating stochastic problems (the closeness in some norm provides additional a priori
bounds), leading to delay of blow-up results [20]. See also [1, 26, 32, 33, 35, 43, 45, 47, 49, 57] for
various other applications, examples and numerical approximations. The problem is of interest
also for Large Eddy Simulations and Boussinesq assumption, see [31] for a Smagorinsky type
result. The scaling limit has been also transposed to particle systems, see for instance [29, 40].
This list of works is certainly non complete but it gives the feeling of the fertility of the scaling
limit result proved in [36].
Let us also mention that transport and transport-stretching noise (the second being the topic
of next subsection) is currently used in many other researches and for diﬀerent purposes; above
we have restricted the attention to works dealing with the special scaling limit to an additional
diﬀusion. The list of references on other research directions on transport-stretching noise is too
long, let us only mention as examples [12, 39, 16, 42, 41, 53].
1.2.2. The vector ﬁelds case. The works discussed above dealt with scalar problems, where trans-
port noise induces an additional elliptic operator. When the turbulent ﬂuid acts on vector ﬁelds,
the action has two aspects: not only transport but also stretching: namely the diﬀerential Dφt
of the Lagrangian ﬂow φt of a ﬂuid produces a modiﬁcation of the length of vectors v, v 7→Dφtv.
Since we consider divergence free ﬂuids, the deformation tensor Du of the velocity ﬁeld u has
zero trace, the symmetrization typically has a positive eigenvalues, indicating that an increase
of length should be expected for many directions v.
Understanding deterministic and random stretching is much more diﬃcult and open, with
respect to transport. Two indications of this diﬃculty are that stretching is considered the most
important problem in view of the open problem of blow-up for the 3D Navier-Stokes equations
[19]; and that in contrast to a wide range of results on mixing and dissipation enhancement
produced by chaotic transport of scalars, there is very few on the eﬀect of complex stretching
[66]. The problem of random stretching has been approached also by the scaling limit described
above, and the research of the present paper is along this line. Let us see what previous papers
did on this topic.
The results are more fragmentary than the scalar case. One of the ﬁrst works on the action of
vector ﬁelds has been done in [27] on the 3D Navier-Stokes equations in vorticity form, for the
vorticity ω = ∇u, u being the velocity of the ﬂuid. However, precisely because the eﬀect of the
random stretching term (ω · ∇ek), more precisely
X
k
θN
k (ω · ∇ek) ◦dW k
t
was (and it stills until now) not well understood, this term was neglected and only the transport
X
k
θN
k (ek · ∇ω) ◦dW k
t
was considered (with the need of a projection operator, see [27] for motivation and details).
The result is similar to the scalar case [20], namely a delay of blow-up, relevant because of the
relevance of the equation, but still incomplete because it does not explain what would happen
in the presence of random stretching. See also a generalisation to rough path noise [25] and to
magnetic hydrodynamics [46].

--- Page 7 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
7
Concerning the 3D Navier-Stokes equations, a very important progress appeared recently [2].
It is concerned with the Navier-Stokes equations in velocity form and the noise, of transport
type, is at that level (energy-preserving instead of circulation-preserving as it should be the
transport-stretching noise at the level of vorticity equation, see the foundational work [42]). The
stretching action of such noise is a bit hidden but the mathematical progress is very important
since it shows that a reasonable noise (with some form of stretching) may still regularize the 3D
Navier-Stokes type equations (the result needs an hyperviscosity but of lower degree than the
one of the deterministic theory).
Then three works appeared with explicit inclusion of a random stretching term, all of them
basically assuming that the noise satisﬁes the classical scaling (6) of the scalar case. The ﬁrst
one, [30] deals with a Navier-Stokes type system called 2D-3C, having 3D features but also 2D
simpliﬁcations, which allows one to control the strength of the stretching term; the physics is
motivated by a limit of fast rotating systems. The second one is [7] on a passive magnetic ﬁeld in
a 3D thin domains, where the smallness of one of the three dimensions is a key ingredient for the
control of stretching; the mathematics is quite intricate and thus the result is developed for the
simpliﬁed case of a passive vector ﬁeld. The third one is [9], again on the passive magnetic ﬁeld,
but in a full three dimensional domain. Stretching is full, in a sense, here but the key ingredient
is controlling the solution in a negative Sobolev space, physically speaking at the level of the
magnetic potential. As already said, but crucial for the comparison with the present paper, all
these works try to assume that the noise scales, in N, as in (6), which in particular it means
that we expect a Laplacian coming for the transport, in the limit equation. Heuristically, when
the Laplacian-due-to-transport persists, stretching could be inﬁnite (at least a priori). The ways
to overcome this blow-up of stretching, in the above papers, has been either to constrain it by a
2D-3C structure, or by a smallness parameter related to thin nomains, or controlling the solution
in a negative Sobolev space.
Let us come to the diﬀerent scaling in N used in the present paper, which also appears in [8]
for very diﬀerent purposes (a precise comparison is made below). Here we have stretching of a
passive vector quantity Rt, that in Lagrangian form is written as
X
k
θN
k ∇ek
 XN
t

RN
t ◦dW k
t
(Xt being the position of the polymer), and in Eulerian form as
X
k
θN
k (∇ek (x) r) · ∇f N (x, t) ◦dW k
t
(∇ek is a matrix acting on the vectors RN
t and r respectively). Then we are faced also with the
covariance matrix
CN,r (x, y) =
X
k
 θN
k
2 (∇ek (x) r) ⊗(∇ek (y) r) .
Clearly, since (roughly speaking) |∇ek (x)| ∼|k|, we cannot hope that the classical scaling (6) of
the scalar case holds and simultaneously also the covariance matrix CN,r (x, y) has a ﬁnite limit
in N. For this reason we introduce a diﬀerent scaling w.r.t. (6), where QN (x, y) goes to zero
outside and also on the diagonal with the right speed but CN,r (x, y) satisﬁes, very heuristically,
lim
N→0 CN,r (x, x) = A (r)
lim
N→0 CN,r (x, y) = 0 for x ̸= y

--- Page 8 ---

8
F. FLANDOLI AND Y. TAHRAOUI
where A (r) is the matrix function described in this paper (equal to a multiple of 3 |r|2 I −2r⊗r).
The consequence of this scaling is that no diﬀusion in the x-variable appears, opposite to the
scalar case; but a diﬀusion in r appears, with diﬀusion matrix A (r). In other words, the eﬀect of
transport becomes irrelevant in the scaling limit, while the eﬀect of stretching has a limit which
is a diﬀusion in the length variable r, with a special diﬀusion matrix.
Finally, let us compare the present work with [8]. The work is devoted to a stochastic PDE for
a passive magnetic ﬁeld, subject to a model of turbulence ﬂuid. In [8] it is shown that it is pos-
sible to investigate a Vlasov-type equation, suitably associated to the equation of the magnetic
ﬁeld, prove a diﬀusion limit result for it and deduce informations on the increase of magnetic
ﬁeld, in the scaling regime that controls the derivatives of the stretching used also here. The
two works stem from a similar physical intuition, but the two problems are very diﬀerent, the
present one starting from a Lagrangian description of a polymer, while [8] from the Eulerian
ﬂuid dynamic description of a magnetic ﬁeld. Moreover, the mathematical techniques to deal
with them are completely diﬀerent: in [8] the Vlasov-type equation is investigated in the space
of measures, in the spirit of Young measure solutions, and the technique to prove well posedness
and scaling limit is ultimately based on the properties of the solutions of the original Eulerian
SPDE. On the contrary, in the present paper we analyze the Fokker-Planck equation directly
in a space of functions, with non trivial technical details related to weighted spaces (not used
before in the above mentioned literature on these scaling limit problems).
Structure of the paper. The manuscript is organized as follows: in section 2, we present the
functional and stochastic settings. Then we introduce in section 3 the stochastic FP in Itˆo form
after presenting some properties of the covariance operator. section 4 collects the main results of
our work, the computation of the explicit rotation-invariant solution of the associated stationary
equation of (13). In section 5, we highlight the ideas of the proof and some formal calculations as
well as the technical challenges. section 6 is devoted to the proof of the existence and uniqueness
of quasi-regular solution to the stochastic FP (12). In section 7, we prove the convergence of the
stochastic FP (12) to the limit PDE (13).
2. Notations, definitions and problem formulation
2.0.1. Notations and functional setting. We will consider the periodic boundary conditions with
respect to the spacial variable x, namely x belongs to the 2-dimensional torus T2 = (R/2πZ)2.
On the other hand, the end-to-end vector variable r belongs to R2. Let m ∈N∗and introduce
the following Lebesgue and Sobolev spaces with polynomial weight, namely
L2
r,m(T2 × R2) := {f : T2 × R2 →R :
Z
T2×R2 |f(x, r)|2(1 + |r|2)m/2dxdr := ∥f∥2
L2r,m < ∞},
Hl
r,m(T2 × R2) := {f : T2 × R2 →R :
X
|γ|+|β|≤l
Z
T2×R2 |∂γ
x∂β
r f(x, r)|2(1 + |r|2)m/2dxdr = ∥f∥2
Hlr,m < ∞},
where l ∈N∗. Now, let us precise the functional setting to study (12). We will use the following
notations
H2
r,4(T2 × R2) := V,
L2
r,2(T2 × R2) := H.

--- Page 9 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
9
We recall the deﬁnition of inner products deﬁned on the spaces V and H.
(h, g)V :=
X
|γ|+|β|≤2
Z
T2×R2 ∂γ
x∂β
r h(x, r)∂γ
x∂β
r g(x, r)(1 + |r|2)2dxdr,
∀g, h ∈V ;
(h, g)H :=
Z
T2×R2 h(x, r)g(x, r)(1 + |r|2)dxdr,
∀g, h ∈H;
(h, g) :=
Z
T2×R2 h(x, r)g(x, r)dxdr,
∀g, h ∈L2(T2 × R2).
Since L∞(0, T; H) is not separable, it is convenient to introduce the following space:
L2
w−∗(Ω; L∞(0, T; H)) = {u : Ω→L∞(0, T; H) is weakly-* measurable and E∥u∥2
L∞(0,T;H) < ∞},
where weakly-* measurable stands for the measurability when L∞(0, T; H) is endowed with the
σ-algebra generated by the Borel sets of weak-* topology, we recall that (see [15, Thm. 8.20.3])
L2
w−∗(Ω; L∞([0, T]; H)) ≃
 L2(Ω; L1([0, T]; H′))
′ ,
For y = (y1, y2) ∈R2, y⊥stands for (−y2, y1). We recall the following notations:
• (∇xg)i=1,2 = ( ∂g
∂xi
)i=1,2; (∇rg)i=1,2 = ( ∂g
∂ri
)i=1,2 for scalar function g.
• (∇xg)i,j=1,2 = ( ∂gi
∂xj
)i,j=1,2; (∇rg)i,j=1,2 = (∂gi
∂rj
)i,j=1,2 for vector valued function g.
• ∆xg =
2
X
i=1
∂2g
∂2xi
; ∆rg =
2
X
i=1
∂2g
∂2ri
for scalar function g.
and divx/rg = ∇x/r · g for vector valued function g. We don’t stress the subscript in ∇x when it
is clear from the context.
In order to prove a uniqueness results, we will need some regularization kernel. More precisely,
let δ > 0 and ρ be a smooth density of a probability measure on R2, compactly supported in
B(0, 1) and deﬁne the approximation of identity for the convolution on R2 as ρδ(y) = 1
δ2ρ(y
δ )
(We also assume that ρ is radially symmetric). Since we are working on T2 × R2, we recall that
for any integrable function g on T2, g can be extended periodically to a locally integrable func-
tion on the whole R2 and convolution ρδ∗g is meaningful and ρδ∗g is still a C∞-periodic function.
Finally, throughout the article, we denote by C, Ci, i ∈N, generic constants, which may vary
from line to line.
2.0.2. Assumptions on the noise. Consider Z2
0 := Z2 −{(0, 0)} divided into its four quadrants
(write k = (k1, k2))
K++ =

k ∈Z2
0 : k1 ≥0, k2 > 0
	
;
K−+ =

k ∈Z2
0 : k1 < 0, k2 ≥0
	
K−−=

k ∈Z2
0 : k1 ≤0, k2 < 0
	
;
K+−=

k ∈Z2
0 : k1 > 0, k2 ≤0
	
and set
K+ = K++ ∪K+−;
K−= K−+ ∪K−−and K = K+ ∪K−.

--- Page 10 ---

10
F. FLANDOLI AND Y. TAHRAOUI
Let (Ω, F, (Ft)t, P) be a complete ﬁltered probability space. Deﬁne
σN
k (x) = θN
k
k⊥
|k| cos k · x,
k ∈K+,
σN
k (x) = θN
k
k⊥
|k| sin k · x,
k ∈K−
where
θN
k =
a
|k|2,
N ≤|k| ≤2N,
N ∈N∗;
θN
k = 0
elsewhere.
This is the main assumption about the shell structure of the noise; and a is a positive constant
measuring the intensity. Since θN
k depends only on |k| , sometimes we write θ|k|. Notice that
∂iσα
k (x) = −θk
ki
 k⊥
α
|k|
sin k · x,
k ∈K+,
α, i = 1, 2,
∂iσα
k (x) = θk
ki
 k⊥
α
|k|
cos k · x,
k ∈K−.
Let us also consider a family (W k
t )
k∈Z2
0
t
of independent Brownian motions on the probability
space (Ω, F, P). On the same probability space we shall soon assume that there exists another
independent 2-dimensional Brownian motion (Wt)t.
2.0.3. Dense subsets in the space L2(Ω). The purpose of this part is to recall a density result,
which will play a crucial role in subsection 6.3 and subsubsection 6.3.1. Namely, we will prove
that uniqueness holds a particular class of solution, see Deﬁnition 5. It is sometimes called
Wiener uniqueness and was used for instance by [44, 52, 56, 18, 34]. For that, let Gt be the
ﬁltration associated with (W k
t )
k∈Z2
0
t
namely Gt = σ{W k
s ; s ∈[0, t], k ∈Z2
0}, and denote by Gt its
completed ﬁltration2. For T > 0, let us introduce
H = L2(Ω, GT, P),
Mn = {k ∈Z2
0;
|k| ≤n}
G =
[
n∈N
Gn;
Gn = {g = (gk)k∈Mn; gk ∈L2(0, T);
∀k ∈Mn}.
For n ∈N, g ∈Gn, we set
eg(t) = exp
  X
k∈Mn
Z t
0
gk(s)dW k(s) −1
2
X
k∈Mn
Z t
0
|gk(s)|2ds

, for t ∈[0, T];
D = {eg(T);
g ∈G}.
From Itˆo formula, we get deg(t) =
X
k∈Mn
gk(t)eg(t)dW k(t). Based on the Wiener chaos decompo-
sition, we recall the following result, see [54, Ch. 1].
Lemma 1. D is dense in H.
2.0.4. Lagrangian description and stochastic Fokker-Planck equation. Let Xt ∈R2 and Rt ∈R2
be the position and end-to-end vector of the polymer. In the Introduction we have generically
stated that they satisﬁes (1). Here we shall be more speciﬁc. Let (Xt, Rt) satisfying



dRt
= ∇u(Xt, t)Rtdt −1
β Rtdt +
√
2σdWt,
dXt
= u(Xt, t)dt,
(7)
2We assume that F0 contains all the P-null subset of Ω.

--- Page 11 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
11
where ∇is the gradient with respect to x-variable. We assume that the velocity ﬁeld u is the sum
of a large scale divergence-free component uL(x, t) (deterministic, with a reasonable smoothness
speciﬁed below) plus a stochastic small-scale component, precisely given by the noise coeﬃcients
introduced above, in other words
u(x, t) := uN(x, t) = uL(x, t) + ◦
X
k∈K
σN
k (x)∂tW k,
(8)
where we choose the Stratonovich multiplication both in virtue of Wong-Zakai principle (a white
noise is the idealization of smooth noise) and because of conservation laws. Since the Brownian
motions (Wt)t, due to thermal force( microscopic level), in (7) acts on a very short time scale and
also that the polymer length is much smaller than the viscous length of the turbulent ﬂow, we
write ﬁrstly the FP equations with respect to it, with quenched velocity. Then we use the random
velocity given by (8) in the resulting FP equation, with Brownian motions (W k
t )k∈K
t
having a
diﬀerent time scale (mesoscopic/macroscopic level).
Formally speaking, we may associate a
stochastic Fokker-Planck equation in Stratonovich form:







∂tf N(x, r, t)
+divx(uL(x, t)f N(x, r, t)) + divr((∇uL(t, x)r −1
βr)f N(x, r, t)) = σ2∆rf N(x, r, t)
−P
k∈K σN
k .∇xf N(x, r, t) ◦∂tW k −P
k∈K(∇σN
k r).∇rf N(x, r, t) ◦∂tW k
f N|t=0
= f0,
(9)
where we have used the properties divx(σN
k ) = 0, k ∈K, divx(uL) = 0 and divr(∇σN
k r) = 03.
Therefore, (9) will be used as the main equation we study in this work.
Before we formulate rigorously the meaning of the equation (9), let us rewrite the previous
equation (formally) from the Stratonovich to the Itˆo form. The question is the form of the
Itˆo-Stratonovich corrector. This computations requires some additional care with respect to
previously known cases developed in the literature, hence we devote to it a separate section.
3. Itˆo-Stratonovich correctors
Let ψ be a given smooth function and set Q(x, y) := P
k∈K σN
k (x)⊗σN
k (y). In this part, we will
write the Itˆo form associated with (9) when Q is space-homogeneous and has a mirror symmetry
property.
Denote by Lkψ = −(σN
k .∇xψ+(∇σN
k r).∇rψ) then the corrector term is given by 1
2
P
k∈K LkLkψ.
Recall that divx(σN
k ) = 0 and let us compute LkLkψ.
LkLkψ = −(σN
k .∇xLkψ + (∇σN
k r).∇rLkψ)
=(σN
k .∇x(σN
k .∇xψ + (∇σN
k r).∇rψ) + (∇σN
k r).∇r(σN
k .∇xψ + (∇σN
k r).∇rψ)
=divx((σN
k ⊗σN
k )∇xψ) + divr(((∇σN
k r) ⊗(∇σN
k r))∇rψ)
+ σN
k .∇x((∇σN
k r).∇rf) + (∇σN
k r).∇r(σN
k .∇xψ).
3divr(∇σN
k r) = 0 is consequence of divx(σN
k ) = 0.

--- Page 12 ---

12
F. FLANDOLI AND Y. TAHRAOUI
Lemma 2. Assume the noise is space-homogeneous i.e. Q(x, y) = Q(x−y) and Q(x, x) = Q(0),
be a constant matrix, then
I(ψ) = I1(ψ) + I2(ψ) =
X
k∈K
σN
k .∇x((∇σN
k r).∇rψ) + (∇σN
k r).∇r(σN
k .∇xψ)
= 2
2
X
l,γ,i=1
∂xγQi,l(0)∂xl(rγ∂riψ).
If moreover Q has the mirror symmetry property i.e. Q(x) = Q(−x), then I(ψ) = 0.
Proof. Let ψ be a smooth function (we drop the dependence of σk on N here for the simplicity
of notation). We have
I1(ψ) =
X
k∈K
2
X
l,γ,i=1
σl
k∂xl(∂xγσi
krγ∂riψ)
=
X
k∈K
2
X
l,γ,i=1
σl
k(∂xl∂xγσi
k)rγ∂riψ +
X
k∈K
2
X
l,γ,i=1
σl
k∂xγσi
k∂xl(rγ∂riψ).
First, let us compute the second term in the last equation. We have
X
k∈K
σl
k(y)∂xγσi
k(x) = ∂xγ
X
k∈K
σl
k(y)σi
k(x) = ∂xγQi,l(x −y),
which gives ( we recall that Q is space-homogeneous)
X
k∈K
σl
k(x)∂xγσi
k(x) = ∂xγQi,l(0).
(10)
Thus
X
k∈K
2
X
l,γ,i=1
σl
k∂xγσi
k∂xl(rγ∂riψ) =
2
X
l,γ,i=1
∂xγQi,l(0)∂xl(rγ∂riψ). Next, let us compute I2
I2(ψ) =
X
k∈K
(∇σN
k r).∇r(σN
k .∇xψ) =
X
k∈K
2
X
l,γ,i=1
∂xγσi
krγ∂ri(σl
k∂xlψ)
=
X
k∈K
2
X
l,γ,i=1
∂xγσi
kσl
k∂xl(rγ∂riψ) =
2
X
l,γ,i=1
∂xγQi,l(0)∂xl(rγ∂riψ).
Now, let us prove that the ﬁrst part of I1 vanishes. Namely
X
k∈K
2
X
l,γ,i=1
σl
k(∂xl∂xγσi
k)rγ∂riψ =
2
X
γ,i=1
 
2
X
l
X
k∈K
σl
k∂xl∂xγσi
k
!
rγ∂riψ = 0.
It is suﬃcient to show that
2
X
l
X
k∈K
σl
k∂xl∂xγσi
k = 0. Indeed, notice that
2
X
l
X
k∈K
σl
k∂xl∂xγσi
k =
2
X
l
∂xγ
X
k∈K
σl
k∂xlσi
k −
2
X
l
X
k∈K
∂xγσl
k∂xlσi
k = −
2
X
l
X
k∈K
∂xγσl
k∂xlσi
k,

--- Page 13 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
13
where we used similar arguments to the one used to obtain (10) to get
X
k∈K
σl
k(x)∂xlσi
k(x) = ∂xlQi,l(0) and ∂xγ
X
k∈K
σl
k∂xlσi
k = 0.
On the other hand, note that
2
X
l
X
k∈K
∂xγσl
k∂xlσi
k =
2
X
l
∂xl
X
k∈K
∂xγσl
kσi
k −
X
k∈K
∂xγ(
2
X
l
∂xlσl
k)σi
k =
2
X
l
∂xl
X
k∈K
∂xγσl
kσi
k,
since divx(σk) = 0. Again, note that P
k∈K ∂xγσl
kσi
k = ∂xγQl,i(0). Therefore
∂xl
X
k∈K
∂xγσl
kσi
k = ∂xl(∂xγQl,i(0)) = 0.
Summing up, we get I(ψ) = 2 P2
l,γ,i=1 ∂xγQi,l(0)∂xl(rγ∂riψ). If Q(x) = Q(−x) and Q is smooth
function, we see that ∂xγQi,l(0) = 0 and the second part of Lemma 2 follows.
□
Moreover, the correctors have a special form.
Lemma 3. The following equalities hold
1
2divx(
X
k∈K
(σN
k ⊗σN
k )∇xf) = 1
2
X
k∈K++
(θN
|k|)2∆xf := αN∆xf,
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

= A(r) + O( 1
N )P(r),
where A(r) = kT(3 |r|2 I −2r ⊗r) = kT(|r|2 I + 2r⊥⊗r⊥), kT = π log(2)
8
a2, r = (r1, r2) and P
is a polynomial of second degree.
Proof. Let us simplify the expressions of
S(f) := 1
2divr(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rf) and B(f) := 1
2divx(
X
k∈K
(σN
k ⊗σN
k )∇xf).
First, we consider the term B. Recall that
σN
k (x) = θN
|k|
k⊥
|k| cos k · x,
k ∈K+,
σN
k (x) = θN
|k|
k⊥
|k| sin k · x,
k ∈K−.
We have
X
k∈K
σN
k ⊗σN
k =
X
k∈K+
(θN
|k|)2k⊥⊗k⊥
|k|2
cos2 k · x +
X
k∈K−
(θN
|k|)2k⊥⊗k⊥
|k|2
sin2 k · x
(k ∈K−→−k ∈K+) =
X
k∈K+
(θN
|k|)2k⊥⊗k⊥
|k|2
(k ∈K+−→k⊥∈K++) =
X
k∈K++
(θN
|k|)2
k⊥⊗k⊥
|k|2
+ k ⊗k
|k|2

(K+ = K++ ∪K+−).
Thus P
k∈K σN
k ⊗σN
k = P
k∈K++(θN
|k|)2I;
I =

1
0
0
1

and therefore
1
2divx(
X
k∈K
(σN
k ⊗σN
k )∇xf) = 1
2
X
k∈K++
(θN
|k|)2∆xf := αN∆xf.

--- Page 14 ---

14
F. FLANDOLI AND Y. TAHRAOUI
On the other hand, let us present some properties of S. We have (with slight abuse of notation
we use σk instead of σN
k )
 X
k∈K
(∇σkr) ⊗(∇σkr)
!
i,l
=
2
X
j,α=1
X
k∈K
(∂xjσi
krj∂xασl
krα)
=
X
k∈K+
(θN
|k|)2(k · r)2k⊥⊗k⊥
|k|2
sin2 k · x +
X
k∈K−
(θN
|k|)2(k · r)2k⊥⊗k⊥
|k|2
cos2 k · x
(k ∈K−→−k ∈K+) =
X
k∈K+
(θN
|k|)2(k · r)2k⊥⊗k⊥
|k|2
= a2
X
k∈K+
N≤|k|≤2N
1
|k|6(k · r)2k⊥⊗k⊥.
Now, let us compute
X
k∈K+
N≤|k|≤2N
1
|k|6(k · r)2k⊥⊗k⊥. Note that
X
k∈K+
N≤|k|≤2N
1
|k|6(k · r)2k⊥⊗k⊥= 1
N2
X
k∈K+
1≤|k|
N ≤2
N6
|k|6
1
N2(k · r)2 1
N2(k⊥⊗k⊥).
Note that hr(x) = 1
x6(x · r)2(x⊥⊗x⊥) is smooth function for 1 ≤|x| ≤2. By using Riemann
sum, we get
1
N2
X
k∈K+
1≤|k|
N ≤2
N6
|k|6
1
N2(k · r)2 1
N2(k⊥⊗k⊥) =
Z
D
hr(x)dx + O( 1
N )P(r),
where D = {x = (|x| cos(ϕ), |x| sin(ϕ)) : 1 ≤|x| ≤2 and ϕ ∈Dπ :=]0, π
2 ]∪]3π
2 , 2π]} and P is a
polynomial of second degree. On the other hand, we have
Z
D
hr(x)dx =
Z 2
1
1
z
Z
Dπ
(r1 cos(ϕ) + r2 sin(ϕ))2

sin2(ϕ)
−sin(ϕ) cos(ϕ)
−sin(ϕ) cos(ϕ)
cos2(ϕ)

dϕdz.
Let us compute the following integral
I(r) :=
Z
Dπ
(r1 cos(ϕ) + r2 sin(ϕ))2

sin2(ϕ)
−sin(ϕ) cos(ϕ)
−sin(ϕ) cos(ϕ)
cos2(ϕ)

dϕ.
A standard integration with respect to ϕ gives
I(r) = π
8

3 |r|2 −2r2
1
−2r1r2
−2r1r2
3 |r|2 −2r2
2

; r = (r1, r2).
Since
Z 2
1
1
zdz = log(2), we get the ﬁnal expression of A(r).
□
Remark 4. When θN
k =
a
|k|2 if N ≤|k| ≤2N, N ∈N∗and θN
k = 0 elsewhere, we get
0 < π
64
a2
N3 ≤αN ≤π
4
a2
N3 < a2 and αN →0.
(11)

--- Page 15 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
15
Based on these two lemmata, the Itˆo form (still formulated only fomally) of the stochastic
Fokker Planck equation (9), by assuming that the noise is space-homogeneous and satisﬁes mirror
symmetry property, is given by4













df N + divx(uL(x, t)f N)dt + divr((∇uL(t, x)r −1
βr)f N)dt
= σ2∆rf Ndt −P
k∈K σN
k .∇xf NdW k −P
k∈K(∇σN
k r).∇rf NdW k
+αN∆xf Ndt + 1
2divr(P
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rf N)dt
f N|t=0 = f0.
(12)
where
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

= A(r) + O( 1
N )P(r).
3.0.1. Assumptions on large scale component. Let T > 0. In the following, we assume that
uL ∈C([0, T], C2(T2; R2)) such that divx(uL) = 0.
4. Main results
Following [56, 18, 34]. We introduce the concept of ”quasi-regular weak solution” to (12),
where we prove the well-posedness.
Notice that uniqueness in this class (sometimes called
Wiener uniqueness) is weaker than pathwise uniqueness.
Deﬁnition 5. (Quasi-regular weak solution) Let f0 ∈H and N ∈N.
We say that f N is
quasi-regular weak solution to (12) if f N is (Ft)t-adapted and
(1) f N ∈L2
w−∗(Ω; L∞([0, T]; H)), ∇rf N ∈L2(Ω× [0, T]; H),
(2) P a.s. in Ω: f N ∈Cw([0, T]; H)5,
(3) P-a.s: for any t ∈]0, T] the following equation holds:
Z
T2
Z
R2 f N(t)φdrdx −
Z
T2
Z
R2 f0φdrdx
−
Z t
0
Z
T2
Z
R2 f N(s)

uL(s) · ∇xφ + (∇uL(s)r −1
β r) · ∇rφ

drdxds
= −σ2
Z t
0
Z
T2
Z
R2 ∇rf N(s) · ∇rφdrdxds + αN
Z t
0
Z
T2
Z
R2 f N(s) · ∆xφdrdxds
+
X
k∈K
Z t
0
Z
T2
Z
R2
 f N(s)σN
k .∇xφ + f N(s)(∇σN
k r).∇rφ

drdxdW k(s)
−1
2
Z t
0
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rf N(s)) · ∇rφdrdxds,
for any φ ∈U.
(4) (Regularity in Mean) For all n ∈N∗and each function g ∈Gn, the deterministic function
V N(t, x, r) = E[f N(t, x, r)eg(t)] is a measurable function, which belongs to L∞([0, T]; H)∩
4Recall that f depends on t, x, r, ω and N but we don’t stress the dependence on the above variables for the
simplicity of notation, that is, with slight abuse of notation f N := f N(t, x, r, ω).
5Cw([0, T ]; H) denotes the Bochner space of weakly continuous functions with values in H.

--- Page 16 ---

16
F. FLANDOLI AND Y. TAHRAOUI
Cw([0, T]; H) and ∇rV N ∈L2([0, T]; H) and satisﬁes the following equation
dV N
dt
+ divx([uL −hn]V N) + divr([(∇uLr) −yn] −1
βr)V N)
= σ2∆rV N + αN∆xV N + 1
2divr(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rV N),
in a weak sense (see Proposition 17), where
X
k∈Kn
gkσN
k = hn and
X
k∈Kn
gk(∇σN
k r) = yn, where Kn = {k ∈K : min(n, N) ≤|k| ≤max(2N, n)}.
Remark 6. The point (3) in Deﬁnition 5 is satisﬁed for larger class of test functions, namely
φ ∈V thanks to the regularity properties of f N.
The main results are given by the following theorems.
Theorem 7. There exists at least one solution f N to (12) in the sense of Deﬁnition 5. Moreover,
(f N)N and (∇rf N)N are bounded in L2
w−∗(Ω; L∞([0, T]; H)) and L2(Ω× [0, T]; H) respectively.
Proof. See subsection 6.2.
□
Theorem 8. Under the assumptions of Theorem 7, let f N
i , i = 1, 2, be two quasi-regular weak
solutions of (12) with the same initial data f0. Assume that (f N
i (t), ϕ) is Gt-adapted, for both
i = 1, 2, for any ϕ ∈V . Then f N
1 = f N
2 .
Proof. See subsubsection 6.3.1.
□
Concerning the scaling limit as N →+∞, we have
Theorem 9. There exists a new probability space, denoted by the same way (for simplicity)
(Ω, F, P), f ∈L2
w−∗(Ω; L∞([0, T]; H))), ∇rf ∈L2(Ω; L2([0, T]; H))) such that the following con-
vergence holds (up to a sub-sequence): f N →f in C([0, T]; U′)
P −a.s. and
f N ⇀f in L2
w−∗(Ω; L∞([0, T]; H))),
∇rf N ⇀∇rf in L2(Ω; L2([0, T]; H)).
Moreover f is the unique solution of the following problem: P-a.s.
Z
T2
Z
R2 f(x, r, t)φ(x)ψ(r)drdx −
Z
T2
Z
R2 f0(x, r)φ(x)ψ(r)drdx
(13)
=
Z t
0
Z
T2
Z
R2 f(x, r, s)

uL(x, s) · ∇xφ(x)ψ(r) + (∇uL(s, x)r −1
β r) · ∇rψ(r)φ(x)

drdxds
−σ2
Z t
0
Z
T2
Z
R2 ∇rf(x, r, s) · ∇rψ(r)φ(x)drdxds −1
2
Z t
0
Z
T2
Z
R2 A(r)∇rf(x, r, s)) · ∇rψ(r)φ(x)drdxds,
for any φ ∈C∞(T2) and ψ ∈C∞
c (R2) and A(r) is given in Lemma 3.
Proof. See subsubsection 7.2.1 for the existence proof and Lemma 31 for the uniqueness.
□
Remark 10. By taking into account the regularity of f, (13) can be written as









∂tf(x, r, t)
+divx(uL(x, t)f(x, r, t)) + divr((∇uL(t, x)r −1
β r)f(x, r, t))
= σ2∆rf(x, r, t) + 1
2divr(A(r)∇rf(x, r, t))
f|t=0
= f0,
(14)

--- Page 17 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
17
in Y′-sense, where Y = {ϕ ∈H : ∇rϕ ∈H, ∇xϕ ∈L2(T2 × R2)}.
Moreover, since f ∈
L∞(0, T; H) and f ∈C([0, T]; U′), we get f ∈Cw([0, T]; H) P-a.s.( see [62, Lem. 1.4 p. 263]).
• Since (14) is Fokker-Planck equation of (15) then f ≥0 and d
dt
R
T2×R2 f(t, x, r)dxdr = 0 if
f0 ≥0 and f0 ∈L1(T2 × R2).
Remark 11. (The limit FP, Lagrangian description and macroscopic equation)
• From Lemma 3, we get for each r ∈R2
A(r) = a2π log 2
8
|r|2r ⊗r
|r|2 + 2a2π log 2
8
|r|2
r⊥⊗r⊥
|r|2

.
Therefore A(r) = Q(r)Q(r), where Q(r) = a√π log 2
2
√
2
r ⊗r
|r|
+
√
2r⊥⊗r⊥
|r|

. Notice that Q(r) is
a symmetric, non negative matrix for each r ∈R2 and the function r →Q(r) is Lipschitz with
linear growth.
• Since for each i ∈{1, 2}, P2
j=1 ∂jAi,j(r) = 0, if f
W and f
f
W are 2D independent Brownian
motions, then the stochastic diﬀerential equation (SDE)



dXt
= uL(t, Xt)dt;
X0 = x
dRt
= (∇uL(t, Xt)Rt −1
βRt)dt + Q(Rt)df
f
W t +
√
2σdf
Wt;
R0 = r,
(15)
has (14) as Fokker-Planck equation.
• Deﬁne T = Er(Rt ⊗Rt), a standard computations gives that T satisﬁes



∂tT + uL · ∇T = (∇uL)T + T(∇uL)t −2
β(T −kTI) + EA(Rt)
T|t=0 = T0,
(16)
which means that TN solution to (5) converges weakly to T in appropriate (weak) sense and the
turbulent velocity generates the term EA(Rt), as N →+∞, at the macroscopic level.
Let us brieﬂy interpret the previous results. The additional term Q(Rt)df
f
W t in the stochastic
equation contributes to a higher dispersion of the values of Rt, increasing the variance; and not
in a ”Gaussian” way, since the diﬀusion matrix depends on Rt and its quadratic form evaluated
in the Rt direction increases with Rt. This is coherent with the power law result for the stationary
solution illustrated in the next subsection. Similarly, the additional term ErA(Rt) in the equation
for the tensor Er(Rt ⊗Rt) is non-negative deﬁnite, mostly positive deﬁnite, hence it contributes
to a higher value of ∂tT hence to an increase of Rt, coherent with the picture above: turbulent
stretching statistically increases polymer length.
Remark 12. It is worth mentioning that we consider the Hookean model. If we consider the
”Finitely Extensible Nonlinear Elastic (FENE)” model, namely replace 1
βRt in (1) by 1
β
Rt
1−|Rt|2/b,
where b is a parameter denote the maximal length of the polymer.
Then, the analysis must
be considered in a bounded domain with respect to r-variable with the appropriate boundary
conditions, see e.g. [51]. It is interesting to extend our result to the FENE case. It seems that
the scaling limit equation should have similar features as the current one. However, since it
requires signiﬁcant changes, this will be considered in a future work.

--- Page 18 ---

18
F. FLANDOLI AND Y. TAHRAOUI
4.1. Stationary solutions and power-law tail. The aim of this section is to discuss ”for-
mally” that the limit PDE (13) exhibits interesting features of the power-law tail predicted in the
physical literature, see for example [4]. More rigorous results and discussions will be the subject
of a future work. We consider the limit equation (13) in the simplest case uL = 0 and look for
stationary solutions f(r), independent of x. We look for rotation-invariant and non-negative
solutions f (r) = g (|r|), so that f should satisfy
kT divr
1
2
 3 |r|2 Id −2r ⊗r

∇f (r) + σ2
kT
∇f (r) +
r
βkT
f (r)

= 0.
Then, since ∇f (r) =
r
|r|g′ (|r|) and kT > 0 we get
divr
 
(|r|2
2 + σ2
kT
)∇f (r) +
r
βkT
f (r)
!
= 0.
(17)
Set
1
βkT = α and p(r) = |r|2
2 + σ2
kT . Then we can write (17) as follows
divr
 p1−α(r)∇[pα(r)f (r)]

= 0.
(18)
If f is smooth function, we can multiply (18) by pα(r)f and integrate over R2 to get
Z
R2 p1−α(r)|∇(pα(r)f (r))|2dr = 0.
Since σ2
kT
> 0, the last equality implies the existence of C ∈R such that pα(r)f (r) = C. Thus,
since we are looking for positive nontrivial solution, we obtain
f (|r|) = Cp−α(r) = C
 
|r|2
2 + σ2
kT
!−
1
βkT
, C > 0.
In relation to physical literature, e.g. [4, eqn.(11)]. Let us just write the last formula only in |r|,
namely
f (|r|) ∼|r|−
2
βkT = |r|−(
2
βkT −1)−1 = |r|−γ−1 ,
γ =
2
βkT
−1.
(19)
Notice that the power γ depends on the interpretable constants, the relaxation time of the
polymer β and the number kT proportional to the square-intensity of the turbulent eddies. Let
us make some comments about the formula (19).
• The case γ =
2
βkT −1 < 0 ⇔2 < βkT : f is not integrable and larger values of |r| are
more probable, which means that the most of polymers have large size and the polymers
are in stretched state. This state holds either when the relaxation time β is large or the
intensity kT of the turbulent ﬂuid is large.
• The case γ =
2
βkT −1 > 0 ⇔βkT < 2 : f is integrable and thus the normalized f is PDF,
in other words, most polymers have an equilibrium size and the Polymers are in coil state.
the last expression of f conﬁrms that when either the relaxation time is small (namely
the polymer is fast in recovering its equilibrium position) or the intensity kT of the tur-
bulent ﬂuid is small then the polymers tends to be in coil state.

--- Page 19 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
19
• The case γ =
2
βkT −1 = 0 ⇔βkT = 2 : The power γ changes the sign and as discussed
in [4], this can be interpreted as the criterion for the coil-stretch transition.
• As mentioned in Introduction, we recall that the power tail is related to Lyapunov ex-
ponent λ of the turbulent ﬂow, which is not trivial to compute in general but one would
like also to predict it. From [4], one extracts the following link between λ and γ:
i. If λ increases then γ decreases.
ii. γ changes its sign at λ = 1
β.
iii. As λ tends to zero, γ tends to inﬁnity.
From (ii), we get that γ changes the sign at kT
2 = 1
β = λ. Moreover, as λ is related to the
turbulent ﬂow and by combining (i) and (iii), we can say that the Lyapunov exponent λ
is our model of turbulent ﬂow is λ = KT
2 . However, we do not prove such equality ”just
heuristic!”. Finally, in the case of the point (iii), we get strong suppression of the tail,
which is quite natural since in a weak ﬂow the molecules are only weakly stretched.
5. About proofs and mathematical challenges
For the convenience of the reader, let us summarize the outline of the proof and the main
technical diﬃculties we face in proving the main results. The details will be provided in section 6
and section 7. Note that (12) is stochastic Fokker Planck, has a hyperbolic nature with respect
to the space variable x, it cannot regularize the initial condition. Moreover, its well-posedness is
not a standard result and we need to construct a solution in an appropriate sense, see Deﬁnition 5.
The ﬁrst step concerns the construction of weak solutions (see Deﬁnition 5, point (3)) by using
Galerkin approximation scheme. We proceed as follows: we construct an orthonormal basis of
H (the weight used to give sense to the terms including the coeﬃcient with r-variable, r ∈R2).
It’s worth to mention we consider a general setting to prove the existence of solution and up to
a cosmetic modiﬁcations, the same result follows by using other weights e.g. (1 + |r|2)m, m > 1
which corresponds to L2
r,m(T2 × R2) ֒→L1(T2 × R2) if m > 2. The ﬁrst problem concerns the
proof of some a priori estimates, for that we add the extra term Ym given by (29) to control the
term coming from the interaction between the two part of the stochastic integral, in order to get
the desired estimates. Then, we may pass to the limit as m →+∞and construct solution to our
problem, after showing that Ym vanishes as m →+∞(we exploit that Q is space-homogeneous
and has mirror symmetry property). Consequently, we construct weak solution, see Theorem 7.
After that, we face the problem of uniqueness due to lack of regularity with respect to the
space variable x and the presence of noise, which motivates the introduction of the notion ”quasi-
regular weak solution”, which is characterized by the point (4) of Deﬁnition 5 to show uniqueness
in this subclass of solution, see Theorem 8 ( we take the advantage of the linearity of (12)). On
the other hand, we should use commutators estimates and techniques associated with hyperbolic
equations to prove in the beginning the uniqueness of solution to the equation satisﬁed by some
appropriate mean (Deﬁnition 5, point (4)) and we combine that with some density arguments in
the L2-space of random variables to deduce the well-posedness in the sense of Deﬁnition 5. We
recall that this notion of uniqueness is weaker than the classical notion of pathwise uniqueness,
see [34, Rmk. 7]. Another key point concerns the uniform estimate with respect to N, which
follows directly from the construction of the solution since Itˆo formula is classical at the level of
Galerkin approximation in contrast with inﬁnite dimension where the solution f N is not smooth

--- Page 20 ---

20
F. FLANDOLI AND Y. TAHRAOUI
and one needs to be careful in the application of Itˆo formula.
Finally, after obtaining some estimates regarding to N, we can pass to the limit as N →+∞
(in weak sense) by considering the new regime when the noise covariance goes to zero but a
suitable covariance built on derivatives of the noise converges to a non zero limit and we obtain
a degenerate PDE with respect to the variable r, see Theorem 9 where the stationary solution
of the limit equation (13) has a power-law, with an explicit power depending on the friction
parameter β and the number kT ( related to the turbulent kinetic energy), see subsection 4.1.
5.0.1. Formal computations and estimates. Let us present some formal computations related to
(12). Namely, we compute ∥f N∥2, by applying Itˆo formula (formally), we get
∥f N(t)∥2 −∥f0∥2 = 2
Z t
0
(f N(s), uL · ∇xf N(s) + (∇xuLr −1
βr) · ∇rf N(s))ds
−2σ2
Z t
0
∥∇rf N(s)∥2ds −2αN
Z t
0
∥∇xf N(s)∥2ds −
Z t
0
(AN
k (x, r)∇rf N(s), ∇rf N(s))ds
+ 2
X
k∈K
Z t
0
[(f N(s), σN
k .∇xf N(s)) + (f N(s), (∇σN
k r).∇rf N(s))]dW k(s)
+
X
k∈K
Z t
0
∥σN
k .∇xf N(s)∥2 + ∥(∇σN
k r).∇rf N(s)∥2ds + 2
X
k∈K
Z t
0
(σN
k .∇xf N(s), (∇σN
k r).∇rf N(s))ds.
Since divx(uL) = divr(∇xuLr) = divx(σN
k ) = divr(∇σN
k r) = 0, one has
(f N, uL · ∇xf N) = (f N, σN
k .∇xf N) = 0,
(f N, (∇xuLr) · ∇rf N) = (f N, (∇σN
k r).∇rf N) = 0.
On the other hand, since
X
k∈K
Z t
0
∥σN
k .∇xf N(s)∥2ds =
X
k∈K
Z t
0
(σN
k .∇xf N(s), σN
k .∇xf N(s))ds
=
Z t
0
(
X
k∈K
σN
k (x) ⊗σN
k (x)∇xf N(s), ∇xf N(s))ds
=
X
k∈K++
(θN
|k|)2
Z t
0
(∇xf N(s), ∇xf N(s))ds = 2αN
Z t
0
∥∇xf N(s)∥2ds.
Hence −2αN
Z t
0
∥∇xfm(s)∥2ds +
X
k∈K
Z t
0
∥σN
k .∇xfm(s)∥2ds = 0. Similarly, we have
X
k∈K
Z t
0
∥(∇σN
k r).∇rf N(s)∥2ds =
Z t
0
(AN
k ∇rf N(s), ∇rf N(s))ds,
where AN
k is given by
AN
k :=
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

;
(20)

--- Page 21 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
21
thus −
Z t
0
(AN
k ∇rf N(s), ∇rf N(s))ds +
X
k∈K
Z t
0
∥(∇σN
k r).∇rf N(s)∥2ds = 0.
Summing up, we get
∥f N(t)∥2 + 2σ2
Z t
0
∥∇rf N(s)∥2ds −∥f0∥2
≤−2
β
Z t
0
(f N(s), r · ∇rf N(s))ds + 2
X
k∈K
Z t
0
(σN
k .∇xf N(s), (∇σN
k r).∇rf N(s))ds.
On the other hand, notice that
X
k∈K
(σN
k .∇xf N(s), (∇σN
k r).∇rf N(s)) = −(
X
k∈K
(∇σN
k r).∇r(σN
k .∇xf N(s)), f N(s)) = 0,
(21)
since the covariance matrix Q is space-homogeneous and has mirror symmetry property, see
Lemma 2. By using (21), we obtain
∥f N(t)∥2 + 2σ2
Z t
0
∥∇rf N(s)∥2ds ≤∥f0∥2 −2
β
Z t
0
(f N(s), r · ∇rf N(s))ds.
Let us compute the last term of the RHS. We have
(f N, r · ∇rf N) =
2
X
i=1
Z
T2×R2
f N(x, r)ri · ∂rif N(x, r)drdx = 1
2
2
X
i=1
Z
T2×R2
ri∂ri(f N)2(x, r)drdx = −∥f N∥2.
Consequently, ∥f N(t)∥2 + 2σ2
Z t
0
∥∇rf N(s)∥2ds ≤∥f0∥2 + 2
β
Z t
0
∥f N(s)∥2ds. Gr¨onwall lemma
ensures the following: P-a.s.
∀t ≥0 :
∥f N(t)∥2 + 2σ2
Z t
0
∥∇rf N(s)∥2ds ≤∥f0∥2e
2
β t.
(22)
Note that the last inequality (22) is suﬃcient, a priori, to construct a weak solution and also
ensure the uniqueness, since (12) is a linear equation. Unfortunately, (22) is not rigorous. Indeed,
if f N satisﬁes (22) only then we are not able to apply directly Itˆo formula to (12) and we need
either to approximate or regularize (12) in appropriate way and prove the existence of f N and
(22), after passing to the limit with respect to the approximation or regularization parameters.
It turns out that it is not suﬃcient to consider f0 ∈L2(T×R2) and we need more regular initial
data, namely f0 ∈H to construct a weak solution, see Deﬁnition 5. Uniqueness is more delicate,
since (12) has a hyperbolic character with respect to x-variable and we will prove uniqueness in
particular class of solution, see Theorem 8. For the convenience of the reader, let us explain the
arguments that failed when we tried to obtain (22) in rigorous way.
5.0.2. A priori estimates via Galerkin approximation. The ﬁrst step concerns the projection of
(12) onto a ﬁnite dimensional space, see (28). Then, we apply ﬁnite dimensional Itˆo formula
which leads to the presence of the term
X
k∈K
(σN
k · ∇xPm[(∇σN
k r).∇rfm], wj))H
(fm = Pmf N)
(23)
instead of
X
k∈K
(σN
k .∇xf N(s), (∇σN
k r).∇rf N(s)) and (21) is not valid anymore. We remedy this
issue by subtraction this term (23) at the level of Galerkin approximation to get an appropriate

--- Page 22 ---

22
F. FLANDOLI AND Y. TAHRAOUI
estimate, see Lemma 15 and we need to show that lim
m (σN
k · ∇xPm[(∇σN
k r).∇rfm], wj))H = 0
to recover the original problem (12). It’s worth to mention that since r ∈R2 and it acts as
coeﬃcient then we need to use initial data f0 ∈H to prove that the extra term (23) vanishes as
m →+∞, see (46) and one obtains the desired estimates of Lemma 15. We refer to section 6
for more details.
5.0.3. Uniqueness via commutators and quasi-regular weak solution. Once the existence of weak
solution satisfying the points (1),(2) and (3) of Deﬁnition 5 is established, one seeks to prove
the uniqueness of this class of solutions.
Since (12) has an hyperbolic nature, one uses the
commutators estimates in order to prove pathwise uniqueness. Let us explain why using this
technique does not give uniqueness of this class of solution, for that we mention only the terms
that cause problems. Let δ > 0 and ϕ ∈C∞
c (T2 × R2), if we denote X = (x, r) ∈T2 × R2,
ρδ(X) = ρδ(x) and ϕδ := ρδ ∗ϕ then we need to pass to the limit as δ →0 in the equality
1
2E∥[f N(t)]δ∥2 + E
Z t
0
⟨[uL(s) · ∇xf N(s)]δ + [divr(∇uL(s)r −1
βr)f N(s)]δ, [f N(s)]δ⟩ds
=E
Z t
0
⟨σ2[∆rf N(s)]δ + αN[∆xf N(s)]δ, [f N(s)]δ⟩ds
+ 1
2E
Z t
0
⟨[divr
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rf N(s))]δ, [f N(s)]δ⟩ds
+ 1
2
X
k∈K
E
Z t
0
∥[σN
k .∇xf N(s)]δ + [(∇σN
k r).∇rf N(s)]δ∥2ds.
We can estimate all the terms in convenient way except the terms
E
Z t
0
⟨αN[∆xf N(s)]δ, [f N(s)]δ⟩ds + 1
2
X
k∈K
E
Z t
0
∥[σN
k .∇xf N(s)]δ∥2ds
(24)
+
X
k∈K
E
Z t
0
(σN
k .∇xf N(s)]δ, [(∇σN
k r).∇rf N(s)]δ)ds.
The last two terms come from the term 1
2
X
k∈K
E
Z t
0
∥[σN
k .∇xf N(s)]δ + [(∇σN
k r).∇rf N(s)]δ∥2ds.
A priori, we expect that the sum of the ﬁrst two terms in (24) vanishes as δ →0 (balance of
energy of Itˆo Stratonovich corrector) but in order to get that, we need more regularity of f N,
namely ∇xf N ∈L2(T2 × R2), which is not our case. Concerning the last term in (24), it is
expected to disappear due to the space homogeneity and the mirror symmetry of the covariance
Q but also it requires ∇xf N ∈L2(T2 × R2) as well. Consequently, we take the advantage of the
linearity of the equation (12) and we prove uniqueness in weaker sense, see Theorem 8.
6. Existence and uniqueness of solutions to (12)
Our aim is this section is to prove the existence and uniqueness of solution to (12) in the sense
of Deﬁnition 5, namely Theorem 7 and Theorem 8. We divide the proof into several steps. First,
we introduce the Galerkin approximation. Then, we prove some estimates in the appropriate
spaces. Next, we show the existence of analytically weak solution to (12). Finally, we prove the
uniqueness of the class of quasi-regular weak solutions after showing the existence and uniqueness
of the solution to an appropriate mean equation associated with (12), see Proposition 17 and
Lemma 21.

--- Page 23 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
23
6.0.1. Galerkin basis and approximation. We need to construct an orthonormal basis of H such
that all the terms in our approximation scheme are meaningful. For that, note that V ֒→
cont. H.
On the other hand, (V, (·, ·)V ) is a separable Hilbert space. By using [6, Lem. C.1.], there exists
a Hilbert space (U, (·|·)U) such that U ֒→V , U is dense in V and the embedding U ֒→V is
compact. Thus the embedding U ֒→H is also compact and we can construct an orthonormal
basis for H by using the eigenvectors of the compact embeeding operator. More precisely, there
exists an orthonormal basis {wi}i∈N of H such that wi ∈U and satisﬁes
(v, wi)U = λi(v, wi)H,
∀v ∈U,
i ∈N,
(25)
where the sequence {λi}i∈N of the corresponding eigenvalues fulﬁls the properties: λi > 0, ∀i ∈N.
Note that { ewi =
1
√λiwi} is an orthonormal basis for U, see [6, Subsect. 2.3] for similar argument
of construction. Now, let m ∈N∗and denote by Hm = span{w1, · · · , wm} and the operator Pm
deﬁned from U′ to Hm deﬁned by Pm : U′ →Hm;
u 7→Pmu =
m
X
i=1
⟨u, wi⟩U′,Uwi. In particular,
the restriction of Pm to H, denoted by the same way, is the (·, ·)-orthogonal projection from H
to Hm and given by
Pm : H →Hm;
u 7→Pmu =
m
X
i=1
(u, wi)Hwi.
(26)
We notice that ∥Pmu∥H ≤∥u∥H, ∀u ∈H, then ∥Pm∥L(H,H) ≤1.
Remark 13. It is worth to mention that the restriction of Pm to U is also an orthogonal
projection, thanks to (25) and thus ∥Pm∥L(U,U) ≤1.
We have the following continuous embedding U ֒→V ֒→H ֒→L2(T2 × R2). Since U is dense
subset of L2(T2 × R2), we can consider the following compact Lions-Gelfand triple, namely
U ֒→
dense L2(T2 × R2) ≡L2(T2 × R2) ֒→U′.
To simplify the notation, the duality between U and U′ will be denoted ⟨·, ·⟩instead of ⟨·, ·⟩U′,U.
Thus, we have the following equality
⟨f, u⟩= (f, u),
∀f ∈L2(T2 × R2), ∀u ∈U.
(27)
We use Faedo-Galerkin method, we introduce the approximation fm(t) =
m
X
j=1
gmj(t)wj and set
fm(0) = Pmf0 ∈Hm. We consider the following ﬁnite dimensional SDE

--- Page 24 ---

24
F. FLANDOLI AND Y. TAHRAOUI
(fm(t), wj)H −(f0, wj)H −
Z t
0
(fm(s), uL · ∇xwj)Hds −
Z t
0
(fm(s), Ymwj)Hds;
1 ≤j ≤m
(28)
= −
Z t
0
((∇xuLr) · ∇rfm(s), wj)H + 2
β(fm(s), wj)H + 1
β (r · ∇rfm(s), wj)Hds
−
Z t
0
[σ2(∇rfm(s), ∇rwj)H + 2σ2(∇rfm(s), rwj) + αN(∇xfm(s), ∇xwj)H]ds
−1
2
Z t
0
(AN
k ∇rfm(s), ∇rwj)Hds −
Z t
0
(AN
k ∇rfm(s), rwj)ds,
+
X
k∈K
Z t
0
((fm(s), σN
k .∇xwj)H −((∇σN
k r) · ∇rfm(s), wj)H)dW k(s),
where
Ymφ :=
X
k∈K
Pm

(∇σN
k r).∇r(Pm(σN
k .∇xφ)) + (2(∇σN
k r) · r
1 + |r|2
Pm(σN
k .∇xφ)

, ∀φ ∈U.
(29)
Note that (28) is a linear system of SDE, by classical result (see e.g. [55, Chapter V]), we get
the existence and uniqueness of Ft-adapted solution fm ∈C([0, T], L2(Ω; Hm)).
Remark 14. Note that
(fm, Ymwj)H =
X
k∈K
(fm, Pm

(∇σN
k r).∇r(Pm(σN
k .∇xwj)) + 2(∇σN
k r) · r
1 + |r|2
Pm(σN
k .∇xwj)

)H
=
X
k∈K
(fm, (∇σN
k r).∇r(Pm(σN
k .∇xwj)))H + 2(fm, (∇σN
k r) · r
1 + |r|2
Pm(σN
k .∇xwj))H
=
X
k∈K
(σN
k · ∇xPm[(∇σN
k r).∇rfm], wj))H.

--- Page 25 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
25
6.1. A priori estimates. We apply the ﬁnite dimensional Itˆo formula to the process fm to get
∥fm(t)∥2
H −∥Pmf0∥2
H = 2
Z t
0
(fm(s), uL · ∇xfm(s))Hds
(30)
−2
Z t
0
((∇xuLr) · ∇rfm(s), fm(s))H + 2
β∥fm(s)∥2
H + 1
β(r · ∇rfm(s), fm(s))Hds
+ 2
Z t
0
(fm(s), Ymfm)Hds −2
Z t
0
[σ2∥∇rfm(s)∥2
H + 2σ2(∇rfm(s), rfm(s)) + αN∥∇xfm(s)∥2
H]ds
−
Z t
0
(AN
k ∇rfm(s), ∇rfm(s))Hds −2
Z t
0
(AN
k ∇rfm(s), rfm(s))ds
+ 2
X
k∈K
Z t
0
((fm(s), σN
k .∇xfm(s))H −((∇σN
k r) · ∇rfm(s), fm(s))H)dW k(s)
+
X
k∈K
Z t
0
∥PmσN
k .∇xfm(s)∥2
H + ∥Pm(∇σN
k r).∇rfm(s)∥2
Hds
+ 2
m
X
j=1
X
k∈K
Z t
0
(σN
k .∇xfm(s), ej)H((∇σN
k r).∇rfm(s), ej)Hds.
Since divx(uL) = divx(σN
k ) = 0, one has (fm, uL · ∇xfm)H = (fm, σN
k .∇xfm)H = 0. On the other
hand, note that
X
k∈K
Z t
0
∥σN
k .∇xfm(s)∥2
Hds =
X
k∈K++
(θN
|k|)2
Z t
0
(∇xfm(s), ∇xfm(s))Hds = 2αN
Z t
0
∥∇xfm(s)∥2
Hds,
where we used that (σN
k .∇xfm, σN
k .∇xfm)H = (σN
k ⊗σN
k ∇xfm, ∇xfm)H. Therefore
−2αN
Z t
0
∥∇xfm(s)∥2
Hds +
X
k∈K
Z t
0
∥PmσN
k .∇xfm(s)∥2
H ≤0,
since ∥PmσN
k .∇xfm(s)∥2
H ≤∥σN
k .∇xfm(s)∥2
H due to that Pm is the (·, ·)H-orthogonal projection
from H to Hm. Similarly, we have
X
k∈K
Z t
0
∥(∇σN
k r).∇rfm(s)∥2
Hds =
Z t
0
(AN
k ∇rfm(s), ∇rfm(s))Hds,
where AN
k is given by (20), thus
−
Z t
0
(AN
k ∇rfm(s), ∇rfm(s))Hds +
X
k∈K
Z t
0
∥Pm(∇σN
k r).∇rfm(s)∥2
Hds ≤0.

--- Page 26 ---

26
F. FLANDOLI AND Y. TAHRAOUI
On the other hand, note that
m
X
j=1
X
k∈K
Z t
0
(σN
k .∇xfm(s), ej)H((∇σN
k r).∇rfm(s), ej)Hds
=
X
k∈K
Z t
0
(
m
X
j=1
(σN
k .∇xfm(s), ej)Hej, (∇σN
k r).∇rfm(s))Hds
= −
X
k∈K
Z t
0
(fm(s), Pm

(∇σN
k r).∇r(Pm(σN
k .∇xfm(s)) + 2(∇σN
k r) · r
1 + |r|2
Pm(σN
k .∇xfm(s))

)Hds
= −
Z t
0
(fm(s), Ymfm(s))ds.
Summing up, we get
∥fm(t)∥2
H −∥Pmf0∥2
H + 2σ2
Z t
0
∥∇rfm(s)∥2
Hds = −2
Z t
0
((∇xuLr) · ∇rfm(s), fm(s))H
(31)
+ 2
β ∥fm(s)∥2
H + 1
β (r · ∇rfm(s), fm(s))Hds −4σ2
Z t
0
(∇rfm(s), rfm(s))ds
−2
Z t
0
(AN
k ∇rfm(s), rfm(s))ds −2
X
k∈K
Z t
0
((∇σN
k r) · ∇rfm(s), fm(s))HdW k(s).
Let us estimate the terms of the right hand side in (31). First, note that
Z t
0
((∇xuLr) · ∇rfm(s), fm(s))Hds = −
Z t
0
(fm(s), fm(s)(∇xuLr) · r)ds
≤∥∇xuL∥∞
Z t
0
∥fm(s)∥2
Hds.
(32)
A standard integration by parts gives
Z t
0
1
β(r · ∇rfm(s), fm(s))Hds = −1
β
Z t
0
(∥fm(s)∥2
H + (|r|2fm(s), fm(s))ds,
and |
Z t
0
1
β (r·∇rfm(s), fm(s))Hds| ≤2
β
Z t
0
∥fm(s)∥2
Hds. Let us estimate
Z t
0
(∇rfm(s), rfm(s))ds.
Note that
Z t
0
(∇rfm(s), rfm(s))ds = −
Z t
0
(fm(s), fm(s))ds, thus
(33)
−4σ2
Z t
0
(∇rfm(s), rfm(s))ds = 4σ2
Z t
0
∥fm(s)∥2ds.
Next, the term −2
Z t
0
(AN
k ∇rfm(s), rfm(s))ds. Since divr[∇σN
k r] = 0, we get
Z t
0
(AN
k ∇rfm(s), rfm(s))ds =
X
k∈K
Z t
0
((∇σN
k r) · ∇rfm(s), (∇σN
k r) · rfm(s))ds
= −
X
k∈K
Z t
0

((∇σN
k r) · ∇rfm(s), (∇σN
k r) · rfm(s)) + ((∇σN
k r)fm(s), fm(s)∇r[(∇σN
k r) · r])

ds,

--- Page 27 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
27
and 2
Z t
0
(AN
k ∇rfm(s), rfm(s))ds = −
X
k∈K
Z t
0
((∇σN
k r)fm(s), fm(s)∇r[(∇σN
k r) · r])ds. On the
other hand, note that
X
k∈K
Z t
0
((∇σN
k r)fm(s), fm(s)∇r[(∇σN
k r) · r])ds
=
X
k∈K+
Z t
0
(θN
|k|)2|k|2( k
|k| · rk⊥
|k| sin k · xfm(s), fm(s) sin k · x∇r[ k
|k| · rk⊥
|k| · r])ds
+
X
k∈K−
Z t
0
(θN
|k|)2|k|2( k
|k| · rk⊥
|k| cos k · xfm(s), fm(s) cos k · x∇r[ k
|k| · rk⊥
|k| · r])ds
=
X
k∈K+
Z t
0
(θN
|k|)2|k|2( k
|k| · rk⊥
|k|fm(s), fm(s)∇r[ k
|k| · rk⊥
|k| · r])ds
=
X
k∈K+
Z t
0
(θN
|k|)2|k|2

( k
|k| · rk⊥· k
|k|2 fm(s), fm(s)k⊥
|k| · r) + ( k
|k| · rk⊥· k⊥
|k|2
fm(s), fm(s) k
|k| · r)

ds
≤2
X
k∈K+
Z t
0
(θN
|k|)2|k|2∥|r|fm(s)∥2ds ≤
X
k∈K+
N≤|k|≤2N
2
|k|2
Z t
0
∥fm(s)∥2
Hds ≤C
Z t
0
∥fm(s)∥2
Hds,
thus
|
X
k∈K
Z t
0
((∇σN
k r)fm(s), fm(s)∇r[(∇σN
k r) · r])ds| ≤C
Z t
0
∥fm(s)∥2
Hds,
(34)
where C > 0 independent of N satisﬁes P
k∈K+
N≤|k|≤2N
2
|k|2 ≤C. Concerning the stochastic
integral, note that ((∇σN
k r) · ∇rfm(s), fm(s))H = −(fm(s), fm(s)(∇σN
k r) · r)). Recall that
(∇σN
k r)(x) = −k · rθN
|k|
k⊥
|k| sin k · x,
k ∈K+; (∇σN
k r)(x) = k · rθN
|k|
k⊥
|k| cos k · x,
k ∈K−
(35)
and
X
k∈K
Z t
0
(−((∇σN
k r) · ∇rfm(s), fm(s))H)dW k(s) = 2
X
k∈K
Z t
0
((fm(s), fm(s)(∇σN
k r) · r)dW k(s).
By using the Burkholder-Davis-Gundy inequality, we get
2E sup
q∈[0,t]
|
Z q
0
X
k∈K
(fm(s), fm(s)(∇σN
k r) · r)dW k(s)| ≤2E[
Z t
0
X
k∈K
|(fm(s), fm(s)(∇σN
k r)) · r)|2ds]1/2,

--- Page 28 ---

28
F. FLANDOLI AND Y. TAHRAOUI
On the other hand, we have
Z t
0
X
k∈K
|(fm(s), fm(s)(∇σN
k r)) · r)|2ds
=
X
k∈K+
(θN
|k|)2|k|2
Z t
0
(−k
|k| ·
r
(1 + |r|2)(1 + |r|2)1/2fm(s), r · k⊥
|k| sin k · x(1 + |r|2)1/2fm)2ds
+
X
k∈K−
(θN
|k|)2|k|2
Z t
0
( k
|k| ·
r
(1 + |r|2)(1 + |r|2)1/2fm(s), r · k⊥
|k| cos k · x(1 + |r|2)1/2fm(s))2ds
≤
X
k∈K
(θN
|k|)2|k|2
Z t
0
∥(1 + |r|2)1/2fm(s)∥2∥(1 + |r|2)1/2fm∥2ds
≤
X
k∈K
(θN
|k|)2|k|2
Z t
0
∥(1 + |r|2)1/2fm(s)∥4ds =
X
k∈K
N≤|k|≤2N
(θN
|k|)2|k|2
Z t
0
∥fm(s)∥2
H∥fm(s)∥2
Hds
≤
X
k∈K
N≤|k|≤2N
1
|k|2
Z t
0
∥fm(s)∥2
H∥fm(s)∥2
Hds ≤C
Z t
0
∥fm(s)∥2
H∥fm(s)∥2
Hds
≤C sup
q∈[0,t]
∥fm(q)∥2
H
Z t
0
∥fm(s)∥2
Hds,
which gives
Z t
0
X
k∈K
|(fm(s), fm(s)(∇σN
k r)) · r)|2ds ≤C sup
q∈[0,t]
∥fm(q)∥2
H
Z t
0
∥fm(s)∥2
Hds,
(36)
where we used
X
k∈K
N≤|k|≤2N
1
|k|2 ≤C, with C > 0 independent of N. Therefore
2E sup
q∈[0,t]
|
Z q
0
X
k∈K
(fm(s), fm(s)(∇σN
k r) · r)dW k(s)| ≤2E[
Z t
0
X
k∈K
|(fm(s), fm(s)(∇σN
k r)) · r)|2ds]1/2
≤2E[C sup
q∈[0,t]
∥fm(q)∥2
H
Z t
0
∥fm(s)∥2
Hds]1/2
≤ǫE sup
q∈[0,t]
∥fm(q)∥2
H + C
ǫ E
Z t
0
∥fm(s)∥2
Hds,
for any ǫ > 0 (to be chosen later). By using (31) and gathering the previous estimates, we get
(1 −ǫ)E sup
q∈[0,t]
∥fm(q)∥2
H + 2σ2E
Z t
0
∥∇rfm(s)∥2
H
≤∥Pmf0∥2
H + [2∥∇xuL∥∞+ 8
β + 4σ2 + 2C + C
ǫ ]E
Z t
0
∥fm(s)∥2
Hds.
By chosing ǫ = 1
2 and setting
λ = 2[2∥∇xuL∥∞+ 8
β + 4σ2 + 4C],
(37)

--- Page 29 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
29
we obtain
E sup
q∈[0,t]
∥fm(q)∥2
H + 4σ2E
Z t
0
∥∇rfm(s)∥2
H ≤2∥f0∥2
H + λE
Z t
0
∥fm(s)∥2
Hds.
Finally, Gr¨onwall lemma ensures
∀t ≥0 : E sup
q∈[0,t]
∥fm(q)∥2
H + 4σ2E
Z t
0
∥∇rfm(s)∥2
H ≤2∥f0∥2
Heλt.
As a conclusion, we get
Lemma 15. For every m ∈N∗, there exists a unique solution fm ∈C([0, T], L2(Ω; Hm)) to (28),
which is adapted to the ﬁltration and satisfy
∀t ≥0 : E sup
q∈[0,t]
∥fm(q)∥2
H + 4σ2E
Z t
0
∥∇rfm(s)∥2
H ≤2∥f0∥2
Heλt,
(38)
where λ is given by (37).
In order to handle the stochastic integral as N →+∞, it is convenient to show the following.
Lemma 16. The unique solution fm ∈C([0, T], L2(Ω; Hm)) to (28) satisﬁes
∀t ∈[0, T] : E sup
q∈[0,t]
∥fm(q)∥2p
H + (2σ2)pE(
Z t
0
∥∇rfm(s)∥2
H)p ≤C∥f0∥2p
H eCt, ∀1 < p < +∞
(39)
where C > 0 is independent of N and m.
Proof. From (31), by using (32), (33) and (34) we get
∥fm(t)∥2
H + 2σ2
Z t
0
∥∇rfm(s)∥2
Hds ≤∥f0∥2
H + λ
2
Z t
0
∥fm(s)∥2
Hds
+ 2|
X
k∈K
Z t
0
(−((∇σN
k r) · ∇rfm(s), fm(s))H)dW k(s)|.
Let p > 1, we have
∥fm(t)∥2p
H + (2σ2)p(
Z t
0
∥∇rfm(s)∥2
Hds)p ≤Cp[∥f0∥2p
H + [λ
2]ptp−1
Z t
0
∥fm(s)∥2p
H ds
+ 2pCp|
X
k∈K
Z t
0
(−((∇σN
k r) · ∇rfm(s), fm(s))H)dW k(s)|p.
Now, by using Burkholder-Davis-Gundy inequality and (36), we get
2pCpE sup
q∈[0,t]
|
Z q
0
X
k∈K
(fm(s), fm(s)(∇σN
k r) · r)dW k(s)|p
≤2pCpE[
Z t
0
X
k∈K
|(fm(s), fm(s)(∇σN
k r)) · r)|2ds]p/2
≤2pCpCp/2t(p−1)/2E[ sup
q∈[0,t]
∥fm(q)∥2p
H
Z t
0
∥fm(s)∥2p
H ds]1/2
≤ǫE sup
q∈[0,t]
∥fm(q)∥2p
H + (2pCp)2Cptp−1
ǫ
E
Z t
0
∥fm(s)∥2p
H ds,

--- Page 30 ---

30
F. FLANDOLI AND Y. TAHRAOUI
for any ǫ > 0 (to be chosen later). Consequently, there exists C > 0 independent of m and N
such that
(1 −ǫ)E sup
q∈[0,t]
∥fm(q)∥2p
H + (2σ2)pE(
Z t
0
∥∇rfm(s)∥2
Hds)p ≤C[∥f0∥2p
H + (C + C
ǫ )E
Z t
0
∥fm(s)∥2p
H ds.
Hence, (39) follows by choosing ǫ = 1
2 and applying Gr¨onwall lemma.
□
6.2. Existence of solution to (12). We have the following equation of fm(t) = fm(x, r, t):
dfm(t) + Pmdivx(uLfm(t))dt + Pmdivr((∇uLr −1
β r)fm(t))dt
(40)
=
X
k∈K
Pm(σN
k · ∇xPm[(∇σN
k r).∇rfm])dt + σ2Pm∆rfm(t)dt
−
X
k∈K
PmσN
k .∇xf N(t)dW k −
X
k∈K
Pm(∇σN
k r).∇rfm(t)dW k
+ αNPm∆xfm(t)dt + 1
2Pmdivr(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rfm(t))dt,
fm|t=0 = Pmf0.
From (40) we get for 1 ≤j ≤m :
Z
T2
Z
R2 fm(t)wjdrdx −
Z
T2
Z
R2 Pmf0wjdrdx
(41)
−
Z t
0
Z
T2
Z
R2 fm(s)

uL(s) · ∇xwj + (∇uL(s)r −1
β r) · ∇rwj

drdxds
= −
X
k∈K
Z t
0
Z
T2
Z
R2 ∇rfm(s), (∇σN
k r)Pm[σN
k · ∇xwi]drdxds
−σ2
Z t
0
Z
T2
Z
R2 ∇rfm(s) · ∇rwjdrdxds + αN
Z t
0
Z
T2
Z
R2 fm(s) · ∆xwjdrdxds
+
X
k∈K
Z t
0
Z
T2
Z
R2[fm(s)σN
k .∇xwj + fm(s)(∇σN
k r).∇rwj]drdxdW k(s)
−1
2
Z t
0
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rfm(s)) · ∇rwjdrdxds.
Let us pass to the limit in the last equation.
6.2.1. 1ststep. By using Lemma 15, we are able to get the following convergences (up to a
subsequence)
fm ⇀ef in L2(Ω; L2([0, T]; H)),
(42)
fm ⇀∗ef in L2
w−∗(Ω; L∞([0, T]; H))),
(43)
∇rfm ⇀∇r ef in L2(Ω; L2([0, T]; H)),
(44)
On the other hand, from Lemma 16, we obtain also
∀t ∈[0, T] : E sup
q∈[0,t]
∥ef(q)∥2p
H + (2σ2)pE(
Z t
0
∥∇r ef(s)∥2
H)p ≤C∥f0∥2p
H eCt, ∀1 < p < +∞
(45)

--- Page 31 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
31
where C > 0 is independent of N and m.
6.2.2. 2ndstep. For φ ∈U, note that
Z
T2
Z
R2 fm(x, r, t)φ(x, r)dxdr is adapted with respect to
(Ft)t and recall that the space of adapted processes is a closed convex subspace of L2(Ω×[0, T]),
hence weakly closed. Therefore
Z
T2
Z
R2
ef(x, r, t)φ(x, r)dxdr is also adapted and its Itˆo integral
is well deﬁned and bounded. Now, let us consider the following mapping
L : L2(Ω× [0, T]; H) →L2(Ω× [0, T]; R)
fm 7→
X
k∈K
Z t
0
Z
T2
Z
R2 fm(s)(σN
k .∇xφ + (∇σN
k r).∇rφ)drdxdW k(s),
which is linear and bounded. Therefore, by using (42), we infer that
X
k∈K
Z t
0
Z
T2
Z
R2 fm(s)(σN
k .∇xφ + (∇σN
k r).∇rφ)drdxdW k(s)
⇀
X
k∈K
Z t
0
Z
T2
Z
R2
ef(s)(σN
k .∇xφ + (∇σN
k r).∇rφ)drdxdW k(s) in L2(Ω× [0, T]).
6.2.3. 3rdstep. For φ ∈Hm and t ∈[0, T], let us set
Bm(t) :=
Z
T2
Z
R2 fm(t)φdrdx −
X
k∈K
Z t
0
Z
T2
Z
R2 fm(s)(σN
k .∇xφ + (∇σN
k r).∇rφ)drdxdW k(s).
From (41), we write (in distributional sense with respect to t)
d
dtBm =
Z
T2
Z
R2 fm

uL · ∇xφ + (∇uLr −1
β r) · ∇rφ

drdx
−
X
k∈K
Z
T2
Z
R2 ∇rfm(∇σN
k r)Pm[σN
k · ∇xφ]drdx −σ2
Z
T2
Z
R2 ∇rfm · ∇rφdrdxds
+ αN
Z
T2
Z
R2 fm∆xφdrdx −1
2
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rfm) · ∇rφdrdx.

--- Page 32 ---

32
F. FLANDOLI AND Y. TAHRAOUI
Let A ∈F and ξ ∈D(0, T)6, by multiplying the last equation by IAξ and integrating over
Ω× [0, T] we derive
−
Z
A
Z T
0

Bm
dξ
ds

dsdP
=
Z
A
Z T
0
Z
T2
Z
R2 fm(s)

uL(s) · ∇xφ + (∇uL(s)r −1
β r) · ∇rφ

ξ(s)drdxdsdP
−
Z
A
Z T
0
X
k∈K
Z
T2
Z
R2 ∇rfm(s)(∇σN
k r)Pm[σN
k · ∇xφ]ξ(s)drdxdsdP
−
Z
A
Z T
0
σ2
Z
T2
Z
R2 ∇rfm(s) · ∇rφξ(s)drdxdsdP +
Z
A
Z T
0
αN
Z
T2
Z
R2 fm(s) · ∆xφξ(s)drdxdsdP
−
Z
A
Z T
0
1
2
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rfm(s)) · ∇rφξ(s)drdxdsdP,
∀φ ∈Hm.
Now, let us prove the following.
Z
A
Z T
0
X
k∈K
Z
T2
Z
R2 ∇rfm(s)(∇σN
k r)Pm[σN
k · ∇xφ]ξ(s)drdxdsdP →0 as m →+∞.
(46)
Indeed, it’s suﬃcient to pass to the limit with (wi)i∈N as test functions. Thus, for 1 ≤i ≤m,
we recall
−
Z
A
Z T
0
X
k∈K
Z
T2
Z
R2 ∇rfm(s)(∇σN
k r)Pm[σN
k · ∇xφ]ξ(s)drdxdsdP
= −
X
k∈K
E
Z T
0
(∇rfm(s), (∇σN
k r)Pm[σN
k · ∇xwi])1Aξ(s)ds
= E
Z T
0
⟨
X
k∈K
Pm(σN
k · ∇xPm[(∇σN
k r).∇rfm(s)]), wi⟩1Aξ(s)ds
where E denotes the expectation. On the other hand, the following convergence holds
X
k∈K
(∇σN
k r)Pm[σN
k · ∇xwi] →
X
k∈K
(∇σN
k r)σN
k · ∇xwi in L2(T2 × R2).
Indeed, denote by ∥· ∥2 the norm in L2(T2 × R2), we get
∥
X
k∈K
(∇σN
k r)(Pm −I)[σN
k · ∇xwi]∥2
2 ≤
X
k∈K
(θN
|k|)2|k|2∥|r|(Pm −I)[σN
k · ∇xwi]∥2
2
≤
X
k∈K
(θN
|k|)2|k|2∥(Pm −I)[σN
k · ∇xwi]∥2
H
≤
X
k∈K
(θN
|k|)4|k|2∥Pm −I∥2
L(H,H)∥∇xwi∥2
H
≤
X
k∈K
(θN
|k|)4|k|2∥Pm −I∥2
L(H,H)∥wi∥2
U
≤C∥Pm −I∥2
L(H,H)∥wi∥2
U →0,
6D(0, T ) denotes the space of C∞-functions with compact support in ]0, T [.

--- Page 33 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
33
where C > 0 7 and since Pm is an orthogonal projection on H. On the other hand, ∇rfm
converges weakly to ∇r ef in L2(Ω× [0, T] × T2 × R2), thanks to (44). Therefore
lim
m −
Z
A
Z T
0
X
k∈K
Z
T2
Z
R2 ∇rfm(s)(∇σN
k r)Pm[σN
k · ∇xφ]ξ(s)drdxdsdP
= −
X
k∈K
Z
A
Z T
0
(∇r ef(s), (∇σN
k r)σN
k · ∇xwi)ξ(s)dsdP
=
Z
A
Z T
0
( ef(s),
X
k∈K
(∇σN
k r) · ∇rσN
k · ∇xwi)ξ(s)dsdP = 0
∀i ∈N.
Indeed, for given function ψ we have
X
k∈K
(∇σN
k r).∇r(σN
k .∇xψ) =
X
k∈K
2
X
l,γ,i=1
∂xγσi
krγ∂ri(σl
k∂xlψ)
and
X
k∈K
2
X
l,γ,i=1
∂xγσi
krγ∂ri(σl
k∂xlψ) =
X
k∈K
2
X
l,γ,i=1
∂xγσi
kσl
k∂xl(rγ∂riψ) =
2
X
l,γ,i=1
∂xγQi,l(0)∂xl(rγ∂riψ).
Since the covariance matrix Q satisﬁes Q(x) = Q(−x) then ∂xγQi,l(0) = 0. As a result we get
−
Z
A
Z T
0

B dξ
ds

dsdP
=
Z
A
Z T
0
Z
T2
Z
R2
ef(s)

uL(s) · ∇xφ + (∇uL(s)r −1
β r) · ∇rφ

ξ(s)drdxdsdP
−
Z
A
Z T
0
σ2
Z
T2
Z
R2 ∇r ef(s) · ∇rφξ(s)drdxdsdP +
Z
A
Z T
0
αN
Z
T2
Z
R2
ef(s) · ∆xφξ(s)drdxdsdP
−
Z
A
Z T
0
1
2
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇r ef(s)) · ∇rφξ(s)drdxdsdP,
∀φ ∈U,
where
B(t) :=
Z
T2
Z
R2
ef(t)φdrdx −
X
k∈K
Z t
0
Z
T2
Z
R2
ef(s)(σN
k .∇xφ + (∇σN
k r).∇rφ)drdxdW k(s).
Then, taking into account the regularity of ef , we infer that the distributional derivative dB
dt
belongs to the space L2(Ω× [0, T]). Recalling that B ∈L2(Ω× [0, T]), we conclude that
B(·) ∈L2(Ω; C([0, T]).
Considering the properties of Itˆo’s integral, we deduce
Z
T2
Z
R2
ef(t)φdrdx ∈L2(Ω; C([0, T]),
which means that ef ∈L2(Ω; C([0, T]; U′) and therefore ef ∈L2(Ω; Cw([0, T]; H), thanks to (43)
and [62, Lemma. 1.4 p. 263]. We ﬁnish the proof by showing some continuous convergence in
7Recall that
X
k∈K
(θN
|k|)4|k|2 =
X
k∈K
1
|k|6 ≤C.

--- Page 34 ---

34
F. FLANDOLI AND Y. TAHRAOUI
time. Indeed, let ξ ∈C∞([0, t]) for t ∈]0, T] and note that the following integration by parts
formula holds
Z t
0
dB
ds (s)ξ(s)ds = −
Z t
0
B(s)dξ
dsds + B(t)ξ(t) −
Z
T2
Z
R2 f0φdrdxξ(0).
(47)
Now, by standard arguments (see e.g. [64, proof of Prop. 3.] ) we get for any t ∈]0, T],
Z
T2
Z
R2
efm(t)φdrdx ⇀
Z
T2
Z
R2
ef(t)φdrdx in L2(Ω, H), as m →∞.
and ef(0) = f0 in H-sense. In conclusion, there exists a solution in the sense of Deﬁnition 5
( ef = f N to stress the dependence N, since we will pass to the limit as N →+∞in section 7.)
Z
T2
Z
R2 f N(t)φdrdx −
Z
T2
Z
R2 f0φdrdx
−
Z t
0
Z
T2
Z
R2 f N(s)

uL(s) · ∇xφ + (∇uL(s)r −1
β r) · ∇rφ

drdxds
= −σ2
Z t
0
Z
T2
Z
R2 ∇rf N(s) · ∇rφdrdxds + αN
Z t
0
Z
T2
Z
R2 f N(s) · ∆xφdrdxds
+
X
k∈K
Z t
0
Z
T2
Z
R2[f N(s)σN
k .∇xφ + f N(s)(∇σN
k r).∇rφ]drdxdW k(s)
−1
2
Z t
0
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rf N(s)) · ∇rφdrdxds,
for any φ ∈U. In particular, f N is adapted with respect to the given ﬁltration.
6.3. Uniqueness of quasi-regular weak solution. In order to prove (4) in Deﬁnition 5 and
the uniqueness of ”quasi-regular weak solution” to (12), we need ﬁrst to prove the existence and
uniqueness of solution V N to an appropriate mean equation. Namely, we prove the following.
Proposition 17. For any t ∈[0, T], there exists V N(t) = E[f N(t)eg(t)] such that
(1) V N ∈L∞([0, T]; H), ∇rV N ∈L2([0, T]; H) and V N ∈Cw([0, T]; H).
(2) For any t ∈[0, T], it holds
Z
T2
Z
R2 V N(t)φdxdr −
Z
T2
Z
R2 f0φdxdr
=
Z t
0
Z
T2
Z
R2 V N(s)

[uL(s) −hn] · ∇xφ + ([∇uL(s)r −yn] −1
βr) · ∇rφ

drdxds
−
Z t
0
σ2
Z
T2
Z
R2 ∇rV N(s) · ∇rφdrdxds +
Z T
0
αN
Z
T2
Z
R2 V N(s) · ∆xφdrdxds
−
Z t
0
1
2
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rV N(s)) · ∇rφdrdxds,
∀φ ∈V,
Remark 18. A priori, the last point holds for any φ ∈U and by taking into account the regularity
of the solution V N, it holds as well for all φ ∈V.

--- Page 35 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
35
Proof of Proposition 17. Let g ∈Gn, by using Itˆo formula to the product, we get
d[eg(t)fm(t)] + eg(t)Pmdivx(uLfm(t))dt + eg(t)Pmdivr((∇uLr −1
βr)fm(t))dt
=
X
k∈K
eg(t)Pm(σN
k · ∇xPm[(∇σN
k r).∇rfm])dt + σ2eg(t)Pm∆rfm(t)dt
−
X
k∈K
eg(t)PmσN
k .∇xf N(t)dW k −
X
k∈K
eg(t)Pm(∇σN
k r).∇rfm(t)dW k
+ αNeg(t)Pm∆xfm(t)dt + 1
2eg(t)Pmdivr(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rfm(t))dt,
+
X
k∈Mn
fm(t)gk(t)eg(t)dW k(t)
−[
X
k∈Mn
gk(t)eg(t)dW k(t),
X
k∈K
eg(t)PmσN
k .∇xf N(t) + eg(t)Pm(∇σN
k r).∇rfm(t)dW k]
eg(t)fm|t=0 = Pmf0.
Denote Kn = {k ∈K : min(n, N) ≤|k| ≤max(2N, n)} and set Vm(t) = E(fm(t)eg(t)) then
d[Vm(t)] + Pmdivx(uLVm(t))dt + Pmdivr((∇uLr −1
βr)Vm(t))dt
=
X
k∈K
Pm(σN
k · ∇xPm[(∇σN
k r).∇rVm(t)])dt + σ2Pm∆rVm(t)dt
+ αNPm∆xVm(t)dt + 1
2Pmdivr(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rVm(t))dt,
−
X
k∈Kn
PmgkσN
k .∇xVm(t) + Pmgk(∇σN
k r).∇rVm(t)
Vm|t=0 = Pmf0.
Denote
X
k∈Kn
gkσN
k = hn and
X
k∈Kn
gk(∇σN
k r) = yn. Then Vm satisﬁes
dVm
dt + Pmdivx([uL −hn]Vm(t)) + Pmdivr([(∇uLr) −yn] −1
β r)Vm(t))
(48)
=
X
k∈K
Pm(σN
k · ∇xPm[(∇σN
k r).∇rVm]) + σ2Pm∆rVm(t)
+ αNPm∆xVm(t) + 1
2Pmdivr(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rVm(t)),
Vm|t=0 = Pmf0.
(48) is linear system of ODE, by using a classical results (see e.g. [55, Chapter V]) we get
Lemma 19. There exists a unique Vm ∈C([0, T]; Hm) to (48).
Lemma 20. For every m ∈N∗, there exists a unique solution Vm = E[egfm] ∈C([0, T]; Hm) to
(48), which satisfy
∀t ≥0 : sup
q∈[0,t]
∥Vm(q)∥2
H + 4σ2
Z t
0
∥∇rVm(s)∥2
H ≤2∥f0∥2
Heλ(t),
(49)

--- Page 36 ---

36
F. FLANDOLI AND Y. TAHRAOUI
where
λ(t) = [2∥∇xuL∥∞+ 8
β + 4σ2 + 2C]t +
Z t
0
(∥g(s)∥2 + 1)ds < +∞.
Proof. The proof consists of arguments analogous to the proof of Lemma 15 but for the reader’s
convenience, let us sketch it. By applying Itˆo formula with ∥· ∥2
H to the process Vm satisfying
(48), we obtain
∥Vm(t)∥2
H −∥Pmf0∥2
H
= 2
Z t
0
(Vm(s), uL · ∇xVm(s))Hds −2
Z t
0
(Vm(s), hn · ∇xVm(s))Hds −2
Z t
0
((∇xuLr) · ∇rVm(s), Vm(s))H
+ 2
Z t
0
(Vm(s), yn · ∇rVm(s))Hds +
Z t
0
2
β ∥Vm(s)∥2
Hds + 1
β
Z t
0
(r · ∇rVm(s), Vm(s))Hds
+ 2
X
k∈K
Z t
0
(Vm(s), σN
k · ∇xPm[(∇σN
k r))∇rVm(s)])Hds
−2
Z t
0
[σ2∥∇rVm(s)∥2
H + 2σ2(∇rVm(s), rVm(s)) + αN∥∇xVm(s)∥2
H]ds
−
Z t
0
(AN
k (x, r)∇rVm(s), ∇rVm(s))Hds −2
Z t
0
(AN
k (x, r)∇rVm(s), rVm(s))ds
The last equation has similar terms as (30) (without the stochastic integrals and Itˆo correctors)
but with the two new terms
2
Z t
0
(Vm(s), hn · ∇xVm(s))Hds + 2
Z t
0
(Vm(s), yn · ∇rVm(s))Hds.
By noticing that divx(hn) = 0, the ﬁrst term vanishes. Concerning the second one, note that
|yn| ≤|r|
X
|k|≤n
|gk| = |r|∥g∥and
Z t
0
(Vm(s), yn · ∇rVm(s))Hds = −
X
k∈Kn
(Vm(s), gk(∇σN
k r) · rVm(s))ds,
which ensures that
Z t
0
|(Vm(s), yn·∇rVm(s))H|ds ≤
Z t
0
(∥g(s)∥2+1)∥Vm(s)∥2
Hds. Thus, the other
terms can be estimated by similar arguments as in subsection 6.1 and we obtain Lemma 20.
□
By using Lemma 20, we are able to get the following convergences (up to a subsequence)
Vm ⇀eV in L2([0, T]; H),
(50)
Vm ⇀∗eV in L∞([0, T]; H),
(51)
∇rVm ⇀∇r eV in L2([0, T]; H),
(52)
moreover, by using the linearity of the expectation we get eV = E[eg ef] (recall that Vm = E(egfm)
and eg ∈L2(Ω)). Now, we have all the ingredients in hand to argue as in subsection 6.2 and
obtain Proposition 17.
Lemma 21. Let N ∈N∗. Then, the solution V N given by Proposition 17 is unique.

--- Page 37 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
37
Proof of Lemma 21. Let V N
1
and V N
2
be two solutions, with the same initial data, given by
Proposition 17 and denote by V N their diﬀerence. Then for any t ∈]0, T] and φ ∈V , we have
Z
T2
Z
R2 V N(t)φdxdr
(53)
=
Z t
0
Z
T2
Z
R2 V N(x, r, s)

[uL(x, s) −hn] · ∇xφ + ([∇uL(s, x)r −yn] −1
β r) · ∇rφ

drdxds
−
Z t
0
σ2
Z
T2
Z
R2 ∇rV N(x, r, s) · ∇rφdrdxds +
Z T
0
αN
Z
T2
Z
R2 V N(x, r, s) · ∆xφdrdxds
−
Z t
0
1
2
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rV N(x, r, s)) · ∇rφdrdxds.
Since the above equation is understood in weak form, we need ﬁrst to consider an appropriate
regularization of V N, denoted by [V N]δ. Then, take the L2-inner product of the above equation
with [V N]δ and ﬁnally pass to the limit with respect to the regularization parameters δ.
Step 1: Regularization. Let ϕ ∈C∞
c (T2 × R2), if we denote X = (x, r) ∈T2 × R2 and ρδ(X) =
ρδ(x), then ϕδ := ρδ ∗ϕ is an appropriate test function in (53), namely we get
(V N(t), ϕδ)
=
Z t
0
Z
T2
Z
R2 V N(s)

[uL(s) −hn] · ∇xϕδ + ([∇uL(s)r −yn] −1
βr) · ∇rϕδ

drdxds
−
Z t
0
σ2
Z
T2
Z
R2 ∇rV N(s) · ∇rϕδdrdxds +
Z T
0
αN
Z
T2
Z
R2 V N(s) · ∆xϕδdrdxds
−
Z t
0
1
2
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rV N(s)) · ∇rϕδdrdxds.
Since ρ is radially symmetric then the operator of convolution with ρδ is self-adjoint on L2(T2 ×
R2). Thus
([V N(t)]δ, ϕ) +
Z t
0

[(uL(s) −hn) · ∇xV N(s)]δ + +[divr
 (∇uL(s)r −yn −1
β r)V N(s)

]δ, ϕ

ds
=
Z t
0
σ2([∆rV N(s)]δ, ϕ)ds +
Z T
0
αN([∆xV N(s)]δ, ϕ)ds
+
Z t
0
1
2[divr(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rV N(s))]δ, ϕ)ds =
Z t
0
([d(s)]δ, ϕ)ds.
Consider the following space X := {ϕ ∈H; ∇rϕ ∈H} and note that X ֒→L2(T2 × R2) ֒→X′
is Gelfand triple. Since
V N ∈L∞([0, T]; H), ∇rV N ∈L2([0, T]; H),

--- Page 38 ---

38
F. FLANDOLI AND Y. TAHRAOUI
and by using the regularization properties of ρ, one gets that [d(·)]δ ∈L2([0, T]; X′). therefore,
we can set ϕ = [V N(·)]δ to get
1
2∥[V N(t)]δ∥2 +
Z t
0

[(uL(s) −hn) · ∇xV N(s)]δ + [divr
 (∇uL(s)r −yn −1
β r)V N(s)

]δ, [V N(s)]δ

ds
(54)
=
Z t
0
σ2([∆rV N(s)]δ, [V N(s)]δ)ds +
Z T
0
αN([∆xV N(s)]δ, [V N(s)]δ)ds
+
Z t
0
1
2[divr(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rV N(s))]δ, [V N(s)]δ)ds.
Now, let us pass to the limit in the last equality (54).
The proof is based on commutator
estimates and using the properties of (σk)k∈K.
Step 2: Passage to the limit as δ →0. First, recall that V N(·) ∈L2(T2 × R2), by properties of
convolution product, we get lim
δ→0[V N(r, ·)]δ = V N(r, ·) in L2(T2) uniformly for a.e. r ∈R2 and
we get lim
δ→0 ∥[V N(t)]δ∥2 = ∥V N(t)∥2. Next, we will prove the following
lim
δ
Z t
0
⟨[uL(s) · ∇xV N(s)]δ, [V N(s)]δ⟩ds = 0.
(55)
Since divxuL = 0, we get
Z t
0
⟨[uL(s) · ∇xV N(s)]δ, [V N(s)]δ⟩ds
=
Z t
0
⟨ρδ ∗[uL(s) · ∇xV N(s)] −uL(s) · ∇xρδ ∗[V N(s)], ρδ ∗[V N(s)]⟩ds.
Let us introduce the commutator rδ(s) = ρδ ∗[uL(s) · ∇xV N(s)] −uL(s) · ∇xρδ ∗[V N(s)]. Thus,
(55) is a consequence of the following: a.e. s ∈[0, T]
∥rδ(s)∥L2(T2×R2) ≤C ∥∇uL(s)∥∞
V N(s)

L2(T2×R2) ,
(56)
lim
δ rδ(s) = 0 in L2(T2 × R2),
(57)
where C > 0 independent of δ. Indeed, let us show (56), note that
rδ (s, x, r) = −
Z
R2 (uL (x, s) −uL (y, s)) · ∇xρδ (x −y) V N (s, y, r)dy
Consider the following change of variables z = x −y
δ
to get
rδ (s, x, r) = −
Z
R2
uL (y + δz, s) −uL (y, s)
δ
· ∇xρ (z) V N (s, y, r) dz
= −
Z
R2
Z 1
0
∇uL(y + αδz, s)zdα · ∇xρ (z) V N (s, y, r)dz.

--- Page 39 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
39
Thus |rδ (s, x, r) | ≤∥∇uL(s)∥∞
R
R2 |z||∇xρ (z) ||V N (s, y, r) |dz. Since x = y + δz, we get
∥rδ(s)∥2
L2(T2×R2) ≤∥∇uL(s)∥2
∞
Z
R2
Z
T2(
Z
R2 |z||∇xρ (z) ||V N (s, y, r) |dz)2dydr
≤∥∇uL(s)∥2
∞(
Z
R2
Z
T2(
Z
R2 z · ∇xρ (z) V N (s, y, r) dz)2dydr
≤∥∇uL(s)∥2
∞
Z
R2 |z|2|∇xρ (z) |2dz(
Z
R2
Z
T2 |V N (s, y, r) |2dydr,
≤C2∥∇uL(s)∥2
∞∥V N(s)∥2
L2(T2×R2),
since supp[ρ] ⊂B(0, 1) and denoted by C2 =
R
R2 |z|2|∇xρ (z) |2dz < +∞. Concerning (57), we
have
L2(T2 × R2)- lim
δ→0 rδ(s) = −V N(s)
Z
R2 ∇uL(s)z · ∇xρ(z)dz

.
Indeed, we have
Z
R2
Z
T 2 |
Z
R2
Z 1
0
∇uL(y + αδz, s)zdα · ∇xρ (z) V N (s, y, r)dz
−V N(s, x, r)
Z
R2 ∇uL(s, x)z · ∇xρ(z)dz

|2dxdr
=
Z
R2
Z
T 2 |
Z
R2
Z 1
0
∇uL(y + αδz, s)zdα · ∇xρ (z) V N (s, y, r) dz
−
Z
R2 V N(s, x, r)∇uL(s, x)z · ∇xρ(z)dz|2dxdr
≤
Z
R2
Z
T 2
Z
R2
Z 1
0
|∇uL(y + αδz, s)z · ∇xρ (z) V N (s, y, r) dz −V N(s, x, r)∇uL(s, x)z · ∇xρ(z)|2dαdzdxdr
≤
Z
R2
Z
R2
Z
T 2
Z 1
0
|∇uL(y + αδz, s)V N (s, y, r) −V N(s, y + δz, r)∇uL(s, y + δz)|2dαdydr|z|2|∇xρ(z)|2dz
≤2
Z
R2
Z
R2
Z
T 2
Z 1
0
|∇uL(y + αδz, s)V N (s, y, r) −V N(s, y, r)∇uL(s, y)|2dαdydr|z|2|∇xρ(z)|2dz
+ 2
Z
R2
Z
R2
Z
T 2
Z 1
0
|V N(s, y, r)∇uL(s, y) −V N(s, y + δz, r)∇uL(s, y + δz)|2dαdydr|z|2|∇xρ(z)|2dz
= I1
δ + I2
δ .
Using the continuity of translations in L2(T2) for the function V N∇uL, we get lim sup
δ→0
I2
δ = 0
Concerning I1
δ , note that
I1
δ ≤2
Z
R2
Z
R2
Z
T 2
Z 1
0
|∇uL(y + αδz, s) −∇uL(s, y)|2|V N (s, y, r)|2dαdydr|z|2|∇xρ(z)|2dz.
On the other hand, by mean-value theorem we get
|∇uL(y + αδz, s) −∇uL(s, y)| ≤αδ|z|∥uL∥C2

--- Page 40 ---

40
F. FLANDOLI AND Y. TAHRAOUI
Thus I1
δ ≤δ2∥uL∥2
C2
Z
R2
Z
T 2 |V N (s, y, r) |2dydr
Z
R2 |z|4|∇xρ(z)|2dz →0. Finally, since ρ is smooth
density of a probability measure, we get
R
R2 zi∂jρ(z)dz = −δij and so
Z
R2 ∇uL(s)z · ∇xρ(z)dz = −divuL = 0,
which gives (57). The next step is proving the following
lim
δ
Z t
0
⟨[hn(s) · ∇xV N(s)]δ, [V N(s)]δ⟩ds = 0.
(58)
We recall that
X
k∈Kn
gkσN
k = hn and divxhn = 0, hence
Z t
0
⟨[hn(s) · ∇xV N(s)]δ, [V N(s)]δ⟩ds
=
Z t
0
⟨ρδ ∗[hn(s) · ∇xV N(s)] −hn(s) · ∇xρδ ∗[V N(s)], ρδ ∗[V N(s)]⟩ds
Let us introduce the commutator
rh
δ (s) = ρδ ∗[hn(s) · ∇xV N(s)] −uL(s) · ∇xρδ ∗[V N(s)].
(58) is a consequence of the following: a.e. s ∈[0, T]
rh
δ (s)

L2(T2×R2) ≤C ∥g∥
V N(s)

L2(T2×R2) ,
(59)
lim
δ rh
δ (s) = 0 in L2(T2 × R2),
(60)
where C > 0 independent of δ. Indeed, similarly to (56), we get
rh
δ (s, x, r) = −
Z
R2 (hn (x, s) −hn (y, s)) · ∇xρδ (x −y) V N (s, y, r) dy
thus, we obtain (∥· ∥∞denotes the L∞-norm with respect to the x-variable)
∥rh
δ (s)∥2
L2(T2×R2) ≤C2∥∇hn(s)∥2
∞∥V N(s)∥2
L2(T2×R2),
since supp[ρ] ⊂B(0, 1) and denoted by C2 =
R
R2 |z|2|∇xρ (z) |2dz < +∞. On the other hand,
note that
∥∇xhn∥∞≤
X
k∈Kn
|gk|∥∇σN
k ∥∞≤
X
k∈Kn
1
|k||gk| ≤
X
|k|≤n
|gk| := ∥g∥∈L2(0, T).
The proof (60) is analogous to the proof (57) and we omit this detail.
Let us prove that
lim
δ
Z t
0
⟨[divr(∇uL(s)r)V N(s)]δ, [V N(s)]δ⟩ds = 0. Since divr(∇uL(s)r) = 0, we get
Z t
0
⟨[divr(∇uL(s)r)V N(s)]δ, [V N(s)]δ⟩ds
=
Z t
0
⟨divrρδ ∗(∇uL(s)r)V N(s) −divr(∇uL(s)r)ρδ ∗V N(s), ρδ ∗V N(s)⟩ds
= −
Z t
0
⟨ρδ ∗(∇uL(s)r)V N(s) −(∇uL(s)r)ρδ ∗V N(s), ρδ ∗∇rV N(s)⟩ds.

--- Page 41 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
41
On the other hand, note that
 ρδ ∗(∇uL(·)r)V N
(s, x, r) −(∇uL(s, x)r)(ρδ ∗V N)(s, x, r)
=
Z
R2[∇uL(x −y, s) −∇uL(x, s)]rρδ(y)V N(s, x −y, r)dy.
By mean-value theorem we get |∇uL(x −y, s) −∇uL(x, s)| ≤|y|∥uL∥C2 and
|
 ρδ ∗(∇uL(·)r)V N
(s, x, r) −(∇uL(s, x)r)(ρδ ∗V N)(s, x, r)|
≤∥uL∥C2
Z
R2 |y||r|ρδ(y)|V N(s, x −y, r)|dy ≤δ∥uL∥C2
Z
R2 ρδ(y)|r||V N(s, x −y, r)|dy,
since supp[ρ] ⊂B(0, 1). Therefore, we get
Z t
0
|⟨ρδ ∗(∇uL(s)r)V N(s) −(∇uL(s)r)ρδ ∗V N(s), ρδ ∗∇rV N(s)⟩|ds
≤δ∥uL∥C2
Z t
0
∥
Z
R2 ρδ(y)|r||V N(s, x −y, r)|dy∥∥ρδ ∗∇rV N(s)∥ds
≤δ∥uL∥C2
Z t
0
∥ρδ ∗|r||V N(s)||∥∥ρδ ∗∇rV N(s)∥ds
≤δ∥uL∥C2
Z t
0
∥V N(s)|∥H∥∇rV N(s)∥ds →0 as δ →0.
Concerning the term
Z t
0
⟨[divr(ynV N(s))]δ, [V N(s)]δ⟩ds. We recall that
X
k∈Kn
gk(∇σN
k r) = yn.
Since divr(yn) = 0, we have
Z t
0
⟨[divrynV N(s)]δ, [V N(s)]δ⟩ds =
Z t
0
⟨[divrynV N(s)]δ −divryn[V N(s)]δ, [V N(s)]δ⟩ds
=
Z t
0
⟨divrρδ ∗ynV N(s) −divrynρδ ∗V N(s), ρδ ∗V N(s)⟩ds
= −
Z t
0
⟨ρδ ∗ynV N(s) −ynρδ ∗V N(s), ρδ ∗∇rV N(s)⟩ds.
On the other hand, note that
 ρδ ∗ynV N
(s, x, r) −yn(ρδ ∗V N)(s, x, r) =
Z
R2[yn(x −y, s) −yn(x, s)]ρδ(y)V N(s, x −y, r)dy.
By mean-value theorem we get
|yn(x −y, s) −yn(x, s)| = |
X
k∈Kn
(gk(∇σN
k r)(x −y, s) −gk(∇σN
k r)(x, s))|
≤
X
k∈Kn
|gk|∥D2σN
k ∥∞|y||r| ≤|y||r|∥g∥since ∥D2σN
k ∥∞≤1,
and
|
 ρδ ∗(∇uL(·)r)V N
(s, x, r) −(∇uL(s, x)r)(ρδ ∗V N)(s, x, r)|
≤∥g∥
Z
R2 |y||r|ρδ(y)|V N(s, x −y, r)|dy ≤δ∥g∥
Z
R2 ρδ(y)|r||V N(s, x −y, r)|dy,

--- Page 42 ---

42
F. FLANDOLI AND Y. TAHRAOUI
since supp[ρ] ⊂B(0, 1). Therefore, we get
Z t
0
|⟨ρδ ∗(∇uL(s)r)V N(s) −(∇uL(s)r)ρδ ∗V N(s), ρδ ∗∇rV N(s)⟩|ds
≤δ
Z t
0
∥g∥∥ρδ ∗|r||V N(s)||∥∥ρδ ∗∇rV N(s)∥ds
≤δ
Z t
0
∥g∥∥V N(s)∥H∥∇rV N(s)∥ds →0 as δ →0.
Now, notice that [divrrV N(s)]δ = divrr[V N(s)]δ. Hence
1
β
Z t
0
⟨[divrrV N(s)]δ, [V N(s)]δ⟩ds = 1
β
Z t
0
∥[V N(s)]δ∥2ds ≤1
β
Z t
0
∥V N(s)∥2ds.
Next, we have ⟨σ2[∆rV N(s)]δ, [V N(s)]δ⟩= ⟨σ2∆r[V N(s)]δ, [V N(s)]δ⟩= −σ2∥∇r[V N(s)]δ∥2, thus
Z t
0
⟨σ2[∆rV N(s)]δ, [V N(s)]δ⟩ds = −σ2
Z t
0
∥[∇rV N(s)]δ∥2ds →−σ2
Z t
0
∥∇rV N(s)∥2ds as δ →0,
since ∇rV N ∈L2(0, T; H). We have ([∆xV N(s)]δ, [V N(s)]δ) = (∆x[V N(s)]δ, [V N(s)]δ) which
gives
Z t
0
αN([∆xV N(s)]δ, [V N(s)]δ)ds = −
Z t
0
αN∥∇x[V N(s)]δ∥2ds ≤0.
Concerning the last term, ﬁrst we prove the following
Z t
0
⟨[divr
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rV N(s))]δ, [V N(s)]δ⟩ds +
X
k∈K
Z t
0
∥[(∇σN
k r).∇rV N(s)]δ∥2ds →
δ→0 0.
Indeed, we have
Z t
0
⟨[divr
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rV N(s))]δ, [V N(s)]δ⟩ds +
X
k∈K
Z t
0
∥[(∇σN
k r).∇rV N(s)]δ∥2ds
= −
X
k∈K
Z t
0
⟨[(∇σN
k r)(∇σN
k r) · ∇rV N(s)]δ, ∇r[V N(s)]δ⟩ds +
X
k∈K
Z t
0
∥[(∇σN
k r).∇rV N(s)]δ∥2ds
= −
X
k∈K
Z t
0
⟨[(∇σN
k r)(∇σN
k r) · ∇rV N(s)]δ −(∇σN
k r)[(∇σN
k r) · ∇rV N(s)]δ, ∇r[V N(s)]δ⟩ds
−
X
k∈K
Z t
0
⟨(∇σN
k r)[(∇σN
k r) · ∇rV N(s)]δ, ∇r[V N(s)]δ⟩ds
+
X
k∈K
Z t
0
([(∇σN
k r).∇rV N(s)]δ, [(∇σN
k r).∇rV N(s)]δ)ds
= −
X
k∈K
Z t
0
⟨[(∇σN
k r)(∇σN
k r) · ∇rV N(s)]δ −(∇σN
k r)[(∇σN
k r) · ∇rV N(s)]δ, ∇r[V N(s)]δ⟩ds
−
X
k∈K
Z t
0
⟨[(∇σN
k r) · ∇rV N(s)]δ, (∇σN
k r) · ∇r[V N(s)]δ −[(∇σN
k r).∇rV N(s)]δ)⟩ds
= J1
δ + J2
δ .

--- Page 43 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
43
Let us prove that lim sup
δ→0
|J1
δ | = 0. Recall that (∇σN
k r) has the form θN
|k||k| k
|k| · rk⊥
|k|h(k · x)8 for
any k ∈Z2
0. Thus, |∇σN
k r| ≤θN
|k||k||r|. On the other hand, we have
|J1
δ | ≤
X
k∈K
Z t
0
|⟨[(∇σN
k r)(∇σN
k r) · ∇rV N(s)]δ −(∇σN
k r)[(∇σN
k r) · ∇rV N(s)]δ, ∇r[V N(s)]δ⟩|ds
and
 [(∇σN
k r)(∇σN
k r) · ∇rf N(s)]δ −(∇σN
k r)[(∇σN
k r) · ∇rV N(s)]δ

(x, r)
= −
Z
R2[(∇σN
k (x)r) −(∇σN
k (x −y)r)](∇σN
k (x −y)r) · ∇rV N(s, x −y, r)ρδ(y)dy.
By mean-value theorem, we get
|(∇σN
k (x)r) −(∇σN
k (x −y)r)| ≤θN
|k||k|2 · |r||y| ≤2N|k|θN
|k| · |r||y|.
Therefore
|
 [(∇σN
k r)(∇σN
k r) · ∇rV N(s)]δ −(∇σN
k r)[(∇σN
k r) · ∇rV N(s)]δ

(x, r)|
≤
Z
R2 2N|k|θN
|k| · |r||y||(∇σN
k (x −y)r) · ∇rV N(s, x −y, r)|ρδ(y)dy
≤2δN(θN
|k|)2|k|2 · |r|
Z
R2 ||r||∇rV N(s, x −y, r)|ρδ(y)dy.
Thus, we get
|⟨[(∇σN
k r)(∇σN
k r) · ∇rV N(s)]δ −(∇σN
k r)[(∇σN
k r) · ∇rV N(s)]δ, ∇r[V N(s)]δ⟩|
= |
Z
R2
Z
T2[(∇σN
k r)(∇σN
k r) · ∇rV N(s)]δ −(∇σN
k r)[(∇σN
k r) · ∇rV N(s)]δ∇r[V N(s)]δdxdr|
≤
Z
R2
Z
T2 |(∇σN
k r)(∇σN
k r) · ∇rV N(s)]δ −(∇σN
k r)[(∇σN
k r) · ∇rV N(s)]δ||∇r[V N(s)]δ|dxdr
≤2δN(θN
|k|)2|k|2
Z
R2
Z
T2 |r|
Z
R2 ||r||∇rV N(s, x −y, r)|ρδ(y)dy|∇r[V N(s)]δ|dxdr|
≤2δN(θN
|k|)2|k|2∥ρδ ∗|r||∇rV N(s)|∥2
L2(T2×R2)
≤2δN(θN
|k|)2|k|2∥|r||∇rV N(s)|∥2
L2(T2×R2) ≤2δN(θN
|k|)2|k|2∥∇rV N(s)∥2
H.
Hence, we deduce |J1
δ | ≤2δN
X
k∈K
(θN
|k|)2|k|2
Z t
0
∥∇rV N(s)∥2
Hds →0 as δ →0. Concerning J2
δ , we
recall that
|J2
δ | ≤
X
k∈K
Z t
0
|⟨[(∇σN
k r) · ∇rV N(s)]δ, (∇σN
k r) · ∇r[V N(s)]δ −[(∇σN
k r).∇rV N(s)]δ)⟩|ds.
8h(·) = cos(·) or h(·) = −sin(·), see (35).

--- Page 44 ---

44
F. FLANDOLI AND Y. TAHRAOUI
On the other hand, we have
|(∇σN
k r) · ∇r[V N(s)]δ −[(∇σN
k r).∇rV N(s)]δ|
= |
Z
R2[(∇σN
k (x)r) −(∇σN
k (x −y)r)] · ∇rV N(s, x −y, r)ρδ(y)dy|
≤δ|k|2θN
|k|
Z
R2 |r||∇rV N(s, x −y, r)|ρδ(y)dy,
consequently, we get
|⟨[(∇σN
k r) · ∇rf N(s)]δ, (∇σN
k r) · ∇r[V N(s)]δ −[(∇σN
k r).∇rV N(s)]δ)⟩|
≤
Z
R2
Z
T2 |[(∇σN
k r) · ∇rV N(s)]δ||(∇σN
k r) · ∇r[V N(s)]δ −[(∇σN
k r).∇rV N(s)]δ)|dxdr
≤δ|k|2θN
|k|
Z
R2
Z
T2 |[(∇σN
k r) · ∇rV N(s)]δ|
Z
R2 |r||∇rV N(s, x −y, r)|ρδ(y)dy|dxdr
≤δ|k|3(θN
|k|)2
Z
R2
Z
T2 |
Z
R2 |r||∇rV N(s, x −y, r)|ρδ(y)dy|2dxdr
≤δ|k|3(θN
|k|)2∥|
Z
R2 |r||∇rV N(s, x −y, r)|ρδ(y)dy|∥2
L2(T2×R2)
≤δ|k|3(θN
|k|)2∥∇rV N(s)|∥2
H ≤2δN|k|2(θN
|k|)2∥∇rV N(s)|∥2
H
and
|J2
δ | ≤2δN
X
k∈K
(θN
|k|)2|k|2E
Z t
0
∥∇rV N(s)∥2
Hds →0 as δ →0.
Finally, we get
lim
δ→0
Z t
0
⟨[divr
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇rV N(s))]δ, [V N(s)]δ⟩ds
= −
X
k∈K
Z t
0
∥(∇σN
k r).∇rV N(s)∥2ds ≤0,
where we used ∇rV N ∈L2(0, T; H)) and
X
k∈K
Z t
0
∥[(∇σN
k r).∇rV N(s)]δ∥2ds →δ→0
X
k∈K
Z t
0
∥(∇σN
k r).∇rV N(s)∥2ds.
In conclusion, by passing to the limit as δ →0 in (54) and using the above estimates, we get
1
2∥V N(t)∥2 + σ2
Z t
0
∥∇rV N(s)∥2ds ≤1
β
Z t
0
∥V N(s)∥2ds.
(61)
The last inequality (61) and Gr¨onwall lemma ensure that V N ≡0 in L∞(0, T; H)-sense and
∇V N ≡0 in L2(0, T; H)−sense as well, which ends the proof of uniqueness.
6.3.1. Uniqueness of quasi-regular weak solutions of (12). We will use Lemma 21 to prove that
the solution to (12) in the sense of Deﬁnition 5 is unique (in particular we use the point (4)).
First, note that the set of quasi-regular weak solutions forms a linear subspace of L2(0, T; H),
since (12) is a linear equation, and the regularity conditions is a linear constraint. Therefore, it
is enough to show that a quasi-regular weak solution f N ≡0 if the initial data f0 ≡0.

--- Page 45 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
45
Let g ∈Gn, by using Lemma 21 we proved that E[f N(t)eg(t)] = 0 in L∞(0, T; H)-sense. Our
aim is to prove that f N ≡0. We recall that from Lemma 21: for any t ∈[0, T], we have
(E[f N(t)eg(t)], ϕ) = 0, ∀ϕ ∈V and for any g ∈D.
Now, let G be a random variable, which can be written as a linear combination of ﬁnite number
of eg(t), it follows (by linearity)
(E[f N(t)G], ϕ) = 0, ∀ϕ ∈V.
Next, by density of D in L2(Ω, Gt), the last equality holds for any G ∈L2(Ω, Gt), namely
E[(f N(t), ϕ)G] = 0, ∀ϕ ∈V,
∀G ∈L2(Ω, Gt).
Since (f N(t), ϕ) is Gt-adapted, we get (f N(t), ϕ) = 0, for any ϕ ∈V . Recall that V is dense
subspace in H, thus, we deduce that f N ≡0 and the uniqueness holds.
7. Diffusion scaling limit as N →+∞
Our aim in this section is to show that the unique solution of stochastic FP equation (12), in
the sense of Deﬁnition 5, converges weakly to the unique solution of (13), under the following
scaling of the noise coeﬃcients: θN
|k| =
a
|k|2 if N ≤|k| ≤2N and θN
|k| = 0 else. First, note that
lim
N→+∞
X
k∈K++
 θN
|k|
2 = 0;
lim
N→+∞sup
k∈K
 θN
|k|
2 = 0 and
lim
N→+∞sup
k∈K
|k|2  θN
|k|
2 = 0.
(62)
7.1. Time regularity and tightness of laws. We begin by showing the following result about
regularity in time of (f N)N.
Lemma 22. Let 2 < p < +∞, there exists C > 0, independent of N such that
E∥f N∥p
Cη([0,T],U′) ≤C for any 0 < η < min(p −2
p
, 1
2).
Proof. Let 0 < h < 1 and t ∈[0, T −h]. From Deﬁnition 5, point (3), the following equality
holds in U′-sense:
f N(t + h) −f N(t) = −
Z t+h
t
((uL · ∇xf N(s)) −divr[(∇xuLr −1
β r)f N(s)])ds
+
Z t+h
t
[σ2∆rf N(s) + αN(∆xf N(s)]ds + 1
2
Z t+h
t
divr(AN
k ∇rf N(s))ds
−
X
k∈K
Z t+h
t
(σN
k .∇xf N(s) + (∇σN
k r).∇rf N(s))dW k(s) := I1 + I2 + I3 + I4.
On the one hand, we have P-a.s.
∥I1∥U′ ≤
Z t+h
t
∥uL · ∇xf N(s) + divr[(∇xuLr −1
βr)f N(s)]∥U′ds
≤[∥uL∥∞+ ∥∇xuL∥∞+ 1
β]
Z t+h
t
∥f N(s)∥Hds
≤h[∥uL∥∞+ ∥∇xuL∥∞+ 1
β] sup
t∈[0,T]
∥f N(t)∥H,

--- Page 46 ---

46
F. FLANDOLI AND Y. TAHRAOUI
since uL is a smooth function. Concerning I2, note that
∥I2∥U′ ≤
Z t+h
t
∥σ2∆rf N(s) + αN∆xf N(s)∥U′ds ≤(σ2 + αN)
Z t+h
t
∥f N(s)∥Hds
≤(σ2 + 1)
Z t+h
t
∥f N(s)∥Hds ≤h(σ2 + 1) sup
t∈[0,T]
∥f N(t)∥H.
Moreover ∥I3∥U′ ≤
Z t+h
t
∥divr(AN
k ∇rf N(s)∥U′ds, we recall that
∥divr(AN
k ∇rf N(s)∥U′ =
sup
∥φ∥U ≤1
|⟨divr(AN
k ∇rf N(s), φ⟩|
but ⟨divr(AN
k ∇rf N), φ⟩= (divr(AN
k ∇rf N), φ) = (f N, divr(AN
k ∇rφ)), therefore
Z t+h
t
∥divr(AN
k ∇rf N(s)∥U′ds ≤
X
k∈K
|k|2  θN
|k|
2 Z t+h
t
∥f N(s)∥Hds
≤h sup
t∈[0,T]
∥f N(t)∥H
X
k∈K
|k|2  θN
|k|
2 .
Concerning the stochastic integral I4, let φ ∈U and note that
X
k∈K
Z t+h
t
⟨(σN
k .∇xf N(s) + (∇σN
k r).∇rf N(s), φ⟩dW k(s)
=
X
k∈K
Z t+h
t
⟨σN
k .∇xf N(s) + (∇σN
k r).∇rf N(s), φ⟩dW k(s)
= −
X
k∈K
Z t+h
t
(f N(s), σN
k .∇xφ + (∇σN
k r).∇rφ)dW k(s).
We recall
∥
X
k∈K
Z t+h
t
(σN
k .∇xf N(s) + (∇σN
k r).∇rf N(s))dW k(s)∥U′
=
sup
∥φ∥U≤1
|
X
k∈K
Z t+h
t
(f N(s), σN
k .∇xφ + (∇σN
k r).∇rφ)dW k(s)|.
Let φ ∈U such that ∥φ∥U ≤1 and 1 < p < +∞. Burkholder-Davis-Gundy inequality ensures
E|
X
k∈K
Z t+h
t
(f N(s), σN
k .∇xφ + (∇σN
k r).∇rφ)dW k(s)|p
≤E[
Z t+h
t
X
k∈K
(f N(s), σN
k .∇xφ + (∇σN
k r).∇rφ)2ds]p/2
≤[
X
k∈K
(|k|2 + 1)
 θN
|k|
2]p/2E[
Z t+h
t
(f N(s), ∇xφ + |r||∇rφ|)2ds]p/2
≤C1E[
Z t+h
t
∥f N(s)∥2∥φ∥2
Uds]p/2 ≤C1E[
Z t+h
t
∥f N(s)∥2∥φ∥2
Uds]p/2 ≤C1E[
Z t+h
t
∥f N(s)∥2ds]p/2,

--- Page 47 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
47
where C1 := [P
k∈K (|k|2 + 1)

θN
|k|
2
]p/2. Thus, we obtain
E∥
X
k∈K
Z t+h
t
(σN
k .∇xf N(s) + (∇σN
k r).∇rf N(s))dW k(s)∥p
U′ ≤C1E[
Z t+h
t
∥f N(s)∥2ds]p/2
≤C1hp/2E sup
q∈[0,T]
∥f N(q)∥p.
(63)
Recall the deﬁnition of W s,p(0, T; U′), the Sobolev space of all u ∈Lp(0, T; U′) such that
Z T
0
Z T
0
∥u(t) −u(r)∥p
U′
|t −r|1+sp
dtdr < +∞,
endowed with the norm
∥u∥p
W s,p(0,T;U′) = ∥u∥p
Lp(0,T;U′) +
Z T
0
Z T
0
∥u(t) −u(r)∥p
U′
|t −r|1+sp
dtdr.
Now, denote by I(f N)(·) =
X
k∈K
Z ·
0
(σN
k .∇xf N(s) + (∇σN
k r).∇rf N(s))dW k(s).
Thanks to (45) and Burkholder-Davis-Gundy inequality, one has
E∥I(f N)∥p
Lp(0,T;U′) ≤M,
M > 0 independent of m and N.
Concerning the second part, note that
E
Z T
0
Z T
0
∥I(f N)(t) −I(f N)(r)∥p
U′
|t −r|1+sp
dtdr =
Z T
0
Z T
0
E∥I(f N)(t) −I(f N)(r)∥p
U′
|t −r|1+sp
dtdr
≤C1E sup
q∈[0,T]
∥f N(q)∥p
Z T
0
Z T
0
|t −r|p/2
|t −r|1+spdtdr
≤C1E sup
q∈[0,T]
∥f N(q)∥p
Z T
0
Z T
0
|t −r|p( 1
2−s)−1dtdr ≤C,
if p( 1
2 −s) > 0, which holds for any s ∈]0, 1
2[.
Let p > 2, then 0 < sp −1 < p −2
2
. Denote by Cη([0, T], U′) the space of η-H¨older continuous
functions with values in U′. and we recall that (see e.g. [24])
W s,p(0, T; U′) ֒→Cη([0, T], U′)
if
0 < η < sp −1.
Let us take s ∈

0, 1
2

such that sp > 1. For η ∈

0, sp−1

, it follows from the previous estimates
E∥
X
k∈K
Z ·
0
(σN
k .∇xf N(s) + (∇σN
k r).∇rf N(s))dW k(s)∥p
W s,p(0,T;U′) ≤C + M.
Thus E∥I(f N)∥p
Cη([0,T],U′) ≤C + M. Consequently, we obtain
E∥f N∥p
Cη([0,T],U′) ≤C + M for any 0 < η < min(p −2
p
, 1
2),
which gives that (f N)N is bounded in Lp(Ω, Cη([0, T], U′)), η ∈]0, min( p−2
p , 1
2)[ with 2 < p < +∞.
□

--- Page 48 ---

48
F. FLANDOLI AND Y. TAHRAOUI
As a consequence of Lemma 15, Lemma 16, Lemma 22 and the lower semi-continuity of the
weak convergence, we obtain
Proposition 23. Let p ≥2, there exists K > 0 such that the unique solution (f N)N to (12) is
bounded by K in
Lp(Ω, L∞(0, T; H)) ∩Lp(Ω, Cη([0, T], U′)),
0 < η < min(p −2
p
, 1
2).
Moreover, (∇rf N)N is bounded in L2(Ω, L2(0, T; H)).
7.1.1. Tightness of laws. Denote by µfN the law of f N, µW the law of W := (W k)k∈Z2
0 and their
joint law µN deﬁned on C([0, T], U′) × C([0, T]; H0).
Lemma 24. The set {µfN; N ∈N} is tight on C([0, T], U′).
Proof. First, we have H
֒→
compact U′, since U
֒→
compact H. Let A be a subset C([0, T]; U′). Following
[59, Thm. 3] (the case p = ∞), A is relatively compact in C([0, T]; U′) if the following conditions
hold.
(1) A is bounded in L∞(0, T; H).
(2) Let h > 0, ∥f(· + h) −f(·)∥L∞(0,T−h;U′) →0 as h →0 uniformly for f ∈A.
The following embedding is compact
Z := L∞(0, T; H) ∩Cη([0, T], U′) ֒→C([0, T], U′),
0 < η < min(p −2
p
, 1
2).
Indeed, Let A be a bounded set of Z. First, note that (1) is satisﬁed by assumptions. Concerning
the second condition, let h > 0 and f ∈A, by using that f ∈Cη([0, T], U′) we infer
∥f(· + h) −f(·)∥L∞(0,T−h;U′) =
sup
r∈[0,T−h]
∥f(r + h) −f(r)∥U′ ≤Chη →0, as h →0,
where C > 0 is independent of f. Let R > 0 and set BZ(0, R) := {v ∈Z | ∥v∥Z ≤R}. Then
BZ(0, R) is a compact subset of C([0, T], U′), by using Proposition 23 the following holds
µfN(BZ(0, R)) = 1 −µfN(BZ(0, R)c) = 1 −
Z
{ω∈Ω,∥fN∥Z>R}
1dP
≥1 −1
Rp
Z
{ω∈Ω,∥fN∥Z>R}
∥f N∥p
ZdP
≥1 −1
RpE∥f N∥p
Z = 1 −Kp
Rp ,
for any R > 0,
and any N ∈N.
Therefore, for any δ > 0 we can ﬁnd Rδ > 0 such that
µfN(BZ(0, Rδ)) ≥1 −δ, for all N ∈N.
Thus the family of laws {µfN; N ∈N} is tight on C([0, T], U′).
□
Notice that the family of Brownian motions W := (W k)k∈Z2
0 can be seen as cylindrical Wiener
process deﬁned on the ﬁltred probability space (Ω, F, P; (Ft)t) with values in appropriate separa-
ble Hilbert space H0, more precisely W k = Wek, k ∈Z2
0, where (ek)k∈Z2
0 is complete orthonormal
system in a separable Hilbert space H and recall that the sample paths of W take values in a
larger Hilbert space H0 such that H ֒→H0 deﬁnes a Hilbert–Schmidt embedding. Hence, P-a.s.
the trajectories of W belong to the space C([0, T], H0), see e.g. [13, Chapter 4]. By taking into
account that the law µW is a Radon measure on C([0, T]; H0), we obtain
Lemma 25. The set {µW} is tight on C([0, T]; H0).

--- Page 49 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
49
7.1.2. Prokhorov and Skorokhod’s representation’s theorem. Thanks to Lemma 24 and Lemma 25,
by Skorokhod’s representation’s theorem (see e.g. [65, Thm. 1.10.4, p. 59]), by passing to the
limit up to subsequences (denoted by the same way), we can ﬁnd a new probability space,
denoted by the same way ”for simplicity” (Ω, F, P) and processes

ef N, W N := {W N,k}k∈Z2
0

,

f, W := {W
k}k∈Z2
0

,
such that:
(a) L

ef N, W N := {W N,k}k∈Z2
0

= L

f N, W := {W k}k∈Z2
0

9 on C([0, T], U′)×C([0, T], H0).
(b) the following convergences hold
ef N →f
in C([0, T]; U′)
P −a.s.
(64)
W N →W
in C([0, T]; H0)
P −a.s.
(65)
On the other hand, thanks to Proposition 23, L(f N)(X ) = 1 where X ֒→
cont. C([0, T], U′), with
X = {g :
g ∈L∞(0, T; H) ∩Cη([0, T], U′); ∇rg ∈L2(0, T; H)}.
By using the point (a) above, one gets L( ef N)(X ) = 1 and ( ef N, W N) satisﬁes the point (3) of
Deﬁnition 5. Moreover, ( ef N)N satisﬁes the estimates of Proposition 23 in the new probability
space. Thus, we have the following result.
Lemma 26. There exists f ∈L2(Ω; L2([0, T]; H)), ∇rf ∈L2(Ω; L2([0, T]; H)) such that
ef N ⇀f in L2(Ω; L2([0, T]; H)),
∇r ef N ⇀∇rf in L2(Ω; L2([0, T]; H)).
Moreover, f ∈L2
w−∗(Ω; L∞([0, T]; H)) and ef N ⇀∗f in L2
w−∗(Ω; L∞([0, T]; H)).
Proof. By using Proposition 23, diagonal extraction argument and Banach–Alaoglu theorem in
the spaces L2(Ω; L2([0, T]; H)) and L2
w−∗(Ω; L∞([0, T]; H)), there exist f, ∇rf ∈L2(Ω; L2([0, T]; H))
such that
ef N ⇀f in L2(Ω; L2([0, T]; H)),
(66)
∇r ef N ⇀∇rf in L2(Ω; L2([0, T]; H)).
(67)
Moreover, f ∈L2
w−∗(Ω; L∞([0, T]; H))) and the following convergence holds
ef N ⇀∗f in L2
w−∗(Ω; L∞([0, T]; H)),
(68)
since ( ef N)N is bounded in L2(Ω; L∞([0, T]; H)) and L2
w−∗(Ω; L∞([0, T]; H)) ≃(L2(Ω; L1([0, T]; H′)))′ .
□
7.2. Passage to the limit as N →+∞. In the following, we will establish some lemmas to
pass to the limit as N →+∞. For that, consider φ ∈C∞(T2), ψ ∈C∞
c (R2)10, and A ∈F.
Lemma 27. Let t ∈]0, T[, the following convergence holds:
lim
N αN
Z
A
Z t
0
Z
T2
Z
R2 ∇x ef N(x, r, s) · ∇xφ(x)ψ(r)drdxdsdP = 0.
9Given a random variable ξ with values in space E, its law L(ξ)(Γ) = P(ξ ∈Γ) for any Borel subset Γ of E.
10Note that φ ⊗ψ ∈V, thus it is an appropriate test function in Deﬁnition 5, point (3).

--- Page 50 ---

50
F. FLANDOLI AND Y. TAHRAOUI
Proof. Thanks to Fubini’s theorem and by using integration by part with respect to x, we get
|αN
Z
A
Z t
0
Z
T2
Z
R2 ∇x ef N(x, r, s) · ∇xφ(x)ψ(r)drdxdsdP|
= |αN
Z
A
Z t
0
Z
R2
Z
T2
ef N(x, r, s)∆xφ(x)ψ(r)dxdrdsdP|.
≤CαN∥ef N∥L2(Ω×[0,T];L2(T2×R2)))∥∆xφ∥∞∥ψ∥∞,
where C is a constant depends only on the measure of supp(ψ), T and the volume of T2. We
recall from (11) that lim
N αN = 0 and the result follows.
□
Lemma 28. Let t ∈]0, T[, we have
lim
N −1
2
Z
A
Z t
0
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇r ef N(x, r, s)) · ∇rψ(r)φ(x)drdxdsdP
= −1
2
Z
A
Z t
0
Z
T2
Z
R2 A(r)∇rf(x, r, s)) · ∇rψ(r)φ(x)drdxdsdP.
Proof. By using Lemma 3, we get
−1
2
Z
A
Z t
0
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇r ef N(x, r, s)) · ∇rψ(r)φ(x)drdxdsdP
= −1
2
Z
A
Z t
0
Z
T2
Z
R2 A(r)∇r ef N(x, r, s)) · ∇rψ(r)φ(x)drdxdsdP + RN,
(69)
where RN satisﬁes
|RN| ≤C
N
Z
A
Z T
0
Z
T2
Z
R2 |P(r)|| ef N(x, r, s)| · |D2
rψ(r)φ(x)|||drdxdsdP
≤C
N ∥ef N∥L2(Ω×[0,T];H))∥D2
rψ∥∞∥φ∥∞→0 as N →+∞.
Now, by passing to the limit in (69) and using Lemma 26, the conclusion follows.
□
Concerning the stochastic integral part, we have the following result.
Lemma 29. Let t ∈]0, T], the following convergence holds
lim
N |E
Z t
0
X
k∈K
Z
T2
Z
R2
ef N(x, r, s)
 σN
k .∇xφ(x)ψ(r) + (∇σN
k r).∇rψ(r)φ(x)

drdxdW N,k(s)1A| = 0.

--- Page 51 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
51
Proof. Let A ∈F, φ ∈C∞(T2) and ψ ∈C∞
c (R2), by using Itˆo isometry we get
E
 Z t
0
X
k∈K
Z
T2
Z
R2
ef N(x, r, s)
 σN
k .∇xφ(x)ψ(r) + (∇σN
k r).∇rψ(r)φ(x)

drdxdW N,k(s)1A
!2
= E
Z t
0
X
k∈K
Z
R2
Z
T2 1A ef N(x, r, s)
 σN
k .∇xφ(x)ψ(r) + (∇σN
k r).∇rψ(r)φ(x)

dxdr
2
ds
= E
Z t
0
X
k∈K
Z
R2
Z
T2(1A ef N(x, r, s)∇xφ(x)ψ(r)) · σN
k +

1A ef N(x, r, s)∇rψ(r)φ(x)

· (∇σN
k r)dxdr
2
ds
≤2E
Z t
0
X
k∈K
Z
R2
Z
T2(1A ef N(x, r, s)∇xφ(x)ψ(r)) · σN
k dxdr
2
ds
+ 2E
Z t
0
X
k∈K
Z
R2
Z
T2

1A ef N(x, r, s)∇rψ(r)φ(x)

· (∇σN
k r)dxdr
2
ds := 2(IN
1 + IN
2 ).
By using the deﬁnition of σN
k , we get
IN
1 = E
Z t
0
X
k∈K
Z
R2
Z
T2(1A ef N(x, r, s)∇xφ(x)ψ(r)) · σN
k dxdr
2
ds
= E
Z t
0
X
k∈K+
(θN
|k|)2
Z
R2
Z
T2(1A ef N(x, r, s)∇xφ(x)ψ(r)) · k⊥
|k| cos k · xdxdr
2
ds
+ E
Z t
0
X
k∈K−
(θN
|k|)2
Z
R2
Z
T2(1A ef N(x, r, s)∇xφ(x)ψ(r)) · k⊥
|k| sin k · xdxdr
2
ds.
By using that (k⊥
|k| cos k · x, k⊥
|k| sin k · x)k∈K is an (incomplete) orthonormal system in L2(T2; R2),
we obtain by using (62)
|IN
1 | ≤sup
k∈K
(θN
|k|)2E
Z t
0
Z
R2
Z
T2( ef N(x, r, s)∇xφ(x)ψ(r))2dxdrds
≤∥∇xφψ∥2
∞sup
k∈K
(θN
|k|)2E
Z T
0
Z
R2
Z
T2
ef N(x, r, s)2dxdrds
≤K2∥∇xφψ∥2
∞sup
k∈K
(θN
|k|)2 →0 as N →+∞.
Concerning IN
2 , we have
IN
2 = E
Z t
0
X
k∈K
Z
R2
Z
T2

1A ef N(x, r, s)∇rψ(r)φ(x)

· (∇σN
k r)dxdr
2
ds
= E
Z t
0
X
k∈K+
(θN
|k|)2|k|2
Z
R2
Z
T2
k
|k| · r

1A ef N(x, r, s)∇rψ(r)φ(x)

· k⊥
|k| sin k · xdxdr
2
ds
+ E
Z t
0
X
k∈K−
(θN
|k|)2|k|2
Z
R2
Z
T2
k
|k| · r

1A ef N(x, r, s)∇rψ(r)φ(x)

· k⊥
|k| cos k · xdxdr
2
ds.

--- Page 52 ---

52
F. FLANDOLI AND Y. TAHRAOUI
Thus, by using the same argument as above we obtain
|IN
1 | ≤sup
k∈K
[(θN
|k|)2|k|2]E
Z T
0
Z
R2
Z
T2 |r|2 
ef N(x, r, s)∇rψ(r)φ(x)
2
dxdrds
≤sup
k∈K
[(θN
|k|)2|k|2]∥∇rψφ∥2
∞∥ef N∥2
L2(Ω×[0,T];H) →0 as N →+∞.
□
Lemma 30. For any t ∈]0, T[, the following convergence holds (up to a subsequence)
lim
N
Z
A
Z
T2
Z
R2
ef N(x, r, t)φ(x)ψ(r)drdxdP =
Z
A
Z
T2
Z
R2 f(x, r, t)φ(x)ψ(r)drdxdP.
Proof. From (64), ef N →f
in C([0, T]; U′) P-a.s. Since ( ef N)N is bounded in L2
w−∗(Ω; L∞([0, T]; H)),
Vitali’s convergence theorem ensures the convergence of ef N to f in L1(Ω; C([0, T]; U′)).
□
7.2.1. Proof of Theorem 9. Let φ ∈C∞(T2) and ψ ∈C∞
c (R2), Let t ∈]0, T] and A ∈F. From
Deﬁnition 5, point (3) and by multiplying by IA and integrating over Ω× [0, t], we derive
Z
A
Z
T2
Z
R2
ef N(t)φψdrdxdP −
Z
A
Z
T2
Z
R2 f0φψdrdxdP
−
Z
A
Z t
0
X
k∈K
Z
T2
Z
R2
ef N(s)
 σN
k .∇xφψ + (∇σN
k r).∇rψφ

drdxdW N,k(s)dP
=
Z
A
Z t
0
Z
T2
Z
R2
ef N(s)

uL(s) · ∇xφψ + (∇uL(s)r −1
β r) · ∇rψφ

drdxdsdP
−σ2
Z
A
Z t
0
Z
T2
Z
R2 ∇r ef N(s) · ∇rψφdrdxdsdP −αN
Z
A
Z t
0
Z
T2
Z
R2 ∇x ef N(s) · ∇xφψdrdxdsdP
−1
2
Z
A
Z t
0
Z
T2
Z
R2(
X
k∈K
 (∇σN
k r) ⊗(∇σN
k r)

∇r ef N(s)) · ∇rψφdrdxdsdP
:= JN
1 + JN
2 + JN
3 + JN
4 .
We pass to the limit as N →+∞in the RHS of the last equation. By using Lemma 26, one has
lim
N
Z
A
Z T
0
Z
T2
Z
R2
ef N(s)

uL(s) · ∇xφψ + (∇uL(s)r −1
β r) · ∇rψφ

drdxdsdP
=
Z
A
Z T
0
Z
T2
Z
R2 f(s)

uL(s) · ∇xφψ + (∇uL(s)r −1
βr) · ∇rψφ

drdxdsdP.
Additionally, we have
lim
N
Z
A
Z T
0
Z
T2
Z
R2 ∇r ef N(s) · ∇rψφdrdxdsdP =
Z
A
Z T
0
Z
T2
Z
R2 ∇rf(s) · ∇rψφdrdxdsdP.
From Lemma 27 and Lemma 28, we get
lim
N (JN
3 + JN
4 ) = −1
2
Z
A
Z T
0
Z
T2
Z
R2 A(r)∇rf(s)) · ∇rψφdrdxdsdP.
Finally, we use Lemma 29 and Lemma 30 to pass to the limit in LHS to complete the proof.

--- Page 53 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
53
7.3. Uniqueness of the limit problem (13). Let us conclude this section by showing that
the limit equation (13) has at most one solution.
Lemma 31. The solution f to (13) is unique.
Proof. Let f 1 and f 2 be two solutions to (13) and denote by f be their diﬀerence. Then P-a.s
for any t ∈]0, T] and φ ∈Y , we have
(f(t), φ) −
Z t
0
⟨f(s), uL(s) · ∇xφ + (∇uL(s)r −1
βr) · ∇rφ⟩ds
(70)
= −
Z t
0
σ2⟨∇rf(s), ∇rφ⟩ds −1
2
Z t
0
⟨A(r)∇rf N(s)), ∇rφ⟩ds.
Since the above equation is in weak form, we need ﬁrst to consider an appropriate regularization
to get an equation for ∥f(t)∥2 for any t ∈[0, T]. We use analogous argument to ”Step 1” in the
proof of Lemma 21 to obtain
1
2∥[f(t)]δ∥2 +
Z t
0
⟨[uL(s) · ∇xf(s)]δ + [divr(∇uL(s)r −1
βr)f(s)]δ, [f(s)]δ⟩ds
(71)
=
Z t
0
⟨σ2[∆rf(s)]δ, [f(s)]δ⟩ds + 1
2
Z t
0
⟨[divrA(r)∇rf(s))]δ, [f(s)]δ⟩ds.
Notice that [divrA(r)∇rf(s))]δ, [f(s)]δ⟩= ⟨divrA(r)∇r[f(s))]δ, [f(s)]δ⟩hence
1
2
Z t
0
⟨[divrA(r)∇rf(s))]δ, [f(s)]δ⟩ds = −3kT
2
Z t
0
∥|r|∇r[f(s)]δ∥2ds + kT
Z t
0
∥r · ∇r[f(s)]δ∥2ds
≤−kT
2
Z t
0
∥[|r|∇rf(s)]δ∥2ds →−kT
2
Z t
0
∥|r|∇rf(s)∥2ds as δ →0.
Next, arguments similar to that used in ”Step 2” of the proof of Lemma 21 allow to pass to the
limit as δ →0 in (71) and we get
1
2∥f(t)∥2 + σ2
Z t
0
∥∇rf(s)∥2ds + kT
2
Z t
0
∥|r|∇rf(s)∥2ds ≤1
β
Z t
0
∥f(s)∥2ds.
(72)
The last inequality (72) and Gr¨onwall lemma completes the proof of Lemma 31.
□
Remark 32. Another way to prove that uniqueness to (13) holds is to notice that (15) has (13)
as FP equation associated. We have uniqueness in law of weak solutions of the SDE (15) due to
the properties of Σ(r). The latter ensures uniqueness of solutions of (13) due to [63, Thm. 2.5].
7.4. About the 3D case. It is worth drawing the reader’s attention to the fact that with
cosmetic changes to what was made above, it is possible to prove a similar result in a three-
dimensional setting. However, we preferred to present the result in 2D because we could present
the stochastic turbulent velocity explicitly, see subsubsection 2.0.2. The main diﬀerence between
2D and 3D will be in the form of the stochastic turbulent velocity. In 3D, we can formulate
the result using Fourier decomposition. Let us give an example of noise where we get a similar
result in 3D.
We introduce the partition Z3
0 = Γ3,+ ∪Γ3,−
11 such that Γ3,+ = −Γ3,−and we consider
a family of real valued independent Brownian motions (Bk,j
t )
k∈Z3
0
t
, j ∈{1, 2} deﬁned on the
11Z3
0 = Z3 −{(0, 0, 0)}

--- Page 54 ---

54
F. FLANDOLI AND Y. TAHRAOUI
complete ﬁltered probability space (Ω, F, (Ft)t, P), that is E(Bk,j
t Bl,m
s
) = min(t, s)δk,lδj,m. Then,
we introduce a sequence of complex-valued Brownian motions adapted to (Ft)t deﬁned as follows
W k,j
t
=
(
Bk,j
t
+ iB−k,j
t
if k ∈Γ3,+
B−k,j
t
−iBk,j
t
if k ∈Γ3,−.
Note that W −k,j
t
= W k,j
t
12 and satisﬁes
E(W k,j
1 , W l,m
1
) =
(
2
if k = l, m = j
0
otherwise;

W k,j
·
, W l,m
·

t =
(
2t
if k = −l, m = j
0
otherwise .
Let N ∈N∗, deﬁne θN
k,j =
a
|k|5/21{N≤|k|≤2N}, for a positive constant a. Then, for each k ∈Z3
0, j ∈
{1, 2} we denote by σN
k,j(x) = θN
k,jak,jeik·x, where { k
|k|, ak,1, ak,2} is an orthonormal system of R3
for k ∈Γ3,+ and ak,j = a−k,j if k ∈Γ3,−. Set
WN(t, x) =
X
k∈Z3
0,j∈{1,2}
θN
k,jak,jeik·xW k,j(t).
(73)
Thanks to the assumptions on θN
k,j, ak,j and W k,j, we can prove that WN is a real, mean-zero
and divergence free random distribution. Moreover, WN(t, ·) ∈L2(Ω, L2(T3, R3)), see [36, Sect.
2.2.]. On the other hand, it is not diﬀucult to check that the covariance operator associated
with WN is space-homogeneous and has a mirror symmetry property.
Now, by considering
uN = uL +◦∂tWN instead of (8) and then replace in (9) we obtain a stochastic FP in 3D similar
to (12). Then, by cosmetic changes to what has been done above and noticing that
X
k∈Z3
0,j∈{1,2}
N≤|k|≤2N

(∇σN
k,jr) ⊗(∇σN
k,jr)

=
X
k∈Z3
0
N≤|k|≤2N
(r · k)2
|k|5

I −k ⊗k
|k|2

= M(r) + O( 1
N )P(r),
where M(r) = 8π log 2
15
(2|r|2I −r ⊗r) . We can prove that the initial stochastic FP (12) in 3D
converges to a limit PDE as (14) where the matrix A(r) is replaced by M(r).
Acknowledgements. The research of F.F. and Y.T. is funded by the European Union (ERC,
NoisyFluid, No. 101053472). Views and opinions expressed are however those of the authors only
and do not necessarily reﬂect those of the European Union or the European Research Council.
Neither the European Union nor the granting authority can be held responsible for them.
References
[1] A. Agresti. Delayed blow-up and enhanced diﬀusion by transport noise for systems of reaction–diﬀusion
equations. Stoch PDE: Anal Comp, 12(3):1907–1981, 2024.
[2] A. Agresti. Global smooth solutions by transport noise of 3D Navier-Stokes equations with small hypervis-
cosity. arXiv preprint arXiv:2406.09267, 2024.
[3] A. Agresti. On anomalous dissipation induced by transport noise. arXiv preprint arXiv:2405.03525, 2024.
[4] E Balkovsky, A Fouxon, and V Lebedev. Turbulent dynamics of polymer solutions. Physical review letters,
84(20):4765–4768, 2000.
[5] C. L. Bris and T. Lelievre. Multiscale modelling of complex ﬂuids: a mathematical initiation. Multiscale
modeling and simulation in science, pages 49–137, 2009.
[6] Z. Brze´zniak and E. Motyl. Existence of a martingale solution of the stochastic Navier–Stokes equations in
unbounded 2D and 3D domains. Journal of Diﬀerential Equations, 254(4):1627–1685, 2013.
12For a complex number z, z denotes its complex conjugate.

--- Page 55 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
55
[7] F. Butori, F. Flandoli, and E. Luongo. On the Itˆo-Stratonovich Diﬀusion Limit for the Magnetic Field in a
3D Thin Domain. arXiv preprint arXiv:2401.15701, 2024.
[8] F. Butori, F. Flandoli, E. Luongo, and Y. Tahraoui. Background Vlasov equations and Young measures
for passive scalar and vector advection equations under special stochastic scaling limits. arXiv preprint
arXiv:2407.10594, 2024.
[9] F. Butori and E. Luongo. Mean-Field Magnetohydrodynamics Models as Scaling Limits of Stochastic In-
duction Equations. arXiv preprint arXiv:2406.07206, 2024.
[10] M. Chertkov. Polymer stretching by turbulence. Physical review letters, 84(20):4761–4764, 2000.
[11] D. Cioranescu, V. Girault, and K. R. Rajagopal. Mechanics and mathematics of ﬂuids of the diﬀerential
type, volume 35. Springer, 2016.
[12] D. Crisan, D. D Holm, J-M. Leahy, and T. Nilssen. Variational principles for ﬂuid dynamics on rough paths.
Advances in Mathematics, 404:108409, 2022.
[13] G. Da Prato and J. Zabczyk. Stochastic equations in inﬁnite dimensions, volume 44. Cambridge university
press, 1992.
[14] Z. Dong, D. Luo, and B. Tang. Dissipation enhancement by transport noise for stochastic p-Laplace equa-
tions. Nonlinear Diﬀerential Equations and Applications NoDEA, 30(1):5, 2023.
[15] R. E. Edwards. Functional analysis. New York: Dover Publications Inc., 1995.
[16] S. R Ephrati, P. Cifani, E. Luesink, and B. J Geurts. Data-driven stochastic lie transport modeling of the
2D Euler equations. Journal of Advances in Modeling Earth Systems, 15(1):e2022MS003268, 2023.
[17] G. Falkovich, K. Gawedzki, and M. Vergassola. Particles and ﬁelds in ﬂuid turbulence. Reviews of modern
Physics, 73(4):913–975, 2001.
[18] E. Fedrizzi, C Olivera, and V. Neves. On a class of stochastic transport equations for L2loc vector ﬁelds.
Ann. Sc. Norm. Super. Pisa Cl. Sci., 18(2):397–419, 2015.
[19] C. L Feﬀerman. Existence and smoothness of the Navier-Stokes equation. The millennium prize problems,
Clay Math. Inst, 57:67, 2000.
[20] F. Flandoli, L. Galeati, and D. Luo. Delayed blow-up by transport noise. Communications in Partial Dif-
ferential Equations, 46(9):1757–1788, 2021.
[21] F. Flandoli, L. Galeati, and D. Luo. Scaling limit of stochastic 2D Euler equations with transport noises to
the deterministic Navier–Stokes equations. Journal of Evolution Equations, 21(1):567–600, 2021.
[22] F. Flandoli, L. Galeati, and D. Luo. Eddy heat exchange at the boundary under white noise turbulence.
Philosophical Transactions of the Royal Society A, 380(2219):20210096, 2022.
[23] F. Flandoli, L. Galeati, and D. Luo. Quantitative convergence rates for scaling limit of SPDEs with transport
noise. Journal of Diﬀerential Equations, 394:237–277, 2024.
[24] F. Flandoli and D. Gatarek. Martingale and stationary solutions for stochastic Navier-Stokes equations.
Probability Theory and Related Fields, 102:367–391, 1995.
[25] F. Flandoli, M. Hofmanov´a, D. Luo, and T. Nilssen. Global well-posedness of the 3D Navier–Stokes equations
perturbed by a deterministic vector ﬁeld. The Annals of Applied Probability, 32(4):2568–2586, 2022.
[26] F. Flandoli and R. Huang. Noise based on vortex structures in 2D and 3D. J. Math. Phys., 64(5), 2023.
[27] F. Flandoli and D. Luo. High mode transport noise improves vorticity blow-up control in 3D Navier–Stokes
equations. Probability Theory and Related Fields, 180:309–363, 2021.
[28] F. Flandoli and D. Luo. Enhanced dissipation and Lyapunov exponents for stochastic transport-diﬀusion
equations with small molecular diﬀusivity and small noise intensity. preprint, 2024.
[29] F. Flandoli and D. Luo. Mean ﬁeld limit of point vortices with environmental noises to deterministic 2D
Navier-Stokes equations. Communications in Mathematics and Statistics, 2024.
[30] F. Flandoli and D. Luo. On the Boussinesq hypothesis for a stochastic Proudman-Taylor model. SIAM J.
Math. Anal, 56(3):3886–3923, 2024.
[31] F. Flandoli, D. Luo, and E. Luongo. 2D Smagorinsky-type large eddy models as limits of stochastic PDEs.
Journal of Nonlinear Science, 34(3):54, 2024.
[32] F. Flandoli and E. Luongo. Stochastic partial diﬀerential equations in ﬂuid mechanics, volume 2330. Springer
Nature, 2023.
[33] F. Flandoli, S. Morlacchi, and A. Papini. Eﬀect of transport noise on Kelvin–Helmholtz instability. In
Stochastic Transport in Upper Ocean Dynamics II, pages 29–52. Springer Nature Switzerland Cham, 2024.
[34] F. Flandoli and C. Olivera. Well-posedness of the vector advection equations by stochastic perturbation.
Journal of Evolution Equations, 18:277–301, 2018.

--- Page 56 ---

56
F. FLANDOLI AND Y. TAHRAOUI
[35] F. Flandoli and F. Russo. Reduced dissipation eﬀect in stochastic transport by gaussian noise with regularity
greater than 1/2. arXiv preprint arXiv:2305.19293, 2023.
[36] L. Galeati. On the convergence of stochastic transport equations to a deterministic parabolic one. Stochastics
and Partial Diﬀerential Equations: Analysis and Computations, 8(4):833–868, 2020.
[37] L. Galeati and D. Luo. LDP and CLT for SPDEs with transport noise. Stochastics and Partial Diﬀerential
Equations: Analysis and Computations, 12(1):736–793, 2024.
[38] S. Gerashchenko, C. Chevallard, and V. Steinberg. Single-polymer dynamics: Coil-stretch transition in a
random ﬂow. Europhysics Letters, 71(2):221–227, 2005.
[39] D. Goodair and D. Crisan. Stochastic Calculus in Inﬁnite Dimensions and SPDEs. Springer Nature, 2024.
[40] S. Guo and D. Luo. Scaling limit of moderately interacting particle systems with singular interaction and
environmental noise. The Annals of Applied Probability, 33(3):2066–2102, 2023.
[41] S K. Harouna and E. M´emin. Stochastic representation of the Reynolds transport theorem: revisiting large-
scale modeling. Computers & Fluids, 156:456–469, 2017.
[42] D. D Holm. Variational principles for stochastic ﬂuid dynamics. Proceedings of the Royal Society A: Mathe-
matical, Physical and Engineering Sciences, 471(2176):20140963, 2015.
[43] W. Huang. Scaling limits of stochastic transport equations on manifolds. arXiv preprint arXiv:2308.15350,
2023.
[44] Y. Le Jan and O. Raimond. Integration of brownian vector ﬁelds. Ann. Probab., 30(2):826–873, 2002.
[45] D. Luo. Convergence of stochastic 2D inviscid Boussinesq equations with transport noise to a deterministic
viscous system. Nonlinearity, 34(12):8311, 2021.
[46] D. Luo. Enhanced dissipation for stochastic Navier–Stokes equations with transport noise. Journal of Dy-
namics and Diﬀerential Equations, pages 1–36, 2023.
[47] D. Luo and B. Tang. Stochastic inviscid Leray-α model with transport noise: convergence rates and CLT.
Nonlinear Analysis, 234:113301, 2023.
[48] D. Luo, B. Tang, and G. Zhao. An elementary approach to mixing and dissipation enhancement by transport
noise. arXiv preprint arXiv:2402.07484, 2024.
[49] D. Luo and D. Wang. Well posedness and limit theorems for a class of stochastic dyadic models. SIAM
Journal on Mathematical Analysis, 55(2):1464–1498, 2023.
[50] A. J Majda and P. R Kramer. Simpliﬁed models for turbulent diﬀusion: theory, numerical modelling, and
physical phenomena. Physics reports, 314(4-5):237–574, 1999.
[51] N. Masmoudi. Global existence of weak solutions to the FENE dumbbell model of polymeric ﬂows. Inven-
tiones mathematicae, 191:427–500, 2013.
[52] M Maurelli. Wiener chaos and uniqueness for stochastic transport equation. C. R. Math. Acad. Sci. Paris,
349:669–672, 2011.
[53] E. M´emin. Fluid ﬂow dynamics under location uncertainty. Geophysical & Astrophysical Fluid Dynamics,
108(2):119–146, 2014.
[54] D. Nualart. The Malliavin calculus and related topics, volume 1995. Springer, 2006.
[55] B. Oksendal. Stochastic diﬀerential equations: an introduction with applications. Fourth Edition, Springer
Science & Business Media, 1995.
[56] C. Olivera and V. Neves. Wellposedness for stochastic continuity equations with Ladyzhenskaya-Prodi-Serrin
condition. Nonlinear Diﬀ. Eq. Appl., 22:1247–1258, 2015.
[57] A. Papini, F. Flandoli, and R. Huang. Turbulence enhancement of coagulation: The role of eddy diﬀusion
in velocity. Physica D: Nonlinear Phenomena, 448:133726, 2023.
[58] J. R. Picardo, L.C. VI M. Plan Emmanuel, and D. Vincenzi. Polymers in turbulence: stretching statistics
and the role of extreme strain rate ﬂuctuations. Journal of Fluid Mechanics, 969:A24, 2023.
[59] J. Simon. Compact sets in the space Lp(0, T ; B). Annali di Matematica pura ed applicata, 146(1):65–96,
1986.
[60] Y. Tahraoui and F. Cipriano. Optimal control of two dimensional third grade ﬂuids. Journal of Mathematical
Analysis and Applications, 523(2):127032, 2023.
[61] Y. Tahraoui and F. Cipriano. Local strong solutions to the stochastic third grade ﬂuid equations with Navier
boundary conditions. Stoch PDE: Anal Comp, 12:1699–1744, 2024.
[62] R. Temam. Navier-Stokes equations: Theory and numerical analysis(Book), volume 2. Amsterdam, North-
Holland Publishing Co.(Studies in Mathematics and Its Applications, 1977.
[63] D. Trevisan. Well-posedness of multidimensional diﬀusion processes with weakly diﬀerentiable coeﬃcients.
Electron. J. Probab., 21:Paper No. 22, 41, 2016.

--- Page 57 ---

STRETCHING OF POLYMERS AND TURBULENCE: FP EQUATION AND SCALING LIMITS
57
[64] G. Vallet and A. Zimmermann. Well-posedness for a pseudomonotone evolution problem with multiplicative
noise. Journal of Evolution Equations, 19:153–202, 2019.
[65] A. W Van Der Vaart and J. A. Wellner. Weak convergence and empirical processes. Springer, 1996.
[66] Mi. Coti Zelati and V. Navarro-Fern´andez. Three-dimensional exponential mixing and ideal kinematic dy-
namo with randomized ABC ﬂows. arXiv preprint arXiv:2407.18028, 2024.

```
