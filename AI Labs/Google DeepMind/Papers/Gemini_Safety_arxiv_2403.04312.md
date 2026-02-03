---
title: "Gemini Safety arxiv 2403.04312"
source_pdf: "AI Labs/Google DeepMind/Papers/Gemini_Safety_arxiv_2403.04312.pdf"
company: "Google DeepMind"
pages: 16
extracted_at: "2026-01-25T04:43:47.534716"
type: "ai_lab_paper"
---

# Gemini Safety arxiv 2403.04312

**Company/Lab:** Google DeepMind
**Source PDF:** AI Labs/Google DeepMind/Papers/Gemini_Safety_arxiv_2403.04312.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

arXiv:2403.04312v2  [math.NT]  10 Aug 2024
DISTRIBUTION OF POWER RESIDUES OVER SHIFTED SUBFIELDS AND
MAXIMAL CLIQUES IN GENERALIZED PALEY GRAPHS
GREG MARTIN AND CHI HOI YIP
ABSTRACT. We derive an asymptotic formula for the number of solutions in a given subﬁeld to cer-
tain system of equations over ﬁnite ﬁelds. As an application, we construct new families of maximal
cliques in generalized Paley graphs. Given integers d ≥2 and q ≡1 (mod d), we show that for
each positive integer m such that rad(m) | rad(d), there are maximal cliques of size approximately
q/m in the d-Paley graph deﬁned on Fqd. We also conﬁrm a conjecture of Goryainov, Shalaginov,
and Yip on the maximality of certain cliques in generalized Paley graphs, as well as an analogous
conjecture of Goryainov for Peisert graphs.
1. INTRODUCTION
Throughout this paper, q will always denote a prime power and Fq the ﬁnite ﬁeld with q elements,
and we write F∗
q = Fq \ {0}.
Let d ≥2 be an integer, and let q ≡1 (mod d) be a sufﬁciently large prime power. It is well
known that the set of d-th powers (of nonzero elements) in Fq behaves like a random set [19].
There are different ways to make this statement precise. One typical way to do so is to consider
the following well-known lemma [13, Exercise 5.66], which follows from a standard application
of Weil’s bound on complete character sums.
Lemma 1.1. Let v1, . . . , vk be distinct elements of the ﬁnite ﬁeld Fq and let d | (q −1), where
d ≥2. Let M be the number of solutions x ∈Fq to the system of equations (x −vi)(q−1)/d = 1
(i = 1, . . . , k). Then |M −q/dk| ≤k√q.
In other words, the number of x ∈Fq such that x −vi is a d-th power for all i is asymptotically
equal to q/dk. Note that if we model the set of d-th powers as a random subset S of Fq with density
1/d, then the expected number of x ∈Fq such that each x −vi ∈S would also be q/dk; in this
sense, the set of d-th powers in Fq behaves like a random set. Lemma 1.1 and its generalizations
have plenty of applications in number theory, combinatorics, and ﬁnite geometry; we refer the
reader to an excellent survey by Sz˝onyi [17].
While Lemma 1.1 states that globally the solutions behave randomly, it is desirable to obtain
reﬁned information on the distribution of these solutions for various applications. In this paper, we
aim to understand the “local distribution” of these solutions within a given subﬁeld, or equivalently
the distribution of power residues in a shifted subﬁeld. More precisely, given a ﬁeld extension K/L
of ﬁnite ﬁelds with |L| ≡1 (mod d), we want to count the number of solutions of (x−vi)(|K|−1)/d =
1 in the base ﬁeld L, where v1, . . . , vk ∈K. Without loss of generality, assume that L = Fq and
K = Fqn. Our ﬁrst main result gives an asymptotic formula for the number of solutions.
2020 Mathematics Subject Classiﬁcation. 11T24, 11B30, 05C25.
Key words and phrases. character sum, subﬁeld, maximal clique, Paley graph, Peisert graph.
1

--- Page 2 ---

Theorem 1.2. Let d ≥2 and q ≡1 (mod d). For 1 ≤i ≤k, let vi ∈Fqn be of degree di
over Fq, and let M be the number of solutions x in the base ﬁeld Fq to the system of k equations
(x −vi)(qn−1)/d = 1. Suppose that vi and vj are not Galois conjugates with respect to the ﬁeld
extension Fqn/Fq whenever i ̸= j. Then
M −q
k
Y
i=1
gcd(ddi, n)
ddi
 ≤

k
X
i=1
di −1
√q.
We remark that the assumption that no two vi are Galois conjugates is necessary. Indeed, if vi
and vj are Galois conjugates, then for x ∈Fq, it is easy to verify that (x −vi)(qn−1)/d = 1 if and
only if (x −vj)(qn−1)/d = 1.
Theorem 1.2 recovers a few known results in the literature. In particular, if n = 1, then di = 1
for all i and Theorem 1.2 recovers Lemma 1.1. Also, in the special case d = 2, k = 1, n even,
and v1 /∈Fqn/2, Theorem 1.2 shows that the number of solutions is q/2 + O(n√q), which recovers
a result of Hirschfeld and Sz˝onyi [12]; moreover, they showed this special case already has some
nice applications in ﬁnite geometry.
We also prove the following theorem, which complements Theorem 1.2 when n = 2 and q ̸≡
1 (mod d).
Theorem 1.3. Let d ≥2 and let q2 ≡1 (mod d). Choose v1, v2, . . . , vk ∈Fq2 \ Fq, no two of
which are Galois conjugates. Let M be the number of solutions x in Fq to the system of equations
(x −vi)(q2−1)/d = 1 for 1 ≤i ≤k. Then
M −q
dk
 ≤(2k −1)√q.
Note that if q ≡−1 (mod d), then we always have (x−v)(q2−1)/d = 1 when v, x ∈Fq and x ̸= v.
Also note that the condition that no two vi are Galois conjugates is necessary, for the same rea-
son as in Theorem 1.2. We remark that some related results have appeared in [20, Corollaries 2.4
and 2.5]. However, the statements of those two corollaries omitted some necessary hypotheses1. In
Section 3, we shall state and prove a corrected version for the sake of completeness. In particular,
we will prove Theorem 3.2 and then deduce Theorem 1.3 as a consequence. One can use Theo-
rem 3.2 to prove a more general result on the distribution of power residues over shifted subﬁelds.
Before discussing the applications of Theorem 1.2 and Theorem 1.3, we introduce some nec-
essary terminology. Generalized Paley graphs are well-studied Cayley graphs, ﬁrst introduced by
Cohen [5] in 1988 and reintroduced by several groups of authors since then. Let d ≥2 be an integer
and q a prime power such that q ≡1 (mod 2d). The d-Paley graph on Fq, denoted GP(q, d), is the
graph with vertex set Fq such that two vertices are adjacent if their difference is a d-th power in F∗
q.
Note that the condition q ≡1 (mod 2d) guarantees the graph is undirected and non-degenerate; see
for example [5, Section 4]. The well-known Paley graphs are simply 2-Paley graphs. We refer to
[2, 8, 9, 10, 21, 23] for extensive discussions on different constructions of maximal cliques in gen-
eralized Paley graphs; we also refer to [16, Proposition 2] for a nice connection between maximal
cliques in Paley graphs and minimal blocking sets.
Recall that a clique C in a graph G is a subset of vertices of G such that every two distinct
vertices in C are adjacent. A maximal clique is a clique that cannot be extended by adding a new
1Private communication with Daqing Wan. For example, [20, Corollary 2.4] does not apply to the case m = 2, n =
1 and f1(T ) = (T −a)(T −aq) for a ∈Fq2 \ Fq.
2

