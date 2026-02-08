---
title: "U-SafeBench - PDF Extract"
source_pdf: "2025-Various-U-SafeBench.pdf"
pages: 21
extracted_at: "2026-01-24T16:38:37.192460"
---

# PDF Extract: U-SafeBench

**Source PDF:** 2025-Various-U-SafeBench.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

THE GFB TREE AND TREE IMBALANCE INDICES
SEAN CLEARY∗, MAREIKE FISCHER†, AND KATHERINE ST. JOHN‡
Abstract. Tree balance plays an important role in various research areas in phylogenetics and computer science. Typically,
it is measured with the help of a balance index or imbalance index. There are more than 25 such indices available, recently
surveyed in a book by Fischer et al. They are used to rank rooted binary trees on a scale from the most balanced to the
least balanced. We show that a wide range of subtree-size based measures satisfying concavity and monotonicity conditions
are minimized by the complete or greedy-from-the-bottom (GFB) tree and maximized by the caterpillar tree, yielding an
infinitely large family of distinct new imbalance indices. Answering an open question from the literature, we show that one
such established measure, the bs-shape statistic, has the GFB tree as its unique minimizer. We also provide an alternative
characterization of GFB trees, showing that they are equivalent to complete trees, which arise in different contexts. We give
asymptotic bounds on the expected bs-shape statistic under the uniform and Yule-Harding distributions of trees, and answer
questions for the related Q-shape statistic as well.
1. Introduction. Trees are a canonical data structure, providing an efficient way to implement fun-
damental concepts such as dynamic sets as well as representing hierarchical and phylogenetic relationships
between data (see [3] and [15]). Much of the power of the tree data structure relies on well-distributed
branching that can yield tree height logarithmic in the total size of the tree, and result in efficient access,
assuming a reasonable balance. The balance, or lack thereof, often affects the running time of algorithms,
with many tree-based algorithms having significantly different times depending if they are very balanced (an
element in a balanced, binary search tree on n leaves can be found in O(log n) time) or very imbalanced
(the same search has O(n) time for the pectinate or caterpillar tree) [3]. There are many different measures
suggested to assess balance, this fundamental property of trees, surveyed in [6]. While similar in format,
these indices can yield quite different rankings of trees, as illustrated in Figure 1.1. This figure compares the
rankings of three different indices considered in the present manuscript (the bs-shape statistic, the Q-shape
statistic and the Sackin index) as well as two other well-known indices, namely the popular Colless and total
cophenetic indices for the case n = 10.
When the number of leaves, n, is a power of 2, with n = 2h for some h, all imbalance indices are minimal
for the fully balanced tree and maximal for the caterpillar tree. For trees which are neither the fully balanced
tree nor caterpillars, the values of each of these indices lie in the interval containing these extremes for that
imbalance index.
We show a general result that applies to a broad range of tree imbalance indices. If a tree imbalance
index function using subtree sizes satisfies some concavity and increasing conditions, the minimum value is
achieved by “greedy from the bottom” (GFB) trees, as named in [6]. We will show that these trees coincide
with trees termed “complete trees” [5], which have occurred in other contexts. The bs-shape statistic of Blum
and Fran¸cois [1] satisfies this property. The bs-shape statistic sums the logarithms of the subtree sizes across
the tree, so for a rooted binary tree T, the bs-shape statistic is P log(nv −1), where nv is the number of leaves
in the subtree rooted at the internal node v. Blum and Fran¸cois [1] note that once a normalizing constant has
been removed, the bs-shape statistic corresponds to the logarithm of the probability of a tree in the uniform or
equal rates model (ERM) for generating random trees (see [15, p. 29-30]), and provides a strong tool rejecting
the various tree models against the Yule-Harding or proportional to distinguished arrangements model (PDA)
(see [10] and Section 2 of the present manuscript concerning probabilistic models of phylogenetic trees).
Our findings answer the open question of which trees, among all rooted binary trees of size n, minimize
the bs-shape statistic as well as the question if there is an explicit formula for the minimum value of bs, both of
which were posed in [6]. We further analyze a related measure of tree balance, namely the Q-shape statistic,
described by Fill [5]. Motivated by building binary search trees from random permutations, it can be recast
as a close parallel to the bs-shape statistic. We discuss how his work shows the maximal and minimal tree
shapes for this statistic and the moments for it under the uniform distribution. We consider the distribution
of the relevant statistic under the Yule-Harding distribution as well. We describe many indices built from
concave functions of subtree sizes as imbalance indices, in that they have maximal values on caterpillar trees
∗Department of Mathematics, The City College of New York, NY 10031, USA (scleary@ccny.cuny.edu).
†University of Greifswald, Institute of Mathematics and Computer Science, Walther-Rathenau-Str. 47, 17487 Greifswald,
Germany (email@mareikefischer.de, mareike.fischer@uni-greifswald.de).
‡Department of Computer Science, Hunter College of CUNY and the Division of Invertebrate Zoology, American Museum
of Natural History, New York, NY (stjohn@hunter.cuny.edu).
1
arXiv:2502.12854v3  [q-bio.PE]  19 Aug 2025

--- Page 2 ---

2
CLEARY, FISCHER, AND ST. JOHN
Sackin index
sstatistic
Q statistic
Colless index
total coph. index
20
40
60
80
100
Fig. 1.1. The rankings of all 98 tree shapes of size 10 with respect to the Sackin index, the bs-shape statistic, the Q-shape
statistic, the Colless index, and the total cophenetic index (see [6] for a survey of indices). All indices rate the caterpillar
tree shown in blue as extremely unbalanced, and the indices rank trees of intermediate balance in different orders. The sets of
other minimal trees with respect to the other rankings contain the maximally balanced tree shown in green and/or the GFB
tree shown in red.
and minimal values on GFB trees, which necessarily include fully balanced trees when the size is a power of
two. We show that there are infinitely many distinct such indices.
The present manuscript is organized as follows: In Section 2, we present all definitions and notations
needed throughout the manuscript. In Section 3, we state some known results from the literature which we
will use to derive our results. Section 4 then contains all our results, which are structured as follows: Section
4.1 gives an overview of the minimizing properties of the GFB tree. The results of this subsection are used
in Section 4.2 to show that both the bs-shape statistic and the Q-shape statistic belong to an infinitely large
family of different imbalance indices. Section 4.3 then gives two explicit formulas for the minimum value
both for bs and Q, both of which are derived from the GFB tree. Finally, Section 4.4 derives some expected
values for the bs-shape statistic, which also answers open questions posed in [6]. We conclude with a brief
discussion in Section 5.
2. Definitions. We outline the terminology used, following the standard notions from [6, 11, 18].
Graph theoretical trees and phylogenetic trees. A rooted binary tree, or simply a tree, is a directed
graph T = (V (T), E(T)) with vertex set V (T) and edge set E(T), containing precisely one vertex of in-degree
0, the root (denoted by ρ), such that for every v ∈V (T) there exists a unique path from ρ to v, and such
that all vertices have out-degree 0 or 2. In particular, the edges are directed away from the root. Nodes
with out-degree 2 are internal nodes and nodes with out-degree 0 are leaf nodes or leaves. We use ˚V (T) (or
simply ˚V ) to denote the set of internal vertices of T and VL(T) to denote the set of leaves of T, respectively.
Tree balance is independent of any leaf labeling, but in phylogenetics, the leaf labeling plays an important
role and is used when considering evolutionary models. A rooted binary phylogenetic X-tree T (or simply
phylogenetic tree) is simply a tuple T = (T, ϕ), where T is a rooted binary tree and ϕ is a bijection from the
set of leaves VL(T) to X. The (unlabeled) tree T is often referred to as the topology or tree shape of T and
X is called the taxon set of T . We assume that the label sets are the numbers: X = {1, . . . , n}.
We consider two trees T and T ′ as equal if they are isomorphic; that is, if there exists a mapping
θ : V (T) →V (T ′) such that for all u, v ∈V (T) we have (u, v) ∈E(T) ⇔(θ(u), θ(v)) ∈E(T ′) and with
θ(ρ(T)) = ρ(T ′). In particular, θ is a graph isomorphism which preserves the root position. We use BT ∗
n to
denote the space (of isomorphism classes) of (rooted binary) trees with n leaves, which are unlabeled.
We use BT n to denote the space (of isomorphism classes) of rooted binary phylogenetic X-trees with
|X| = n where the leaves are labeled.
Moreover, we recall that |BT 1| = 1 and |BT n| = (2n −3)!! =
(2n −3)(2n −5) · · · 1 for n ≥2 ([15, Corollary 2.2.4]).

--- Page 3 ---

THE GFB TREE AND TREE IMBALANCE INDICES
3
(a) caterpillar
(b) greedy-from-the-bottom
(c) maximally-balanced
Fig. 2.1. Three tree shapes on 10 leaves: (a) a caterpillar with bs-shape of P9
i=2 log i = log(9!) ∼12.8, (b) a greedy-from-
the-bottom (GFB) tree with bs-shape of log(9·51·32) ∼6.0, and (c) a maximally-balanced tree with bs-shape of log(9·42·22) ∼6.4,
with the middle GFB tree (b) being the unique minimizer for the bs-shape statistic among all trees with 10 leaves.
Vertices and subtrees. We now define some properties of vertices and subtrees, which apply both for
trees as well as phylogenetic trees. Throughout, for a given tree T, we denote the number of leaves by n,
with n = |VL(T)|. In the special case of n = 1, the tree consists of only one vertex, which is at the same
time the root and its only leaf. The size of a tree T is defined as the number of leaf nodes and is sometimes
also indicated as |T|.
Whenever there is a directed path P from a vertex u to a vertex v in T, we call u an ancestor of v and
v a descendant of u. The depth δT (v) of a vertex v in T denotes the number of edges on the unique path P
from the root ρ of T to v. If P consists of a single edge, u is the parent of v and v is the child of u. If two
leaves u and v have the same parent w, u and v form a sibling pair or cherry, which we denote by [u, v].
Every internal vertex v of T induces a pending subtree Tv, that is, the subtree of T which has v as its
root and contains all descendants of v. The number of leaves of this subtree will be referred to as the size
of Tv and will be denoted by nv. Note that nρ = n. An internal vertex u with children v and w is called
balanced if |nv −nw| ≤1. Finally, for a (phylogenetic) tree T, we denote its standard decomposition into its
maximal pending subtrees (that is, the two subtrees rooted at the children of the root ρ of T) Ta and Tb
by T = (Ta, Tb). Note that the height h(T) of a tree T is defined as h(T) = maxv∈V (T ) δT (v); that is, the
height of a trees coincides with the maximum depth of its vertices.
Special trees. We describe some trees which play important roles in tree balance. The first tree is the
caterpillar tree, denoted by T cat
n
, which is a rooted binary tree with n leaves which either consists of only
one vertex or it contains precisely one cherry (see Figure 2.1(a)).
In considering a tree of size 2h, the fully balanced tree of height h, T fb
h , is the tree where every node has
two children and all leaves have depth exactly h. Note that for n ≥2 both maximal pending subtrees of a
fully balanced tree are again fully balanced trees, and we have T fb
h =

