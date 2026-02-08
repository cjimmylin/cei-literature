---
title: "Towards Artificial Virtuous Agents - Games and ML - PDF Extract"
source_pdf: "2022-Vishwanath-Towards Artificial Virtuous Agents - Games and ML.pdf"
pages: 21
extracted_at: "2026-01-25T05:00:17.968733"
---

# PDF Extract: Towards Artificial Virtuous Agents - Games and ML

**Source PDF:** 2022-Vishwanath-Towards Artificial Virtuous Agents - Games and ML.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

arXiv:2205.14350v2  [math.AP]  14 Oct 2023
Norm inﬂation for a non-linear heat equation with Gaussian
initial conditions
Ilya Chevyrev∗
Abstract
We consider a non-linear heat equation ∂tu = ∆u + B(u, Du) + P(u) posed on
the d-dimensional torus, where P is a polynomial of degree at most 3 and B is a
bilinear map that is not a total derivative. We show that, if the initial condition u0
is taken from a sequence of smooth Gaussian ﬁelds with a speciﬁed covariance, then
u exhibits norm inﬂation with high probability. A consequence of this result is that
there exists no Banach space of distributions which carries the Gaussian free ﬁeld on
the 3D torus and to which the DeTurck–Yang–Mills heat ﬂow extends continuously,
which complements recent well-posedness results of Cao–Chatterjee and the author
with Chandra–Hairer–Shen. Another consequence is that the (deterministic) non-
linear heat equation exhibits norm inﬂation, and is thus locally ill-posed, at every
point in the Besov space B−1/2
∞,∞; the space B−1/2
∞,∞is an endpoint since the equation
is locally well-posed for Bη
∞,∞for every η > −1
2.
Keywords: Non-linear heat equation; norm inﬂation; Gaussian free ﬁeld; random Fourier series;
ill-posedness; Yang–Mills heat ﬂow.
2020 Mathematics Subject Classiﬁcation: Primary: 35K05, Secondary: 35R60
1
Introduction
We consider the initial value problem for a non-linear heat equation of the form
(
∂tu = ∆u + B(u, Du) + P(u)
on [0, T ] × Td
u(0, ·) = u0(·) ∈C∞(Td, E) ,
(1.1)
where Td = Rd/2πZd is the d-dimensional torus, E is a vector space (over R) of dimension
2 ≤dim(E) < ∞, B : E × Ed →E is a bilinear map, Du = (∂1u, . . . , ∂du), and P : E →E is a
polynomial of degree at most 3. In what follows, we assume B is not a total derivative, i.e., if
we write B for y = (y1, . . . , yd) ∈Ed as
B(·, y) = B1(·, y1) + . . . + Bd(·, yd) ,
where Bi : E × E →E is bilinear, then we assume that Bi is not symmetric for some 1 ≤i ≤d.
We note that Bi is symmetric if and only if there exists a bilinear map ˜Bi : E × E →E such that
∂i ˜Bi(u, u) = Bi(u, ∂iu) for all smooth u.
∗School of Mathematics, The University of Edinburgh, Edinburgh EH9 3FD, United Kingdom.
ichevyrev@gmail.com
1

--- Page 2 ---

It is easy to show that, for η > −1
2, a solution u to (1.1) exists for T > 0 suﬃciently small
depending (polynomially) on |u0|Cη, where Cη = Bη
∞,∞is the H¨older–Besov space of regularity η
(see Section 2.1 for a deﬁnition of Bα
p,q). Furthermore, the map Cη ∋u0 7→u is locally Lipschitz
once the target space is equipped with a suitable norm and T is taken suﬃciently small on each
ball in Cη. We give a proof of these facts in Appendix B. (If each Bi were symmetric, these facts
would hold for η > −1.)
The goal of this article is to prove a corresponding local ill-posedness result for a family of
function spaces that carry suﬃciently irregular Gaussian ﬁelds. Leaving precise deﬁnitions for
later, the main result of this article can be stated as follows.
Theorem 1.1. Suppose that X is an E-valued Gaussian Fourier series (GFS) on Td whose
Fourier truncations {XN}N≥1 satisfy Assumption 2.6 below. Then there exists another E-valued
GFS Y , deﬁned on a larger probability space, such that Y
law
= X and, for every δ > 0,
lim
N→∞P
h
sup
t∈[0,δ]

Z
Td ut(x) dx
 > δ−1i
= 1 ,
where u is the solution to (1.1) with u0 = XN + Y N and if u blows up at or before time δ, then
we treat supt∈[0,δ] |
R
Td ut(x) dx| = ∞.
We formulate a more general and precise statement in Theorem 2.13 below. See the end of
Section 2 for a description of the proof and of the structure of the article. The deﬁnition of an
E-valued GFS is given in Section 2.3.
Remark 1.2. The Gaussian free ﬁeld X on Td with E|Xk|2 = |k|−2 for k ̸= 0 (see e.g. [She07])
is a GFS (for any d ≥1) and X satisﬁes Assumption 2.6 for d = 3 (but not other values of d).
There is considerable interest in studying partial diﬀerential equations (PDEs) with random
initial conditions in connection to local and global well-posedness; for dispersive PDEs, see for in-
stance [Bou94, BT08, OP16, Poc17] and the review article [BOP19]; for recent work on parabolic
PDEs, see [CC23, CCHS22b, HLR23].
Furthermore, there have been many developments in
the past decade in the study of singular stochastic PDEs with both parabolic [Hai14, GIP15,
BCCH21] and dispersive [GKO18, GKOT21, Tol21] dynamics, for which it is often important to
understand the eﬀect of irregularities of (random) initial condition.
In [CC23, CCHS22b], it is shown that (1.1) is locally well-posed1 for the GFF X on T3, in
the sense that, if u0 = XN, then u converges in probability as N →∞to a continuous process
with values in Cη for η < −1/2, at least over short random time intervals; we discuss these
works in more detail at the end of this section. Theorem 1.1 therefore shows the importance of
taking precisely the GFF X in these works, rather than another Gaussian ﬁeld which has the
same regularity as X when measured in any normed space. We note that Y in Theorem 1.1 can
therefore clearly not be taken independent of X.
We now state a corollary of Theorem 1.1 and of the construction of Y which elaborates on
this last point and is of analytic interest. Consider a Banach space (I, ∥· ∥) of distributions with
(continuous) inclusions C∞⊂I ⊂S′(Td, R). Let
(ˆI, ∥· ∥) ,
ˆI ⊂S′(Td, E) ,
1Strictly speaking, only the DeTurck–Yang–Mills heat ﬂow, which is a special form of (1.1), was
considered in [CC23, CCHS22b] but the methods therein apply to the general form of (1.1); further-
more, only molliﬁer approximations were considered in [CCHS22b], but the methods apply to Fourier
truncations.
2

--- Page 3 ---

denote the Banach space of all E-valued distributions of the form P
a∈A xaT a, where each xa ∈I
and {T a}a∈A is some ﬁxed basis of E, with norm ∥P
a∈A xaT a∥
def
= P
a ∥xa∥. We say that there
is norm inﬂation for (1.1) at x ∈ˆI if, for every δ > 0, there exists a solution u to (1.1) such that
∥x −u0∥< δ
and

Z
Td ut(x) dx
 > δ−1 .
(1.2)
This notion of norm inﬂation is slightly stronger than the usual one introduced by Christ–
Colliander–Tao [CCT03] in their study of the wave and Schr¨odinger equations, for which only
x = 0 and ∥ut∥> δ−1 are considered in (1.2). Norm inﬂation (in the sense that ∥ut∥> δ−1) at
arbitrary points x ∈ˆI was shown by Xia [Xia21] for the non-linear wave equation below critical
scaling. Oh [Oh17] showed that there is norm inﬂation for the cubic non-linear Schr¨odinger
equation at every point in negative Sobolev spaces at and below the critical scaling.
Norm inﬂation captures a strong form of ill-posedness of (1.1): (1.2) in particular shows that
the solution map C∞∋u0 7→u ∈C([0, T ], S′) is discontinuous at x in ˆI, even locally in time.
See [IO15, CK17, OW18, Kis19] and [BP08, CD14, MT15] where norm inﬂation of various types
is shown for dispersive and parabolic PDEs respectively.
Consider now a family of non-negative numbers σ2 = {σ2(k)}k∈Zd. We say that I carries
the GFS with variances σ2 if
lim
N→∞∥X −XN∥= 0
in probability
(1.3)
whenever {Xk}k∈Zd is a family of (complex) Gaussian random variables such that E|Xk|2 = σ2(k)
and XN def
= P
|k|≤N Xkei⟨k,·⟩is a real GFS for every N ≥1 (see Deﬁnition 2.5), and where X is
a real GFS.
Example 1.3. For d = 1 and η < −1
2, I
def
= Cη carries the GFS with variances σ2 ≡1, which
corresponds to white noise on T1 and which satisﬁes Assumption 2.6.
Corollary 1.4. Suppose I carries the GFS with variances σ2 = {σ2(k)}k∈Zd satisfying the
bounds in Assumption 2.6. Suppose that the law of X in (1.3) has full support in I. Then there
is norm inﬂation for (1.1) at every point in ˆI.
The proof of Corollary 1.4 is given in Section 2.4. We note that a simple criterion for the
law of X to have full support in I is that every σ2(k) > 0 and that the smooth functions are
dense in I (see Remark 2.14).
Note that the Besov space C−1/2 = B−1/2
∞,∞is an ‘endpoint’ case since (1.1) is well-posed
on Cη for every η > −1
2. In Proposition A.1(i) below, we show that C−1/2 carries a GFS with
variances σ2 satisfying the bounds in Assumption 2.6. Corollary 1.4, together with Remark 2.14
and Proposition A.1(i), therefore gives a probabilistic proof of the following result, which appears
to be folklore.
Corollary 1.5. There is norm inﬂation for (1.1) at every point in C−1/2(Td, E).
We remark that C−1 is the scaling critical space for (1.1), so our results show ill-posedness
above scaling criticality. Norm inﬂation of the same type as (1.2) in C−2/3 was shown for the
cubic non-linear heat equation (NLH) ∂tu = ∆u±u3 by the author and Oh–Wang [COW22] using
a Fourier analytic approach taking its roots in [IO15, Oh17, Kis19]. The method of [COW22] can
likely be adapted to yield norm inﬂation for (1.1) in C−1/2, and we expect that the methods of
this article can similarly be adapted to show (probabilistic) norm inﬂation for the cubic NLH. We
3

--- Page 4 ---

remark, however, that our method appears not to reach B−1/2
∞,q for q < ∞(see Proposition A.1(ii)),
while the method in [COW22] for the cubic NLH does extend to B−2/3
∞,q
for q > 3.
Corollary 1.5 should be contrasted with the 3D Navier–Stokes equations (NSE) for which
norm inﬂation (in a slightly weaker sense than (1.2)) was shown in the scaling critical space C−1 by
Bourgain–Pavlovi´c [BP08] and which is locally well-posed in Cη for η > −1 (the main diﬀerence
with (1.1) is that the non-linearity in NSE is a total derivative). In fact, norm inﬂation for NSE
has been shown in B−1
∞,q for q > 2 by Yoneda [Yon10] and for all q ∈[1, ∞] by Wang [Wan15]. We
remark that our analysis (and generality of results) relies on the fact that any space carrying X
as in Theorem 1.1, in particular C−1/2, is scaling subcritical. See also [CP18] and [FO20] where
norm inﬂation is established for the fractional non-linear Schr¨odinger (NLS) and non-linear wave
(NLW) equations respectively above the critical scaling.
In [ST20] and [CG23], norm inﬂation is shown for the NLW and NLS respectively for all
initial data u0 belonging to a dense Gδ subset of the scaling supercritical Sobolev space and
where the approximation x is taken as a molliﬁcation of u0. These works in particular imply a
statement similar to Corollary 1.5 for the NLW and NLS but with a more precise description of
the approximating sequence that exhibits norm inﬂation (cf. [Oh17, Xia21]).
We ﬁnish the introduction by describing one of the motivations for this study. The author and
Chandra–Hairer–Shen in [CCHS22a, CCHS22b] analysed the stochastic quantisation equations
of the Yang–Mills (YM) and YM–Higgs (YMH) theories on T2 and T3 respectively (see also the
review article [Che22]); we also mention that Bringmann-Cao [BC23] analysed the YM stochastic
quantisation equations on T2 by means of para-controlled calculus (vs. regularity structures as
in [CCHS22a]), and that the invariance of the YM measure on T2 for this dynamic was shown
in [CS23]. In [CCHS22b], the authors in particular constructed a candidate state space for the
YM(H) measure on T3. A related construction was also proposed by Cao–Chatterjee [CC21,
CC23]. An ingredient in the construction of [CCHS22b] is a metric space I of distributions such
that the solution map of the DeTurck–YM(H) heat ﬂow (or of any equation of the form (1.1),
see [CCHS22b, Prop. 2.9]) extends continuously locally in time to I and such that suitable
smooth approximations of the GFF on T3 converge in I; essentially the same space was identiﬁed
in [CC23]. The works [CC23, CCHS22b] thus provide a local well-posedness result for (1.1) with
the GFF on T3 as initial condition.
In contrast, our results provide a corresponding ill-posedness result. Indeed, the GFF on
T3 satisﬁes Assumption 2.6 and the DeTurck–YM(H) heat ﬂow is an example of equation (1.1)
covered by our results (see Examples 2.2 and 2.3). Theorem 1.1 and Corollary 1.4 therefore
imply that the metric space I in [CCHS22b] is not a vector space, and, more importantly, that
this situation is unavoidable. That is, there exists no Banach space of distributions which carries
the GFF on T3 and admits a continuous extension of the DeTurck–YM(H) heat ﬂow. Since the
3D YM measure (at least in a regular gauge) is expected to be a perturbation of the standard
3D GFF, this suggests that every sensible state space for the 3D YM(H) measure is necessarily
non-linear (cf. [Che19, CCHS22a] in which natural linear state spaces for the 2D YM measure
were constructed).
A non-existence result in the same spirit was shown for iterated integrals of Brownian paths
by Lyons [Lyo91] (see also [LCL07, Prop. 1.29] and [FH20, Prop. 1.1]); the construction of the
ﬁeld Y in Theorem 1.1 is inspired by a similar one in [Lyo91].
4

--- Page 5 ---

2
Preliminaries and main result
2.1
Fourier series and Besov spaces
We recall the deﬁnition of Besov spaces that we use later. Thorough references on this topic
include [BCD11, Tri83]; see also [GIP15, Appendix A] and [MW17, Appendix A] for concise
summaries. Let χ−1, χ ∈C∞(Rd, R) take values in [0, 1] such that supp χ−1 ⊂B0(4/3) and
supp χ ⊂B0(8/3) \ B0(3/4), where Bx(r) = {y ∈Rd : |x −y| ≤r}, and P∞
ℓ=−1 χℓ= 1, where
χℓ
def
= χ(2−ℓ·) for ℓ≥0.
Let i = √−1 and, for k ∈Zd, let ek = ei⟨k,·⟩∈C∞(Td) denote the orthonormal Fourier basis;
here and below, we equip Td = Rd/2πZd with the normalised Lebesgue measure of total mass 1.
For f ∈S′(Td) denote fk = ⟨f, ek⟩=
R
Td f(x)e−k(x) dx and, for ℓ≥−1, deﬁne ∆ℓf ∈C∞(Td)
by
∆ℓf =
X
k∈Zd
χℓ(k)fkek .
For s ∈R and 1 ≤p, q ≤∞, we deﬁne the Besov norm of f ∈C∞(Td) by
|f|Bα
p,q
def
=
 X
ℓ≥−1
2αℓq|∆ℓf|q
Lp(Td)
1/q
< ∞.
We let Bα
p,q be the space obtained by completing C∞(Td) with this norm, which one can identify
with a subspace of distributions S′(Td). We use the shorthand Cα = Bα
∞,∞.
We let Pt = et∆: S′(Td) →C∞(Td) for t > 0 denote the heat ﬂow (with P0 = id as usual).
In particular, Ptek = e−|k|2tek for all k ∈Zd. We denote by ΠN : S′(Td) →C∞(Td) the Fourier
truncation operator
ΠNξ =
X
|k|≤N
ξkek .
2.2
Assumptions on the equation
Consider E, B, P as in Section 1. Without loss of generality, we will assume B1 is not symmetric
and henceforth make the following assumption.
Assumption 2.1. Fix a basis {T a}a∈A of E. There exist a ̸= b ∈A such that B1(T a, T b) ̸=
B1(T b, T a).
The next two examples show that our results cover the DeTurck–YM(H) heat ﬂow.
Example 2.2 (Yang–Mills heat ﬂow with DeTurck term). Let E = gd, where g is a non-Abelian
ﬁnite-dimensional Lie algebra with Lie bracket [·, ·]. We write elements of E as X = Pd
j=1 Xj dxj,
Xj ∈g. The DeTurck–YM heat ﬂow is
∂tXj = ∆Xj +
d
X
i=1
[Xi, 2∂iXj −∂jXi + [Xi, Xj]] ,
1 ≤j ≤d .
(DYM)
To bring this into the form (1.1), we write elements of Ed as (∂1Y, . . . , ∂dY ) ∈Ed, ∂iY =
P
j ∂iY j dxj ∈E, ∂iY j ∈g. Deﬁne B : E × Ed →E by
B(X, Y ) =
d
X
i,j=1
[Xi, 2∂iY j −∂jY i] dxj ,
5

--- Page 6 ---

so that the corresponding Bi : E × E →E is
Bi(X, Y ) =
d
X
j=1
[Xi, 2Y j −δi,jY j] dxj .
Then Bi is not symmetric for every 1 ≤i ≤d since Bi(X, Y ) = [Xi, Y i] dxi+P
j̸=i cj dxj for some
cj ∈g and [Xi, Y i] is anti-symmetric and non-zero for some X, Y ∈E since g is non-Abelian.
Equation (DYM) therefore satisﬁes Assumption 2.1.
Example 2.3. The same example as above shows that the DeTurck–YM–Higgs heat ﬂow (with or
without the cube of the Higgs ﬁeld, see [CCHS22b, Eq. (1.9) resp. (2.2)]) satisﬁes Assumption 2.1.
Example 2.4. If dim(E) = 1, then Assumption 2.1 is never satisﬁed.
2.3
Gaussian Fourier series
Deﬁnition 2.5. A complex Gaussian Fourier series (GFS) is an S′(Td, C)-valued random vari-
able X such that {Xk}k∈Zd is a family of complex Gaussians with EX2
k = 0 for all k ̸= 0 and
Xk and Xn are independent for all k, n ∈Zd such that k /∈{−n, n}. Here, as before, we denote
Xk
def
= ⟨X, ek⟩. A real GFS is a complex GFS X such that X−k = Xk for all k ∈Zd. An E-valued
GFS is an S′(Td, E)-valued random variable such that X = P
a∈A XaT a with {Xa}a∈A a family
of independent real GFSs.
The sequence {E|Xk|2}k∈Zd uniquely determines the law of a real GFS X. Conversely, a real
GFS can be constructed from any sequence {σ2(k)}k∈Zd with polynomial growth by taking a set
K ⊂Zd such that K ∩(−K) = ̸# and K ∪(−K) = Zd \ {0}, deﬁning {Xk}k∈K as a family of
independent complex Gaussians with E|Xk|2 = σ2(k) and EX2
k = 0, and setting X−k = Xk for
all k ∈K, and X0 as a real Gaussian with E|X0|2 = σ2(0).
Assumption 2.6. Suppose {XN}N≥1 is a family of E-valued GFSs such that2
C−1k−d+1| log k|−1| log log k|−1 ≤σ2
N(k)
def
= E|XN
k |2 ≤Ck−d+1 ,
for all k0 ≤|k| ≤N, and σ2
N(k) ≤C for 0 ≤|k| < k0, where k0, C > 0 are independent of N,
and σ2(k) = 0 for |k| > N.
Example 2.7. Let X be an E-valued GFS with E|Xk|2 = k−d+1 for k ̸= 0. Then XN def
= ΠNX
satisﬁes Assumption 2.6.
Remark 2.8. The upper bound σ2
N(k) ≤Ck−d+1 in Assumption 2.6 can be relaxed to σ2
N(k) ≤
Ckγ for γ ∈[−d+1, −d+1+ε] for some suﬃciently small ε > 0 without changing the statement
of Theorem 2.13 below. We restrict to γ = −d + 1 only for simplicity.
Lemma 2.9. Let η < −1
2 and suppose that the upper bound on σ2
N(k) in Assumption 2.6 holds.
Then supN E|XN|p
Cη < ∞for all p ∈[1, ∞).
Proof. This follows from a standard Kolmogorov-type argument (similar to and simpler than
the proof of Lemma 3.2). It also follows directly from the sharper result of Proposition A.1(ii)
combined with the obvious embedding Bα
p,q ֒→Bα
p,∞.
2For k ∈Zd, we use the shorthand log k = log |k| and kγ = |k|γ.
6

--- Page 7 ---

Remark 2.10. The logarithmic factors in Assumption 2.6 are considered to allow for endpoint
cases; we will see in Proposition A.1 that they allow for XN def
= ΠNX to converge to a GFS X in
C−1/2, which would not be the case without these factors. This allows us to show norm inﬂation
for (1.1) in C−1/2 (Corollary 1.5).
If these logarithmic factors are dropped, then |Π0uT | >
c log log log N in (2.1) can be replaced by inft∈[N −2+ε,T ] |Π0ut| > c log N for any ε > 0.
2.4
Main result
Deﬁnition 2.11. For a distribution ξ ∈S′(Td, C), we deﬁne Rξ ∈S′(Td, C) as the unique
distribution such that, for all k ∈Zd,
(Rξ)k
def
= ⟨Rξ, ek⟩=





iξk
if k1 > 0 ,
−iξk
if k1 < 0 ,
ξk
if k1 = 0 .
If ξ satisﬁes the reality condition ξ−n = ξn, then so does Rξ. Furthermore, if X is a real
GFS, then so is RX and RX
law
= X. Recall now Assumption 2.1.
Deﬁnition 2.12. For an E-valued GFS X, we deﬁne another E-valued GFS Y = P
c∈A Y cT c
by setting, for each c ̸= b, Y c law
= Xc and independent of X, and setting Y b = RXa.
Note that Y can be deﬁned on a larger probability space than that of X and that Y
law
= X
by construction. The following is the main result of this article.
Theorem 2.13. Suppose B satisﬁes Assumption 2.1 and {XN}N≥1 satisﬁes Assumption 2.6.
Deﬁne Y N as in Deﬁnition 2.12, u0
def
= XN + Y N, and let u be the solution to (1.1). Then there
exist M, c > 0 such that, for every ε > 0, if we set T = (log N)−M for N ≥2,
lim
N→∞P[u exists on [0, T ] × Td & |Π0uT | > c log log log N] = 1 .
(2.1)
The proof of Theorem 2.13 is given in Section 6. Before continuing, we note that Theorem 2.13
clearly proves Theorem 1.1. We can now also give the proof of Corollary 1.4.
Proof of Corollary 1.4. Let X be an E-valued GFS with E|Xa
k|2 = σ2(k) for every a ∈A, and
let Y be deﬁned as in Deﬁnition 2.12. It follows from the assumption that I carries the GFS
with variances σ2(k) that the law of Z
def
= X + Y is a Gaussian measure on the Banach space ˆI
and that
lim
N→∞∥ZN −Z∥= 0
in probability.
(2.2)
By the assumption that the law of Xa has full support in I, it follows that Z has full support
in ˆI. (One only needs to be careful about the component T b for which Zb = Xb + RXa since
this is not independent of Za = Xa + Y a. However, since Xb is independent of {Xc}c̸=b and of
Y , we indeed obtain that the law of Z has full support in ˆI.)
Now, for every x ∈ˆI and δ > 0, one has ε
def
= P[∥Z −x∥< δ/2] > 0. Furthermore, it follows
from (2.2) that, for all N suﬃciently large,
P[∥ZN −x∥< δ] > ε/2 .
The conclusion follows from Theorem 2.13 (or, more simply, Theorem 1.1).
7

--- Page 8 ---

Remark 2.14. In the context of Corollary 1.4, a suﬃcient condition for the law of the real GFS
X in (1.3) to have full support in I is that σ2(k) > 0 for all k ∈Zd and that the smooth functions
are dense in I. Indeed, the condition σ2(k) > 0 implies that the Cameron–Martin space of X
contains all trigonometric functions, which are dense in the smooth functions.
We brieﬂy outline the proof of Theorem 2.13 and the structure of the rest of the article.
Dropping the reference to N, in Section 3 we show that all the quadratic terms in B(Pt(X +
Y ), DPt(X + Y )) are controlled uniformly in N ≥1 and t ∈(0, 1) except for the spatial mean
J
def
= Π0[B1(PtXaT a, ∂1PtY bT b) + B1(PtY bT b, ∂1PtXaT a))] .
In Section 4 we show that J −EJ is controlled uniformly in N, t, together with an upper bound
EJ ≤CN 2 ∧t−1 uniformly in N, t and a lower bound as t →0 and N > t−1/2
t−1| log t|−1(log | log t|)−1 ≤CEJ .
(2.3)
Finally, in Section 5, we show that the solution ut to (1.1) tracks closely the ﬁrst Picard iterate
Ptu0 +
R t
0 B(Psu0, DPsu0) ds at all times t ≤(log N)−M. Since this ﬁrst Picard iterate blows
up like log log log N at time t = (log N)−M due to (2.3), this allows us to conclude the proof
of Theorem 2.13 in Section 6. In Appendix A, we give conditions under which the Besov space
Bα
∞,q for α ∈R and q ∈[1, ∞] carries the GFS with a speciﬁed covariance σ2.
3
Decorrelated terms
In the remainder of the article, we will use x ≲y to denote that x ≤Cy for some ﬁxed
proportionality constant C > 0, and likewise let x ≍y to denote C−1x ≤y ≤Cx. We let x ≫1
and x ≪1 denote x > C and 0 < x < C−1 respectively for some suﬃciently large ﬁxed C > 0.
In this section, we let X and Y be real GFSs such that EXkYn = 0 for all k ̸= −n and such
that there exists C > 0 such that, for all k ∈Zd
E|Xk|2 + E|Yk|2 ≤C(|k| + 1)−d+1
We will apply the results of this section to the three cases X = Y , RX = Y , or X and Y are
independent. We record the following lemma, the proof of which is straightforward and we omit.
Lemma 3.1. Consider m, n, ¯m, ¯n ∈Zd with m + n ̸= 0.
Then EXmYnX ¯mY¯n = 0 unless
(−m, −n) = ( ¯m, ¯n) or (−m, −n) = (¯n, ¯m).
Let π0ξ = ξ −Π0ξ denote the projection onto the zero-mean distributions.
Lemma 3.2. Consider 1 ≤i ≤d, δ ∈(0, 1] and β < 0 such that β + 2(1 −δ) < 0 and δ >
1−d
4. Then every moment of supt∈(0,1) tδ|π0(PtX∂iPtY )|Cβ is ﬁnite and depends only on C, δ, β.
Furthermore, if X and Y are independent, then the same holds for supt∈(0,1) tδ|(PtX∂iPtY )|Cβ.
Proof. Let us denote Zt = tδPtX∂iPtY for t ∈(0, 1] and Z0 = 0. We will show that there exists
κ > 0 such that for all p ≥1
E|π0(Zu −Zt)|p
Cβ ≲|u −t|κp
(3.1)
uniformly over 0 ≤t < u ≤1, from which the ﬁrst statement follows by Kolmogorov’s continuity
theorem [FV10, Thm. A.10]. The second statement will be shown in a similar way. It suﬃces to
consider t < u ≤2t.
8