--- Page 3 ---

vertex. Every maximum clique (a clique of highest cardinality) is a maximal clique, but there can be
smaller maximal cliques as well. As an application of Theorem 1.2, we construct new families of
maximal cliques in generalized Paley graphs of the form GP(qd, d), where q is an odd prime power
such that q ≡1 (mod d). It is known that if q > (d −1)2, then the subﬁeld Fq forms a maximal
clique in such a graph [23, Theorem 1.2]. Our next result constructs many new maximal cliques
with smaller sizes. To state the theorem, recall that for a positive integer m, its radical rad(m) is
deﬁned to be the product of the distinct prime divisors of m. In particular, rad(m) | rad(d) if and
only if every prime dividing m also divides d. We let logr denote the base-r logarithm.
Theorem 1.4. Let d ≥2 and let r be the smallest prime divisor of d. Let m be a positive integer
such that rad(m) | rad(d). If q ≡1 (mod d) is an odd prime power such that
q > (8 logr m + 4)d2m2,
then there is a maximal clique C in GP(qd, d) with size |C| = q
m +O(d log m√q). More precisely,
q
m −d logr m · √q ≤|C| ≤q
m + d logr m · (√q + 1).
In particular, if d ≥2 is ﬁxed and m is a positive integer such that rad(m) | rad(d), then
there is a maximal clique of size approximately q/m in GP(qd, d), provided that q ≡1 (mod d)
is sufﬁciently large. (We believe that these are the only possible approximate sizes of maximal
cliques; see Conjecture 6.4 for a more precise statement.) When d = 2 and m is a power of 2,
this recovers a result of Hirschfeld and Sz˝onyi on maximal cliques in Paley graphs of square order,
which they did not state explicitly but is implicit in their constructions of minimal blocking sets
[11, 16]. It would be interesting to see if Theorem 1.4 has some applications in ﬁnite geometry.
For our second application, we focus on generalized Paley graphs of the form GP(q2, d), where q
is an odd prime power such that d | (q+1). Such generalized Paley graphs are of particular interest
since the subﬁeld Fq forms a maximum clique, and it is known that the only maximum clique
containing 0 and 1 is the subﬁeld Fq; see Blokhuis [3] for Paley graphs (that is, when d = 2) and
Sziklai [18] for general d. This characterization of maximum cliques is also known as the Erd˝os–
Ko–Rado (EKR) theorem for the graph GP(q2, d), in the sense that all maximum cliques are given
by afﬁne translates of the subﬁeld Fq; see related discussions in [1, 24] and [7, Section 5.9].
Baker, Ebert, Hemmeter, and Woldar [2] constructed maximal cliques that are not maximum
in the Paley graph GP(q2, 2) as the following. Pick an element α ∈Fq2 \ Fq, and consider the
clique C obtained by α and its Fq-neighborhood, that is,
C = {α} ∪{x ∈Fq : α −x ∈(F∗
q2)2}.
They showed that C is a maximal clique of size q+1
2
if q ≡1 (mod 4), and C ∪{αq} is a maximal
clique of size q+3
2
if q ≡3 (mod 4). Their construction is also known as the (Fq, α)-construction
[8, 9]. Analogously, Goryainov, Shalaginov, and Yip [10] considered a similar construction of
cliques in GP(q2, d), where d | (q + 1) and d ≥3. Let u ∈Fq2 \ Fq and let N(u) be the Fq-
neighborhood of u in GP(q2, d). Let Cu = N(u) ∪{u} if d ∤q+1
2 , and Cu = N(u) ∪{u, uq}
if d | q+1
2 , which they described [10, Proposition 4.6] as a clique from the (Fq, α)-construction.
They conjectured that such a clique Cu is maximal if 3 ≤d ≤q+1
3
and p ∤(d −1), where p is the
characteristic of the ﬁeld Fq [10, Conjecture 4.7]; see [10, Corollary 3.4] and [10, Example 5.9]
for the necessity of these two additional assumptions. Some partial progress of the conjecture can
be found in [10, Section 5]. In particular, they proved the conjecture when gcd(q −1, q+1
d −2) ∈
3

--- Page 4 ---