T fb
h−1, T fb
h−1

. The maximally balanced
(MB) tree with n leaves, denoted by T mb
n , is the unique rooted binary tree with n leaves in which all internal
vertices are balanced. Recursively, a rooted binary tree with n ≥2 leaves is maximally balanced if its root is
balanced and its two maximal pending subtrees are maximally balanced, with T mb
n
=

T mb
⌈n/2⌉, T mb
⌊n/2⌋

(see
Figure 2.1(c)).
The greedy from the bottom (GFB) tree for n leaves, denoted by T gfb
n , is a rooted binary tree with n leaves
that results from greedily clustering trees of minimal sizes from an initial forest in the following manner. We
start with a forest of n trees each consisting of a single vertex and proceed by successively joining two of the
smallest remaining trees in the forest until the forest is resolved into a single tree, with the resulting tree of
the shape depicted in Figure 2.1(b). Coronado et al. describe this construction in [4, Algorithm 2].
The complete tree (as defined in Fill [5]) for n leaves, denoted by T c
n, is a rooted binary tree with n
leaves that results from creating the fully balanced tree of size 2⌊log2(n)⌋, the largest fully balanced tree with
n leaves or fewer, ordering the leaves from the left to the right and then attaching sibling pairs on the leaves
from left to right until a total of n leaves are obtained. We will show below that the complete tree coincides
with the GFB tree for all sizes, cf. Lemma 4.17. In order to simplify notation, throughout we use the
shorthand log instead of log2 whenever we refer to a base-2 logarithm.
Note that if n = 2h, we have T gfb
n
= T fb
h = T mb
n . The latter equality follows from the fact that in the

--- Page 4 ---

4
CLEARY, FISCHER, AND ST. JOHN
case where the number of leaves is a power of 2, T fb
h is the unique tree all of whose internal vertices have a
balance value of zero. The first equality holds, because if n = 2h, n mod 2i ≡0 for all i = 0, . . . , h −1 and
during the greedy clustering procedure, every tree with 2i leaves clusters with another tree of 2i leaves for
all i = 0, . . . , h −1. This process continues until the single remaining tree is the fully-balanced tree.
Tree shape statistics and (im)balance indices. We focus on tree imbalance indices. Following [6],
we call a function t : BT ∗
n →R a tree shape statistic (TSS) if t(T) depends only on the shape of T and not
on the labeling of vertices or the lengths of edges. Such a tree shape statistic t is called an imbalance index
if
• the caterpillar tree T cat
n
is the unique tree maximizing t on BT ∗
n for all n ≥1, and
• the fully balanced tree T fb
h is the unique tree minimizing t on BT ∗
n for all n = 2h for natural h.
The choice of base for the logarithm only affects the following indices by a multiplicative factor, and so
we presume base 2 for all evaluations below. We first focus on several well-known and frequently used tree
imbalance indices that are defined in terms of leaf counts of subtrees:
Definition 2.1. Let T ∈BT ∗
n.
• Sackin index (cf. [7, 6, 16]): S(T) =
P
v∈˚
V (T )
nv.
• bs-shape statistic [1, 6]: bs(T) :=
P
v∈˚
V (T )
log(nv −1) = log
 
Q
v∈˚
V (T )
(nv −1)
!
.
• Q-shape statistic (related to Fill [5]): Q(T) :=
P
v∈˚
V (T )
log(nv) = log
 
Q
v∈˚
V (T )
nv
!
.
Note that the logarithm base was originally not stated [1], however, it is common to use base 2 in binary
(phylogenetic) trees, and we follow this convention here just as the authors of [6]. In fact, we only consider
logarithms of base 2 here; this is not limited to Definition 2.1.
Moreover, while we are mainly concerned with two imbalance indices, the bs-shape statistic and the Q-
shape statistic, we also consider broader families containing both indices. The Q-shape statistic is related
to measures introduced by Fill [5] and differs from the bs-shape statistic by a difference of one before taking
the logarithms for each term in the product. Despite the similarity, the statistics yield different rankings
(see Figures 1.1 and 4.4). Note that Fill [5] uses Q(T) for the reciprocal of the quantity of which we are
taking the logarithm, and defines Ln = −ln(Q(T)) for the negative of its natural logarithm. Ln(T) differs
from how we choose to define the Q-shape statistic here in the base of logarithm, but we proceed as above
to make the Q-shape statistic more closely parallel to the bs-shape statistic. Fill [5] shows that the complete
(GFB) tree minimizes the Q-shape statistic and the caterpillar tree maximizes it, and further computes the
moments under the uniform distribution as well as the random permutation model. King and Rosenberg
[11] employ a parallel structure to Fill’s methods for similar results on the Sackin index.
Probabilistic models of phylogenetic trees. We consider two popular models of evolution: the
Yule-Harding and the uniform models. The Yule-Harding model is a pure birth process in which species are
born but do not go extinct. It is a forward process generating a tree T as follows. The process starts with
a single vertex and, at each step, chooses a leaf uniformly at random from those present and subsequently
replaces that leaf by a cherry. As soon as the desired number n of leaves is reached, leaf labels X = {1, . . . , n}
are assigned uniformly at random to the leaves. The probability PY,n(T) of generating a phylogenetic X-tree
T = (T, ϕ) under the Yule-Harding model is then given by Steel [18, Proposition 3.2]:
PY,n(T) = 2n−1
n!
·
Y
v∈˚
V (T )
1
nv −1.
(2.1)
The uniform model selects a phylogenetic X-tree uniformly at random from the set of all possible
phylogenetic trees ([14]). As |BT n| = (2n −3)!! for every n ≥1 (with the convention that (−1)!! = 1; see,
for instance, [15, Corollary 2.2.4]), the probability PU,n(T) of generating a phylogenetic X-tree T under the

--- Page 5 ---

THE GFB TREE AND TREE IMBALANCE INDICES
5
uniform model is thus given by
PU,n(T) =
1
(2n −3)!!.
(2.2)
3. Prior results. In order to investigate the GFB tree and its relevance for the bs-shape statistic more
deeply, we use the following earlier results.
Lemma 3.1 (Lemma 5 in [4]).
If T = (Ta, Tb) is a GFB tree, then Ta and Tb are also GFB trees.
Note that recursively applying Lemma 3.1 to the maximum pending subtrees of T and again their
maximum pending subtrees and so forth, we easily derive the following corollary.
Corollary 3.2. If T is a GFB tree and v is a vertex of T inducing the pending subtree Tv, then Tv is
also a GFB tree.
The following proposition, which has been adapted from Proposition 5 in [4], characterizes the sizes of
the maximal pending subtrees of GFB trees.
Proposition 3.3 (adapted from Proposition 5 in [4]). For n ≥2, we let T gfb
n
= (Ta, Tb), where na and
nb denote the sizes of Ta and Tb, respectively. Let ℓn = ⌊log(n)⌋. Then, we have:
1. If 2ℓn ≤n ≤3 · 2ℓn−1, then na = n −2ℓn−1, nb = 2ℓn−1 and Tb = T fb
ℓn−1.
2. If 3 · 2ℓn−1 ≤n < 2ℓn+1 −1, then na = 2ℓn, nb = n −2ℓn and Ta = T fb
ℓn .
We mainly work with kn = ⌈log(n)⌉rather than ℓn = ⌊log(n)⌋to simplify some proofs later.
Corollary 3.4. For n ≥2, we let T gfb
n
= (Ta, Tb), where na and nb denote the sizes of Ta and Tb,
respectively. Let kn = ⌈log(n)⌉. Then, we have:
1. If 2kn−1 < n ≤3 · 2kn−2, then na = n −2kn−2, nb = 2kn−2 and Tb = T fb
kn−2.
2. If 3 · 2kn−2 ≤n ≤2kn, then na = 2kn−1, nb = n −2kn−1 and Ta = T fb
kn−1.
Proof. For all cases in which n is not a power of 2, we have kn = ℓn + 1. For these cases, substituting
ℓn in Proposition 3.3 by kn −1 directly leads to the required claims.
So it only remains to consider the case in which n is a power of 2.
Note that in this case, kn =
⌈log(n)⌉= ⌊log(n)⌋= ℓn, so we have n = 2ℓn = 2kn. Proposition 3.3 covers this case in Case 1, which says
that na = n −2ℓn−1 and nb = 2ℓn−1. Using na + nb = n and kn = ℓn and n = 2kn in this case, we get:
na = n −2ℓn−1 = 2kn −2kn−1 = 2kn−1 and nb = 2ℓn−1 = 2kn−1.
Corollary 3.4 covers this case in Case 2, which implies that na = 2kn−1 and nb = 2ℓn−1 = 2kn−1.
4. Results. We show that the GFB tree plays a fundamental role for the bs-shape statistic, even more
so than it does for other balance indices like the Sackin index, for which it is known to be contained in the
set of minimal trees (cf. [7, 6]). Note that the GFB tree plays a similar role for other imbalance indices like
the well-known Colless index, for which it is also known to be minimal ([4, 6]). Figure 1.1 depicts the role of
the GFB tree for various indices. Notably, there are indices like the so-called total cophenetic index, which
do not assume their minimal values at the GFB tree, but at the MB tree instead [12], cf. Figure 1.1.
We now start to investigate the GFB tree further.
4.1. Minimizing properties of the GFB tree. The aim of this section is to show that T gfb
n
is the
unique minimizer of all functions of the form Φf, which we define for any rooted binary tree T as follows:
Φf(T) =
X
v∈˚
V (T )
f(nv),
where f is any strictly monotonically increasing and strictly concave function. Moreover, we will show that
this implies that the GFB tree is the unique minimizer of the product function, which we define as follows:
πc(T) =
Y
v∈˚
V (T )
(nv + c),
where T is a rooted binary tree and c ∈R>−2 is a constant. Note that the choice of c > −2 guarantees that
nv +c > 0 for all v ∈˚V (T) (as the smallest pending subtree size is nv = 2, when v is the parent of a cherry).

