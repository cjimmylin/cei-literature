---
title: "Design Patterns for the Common Good - PDF Extract"
source_pdf: "2025-Conwill-Design Patterns for the Common Good.pdf"
pages: 27
extracted_at: "2026-01-24T16:38:24.857691"
---

# PDF Extract: Design Patterns for the Common Good

**Source PDF:** 2025-Conwill-Design Patterns for the Common Good.pdf
**Total Pages:** 27

---

## Content

```
--- Page 1 ---

Obstructions and dualities for matroid depth
parameters
Jakub Gajarský∗
Kristýna Pekárková†
Michał Pilipczuk‡
Abstract
Contraction∗-depth is considered to be one of the analogues of graph tree-depth in
the matroid setting. In this paper, we investigate structural properties of contraction∗-
depth of matroids representable over finite fields and rationals. In particular, we prove
that the obstructions for contraction∗-depth for these classes of matroids are bounded
in size. From this we derive analogous results for related notions of contraction-depth
and deletion-depth. Moreover, we define a dual notion to contraction∗-depth, named
deletion∗-depth, for F-representable matroids, and by duality extend our results from
contraction∗-depth to this notion.
1
Introduction
A recent line of research in structural matroid theory focuses on various matroid depth
parameters and their applications. These parameters typically capture whether a matroid
M can be suitably encoded in a tree of bounded depth. Probably the most prominent
examples are branch-depth, introduced by DeVos, Kwon and Oum [6], and contraction∗-
depth1, introduced by Kardoš, Kráľ, Liebenau and Mach [13].
∗Institute of Informatics, University of Warsaw, Poland. Email: gajarsky@mimuw.edu.pl.
†Faculty of Informatics, Masaryk University, Botanická 68A, 602 00 Brno, Czech Republic. Email:
kristyna.pekarkova@mail.muni.cz.
‡Institute of Informatics, University of Warsaw, Poland. Email: michal.pilipczuk@mimuw.edu.pl.
MP was supported by the project BOBR that have received fund-
ing from the European Research Council (ERC) under the Eu-
ropean Union’s Horizon 2020 research and innovation programme
(grant agreement No948057).
KP was supported by the project
GA24-11098S of the Czech Science Foundation. JG was supported
by the Polish National Science Centre SONATA-18 grant number
2022/47/D/ST6/03421.
1In the original paper [13], contraction∗-depth was called branch-depth. However, due to the naming
clash with the notion by DeVos et al., this parameter was renamed to contraction∗-depth.
1
arXiv:2501.09689v1  [math.CO]  16 Jan 2025

--- Page 2 ---

Recently it was shown that matroids of bounded contraction∗-depth can be used to
find efficient algorithms for block-structured integer programs [2, 5]. This has led to fur-
ther study of this notion and introduction of similar parameters such as deletion-depth,
contraction-depth [6,7] and contraction∗-deletion-depth [3]. All these parameters have the
same general structure: The aim is to recursively decompose a matroid M by applying
a simplification operation (contraction, deletion, ...) to M (if M is connected) and then
continuing in each connected component of the resulting matroid separately. The X-depth
(where X is the simplification operation in question) of M corresponds to the number of
applications of the simplification operation in the deepest branch in this recursive decom-
position.
In this work, we focus on obstructions for these depth parameters. First, we prove that
obstructions for contraction∗-depth of F-representable matroids are bounded in size:
Theorem 1. Let F be a finite field. Let M be an F-represented matroid such that c*d(M) =
d and c*d(M \ e) < d for every e ∈M. Then |M| ⩽f(|F|, d) for some function f.
Our proof relies on techniques from finite model theory.
We show that every F-
represented matroid of bounded contraction∗-depth can be encoded in a tree T of bounded
depth using CMSO logic and also that the property of having contraction∗-depth exactly
d can be expressed in CMSO. Then we use a result of [9] to argue that if T is tree that
encodes matroid satisfying the assumptions of Theorem 1, then T cannot be too large.
Next, we introduce a new depth parameter named deletion∗-depth and show that this
parameter is dual to contraction∗-depth in the following sense.
Theorem 2. For every represented matroid M we have c*d(M) = d*d(M ∗).
We use this duality result to extend Theorem 5 to this new parameter.
Theorem 3. Let F be a finite field. Let M be an F-represented matroid such that d*d(M) =
d and d*d(M/e) < d for every e ∈M. Then |M| ⩽f(|F|, d) for some function f.
We then focus on contraction-depth and deletion-depth. The proof Theorem 1 can be
easily adjusted to obtain the following result for contraction-depth.
Theorem 4. Let F be a finite field. Let M be an F-represented matroid such that cd(M) =
d and cd(M \ S) < d for every non-empty set S of elements of M. Then |M| ⩽f(|F|, d)
for some function f.
Using the fact that contraction and deletion are dual operations, we also obtain the
following dual result for deletion-depth.
Theorem 5. Let F be a finite field. Let M be an F-represented matroid such that dd(M) =
d and dd(M/S) < d for every non-empty set S of elements of M. Then |M| ⩽f(|F|, d)
for some function f.
2

--- Page 3 ---

As a an example application of our Theorem 1 we obtain Theorem 6 below. For its
statement, we note that if M is a matroid represented by a matrix with m rows, and if
v ∈Fm, then by M/v we denote simplification operation used to define contraction∗-depth.
We then call a vector v ∈Fm progresive if c*d(M/v) < c*d(M).
Theorem 6. There exists a function g : N × N →N such that for every F and d, if M is
a F-represented matroid with c*d(M) = d, then the number of progressive vectors for M is
at most g(|F|, d).
Finally, we note that Theorems 1 and 6 can be extended to Q-representable matroids
with small entry complexity.
Related work.
Characterizing obstructions is one of the classical problems surrounding
structural parameters. For matroids of branch-width at most k, it is known that each
excluded minor has size at most (6k+1−1)/5 due to the result of Geelen, Gerards, Robertson
and Whittle [10]. In [12], Kanté, Kim, Kwon and Oum studied obstructions for matroid
path-width. Precisely, they proved that every excluded minor representable over a finite
field F for the class of matroids of path-width at most k has at most 2|F|O(k2) elements.
Various structural and algorithmic properties of contraction∗-depth were studied in [4],
who studied the connection of contraction∗-depth to integer programming, and gave an FPT
algorithm for computing contraction∗-depth of matroid representable over finite fields. The
closure properties of contraction-depth in relationship to contraction∗-depth was studied
by Briański, Kráľ and Lamaison [3], who proved that the minimum contraction-depth of
a matroid M ′ that contains M as a restriction is equal to the contraction∗-depth of M
increased by one.
A result analogous to our Theorem 6 was proven for graphs of bounded treedepth in [8],
and was used in [1] to show that the graph isomorphism problem is in FPT for graph classes
of bounded treedepth.
2
Preliminaries
In this section, we recall the notation and preliminaries needed throughout the paper.
2.1
Graph theory
All graphs in this paper are finite, undirected and simple, without loops. We use standard
graph theoretic notation and terminology. By a rooted tree we mean a connected acyclic
graph with a specified vertex, called the root of the tree. All trees in this paper are rooted,
unless stated otherwise.
The depth of a tree T is the number of edges on the longest
leaf-to-root path in T. Let u, v be two vertices of a tree T. We say that u is an ancestor
of v if u lies on the unique path from v to the root of T. The closure of a tree T, denoted
by cl(T), is the graph obtained by making every vertex of T adjacent to all its ancestors
(except itself).
3

--- Page 4 ---

A rooted forest is a graph in which each connected component is a rooted tree. The
depth of a rooted forest is the largest depth of its connected components. The closure of a
rooted forest F, denoted by cl(F), is the graph obtained from F by taking the closure of
each connected component.
Let G be a graph. A rooted forest F is a elimination forest of G if V (G) = V (F) and
G is a subgraph of cl(F). The tree-depth of G, denoted by td(G), is defined as
td(G) := min
F
depth(F) + 1,
where the minimum is taken over all elimination forests of G.
The following simple observation follows directly from the definition of tree-depth.
Lemma 7. Let G be a graph and F its elimination forest. Then in every clique K of G,
all vertices of K are pairwise comparable by the ancestor relation of F. In particular, in
every clique K of G there is a vertex v sucht that all vertices of K are ancestors of v in F.
2.2
Linear algebra and matrices
We assume familiarity with vector spaces and basic notions of linear algebra.
In this
section, we mainly review the concepts and notation used in this paper. In what follows, F
always denotes a field; usually this will be a finite field or Q. All vector spaces we consider
are finite-dimensional. Vectors are written in bold, while their coordinates are written in
normal font. For example, v denotes a vector, while vi its i-th coordinate.
Vectors v1, . . . , vk from a vector space V are linearly independent if α1v1+. . .+αkvk =
0 implies α1 = . . . = αk = 0; otherwise they are linearly dependent. Let S be a set of vectors
from a vector space V over F. By span(S) we denote the set of all F-linear combinations
of vectors from S, i.e. span(S) := {α1v1 + . . . + αkvk | k ∈N, αi ∈F, vi ∈S}. Note that
span(S) is always a linear subspace of V .
For two vectors v = (v1, . . . , vn)⊤and w = (w1, . . . , wn)⊤in Fn we define v · w =
Pn
i=1 viwi. Let W be a linear subspace of Fn. We define the orthogonal complement of
W by W ⊥:= {v ∈Fn | v · w = 0 for all w ∈W}. Note that we have (W ⊤)⊤= W and
(U ∩W)⊥= span(U ⊥∪W ⊥). Also, every v ∈Fn can be uniquely written as v′ +v′′ where
v′ ∈W and v′′ ∈W ⊥. From this one easily shows that W ∩span(v)⊥= W ∩span(v′)⊥.
Let V be a vector space over F. A set B = {v1, . . . , vk} of vectors is a basis of V if B is
inclusion-wise minimal such that V = span(v1, . . . , vk). We say that a basis B is orthogonal
if vi · vj = 0 if and only if i ̸= j for each i, j. By the Gram-Schmidt orthogonalization, for
any finite-dimensional vector space V and any v ∈V with v ̸= 0 we can find an orthogonal
basis v1, . . . , vk of V such that v1 = v.
Let V be a vector space over F and W be its linear subspace. The quotient space V/W
has as its elements the equivalence classes of relation ∼defined by v ∼u if v −u ∈W.
The vector space structure V/W is defined in the natural way.
For a matrix A over Q, the entry complexity of A, denoted by ec(A), is the maximum
length of a binary encoding of an entry. The length of a binary encoding of a rational
number r = p/q with p and q being coprime is ⌈log2(|p| + 1)⌉+ ⌈(log2 |q| + 1)⌉.
4

--- Page 5 ---

Finally, we define the tree-depth of matrices. This is done by measuring the tree-depth
of a graph associated with the matrix. There exist several ways to derive such underlying
graph; in this paper, we focus on the concept of so called dual graph. Formally, the dual
graph of a matrix A, denoted by GD(A), is the graph where vertices one-to-one correspond
to the rows of A and there is an edge between two rows r1 and r2 if there exists a column
c such that both entries of r1 and r2 at c are non-zero. The dual tree-depth of a matrix A
is then defined as tdD(A) := td(GD(A)).
2.3
Matroids
For matroids, our presentation is primarily based on the monography of Oxley [14].
A matroid M is a pair (X, I), where X is a finite set and I ⊆2X a collection of subsets
that satisfies the following three matroid axioms:
1. ∅∈I.
2. If A ∈I and B ⊆A, then B ∈I.
3. if A, B ∈I and |A| > |B|, then there exists an element x ∈A \ B such that
B ∪{x} ∈I.
The set X is called the ground set of M, and the sets in I are referred to as independent.
We usually refer to elements of the ground set of a matroid M as elements of M.
If X′ ⊆X is a set of elements of a matroid M, then M[X′] denotes the restriction of
M to X′. This is a matroid with the ground set begin X′, and a subset of elements of this
matroid is independent if and only if it is independent in the original matroid M. For a
subset X′ ⊆X, the rank of X′, denoted by rM(X′) is the largest size of an independent
set contained in X′. The rank of M is r(M) = rM(X). A basis of a matroid M is a
maximal independent set of the ground set, while a circuit of the matroid is a minimal
dependent set. A matroid M is connected if any two elements of M are contained in a
common circuit. The property of being contained in a common circuit is transitive, that
is, if two elements e, e′ ∈M are contained in a common circuit and e′ and e′′ are contained
in a common circuit, then also e, e′′ are contained in a common circuit. A component of a
matroid M is an inclusion-wise maximal connected restriction of M.
Let A be a matrix over some field F and M(A) its vector matroid, i.e., a matroid, where
the grounds set consists of the column vectors of A and whose independent sets are the
linearly independent sets of column vectors of A. If a matroid M is isomorphic to M(A),
then we say that M is representable over F or F-representable. The matrix A is then called
the representation for M over F or F-representation. When a matroid M is given by its
representation A, we say that M is F-represented or just represented, if F is clear from the
context or not important.
5

--- Page 6 ---

2.3.1
Matroid contraction and deletion
Let M = (X, I) be a matroid and X′ ⊆X a set of its elements. The restriction of M to
X′, denoted by M[X′], is the matroid on the ground set X′ where a subset X′′ ⊆X′ is
independent if it was independent in the original matroid M. By the deletion of X′ from
the matroid M we mean the operation that takes M to the matroid M \ X′ := M[X \ X′].
To simplify the notation, if X′ is, in fact, just a single element, we write M \ x rather than
M \ {x}.
The contraction of a matroid M by X′, denoted by M/X′, is the matroid with the
ground set X \X′ and the independence notion defined as follows: a subset X′′ ⊆(X \X′)
is independent in M/X′ if and only if:
rM(X′′ ∪X′) = |X′′| + rM(X′)
For represented matroids, contraction can be defined as follows. Let M = M(A) be
a represented matroid and let h be the number of rows of A. Further, let K be a linear
subspace of Fh.
We then define the matroid M/K as the matroid whose ground set
consists of the columns of A and where columns v1, . . . , vk are dependent if there exist
α1, . . . , αk ∈F, not all 0, such that α1v1 + . . . αkvk ∈K. If K is a 1-dimensional subspace
of Fh spanned by a vector v ∈Fh, we often write M/v instead of M/K. We remark that
contraction for represented matroids is usually introduced using quotient spaces, but the
more explicit (and equivalent) definition given above will be useful for us.
2.3.2
Matroid duality
Let M = (X, I) be a matroid. We define the dual of M, denoted by M ∗, to be the matroid
on the same ground set, and in which a set S is independent if and only if M has a basis
B disjoint from S.
We will need the following two facts about matroid duality.
Lemma 8 (Deletion is dual to contraction). For every matroid M and any e we have
(M \ e)∗= M ∗/e.
Lemma 9. For a matroid M, a subset S of its ground set is a connected component of M
if and only if it is a connected component of M ∗.
2.4
Matroid parameters and their properties
Definition 10 ([6]). The deletion-depth dd(M) of a matroid M is defined recursively as:
• If M has single element, then dd(M) = 1.
• If M is not connected, then the deletion-depth of M is the maximum deletion-depth
of a component of M.
• If M is connected, then dd(M) = 1 + mine∈M dd(M \ e).
6

--- Page 7 ---

For a matrix A, the deletion depth of A is defined as dd(A) := dd(M(A)).
Definition 11 ([6]). The contraction-depth dd(M) of a matroid M is defined recursively
as:
• If M has single element, then cd(M) = 1.
• If M is not connected, then the contraction-depth of M is the maximum contraction-
depth a component of M.
• If M is connected, then cd(M) = 1 + mine∈M cd(M/e).
From the fact that deletion and contraction are dual operations one easily proves the
following.
Lemma 12. For any matroid M we have cd(M) = dd(M ∗) and cd(M ∗) = dd(M).
For representable matroids, a generalization of contraction-depth called contraction∗-
depth was introduced in [13]. The difference between these two notions is that in contraction∗-
depth we do not have to perform contraction by an element of M, but by arbitrary one-
dimensional subspace of the space in which the matroid is represented.
Definition 13 ([5]). For a represented matroid M = M(A), the contraction∗-depth c*d(M)
of M is defined recursively as:
• If M has rank 0, then c*d(M) = 0.
• If M is not connected, then the contraction∗-depth of M is the maximum contraction∗-
depth a component of M.
• If M is connected, then c*d(M) = 1 + min c*d(M/v), where v ∈Fh (here h is the
number of rows in A).
For a matrix A, we define c*d(A) := c*d(M(A)).
Theorem 14 ([5]). Let A be a matrix over a field F. The contraction∗-depth of A is the
minimum dual tree-depth of any matrix A′ that is row equivalent to A.
Since c*d(A) = c*d(M(A)) and row equivalent matrices describe the same matroids, we
have the following corollary.
Corollary 15. If M is a matroid representable over F with c*d(M) = d, then it can be
represented by a matrix A over F of dual tree-depth d.
We will use the fact that contraction∗-depth is closed under deletion of elements.
Lemma 16 ([13]). For every representable matroid M and any subset X′ of elements of
M we have c*d(M[X]) ≤c*d(M).
7

--- Page 8 ---

DeVos, Kwon and Oum [6] established the following relationship between contraction-
depth and maximum circuit length:
Theorem 17. Let M be a matroid and c the length of its largest circuit; if M has no
circuit, then set c = 1. Then
log2 (c) ⩽cd(M) ⩽c(c + 1)
2
Kardoš, Kráľ, Liebenau and Mach [13] showed the following for contraction∗-depth:
Proposition 18. Let M be a matroid and c the size of its largest circuit. Then
log2 c ⩽c*d(M) ⩽c2.
As an easy corollary of the previous two results, we see that contraction-depth and
contraction∗-depth are functionally equivalent. This was already observed in [6] without a
proof, so we provide a proof for completeness.
Theorem 19. There exists a function f such that c*d(M) ⩽cd(M) ⩽f(c*d(M)) for any
matroid M.
Proof. The first inequality is easily seen from the definitions of contraction-depth and
contraction∗-depth. For the second inequality, let M be a matroid of contraction∗-depth
c*d(M) = d, and let c denote the length of its largest circuit. By Theorem 18, log2 c ⩽k,
and hence c ⩽2d. By Theorem 17, we have cd(M) ⩽1
2(c(c + 1)), and by plugging in the
previous inequality, we obtain that cd(M) ⩽1
2(2d(2d + 1)) = 1
2(22 c*d(M) + 2c*d(M)).
Finally, to extend some of our results to Q-representable matroids we will need the
following lemma.
Lemma 20 ([5]). There exists a function h : N × N →N such that for every matroid M
represented over Q with entry complexity e can be represented over Fq with q ≤h(e, c*d(M)).
2.5
Logic
We will use Monadic Second Order logic with modulo counting (CMSO) in some of our
proofs. We will specialize our treatment of logic to the two domains that will be relevant
for us – rooted labelled trees and matrices.
We model rooted labelled trees that use labels from a finite set S as structures over
the signature consisting of a binary predicate symbol par and for each a ∈S a unary
predicate symbol La(x). These predicates have the natural meaning – par(x, y) says that
x is a parent of y and La(x) means that node x is labelled with label a. For example, we
can express that x is a leaf by ¬(∃y.par(x, y)) and express ‘Every leaf has label a’ by the
sentence ∀x.(leaf(x) →La(x)).
8

--- Page 9 ---



c1
c2
c3
c4
r1
1
1
2
0
r2
2
0
1
2
r3
1
2
0
1


S(A) = {r1, r2, r3, c1, c2, c3, c4}
RS(A) = {r1, r2, r3}
CS(A) = {c1, c2, c3, c4}
EntryS(A)
0
= {(r1, c4), (r2, c2), (r3, c3)}
EntryS(A)
1
= {(r1, c1), (r1, c2), (r2, c3), (r3, c1), (r3, c4)}
EntryS(A)
2
= {(r1, c3), (r2, c1), (r2, c4), (r3, c2)}
Figure 1: An example of a matrix A and its associated structure S(A).
For a finite field F we model matrices with entries from F as structures over the signature
ΣF = {R, C}∪{Entryα}α∈F where R and C are unary predicate symbols and each Entryα
is a binary predicate symbol. To any matrix A over F, we associate a ΣF-structure S(A)
as follows: The universe if S(A) is rows(A) ∪columns(A). Unary predicate R is realized
as RS(A) = rows(A) and analogously CS(A) = columns(A). To define the realization of
Entryα, for a row r and a column c we denote by A(r, c) the entry of A in row r and
column c. Then, for each α ∈F we define
EntryS(A)
α
= {(r, c) | r ∈rows(A), c ∈columns(A), A(r, c) = α}
For example, if we want to say that every row of A contains a specific element α ∈F, we
can express it as follows: ∀x(R(x) →∃y(C(y)∧Entryα(x, y)). To shorten and unclutter our
formulas, we will introduce row and column quantifiers: ∀Rx means ‘for each row x’ and ∃Rx
means ‘there exists a row x’. For columns the quantifiers ∀C and ∃C are defined analogously.
The example formula given above can then be expressed as ∀Rx∃Cy.Entryα(x, y).
The examples of formulas given above were formulated in the first-order logic (FO),
meaning that the quantification was over the elements of the universe in question (nodes
of a tree or rows/columns of a matrix). In MSO logic we can also quantify over subsets
of the universe. In this setting, we use capital letters X, Y, . . . for set variables, and we
use predicate x ∈X to denote that x belongs to set X.
For example, the sentence
∃X.∀x.((leaf(x) →x ∈X) ∧(root(x) →x ̸∈X)) ∧(∀x∀y(par(x, y) →(x ∈X ↔y ̸∈X))
expresses that all leaves are at odd distance from the root. For formulas in the language of
matrices, we can consider set quantifiers that speak of sets of rows or columns only, so for
example ∀CX reads as ‘for all sets of rows’ and the quantifiers ∃CX, ∀RX, ∃RX are defined
analogously. We note that these quantifiers are only syntactic shorthands, and they can
be replaced by the standard set quantifiers. For example, the formula ∀XC.φ(X) can be
expressed as ∀X.(∀x.(x ∈X →C(x))) →φ(X)).
Finally, in the CMSO logic we can also use predicates of the form moda,b(X); the
semantics of this predicate is that |X| = a (mod b).
An interpretation of matrices in trees is a tuple I = (ν(x), ρC(x), ρR(x), {ψα(x, y)}α∈F)
of formulas over the signature of labelled trees. To labelled tree T the interpretation I
9

--- Page 10 ---

assigns a matrix structure I(T) as follows: The universe of I(T) is the set {v ∈V (T) | T |=
ν(v)}. The realization of predicate R in I(T) is given by {v ∈V (T) | T |= ρR(v)}, and
the realization of predicate C is defined analogously. Finally, for each α ∈F the predicate
Entryα is realized as {(u, v) | T |= ψα(u, v)}.
To a sentence φ in the language of matrices, the interpretation I assigns a new sentence
I(φ) in the language of trees as follows. Each occurrence of R(x) and C(x) is replaced by
ρR(x) and ρC(x), respectively, and each occurrence of Entryα(x, y) is replaced by ψα(x, y).
Moreover, all quantifications are relativized to elements x that satisfy ν(x).
We will need the following lemma, proof of which (in the case of general interpretations)
can be found for example in [11].
Lemma 21. Let φ be a sentence over the language of matrices and let I be an interpretation
of matrices in trees. Then for every tree T we have I(T) |= φ ⇐⇒T |= I(φ).
3
Expressing contraction∗-depth in CMSO
In this section, we show that in CMSO it is possible to express that a matrix A represents
a matroid of contraction∗-depth at most d.
This result will be crucial in the proof of
Theorem 1.
Theorem 22. For every d there exists a CMSO sentence csdd such that for every matrix
A over F we have SA |= csdd if and only if c*d(M(A)) ≤d.
To prove Theorem 22 we need to overcome several difficulties:
• The definition of contraction∗-depth is phrased in terms of matroids, but the sentence
csdd from Theorem 22 has to work on a matrix (on a matrix structure, to be more
precise). We will therefore rephrase Definition 13 in terms of matrices and quotient
spaces (see Section 3.1).
• Let A be a matrix over F and let m be the number of rows of A. The definition of
contraction∗-depth uses an operation where we pick an arbitrary vector v in Fm and
we quotient the vector space we are currently working with by v. Expressing this in
CMSO would be easy if v was one of the columns of A, but in general we cannot
assume this, and so our formula csdd has to be able to quantify over all vectors from
Fm. We resolve this by introducing virtual columns (Section 3.2).
• In our formula csdd, we need to be able to check whether a set X of columns of A is
linearly (in)dependent over F (Section 3.3). To do this, our formula will have to be
able to speak about sums of arbitrarily large number of entries that are in the same
row of A. We will now illustrate how we can address this on a simpler problem –
checking whether all entries of A in a given row r of A sum to 0. To check this, we
can proceed as follows. Let p := |F| and let α1, . . . , αp be an enumeration of elements
of F. We partition the columns of A into sets X1, . . . , Xp by putting c into Xi if
10

--- Page 11 ---

A(r, c) = αi. For each i ∈[p] set ki := |Xi|. Then our problem reduces to checking
whether k1α1 + . . . + kpαp = 0. While each ki can be arbitrarily large, we know that
for each α ∈F we have pα = 0 in F, and so kiαi = riαi, where ri is the reminder of
ki/p, i.e. ri = ki(mod p). Thus, we only need to check whether r1α1 +. . .+rpαp = 0.
This is where we use the modulo counting feature of CMSO: we can use predicates
of the form modri,p(Xi) to determine ri. Since for us the value p is a fixed constant
(our formula is allowed to depend on F) and for each i we have ri < p, the formula
that checks whether the entries in row r sum to 0 can be written as
ZeroSum(x) := ∃X1 . . . ∃Xp ∀y
 p^
i=1
(c ∈Xi ↔Entryαi(x, y))
!
∧
∧
_
r1,...,rp∈F
r1α1+...+rpαp=0
 p^
i=1
modri,p(Xi)
!
.
3.1
Rephrasing the definition of contraction∗-depth
To be able to speak in CMSO about contraction∗-depth of a matrix, it will be convenient
for us to rephrase the definition contraction∗-depth explicitly in terms of quotient spaces.
Let A be a matrix A and let v1, . . . , vk be vectors from Fm, where m is the number
of rows of A.
We say that a set X = {u1, . . . , uℓ} of columns of A (where we treat
them as vectors from Fm) is dependent with respect to v1, . . . , vk if there exist coefficients
α1, . . . , αℓ∈F, not all 0, such that α1u1 + . . . + αℓuℓ∈span(v1, . . . , vk). In other words,
X is dependent with respect to v1, . . . , vk if it is dependent in Fm/span(v1, . . . , vk).
Based on A and v1, . . . , vk we define matroid M(A, {v1, . . . , vk}) as follows.
The
ground set of M(A, {v1, . . . , vk}) is the set of all columns of A, and we say that a subset
X = {u1, . . . , us} of columns(A) is dependent in M(A, {v1, . . . , vk}) if it is dependent with
respect to v1, . . . , vk.
The contraction∗-depth c*d(A, {v1, . . . , vk}) of a matrix A and set {v1, . . . , vk} of
columns is defined recursively as:
• If M(A, {v1, . . . , vk}) has rank 0, then c*d(A, {v1, . . . , vk}) = 0.
• If M(A, {v1, . . . , vk}) is not connected, then the contraction∗-depth of A, {v1, . . . , vk}
is the maximum contraction∗-depth of any A′, {v1, . . . , vk} where A′ is a submatrix
of A formed by the elements of a connected component of M(A, {v1, . . . , vk}).
• If M is connected, then c*d(A, {v1, . . . , vk}) = 1 + min c*d(A, {v1, . . . , vk, vk+1}),
where the minimum is taken over all vectors vk+1 from Fm.
It is easily verified that for a matrix A we have c*d(M(A)) = c*d(A, ∅).
11

--- Page 12 ---

3.2
Virtual columns
Let A be a matrix and SA the corresponding matrix structure. A virtual column of S(A) is
an F-indexed family {Qα}α∈F of subsets of rows of SA such that S
α∈F Qα = R (recall that
R is the set of elements of SA that correspond to rows of A) and Qα ∩Qβ = ∅if α ̸= β.
To simplify the notation, we will denote virtual columns by ⟨Q⟩instead of {Qα}α∈F.
Let R = {r1, . . . , rm} be the set of rows of A. To every virtual column ⟨Q⟩we assign a
vector v(⟨Q⟩) = (v1, . . . , vm)T ∈Fm by setting vi := α if ri ∈Qα.
Since every virtual column corresponds to a finite family of subsets of rows of SA, we
can work with virtual columns in CMSO – they correspond to F-indexed families of set
variables. Again, to simplify the notation, we will write ⟨X⟩instead of {Xα}α∈F. Note
that we can quantify over virtual columns – for example, ∃⟨X⟩can be implemented as
∃CXα1 . . . ∃CXαp, where α1, . . . , αp is an enumeration of elements of F. Universal quantifi-
cation is handled analogously. We will need the following lemma.
Lemma 23. For every k, there exists a formula LinCom(⟨Z⟩, ⟨Y 1⟩, . . . , ⟨Y k⟩) such that
for any matrix structure S(A) and any virtual columns ⟨L⟩, ⟨J1⟩, . . . , ⟨Jk⟩we have that
S(A) |= LinCom(⟨L⟩, ⟨J1⟩, . . . , ⟨Jk⟩) if and only if v(⟨L⟩) ∈span(v(⟨J1⟩), . . . , v(⟨Jk⟩)).
Proof. For any (α1, . . . , αk) ∈Fk define
I(α1, . . . , αk) := {(γ, β1, . . . , βk) | α1β1 + . . . + αkβk = γ}
We define the formula LinCom(⟨Z⟩, ⟨Y 1⟩, . . . , ⟨Y k⟩) by
_
(α1,...,αk)∈Fk
∀x.R(x) →


_
(γ,β1,...,βk)∈I(α1,...,αk)
 k^
i=1
(x ∈Y i
βi) ∧x ∈Zγ
!

We now argue that the formula has the required property.
Let ⟨L⟩, ⟨J1⟩, . . . , ⟨Jk⟩
be virtual columns and set u := v(⟨L⟩), v1 := v(⟨J1⟩), . . . , vk := v(⟨Jk⟩) to simplify
the notation. Then u ∈span(v1, . . . , vk) if and only if there exist α1, . . . , αk (the first
disjunction in our formula) such that α1v1 + . . . + αkvk = u. This equality is true if and
only if for every row x of SA we have that if γ is the value of Z on row r and βi is the
value of Y i on row r, then γ = α1β1 + . . . + αkβk (this is the innermost conjunction in our
formula; the big disjunction over members of I(α1, . . . , αk) is there to obtain the values of
all entries of ⟨Z⟩, ⟨Y 1⟩, . . . , ⟨Y k⟩at row x).
3.3
Linear dependence in quotient spaces in CMSO
Lemma 24. For every k there exists a CMSO formula Dep(X, ⟨Y 1⟩, . . . , ⟨Y k⟩) such that
for any matrix A over F, any set S of columns of A and any virtual columns ⟨Q1⟩, . . . , ⟨Qk⟩
we have that S is linearly dependent with respect to v(⟨Q1⟩), . . . , v(⟨Qk⟩) if and only if
S(A) |= Dep(S, ⟨Q1⟩, . . . , ⟨Qk⟩).
12

--- Page 13 ---

Proof. It suffices to show that there exists a formula Dep(X, ⟨Z⟩) that expresses that
the set X of columns is dependent with respect to ⟨Z⟩.
Then, the desired formula
Dep(X, ⟨Y 1⟩, . . . , ⟨Y k⟩) can be written as
Dep(X, ⟨Y 1⟩, . . . , ⟨Y k⟩) := ∃⟨Z⟩(Dep(X, ⟨Z⟩) ∧LinCom(⟨Z⟩, ⟨Y1⟩, . . . , ⟨Yk⟩))
where LinCom is the formula from Lemma 23.
Next, set p := |F|.
We now proceed to building the formula Dep(X, ⟨Z⟩) in steps
from simpler formulas.
First, we show that for every α, β ∈F there exists a formula
sumα,β(X, y) such that the following holds: If S is a set of columns of A and r is a row of
A, then SA |= sumα,β(S, r) if and only if
X
c∈S
A(r,c)=β
A(r, c) = α.
In words, the formula sumα,β(X, y) checks whether α is the sum of all entries of A in row
r that intersect Q and have value β. We now describe the formula’s construction. Let S′
be the subset of S that contains precisely the columns c for which A(r, c) = β. Note that
all the entries A(r, c) in the sum above are equal to β, and so we have
X
c∈S
A(r,c)=β
A(r, c) =
X
c∈S′
A(r, c) = |S′| · β
Note that in F we have |S′| · β = q · β, where q ≡|S′| mod p (this is because p · β = 0),
and so the formula sumα,β only needs to check whether |S′| ≡q mod p for some q with
q · β = α. Thus, we can write sumα,β as follows:
sumα,β(X, y) :=
_
q
∃CZ[(∀z ∈Z ↔(Entryβ(y, z) ∧z ∈X)) ∧modq,p(Z)]
where the disjunction is over all q ≤p with q · β = α.
Next, we describe, for each γ ∈F, the formula sumγ(Y, y) such that for every row r
and every set S of columns of A we have that S(A) |= sumγ(S, r) if and only if
X
c∈Q
A(r, c) = γ.
(1)
Let us enumerate the elements of F as β1, . . . , βp. Clearly we have
X
c∈S
A(r, c) =
p
X
i=1
X
c∈S
A(r,c)=βi
A(r, c).
Consequently, we have that (1) holds if and only if for some α1, . . . , αp with α1+. . .+αp = γ
we have
S(A) |=
p^
i=1
sumαi,βi(S, r)
13

--- Page 14 ---

Thus, we can write the formula sumγ(Y, y) as
sumγ(Y, y) :=
_
(α1,...,αp)
α1+...+αp=γ
 p^
i=1
sumαi,βi(Y, y)
!
Finally, we describe the formula Dep(X, ⟨Z⟩) such that for every set S of columns
and every virtual column ⟨Q⟩of A we have that S(A) |= Dep(S, ⟨Q⟩) if and only if S
is dependent with respect to v(⟨Q⟩). By definition, S = {u1, . . . , uℓ} is dependent with
respect to v(⟨Q⟩) if there are coefficients α1, . . . , αℓin F, not all 0, such that α1u1 + . . . +
αℓuℓ= δv(⟨Q⟩) for some δ ∈F. In the language of S(A), where we have S = {c1, . . . , cℓ},
this translates to requiring that for every row r we have
ℓ
X
j=1
αiA(r, ci) = δσr,
(2)
where σr is the entry of v(⟨z⟩) at row r.
Again, let β1, . . . , βp be an enumeration of the elements of F. Since each coefficient αj
is equal to some βi, we can think of an assignment of coefficients α1, . . . , αℓto columns in
S as of partitioning of S into sets Y1, . . . , Yp, where we put αj into Yi if αj = βi. Here we
require at least one Yi with βi ̸= 0 is non-empty. Condition (2) then says that for each row
r we require that
p
X
i=1
(βi ·
X
c∈Yi
A(r, c)) = σr
This happens if for each row r of A there are γ1, . . . , γp such that β1·γ1+. . .+βp·γp = σr
and for each i ∈[p] we have that SA |= sumγi(Yi, r). Thus, we can write Dep(X, ⟨Z⟩) as
Dep(X, ⟨Z⟩) := ∃Y1 . . . ∃Yp∀Ry
_
(γ1,...,γp,σ)
β1·γ1+...+βp·γp=σ
 ^
1≤i≤p
sumγi(Yi, c) ∧y ∈Zσ
!
∧
p_
i=1
βi̸=0
Yi ̸= ∅.
3.4
Formula for contraction∗-depth
In this section we will prove Theorem 22.
We start by showing that we can express
connectivity and connected components in CMSO. To unclutter the notation we will assume
that all set quantifiers in this section are over sets of columns, and we will write ∃, ∀
everywhere instead of ∃C and ∀C.
Lemma 25. For every k there is a CMSO formula cc(X, Z, ⟨Y1⟩, . . . , ⟨Yk⟩) such that for ev-
ery matrix A, subsets S, T of columns of A with S ⊆T and virtual columns ⟨Q1⟩, . . . , ⟨Qk⟩
we have that S(A) |= cc(S, T, ⟨Q1⟩, . . . , ⟨Qk⟩) if and only if S is a connected component of
M(A, v(⟨Qk⟩), . . . , v(⟨Qk⟩))[T].
14

--- Page 15 ---

Proof. We can express that a set Y of columns is a circuit:
circ(Y, ⟨Y1⟩, . . . , ⟨Yk⟩) := Dep(Y, ⟨Y1⟩, . . . , ⟨Yk⟩)∧(∀Y ′.(Y ′ ⊊Y →¬Dep(Y ′, ⟨Y1⟩, . . . , ⟨Yk⟩))
Using this, it is straightforward to express that a set X of columns is connected in the
restriction of the original matroid to a set Z of columns:
conn(X, Z, ⟨Y1⟩, . . . , ⟨Yk⟩) :=∀x∀y(x ∈X ∧y ∈X) →
→(∃Y.Y ⊆Z ∧x ∈Y ∧y ∈Y ∧circ(Y, ⟨Y1⟩, . . . , ⟨Yk⟩))
Finally, it is easy to express that X is a maximal connected set in Z.
cc(X, Z, ⟨Y1⟩, . . . , ⟨Yk⟩) :=conn(X, Z, ⟨Y1⟩, . . . , ⟨Yk⟩)∧
∧∀Y. ((X ⊆Z ∧X ⊊Y ) →¬conn(Y, Z, ⟨Y1⟩, . . . , ⟨Yk⟩))
Proof of Theorem 22. For every d we provide a formula that expresses that a subset Z of
columns of a matrix A represents a matroid of contraction∗-depth at most d.
For contraction∗-depth 0, we just need to check whether all non-empty subsets of
columns are dependent (meaning that the only independent set has size 0 and so the
rank is 0):
csd0(Z, ⟨Y1⟩, . . . , ⟨Yk⟩) := ∀X. (X ⊆Z ∧X ̸= ∅) →Dep(X, ⟨Y1⟩, . . . , ⟨Yk⟩)
For contraction∗-depth d > 1, we proceed according to the recursive definition:
csdd(Z, ⟨Y1⟩, . . . , ⟨Yk⟩) := (conn(Z, Z, ⟨Y1⟩, . . . , ⟨Yk⟩) →∃⟨Y ⟩.(csdd−1(Z, ⟨Y1⟩, . . . , ⟨Yk⟩, ⟨Y ⟩))
∧(¬conn(Z, Z⟨Y1⟩, . . . , ⟨Yk⟩) →(∃X.cc(X, Z, ⟨Y1⟩, . . . , ⟨Yk⟩) →csdd(X, ⟨Y1⟩, . . . , ⟨Yl⟩)))
∧∀X.cc(X, Z, ⟨Y1⟩, . . . , ⟨Yk⟩) →
d_
i=0
csdi(X, ⟨Y1⟩, . . . , ⟨Yl⟩)))
Finally, the sentence csdd will work on the set of all column vectors and will not use
any virtual columns:
csdd := ∃Z ((∀x(x ∈Z)) ∧csdd(Z))
4
Minimal matroids of given contraction∗-depth
In this section we prove Theorem 1, showing that deletion-minimal matroids with contraction∗-
depth d have size bounded in terms of d and |F|. We will proceed as follows.
• Going for contradiction, we will assume that there exists a matroid M with c*d(M) =
d and |M| > N, where N is suitably chosen number depending on d and |F|.
15

--- Page 16 ---

• Based on Corollary 15, M can be represented by a matrix A of dual tree-depth d.
We will show each such matrix can be encoded in a colored tree T of depth d + 2
in such a way that we can recover matrix the structure S(A) from T by a CMSO
interpretation.
• Since S(A) can be intrepreted in T, by Lemma 21 we can translate the sentence csdd
from Theorem 22 to a sentence csdtree
d
such that T |= c*d
tree
d
if and only if the matrix
represented by T has contraction∗-depth d.
• By a result of [9], if T is larger than N (for some N depending on d and csdtree
d
), then
there is a subtree T ′ such that T |= csdtree
d
if and only if T ′ |= csdtree
d
. From this we
deduce that the matrix A′ that is encoded by T ′ represents a matroid M ′ = M(A′) of
contraction∗-depth d. We will show that this matroid is a restriction of M, and this
will yield a contradiction with our assumption that M is deletion-minimal matroid
of contraction∗-depth d.
4.1
Encoding matrices in trees
A (d, F)-matrix-tree is a rooted tree T of depth at most d equipped with unary predicates
from the set {LR, LC} ∪{Li,α | i ∈{0, . . . , d} and α ∈F} with the following properties:
• If a node v of T is marked with a unary predicate LC, then v is a leaf.
• All other nodes of T except for the root are marked with LR.
• If v is a leaf marked with LC and v is at distance k ≤d from the root, then for each
i ∈{0, . . . , k −1} there exists exactly one α ∈F such that v is marked with Li,α.
To each (d, F)-matrix-tree T we assign a matrix AT as follows:
• The rows of AT are the nodes of T marked with LR.
• The columns of AT are the nodes of T marked with LC.
• The entry AT at row r and column c is determined by the following rule: If r is not
an ancestor of c in T, then A(T)(r, c) := 0. If r is an ancestor of c in T at distance i
from the root, then A(T)(r, c) := α, where α is the unique element of F such that c
is marked with Li,α.
Lemma 26. Let A be a matrix over F of dual tree-depth at most d.
Then there is a
(d + 3, F)-matrix-tree T(A) such that A = A(T(A)).
Proof. We construct the tree as follows:
16

--- Page 17 ---

• Let F be an elimination forest of the dual graph GD(A) of A of depth d + 1; note
that vertices of F are the rows of A. For every column c of A do the following: Let
Sc be the set of rows r for which A(r, c) ̸= 0. By construction of GD(A), these rows
form a clique K in GD(A), and so by Lemma 7 there is a vertex v ∈Sc such that all
vertices in Sc are ancestors of v in F. Create a new vertex for column c and make
it a child of v. Finally, create a new vertex and make it a parent of the roots of
connected components of F. This finishes the construction of T(A), apart from the
labelling.
• We now describe the labelling of T(A). All vertices of the original elimination forest
F will be marked with unary predicate LR and all newly created vertices for columns
will receive unary predicate LC. Finally, we will mark every vertex c corresponding
to a column of A as follows: if c has an ancestor r at distance i from the root of T
and the entry A(r, c) = α, then we mark c with label Li,α.
The fact that A = A(T(A)) follows directly from the construction.
Lemma 27. There is an interpretation I from the language of labelled rooted trees to the
language matrices over F such that for any matrix A of dual tree-depth d we have that
S(A) = I(T(A)).
Proof. To show this, we need to describe formulas ν(x), ρ(x)R, ρC(x) and ψα(x, y) for each
α ∈F that define the new universe and express that x is a row of S(A), x is a column of
S(A) and that the entry of S(A) at row x and column y is α, respectively.
These formulas can be obtained as follows. We set ν(x) := ¬root(x), where root(x) is a
formula that states that x has no parent. We then set ρR(x) := LR(x) and ρC(x) := LC(x).
To recover the entries of A, for α ̸= 0 we set
ψα(x, y) := LR(x) ∧LC(y) ∧anc(x, y) ∧
 d_
k=1
(depthk(y) ∧Lk,α(x))
!
where anc(x, t) says that y is an ancestor of x and depthk(x) says that x is at distance k
from the root; both of these are easily expressible in CMSO. For α = 0 we set φα(x, y) :=
LR(x) ∧LC(y) ∧V
β̸=0 ¬φβ(x, y).
As a simple corollary of the previous two lemmas we get a CMSO sentence that can
check whether contraction∗-depth of a matrix A is equal to d by looking at tree T(A) from
Lemma 26.
Lemma 28. For every d and F there exists a CMSO sentence csdtree
d
such that if A is a
matrix of dual tree-depth d and T(A) is the (d + 3, F)-matrix-tree from Lemma 26, then
T(A) |= c*d
tree
d
if and only if contraction∗-depth of A is d.
Proof. From Theorem 22 we have a CMSO sentence csdd such that S(A) |= csdd if and only
if c*d(A) = d. Since by Lemma 27 there exists intrepretation I such that S(A) = I(T(A)),
by Lemma 21 there is a formula csdtree
d
:= I(csdd) such that S(A) |= csdd if and only if
T(A) |= csdtree
d
.
17

--- Page 18 ---

4.2
Finishing the proof
Let T be a tree and let v be a vertex of T. A subtree Tv of T based in v is the subtree
of T consisting v together with all its descendants. If v1, . . . , vℓare nodes of T, then by
T −(Tv1 ∪. . . ∪Tvℓ) we mean the tree obtained from T by removing all vertices from
Tv1 ∪. . . ∪Tvℓ. We will need the following Theorem from [9], which we present here in a
form adjusted to our purposes.
Theorem 29 ([9], Theorem 3.5). For every d, m and every CMSO sentence φ there exist
N and M with the following property: Let T be a tree of depth at most d labelled with at
most m unary predicates such that T |= φ. If |T| > N, then there is a node v ∈V (T) and
M nodes v1, . . . , vM among its children such that for T ′ := T −(Tv1 ∪. . . ∪TvM) we have
that T ′ |= φ.
Finally, we will need one more technical lemma.
Lemma 30. Let T be a (d, F)-matrix-tree and let v be its vertex. Let T ′ = T −Tv, and let
T ′′ be obtained from T by removing all leaves of Tv marked with unary predicate Lc. Then
M(A(T ′)) is isomorphic to M(A(T ′′)).
Proof. Set A′ := A(T ′) and A′′ := A(T ′′). Note that A′ and A′′ have the same set of
columns; the difference between them is that A′′ contains more rows – these correspond
precisely to the vertices of Tv marked with predicate LR. We will argue that in A′ these
rows are identically 0.
Then clearly we will have that any set X of columns of A′ is
independent if an only if it is independent in A′′, and the result follows.
To argue that all rows contained in Tv are identically 0 in A′′, we proceed as follows. Let
r be any row contained in Tv. If c is any column such that A(r, c) ̸= 0, then by construction
of T(A) we have that c must be a descendant of r, and therefore c must be a leaf of Tv.
Since A′′ does not contain any leaves of T(A)v, this finishes the proof.
Theorem 1 will be an easy corollary of the following lemma.
Lemma 31. Let F be a finite field. Let M be an F-represented matroid such that c*d(M) =
d and c*d(M \S) < d for every non-empty subset S of elements of M. Then |M| ⩽f(|F|, d)
for some function f.
Proof. Let p := |F| and let csdtree
d
be the CMSO sentence from Lemma 28. Let N be the
number obtained by applying Theorem 29 to d + 3, m := dp + 2 and sentence csdtree
d
;
note that m and sentence csdtree
d
depend only on d and F. Assume for contradiction that
there is a F-represented matroid as in the assumptions of the lemma for which |M| > N.
By Corollary 15 there exists a matrix A of dual tree-depth at most d such that M(A) is
isomorphic to M. By Lemma 28 we have that T(A) |= csdtree
d
. We set T := T(A) for the
rest of the proof and we note that A = A(T) by Lemma 26. Since T has depth d + 3,
uses m labels, and has size more than N, by Theorem 29 there is a node v of T that has
nodes v1, . . . , vM among its children such that for the tree T ′ := T −(Tv1 ∪. . . ∪TvM)
we have T ′ |= csdtree
d
. This means that the matrix A(T ′) has contraction∗-depth d and
18

--- Page 19 ---

consequently c*d(M(A(T ′))) = d. To obtain a contradiction with the assumptions on M, it
remains to argue that M(A(T ′)) is a restriction of M. Let T ′′ be the tree obtained from T by
removing the leaves of trees Tv1, . . . , TvM marked with label LC. By repeated application of
Lemma 30 we have that M(A(T ′′)) is isomorphic to M(A(T ′)), and so c*d(M(A(T ′′))) = d.
Since A(T ′′) is obtained from A = A(T) by removing columns, M(A(T ′′)) is a restriction
of M with c*d(M(A(T ′′))) = d, a contradiction.
Proof of Theorem 1. Let M be a F-represented matroid with c*d(M) = d and c*d(M\e) < d
for every e ∈M. Let S be any non-empty set of elements of M. Consider any e ∈S. Then
M \ S is a restriction of M \ e. By our assumption on M we have that c*d(M \ e) < d.
Since contraction∗-depth is closed under deletion, we have c*d(M \ S) ≤c*d(M \ e) and so
c*d(M \ S) < d. Thus, by Lemma 31 we have |M| < f(|F|, d).
5
Deletion∗-depth
In this section we define a new depth parameter for representable matroids called the
deletion∗-depth, and investigate its properties.
Definition 32. Let M = M(A) be a represented matroid and let h be the number of rows
of A. The deletion∗-depth d*d(M) of M is defined recursively as:
• If r(M) = |M|, then d*d(M) = 0.
• If M is not connected, then the deletion∗-depth of M is the maximum deletion∗-depth
of a component of M.
• If M is connected, then d*d(M) = 1 + min d*d(M(A ⊕v⊤)), where the minimum is
taken over all v ∈Fh and ⊕is the operation that adds a row to A.
We claim that deletion∗-depth is a natural counterpart of contraction∗-depth. We base
this on the following:
• For every represented matroid M we have c*d(M) = d*d(M ∗).
This is the core
technical result of this section.
• Deletion∗-depth is functionally equivalent to deletion-depth. More precisely, we will
show that for any represented matroid we have d*d(M) ≤dd(M) ≤f(d*d(M)) for
some function f. This follows easily from the analogous result for cd and c*d and
duality (see Theorem 41).
Before we proceed with proving that c*d(M) = d*d(M ∗), let us briefly comment on the
relationship between the operation of deletion (that in the case of represented matroids
deletes a column of A) and operation ⊕used in the definition of deletion∗-depth. These two
operations are quite different, and it may seem counterintuitive that ⊕should generalize
the deletion operation (so that we get d*d(M) ≤dd(M)).
However, we can simulate
19

--- Page 20 ---

deletion of a column by ⊕as follows. Let u be the column of A that we wish to remove;
say u is the i-th column of A. Consider the vector ei ∈Fn that has 0 everywhere except
for the i-th position, where it has 1. It is easily seen that M(A ⊕ei) \ u′ is isomorphic
to M(A) \ u, where u′ is the i-th column of A ⊕ei. Moreover, note that even though the
column u′ is not removed from the matrix A ⊕ei, it is now disconnected from the rest of
the matroid, and so from this point on it will be treated separately by the definition of
deletion∗-depth.
5.1
Interlude – matroids via linear subspaces
In what follows, it will be convenient to think of F-representable matroids with ground set
of size n as of linear subspaces of Fn. To be more explicit, if A is a matrix representing a
matroid M, we will associate with M the linear subspace W = span(rows(A)) of Fn. This
correspondence between F-representable matroids with n elements and subspaces of Fn
works also in the other direction – to each subspace W of Fn we can meaningfully associate
matroid M(W), as we show below. We will need the following lemma.
Lemma 33. Let W be a subspace of Fn. Let v1, . . . , vk and u1, . . . , uk be two bases of W.
Let A be the matrix with rows v⊤
1 , . . . , vk⊤and A′ be the matrix with rows u1⊤, . . . , uk⊤.
Then M(A) is isomorphic to M(A′).
Proof. The transformation of A into A′ can be obtained by a sequence of elementary row
operations. It is easy to check that each elementary row operation preserves the matroid
structure.
Next, for any linear subspace W of Fn we define matroid M(W). The definition of
M(W) relies on using a basis of W, but by Lemma 33 the matroid M(W) itself is inde-
pendent of the choice of basis.
Definition 34. Let W be a linear subspace of Fn. We define the matroid M(W) as follows.
Let v1, . . . , vk be a basis of W. Let A be a matrix with rows v1⊤, . . . , vk⊤. Then M(W) :=
M(A).
Next we show that the dual of M(W) has a very natural representation in terms of
subspaces – it is represented by W ⊥, the subspace of Fn orthogonal to W.
Lemma 35. For any subspace W of Fn, we have M(W)∗∼= M(W ⊥)
Proof. Let w1, . . . , wk be a basis of W and let wk+1, . . . , wn be a basis of W ⊥. Let A be the
matrix with rows w1⊤, . . . , wk⊤and let B be a matrix with rows wk+1⊤, . . . , wn⊤. Then
we have M(W) = M(A) and our goal is to prove that M(W)∗= M(B). Note that since
the row rank of A is k, the column rank of A is also k, and hence r(M(W)) = r(M(A)) = k.
Also note that r(B) = n −k.
In what follows we will index columns of A and B by numbers from [n]. This sets up a
natural correspondence between the columns of A and B: the i-th column of A corresponds
20

--- Page 21 ---

to the i-th column of B. We will use the following notation: if U ⊂[n] and C is a matrix
that has as its rows transposed vectors from Fn, then by C[U] we mean the submatrix of
C given by the columns with indexes from U. In particular, if U = {i} is a singleton and
u ∈F n, then u⊤[{i}] is the i-th entry of u. In this case we will write u⊤[i] instead of
u⊤[{i}]
Let S ⊆[n] be a set such that the columns of A[S] form a basis of M(A) (equivalently,
a basis of Fk). Let ¯S be the complement of S in [n]. Our goal is to show that B[ ¯S] has
rank n −k; this will mean that the columns of B[ ¯S] form a basis of n M(W ⊥), which will
confirm that M(W)∗= M(B). Assume for contradiction that B[ ¯S] has rank strictly less
than n −k. Since B[ ¯S] has n −k rows, this means that the set of rows of B[ ¯S] is linearly
dependent. Therefore, there exists a vector u ∈Fn such that u⊤∈span(rows(B)) and
u⊤[ ¯S] = 0. Moreover, we know that u ̸= 0, since u⊤∈span(rows(B)) and B has rank
n −k and n −k rows. Therefore, there exists i ∈S such that u⊤[i] = α with α ̸= 0. Let
v⊤be a vector in span(rows(A)) such that v⊤[i] = 1, v⊤[j] = 0 for all j ∈S \ {i}, and
with arbitrary value v⊤[j′] for any j′ ∈¯S; such i ∈S exists since A[S] is of full rank. Then
we have that u · v = α. This is a contradiction, since from v ∈W and u ∈W ⊥we have
that u · v = 0.
For a subspace W of Fn, there are two very natural operations – ‘adding’ a vector
v ∈Fn to W (this can be realized as replacing W with span(W ∪v)) and ‘removing’ a
vector from W (this can be realized as replacing W by W ∩span(v)⊥). It can be easily
checked that these two operations are dual to each other – see also below. Later we will
see that if we consider the matroid M(W), these operations correspond to deletion∗and
contraction∗, respectively.
Definition 36 (Contraction• on a subspace). Let W be a subspace of Fn and v ∈Fn. We
define M(W)/•v = M(W ∩span(v)⊥).
Definition 37 (Deletion• on a subspace). Let W be a subspace of Fn and v ∈Fn. We
define M(W) \• v = M(span(W ∪{v})).
A simple formal argument shows that these two operations are dual to each other.
Theorem 38. Contraction• is dual to deletion•, i.e. for any matroid M(W) and any
vector v we have (M(W)/•v)∗= M(W)∗\• v.
Proof. We have
(W ∩span(v)⊥)⊥= span(W ⊥∪span(v)⊥⊥) = span(W ⊥∪span(v)) = span(W ⊥∪{v}).
Using this and Lemma 35 we have that
(M(W)/•v)∗= M(W ∩span(v)⊥)∗= M((W ∩span(v)⊥)⊥) = M(span(W ⊥∪{v})) =
= M(W ⊥) \• v = M(W)∗\• v
21

--- Page 22 ---

Let M = M(W) be a matroid given by a subspace W of Fn. We can now define two
auxiliary depth parameters c
•d(M) and d
•d(M) as follows. We set c
•d(M) := 0 if r(M) = 0.
If M is disconnected, then c
•d(M) is the maximum c
•d of any connected component of
M. If M is connected and r(M) > 0, then c
•d(M) is the minimum of c
•d(M/•v) over all
v ∈Fn. For d
•d we set d
•d(M) := 0 if r(M) = n. If M is disconnected, then d
•d(M) is the
maximum d
•d of any connected component of M. If M is connected and r(M) > 0, then
d
•d(M) is the minimum of d
•d(M \• v) over all v ∈Fn.
From Theorem 38 and Lemma 35 we easily get the following.
Lemma 39. For any matroid M = M(W), we have c
•d(M) = d
•d(M ∗) and c
•d(M ∗) =
d
•d(M).
For a represented matroid M = M(A) we set c
•d(M) := c
•d(span(rows(A))) and
d
•d(M) := d
•d(span(rows(A))). Then of course the results from Lemma 39 apply to repre-
sented matroids.
Before we proceed further, let us briefly comment on how the operations /• and \• are
realized in the case of represented matroids. If M = M(A) is a represented matroid, we
can obtain a representation for M \• v by simply adding the row v⊤to A to obtain matrix
A′. It is easily seen that M \• v = M(A′), because if W = span(rows(A)), then span(W ∪
{v}) = span(rows(A) ∪{v}) = span(rows(A′)). For the operation /•, we can obtain a
representation of M/•v as follows. We consider two cases. First, if v ∈span(rows(A)),
then we pick an orthogonal basis v1, . . . , vk of span(rows(A)) such that v1 = v and consider
matrix A′ consisting of rows v2, . . . , vk. Then one easily checks that for every w we have
w ∈span(rows(A)) ∩v⊥if and only if w ∈span(v2, . . . , vk), and so A′ is a representation
for M \• v. Second, if v ̸∈span(rows(A)), we can write v uniquely as v′ + v′′, where
v′ ∈span(rows(A)) and v′′ ∈span(rows(A))⊥.
The we have span(rows(A)) ∩v⊥=
span(rows(A)) ∩v′⊥(see Section 2.2) and we can proceed as before with v1 = v′.
5.2
Duality of deletion∗-depth and contraction∗-depth
In this section we prove Theorem 2, stating that for every represented matroid M = M(A)
we have c*d(M) = d*d(M ∗). To this end, we will show that for every represented matroid
we have c*d(M) = c
•d(M) and d*d(M) = d
•d(M). Since we know from the previous section
that c
•d(M) = d
•d(M ∗), we will then get c*d(M) = c
•d(M) = d
•d(M ∗) = d*d(M ∗), as
desired.
Next, we show that the contraction∗operation is the same as the newly defined op-
eration of contraction• on a subspace.
In the following lemma we will assume that a
represented matroid M we are working with is represented by a matrix of full rank. One
easily checks that that every representable matroid can be represented in this way.
Lemma 40. Let A ∈Fk×n be a matrix of rank k and W = span(rows(A)). Let M = M(A).
For every u ∈Fk there exists v ∈Fn such that M/u = M/•v and conversely, for every
v ∈Fn there exists u ∈Fk such that M/u = M/•v.
22

--- Page 23 ---

Proof. Fist note that it is enough to consider the situations when v ∈W. This is because
if v ̸∈W, then we can write v as v′ + v′′, where v′ ∈W and v′′ ∈W ⊥. But then we have
M/•v = M/•v′ (see the discussion at the end of the previous section) and so it is enough
to consider v′ ∈W instead of v.
We will now proceed with the proof of the lemma assuming that v ∈W. The proof
will be based on two observations.
Observation 1: Let T be a k × k matrix of rank k. Further, let u1 be the first column
of T and set A′ := T −1A.
Let S = {w1, . . . , wm} be a set of columns of A and let
S′ = {w′
1, . . . , w′
m} be the corresponding set of columns of A′ (so we have w′
i = T −1wi).
We claim that for every α1, . . . , αm ∈F we have
α1w1 + . . . + αmwm ∈span(u1) ⇐⇒α1w′
1 + . . . + αmw′
m ∈span(e1)
(3)
where e1 = (1, 0, . . . , 0) ∈Fk.
To see this, assume that α1w1 +. . .+αmwm = βu1 for some β ∈F. Then, by applying
T −1 to both sides of this equality we get α1w′
1+. . .+αmw′
m = βe1. For the other direction,
we assume that α1w′
1 + . . . + αmw′
m = βe1 for some β ∈F and apply T to both sides.
Then, analogously to the previous case, we get α1w1 + . . . + αmwm = βu1.
Observation 2: Let A′′ be the matrix obtained from A′ by removing the first row.
Let S′ = {w′
1, . . . , w′
m} be a set of columns of A′ and let S′′ = {w′′
1, . . . , wm′′} be the
corresponding set of columns of A′′. Then for every α1, . . . , αk ∈F we have that
α1w′
1 + . . . + αmw′
m ∈span(e1) ⇐⇒α1w′′
1 + . . . + αmw′′
m = 0
(4)
We now prove that for every u ∈Fk there exists a corresponding v ∈W as in the
statement of the lemma. Let u1, . . . , uk be a basis of Fk such that u1 = u. Let T be
the matrix with columns u1, . . . , uk. Set A′ := T −1A and let A′′ be obtained from A′
by removing its first row v1. Let S = {w1, . . . , wm} be any set of columns of A and
α1, . . . , αm ∈F arbitrary. Then by (3) and (4) we have that that
α1w1 + . . . + αmwm ∈span(u) ⇐⇒α1w′′
1 + . . . + αmw′′
m = 0
(5)
and so A′′ is a representation of M/u. We now argue that A′′ is also a representation of
M/•v for some v ∈W. By construction it is easy to see that span(rows(A′)) = W and
that A′ has k rows, so after removing its first row v1 we know that W ′′ = span(rows(A′′))
is a (k −1)-dimensional subspace of W. Hence we can pick v ∈W such that W ′′ =
W ∩span(v)⊥. Consequently, we have that M(A′′) = M(W ∩span(v)⊥) = M/•v. Thus,
we have M/u = M(A′′) = M/•v, as desired.
For the other direction, we prove that for every v ∈W there exists u ∈Fk as in the
statement of the lemma. Let w′
1, . . . , w′
k be an orthogonal basis of W with w′
1 = v. Let
A′ be the matrix with rows w′
1
⊤, . . . , w′
k
⊤and let A′′ be obtained from A′ by removing
its first row v⊤. Then we have that the rows of A′′ are a basis of W ∩span(v)⊥, and so
M(A′′) = M/•v. Since rk(A) = rk(A′), there exists an invertible matrix T such that A =
TA′, and so we have A′ = T −1A. Let u be the first column of T. Let S′′ = {w′′
1, . . . , w′′
m}
23

--- Page 24 ---

be a set of vectors of A′′ and let S = {w1, . . . , wm} be the corresponding set of columns
of A. Let α1, . . . , αk ∈F be arbitrary. By (4) and (3) we again get (5), and so A′′ is a
representation of M/u. Thus, we again have M/u = M(A′′) = M/•v, as desired.
As an immediate consequence of Lemma 40 we obtain that for every represented matroid
M we have c*d(M) = c
•d(M). This finishes the proof of Theorem 2.
5.3
Functional equivalence of deletion-depth and deletion∗-depth
Theorem 41. There exists a function f such that d*d(M) ⩽dd(M) ⩽f(d*d(M)) for any
represented matroid M.
Proof. We have
d*d(M) = c*d(M ∗) ≤cd(M ∗) = dd(M)
by Theorem 2, Theorem 19 and Lemma 12, respectively. By the same results (in reverse
order) we have
dd(M) = cd(M ∗) ≤f(c*d(M ∗)) = f(d*d(M ∗))
where f is the function from Theorem 19.
5.4
Minimal matroids of bounded deletion∗-depth
We now use Theorem 2 to prove Theorem 3.
Proof of Theorem 3. Let M be a matroid as in the assumptions of the theorem.
For
contradiction assume that |M| > f(|F|, d), where f is the function from Theorem 1. By
Theorem 2 we have that c*d(M ∗) = d. Since |M ∗| > f(|F|, d), there exists e ∈M such that
c*d(M ∗\ e) = d. By using Theorem 2 once more we then have d*d((M ∗\ e)∗) = d. Finally,
by the duality of deletion and contraction we have (M ∗\ e)∗= M ∗∗/e = M/e, and so we
get that d*d(M/e) = d, which is a contradiction with our assumption on M.
6
Minimal matroids for contraction-depth and deletion-
depth
The proof of Theorem 1 can be easily adapted to give a proof of Theorem 4.
Recall
that this theorem states that if M is an F-represented matroid such that cd(M) = d and
cd(M\S) < d for every non-empty subset S of elements of M, then |M| ⩽f(|F|, d) for some
function f. We can follow the same proof as in Theorem 1 all the way up to Lemma 31,
adjusting what is necessary. We only sketch the steps below, as they are analogous than
the proof of Theorem 1. We proceed as follows:
1. We start with a F-represented matroid M = M(A) with cd(M) = d, and for contra-
diction assume that |M| > N for a suitably chosen N depending on |F| and d.
24

--- Page 25 ---

2. We show that for every d there exists a CMSO formula cdd such that for every matrix
A we have that S(A) |= cdd if and only if cd(A) = d. This formula can be constructed
the same way as in the proof of Theorem 22, with the main difference being that we
do not need to use virtual columns (alternatively, we can require that each virtual
column corresponds to an actual column of A). Apart from this, we only need to
adjust the basis of the definition to reflect that a matroid with one element has
contraction-depth 1.
3. By Theorem 19 we have c*d(M) ≤g(cd(M)) for some function g, and by Corollary 15
we know that M can be represented by matrix A′ of dual treedepth at most g(cd(M)).
4. From this point on, we continue the same way as in Sections 4.1 and 4.2. The result
of this is a variant of Lemma 31 with c*d replaced by cd, which is precisely Theorem 4.
From Theorem 4 we easily obtain Theorem 5 by duality. Recall that this theorem states
that if M is an F-represented matroid such that dd(M) = d and dd(M/e) < d for every
e ∈M, then |M| ⩽f(|F|, d) for some function f.
Proof of Theorem 5. Let M be a matroid as in the assumptions of the theorem.
For
contradiction assume that |M| > f(|F|, d), where f is the function from Theorem 4. By
Lemma 12 we have that cd(M ∗) = d. Since |M ∗| > f(|F|, d), there exists a non-empty set
S of elements of M ∗cd(M ∗\S) = d. By using Lemma 12 again, we have dd((M ∗\S)∗) = d.
Finally, by the duality of deletion and contraction we have (M ∗\ S)∗= M ∗∗/S = M/S,
and so we obtain that dd(M/S) = d, which is a contradiction with our assumption on
M.
7
Further results
Let M be a matroid represented by a matrix A with m rows. Recall that we call a vector
v ∈Fm progresive if c*d(M/v) < c*d(M). Theorem 6 states that there exists a function
g : N × N →N with the following property: For every finite field F and d ∈N, if M is a
F-represented matroid with c*d(M) = d, then the number of progressive vectors for M is
at most g(|F|, d).
Proof of Theorem 6. Let A be the matrix representing M. By Theorem 1 M contains a
submatroid M ′ with c*d(M ′) = d and with at most f(|F|, d) elements. Let S be the set of
columns of A that correspond to the elements of M ′.
We claim that every progressive vector v for M is in span(S). Assume for contradiction
that this is not the case. Then the matroid M ′/v has contraction∗-depth d, because any
subset of S is dependent in M ′/v if and only if it is dependent in M ′. But c*d(M/v) < d
since v is progressive, and by Lemma 16 we have c*d((M ′/v) ≤c*d(M/v), so c*d((M ′/v) <
d, a contradiction.
Consequently, since every progressive vector is a linear combination of vectors from S,
it is determined by |S| coefficients from F. Therefore, there are at most F|S| such vectors.
Thus, we can set g(|F|, d) := |F|f(|F|,d), where f is the function from Theorem 1.
25

--- Page 26 ---

7.1
Results for Q-represented matroids
Recall that by Lemma 20 every Q-represented matroid M with c*d(M) = d and entry
complexity k can be Fq-represented with q ≤f(d, k) for some function f. Then we get the
following two results as an easy corollary of Theorem 1 and Theorem 6.
Theorem 42. Let M be an Q-represented matroid with entry complexity k such that
c*d(M) = d and c*d(M \ e) < d for every e ∈M. Then |M| ⩽f(d, k) for some func-
tion f.
Theorem 43. Let M be a Q-represented matroid with c*d(M) = d with entry complexity
k. Then the number of progressive vectors for M is at most g(d, k) for some function g.
References
[1] A. Bouland, A. Dawar, and E. Kopczynski. On tractable parameterizations of graph
isomorphism. In D. M. Thilikos and G. J. Woeginger, editors, Parameterized and
Exact Computation - 7th International Symposium, IPEC 2012, Ljubljana, Slovenia,
September 12-14, 2012. Proceedings, volume 7535 of Lecture Notes in Computer Sci-
ence, pages 218–230. Springer, 2012.
[2] M. Brianski, M. Koutecký, D. Král’, K. Pekárková, and F. Schröder. Characterization
of matrices with bounded graver bases and depth parameters and applications to
integer programming. Math. Program., 208(1):497–531, 2024.
[3] M. Brianski, D. Král, and A. Lamaison. Closure property of contraction-depth of
matroids. CoRR, abs/2311.01945, 2023.
[4] T. F. N. Chan, J. W. Cooper, M. Koutecký, D. Král’, and K. Pekárková. Matrices
of optimal tree-depth and row-invariant parameterized algorithm for integer program-
ming. In A. Czumaj, A. Dawar, and E. Merelli, editors, 47th International Colloquium
on Automata, Languages, and Programming (ICALP), LIPIcs vol. 168, volume 168 of
Leibniz International Proceedings in Informatics (LIPIcs), pages 26:1–26:19, Dagstuhl,
Germany, 2020. Schloss Dagstuhl–Leibniz-Zentrum für Informatik.
[5] T. F. N. Chan, J. W. Cooper, M. Koutecký, D. Král’, and K. Pekárková. Matrices of
optimal tree-depth and a row-invariant parameterized algorithm for integer program-
ming. SIAM Journal on Computing, 51(3):664–700, 2022.
[6] M. DeVos, O. Kwon, and S. Oum. Branch-depth: Generalizing tree-depth of graphs.
European Journal of Combinatorics, 90:103186, 2020.
[7] G. Ding and B. Oporowski. Some results on tree decomposition of graphs. J. Graph
Theory, 20(4):481–499, 1995.
26

--- Page 27 ---

[8] Z. Dvorák, A. C. Giannopoulou, and D. M. Thilikos. Forbidden graphs for tree-depth.
Eur. J. Comb., 33(5):969–979, 2012.
[9] J. Gajarský and P. Hlinený. Kernelizing MSO properties of trees of fixed height, and
some consequences. Log. Methods Comput. Sci., 11(1), 2015.
[10] J. Geelen, A. Gerards, N. Robertson, and G. Whittle. On the excluded minors for the
matroids of branch-width k. Journal of Combinatorial Theory Series B, 88(2):261 –
265, 2003.
[11] W. Hodges. A Shorter Model Theory. Cambridge University Press, 1997.
[12] M. M. Kanté, E. J. Kim, O. Kwon, and S. Oum. Obstructions for matroids of path-
width at most k and graphs of linear rank-width at most k. Journal of Combinatorial
Theory, Series B, 160:15–35, 2023.
[13] F. Kardoš, D. Král’, A. Liebenau, and L. Mach. First order convergence of matroids.
European Journal of Combinatorics, 59:150–168, 2017.
[14] J. Oxley. Matroid Theory. Oxford Graduate Texts in Mathematics. Oxford University
Press, 2011.
27

```