{1, 2} [10, Corollary 5.4]. We are able to conﬁrm their conjecture when q is sufﬁciently large
compared to d.
Theorem 1.5. Let d ≥3. If q ≡−1 (mod d) is an odd prime power such that q > 10d4/(d −1)2,
then in GP(q2, d), cliques obtained from the (Fq, α)-construction are maximal. More precisely, if
u ∈Fq2 \ Fq and N(u) is the Fq-neighborhood of u in GP(q2, d), then the following statements
hold:
(a) If d ∤q+1
2 , then N(u) ∪{u} forms a maximal clique of size q+1
d in GP(q2, d).
(b) If d | q+1
2 , then N(u) ∪{u, uq} forms a maximal clique of size q+d+1
d
in GP(q2, d).
Our techniques extend to a larger family of Cayley graphs, and in particular to Peisert graphs.
Let p ≡3 (mod 4) be a prime and q = pr with r even. The Peisert graph of order q = pr,
denoted P ∗
q , is deﬁned to be the graph with vertex set Fq such that two vertices are adjacent if their
difference belongs to the set S = {gj : j ≡0, 1 (mod 4)}, where g is a primitive root of the ﬁeld Fq.
Note the structure of the graph does not depend on the choice of the primitive root. Peisert [14]
showed that the only self-complementary symmetric graphs are Paley graphs, Peisert graphs, and
an exceptional graph of order 529. Asgarli and Yip [1, Theorem 1.4] showed an analgoue of the
EKR theorem for the Peisert graph P ∗
q2 with q ≡3 (mod 4); more precisely, the only maximum
clique containing 0, 1 in P ∗
q2 is the subﬁeld Fq if q = pn and p > 8.2n2, where p is the characteristic
of Fq. Sergey Goryainov conjectured2 that (Fq, α)-constructions also give maximal cliques in P ∗
q2
with q ≡3 (mod 4) and q ≥7, based on the similarity between Paley graphs and Peisert graphs.
We conﬁrm his conjecture using a similar method.
Theorem 1.6. Let q ≡3 (mod 4) be a prime power such that q ≥7. Let u ∈Fq2 \ Fq and let N(u)
be the Fq-neighborhood of u in P ∗
q2. Then N(u) ∪{u} forms a maximal clique of size q+1
2
in P ∗
q2.
The paper is organized as follows. In Section 2, we prove Theorem 1.2. In Section 3, we
establish some estimates on character sums over subﬁelds and prove Theorem 1.3. In Section 4, we
construct new maximal cliques in generalized Paley graphs and prove Theorem 1.4. In Section 5,
we study the maximality of cliques obtained from the (Fq, α)-construction and prove Theorem 1.5
as well as Theorem 1.6. We end the paper with some remarks and open questions in Section 6.
2. PROOF OF THEOREM 1.2
Consider the norm map NFqn/Fq : Fqn →Fq of the ﬁeld extension Fqn/Fq; explicitly,
NFqn/Fq(x) =
n−1
Y
j=0
xqj = x
qn−1
q−1 .
The next lemma provides a criterion to determine whether an element x in Fqn is a d-th power
based on its norm NFqn/Fq(x). To discuss d-th powers in the base ﬁeld Fq, we need to further
assume d | (q −1).
Lemma 2.1. Assume d | (q −1). Let x ∈Fqn. Then x is a d-th power in Fqn if and only if
NFqn/Fq(x) is a d-th power in Fq.
2Private communication
4

--- Page 5 ---

Proof. The case x = 0 is trivial. Next, assume x ̸= 0. Let g be a primitive root of Fqd. Let x = gk.
Then x is a d-th power in Fqn if and only if d | k. Note that NFqn/Fq(g) = g
qn−1
q−1 is a primitive root
of Fq. Thus, NFqn/Fq(x) = (g
qn−1
q−1 )k is a d-th power in Fq if and only if d | k, as claimed.
□
To prove Theorem 1.2, we also need the celebrated Weil bound; see for example [13, Theo-
rem 5.41].
Lemma 2.2 (Weil’s bound). Let χ be a multiplicative character of Fq of order d > 1, and let
f ∈Fq[z] be a monic polynomial of positive degree that is not a d-th power of a polynomial. Let m
be the number of distinct roots of f in its splitting ﬁeld over Fq. Then for any a ∈Fq,

X
z∈Fq
χ
 af(z)
 ≤(m −1)√q .
Now we are ready to present the proof of Theorem 1.2.
Proof of Theorem 1.2. Let gi(z) be the minimal polynomial of vi over Fq; then gi(z) has degree di
and
gi(z) =
di−1
Y
j=0
(z −vqj
i ).
Let fi = gn/di
i
. Then fi is of degree n, and each root of fi is a Galois conjugate of vi with
multiplicity n/di.
Note that for each z ∈Fq, since vqdi
i
= vi, we have
fi(z) =
di−1
Y
j=0
(z −vqj
i )n/di =
n−1
Y
j=0
(z −vqj
i ) =
n−1
Y
j=0
(z −vi)qj = NFqn/Fq(z −vi).
Let χ be a multiplicative character of Fq, with order d. If x ∈Fq, then (x −vi)(qn−1)/d = 1 for
each i if and only if x −vi is a d-th power in Fqn for each i, if and only if fi(x) = NFqn/Fq(x −vi)
is a d-th power in Fq for each i (by Lemma 2.1), if and only if χ(fi(x)) = 1 for each i.
By the orthogonality relations, 1
d
Pd−1
j=0 χj is the indicator function of d-th powers in F∗
q. There-
fore, by the above discussion, the number of solutions to the given system of equations is
M =
X
x∈Fq
k
Y
i=1
1
d
d−1
X
j=0
χj(fi(x))

= 1
dk
X
0≤j1,j2,...,jk≤d−1
X
x∈Fq
χ

k
Y
i=1
f ji
i (x)

.
(1)
Since vi and vj are not Galois conjugates whenever i ̸= j, it follows that f1, f2, . . . , fk are
pairwise coprime. It follows that Qk
i=1 f ji
i (z) is a d-th power of a polynomial if and only if d |
ji · n/di for each i, or equivalently,
ddi
gcd(ddi, n) | ji.
Thus, the number of k-tuples (j1, j2, . . . , jk) such that 0 ≤ji ≤d −1 and Qk
i=1 f ji
i (z) is a d-th
power of a polynomial is
k
Y
i=1
d gcd(ddi, n)
ddi
=
k
Y
i=1
gcd(ddi, n)
di
,
5

--- Page 6 ---

and the contribution of these k-tuples (corresponding to trivial character sums) to the sum (1) is
q
dk ·
k
Y
i=1
gcd(ddi, n)
di
= q ·
k
Y
i=1
gcd(ddi, n)
ddi
.
When Qk
i=1 f ji
i (z) is not a d-th power of a polynomial, the number of distinct roots of the polyno-
mial Qk
i=1 fi(z) in its splitting ﬁeld is at most Pk
i=1 di, and thus Weil’s bound (Lemma 2.2) implies
that

X
x∈Fq
χ

k
Y
i=1
f ji
i (x)
 ≤

k
X
i=1
di −1
√q.
We conclude that
M −q ·
k
Y
i=1
gcd(ddi, n)
ddi
 ≤1
dk · dk ·

k
X
i=1
di −1
√q =

k
X
i=1
di −1
√q
as required.
□
3. PROOF OF THEOREM 1.3
Similar to the discussions in the previous section, the proof of Theorem 1.3 will be based on
character sums. Clearly, we need to estimate character sums of the form P
x∈Fq χ(f(x)), where χ
is a multiplicative character of Fq2. The key idea is to convert the desired character sum over ﬁnite
ﬁelds to an equivalent character sum over function ﬁelds.
Let Fq[T] be the polynomial ring in variable T over Fq. Let f ∈Fq[T] be a non-constant
polynomial. A Dirichlet character modulo f, usually denoted by χf, is a character on the multi-
plicative group (Fq[T]/fFq[T])∗, which can be extended to a function on Fq[T] by setting χf(g) =
χf(g mod f) if f and g are coprime, and χf(g) = 0 otherwise. We refer to [15, Section 4] for
more background.
We need the following Weil bound on character sums over monic linear polynomials; see for
example [20, Theorem 2.1].
Lemma 3.1. Let f ∈Fq[T] be a polynomial with degree n ≥1, and let χf be a non-trivial
Dirichlet character modulo f. Then