--- Page 6 ---

6
CLEARY, FISCHER, AND ST. JOHN
The fact that all factors of the product function are strictly larger than 0 leads to meaningful properties of
the product including the existence of the logarithm of the product function.
In Section 4.2, we will subsequently show that the above minimizing properties have significant implica-
tions on tree balance, as they lead to two new families of tree (im)balance indices, one of which can be shown
to be a subfamily of the other one. Moreover, our results will lead to answers to open questions concerning
existing imbalance indices.
We start with the following theorem, parts of which are based on the ideas of [8, Theorem 4].
Theorem 4.1. Let n ∈N with n ≥2 and let f : R≥2 →R a strictly monotonically increasing and
strictly concave function.
That is, we have f(n1) > f(n2) if and only if n1 > n2, and we also have
f(λx + (1 −λ)y) > λf(x) + (1 −λ)f(y) for all λ ∈(0, 1) and all x, y ∈R≥2 with x ̸= y. We consider
Φf(T) =
P
v∈˚
V (T )
f(nv). Then, T gfb
n
is the unique tree in BT ∗
n minimizing Φf.
Proof. Towards a contradiction, we assume n is the smallest number where the minimizing tree is not
the GFB tree. We let T be a rooted binary tree with n leaves minimizing Φf, such that T is not a GFB
tree. Since there is only one tree when n = 1, we can assume n > 1.
By Lemma 3.1, the subtrees of a GFB tree are also GFB trees. T is by assumption not a GFB tree, so
there will be at least two pending subtrees of T that would form a GFB tree but do not have a common parent
in T. This is due to the fact that T, just like every rooted binary tree, can be obtained from clustering,
starting with a forest of one-leaf trees and clustering two trees at a time until a single tree is obtained.
We do this to build T by using the two smallest available trees at any point in time (just as in the GFB
construction), until no such further clustering is possible. So there must be two trees which are present both
in T and T gfb
n , that have a common parent in T gfb
n
but do not in T. Let Ta and Tb be the smallest such
subtrees of T.
We note that as all previous trees of T gfb
n
were also formed when building T, only two situations are
possible:
1. One of the two trees Ta, Tb, say Ta, is contained in T as a sibling tree to some tree Tc, and the other
one, say Tb, is a sibling to a subtree of T containing the first tree, say Ta. This situation is depicted
in Figure 4.1 at the left-hand side.
2. The tree Ta is a sibling to some tree Tc not containing Tb, and Tb is a sibling to some tree Td not
containing Ta. This situation is depicted in Figure 4.1 at the right-hand side.
We now consider these two cases separately.
1. We start with Case 1 as depicted in Figure 4.1. We construct a new tree T ′ as follows: T ′ is like
T, but the subtrees Tb and Tc are interchanged. We let P be the path highlighted in Figure 4.1,
where P is the path containing all vertices v for which we have nv(T) ̸= nv(T ′), where nv(T) and
nv(T ′) denote the induced subtree sizes of v in T and T ′, respectively. We note that for all vertices
v ∈˚V (T)\P we have nv(T) = nv(T ′), as these vertices’ subtree sizes are not affected by the subtree
swap of Tb and Tc. This reasoning leads to the following observation:
Φf(T ′) = Φf(T) −
X
v∈P
(f(nv(T)) −f(nv(T) −nc + nb)) ,
(4.1)
where nb and nc are the subtree sizes of Tb and Tc, respectively.
Now, we know that nc > nb, because if nc < nb, the GFB algorithm would not have merged Ta and
Tb (but Ta and Tc instead). Moreover, if we had nb = nc, then Tb and Tc would be isomorphic, as
all steps prior to merging Ta and Tb worked in T in the same way as in T gfb
n
(by choice of (Ta, Tb)
as the minimal subtree of T gfb
n
which could not be formed to build T).
In this case, however, (Ta, Tb) would be isomorphic to (Ta, Tc) and thus be contained in T, a con-
tradiction to our choice of Ta and Tb. Thus, nc > nb and therefore nv(T) −nc + nb < nv(T) for all
v ∈P. As f is strictly increasing, this implies that f(nv(T)) > f(nv(T) −nc + nb). With Equation
(4.1), this directly leads to:

--- Page 7 ---

THE GFB TREE AND TREE IMBALANCE INDICES
7
ρab
P
Ta
Tc
T1
Tk
Tb
Case 1
ρab
P1
Ta
Tc
T1
Tk
ˆTl
P2
ˆT1
Tb
Td
Case 2
Fig. 4.1. Top: Case 1 of the proof of Theorem 4.1. Here, Ta is a sibling of Tc in T, with size strictly larger than that
of Tb, and Tb is a sibling of a subtree of T containing Ta. The highlighted path P contains all vertices whose induced subtree
sizes change when subtrees Tb and Tc are swapped. The dotted edges and subtrees may or may not exist in T. Bottom: Case
2 of the proof of Theorem 4.1. Here, Ta is a sibling of Tc in T, with size strictly larger than that of Tb, but not containing Tb.
Similarly, Tb is a sibling of Td in T, with size strictly larger than that of Ta, but not containing Ta. The highlighted paths P1
and P2 contain all vertices whose induced subtree sizes change when Tb and Tc or Ta and Td are swapped. The dotted edges
and subtrees may or may not exist in T.
Φf(T ′) = Φf(T) −
X
v∈P
(f(nv(T)) −f(nv(T) −nc + nb))
|
{z
}
>0
< Φf(T).
(4.2)
Thus, we have Φf(T ′) < Φf(T), which contradicts the minimality of T and thus completes this case.
2. Next, we let T be as depicted as Case 2 in Figure 4.1, with Ta a sibling to some tree Tc not containing
Tb, and Tb a sibling to some tree Td not containing Ta. We now construct two trees T ′ and T ′′ as
follows: T ′ is like T, but subtrees Tb and Tc are swapped. Similarly, T ′′ is like T, but subtrees Ta
and Td are swapped. We denote by na, nb, nc and nd the number of leaves in Ta, Tb, Tc and Td,

--- Page 8 ---

8
CLEARY, FISCHER, AND ST. JOHN
respectively. As in the first case, we necessarily have nd > na and nc > nb by choice of Ta and Tb.
We let T1, . . . , Tk be the subtrees pending on path P1 as depicted in Figure 4.1 if these subtrees
exist in T. Similarly, we let bT1, . . . , bTl be the subtrees pending on path P2 as depicted in Figure
4.1 if these subtrees exist in T. We denote by ni the number of leaves in Ti for i = 1, , . . . , k, and
by bni the number of leaves in bTi for i = 1, . . . , l. Moreover, we define n0 = bn0 = 0. With these
definitions, we can now introduce variables ti and bti defined as follows: ti =
iP
j=0
nj for i = 0, . . . , k
and bti =
iP
j=0
bnj for i = 0, . . . , l.
• We enumerate the vertices of P1 such that v0 is the parent of Ta and Tc in T and such that vi
is the parent of vi−1 for each i = 1, . . . , k if k > 0; that is, if trees T1, . . . , Tk exist in T. Then,
for the subtree sizes nvi we derive:
– nvi(T) = na + nc + ti for i = 0, . . . , k,
– nvi(T ′) = na + nb + ti for i = 0, . . . , k,
– nvi(T ′′) = nc + nd + ti for i = 0, . . . , k.
• Similarly, we enumerate the vertices of P2 such that w0 is the parent of Tb and Td in T and
such that wi is the parent of wi−1 for each i = 1, . . . , l if l > 0; that is, if trees bT1, . . . , bTl exist
in T. Then, for the subtree sizes nwi we derive:
– nwi(T) = nb + nd + bti for i = 0, . . . , l,
– nwi(T ′) = nc + nd + bti for i = 0, . . . , l,
– nwi(T ′′) = na + nb + bti for i = 0, . . . , l.
We now set λ =
nd−na
nd−na+nc−nb . Since we have nd > na and nc > nb, we have λ ∈(0, 1). We now
show that this choice of λ has two additional properties, which will be useful regarding the concavity
of f:
• We have nb + nd + bti = λ(nc + nd + bti) + (1 −λ)(na + nb + bti) for all i = 0, . . . , l:
λ(nc + nd + bti) + (1 −λ)(na + nb + bti)
= λnc + λnd −λna −λnb + na + nb + bti
= na + nb + bti + λ(nd −na + nc −nb)
= na + nb + bti +
nd −na
nd −na + nc −nb
(nd −na + nc −nb)
= na + nb + bti + nd −na
= nb + nd + bti.
• Analogously, we have na + nc + ti = λ(na + nb + ti) + (1 −λ)(nc + nd + ti) for all i = 0, . . . , k.
The first one of these two points above shows that there exists λ ∈[0, 1] with nb + nd + bti =
λ(nc + nd + bti) + (1 −λ)(na + nb + bti), so that we have for all i = 0, . . . , l:
f(nb + nd + bti) = f(λ(nc + nd + bti) + (1 −λ)(na + nb + bti))
(4.3)
> λf(nc + nd + bti) + (1 −λ)f(na + nb + bti),
where the inequality holds due to the strict concavity of f. Analogously, by the second point, we
have for all i = 0, . . . , k:
f(na + nc + ti) = f(λ(na + nb + ti) + (1 −λ)(nc + nd + ti))
(4.4)
> λf(na + nb + ti) + (1 −λ)f(nc + nd + ti).
Now we are finally in a position to derive a contradiction, namely by investigating the term Φf(T)−
λΦf(T ′) −(1 −λ)Φf(T ′′) in two different ways.

--- Page 9 ---