--- Page 9 ---

For every p ≥1 and ℓ≥0,
E|∆ℓπ0(Zu −Zt)|2p
L2p =
Z
Td E|(∆ℓπ0(Zu −Zt))(x)|2p dx .
(3.2)
By equivalence of Gaussian moments, the ﬁnal integral is bounded above by a constant C(p) > 0
times
Z
Td(E|(∆ℓπ0(Zu −Zt))(x)|2)p dx =
Z
Td
E
 X
k̸=0
χℓ(k)Fk
t,uek(x)
2
p
dx ,
(3.3)
where Fk
t,u
def
= ⟨Zu −Zt, ek⟩is the k-th Fourier coeﬃcient of Zu −Zt
Fk
t,u =
X
m+n=k
ψt,u(m2 + n2)iniXmYn ,
where
ψt,u(x) = uδe−xu −tδe−xt .
For 0 ̸= k ̸= −¯k, observe that EFk
t,uF¯k
t,u = 0 due to Lemma 3.1. Hence
E
 X
k̸=0
χℓ(k)Fk
t,uek(x)
2
=
X
k̸=0
χℓ(k)2E|Fk
t,u|2 .
Again by Lemma 3.1, for k ̸= 0,
E|Fk
t,u|2 =
X
m+n=k
ψt,u(m2 + n2)2(n2
i EXmYnX−mY−n + nimiEXmYnX−nY−m)
≲
X
m+n=k
ψt,u(m2 + n2)2n2
i (|m| + 1)−d+1(|n| + 1)−d+1 .
(3.4)
Since 0 < δ ≤1, observe that, for κ > 0 small, uniformly in x ≥1 and 0 < t < u ≤2t < 1,
ψt,u(x)2 ≲t2δe−2xt|t −u|κxκ + e−2xu|t −u|2δ ≲e−2xtt2δ−κ|t −u|κxκ ≲|t −u|κx−2δ+2κ , (3.5)
where we used that e−xxp ≲1 for any p > 0 in the ﬁnal bound.
We split the sum (3.4) into two parts with |m| ≤2|k| and |m| > 2|k|. The ﬁrst part is
bounded above by a multiple of
|t −u|κk−4δ+4κ
X
1≤|m|≤2|k|
m−d+1|k −m|−d+3 ≲|t −u|κk−d+4+4κ−4δ ,
where we used (3.5) and
X
1≤|m|≤|k|/2
m−d+1|k −m|−d+3 ≍
X
|k|/2≤|m|≤2|k|
m−d+1|k −m|−d+3 ≍k−d+4 .
The second part is bounded by a multiple of
|t −u|κ
X
|m|>2|k|
m−4δ+4κm−2d+4 ≍|t −u|κk−4δ+4κ+4−d ,
9