X
a∈Fq
χf(T −a)
 ≤(n −1)√q.
From this lemma, we can deduce the following theorem.
Theorem 3.2. Let f1, f2, . . . , fk be monic irreducible polynomials in Fqn[T], no two of which are
Galois conjugates over Fq. Let χ1, χ2, . . . , χk be multiplicative character of Fqn. Assume that
there exists 1 ≤i ≤k such that fi has a root ξi such that χi is not identically 1 on the set
NFqn[ξi]/Fqn(Fq[ξi]) \ {0}. Let bi be the degree of fi(T) and ci be the number of conjugates of fi(T)
over Fq. Then

X
a∈Fq
k
Y
i=1
χi
 fi(a)
 ≤

k
X
i=1
bici −1
√q .
6

--- Page 7 ---

In particular, if m = Pk
i=1 bi is the sum of the degree of the fi, then

X
a∈Fq
k
Y
i=1
χi
 fi(a)
 ≤(mn −1)√q .
Proof. For each 1 ≤i ≤k, let ξi be a root of fi. Since fi is a monic irreducible polynomial in
Fqn[T], it follows that fi is the minimal polynomial of ξi over Fqn and thus
fi(a) = NFqn[ξi]/Fqn(a −ξi)
(2)
for a ∈Fq. For each 1 ≤i ≤k, let Fi be the product of conjugates of fi(T) over Fq. Then,
F1, F2, . . . , Fk are deﬁned and irreducible over Fq. Since no two of f1, f2, . . . , fk are Galois conju-
gates over Fq, it follows that F1, F2, . . . , Fk are coprime. Let F = Qk
i=1 Fi. Since deg(Fi) = bici,
it follows that deg(F) = Pk
i=1 bici.
For g ∈Fq[T], deﬁne
χFi(g) = χi(NFqn[ξi]/Fqn(g(ξi))).
(3)
Note that χFi is a Dirichlet character modulo Fi. Note also that, as g runs over Fq[T], g(ξi) runs
over Fq[ξi], and thus the norm NFqn[ξi]/Fqn(g(ξi)) runs over the set NFqn[ξi]/Fqn(Fq[ξi]). Thus, if
χi is not identically 1 on the set NFqn[ξi]/Fqn(Fq[ξi]) \ {0}, then χFi is non-trivial by deﬁnition.
Therefore, by the given assumption, at least one of the characters χF1, χF2, . . . , χFk is non-trivial.
Since F1, F2, . . . , Fk are irreducible coprime polynomials, by the Chinese remainder theorem, the
product χF := Qk
i=1 χFi is a non-trivial Dirichlet character modulo F. Therefore, by Lemma 3.1
and equations (2) and (3),

X
a∈Fq
k
Y
i=1
χi
 fi(a)
 =

X
a∈Fq
k
Y
i=1
χFi(a −T)
 =

X
a∈Fq
χF(a −T)
 ≤

k
X
i=1
bici −1
√q,
as required. Since ci ≤n, we always have Pk
i=1 bici ≤n Pk
i=1 bi = mn.
□
Remark 3.3. From the above proof, we can infer that the assumption that “there exists 1 ≤i ≤k
such that fi has a root ξi such that χi is not identically 1 on the set NFqn[ξi]/Fqn(Fq[ξi]) \ {0}” in
Theorem 3.2 is equivalent to the character sum being non-trivial. In particular, if this condition
does not hold, then the character sum in Theorem 3.2 is q.
Next, we use Theorem 3.2 to deduce Theorem 1.3.
Proof of Theorem 1.3. For each 1 ≤i ≤k, let fi(T) = T −vi ∈Fq2[T]. By the assumption,
no two of f1, . . . , fk are Galois conjugates of each other. Note that for each 1 ≤i ≤k, we have
NFq2[vi]/Fq2(Fq[vi]) = NFq2/Fq2(Fq2) = Fq2 since vi ∈Fq2 \ Fq.
Let χ be a multiplicative character in Fq2, with order d. Similar to the proof of Theorem 1.2, the
number of solutions to the given system of equations is
M = 1
dk
X
0≤j1,j2,...,jk≤d−1
X
x∈Fq
χ

k
Y
i=1
f ji
i (x)

.
(4)
7

--- Page 8 ---

When j1 = j2 = · · · = jk = 0, the character sum contributes to
q
dk to M. In all other cases, at least
one of χj1, χj2, . . . , χjk is a nontrivial character since χ has order d, and Theorem 3.2 implies that

X
x∈Fq
χ

k
Y
i=1
f ji
i (x)
 =

X
x∈Fq
k
Y
i=1
χji(fi(x))
 ≤(2k −1)√q.
Therefore, summing over k-tuples (j1, j2, . . . , jk) in equation (4), we conclude that
M −q
dk
 ≤(2k −1)√q,
as required.
□
Remark 3.4. Our proof of Theorem 1.3 in this section employed character sums over ﬁnite ﬁelds.
One can give another proof of Theorem 1.2 using Theorem 3.2 and Remark 3.3, which employ
character sums over function ﬁelds. To see that, we again set fi(T) = T −vi ∈Fqn[T] for each
1 ≤i ≤k, and equation (4) still applies. Since vi has degree di over Fq, the number of conjugates
of fi over Fq also is di. Note that we have NFqn[vi]/Fqn(Fq[vi]) \ {0} = F∗
qdi, and thus the main term
q Qk
i=1
gcd(ddi,n)
ddi
in Theorem 1.2 follows from Remark 3.3, and the error term (Pk
i=1 di −1)√q in
Theorem 1.2 comes from Theorem 3.2. While the exact machinery of the two proofs are different,
there are deﬁnite similarities and the two proofs are probably essentially equivalent.
Next, we state and prove a corrected version of [20, Corollary 2.4]. Any monic polynomial
f ∈Fqn[T] with positive degree can be factorized as the product of monic irreducible polynomials
in Fqn[T]:
f =
sY
i=1
f ti
i ,
where the fi are distinct irreducible polynomials. Let ξ be a root of f1. By relabelling, we may
assume f1, f2, . . . , fr are the conjugates of f1 over Fq. Let σ: x 7→xq be the Frobenius map
deﬁned on Fqn; note that σ naturally induces a map on Fqn[T]. Then for each 1 ≤i ≤r, we can
write fi = σαi(f1) for some 0 ≤αi ≤n −1. We deﬁne the total multiplicity of ξ to be
m =
r
X
i=1
tiqαi,
which is the sum of weighted multiplicities among conjugates of ξ. Observe that if χ is a character
over Fqn, then we have
X
a∈Fq
χ(f(a)) =
X
a∈Fq
s
Y
i=1
χti(fi(a)).
Note that for 1 ≤i ≤r, and each a ∈Fq, we have fi(a) = (σαi(f1))(a) = (f1(a))qαi. Thus, for
a ∈Fq, we have
rY
i=1
χti(fi(a)) =
rY
i=1
χtiqαi(f1(a)) = χm(f1(a)).
Using this observation, Theorem 3.2 implies the following corollary immediately.
8