THE GFB TREE AND TREE IMBALANCE INDICES
9
(a) By assumption, T is a minimizer of Φf, so we have that Φf(T ′) ≥Φf(T) as well as Φf(T ′′) ≥
Φf(T). Thus:
Φf(T) −λΦf(T ′) −(1 −λ)Φf(T ′′) ≤Φf(T) −λΦf(T) −(1 −λ)Φf(T) = 0.
(4.5)
(b) We now split the sum of Φf(T) =
P
v∈˚
V (T )
f(nv) into three partial sums, namely the inner
vertices belonging to P1, the ones belonging to P2 and the ones belonging to neither one of the
paths. Note that as all vertices that are not contained in any one of the paths are not affected
by the swaps leading from T to T ′ or T ′′, respectively, the last sum is the same for Φf(T),
Φf(T ′) and Φf(T ′′). From our above observations concerning the subtree sizes nvi of P1 and
nwi of P2, we derive:
Φf(T) −λΦf(T ′) −(1 −λ)Φf(T ′′)
(4.6)
=
X
v∈P1
f(nv(T)) +
X
v∈P2
f(nv(T)) +
X
v∈˚
V \{P1,P2}
f(nv(T))
−λ ·
X
v∈P1
f(nv(T ′)) −λ ·
X
v∈P2
f(nv(T ′))
−λ ·
X
v∈˚
V \{P1,P2}
f(nv(T ′)) −(1 −λ) ·
X
v∈P1
f(nv(T ′′))
−(1 −λ) ·
X
v∈P2
f(nv(T ′′))
−(1 −λ) ·
X
v∈˚
V \{P1,P2}
f(nv(T ′′))
=
k
X
i=0
(f(na + nc + ti) −λf(na + nb + ti) −(1 −λ)f(nc + nd + ti))
|
{z
}
>0 by Eq. (4.4)
+
l
X
i=0
 f(nb + nd + bti) −λf(nc + nd + bti) −(1 −λ)f(na + nb + bti)

|
{z
}
>0 by Eq. (4.3)
> 0.
(4.7)
The obvious contradiction between Inequalities (4.5), which states that Φf(T)−λΦf(T ′)−(1−
λ)Φf(T ′′) ≤0 and (4.7), which states that Φf(T) −λΦf(T ′) −(1 −λ)Φf(T ′′) > 0, shows that
our assumption concerning the existence of T must have been wrong. In fact, this contradiction
shows that at least one of the two trees T ′ and T ′′ must have a lower Φf value than T. This
completes the proof and thus shows that T gfb
n
is the unique tree minimizing Φf.
Before we investigate the implications of Theorem 4.1 on imbalance indices, we derive the following
corollary.
Corollary 4.2. Let n ∈N, n ≥2 and let c ∈R with c > −2. Let f : R≥2 →R be a strictly increasing
function. Then, we have that T gfb
n
is the unique minimizer of f(πc(T)) among all rooted binary trees T with
n leaves, where πc(T) =
Q
v∈˚
V (T )
(nv + c). In particular, this holds for the identity function, f(x) = x for all
x ∈R≥2.
Proof. We start with considering the product function πc. We let c and n be as described in the corollary.
We have nv ≥2 for all inner nodes v of a rooted binary tree T, as the smallest possible subtree size is 2
(which is the case in which v is the parent of a cherry). Thus, we have nv + c > 0 for all v ∈˚V , as c > −2

--- Page 10 ---

10
CLEARY, FISCHER, AND ST. JOHN
by assumption. This, however, means that all factors in πc(T) are strictly larger than 0, which shows that
πc(T) > 0. This, in turn, means that log(πc(T)) is defined.
Now we consider this term further:
log(πc(T)) = log

Y
v∈˚
V (T )
(nv + c)

=
X
v∈˚
V (T )
log(nv + c).
As the logarithm is strictly concave and strictly monotonically increasing, we know by Theorem 4.1 that
the latter sum is uniquely minimized by T gfb
n
. Thus, the same applies to log(πc(T)). However, by the strict
monotonicity of log, the minimum of log(πc(T)) is reached precisely when the minimum of πc(T) is reached,
which shows that T gfb
n
is also the unique tree minimizing πc(T).
Now, for any strictly increasing function f : R≥2 →R, we have that T gfb
n
is also the unique minimizer
of f(πc(T)) due to the monotonicity of f. This completes the proof.
4.2. Implications of the extremal GFB properties on measures of tree balance. The main aim
of this section is two-fold: First, we want to show that both functions Φf and πc as defined in the previous
section form families of imbalance indices for certain choices of f and c, respectively. We will continue to
show that the imbalance index family based on the product function and a constant c is merely a subfamily
of the imbalance index family based on strictly increasing and strictly concave functions f.
Then, we want to use our findings to characterize all trees minimizing the bs-shape and Q-shape statistics,
thus answering several open questions from [6].
However, in order to show that a function is an imbalance index, analyzing the minimum as in the
previous section is not sufficient. Instead, we also need to investigate the caterpillar in order to investigate
the maximum. We start with Φf. Note that the following theorem can already be found in [9, Theorem 4.7],
albeit with a different proof.
Theorem 4.3. Let n ∈N, n ≥2 and let f : R≥2 →R be strictly monotonically increasing, with
f(n1) > f(n2) if and only if n1 > n2. We consider Φf(T) =
P
v∈˚
V (T )
f(nv). Then, T cat
n
is the unique tree
maximizing Φf.
Proof. We prove the statement by contradiction. We suppose that there is a non-caterpillar tree T
maximizing Φf. We choose the smallest possible n for which such a tree T with n leaves exists. Thus, for all
numbers smaller than n, the unique maximizer of Φf is the caterpillar. In particular, this shows that n ≥4,
because for any value smaller than 4, there is only one rooted binary tree.
We let T = (T1, T2) be the standard decomposition of T. Then, Φf(T) = Φf(T1)+Φf(T2)+f(n), where
the last summand f(n) results from the root ρ of T. This equality shows that T can only maximize Φf
among all trees with n leaves if T1 and T2 maximize Φf among all trees with n1 and n2 leaves, respectively,
where n1 is the number of leaves of T1 and n2 is the number of leaves of T2. Thus, as we chose T to be
a counterexample of minimal size concerning the statement of the theorem, we know by assumption that
T1 and T2 must be caterpillars.
Note that this implies that n1 ≥2 and n2 ≥2 (which is possible as
n1 + n2 = n ≥4), because if we had n2 = 1 and T1 is a caterpillar, then T would be a caterpillar also. The
same would happen if n1 = 1.
Thus, we know that, as T1 and T2 are caterpillars with at least two leaves each, each of them has precisely
one cherry. Let [a1, b1] denote the cherry of T1 and [a2, b2] denote the cherry of T2. The parents of [a1, b1]
and [a2, b2] are denoted by v0 and w0, respectively. Note that on the path from v0 to the root ρ of T, there
might be more vertices v1, . . . , vk, all of which – if they exist – are adjacent to a leaf as T1 is a caterpillar.
Analogously, there might be more vertices w1, . . . , wl on the path from w0 to ρ, all of which – if they exist –
are adjacent to a leaf as T2 is a caterpillar. Note that this means that T looks as depicted on the left-hand
side of Figure 4.2. We denote the leaves adjacent to vi with xi for i = 1, . . . , k (if they exist), and the leaves
adjacent to wi with yi for i = 1, . . . , l (if they exist).
Now we assume without loss of generality that k ≥l and consider wl (note that l might be 0) and
consider a leaf zl adjacent to wl (note that zl might be either a2 or b2 if l = 0; otherwise we have zl = yl).
We now create a tree T ′ by deleting edge (wl, zl), subdividing edge (ρ, vk) by introducing a new degree-2
vertex vk+1 and then adding a new edge (vk+1, zl) and suppressing wl. The resulting tree T ′ is depicted on
the right-hand side of Figure 4.2. Note that between T and T ′, all subtree sizes are equal except for that of

--- Page 11 ---

THE GFB TREE AND TREE IMBALANCE INDICES
11
ρ
vk
v1
v0
a1
b1
x1
xk
wl
yl
wl−1
yl−1
w1
y1 w0
a2 b2
ρ
vk+1
vk
v1
v0
a1 b1
x1
xk
yl
wl−1
yl−1
w1
y1
w0
a2
b2
T
T ′
Fig. 4.2. Trees T and T ′ as described in the proof of Theorem 4.3. The only differences between the subtree sizes are at
nodes wl and vk+1, highlighted with a box.
vk+1, which equals k +3 in T ′ as above but does not exist in T, and that of wl, which equals l +2 (stemming
from the fact that wl is ancestral to a2, b2 and y1, . . . , yl if the latter leaves exist). Thus, we derive for
Φf(T ′):
Φf(T ′) = Φf(T) + f(k + 3) −f(l + 2),
which immediately shows that Φf(T ′) > Φf(T), as we assumed that k ≥l. This contradicts the maximality
of T and thus completes the proof.
The maximality of the caterpillar now immediately leads to the following corollary, which shows that
each Φf is indeed an imbalance index.
Corollary 4.4. Let n ∈N, n ≥2 and let f : R≥2 →R be a strictly increasing and strictly concave
function. Then, Φf is an imbalance index. Moreover, the GFB tree T gfb
n
is the only minimizer of this
function in BT ∗
n.
Proof. This is a direct consequence of the definition of an imbalance index in combination with Theorems
4.1 and 4.3 and the fact that T fb
h
= T gfb
n
if n = 2h.
We now use Corollary 4.4 to answer several open problems from the literature, most notably from [6].
Note that while it is already known that the bs-shape statistic is an imbalance index [6], this has not been
formally proven yet for the Q-shape statistic. However, while for the bs-shape statistic the minima have
already been known for the cases in which n = 2h (it is T fb
n
as bs is an imbalance index), it has not been
known what the minimal trees are in cases in which n is not a power of two [6]. The following corollary fully
characterizes these minima both for bs and Q by showing that in both cases, T gfb
n
is the unique minimizer.
Corollary 4.5. The bs-shape statistic and the Q-shape statistic are both tree imbalance indices with the
property that the GFB tree T gfb
n
is their only minimizer in BT ∗
n for any value of n ∈N, n ≥2.
Proof. Let n ∈N, n ≥2. We define fbs(i) = log(i −1) and fQ(i) = log(i) for i ∈R≥2. Note that fbs and
fQ are both strictly increasing and strictly concave. Now, by definition of bs and Q, we have for all rooted
binary trees T with n leaves:
Φfbs(T ) =
X
v∈˚
V (T )
fbs(nv) =
X
v∈˚
V (T )
log(nv −1) = bs(T),
as well as
ΦfQ(T ) =
X
v∈˚
V (T )
fQ(nv) =
X
v∈˚
V (T )
log(nv) = Q(T).
Applying Corollary 4.4 completes the proof.

--- Page 12 ---