--- Page 10 ---

where we again used (3.5) and the fact that −4δ + 4κ −2d + 4 < −d for κ > 0 small since
δ > 1 −d
4 by assumption. In conclusion, E|Fk
t,u|2 ≲|t −u|κk−4δ+4κ+4−d, and thus
E
 X
k̸=0
χℓ(k)Fk
t,uek(x)
2
≲|t −u|κ2ℓ(−4δ+4κ+4) .
(3.6)
Consequently, by (3.2), (3.3), and (3.6),
E|π0(Zu −Zt)|2p
Bβ
2p,2p =
X
ℓ≥−1
22pℓβE|∆ℓπ0(Zu −Zt)|2p
L2p ≲
X
ℓ≥−1
|t −u|κp22pℓβ+ℓ(4−4δ+4κ)p .
Since 2β + 4 −4δ < 0, we can take κ > 0 suﬃciently small such that the series is summable in ℓ.
Recall the Besov embedding Bα
p1,q1 ֒→Bα−d(1/p1−1/p2)
p2,q2
for 1 ≤p1 ≤p2 ≤∞, 1 ≤q1 ≤q2 ≤∞,
and α ∈R (see, e.g., [GIP15, Lem. A.2]). Taking p2 = q2 = ∞, α = β, and p1 = q1 = 2p, we
obtain (3.1) (with β replaced by β −d/(2p) but where we can take p arbitrarily large), which
completes the proof of the ﬁrst statement.
For the second statement, since EF0
t,uFk
t,u = 0 for k ̸= 0, it suﬃces to show E|F0
t,u|2 ≲|t−u|κ
uniformly in 0 < t < u ≤2t < 1. If X and Y are independent, then clearly EXmYnX ¯mY¯n =
EXmX ¯mEYnY¯n, and thus, for κ > 0 small,
E|F0
t,u|2 =
X
m∈Zd
ψt,u(2m2)2(m2
i E|Xm|2E|Ym|2) ≲
X
m̸=0
ψt,u(2m2)2m2
i m−2d+2 ≲|t −u|κ ,
where the ﬁnal bound follows from (3.5) and the fact that −4δ −2d + 4 < −d.
4
Correlated terms
We now take {XN}N≥1 satisfying Assumption 2.6. We will drop N from our notation, writing
simply X for XN. Recall that Assumption 2.1 is in place. We deﬁne Z : [0, 1] →R by
Zt =
X
n1>0
2e−2n2tn1|Xa
n|2 .
The importance of Zt is that, if ξ ∈C∞(Td, R) and 1 ≤i ≤d, then
Π0(ξ∂iRξ) =
X
n
iniξ−n(Rξ)n =
X
n1>0
(−ni)|ξn|2 +
X
n1<0
ni|ξn|2 +
X
n1=0
ini|ξn|2
=
(
−P
n1>0 2n1|ξn|2
if i = 1 ,
0
if i ̸= 1 .
(If i ̸= 1, the 1st and 2nd sums cancels and the 3rd is 0, and if i = 1, the 3rd sum is still 0 but
the 1st and 2nd sums are equal.) Similarly
Π0(Rξ∂iξ) =
X
n
ini(Rξ)−nξn =
X
n1>0
ni|ξn|2 +
X
n1<0
(−ni)|ξn|2 +
X
n1=0
ini|ξn|2
=
(P
n1>0 2n1|ξn|2
if i = 1 ,
0
if i ̸= 1 .
10

--- Page 11 ---

Therefore
Π0(PtRXa∂iPtXa) = −Π0(PtXa∂iPtRXa) =
(
Zt
if i = 1 ,
0
if i ̸= 1 .
Hence, for X, Y related as in Deﬁnition 2.12, by Lemma 3.2, the quantity which we expect to be
well-behaved uniformly in N is
B(Pt(X + Y ), DPt(X + Y )) + (B1(T a, T b) −B1(T b, T a))Zt .
The following lemma shows that Zt is well approximated by its expectation.
Lemma 4.1. Let δ > 1 −d
4. Then supt∈(0,1) tδ(Zt −EZt) has moments of all orders bounded
uniformly in N.
Proof. Deﬁne Wt = tδ(Zt −EZt). We will show that there exists κ > 0 such that, for all p ≥1,
E|Wu −Wt|p ≲|t −u|κp ,
uniformly in 0 ≤t < u ≤1 and N ≥1, from which the conclusion follows by Kolmogorov’s
continuity theorem [FV10, Thm. A.10]. It suﬃces to consider t < u ≤2t and, by equivalence of
Gaussian moments, p = 2.
Since Xa
n and Xa
m are independent if n ̸= m with n1, m1 > 0, and E|Xa
n|4 −(E|Xa
n|2)2 ≤
σ4(n) ≲n−2d+2, we obtain
E(Wu −Wt)2 ≍
X
n1>0
ψt,u(n2)2n2
1(E|Xa
n|4 −(E|Xa
n|2)2) ≲
X
n1>0
ψt,u(n2)2n−2d+4 ,
where
ψt,u(x) = tδe−2xt −uδe−2xu .
Recall from (3.5) that, for κ > 0 small, uniformly in 0 < t < u ≤2t < 1 and x ≥1,
ψt,u(x)2 ≲|t −u|κx−2δ+2κ .
We can take κ > 0 suﬃciently small such that −2d + 4 −4δ + 4κ < −d, and therefore
E(Wu −Wt)2 ≲|t −u|κ X
n1>0
n−2d+4−4δ+4κ ≍|t −u|κ .
We now show that EZt explodes as N →∞and t →0 in a controlled manner.
Lemma 4.2. It holds that
EZt ≲N 2 ∧t−1
(4.1)
uniformly in t ∈(0, 1) and in N ≥1. Furthermore,
EZt ≳t−1| log t|−1(log | log t|)−1
(4.2)
uniformly in 0 < t ≪1 and N > t−1/2.
Proof. Using the upper bound in Assumption 2.6, EZt is bounded above by a multiple of
X
1≤|n|≤N
e−n2tn−d+2 ≲
Z 2N
1
e−r2tr dr =
Z 2Nt1/2
t1/2
e−u2ut−1/2t−1/2 du ≍t−1 ∧N 2 .
11

--- Page 12 ---

On the other hand, using the lower bound in Assumption 2.6, EZt is bounded below by cK
where c > 0 is uniform in t ≪1 and N > t−1/2, and
K =
X
3≤|n|≤N
e−n2tn−d+2| log n|−1| log log n|−1
≳
Z N/2
4
e−r2tr| log r|−1| log log r|−1 dr
=
Z Nt1/2/2
4t1/2
e−u2ut−1/2| log(ut−1/2)|−1| log log(ut−1/2)|−1t−1/2 du
≳t−1| log t|−1(log | log t|)−1 .
Deﬁne the deterministic processes H, I : [0, 1] →E by
Ht
def
= (B1(T a, T b) −B1(T b, T a))EZt ,
It
def
=
Z t
0
Hs ds .
(4.3)
Observe that, by (4.1), uniformly in t ∈(0, 1) and N ≥1,
|It| =
Z t
0
|Hs| ds ≲
Z t∧N −2
0
N 2 ds +
Z t
t∧N −2 s−1 ds = (N 2t) ∧1 + log((N 2t) ∨1) ,
(4.4)
while by (4.2), uniformly in 0 < t ≪1 and N > t−1/2,
|It| ≳
Z t
N −2 s−1| log s|−1(log | log s|)−1 ds = log log log N 2 −log log log(t−1) .
(4.5)
Lemma 4.3. Consider a, b > −1 and p ≥1. Then, uniformly in N ≥2 and t ∈(0, 1),
Z t
0
(t −s)a|Is|psb ds ≲ta+b+1(log N)p .
Proof. If t ≤2N −2, then |It| ≲N 2t by (4.4), and therefore
Z t
0
(t −s)a|Is|psb ds ≲
Z t
0
(t −s)aN 2psb+p ds ≍ta+b+p+1N 2p ≲ta+b+1 .
On the other hand, if t > 2N −2 then (t −s)a ≍ta for s ≤N −2 and therefore, by (4.4),
Z t
0
(t −s)a|Is|psb ds ≲
Z N −2
0
(t −s)aN 2psb+p ds +
Z t
N −2(t −s)asb(log N)p ds
≍ta(N −2)b+1 + ta+b+1(log N)p ≲ta+b+1(log N)p .
5
Deterministic bounds
In this section, we let H, I : [0, 1] →E be deﬁned as in (4.3) from some {XN}N≥1 satisfying
Assumption 2.6. We consider N ≫1 and suppress it from our notation.
We further ﬁx δ ∈( 1
2, 1) and β ∈(−1, 0) such that ˆβ
def
= β + 2(1 −δ) ∈(−1
2, 0). We also ﬁx
η ∈(−2
3, −1
2) such that η + ˆβ > −1. For Q: (0, T ) →Cβ, deﬁne the norm
|Q|Cβ
δ;T
def
=
sup
t∈(0,T )
tδ|Q|Cβ .
12

--- Page 13 ---

Lemma 5.1. Suppose u0 ∈C∞and deﬁne the functions Nt = B(Ptu0, DPtu0) and Qt =
Nt −Ht. Then there exist κ > 0 small and C > 0 large, not depending on N, such that for all
T ∈(0, 1) with
T κ ≤
1
C(log N)3(1 + |Q|Cβ
δ;T + |u0|Cη)3 ,
(5.1)
it holds that the solution u to (1.1) exists on [0, T ] and
sup
t∈[0,T ]
|ut −Ptu0 −It|C ˆ
β ≤C(1 + |Q|Cβ
δ;T ) .
Proof. We decompose ut = Ptu0 + Rt + It where R solves the ﬁxed point
Rt = Mt(R)
def
=
Z t
0
Pt−s(B(us, Dus) + P(us)) ds −It
(5.2)
=
Z t
0
Pt−s[Qs + B(us, DRs) + B(Rs + Is, DPsu0) + P(us)] ds ,
where we used that Ht and It are constant in space in the ﬁnal equality. Deﬁne the Banach
space X = XT = {f ∈C((0, T ), C1) : |f|X < ∞} with norm
|f|X
def
=
sup
t∈(0,T )
|ft|C ˆ
β + t−ˆβ/2|ft|L∞+ t−
ˆ
β
2 + 1
2 |ft|C1 .
We will show that, for T satisfying (5.1), M is a contraction on the ball of radius K ≍1+|Q|Cβ
δ;T
in X, from which the conclusion follows.
Deﬁne Yt =
R t
0 Pt−sQs ds. Recalling the heat ﬂow estimates for α < 0 and γ ≥0 (see,
e.g. [GIP15, Lem. A.7] and the proof of [BCD11, Thm. 2.34])
t−α/2|Ptf|L∞+ t1/2−α/2|Ptf|C1 + tγ/2|Ptf|Cα+γ ≲|f|Cα ,
(5.3)
we obtain
|Yt|C ˆ
β ≲|Q|Cβ
δ;t
Z t
0
(t −s)β/2−ˆβ/2s−δ ds ≍|Q|Cβ
δ;t .
Similarly |Yt|L∞≲|Q|Cβ
δ;tt ˆβ/2 and |Yt|C1 ≲|Q|Cβ
δ;tt ˆβ/2−1
2 (in the last bound we used β > −1 so
that β/2 −1
2 > −1), thus |Y|X ≲|Q|Cβ
δ;T . Furthermore,
t−ˆβ/2
Z t
0
|Pt−sB(Psu0, DRs) + B(Rs, DPsu0)|L∞ds ≲|R|X |u0|Cηt−ˆβ/2
Z t
0
sη/2+ ˆβ/2−1
2 ds
≍t
1
2 + η
2 |R|X |u0|Cη ,
where we used ˆβ + η > −1, and
t−ˆβ/2
Z t
0
|Pt−sB(Rs, DRs)|L∞ds ≲|R|2
X t−ˆβ/2
Z t
0
s
ˆβ−1
2 ds ≍|R|2
X t
1
2 + ˆβ/2 ,
where we used ˆβ > −1
2. Moreover, by Lemma 4.3 with p = 1,
t−ˆβ/2
Z t
0
|Pt−sB(Is, DPsu0)|L∞ds ≲|u0|Cηt−ˆβ/2
Z t
0
|Is|sη/2−1/2 ds ≲|u0|Cηt
1
2 +η/2−ˆβ/2 log N
13

--- Page 14 ---

and
t−ˆβ/2
Z t
0
|Pt−sB(Is, DRs)|L∞ds ≲|R|X t−ˆβ/2
Z t
0
|Is|s
ˆβ/2−1/2 ds ≲t
1
2 |R|X log N .
Exactly the same bounds hold for the norm | · |C1 with t−ˆβ/2 replaced by t−ˆβ/2+ 1
2 in the ﬁrst
terms. Finally, the same bounds obviously hold for the norm | · |C ˆ
β ≲| · |L∞. This bounds the
ﬁrst set of terms in the deﬁnition (5.2) of Mt. It remains to bound
R t
0 Pt−sP(us) ds for which
we have, by Lemma 4.3 with p = 3,
t−ˆβ/2
Z t
0
|Pt−sP(us)|L∞ds ≲t−ˆβ/2
Z t
0
(1 + sη/2|u0|Cη + s
ˆβ/2|R|X + |Is|)3 ds
≲t−ˆβ/2(t + t3η/2+1|u0|3
Cη + t3 ˆβ/2+1|R|3
X + t(log N)3) .
Again the same bound obviously holds for the norm |·|C ˆ
β ≲|·|L∞, and also for the norm |·|C1 with
t−ˆβ/2 replaced by t−ˆβ/2+ 1
2 in the ﬁrst term. In conclusion, for κ = min{ 1
2 + η
2 +
ˆβ
2 , 1
2 + ˆβ, 3η
2 + 1},
|M(R)|X ≲|Q|Cβ
δ;T + T κ(log N)3(1 + |R|X + |u0|Cη)3 .
In exactly the same way,
|M(R) −M( ¯R)|X ≲T κ(log N)3|R −¯R|X (1 + |u0|Cη + |R|X + | ¯R|X )2 .
It follows that for K ≍1 + |Q|Cβ
δ;T and T κ(log N)3(K + |u0|Cη)3 ≲K, M is a contraction on the
ball in X of radius K as desired.
6
Proof of Theorem 2.13
We are now ready for the proof of Theorem 2.13. Consider M > 3/κ for the κ from Lemma 5.1,
and deﬁne T = (log N)−M for N ≫1. Deﬁne N, Q: [0, 1] →C∞as in Lemma 5.1 and I : [0, 1] →
E as in (4.3). Consider δ, β, η, ˆβ as in the previous section such that furthermore δ > 1 −d
4.
The moments of |u0|Cη are bounded uniformly in N (Lemma 2.9), and, by Lemmas 3.2
and 4.1, so are the moments of |Q|Cβ
δ;1. Therefore, for C as in Lemma 5.1,
lim
N→∞P

T κ ≤C−1(log N)−3(1 + |Q|Cβ
δ;T + |u0|Cη)−3
= 1 .
Hence, by Lemma 5.1,
lim
N→∞P

u exists on [0, T ] × Td & |uT −PT u0 −IT |C ˆ
β ≤C(1 + |Q|Cβ
δ;1)

= 1 .
Finally, since |IT | ≳log log log N by (4.5), and
|Π0(uT −PT u0 −IT )| + |Π0PT u0| < |IT |/2 ⇒|Π0uT | > |IT |/2 ,
we obtain (2.1) for c > 0 suﬃciently small, which concludes the proof of Theorem 2.13.
14

--- Page 15 ---

A
Besov regularity of Gaussian free ﬁelds
In this appendix, we consider a (real) GFS X (see Deﬁnition 2.5) and denote σ2(n)
def
= E|Xn|2.
If σ2(n) ≲|n|γ for n ̸= 0, then, for any η < −(d + γ)/2, it is classical that X ∈Cη and
|XN −X|Cη →0 a.s. as N →∞, where XN def
= ΠNX. The following result shows that, if σ2(n)
is logarithmically smaller, then we have improved behaviour.
Proposition A.1. Let γ, θ, η ∈R and suppose
K
def
= sup
|n|≥3
σ2(n)
nγ(log n)θ(log log n)η < ∞.
(i) If θ = −1 and η < 0, then almost surely limN→∞|XN −X|C−(d+γ)/2 = 0.
(ii) If θ < −1 and q > −2/(θ+1), then almost surely limN→∞|XN −X|B−(d+γ)/2
∞,q
= 0. Further-
more, supN E|XN|p
B−(d+γ)/2
∞,q
is ﬁnite for all p ∈[1, ∞) and depends only on p, q, γ, θ, η, d, K,
and {σ2(n)}|n|≤2.
Part (i) of Proposition A.1 is used to prove Corollary 1.5, while part (ii) proves Lemma 2.9.
For the proof of Proposition A.1, recall that if Z is an R-valued centred continuous Gaussian
process on Td (or, more generally, on a totally bounded metric space), then Dudley’s theorem
(see, e.g., [Mas07, Thm. 3.18]) implies that
E|Z|L∞≤24
Z σ
0
q
log N̺(r) dr ,
(A.1)
where N̺(r) is the minimum number of ̺-balls of radius r/2 needed to cover Td, ̺ is the metric
on Td deﬁned by
̺(x, y)2 = E[|Z(x) −Z(y)|2] ,
and
σ2 = sup
x∈Td E|Z(x)|2 .
Furthermore, one has the concentration inequality (see [Mas07, Prop. 3.19]) for all M ≥0
P[||Z|L∞−E|Z|L∞| ≥M] ≤2e−1
2 M2/σ2 .
(A.2)
Proof of Proposition A.1. Consider ℓ≥1 and deﬁne Zℓ= 2−ℓ(d+γ)/2∆ℓ(X −XN).
Clearly
Zℓ= 0 for ℓ≲log N. We henceforth consider ℓ≳log N. Then
σ2
Zℓ
def
= E|Zℓ(x)|2 ≲
X
k
χℓ(k)22−ℓ(d+γ)E[|Xk|2] ≲2dℓ2−ℓ(d+γ)2ℓγℓθ(log ℓ)η = ℓθ(log ℓ)η
uniformly in ℓ, N. Applying (A.2), we obtain for M > 0,
P[ℓ−θ/2(log ℓ)−η/2||Zℓ|L∞−E|Zℓ|L∞| > M] = P[||Zℓ|L∞−E|Zℓ|L∞| > ℓθ/2(log ℓ)η/2M]
≤2 exp

−1
2ℓθ(log ℓ)ηM 2/σ2
Zℓ

≤2e−M2/C ,
(A.3)
for C uniform in ℓ, M, N. To estimate E|Zℓ|L∞, observe that
̺(x, y)2 def
= E|Zℓ(x) −Zℓ(y)|2 ≲
X
k
χℓ(k)22−ℓ(d+γ)E|Xk|2|eikx −eiky|2
15

--- Page 16 ---

≲2ℓd2−ℓ(d+γ)2ℓγℓθ(log ℓ)η(1 ∧22ℓ|x −y|2)
= ℓθ(log ℓ)η(1 ∧22ℓ|x −y|2) .
Therefore, for r ≤σZℓ,
B̺
x(r/2) ⊃Bx(C2−ℓℓ−θ/2(log ℓ)−η/2r/2) ,
where B̺
x(ε) and Bx(ε) are the ̺- and Euclidean-balls respectively centred at x of radius ε, and
where C > 0 does not depend on ℓ, r.
Therefore N̺(r) ≲2ℓdℓθd/2(log ℓ)ηd/2r−d.
It follows
from (A.1) that, uniformly in ℓ,
E|Zℓ|L∞≲
Z ℓθ/2(log ℓ)η/2
0
(ℓd −d log r)1/2 dr ≲ℓθ/2+1/2(log ℓ)η/2 .
(A.4)
Proof of (i). Suppose now that θ = −1. Then, for all ε > 0,
P[||Zℓ|L∞−E|Zℓ|L∞| > ε] ≤2e−ℓ(log ℓ)−ηε2/C ,
which is clearly summable in ℓ. Suppose further that η < 0. Then E|Zℓ|L∞≲(log ℓ)η/2 →0.
Therefore, by the Borel–Cantelli lemma, for all ε > 0,
P
h
limsup
ℓ→∞
|Zℓ|L∞> ε
i
= 0 .
Hence, almost surely, as N →∞,
|XN −X|B−(d+γ)/2
∞,∞
≤
sup
ℓ≳log N
|Zℓ|L∞→0 .
Proof of (ii). Suppose now θ < −1, η ∈R arbitrary, and q > −2/(θ + 1). Then
|XN −X|q
B−(d+γ)/2
∞,q
≤
X
ℓ≳log N
|Zℓ|q
L∞≲
X
ℓ≳log N
||Zℓ|L∞−E|Zℓ|L∞|q +
X
ℓ≳log N
(E|Zℓ|L∞)q . (A.5)
For ε > 0 suﬃciently small, the second sum is bounded by a multiple of (log N)q(θ/2+1/2)+1+ε
due to (A.4) since q(θ/2+1/2) < −1, and thus converges to 0 as N →∞. Furthermore, by (A.3),
P[||Zℓ|L∞−E|Zℓ|L∞|q > ℓq(θ/2+1/2)] ≤2e−ℓ(log ℓ)−η/C ,
which is summable in ℓ. Therefore, again by the Borel–Cantelli lemma,
P
h
lim
N→∞
X
ℓ≳log N
||Zℓ|L∞−E|Zℓ|L∞|q = 0
i
= 1 ,
which proves the almost sure convergence.
For the ﬁnal claim that supN E|XN|p
B−(d+γ)/2
∞,q
is ﬁnite and depends only on the given pa-
rameters, it suﬃces to consider p = q since, by Fernique’s theorem, E|Y |p ≤Cp(E|Y |)p for any
centred Gaussian random variable Y with values in a separable Banach space3 (see, e.g. [Str23,
Cor. 3.2.7]). Then
E|XN −X|q
B−(d+γ)/2
∞,q
≤
X
ℓ≳log N
E|Zℓ|q
L∞≲
X
ℓ≳log N
(E|Zℓ|L∞)q ,
where in the ﬁnal bound we again used E|Zℓ|q
L∞≲(E|Z|L∞)q by Fernique’s theorem. The ﬁnal
sum is ﬁnite and bounded uniformly in N by the argument following (A.5).
3While Bβ
∞,q is not separable, we can work with the closure of smooth functions therein, which is
separable.
16

--- Page 17 ---

B
Well-posedness in the regime η > −1
2
In this appendix, we prove well-posedness of (1.1) in the regime u0 ∈Cη for η > −1
2 (we do not
require here that B is not a total derivative). We follow the notation of Sections 1 and 2.1 (and
start of Section 3).
Proposition B.1. For all η ∈(−1
2, 0), there exists δ > 0 with the following property. For T > 0,
deﬁne the Banach space XT = {f ∈C((0, T ), C1) : |f|XT < ∞} with norm
|f|XT
def
=
sup
t∈(0,T )
t−η−1
2 |ft|L∞+ t−η|ft|C1 .
For all K > 1 and u0 ∈Bη
K
def
= {v ∈Cη : |v|Cη < K}, if T η+1 < δK2, then there exists a unique
R ∈XT such that u
def
= Pu0 + R solves ∂tu = ∆u + B(u, Du) + P(u) on (0, T ) × Td and the map
Bη
K ∋u0 7→R ∈XT is δ−1K-Lipschitz.
Proof. For v ∈Cη and R ∈X, let us denote ut = Ptv + Rt and deﬁne
Mv
t (R) =
Z t
0
{B(us, Dus) + P(us)} ds .
By the elementary bound
R t
0 sa(t −s)b ds ≍ta+b+1 for a, b > −1, we have
t−η−1
2 |Mv
t (R)|L∞≲t−η−1
2
Z t
0
{|us|L∞|us|C1 + (1 + |us|L∞)3} ds
≲t−η−1
2
Z t
0
{sη−1
2 |v|2
Cη + s2η+ 1
2 |R|2
XT + 1 + s3η/2|v|3
Cη + s3η+ 3
2 |R|3
XT } ds
≍|v|2
Cη + tη+1|R|2
XT + t−η+ 1
2 + tη/2+ 1
2 |v|3
Cη + t2η+2|R|3
XT ,
where we used the heat ﬂow estimates (5.3) in the second line and that η > −1
2 in the third line
to estimate the integral R t
0 sη−1
2 |v|2
Cη ds ≍tη+ 1
2 |v|2
Cη. Using again (5.3), the same bound holds
with t−η−1
2 |Mv
t (R)|L∞replaced by t−η|Mv
t (R)|C1.
It follows that there exists ε > 0 such that, for all M > 0 suﬃciently large, K > 1, and
v ∈Bη
K, if T η+1 ≤εM −1K−2, then Mv stabilises the ball in XT centred at 0 of radius MK2.
Likewise, for another ¯v ∈Cη and ¯R ∈XT ,
t−η−1
2 |Mv
t (R) −M¯v
t ( ¯R)|L∞≲(|v|Cη + |¯v|Cη + tη/2+ 1
2 (|R|XT + | ¯R|XT ))
(|v −¯v|Cη + tη/2+ 1
2 |R −¯R|XT )
+ (1 + tη(|v|Cη + |¯v|Cη)2 + t2η+1(|R|XT + | ¯R|XT )2)
(t−η
2 + 1
2 |v −¯v|Cη + t|R −¯R|XT ) .
(B.1)
Again the same bound holds with t−η−1
2 | · · · |L∞replaced by t−η| · · · |C1. Applying this with
v = ¯v ∈Bη
K shows that Mv is a contraction on the ball in XT centred at 0 of radius MK2
provided T η+1 ≤εM −1K−2. This proves the existence of a unique ﬁxed point R = Mv(R) in
this ball. The uniqueness of R in all of XT follows by restarting the equation over suﬃciently
short time intervals.
Furthermore, applying (B.1) to two ﬁxed points R = Mv(R) and ¯R = M¯v( ¯R) with v, ¯v ∈Bη
K
shows that |R −¯R|XT ≲ε1/2M 1/2K|v −¯v|Cη provided T η+1 ≤εM −1K−2, which proves the
claimed local Lipschitz property.
17

--- Page 18 ---

Acknowledgements
The author would like to thank the anonymous referees for their detailed reading and comments
that have helped to improve the paper.
Data availability statement
Data sharing not applicable to this article as no datasets were generated or analysed during the
current study.
Funding
The author acknowledges support by the Engineering and Physical Sciences Research Council
via the New Investigator Award EP/X015688/1.
References
[BC23]
B. Bringmann and S. Cao. A para-controlled approach to the stochastic Yang-
Mills equation in two dimensions. arXiv e-prints (2023). arXiv:2305.07197.
[BCCH21]
Y. Bruned, A. Chandra, I. Chevyrev, and M. Hairer. Renormalising SPDEs
in regularity structures. J. Eur. Math. Soc. (JEMS) 23, no. 3, (2021), 869–947.
doi:10.4171/jems/1025.
[BCD11]
H. Bahouri, J.-Y. Chemin, and R. Danchin. Fourier analysis and nonlinear
partial diﬀerential equations, vol. 343 of Grundlehren der mathematischen Wis-
senschaften [Fundamental Principles of Mathematical Sciences]. Springer, Heidel-
berg, 2011, xvi+523. doi:10.1007/978-3-642-16830-7.
[BOP19]
A. B´enyi, T. Oh, and O. Pocovnicu.
On the probabilistic Cauchy the-
ory for nonlinear dispersive PDEs.
In Landscapes of time-frequency anal-
ysis,
Appl. Numer. Harmon. Anal., 1–32. Birkh¨auser/Springer, Cham,
2019.
doi:10.1007/978-3-030-05210-2_1.
[Bou94]
J. Bourgain.
Periodic nonlinear Schr¨odinger equation and invariant measures.
Comm. Math. Phys. 166, no. 1, (1994), 1–26. doi:10.1007/BF02099299.
[BP08]
J. Bourgain and N. Pavlovi´c.
Ill-posedness of the Navier-Stokes equations
in a critical space in 3D.
J. Funct. Anal. 255, no. 9, (2008), 2233–2247.
doi:10.1016/j.jfa.2008.07.008.
[BT08]
N. Burq and N. Tzvetkov.
Random data Cauchy theory for supercritical
wave equations. I. Local theory.
Invent. Math. 173, no. 3, (2008), 449–475.
doi:10.1007/s00222-008-0124-z.
[CC21]
S. Cao and S. Chatterjee. A state space for 3D Euclidean Yang-Mills theories.
arXiv e-prints (2021). arXiv:2111.12813.
[CC23]
S. Cao and S. Chatterjee.
The Yang-Mills heat ﬂow with random distribu-
tional initial data. Comm. Partial Diﬀerential Equations 48, no. 2, (2023), 209–251.
arXiv:2111.10652. doi:10.1080/03605302.2023.2169937.
18

--- Page 19 ---

[CCHS22a] A. Chandra, I. Chevyrev, M. Hairer, and H. Shen.
Langevin dynamic
for the 2D Yang-Mills measure.
Publ. math. IH´ES (2022).
arXiv:2006.04987.
doi:10.1007/s10240-022-00132-0.
[CCHS22b] A. Chandra, I. Chevyrev, M. Hairer, and H. Shen. Stochastic quantisation
of Yang-Mills-Higgs in 3D. arXiv e-prints (2022). arXiv:2201.03487.
[CCT03]
M. Christ, J. Colliander, and T. Tao. Ill-posedness for nonlinear Schrodinger
and wave equations. arXiv Mathematics e-prints (2003). arXiv:math/0311048.
[CD14]
A.
Cheskidov
and
M.
Dai.
Norm
inﬂation
for
generalized
Navier-
Stokes
equations.
Indiana
Univ.
Math.
J.
63,
no.
3,
(2014),
869–884.
doi:10.1512/iumj.2014.63.5249.
[CG23]
N. Camps and L. Gassot. Pathological Set of Initial Data for Scaling-Supercritical
Nonlinear Schr¨odinger Equations.
Int. Math. Res. Not. IMRN , no. 15, (2023),
13214–13254. doi:10.1093/imrn/rnac194.
[Che19]
I. Chevyrev.
Yang-Mills measure on the two-dimensional torus as a ran-
dom
distribution.
Comm.
Math.
Phys.
372,
no.
3,
(2019),
1027–1058.
doi:10.1007/s00220-019-03567-5.
[Che22]
I. Chevyrev.
Stochastic quantization of Yang–Mills.
Journal of Mathemat-
ical Physics 63, no. 9, (2022), 091101.
Proceedings of ICMP XX (2021).
arXiv:2202.13359. doi:10.1063/5.0089431.
[CK17]
R. Carles and T. Kappeler. Norm-inﬂation with inﬁnite loss of regularity for
periodic NLS equations in negative Sobolev spaces. Bull. Soc. Math. France 145,
no. 4, (2017), 623–642. doi:10.24033/bsmf.2749.
[COW22]
I. Chevyrev, T. Oh, and Y. Wang.
Norm inﬂation for the cubic nonlin-
ear heat equation above the scaling critical regularity.
arXiv e-prints (2022).
arXiv:2205.14488.
[CP18]
A. Choffrut and O. Pocovnicu. Ill-posedness of the cubic nonlinear half-wave
equation and other fractional NLS on the real line. Int. Math. Res. Not. IMRN ,
no. 3, (2018), 699–738. doi:10.1093/imrn/rnw246.
[CS23]
I. Chevyrev and H. Shen. Invariant measure and universality of the 2D Yang-Mills
Langevin dynamic. arXiv e-prints (2023). arXiv:2302.12160.
[FH20]
P. K. Friz and M. Hairer. A course on rough paths. Universitext. Springer, Cham,
2020, xvi+346. With an introduction to regularity structures, Second edition of [
3289027]. doi:10.1007/978-3-030-41556-3.
[FO20]
J. Forlano and M. Okamoto.
A remark on norm inﬂation for nonlin-
ear wave equations.
Dyn. Partial Diﬀer. Equ. 17, no. 4, (2020), 361–381.
doi:10.4310/DPDE.2020.v17.n4.a3.
[FV10]
P. K. Friz and N. B. Victoir. Multidimensional Stochastic Processes as Rough
Paths: Theory and Applications.
Cambridge Studies in Advanced Mathematics.
Cambridge University Press, 2010. doi:10.1017/CBO9780511845079.
[GIP15]
M. Gubinelli, P. Imkeller, and N. Perkowski. Paracontrolled distributions
and singular PDEs.
Forum Math. Pi 3, (2015), e6, 75.
arXiv:1210.2684v3.
doi:10.1017/fmp.2015.2.
19

--- Page 20 ---

[GKO18]
M. Gubinelli, H. Koch, and T. Oh. Renormalization of the two-dimensional
stochastic nonlinear wave equations. Trans. Amer. Math. Soc. 370, no. 10, (2018),
7335–7359. doi:10.1090/tran/7452.
[GKOT21] M. Gubinelli, H. Koch, T. Oh, and L. Tolomeo. Global Dynamics for the
Two-dimensional Stochastic Nonlinear Wave Equations. Int. Math. Res. Not. IMRN
(2021). Rnab084. doi:10.1093/imrn/rnab084.
[Hai14]
M. Hairer. A theory of regularity structures. Invent. Math. 198, no. 2, (2014),
269–504. arXiv:1303.5113. doi:10.1007/s00222-014-0505-4.
[HLR23]
M. Hairer, K. Lˆe, and T. Rosati.
The Allen-Cahn equation with generic
initial datum.
Probab. Theory Related Fields 186, no. 3-4, (2023), 957–998.
doi:10.1007/s00440-023-01198-5.
[IO15]
T. Iwabuchi and T. Ogawa. Ill-posedness for the nonlinear Schr¨odinger equation
with quadratic non-linearity in low dimensions. Trans. Amer. Math. Soc. 367, no. 4,
(2015), 2613–2630. doi:10.1090/S0002-9947-2014-06000-5.
[Kis19]
N.
Kishimoto.
A
remark
on
norm
inﬂation
for
nonlinear
Schr¨odinger
equations.
Commun.
Pure
Appl.
Anal.
18,
no.
3,
(2019),
1375–1402.
doi:10.3934/cpaa.2019067.
[LCL07]
T. J. Lyons, M. Caruana, and T. L´evy. Diﬀerential equations driven by rough
paths, vol. 1908 of Lecture Notes in Mathematics. Springer, Berlin, 2007, xviii+109.
doi:10.1007/978-3-540-71285-5.
[Lyo91]
T. Lyons. On the nonexistence of path integrals. Proc. Roy. Soc. London Ser. A
432, no. 1885, (1991), 281–290. doi:10.1098/rspa.1991.0017.
[Mas07]
P.
Massart.
Concentration
inequalities
and
model
selection,
vol.
1896
of
Lecture
Notes
in
Mathematics.
Springer,
Berlin,
2007,
xiv+337.
doi:10.1007/978-3-540-48503-2.
[MT15]
L. Molinet and S. Tayachi.
Remarks on the Cauchy problem for the one-
dimensional quadratic (fractional) heat equation. J. Funct. Anal. 269, no. 8, (2015),
2305–2327. doi:10.1016/j.jfa.2015.08.002.
[MW17]
J.-C.
Mourrat
and
H.
Weber.
The
dynamic
Φ4
3
model
comes
down
from
inﬁnity.
Comm.
Math.
Phys.
356,
no.
3,
(2017),
673–753.
doi:10.1007/s00220-017-2997-4.
[Oh17]
T. Oh. A remark on norm inﬂation with general initial data for the cubic nonlinear
Schr¨odinger equations in negative Sobolev spaces. Funkcial. Ekvac. 60, no. 2, (2017),
259–277. doi:10.1619/fesi.60.259.
[OP16]
T. Oh and O. Pocovnicu. Probabilistic global well-posedness of the energy-critical
defocusing quintic nonlinear wave equation on R3. J. Math. Pures Appl. (9) 105,
no. 3, (2016), 342–366. doi:10.1016/j.matpur.2015.11.003.
[OW18]
T. Oh and Y. Wang.
On the ill-posedness of the cubic nonlinear Schr¨odinger
equation on the circle. An. S¸tiint¸. Univ. Al. I. Cuza Ia¸si. Mat. (N.S.) 64, no. 1,
(2018), 53–84. arXiv:1508.00827.
[Poc17]
O. Pocovnicu. Almost sure global well-posedness for the energy-critical defocusing
nonlinear wave equation on Rd, d = 4 and 5. J. Eur. Math. Soc. (JEMS) 19, no. 8,
20

--- Page 21 ---

(2017), 2521–2575. doi:10.4171/JEMS/723.
[She07]
S. Sheffield. Gaussian free ﬁelds for mathematicians. Probab. Theory Related
Fields 139, no. 3-4, (2007), 521–541. doi:10.1007/s00440-006-0050-1.
[ST20]
C. Sun and N. Tzvetkov.
Concerning the pathological set in the context of
probabilistic well-posedness. C. R. Math. Acad. Sci. Paris 358, no. 9-10, (2020),
989–999. arXiv:2001.10293. doi:10.5802/crmath.102.
[Str23]
D. W. Stroock. Gaussian measures in ﬁnite and inﬁnite dimensions. Universitext.
Springer, Cham, [2023] ©2023, xii+144. doi:10.1007/978-3-031-23122-3.
[Tol21]
L. Tolomeo. Global well posedness of the two-dimensional stochastic nonlinear
wave equation on an unbounded domain. Ann. Probab. 49, no. 3, (2021), 1402–1426.
doi:10.1214/20-aop1484.
[Tri83]
H. Triebel.
Theory of function spaces, vol. 78 of Monographs in Mathematics.
Birkh¨auser Verlag, Basel, 1983, 284. doi:10.1007/978-3-0346-0416-1.
[Wan15]
B. Wang. Ill-posedness for the Navier-Stokes equations in critical Besov spaces
˙B−1
∞,q. Adv. Math. 268, (2015), 350–372. doi:10.1016/j.aim.2014.09.024.
[Xia21]
B.
Xia.
Generic illposedness for wave equation of power type on three-
dimensional torus.
Int. Math. Res. Not. IMRN , no. 20, (2021), 15533–15554.
doi:10.1093/imrn/rnaa068.
[Yon10]
T. Yoneda.
Ill-posedness of the 3D-Navier-Stokes equations in a generalized
Besov space near BMO−1.
J. Funct. Anal. 258, no. 10, (2010), 3376–3387.
doi:10.1016/j.jfa.2010.02.005.
21

```