--- Page 9 ---

Corollary 3.5. Let f1, f2, . . . , fk be monic polynomials in Fqn[T], no two of which share roots that
are Galois conjugates over Fq. Let m be the degree of the largest squarefree divisor of Qk
i=1 fi. Let
χ1, χ2, . . . , χk be multiplicative characters of Fqn. Assume that there exists 1 ≤i ≤k such that fi
has a root ξi of total multiplicity mi such that χmi
i
is not identically 1 on the set NFqn[ξi]/Fqn(Fq[ξi])\
{0}. Then

X
a∈Fq
k
Y
i=1
χi
 fi(a)
 ≤(mn −1)√q.
4. NEW CONSTRUCTIONS OF MAXIMAL CLIQUES IN GENERALIZED PALEY GRAPHS
To construct maximal cliques in GP(qd, d), we are led to consider the local behavior of the
graph GP(qd, d) in a subﬁeld, equivalently, the structure of the subgraph induced by a subﬁeld.
Lemma 4.1. Let d ≥2 and let q ≡1 (mod d) be an odd prime power. Let d′ be a divisor of d
that is greater than 1. Then the subgraph of GP(qd, d) induced by the subﬁeld Fqd′ is the same as
GP(qd′, d′).
Proof. Let g be a primitive root of Fqd. Then g(qd−1)/(qd′−1) is a primitive root of Fqd′; moreover,
since q ≡1 (mod d), it follows that
qd −1
qd′ −1 =
d/d′−1
X
j=0
qd′j ≡d
d′ (mod d).
Thus, gcd(d, qd−1
qd′−1) =
d
d′. Let x ∈F∗
qd′. Then x is a d-th power in Fqd if and only if x is a d′-th
power in Fqd′. The conclusion follows.
□
As preparation for proving Theorem 1.4, in the next proposition, we establish the existence of
cliques of small size with prescribed degrees.
Proposition 4.2. Let d ≥2 and let q ≡1 (mod d) be an odd prime power. Let r be the smallest
prime divisor of d. Let d1, d2, . . . , dk be positive integers such that d1 > 1 and d1 | d2 | · · · | dk | d.
Assume that
qr > max{(d + (k −1)rk−1)2, e2(k−1)}.
Then there is a clique C = {v1, v2, . . . , vk} in GP(qd, d) such that vi has degree di over Fq for
each 1 ≤i ≤k, and no two vertices in C are Galois conjugates with respect to the ﬁeld extension
Fqd/Fq.
Proof. We build such a clique inductively. We ﬁrst pick an arbitrary v1 ∈Fqd1 such that v1 has
degree d1 over Fq.
Given 2 ≤j ≤k, suppose we have constructed a clique Cj−1 = {v1, v2, . . . , vj−1} in GP(qd, d)
such that vi has degree di over Fq for each 1 ≤i ≤j −1, and no two vertices in Cj−1 are Galois
conjugates with respect to the ﬁeld extension Fqd/Fq. We need to ﬁnd vj ∈Fqdj with degree dj, not
a Galois conjugate of any of v1, v2, . . . , vj−1, such that Cj−1 ∪{vj} forms a clique in GP(qd, d).
Note that v1, v2, . . . , vj−1, vj ∈Fqdj. Thus, by Lemma 4.1, Cj−1 ∪{vj} forms a clique in
GP(qd, d) if and only if Cj−1 ∪{vj} forms a clique in GP(qdj, dj), or equivalently, if and only
if (vj −vi)(qdj −1)/dj = 1 for each 1 ≤i ≤j −1. By Lemma 1.1, the number of such vj is at
9

--- Page 10 ---

least qdj/dj−1
j
−(j −1)
p
qdj. On the other hand, note that the number of elements in Fqdj that are
Galois conjugates of one of v1, v2, . . . , vj−1 is at most (j −1)dj. Therefore, if
qdj
dj−1
j
> (j −1)
p
qdj + (j −1)dj
(5)
holds, then we can ﬁnd a desired vj and achieve our goal.
It remains to show that the given assumption qr > max{(d + (k −1)rk−1)2, e2(k−1)} implies the
inequality (5) for each 2 ≤j ≤k. Consider the function s(t) = t log q −2(k −1) log t, where
t ≥r is a real number. Since qr > e2(k−1), it follows that s′(t) = log q −2(k −1)/t > 0 when
t ≥r. Therefore, s(t) ≥s(r) when t ≥r, or equivalently √qt/tk−1 ≥√qr/rk−1 when t ≥r.
Therefore, given qr > (d + (k −1)rk−1)2 where r is the smallest prime divisor of d, we have for
each 2 ≤j ≤k that
qdj
dj−1
j
−(j −1)
p
qdj −(j −1)dj ≥qdj
dk−1
j
−(k −1)
p
qdj −(k −1)d
= (k −1)
p
qdj

p
qdj
(k −1)dk−1
j
−1

−(k −1)d
≥(k −1)√qr

√qr
(k −1)rk−1 −1

−(k −1)d
> (k −1)2rk−1

d
(k −1)rk−1

−(k −1)d = 0,
as required.
□
After one ﬁnal elementary lemma, we will be ready to prove Theorem 1.4.
Lemma 4.3. Let m, d ≥2 be positive integers with rad(m) | rad(d), and let r be the small-
est prime divisor of m. Then there exist positive integers k and d1, d2, . . . , dk ≥r such that
d1d2 · · · dk = m and d1 | d2 | · · · | dk | d.
Proof. If we let k be the largest exponent of any prime in the prime factorization of m, it is easy to
check that the integers di = Q
pk+1−i|m p have the asserted properties.
□
Proof of Theorem 1.4. Note that the assumption q ≡1 (mod d) guarantees that Fq forms a clique
in GP(qd, d). If m = 1, the subﬁeld Fq forms a maximal clique in GP(qd, d) [23, Theorem 1.2] as
mentioned in the introduction. Thus we may assume that m ≥2 in the following.
Since rad(m) | rad(d), Lemma 4.3 enables us to choose positive integers d1, d2, . . . , dk ≥r so
that m = d1d2 · · · dk and d1 | d2 | · · · | dk | d. Note that m ≥rk and thus k ≤logr m. It follows
that
q > (8 logr m + 4)d2m2 ≥(8k + 4)d2m2 ≥(8k + 4)d2r2k > max{d + (k −1)rk−1, ek−1}.
To see the last inequality, note that (8k + 4)d2r2k > d + (k −1)r2k > d + (k −1)rk−1 and
r2k ≥4k > ek−1. By Proposition 4.2, there exists a clique D = {v1, v2, . . . , vk} in GP(qd, d) such
that vi has degree di over Fq for each 1 ≤i ≤k, and no two vertices in D are Galois conjugates
with respect to the ﬁeld extension Fqd/Fq.
Recall that Fq is a clique. Observe that C = D ∪D′ also forms a clique in GP(qd, d), where
D′ = {x ∈Fq : vi −x is a d-th power in Fqd for all 1 ≤i ≤k}.
10