12
CLEARY, FISCHER, AND ST. JOHN
So, we now know that for all values of n, there is only one tree minimizing the bs-shape statistic (thus
answering the question concerning the number of minima posed in [6, Chapter 9]), and we have fully char-
acterized this unique minimum as T gfb
n
. In Section 4.3, we will also deliver explicit formulas to calculate the
minimal value of bs for all n.
We now turn our attention to the product function to show that functions of this type also form a family
of tree imbalance indices. We again start with considering the caterpillar.
Corollary 4.6. Let n ∈N, n ≥2 and let c ∈R, c > −2. Then, we have that T cat
n
is the unique
maximizer of πc(T) in BT ∗
n, where πc(T) =
Q
v∈˚
V (T )
(nv + c).
Proof. Let c ∈R, c > −2. We can set fc(i) = log(i + c) for i ∈R≥2. Then, fc is both strictly concave
and strictly increasing (as the logarithm with base 2 has these properties). With this function fc, we have
for any rooted binary tree T with n leaves:
Φfc(T) =
X
v∈˚
V (T )
fc(nv) =
X
v∈˚
V (T )
log(nv + c) = log

Y
v∈˚
V (T )
(nv + c)

= log(πc(T)).
(4.8)
By Theorem 4.3 we know that T cat
n
is the unique maximizer of Φfc, and, thus, we can conclude that
log(πc(T cat
n )) > log(πc(T)) for all rooted binary trees T with n leaves. By the monotonicity of log, this
directly implies πc(T cat
n ) > πc(T) for all such trees T. This concludes the proof.
We now use Corollary 4.6 to show that the product function leads to a family of imbalance indices.
Corollary 4.7. Let n ∈N, n ≥2 and let c ∈R, c > −2. Moreover, let f : R≥2 →R be a strictly
increasing function. Then, f(πc) is an imbalance index. Moreover, the GFB tree T gfb
n
is the only minimizer
of this function.
Proof. The fact that T cat
n
is the unique maximizer of πc follows from Corollary 4.6, which in turn shows
by the monotonicity of f that T cat
n
is the unique maximizer of f(πc). The fact that T gfb
n
is the unique
minimizer of f(πc) was shown in Corollary 4.2. Using the fact that T fb
h
= T gfb
n
if n = 2h and the definition
of an imbalance index thus completes the proof.
Corollary 4.7 shows that the product functions are a family of tree imbalance indices. We further classify
this family as merely a subfamily of the family of tree imbalance indices Φf in the sense that the tree rankings
from balanced to imbalanced induced by these indices coincide with rankings induced by members of the Φf
family, as the following proposition shows.
Proposition 4.8. Let c ∈R, c > −2 and n ∈N, n ≥2, let f be a strictly increasing function. We con-
sider the imbalance index f(πc) and its induced ranking of trees T gfb
n
, . . . , T cat
n
from balanced to imbalanced.
Then, there is a strictly increasing and strictly concave function fc : R≥2 →R such that Φfc induces the
same ranking as f(πc).
Proof. First we note that by the monotonicity of f, f(πc) induces the exact same ranking as πc, which
in turn induces the exact same ranking as log(πc) by the monotonicity of the logarithm.
Now, we set fc(i) = log(i + c) for i ∈R≥2. Then, as in the proof of Corollary 4.6, fc is both strictly
concave and strictly increasing, and just as in Equation (4.8) we can conclude Φfc(T) = log(πc(T)) for all
rooted binary trees T with n leaves. This shows that Φfc and f(πc) induce the same rankings of all rooted
binary trees with n leaves and thus completes the proof.
Before we turn our attention to deriving explicit formulas for the minimal values of bs and Q in Section
4.3, we investigate the family of tree imbalance indices πc further. We first show that the family contains
infinitely many different members in the sense that for choices of real c1, c2 larger than −2 with c1 ̸= c2,
we can find two trees T and T ′ such that πc1 will consider T as more imbalanced than T ′ and πc2 gives the
opposite ranking. Thus, there is an uncountably infinite family of genuinely distinct imbalance indices.
Proposition 4.9. Let c1, c2 ∈R be distinct with c1, c2 > −2. Then there exist two trees T and T ′
such that πc1(T) > πc1(T ′) and πc2(T) < πc2(T ′); that is, the imbalance indices πc1 and πc2 rank T and T ′
differently.

--- Page 13 ---

THE GFB TREE AND TREE IMBALANCE INDICES
13
Proof. We will construct T and T ′ as depicted in Figure 4.3 with suitable choices of sizes of subtrees:
n11 of T11, n12 of T12, n21 of T21 and n22 of T22, respectively. Subtrees T11, T12, T21 and T22 can then be
chosen arbitrarily as long as they have the respective numbers of leaves.
ρ
T11
T12
T21
T22
T
ρ
T11
T21
T12
T22
T ′
ρ
T11
T21
T12
T22
T ′′
Fig. 4.3. Trees T, T ′, and T ′′ as needed in the proofs of Propositions 4.9 and 4.10. Note that all three trees share the
same subtrees T11, T12, T21, and T22, which are depicted schematically as triangles. The stars depict the inner vertices that
play an important role in the proofs.
Since the subtree sizes induced by the two trees T and T ′ only differ in two nodes, we can easily express
πc(T ′) using πc(T) for any choice of c ∈R as follows:
πc(T ′) = πc(T) · (n11 + n21 + c) · (n11 + n12 + n21 + c)
(n11 + n12 + c) · (n21 + n22 + c)
.
This implies:
πc(T ′) ≷πc(T)
(4.9)
⇐⇒(n11 + n21 + c) · (n11 + n12 + n21 + c) ≷(n11 + n12 + c) · (n21 + n22 + c)
⇐⇒cn11 + cn21 −cn22 ≷n11n22 + n12n22 −n2
11 −n11n12 −n11n21 −n2
21
⇐⇒c ≷n11n22 + n12n22 −n2
11 −n11n12 −n11n21 −n2
21
n11 + n21 −n22
,
(4.10)
(where the ≷-symbol stands for either > or < consistently throughout).
The proof strategy now is to show that for any choice of c1, c2 larger than −2 we can choose n11, n12,
n12, n21 and n22 such that the fraction of Equation (4.9) lies between c1 and c2. By Equation (4.9), this will
show that πc1(T ′) < πc1(T) and πc2(T ′) > πc2(T) and thus conclude the proof. In the following, we assume
without loss of generality that c2 > c1 by exchanging T and T ′ if needed.
So now we let c1, c2 ∈R with c1 > −2 and c2 > c1. We let k ∈N be such that k · (c2 −c1) > 2. This
guarantees that the open interval (k · c1, k · c2) contains two consecutive integers m and m + 1, where m ∈Z.
This implies that m
k and m+1
k
are contained in the open interval (c1, c2). We have two rational numbers
contained in (c1, c2). We now consider their mean 2m+1
2k . We have:
c1 < m
k < 2m + 1
2k
< m + 1
k
< c2.

--- Page 14 ---

14
CLEARY, FISCHER, AND ST. JOHN
Following our proof strategy, the proof is thus complete if we can show that we can choose n11, n12, n21 and
n22 such that the fraction of Equation (4.9) equals 2m+1
2k .
We now set n11 = 1, n22 = 2, n21 = 2k+1, n12 = 4k2+2+6k+2m. We first verify that these are all valid
leaf numbers: that all of these numbers are natural. Clearly, this holds for n11 and n22. Moreover, recall
that k ∈N, so n21 is also natural. But as m ∈Z, m < 0 could be possible. So we need to verify that n12
is positive. However, we know that m
k > c1 > −2 by the choice of c1 and m
k , respectively. This shows that
m > −2k and thus 2m > −4k, which leads to n12 = 4k2 +2+6k+2m > 4k2 +2+6k−4k = 4k2 +2+2k ∈N.
So our choices of n11, n12, n21 and n22 result in four positive integers and can be realized as subtree sizes in
trees. We show that with these choices, we indeed get that the fraction of Equation (4.9) equals 2m+1
2k :
n11n22 + n12n22 −n2
11 −n11n12 −n11n21 −n2
21
n11 + n21 −n22
= 2 + 2(4k2 + 2 + 6k + 2m) −1 −(4k2 + 2 + 6k + 2m) −(2k + 1) −(2k + 1)2
1 + (2k + 1) −2
= 1 + (4k2 + 2 + 6k + 2m) −(2k + 1) −(4k2 + 4k + 1)
2k
= 2m + 1
2k
.
This completes the proof.
Note that unsurprisingly, it is easier to make πc1 and πc2 disagree concerning the ranking of T and T ′
if c2 −c1 is large. If the difference is larger than one, the value of k chosen in the proof can be 1, which is
as small as possible. As our choice of subtree sizes in the proof was n11 = 1, n22 = 2, n21 = 2k + 1, and n12
such that n12 > 4k2 + 2 + 2k, this shows that even if k = 1, we already need n = 1 + 2 + 3 + 8 = 14 leaves
for our construction. It may be possible to have smaller examples showing different rankings, but it is clear
that no two indices πc1 and πc2 will rank all trees in the same order if c1 ̸= c2.
We note T and T ′ as used in the proof of Proposition 4.9 only differ in two subtree sizes, yet they will
be ranked differently by certain members of the πc family. On the other hand, there are always pairs of
trees that are ranked identically for all choices of c. Most prominently, this is of course the case for T cat
n
and
T gfb
n
, but these differ in most subtree sizes. The next proposition shows that for all n at least 6, there are
pairs of T and T ′ such that these trees differ only in two subtree sizes and we have πc(T) > πc(T ′) for all
c ∈R, c > −2.
Proposition 4.10. Let n ∈N with n ≥6. Then there exist two trees T and T ′′ which only differ in two
subtree sizes such that πc(T) > πc(T ′′) for all c ∈R, with c > −2.
Proof. We give an explicit construction for two non-isomorphic trees T and T ′′ which fulfill the condition.
We begin by choosing nij ∈N such that n11 < n22 and n12 < n21 and such that n11+n12+n21+n22 = n ≥6.
These values of nij (with i, j ∈{1, 2}) will be used as leaf numbers for the subtrees Tij for T and T ′′ as
depicted in Figure 4.3. Note that the conditions on nij guarantee that T and T ′′ are not isomorphic.
Moreover, note that as the subtree sizes induced by the two trees T and T ′′ from Figure 4.3 only differ
in two nodes, we can easily express πc(T ′′) using πc(T) for any choice of c ∈R:
πc(T ′′) = πc(T) · (n11 + n21 + c) · (n12 + n22 + c)
(n11 + n12 + c) · (n21 + n22 + c).
This shows that we have:
πc(T ′′) ≷πc(T) ⇐⇒(n11 + n21 + c) · (n12 + n22 + c) ≷(n11 + n12 + c) · (n21 + n22 + c)
⇐⇒n11n12 + n21n22 ≷n11n21 + n12n22
(where again the ≷-symbol is a consistent inequality throughout). As the latter term is completely indepen-
dent of c, this shows that all indices in the πc family will agree on how to rank T and T ′′, and this will only
be determined by these trees’ subtree sizes. This completes the proof.
Figure 4.4 illustrates the differences of rankings within the πc family by considering the range of values
c = −1.99, −1.5, −1, −0.5, 0, 0.5, 1, 1.5, 2 and comparing the rankings induced by these values for n = 10.