--- Page 11 ---

Since m = d1d2 · · · dk and Pk
i=1 di ≤kd, it follows from Theorem 1.2 that
q
m −kd√q ≤|D′| ≤q
m + kd√q.
(6)
By deﬁnition, C cannot be expanded to a larger clique by adding another vertex in Fq. Assume
that there exists v ∈Fqd \ Fq such that v is not a Galois conjugate of vi with respect to the ﬁeld
extension Fqd/Fq for any 1 ≤i ≤k, and yet C ∪{v} is still a clique. It would then follow that
D′ = D′ ∩{x ∈Fq : v −x is a d-th power in Fqd}.
Theorem 1.2 then implies that
|D′| ≤
q
mr + (k + 1)d√q.
(7)
Comparing inequality (7) with the lower bound on |D′| in inequality (6), we obtain
q
m −kd√q ≤q
mr + (k + 1)d√q,
which implies that
q ≤(2k + 1)d2m2
(1 −1
r)2
≤(8k + 4)d2m2 ≤(8 logr m + 4)d2m2,
violating the assumption that q > (8 logr m + 4)d2m2.
Let C′ be a maximal clique in GP(qd, d) such that C ⊂C′. Based on the above discussions,
each element in C′ \C is a Galois conjugate of vi for some 1 ≤i ≤k. It follows that |C| ≤|C′| ≤
|C| + k(d −1), and thus inequality (6) implies that
q
m −d logr m · √q ≤q
m −kd√q + k ≤|C′| ≤q
m + kd√q + kd ≤q
m + d logr m · (√q + 1),
as required.
□
5. MAXIMALITY OF THE (Fq, α)-CONSTRUCTION
In this section, we prove Theorem 1.5 and Theorem 1.6. We start by presenting the proof of
Theorem 1.5.
Proof of Theorem 1.5. Recall that for each vertex u ∈Fq2, N(u) is the Fq-neighborhood of u in
the d-Paley graph GP(q2, d), that is,
N(u) = {x ∈Fq : u −x is a d-th power in Fq2}.
By [10, Proposition 4.6], |N(u)| = q+1
d −1 if u ∈Fq2 \Fq. Since d | (q +1), the subﬁeld Fq forms
a clique. Since q > 10d4/(d −1)2 > 10d2, we have
9 + 6
√q + 1
q < 9 +
6
√
10d + 1
40 < 10.
It follows that
(3√q + 1)2 = 9q + 6√q + 1 < 10q < q2
1
d −1
d2
2
,
and thus
q
d2 + 3√q < q + 1
d
−1.
(8)
Let u ∈Fq2 \ Fq. Then u and uq are Galois conjugates. Note that N(u) = N(uq). Indeed, if
x ∈Fq, then uq−x = uq−xq = (u−x)q is a d-th power in Fq2 if and only if u−x is a d-th power in
11

--- Page 12 ---

Fq2. We also claim that that u and uq are adjacent if and only if d | q+1
2 . Let β ∈F∗
q be a non-square
in Fq, and let α ∈Fq2 such that α2 = β. Then {1, α} forms a basis of Fq2 over Fq, and thus we can
write u = x + yα for some x, y ∈Fq with y ̸= 0. Since uq = (x + yα)q = xq + yqαq = x −yα,
we have u −uq = 2yα being a d-th power in Fq2 if and only if α is a d-th power in Fq2, if and only
if d | q+1
2 . Thus, N(u) ∪{u, uq} is a clique when d | q+1
2 , and N(u) ∪{u, uq} is not a clique when
d ∤q+1
2 .
Let Cu = N(u)∪{u} when d ∤q+1
2 , and Cu = N(u)∪{u, uq} when d | q+1
2 . Suppose that Cu is
not a maximal clique. Then based on the above discussion, there is v ∈Fq2 \ Fq such that v ̸= uq,
and N(u) ∪{u, v} remains to be a clique. It follows that N(u) ∩N(v) = N(u). By Theorem 1.3
and inequality (8), we have
|N(u) ∩N(v)| ≤q
d2 + 3√q < q + 1
d
−1 = |N(u)|,
a contradiction. We conclude that the desired clique Cu is maximal.
□
Finally, we use a similar approach to show the maximality of cliques from (Fq, α)-constructions
in Peisert graphs.
Proof of Theorem 1.6. When 7 ≤q ≤79, we have used SageMath to verify the statement of the
theorem. In the following discussion, we assume that q ≥83.
Let g be a primitive root of Fq2 and let H be the subgroup of F∗
q2 of index 4. Let S = H ∪gH.
Note that two vertices are adjacent in the Peisert graph P ∗
q2 if and only if their difference is in S.
Also, note that the 4-Paley graph GP(q2, 4) is a subgraph of the Peisert graph P ∗
q2. Since 4 | (q+1),
the subﬁeld Fq forms a clique in GP(q2, 4), and thus in P ∗
q2. For each vertex u ∈Fq2, let N(u) be
the Fq-neighborhood of u in P ∗
q2, that is,
N(u) = {x ∈Fq : u−x ∈S} = {x ∈Fq : u−x ∈H}∪{x ∈Fq : u−x ∈gH} := N1(u)∪N2(u).
Note that N1(u) is exactly the Fq-neighborhood of u in GP(q2, 4), and thus |N1(u)| = q+1
4 −1 if
u /∈Fq. On the other hand, it is known that Peisert graph P ∗
q2 is a (q2, q2−1
2 , q2−5
4 , q2−1
4 )-strongly
regular graph with the smallest eigenvalue −1−q
2
[14]. Thus, the subﬁeld Fq forms a maximum
clique in P ∗
q2 and |N(u)| = q+1
2 −1 for each u ∈Fq2 \ Fq by the Hoffman bound [4, Proposition
1.3.2].
Let u ∈Fq2 \ Fq. For the sake of contradiction, assume that N(u) ∪{u} is not a maximal
clique. Then u and uq are Galois conjugates. We claim that N(u) ̸= N(uq). If x ∈Fq, then
uq −x = (u −x)q, thus u −x ∈H if and only if uq −x ∈H, and uq −x ∈g3H if and only
if u −x ∈gH. Thus, if N(u) = N(uq), then we must have N(u) = N1(u), which is impossible
since |N(u)| > |N1(u)|. Since N(u) ∪{u} is not maximal, there is v ∈Fq2 \ Fq such that v ̸= uq,
and N(u) ∩N(v) = N(u).
Next we estimate |N(u) ∩N(v)| using Theorem 3.2. As a preparation, we need to express the
indicator function on S using characters. Let χ be the multiplicative character of Fq2 with order 4
such that χ(g) = i. It follows that
 χ(x) + 1
 χ(x) + i
2 =
(
8,
if x ∈H ∪gH,
0,
if x ∈g2H ∪g3H.
12

--- Page 13 ---

On the other hand, for x ∈Fq2, we have
 χ(x) + 1
 χ(x) + i
2 =
 2 + χ(x) + χ(x)
 2 + iχ(x) −iχ(x)

= 4 + (2i + 2)χ(x) + (2 −2i)χ(x) + i(χ2(x) −χ2(x))
= 4 + (2i + 2)χ(x) + (2 −2i)χ(x).
Therefore, 1S : F∗
q2 →C, the indicator function of S, can be expressed as
4 · 1S = 2 + (i + 1)χ + (1 −i)χ.
It follows that
16|N(u) ∩N(v)|
=
X
a∈Fq
4 · 1S(u −a) · 4 · 1S(v −a)
=
X
a∈Fq
 2 + (1 + i)χ(u −a) + (1 −i)χ(u −a)
 2 + (1 + i)χ(v −a) + (1 −i)χ(v −a)

= 4q + 2(1 + i)
X
a∈Fq
χ(v −a) + 2(1 −i)
X
a∈Fq
χ(v −a)
+ 2(1 + i)
X
a∈Fq
χ(u −a) + 2i
X
a∈Fq
χ(u −a)χ(v −a) + 2
X
a∈Fq
χ(u −a)χ(v −a)
+ 2(1 −i)
X
a∈Fq
χ(u −a) + 2
X
a∈Fq
χ(u −a)χ(v −a) −2i
X
a∈Fq
χ(u −a)χ(v −a).
Since u, v ∈Fq2 \ Fq are not Galois conjugates, we may apply Theorem 3.2 to bound these eight
character sums: the four sums with one character value can be bounded by √q, while the four sums
with two character values can be bounded by 3√q. Since |2(1 ± i)| = 2
√
2, we obtain
16|N(u) ∩N(v)| ≤4q + 4(2
√
2 · √q) + 4(2 · 3√q) = 4q + (8
√
2 + 24)√q.
Since q ≥83, we conclude that
|N(u) ∩N(v)| ≤q
4 +
√
2 + 3
2
√q < q −1
2
= |N(u)|,
a contradiction. Hence, N(u) ∪{u} is a maximal clique.
□
6. REMARKS AND OPEN QUESTIONS
We conclude this paper with some remarks and open questions.
Remark 6.1. Peisert [14, Section 6] showed that the Paley graph Pq2 and the Peisert graph P ∗
q2 of
the same order are not isomorphic when q ≥7 by showing that Aut(Pq2) ̸= Aut(P ∗
q2). While the
fact that these two graphs are not isomorphic seems obvious (at least when q is sufﬁciently large),
to the best knowledge of the authors, there is no known simple proof. Peisert’s original proof relies
on heavy machinery from group theory.
Here we sketch a new proof that Pq2 and P ∗
q2 are not isomorphic when q ≡3 (mod 4) and
q ≥7, using the structure of maximal cliques from (Fq, α)-constructions. Suppose otherwise that
these two graphs are isomorphic. Then there is a graph isomorphism φ: P ∗
q2 →Pq2 that maps the
13

--- Page 14 ---

subﬁeld Fq to Fq. Indeed, any graph isomorphism must map Fq, a maximum clique in P ∗
q2, to some
maximum clique in Pq2; while any maximum clique in Pq2 can be mapped to a maximum clique
containing 0 and 1 via an automorphism of Pq2. But it is known [3] that the only maximum clique
in Pq2 that contains 0 and 1 is Fq itself.
Choose any α∗∈Fq2 \ Fq, and let C∗be the clique in P ∗
q2 containing α∗and its neighbors in Fq.
Note that C∗is maximal in P ∗
q2 by Theorem 1.6. Similarly, set α = φ(α∗) and let C be the clique
in Pq2 containing α and its neighbors in Fq. However, C = φ(C∗) is not maximal in Pq2 since
C ∪{αq} is a maximal clique (as mentioned in the introduction), which contradicts the existence
of the graph isomorphism φ.
Remark 6.2. By combining the ideas in the proofs of Theorems 1.4 and Theorem 1.5, we can
show the following: if d ≥2 is ﬁxed and k is a non-negative integer, then there is a maximal clique
of size approximately q/dk in GP(q2, d), provided that q ≡−1 (mod d) is sufﬁciently large. We
can also prove the following by modifying the proof of Theorem 1.6: if k is a non-negative integer,
then there is a maximal clique of size approximately q/2k in P ∗
q2, provided that q ≡3 (mod 4) is
sufﬁciently large.
Remark 6.3. Theorem 1.4 says that (for suitable values of d, q, and m) there are maximal cliques
in GP(qd, d) that are approximately
1
m as large as the clique Fq itself, which is believed to be a
maximum clique (essentially the only one, see [22] for a related discussion). These cliques have
a speciﬁc structure, where we choose a small number of points outside of Fq and then add their
common neighbors within Fq. We believe that this construction yields all large maximal cliques in
GP(qd, d) up to automorphisms of the graph and certain induced subgraphs, and we formulate a
conjecture intended to serve as a sort of converse to Theorem 1.4.
Conjecture 6.4. Fix an integer d ≥2. Consider all sequences {rq/q}, indexed by odd prime
powers q ≡1 (mod d), such that rq is the cardinality of some maximal clique in the d-Paley graph
GP(qd, d). Then the set of limit points of all such sequences equals {0} ∪{ 1
m : rad(m) | rad(d)}.
Theorem 1.4 implies that every element of {0} ∪{ 1
m : rad(m) | rad(d)} is such a limit point; we
conjecture that there are no others.
As an example, consider all sequences {rq/q} indexed by odd prime powers q such that rq is
the cardinality of some maximal clique in the Paley graph GP(q2, 2). Theorem 1.4 implies that
every element of the set L2 = {0} ∪{1, 1
2, 1
4, 1
8, . . . } is a limit point of some such sequence, and
we conjecture that every limit point of any such sequence is in L2.
Baker, Ebert, Hemmeter, and Woldar [2] (see also [8, 9]) conjectured that the (Fq, α)-construct-
ion gives a second largest maximal clique in the Paley graph GP(q2, 2); equivalently, there is no
maximal clique of size between q+δq
2
+ 1 and q −1, where δq = 1 if q ≡1 (mod 4) and δq = 3 if
q ≡3 (mod 4). To the best of our knowledge, no progress has been made towards their conjecture.
A consequence of their conjecture would be that there are no limit points of any sequence {rq/q}
in the interval ( 1
2, 1). Our conjecture can thus be viewed as a further extension of their conjecture.
It is likely that new insights towards this conjecture would also shed light on estimating the clique
number of Paley graphs of non-square order, a major open problem in additive combinatorics and
analytic number theory [6]. We refer to [22] and the references therein for recent progress towards
the latter problem.
We similarly conjecture the analogous converses of the two statements in Remark 6.2: the anal-
ogous set of limit points for GP(q2, d) should be exactly Ld = {0} ∪{1, 1
d, 1
d2, . . . }, while the
analogous set of limit points for P ∗
q2 should be exactly L2.
14

--- Page 15 ---

ACKNOWLEDGMENTS
The authors thank the anonymous referees for their valuable comments and suggestions. The
authors thank Daqing Wan for the clariﬁcation of a result in [20] and Sergey Goryainov for shar-
ing the conjecture related to Peisert graphs. The authors also thank Shamil Asgarli for helpful
comments on a preliminary version of the manuscript. The ﬁrst author was supported in part by a
Natural Sciences and Engineering Council of Canada Discovery Grant. The research of the second
author was supported in part by an NSERC fellowship.
REFERENCES
[1] S. Asgarli and C. H. Yip. Van Lint–MacWilliams’ conjecture and maximum cliques in Cayley graphs over ﬁnite
ﬁelds. J. Combin. Theory Ser. A, 192:Paper No. 105667, 23, 2022.
[2] R. D. Baker, G. L. Ebert, J. Hemmeter, and A. Woldar. Maximal cliques in the Paley graph of square order. J.
Statist. Plann. Inference, 56(1):33–38, 1996.
[3] A. Blokhuis. On subsets of GF(q2) with square differences. Nederl. Akad. Wetensch. Indag. Math., 46(4):369–
372, 1984.
[4] A. E. Brouwer, A. M. Cohen, and A. Neumaier. Distance-regular graphs, volume 18 of Ergebnisse der Mathe-
matik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1989.
[5] S. D. Cohen. Clique numbers of Paley graphs. Quaestiones Math., 11(2):225–231, 1988.
[6] E. S. Croot, III and V. F. Lev. Open problems in additive combinatorics. In Additive combinatorics, volume 43
of CRM Proc. Lecture Notes, pages 207–233. Amer. Math. Soc., Providence, RI, 2007.
[7] C. Godsil and K. Meagher. Erd˝os-Ko-Rado theorems: algebraic approaches, volume 149 of Cambridge Studies
in Advanced Mathematics. Cambridge University Press, Cambridge, 2016.
[8] S. Goryainov, V. V. Kabanov, L. Shalaginov, and A. Valyuzhenich. On eigenfunctions and maximal cliques of
Paley graphs of square order. Finite Fields Appl., 52:361–369, 2018.
[9] S. Goryainov, A. Masley, and L. Shalaginov. On a correspondence between maximal cliques in Paley graphs of
square order. Discrete Math., 345(6):Paper No. 112853, 10, 2022.
[10] S. Goryainov, L. Shalaginov, and C. H. Yip. On eigenfunctions and maximal cliques of generalised Paley graphs
of square order. Finite Fields Appl., 87:Paper No. 102150, 2023.
[11] J. W. P. Hirschfeld and T. Sz˝onyi. Constructions of large arcs and blocking sets in ﬁnite planes. European J.
Combin., 12(6):499–511, 1991.
[12] J. W. P. Hirschfeld and T. Sz˝onyi. A problem on squares in a ﬁnite ﬁeld and its application to geometry. In
Advances in ﬁnite geometries and designs (Chelwood Gate, 1990), Oxford Sci. Publ., pages 169–176. Oxford
Univ. Press, New York, 1991.
[13] R. Lidl and H. Niederreiter. Finite ﬁelds, volume 20 of Encyclopedia of Mathematics and its Applications. Cam-
bridge University Press, Cambridge, second edition, 1997.
[14] W. Peisert. All self-complementary symmetric graphs. J. Algebra, 240(1):209–229, 2001.
[15] M. Rosen. Number theory in function ﬁelds, volume 210 of Graduate Texts in Mathematics. Springer-Verlag,
New York, 2002.
[16] T. Sz˝onyi. Note on the existence of large minimal blocking sets in Galois planes. Combinatorica, 12(2):227–235,
1992.
[17] T. Sz˝onyi. Some applications of algebraic curves in ﬁnite geometry and combinatorics. In Surveys in combina-
torics, 1997 (London), volume 241 of London Math. Soc. Lecture Note Ser., pages 197–236. Cambridge Univ.
Press, Cambridge, 1997.
[18] P. Sziklai. On subsets of GF(q2) with dth power differences. Discrete Math., 208/209:547–555, 1999.
[19] P. Sziklai. A lemma on the randomness of d-th powers in GF(q), d | q −1. Bull. Belg. Math. Soc. Simon Stevin,
8(1):95–98, 2001.
[20] D. Wan. Generators and irreducible polynomials over ﬁnite ﬁelds. Math. Comp., 66(219):1195–1212, 1997.
[21] C. H. Yip. On maximal cliques of Cayley graphs over ﬁelds. J. Algebraic Combin., 56(2):323–333, 2022.
[22] C. H. Yip. Exact values and improved bounds on the clique number of cyclotomic graphs, 2023.
arXiv:2304.13213.
15

--- Page 16 ---

[23] C. H. Yip. Maximality of subﬁelds as cliques in Cayley graphs over ﬁnite ﬁelds. Algebr. Comb., 6(4):901–905,
2023.
[24] C. H. Yip. Erd˝os–Ko–Rado theorem in Peisert-type graphs. Canad. Math. Bull., 67(1):176–187, 2024.
DEPARTMENT OF MATHEMATICS, UNIVERSITY OF BRITISH COLUMBIA, VANCOUVER V6T 1Z2, CANADA
Email address: gerg@math.ubc.ca
SCHOOL OF MATHEMATICS, GEORGIA INSTITUTE OF TECHNOLOGY, GA 30332, UNITED STATES
Email address: cyip30@gatech.edu
16

```