--- Page 15 ---

THE GFB TREE AND TREE IMBALANCE INDICES
15
Fig. 4.4. Ranking differences for the imbalance indices from product functions πc for nine different choices of c with
c > −2. The x-axis represents indices for values c = −1.99, −1.5, −1, −0.5, 0, 0.5, 1, 1.5, 2, and the y-axis shows the 98 rooted
binary trees with 10 leaves. Each tree has an associated line showing how high (imbalanced) or low (balanced) it is ranked for
the different choices of c, with the rankings of three trees (caterpillar, GFB, and maximally balanced) highlighted in bold.
4.3. Explicit formulas for π−1
 T gfb
n

and π0
 T gfb
n

. The first aim of this section is to provide
two alternative direct (non-recursive) formulas to calculate the values both of π−1
 T gfb
n

as well as of
π0
 T gfb
n

, corresponding to the bs-shape and the Q-shape statistic, respectively. It turns out that the se-
quence
 π−1
 T gfb
n

n∈N can already be found in the Online Encyclopedia of Integers Sequences OEIS [17],
namely under reference number A132862. However, the OEIS only contained a recursive formula to cal-
culate
 π−1
 T gfb
n

n∈N. Within the scope of the present manuscript, we have submitted our two explicit
formulas for π−1
 T gfb
n

to the OEIS for addition to their database. Moreover, the sequence π0
 T gfb
n

of the
Q statistic was added to the OEIS under the identifier A386912 [17, Sequence A386912].
The second aim of this section is to use our new formulas to derive explicit formulas for the minimum
value of the bs-shape statistic (which answers an open question [6, Chapter 9]) as well as for the Q-shape
statistic.
We first prove the following lemma to give insight into the greedy clustering algorithm defining T gfb
n .
Lemma 4.11. Let n ∈N. Let A be the greedy clustering algorithm constructing T gfb
n . Then, at any point
during the run of this algorithm, there is at most one tree contained in the present set of trees whose size is
not a power of two.
Proof. Towards a contradiction, we assume at some point during the course of the algorithm, there exists
more than one tree in the present set of trees whose size is not a power of two. Consider the first step, j,
where two such trees exist, and call them T and T ′. We assume that T = (T1, T2) (where (T1, T2) denotes
the standard decomposition of T as defined above) was constructed from the trees of minimal size, T1 and
T2 at step i < j. Further assume that at some later step j, T ′ = (T ′
1, T ′
2) was constructed from the trees of
minimal size, T ′
1 and T ′
2. By hypothesis, at the previous step, i −1, all trees, have size a power of 2. And
at step j −1, all trees, besides T, have size a power of 2. Since both T1 and T2 have size a power of 2 and
the result of joining them, T, does not, we know that T1 and T2 have different heights, and without loss of
generality, we have that |T1| < |T2| < |T|. Further, by construction, h(T2)+1 = h(T), and, by Corollary 3.4,
h(T1) + 1 = h(T2). By a similar argument, |T ′
1| < |T ′
2| < |T ′|, h(T ′
2) + 1 = h(T ′), and h(T ′
1) + 1 = h(T ′
2).
At each step, algorithm A joins the two trees of the present set of the smallest size, so, all other trees
at step i −1 must have at least the size of T2, and all other trees at step j −1 must have at least the size
of T ′
2. In particular, T must be as least as large as T ′
2. Since T does not have size a power of 2, but T ′
2
does, we conclude from |T| ≥|T ′
2| that in fact |T| > |T ′
2|. Moreover, as a power of two, |T ′
2| as a subtree of
the GFB tree must be a fully balanced tree by Corollary 3.2, so it has minimal height for any tree with |T ′
2|

--- Page 16 ---

16
CLEARY, FISCHER, AND ST. JOHN
leaves. Thus, as |T| > |T ′
2|, we conclude that we additionally have h(T2) + 1 = h(T) > h(T ′
2) > h(T ′
1). This
necessarily implies h(T2) ≥h(T ′
2) > h(T ′
1). Together with h(T2) > h(T1), this gives a contradiction, as in
step i, T1 would not have been clustered with T2 as tree T ′
1 of strictly smaller size than T2 was still available.
This completes the proof.
The following theorem will prove useful for calculating an explicit formula for the minimum value of the
bs-shape statistic. It counts the number of subtrees of T gfb
n
for all possible subtree sizes.
Theorem 4.12. Let n ≥1, and let an(i) denote the number of subtrees of T gfb
n
of size i for i = 1, . . . , n.
Let ki = ⌈log(i)⌉. Then, we have:
an(i) =









 n
i

if i = 2ki and if ((n
mod i) = 0
or
(n
mod i) ≥2ki−1),
 n
i

−1
if i = 2ki and if (0 < (n
mod i) < 2ki−1),
1
if i ̸= 2ki and
 (n −i)
mod 2ki−1
= 0,
0
if i ̸= 2ki and
 (n −i)
mod 2ki−1
> 0.
.
The appendix contains a proof of Theorem 4.12, which is based on Lemma 4.11.
We now turn our attention to πc
 T gfb
n

.
Corollary 4.13. Let n ∈N, n ≥2 and let c ∈R, c > −2. Then, πc
 T gfb
n

=
nQ
i=2
(i + c)an(i), where
an(i) is given by Theorem 4.12.
Proof. By definition, we have πc(T) =
Q
v∈˚
V (T )
(nv + c). Since the values of nv range between 2 and n,
sorting the subtrees by sizes and using Theorem 4.12 gives the desired result.
Corollary 4.5 together with Corollary 4.13 leads to an explicit formula for the minimum value for the
bs-statistic, thus solving an open problem stated in [6, Chapter 9].
Corollary 4.14. Let bs∗
n =
min
T ′∈BT ∗
n
bs(T ′). Then, we have: bs∗
n = log
 nQ
i=2
(i −1)an(i)

.
Proof. By Corollary 4.5, bs is uniquely minimized by T gfb
n , which directly implies bs∗
n = bs
 T gfb
n

. By defi-
nition, this shows bs∗
n = log


Q
v∈˚
V (T gfb
n )
(nv −1)

. Applying Corollary 4.13 with c = −1 and the monotonicity
of the logarithm, immediately leads to the required result and thus completes the proof.
Remark 1. The sequence
 nQ
i=2
(i −1)an(i)

n≥1
starts with the values:
1, 1, 2, 3, 8, 15, 36, 63, 192, 405, 1080, 2079, 6048, 12285, 31752, 59535193536, 433755, 1224720
has already occurred in different contexts (cf. [2]). It is listed in the Online Encyclopedia of Integer Sequences
([17, Sequence A132862]), where only recursive formulas were given. Using the GFB tree, in particular
Theorem 4.12 and Corollary 4.14, now allows for a simple explicit formula to calculate this sequence.1 The
explicit formulas arising from the present manuscript have meanwhile been submitted to the OEIS.
Analogously, we can derive a result as given by Corollary 4.14 also for the Q-shape statistic.
Corollary 4.15. Let Q∗
n =
min
T ′∈BT ∗
n
Q(T ′). Then, we have: Q∗
n = log
 nQ
i=2
ian(i)

.
Proof. Using c = 0, the proof of Corollary 4.15 is analogous to the proof of Corollary 4.14.
While the explicit formulas for π−1
 T gfb
n

and for π0
 T gfb
n

provided by Corollary 4.13 are non-recursive
and thus already an improvement to the previous state of the literature, they heavily depend on Theorem 4.12.
The following theorem provides another direct formula independent of the values an(i).
Theorem 4.16. Let n ∈N, n ≥2 and let c ∈R, c > −2. Let kn = ⌈log(n)⌉, and let dn = n −2kn−1 be
the difference between n and the next lower power of 2. Then, we have:
1We note that another explicit, but more complicated, formula was independently derived in [13].

--- Page 17 ---

THE GFB TREE AND TREE IMBALANCE INDICES
17
1. If dn = 2kn−1 (with n = 2kn), then πc
 T gfb
n

= πc

T fb
kn

=
kn−1
Q
i=0
(2kn−i + c)2i.
2. If dn < 2kn−1, (with n < 2kn), then we have:
πc
 T gfb
n

=πc

T fb
kn−1

· (2 + c)dn
·
kn−1
Y
i=1


2i+1 + c
2i + c
⌊
dn
2i ⌋
·
 
2i +
 dn −2i ·
 dn
2i

+ c
2i + c
!⌈
dn
2i ⌉−⌊
dn
2i ⌋

Before we can prove Theorem 4.16, we briefly show that the complete tree T c
n of Fill [5] coincides with the
GFB tree T gfb
n , which has been independently shown in Riesterer [13, Theorem 4.2], albeit with a different
proof. This result will enable us to use a different construction of T gfb
n
, namely to start with T fb
kn−1, fix an
orientation and then replace a certain number of leaves by cherries from left to right, until n leaves in total
are reached.
Lemma 4.17 (Theorem 4.2 in [13]).
Let n ≥1. Then, T gfb
n
= T c
n.
Proof. We prove the statement by induction on n. In the following, let T gfb
n
= (Ta, Tb), where Ta has
size na and Tb has size nb with na ≥nb. Similarly, let T c
n = (T c
a, T c
b ), where T c
a has size nc
a and T c
b has size
nc
b with nc
a ≥nc
b.
For n = 1 there is only one tree, so there is nothing to show. We now assume the statement holds for all
trees with up to n −1 leaves and consider n ≥2. Let ℓn = ⌊log(n)⌋, that is n ∈{2ℓn, . . . , 2ℓn+1 −1}. Then,
by construction of T c
n, we know that if n ≤3 · 2ℓn−1, nc
b = 2ℓn−1 (as in this case, no leaves of Tb get replaced
by cherries), and nc
a = n −nc
b = n −2ℓn−1. By Part (1) of Proposition 3.3, we can then conclude na = nc
a
and nb = nc
b.
If, on the other hand, n > 3 · 2ℓn−1, we know by construction that T c
a = T fb
ℓn and thus nc
a = 2ℓn (as all
leaves of the left subtree have been replaced by cherries) and thus nc
b = n −nc
a = n −2ℓn. By Part (2) of
Proposition 3.3, we can then conclude na = nc
a and nb = nc
b.
Thus, in both cases, the sizes of Ta and T c
a as well as the sizes of Tb and T c
b , respectively, coincide, which
by induction shows that Ta = T c
a and Tb = T c
b . Thus, T gfb
n
= (Ta, Tb) = (T c
a, T c
b ) = T c
n, which completes the
proof.
We are now in the position to prove Theorem 4.16.
Proof of Theorem 4.16. For the case in which dn = 2kn−1, the statement is a direct conclusion of the
fact that for n = 2kn, the GFB tree and the fully balanced tree coincide.
It remains to consider the case dn < 2kn−1. In this case, by Lemma 4.17, we can derive the GFB tree
from T fb
kn−1 by replacing dn leaves by cherries from left to right. Thus, we can start with πc

T fb
kn−1

and
modify this product by dividing out all factors of πc

T fb
kn−1

that are no longer present in πc
 T gfb
n

and
multiypling in factors newly occuring in the latter term. We do this using the following considerations:
• The factor (2 + c)dn stems from the dn newly formed cherries, each of which contributes a factor of
2 + c. For this new factor, nothing needs to be divided out as the former leaves did not occur in the
term πc

T fb
kn−1

.
• Next, for each i = 1, . . . , kn −1, we need to check how many subtrees of size 2i in T fb
kn−1 get replaced
by subtrees of size 2i+1 when T gfb
n
is formed. These are precisely the subtrees of size 2i in T fb
kn−1
all of whose leaves get replaced by cherries. As we fill the tree up from left to right, it can be easily
seen that there are
 dn
2i

such trees, explaining the term

2i+1+c
2i+c
⌊
dn
2i ⌋
.
• Last, for each i = 1, . . . , kn −1, there may be at most one subtree of size 2i in T fb
kn−1 some of whose
leaves but not all get replaced by cherries. This depends on whether dn
2i is an integer. If it is, then
the dn new cherries completely fill up all trees of size 2i to which they were added, (that is, all these
trees have already been considered in the previous term). This is the case when
 dn
2i

−
 dn
2i

= 0,
which implies that in this case, the latter term in the equation equals 1 and thus does not contribute
to the overall product.

--- Page 18 ---

18
CLEARY, FISCHER, AND ST. JOHN
If, however, dn
2i is not an integer and thus
 dn
2i

−
 dn
2i

= 1, then there is a tree of size 2i to which
dn −2i ·
 dn
2i

leaves get added, namely precisely the “left over” leaves after filling up
 dn
2i

many
subtrees of T fb
kn−1 with 2i new leaves each. This explains the last factor and thus completes the
proof.
Next, we again turn our attention to the bs-shape statistic.
4.4. Expected values of bs-shape statistic. The bs-shape statistic plays an important role in tree
balance, particularly in the context of mathematical phylogenetics and the Yule-Harding model, cf. [10].
However, so far the expected values of the bs-shape statistic under the Yule-Harding and the uniform models,
which are common distributions of trees, are unknown [6, Chapter 9]. In the following, we give bounds on
the expected value of the bs-shape statistic under these two distributions: the uniform distribution where each
(binary) tree on n leaves is equally likely, and the Yule-Harding distribution. To show our bounds, we outline
and use the elegant approach of King and Rosenberg [11]. They note that the expectation of the Sackin index
can be computed in terms of the cluster sizes for any distribution, θ, on trees which has the exchangeability
property, that is, for each T ∈BT n and each permutation, σ, of its leaf labels, Pθ(T) = Pθ(σ(T)). For such
distributions, the proposition from Than and Rosenberg [19] applies for the Sackin index, Sn:
Proposition 4.18 ([19], Lemma 6). If a probability distribution, Θ, on BT n satisfies the exchangeability
property, then the expected value for the Sackin index on n-leaf trees is:
Eθ[Sn] =
n−1
X
k=1
n
k

kpn(k)
where pn(k) is the probability that a given subset A ⊆X with |A| = k, 1 ≤k ≤n, is a cluster of a tree of
size n leaves sampled from BT n according to Θ.
Note that the bs-shape statistic, like the Sackin index, sums across all cluster sizes of a given tree: the
Sackin index sums up the respective size k, while the bs-statistic sums the logarithm of said size (namely,
log(k−1)). This similarity between the indices allows us to use the above approach introduced for the Sackin
index also for the bs-shape statistic:
Proposition 4.19. If a probability distribution, Θ, on BT n satisfies the exchangeability property, then
the expected value for the bs-shape statistic on n-leaf trees is
Eθ[bsn] =
n−1
X
k=2
n
k

log(k −1)pn(k)
where pn(k) is the probability that a given subset A ⊆X with |A| = k, 2 ≤k ≤n, is a cluster of a tree of
size n leaves sampled from BT n according to Θ.
King and Rosenberg [11] give an elegant proof of the expected value of the Sackin index and the resulting
closed form:
Theorem 4.20 ([11], Corollary 7). The expectation of the Sackin index under the uniform model on
rooted binary labeled trees of n leaves is:
EU[Sn] = 4n−1
Cn−1
−n
where Cn =
1
n+1
 2n
n

, the nth Catalan number.
Using the bounds from [11], we can show:
Theorem 4.21. The expectation of the bs-shape statistic under the uniform model on rooted binary labeled
trees of n leaves is:
log n
n
 4n−1
Cn−1
−n

≤EU[bsn] ≤4n−1
Cn−1
−n

--- Page 19 ---

THE GFB TREE AND TREE IMBALANCE INDICES
19
Proof. The upper bound follows directly from the Sackin index being an upper bound for the bs-shape
statistic.
For the lower bound, we use Proposition 4.19 and the simple bound of log(k−1)
k
≥log(n−1)
n
for 2 ≤k ≤n:
Eθ[bsn]
=
Pn−1
k=2
 n
k

log(k −1)pn(k) = Pn−1
k=2
 n
k
 (
n−1
k−1)
(
2n−2
2k−2) log(k −1)
≥
log(n−1)
nCn−1 (4n−1 −[
 2(n−1)
n−1

+ 2
 2n−5
n−3

+
 2(n−1)
n−1

])
=
log(n−1)
nCn−1 (4n−1 −[2
 2(n−1)
n−1

+ 2
 2n−5
n−3

]).
This completes the proof.
5. Discussion and Conclusion. We have introduced two families of imbalance indices, namely Φf
for strictly increasing and strictly concave functions f and the product functions πc for c > −2, and shown
that both of them are uniquely minimized by the GFB tree. For the bs-shape statistic, which is an important
imbalance index used in the phylogenetic literature, this finding answered the open question concerning its
extrema from [6, Chapter 9]. However, our approach is more general and not just focused on the bs-shape
statistic. In particular, we have shown that our families of imbalance indices contain infinitely many different
imbalance indices, some of which might be useful in phylogenetics and other research areas where tree balance
plays a role.
Acknowledgements. The authors wish to thank Tom N. Hamann, Kristina Wicke and Volkmar Lieb-
scher for helpful discussions. The present manuscript is based upon work supported by the National Science
Foundation under Grant No. DMS-1929284 while the authors were in residence at the Institute for Computa-
tional and Experimental Research in Mathematics (ICERM) in Providence, RI, during the Theory, Methods,
and Applications of Quantitative Phylogenomics semester program.
REFERENCES
[1] Michael GB Blum and Olivier Fran¸cois.
Which random processes describe the tree of life?
A large-scale study of
phylogenetic tree imbalance. Systematic Biology, 55(4):685–691, 2006.
[2] Olivier Bodini, Antoine Genitrini, Bernhard Gittenberger, Isabella Larcher, and Mehdi Naima. Compaction for two models
of logarithmic-depth trees: Analysis and experiments. Random Structures & Algorithms, 61(1):31–61, 2022.
[3] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. Introduction to Algorithms. MIT Press,
Cambridge, MA, second edition, 2001.
[4] Tom´as M. Coronado, Mareike Fischer, Lina Herbst, Francesc Rossell´o, and Kristina Wicke. On the minimum value of the
Colless index and the bifurcating trees that achieve it. Journal of Mathematical Biology, 80(7):1993–2054, 2020.
[5] James Allen Fill. On the distribution of binary search trees under the random permutation model. Random Structures
and Algorithms, 8(1):1–25, 1996.
[6] M. Fischer, L. Herbst, S. J. Kersting, L. K¨uhn, and K. Wicke. Tree Balance Indices - A Comprehensive Survey. Springer,
Berlin, 2023.
[7] Mareike Fischer. Extremal values of the Sackin tree balance index. Annals of Combinatorics, 25(2):515–541, 2021.
[8] Mareike Fischer and Volkmar Liebscher. On the balance of unrooted trees. Journal of Graph Algorithms and Applications,
25(1):133–150, Jan. 2021.
[9] Tom N. Hamann. Metaconcepts for rooted tree balance. Master’s thesis, University of Greifswald, Germany, 2023.
[10] Sophie J Kersting, Kristina Wicke, and Mareike Fischer. Tree balance in phylogenetic models. Philos. Trans. R. Soc.
Lond. B Biol. Sci., 380(1919):20230303, February 2025.
[11] Matthew C King and Noah A Rosenberg. A simple derivation of the mean of the Sackin index of tree balance under the
uniform model on rooted binary labeled trees. Mathematical Biosciences, 342:108688, 2021.
[12] Arnau Mir, Francesc Rossell´o, and Luc´ıa Rotger. A new balance index for phylogenetic trees. Mathematical Biosciences,
241(1):125–136, 2013.
[13] Theresa Riesterer. Der Greedy-from-the-bottom-Baum und seine Bedeutung f¨ur die Phylogenetik. Master’s thesis, Uni-
versity of Greifswald, Germany, 2022.
[14] Donn E. Rosen. Vicariant patterns and historical explanation in biogeography. Systematic Zoology, 27(2):159, 1978.
[15] Charles Semple and Mike Steel.
Phylogenetics.
Oxford Lecture Series in Mathematics and its Applications. Oxford
University Press, Oxford, 2003.
[16] Kwang-Tsao Shao and Robert R. Sokal. Tree balance. Systematic Zoology, 39(3):266, 1990.
[17] N. J. A. Sloane. The On-Line Encyclopedia of Integer Sequences, 1964.
[18] Mike Steel. Phylogeny: Discrete and random processes in evolution. Society for Industrial and Applied Mathematics,
Philadelphia PA, 2016.
[19] Cuong V Than and Noah A Rosenberg. Mean deep coalescence cost under exchangeable probability distributions. Discrete
Applied Mathematics, 174:11–26, 2014.
Declarations.

--- Page 20 ---

20
CLEARY, FISCHER, AND ST. JOHN
• Funding: The present manuscript is based upon work supported by the National Science Foun-
dation under Grant No.
DMS-1929284 while the authors were in residence at the Institute for
Computational and Experimental Research in Mathematics (ICERM) in Providence, RI, during the
Theory, Methods, and Applications of Quantitative Phylogenomics semester program.
• Competing interests: All others received the funding declared above. The authors confirm that
they have no other financial or non-financial interests to declare.
• Data availability: The authors declare that all data generated for this study are contained in the
manuscript. No other sources of data have been used.
APPENDIX. Here we present the somewhat technical proof of Theorem 4.12.
Proof of Theorem 4.12. We first analyze the procedure with which the GFB tree is generated. When
the greedy clustering is performed to form T gfb
n , we refer to all clusterings that involve at least one tree
of size 2m and no tree of size 2m−1 as phase m of the algorithm. Phase 0 includes all steps that cluster
subtrees of size 2m = 20 = 1, that is the leaves to form cherries. If n is odd, this includes as the last step
the clustering of a leaf and a cherry (subtree of size 2). Phase 1 contains all steps that involve clustering of
cherries. Almost all these clusterings will be two cherries clustered into a new subtrees of size 4. The last
clustering in phase 1 could cluster a cherry with a subtree of size 3 or 4, if n mod 4 ≡3 or 2, respectively.
We now proceed by considering some i ∈{1, . . . , n} with ki = ⌈log(i)⌉as the end of phase ki −1 of the
algorithm (or, equivalently, the beginning of phase ki). The trees present at this stage will be referred to as
the current set of trees. All trees in the current set must have size at least 2ki−1 + 1 as all trees of size up to
2ki−1 have already been clustered into larger trees. Moreover, all trees in the current set have size strictly
smaller than 2ki+1. This is due to the following: first, phase ki −1 only performs clusterings in which at least
one tree has size at most 2ki−1. Second, all trees formed throughout the course of the algorithm are again
GFB trees by Corollary 3.2. This implies by Corollary 3.4 that a tree of size 2ki+1 or larger would have two
maximum pending subtrees of size at least 2ki each – but two such trees could not have been clustered during
phase ki −1 of the algorithm. So, all trees T in the current set have size nT ∈S = {2ki−1 +1, . . . , 2ki+1 −1}.
However, by Lemma 4.11, there is at most one tree present in the current set of trees whose size is not a
power of 2. As S only contains one power of 2, namely 2ki, we conclude that all trees except possibly for
one have size 2ki.
We now consider the decomposition n = a · 2ki + b with b =
 n mod 2ki
∈{0, . . . , 2ki −1} and
a =
 n
2ki

. We distinguish three cases depending on the value of b. Note that this decomposition together
with the above observations immediately implies that there are a −1 or a trees of size 2ki in the current set.
In the first case, the only remaining tree has size 2ki + b, and in the second case, the only remaining tree
has size b.
• If b = 0, we have n = a · 2ki. Thus, we have (n mod 2ki) = 0, and obviously all trees in the current
set have size 2ki, because n −(a −1) · 2ki = 2ki, so if you consider a −1 trees of size 2ki and one
remaining tree, the remaining tree has the same size. This directly proves the statement an(i) =
 n
i

of the theorem for i = 2ki and (n mod i) = 0 (as all trees of the current set are subtrees of T gfb
n
and no other trees of size i = 2ki can be formed throughout the algorithm).
Moreover, as b = 0, we also have for i ∈{2ki−1 + 1, . . . , 2ki −1} that ((n −i) mod 2ki−1) > 0, and
as there is no tree of such a size i (as all trees in the current set have size 2ki, which by Corollary
3.4 are formed of two trees of size 2ki−1 each), we have an(i) = 0 for such values of i. This is in
accordance with the last case of the theorem.
• If 0 < b < 2ki−1, we observe that there cannot be a trees of size 2ki in the current set. Otherwise,
there would be b leaves not contained in any 2ki tree, thus belonging to a tree T of size b in the
current set – but this would imply that the size of T is strictly smaller than 2ki−1, a contradiction
to the current set being the set at the end of phase ki −1, as T would have had to cluster in this
phase.
So the only possibility is that there are a −1 trees of size 2ki in the current set and one tree T of
size 2ki + b. But by Corollary 3.4, T cannot have a subtree of size 2ki (as a tree of size 2ki cannot
be clustered with a tree of size b < 2ki−1 to form a GFB tree, and T has to be a GFB tree, too, as
it is a subtree of T gfb
n ); it instead has one maximum pending subtree of size 2ki−1 and one of size
2ki−1 + b.
Thus, T gfb
n
contains a −1 =
 n
i

−1 trees of size i = 2ki, so an
 2ki
=
 n
i

−1, which proves the

--- Page 21 ---

THE GFB TREE AND TREE IMBALANCE INDICES
21
second case of the theorem as we have 0 < b = (n mod i) < 2ki−1.
Further, if i = 2ki−1 + b, we have n −i = a · 2ki + b −
 2ki−1 + b

= (2a −1) · 2ki−1, and thus
((n −i) mod 2ki−1) = 0. As we have already seen that a subtree of size 2ki−1 + b was formed in
the course of the algorithm (and no more such trees can be formed as the algorithm proceeds), we
have an
 2ki−1 + b

= 1, which is in accordance with the third case of the theorem.
Last, if i ∈{2ki−1 + 1, . . . , 2ki −1} with i ̸= 2ki−1 + b, we have seen that no such tree can be formed
in the course of the algorithm, so an(i) = 0. As in this case we have ((n −i) mod 2ki−1) > 0, this
is in accordance with the fourth case of the theorem.
• Finally, we consider the case b > 2ki−1. In this case, before considering the beginning of phase ki
of the algorithm, we consider the beginning of phase ki −1, which is the end of phase ki −2. We
can write n = a · 2ki + b = (2a + 1) · 2ki−1 + b′, where b′ = b −2ki−1 < 2ki−1 (as b < 2ki). Using
the same reasoning as above, in the beginning of phase ki −1, there must either be 2a trees of size
2ki−1 and one tree of size n −2a · 2ki−1 = 2ki−1 + b′, or there are 2a + 1 trees of size 2ki−1 and one
tree of size b′ < 2ki−1.
In the latter case, if in the beginning of phase ki −1 we have 2a + 1 trees of size 2ki−1 and one tree
of size b′ < 2ki−1, note that we must have b′ > 0 (empty trees are never formed in the algorithm).
Then, the tree of size b′ will be the first one to be clustered in phase ki −1 to one of the 2a + 1 trees
of size 2ki−1. This forms a tree of size 2ki−1 +b′, and the remaining 2a trees of size 2ki−1 will cluster
to form a trees of size 2ki in the course of phase ki −1. Thus, in the end of this phase, we have a
trees of size 2ki and one tree of size 2ki−1 + b′ = 2ki−1 + b −2ki−1 = b. This tree of size b would be
the first tree to be clustered in phase ki with one of trees of size 2ki to form a tree of size 2ki + b.
Now, we consider the first case, the case where in the beginning of phase ki −1 we have 2a trees of
size 2ki−1 and one tree of size 2ki−1 + b′. If b′ > 0, phase ki −1 would not involve the last tree, it
would only cluster the 2a trees of size 2ki−1 to form a trees of size 2ki. The remaining tree of size
2ki−1 + b′ would be the first one to be clustered in phase ki with one of trees of size 2ki, though, to
form a tree of size 3 · 2ki−1 + b′ = 2ki + b′ + 2ki−1 = 2ki + b. Similarly, if b′ = 0, phase ki −1 would
first cluster the 2a trees of size 2ki−1 to form a trees of size 2ki and then, in its last step, it would
cluster the remaining tree of size 2ki−1 + b′ = 2ki−1 with one of the already formed trees of size 2ki
to form a tree of size 3 · 2ki−1 + b′ = 2ki + b.
So in all cases, we can see (either directly after phase ki −1 or after the first step of phase ki) that
T gfb
n
contains precisely a trees of size 2ki, one of which gets clustered with a tree of size b to form a
tree of size 2ki + b.
Now, if i = 2ki, the a =
 n
i

many trees of size 2ki are in accordance with the first case of the theorem,
because here we have (n mod 2ki) = b ≥2ki−1. Therefore, in this case we have an(i) =
 n
i

.
However, if i ∈{2ki−1 + 1, . . . , 2ki −1}, we have an(i) = 1 if i = b (because a tree of size b gets
clustered with a tree of size 2ki). This is in accordance with the third case of the theorem, as here
we have n −i = n −b = a · 2ki + b −b = a · 2ki, and thus ((n −i) mod 2ki−1) = 0. If, on the
other hand, we have i ∈{2ki−1 + 1, . . . , 2ki −1} and i ̸= b, then there cannot be a subtree of size
i: It would have to be clustered away last in phase ki of the algorithm. So it would have to be
there in the end of phase ki −1 (which is not the case as we have analyzed above), or it would
have to arise within phase ki. The latter cannot happen as we have seen that at the latest after
one step of phase ki, we are left with only trees of size at least 2ki. Thus, we conclude that for
such values of i, we have an(i) = 0. This is in accordance with the fourth case of the theorem,
because in this case we have n −i = a · 2ki + b −i. Since both b and i are contained in the set
{2ki−1, . . . , 2ki −1}, their maximal difference is bounded by 2ki −2ki−1. We can distinguish two
cases: If b > i, we have n −i = a · 2ki + b −i > a · 2ki = 2a · 2ki−1 as well as n −i = a · 2ki + b −i <
a·2ki +2ki −2ki−1 = (2a+1)·2ki−1, so we have (2a+1)·2ki−1 > n−i > 2a·2ki−1, which shows that
((n−i) mod 2ki−1) > 0. Similarly, if b < i, we have n−i = a·2ki +b−i < a·2ki = 2a·2ki−1 as well as
n−i = a·2ki+b−i > a·2ki−2ki+2ki−1 = (2a−1)·2ki−1, so we have 2a·2ki−1 > n−i > (2a−1)·2ki−1,
which shows that ((n −i) mod 2ki−1) > 0.
This completes the proof of the theorem.

```
