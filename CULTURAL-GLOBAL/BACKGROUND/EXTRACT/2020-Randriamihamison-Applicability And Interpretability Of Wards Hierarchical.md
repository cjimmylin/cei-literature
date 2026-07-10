# 2020-Randriamihamison-Applicability And Interpretability Of Wards Hierarchical

**Source:** 2020-Randriamihamison-Applicability And Interpretability Of Wards Hierarchical.pdf
**Pages:** 40
**Extracted:** 2026-04-03

---

## Page 1

Applicability and Interpretability of Hierarchical
Agglomerative Clustering With or Without
Contiguity Constraints
Nathanaël Randriamihamison1,2,3, Nathalie Vialaneix1 & Pierre Neuvial2
1 MIAT, Université de Toulouse, INRA, Castanet Tolosan, France
{nathanael.randriamihamison, nathalie.vialaneix}@inra.fr
2 Institut de Mathématiques de Toulouse; UMR 5219, Université de
Toulouse, CNRS UPS, F-31062 Toulouse Cedex 9, France
pierre.neuvial@math.univ-toulouse.fr
3 INRIA Bordeaux Sud-Ouest, CQFD Team, France
Abstract
Hierarchical Agglomerative Classiﬁcation (HAC) with Ward’s linkage has been
widely used since its introduction by Ward (1963). This article reviews extensions
of HAC to various input data and contiguity-constrained HAC, and provides ap-
plicability conditions. In addition, various versions of the graphical representation
of the results as a dendrogram are also presented and their properties are clariﬁed.
We clarify and complete the results already available in an heterogeneous literature
using a uniform background. In particular, this study reveals an important distinc-
tion between a consistency property of the dendrogram and the absence of crossover
within it. Finally, a simulation study shows that the constrained version of HAC
can sometimes provide more relevant results than its unconstrained version despite
the fact that the latter optimizes the objective criterion on a reduced set of solutions
1
arXiv:1909.10923v1  [stat.ME]  24 Sep 2019

## Page 2

at each step. Overall, the article provides comprehensive recommendations for the
use of HAC and constrained HAC depending on the input data as well as for the
representation of the results.
Keywords:
Hierarchical Agglomerative Clustering, Ward’s Linkage, Contiguity
Constraint, Dendrogram, Monotonicity
1
Introduction
Hierarchical Agglomerative Classiﬁcation (HAC) with Ward’s linkage has been widely
used since its introduction by Ward (1963). The method is appealing since it provides
a simple approach to approximate, for any given number of clusters, the partition min-
imizing the within-cluster inertia or “error sum of squares”. In addition to its simplicity
and the fact that it is based on a natural quality criterion, HAC often comes with a pop-
ular graphical representation called a dendrogram, that is used as a support for model
selection (choice of the number of clusters) and result interpretation. Originally described
to cluster data in Rp, the method has been applied more generally to data described by
arbitrary distances (or dis-similarities). Constrained versions of HAC have also been pro-
posed to incorporate a “contiguity” relation between objects into the clustering process
(Lebart 1978; Grimm 1987).
However, as already shown by Murtagh and Legendre (2014), confusions still exist be-
tween the diﬀerent versions and how the results are represented with a dendrogram, which
is also illustrated in (Grimm 1987) that presents diﬀerent alternatives for the representa-
tion. These have resulted in diﬀerent implementations of the Ward’s clustering algorithm,
with notable diﬀerences in the results. More importantly, the applicability framework of
the diﬀerent versions is not always clear: Batagelj (1981) has given very general necessary
and suﬃcient conditions on a linkage value to ensure that it is always increasing for any
given dissimilarity. This property is important to ensure the consistency between the
results of HAC and their graphical display as a dendrogram. Conditions on a general
constraint are also provided in Ferligoj and Batagelj (1982) to ensure a similar property
2

## Page 3

and Grimm (1987) proposes alternative solutions to the standard heights to address the
fact that the linkage might sometimes fail to provide a consistent representation of the
results of HAC. However, none of these articles fully cover the theoretical properties of
these alternatives, for unconstrained and constrained versions of the method.
The scope of the present article is to clarify the conditions of applicability and inter-
pretability of the diﬀerent versions of HAC and contiguity-constrained HAC (CCHAC).
We discuss the relevance of using them with diﬀerent types of input data and how the
corresponding results can be interpreted. We perform a systematic study of the mono-
tonicity of the diﬀerent versions of the dendrogram heights by reporting the results already
available in the literature for standard HAC and its various extensions and by completing
the ones that were not available to our knowledge. In addition to providing a uniform
presentation of a number of results partially present in the literature, this study reveals
an important distinction between this consistency property and the absence of crossover
within the dendrogram that was not discussed before.
Finally, we illustrate the respective behavior of HAC and CCHAC in a simulation study
where the diﬀerent heights are used in order to represent the results. This simulation shows
that, in addition to reducing the computational time needed to perform the method, the
constrained version (CCHAC) can also provide better solution than the standard one
(HAC) when the constraint is consistent with the data, despite the fact that it optimizes
the objective criterion on a reduced set of solutions at each step.
2
HAC and contiguity-constrained HAC
2.1
Hierarchical Agglomerative Clustering
HAC was initially described by Ward (1963) for data in Rp. Let Ω:= {x1, · · · , xn} be
the set of objects to be clustered, which are assumed to lie in Rp. A cluster is a subset of
Ω. The loss of information when grouping objects into a cluster G ⊂Ωis quantiﬁed by
3

## Page 4

the inertia (also known as Error Sum of Squares, ESS):
I(G) =
X
xi∈G
∥xi −¯xG∥2
Rp ,
(1)
where ¯xG = n−1 Pn
i=1 xi is the center of gravity of G. Starting from a partition P =
{G1, · · · , Gl} of Ω, the loss of information when merging two clusters Gu and Gv of P is
quantiﬁed by :
δ(Gu, Gv) := I(Gu ∪Gv) −I(Gu) −I(Gv).
(2)
The quantity δ is known as Ward’s linkage and it is equal to the variation of within-
cluster inertia (also called within-cluster sum of squares) after merging two clusters. It
also corresponds to the squared distance between centers of gravity:
δ(Gu, Gv) =
|Gu||Gv|
|Gu| + |Gv|∥¯xGu −¯xGv∥2
Rp.
(3)
The HAC algorithm is described in Algorithm 1. Starting from the trivial partition
P1 = {{x1}, {x2}, · · · , {xn}} with n singletons, the HAC algorithm creates a sequence of
partitions by successively merging the two clusters whose linkage δ is the smallest, until all
objects have been merged into a single cluster. Linkage values at step t can be eﬃciently
Algorithm 1 Standard Hierarchical Agglomerative Clustering (HAC)
1: Initialization: P1 = {{x1}, {x2}, · · · , {xn}}
2: for t = 1 to n −1 do
3:
Compute all pairwise linkage values between clusters of the current partition Pt
4:
Merge the two clusters with minimal linkage value to obtain the next partition
Pt+1
5: end for
6: return {P1, P2, . . . , Pn}
updated using linkage values at step t −1 with a formula known as the Lance-Williams
formula (Lance and Williams 1967). In the case of Ward’s linkage, this formula has ﬁrst
4

## Page 5

been demonstrated by Wishart (1969):
δ(Gu ∪Gv, Gw)
=
|Gu| + |Gw|
|Gu| + |Gv| + |Gw|δ(Gu, Gw) +
|Gv| + |Gw|
|Gu| + |Gv| + |Gw|δ(Gv, Gw)
−
|Gw|
|Gu| + |Gv| + |Gw|δ(Gu, Gv)
(4)
where |G| denotes the cardinal of any cluster G.
The framework of the current section can be extended straightforwardly to the case
where the objects to cluster are weighted. However, this study focuses on uniform weights
for the sake of simplicity.
2.2
HAC under contiguity constraint
In various applications, there exists an a priori information about the relations between
the objects. For instance, it is the case for spatial statistics, where objects possess nat-
ural proximity relations, in genomics, where genomic loci are linearly ordered along the
chromosome, or in neuroimaging, with the three-dimensional structure of the brain. Ac-
cording to this point of view, Contiguity-Constrained HAC (CCHAC) allows only mergers
between contiguous objects. Considering this approach can have two beneﬁts: (i) more
interpretable results by taking into account the natural structure of the data; (ii) a de-
creased computational time, because only a subset of all possible mergers are considered.
A very general framework for constrained HAC is described in Ferligoj and Batagelj
(1982): the contiguity is deﬁned by an arbitrary symmetric relation R ⊂Ω× Ωthat
indicates which pairs of objects are said contiguous. Only these pairs are then allowed to
be merged at the ﬁrst step of the algorithm, using the same objective function than in
the standard HAC algorithm. The next step iterates similarly, by using the following rule
to extend the contiguity relation to merged clusters:
(Gu ∪Gv, Gw) ∈R
⇔
(Gu, Gw) ∈R or (Gv, Gw) ∈R.
Algorithm 2 describes contiguity-constrained hierarchical agglomerative clustering
5

## Page 6

(CCHAC). The only diﬀerence with standard HAC lies in the fact that only contigu-
Algorithm 2 Contiguity-Constrained Hierarchical Agglomerative Clustering (CCHAC)
1: Initialization: P1 = {G1
1, G1
2, · · · , G1
n} where G1
u = {xu}. Contiguous singletons are
deﬁned by R1 = R ⊂Ω× Ω.
2: for t = 1 to n −1 do
3:
Compute all pairwise linkage values between contiguous clusters of the current
partition Pt with respect to Rt
4:
Merge the two contiguous clusters, Gt
v1 and Gt
v2 with minimal linkage value to
obtain the next partition Pt+1 = {Gt+1
u }u=1,...,n−t−1
5:
Extend the contiguity relation to the new cluster Gt
v1 ∪Gt
v2 ∈Pt+1 by setting
 Gt
v1 ∪Gt
v2, Gt
w

∈Rt+1
⇔
 Gt
v1, Gt
w

∈Rt or
 Gt
v2, Gt
w

∈Rt.
6: end for
7: return {P1, P2, . . . , Pn}
ous clusters are merged. From a computational viewpoint, only the linkage values for a
subset of Pt ×Pt have to be considered, which can drastically reduce the number of values
to be computed with respect to the standard algorithm. This gain in computational time
comes at the price of a (potential) loss in the objective function at a given step of the
algorithm, especially if the constraint is not consistent with the dissimilarity or similar-
ity values (see Section 5 for illustration and discussion). This also has a side eﬀect on
standard representations of the result of the algorithm, which is discussed in Section 4.
Order-constrained HAC.
A simple and useful case of contiguity constraint is the
case when the symmetric relation is a contiguity relation deﬁned along a line.
This
special and simple case is frequently encountered in genomics (where the contiguity thus
corresponds to the genomic position on a given chromosome) and will be called order-
constrained HAC (OCHAC) in the sequel. In this speciﬁc case, every cluster has exactly
two neighbours (except for the two positioned at the beginning and the end of the line)
and at step t of the algorithm, only n −t values of the linkage have to be computed
(instead of (n −t)(n −t −1)/2 for standard HAC). This case is the one implemented in
the R package adjclust and an eﬃcient algorithm is described in Ambroise et al. (2019)
for sparse datasets. In this paper, we demonstrate the good properties of the CCHAC for
the case of a general contiguity relation and illustrate the opposite situation (where some
6

## Page 7

good properties are not always satisﬁed for CCHAC) by providing counter-examples and
illustrations in the speciﬁc case of OCHAC.
3
Validity of HAC in possibly non-Euclidean settings
In this section, we systematically justify the use of HAC algorithm (with or without con-
tiguity constraints) for all kinds of proximity data, including dissimilarity and similarity
data.
3.1
Extension to dissimilarity data
The HAC algorithm of Ward (1963) has been designed to cluster elements of Rp. In
practice however, the objects to be clustered are often only indirectly described by a matrix
of pairwise dissimilarities, D = (dij)1≤i,j≤n. Formally, a dissimilarity is a generalization of
a distance, that can not necessarily be embedded into an Euclidean space (e.g., because
the triangle inequality does not hold for instance). Here, we only assume that D satisﬁes
the following properties for all i, j ∈{1, . . . , n}:
dij ≥0;
dii = 0;
dij = dji .
The HAC algorithm will be applicable to such a dissimilarity matrix D if D is Eu-
clidean. Formally, D is Euclidean if there exists an Euclidean space (E, ⟨·, ·⟩) and n points
{x1, ..., xn} ⊂E such that dij = ∥xi −xj∥for all i, j ∈{1, ..., n}, with ∥· ∥the norm
induced by the inner product, ⟨., .⟩, on E. Under this assumption, the dissimilarity case
is a simple extension of the original Rp framework described in Section 2. Diﬀerent ver-
sions of a necessary and suﬃcient condition for which an observed dissimilarity matrix
is Euclidean have been obtained in Schoenberg (1935); Young and Householder (1938);
Krislock and Wolkowicz (2012).
When such conditions do not hold, D is simply called a dissimilarity dataset, which is a
particular case of proximity or relational datasets. Schleif and Tino (2015) have proposed
a typology of such datasets and described diﬀerent approaches that can be used to extend
7

## Page 8

statistical or learning methods deﬁned for Euclidean data to such proximity data. In brief,
the ﬁrst main strategy consists in ﬁnding a way to turn a non Euclidean dissimilarity into
an Euclidean distance, that is the closest (in some sense) to the original dissimilarity. This
can be performed using eigenvalue corrections (Chen et al. 2009), embedding strategies
(like multidimensional scaling, Kruskal (1964)) or solving a maximum alignment problem
(Chen and Ye 2008), for instance.
A general construction.
Alternatively, by using an analogy between distance and
dissimilarity, HAC can be directly extended to non-Euclidean data as in Chavent et al.
(2018). This extension stems from the fact that, in the Euclidean case of Section 2, the
inertia of a clusters may be expressed only in function of sums of the entries of the pairwise
distances (∥xi −xj∥Rp, 1 ≤i, j ≤n):
I(G) = ∆(G, G)
2|G|
,
(5)
where ∆is deﬁned by ∆(Gu, Gv) = P
xi∈Gu,xj∈Gv ∥xi −xj∥2
Rp for any clusters Gu and Gv.
As a consequence of (5), Ward’s linkage between any two clusters Gu and Gv may be
itself be written in function of these pairwise distances, see, e.g., Murtagh and Legendre
(2014, p. 279):
δ(Gu, Gv) =
|Gu||Gv|
|Gu| + |Gv|
∆(Gu, Gv)
|Gu||Gv| −∆(Gu, Gu)
2|Gu|2
−∆(Gv, Gv)
2|Gv|2

.
(6)
Therefore, as proposed by Chavent et al. (2018), an elegant way to extend Ward’s HAC
to dissimilarity data is to deﬁne the inertia of a cluster using (5), with (sums of) distances
replaced by (sums of) dissimilarities, that is:
˜I(G) =
˜∆(G, G)
2|G|
,
(7)
8

## Page 9

where
˜∆(Gu, Gv) =
X
xi∈Gu,xj∈Gv
d2
ij .
(8)
The corresponding HAC is then formally obtained as the output of Algorithm 1, as de-
scribed in Section 2.1. In particular, Ward’s linkage is still given by (6), with ∆formally
replaced by ˜∆, and, as a consequence, the Lance-Williams update formula is also still
given by (4). When the elements of Ωdo belong to an Euclidean space and the dissim-
ilarities are the pairwise Euclidean distances ∥xi −xj∥Rp, these two deﬁnitions of HAC
coincide. Otherwise, HAC is still formally deﬁned, and the linkage can still be seen as a
measure of heterogeneity, but the interpretation of a cluster inertia as an average squared
distance to the center of gravity of the cluster (as in Equation (1)) is lost. Since the two
deﬁnitions, I and ˜I coincide for the Euclidean case, we will only use the notation I in the
sequel for the sake of simplicity, even when the data are non Euclidean dissimilarity data.
The above approach based on pairwise dissimilarities and pseudo-intertia may be
used to recover generalizations of Ward-based HAC to non-Euclidean distances al-
ready proposed in the literature.
In particular, the Ward HAC algorithm associated
to dij = ∥xi −xj∥α/2
Rp for 0 < α ≤2 and dij = ∥xi −xj∥1,Rp (the latter is also called the
Manhattan distance) correspond to the methods proposed by Székely and Rizzo (2005)
and Strauss and von Maltitz (2017), respectively.
Remark 1. Székely and Rizzo (2005) and Strauss and von Maltitz (2017) take a diﬀerent
point of view: they deﬁne the linkage between two clusters by (6) (up to a scaling factor
1/2); their generalized HAC is then the HAC associated to this linkage. Then, they prove
that the Lance-Williams Equation (4) is still valid for this linkage. We favor the above
construction by Chavent et al. (2018), which is simply based on pairwise dissimilarities,
as it is more intrinsic. It provides a justiﬁcation for the linkage formula, and the Lance-
Williams formula is automatically valid with no proof required.
Finally, there is an ambiguity in the deﬁnition of the pseudo-inertia as an extension of
the Ward’s case. If most authors consider that the dissimilarity is associated to a distance
9

## Page 10

and therefore deﬁne the pseudo-inertia based on the squared values d2
ij, some authors (as
Strauss and von Maltitz (2017)) deﬁne a linkage equal to the one that would have been
obtained with Ward’s linkage and a pseudo-inertia described as
1
2|G|
P
xi,xj∈G dij. This
ambiguity has long been enforced by popular implemented versions of the algorithm, as
it was the case in the R function hclust before Murtagh and Legendre (2014) raised and
corrected this problem.
3.2
Extension to kernel data
In some cases, proximity relations between objects are described by their resemblance
instead of their dissimilarity. We start with the case when the data are described by a
kernel matrix. A kernel matrix is a symmetric positive-deﬁnite matrix K = (kij)1≤i,j≤n
whose entry kij corresponds to a measure of resemblance between xi and xj. Here, contrary
to the Euclidean setting, no speciﬁc structure is assumed for Ω, which can be an arbitrary
set.
Aronszajn (1950) has proved that there exists a unique Hilbert space H equipped with
the inner product ⟨·, ·⟩H and a unique map φ : Ω−→H, such that kij = ⟨φ(xi), φ(xj)⟩H.
This allows to consider the associated distance in H between any two elements φ(xi) and
φ(xj) for xi, xj ∈Ω, that implicitly deﬁnes a Euclidean distance in Ωby:
dij = d(xi, xj) := ∥φ(xi) −φ(xj)∥H ,
so that
d2
ij = kii + kjj −2kij .
(9)
Therefore, it is possible to use Algorithm 1 for kernel data, even when H is not known
explicitly and/or when it is not ﬁnite-dimensional. This is an instance of the so-called
“kernel trick” (Schölkopf and Smola 2002). The associated Ward’s linkage can itself be
re-written directly using sums of elements of the kernel matrix, as shown, e.g., in Dehman
(2015):
δ(Gu, Gv) =
|Gu||Gv|
|Gu| + |Gv|
RGu,Gu
|Gu|2 + RGv,Gv
|Gv|2 −2 RGu,Gv
|Gu||Gv|

,
(10)
10

## Page 11

where RGu,Gv =
P
(xi,xj)∈Gu×Gv
kij.
Contrary to the dissimilarity case described in Section 3.1, the kernel case is a truly
interpretable generalization of Ward’s original approach because Ward’s linkage as calcu-
lated in (10) is the variation of within-cluster inertia in the associated Hilbert space H.
This case has been described previously in Qin et al. (2003); Ah-Pine and Wang (2016),
for instance.
3.3
Extension to similarity data
Similarity data also aim at describing pairwise resemblance relations between the objects
of Ωthrough a matrix of similarity (or proximity) measures S = (sij)1≤i,j≤n.
Even
though the precise deﬁnition of a similarity matrix can diﬀer within the literature (see
e.g., Hartigan (1967)), it is generally far less constrained than kernel matrices. In most
cases, the only conditions required to deﬁne a similarity is the symmetry of the matrix S
and the positivity of its diagonal. In some cases, similarity measures are also supposed
to take non negative values, but we will not make this assumption in the present article.
Since both similarities and kernels describe resemblance relations, it seems natural to try
to extend the background of Section 3.2 to similarity datasets by using Equation (10). This
allows the deﬁnition of a linkage, δS, between clusters via sums of elements of S. However,
this heuristic is not well justiﬁed since the quantity sii + sjj −2sij is not necessarily non
negative when S is not a positive deﬁnite kernel. Thus, it can not be associated to a
squared distance as in Equation (9).
The previous work of Miyamoto et al. (2015) has explicitly linked similarity and
kernel data in HAC results.
More precisely, for any given similarity S, the matrix
Sλ = (sλ
ij)1≤i,j≤n such that sλ
ij := sij +1{i=j}λ is deﬁnite positive for any λ larger than the
absolute value of the smallest eigenvalue of S. Therefore, the kernel matrix Sλ induces a
well-deﬁned linkage δSλ via Equation (10), which is linked to δS by:
δSλ(Gu, Gv) = δS(Gu, Gv) + λ .
11

## Page 12

This proposition justiﬁes the extension of Equation (10) to similarity data with
RGu,Gv = P
(xi,xj)∈Gu×Gv sij. Using this heuristic is indeed equivalent to using a given
kernel matrix obtained by translating the diagonal of the original similarity S: doing
so, the clustering is unchanged and the linkage values are all translated from +λ
for the kernel matrix, which does not even change the global shape of the clustering
representation when the heights in this representation are the values of the linkage (as
discussed in Section 4). However, as for general dissimilarity data in Section 3.1, the
interpretation of the linkage as a variation of within-cluster inertia is lost.
Conclusion.
In conclusion to this section, there is ﬁnally only two cases left: the Eu-
clidean case (in which objects are embedded in a direct or indirect manner in a Euclidean
framework) and the non-Euclidean case. The ﬁrst case includes the standard case, the
case of Euclidean distance matrices and the case of kernels while the latter case includes
general dissimilarity and similarity matrices. In the Euclidean case, the original descrip-
tion of the Ward’s algorithm is valid as such while, in the second, the algorithm can still
be formally applied in a very similar manner at the cost of a loss of the interpretability
of the criterion.
4
Interpretability of dendrograms
4.1
Dendrograms
The results of HAC algorithms are usually displayed as dendrograms. A dendrogram is a
binary tree in which each node corresponds to a cluster, and, in particular, the leaves are
the original objects to be clustered. The edges connect the two clusters (nodes) merged at
a given step of the algorithm. The height of the leaves is generally supposed to be h0 = 0.
In the case of OCHAC, these leaves are displayed as indicated by the natural ordering
of the objects, while in the general case of unconstrained HAC they are ordered by a
permutation of the class labels that ensures that the successive mergers are neighbors in
12

## Page 13

the dendrogram. The height of the node corresponding to the cluster created at merger t,
ht, is often the value of the linkage. To distinguish the height of the dendrogram from the
value of the linkage, we will denote by mt the value of the linkage at step t. Alternative
choices for the values of (ht)t are discussed in Section 4.4.
Dendrograms are used to obtain clusterings by horizontal cuts of the tree structure
at a chosen height. A desirable property of a dendrogram is thus that the clusterings
induced by such a cut corresponds to those deﬁned by the HAC algorithm. This property
is equivalent to the fact that the sequence of heights is non-decreasing. When this mono-
tonicity property is not satisﬁed, a merging step t for which ht < ht−1, is called a reversal.
Reversals can be of two types, depending on whether or not they correspond to a visible
crossover between branches of the dendrogram. Mathematically, a crossover corresponds
to the case when the height of a given merger Gv1 ∪Gv2 is less than the height of Gv1 or
the height of Gv2. A toy example of reversal with crossover is shown in Figure 1, between
nodes merged at steps 1 and 2, for the result of OCHAC.
The goal of this section is to study which settings and which deﬁnitions of height
guarantee the absence of reversals – with and without crossovers.
4.2
Monotonicity, crossovers and ultrametricity
A crossover in a dendrogram automatically implies the non-monotonicity of the sequence
of heights. The converse is true when the height of the dendrogram corresponds to the
value of the linkage (or to a non-decreasing function of the linkage) for the corresponding
merger, by virtue of Proposition 1 below.
Proposition 1. Consider a dendrogram whose sequence of heights (ht)t is a non-
decreasing transformation of the linkage values (mt)t. Then the only reversals that can
occur are crossovers.
The proof of Proposition 1 is not speciﬁc to Ward’s linkage and is a simple consequence
of the fact that the linkage is the objective function of the clustering:
Proof of Proposition 1. Consider an arbitrary merger step of the HAC, characterized by
13

## Page 14



x1
x2
x3

=


0
0
0.45
√
0.5
√
1.89875
√
0.5
0


D =


0
√
2
√
0.5
√
2
0
√
2.05
√
0.5
√
2.05
0


Figure 1: A crossover for Euclidean OCHAC with height deﬁned as the linkage
mt. Top left: Conﬁguration of the objects in R2. Top right : Coordinates of the objects
and Euclidean distance matrix corresponding to this conﬁguration. Bottom left: Repre-
sentation of the values of the Euclidean distance (dark colors correspond to larger values,
so to distant objects). Bottom right: Dendrogram obtained from OCHAC (the ordering is
indicated by the indices of objects) and with the height corresponding to Ward’s linkage.
14

## Page 15

the linkage value mt. If the next merger does not involve the newly created cluster, then
this merger was already a candidate at step t. Then, by optimality of the linkage value at
step t, this merger can not be a reversal. Therefore, any reversal must involve the newly
created cluster, and is thus a crossover.
An important consequence of Proposition 1 is that when the height of the dendrogram
is the corresponding linkage, the absence of crossovers is equivalent to the monotonicity
of the sequence of heights.
We shall see in Section 4.4 that for an arbitrary height, the absence of crossover
in the dendrogram is not necessarily equivalent to the monotonicity of the sequence of
heights. The absence of crossover can be characterized by a mathematical property of the
cophenetic distance associated to the heights of the dendrogram, called ultrametricity.
Formally, let us deﬁne, for all i, j ∈{1, . . . , n}, the cophenetic distance hij between i
and j as the value of the height ht∗such that t∗is the ﬁrst step (or the smallest merge
number) such that the i-th and j-th objects are in the same cluster. h is said to satisfy
the ultrametric inequality if:
∀i, j, k ∈{1, ..., n},
hij ≤max{hik, hkj}.
As announced, this property is key to ensure the monotonicity of the sequence of heights.
More precisely, Johnson (1967) has deﬁned an explicit bijection between a hierarchy of
clusterings with an associated sequence of non-decreasing “heights” (called “values” in the
article) and matrix of values with a diagonal equal to zero and satisfying the ultrametric
inequality. It turns out that this bijection explicitly deﬁnes the entries of the ultrametric
matrix as the cophenetic distance of the dendrogram whose heights are the one of the
associated hierarchy of clusterings. In other words, this means that a given sequence of
heights deﬁning a dendrogram is non-decreasing if and only if the cophenetic distance
associated to this dendrogram (or equivalently to this sequence of heights) satisﬁes the
ultrametric inequality.
15

## Page 16

4.3
Monotonicity of Ward’s linkage
Ward’s linkage corresponds to the variation of within-cluster inertia, so that the mono-
tonicity of the linkage is ensured for Ward’s standard HAC algorithm with Euclidean
data. More generally, Batagelj (1981) gives necessary and suﬃcient conditions based only
on the Lance-Williams coeﬃcients that ensures monotonicity for a given linkage. These
results apply to the extensions of HAC to non Euclidean datasets and show that the
monotonicity of the linkage values is always ensured for standard HAC with Ward’s link-
age. In addition, Ferligoj and Batagelj (1982) give necessary and suﬃcient conditions on
the Lance-Williams coeﬃcients to ensure the monotonicity of the linkage values in con-
strained HAC, for an arbitrary symmetric relational constraint. These conditions are not
fulﬁlled for Ward’s linkage. Therefore, monotonicity is not guaranteed for CCHAC with
Ward’s linkage, as also noted by Grimm (1987) for the speciﬁc case of OCHAC. It can be
shown that even for Euclidean data, the contiguity constraint can induce non increasing
linkage values for some steps of the algorithm, as illustrated by Figure 1.
More precisely, if we consider OCHAC, the following proposition establishes necessary
and suﬃcient conditions on a dissimilarity d to observe a reversal at a given step of
OCHAC when the height is deﬁned by Ward’s linkage:
Proposition 2. Suppose that Ω= {xi}i=1,...,n is equipped with the symmetric contiguity
relation xiRxj ⇔|i −j| = 1 (OCHAC). Denote by l and r the indices of the left and
right clusters merged at a given step t, and by ¯l and ¯r their own left and right cluster,
respectively. Then there is a reversal at step t + 1 for the height deﬁned by the linkage if
and only if:
δ(Gl, Gr) ≥min
g¯llδ(G¯l, Gl) + g¯lrδ(G¯l, Gr)
g¯ll + g¯lr
, gl¯rδ(Gl, G¯r) + gr¯rδ(Gr, G¯r)
gl¯r + gr¯r

(11)
where we have used the notation guv := |Gu ∪Gv| = |Gu| + |Gv|.
The fact that Condition (11) involves clusters contiguous to the last merger is a conse-
quence of Proposition 1. The formulation of Condition (11) is quite intuitive: crossovers
correspond to situations in which the Ward linkage between two newly merged clusters
16

## Page 17

is larger than a (weighted) average Ward linkage between each of these two clusters and
one of the contiguous clusters. The proof of Proposition 2 is given in Appendix A.
Let us apply Proposition 2 to the speciﬁc case of the ﬁrst and second mergers in the al-
gorithm. Assuming that the optimal merger at step 1 is between the l-th and r-th objects,
and recalling that the Ward linkage between two singletons is simply δ({u}, {v}) = d2
uv/2,
Condition (11) reduces to:
2d2
l,r > min

d2
¯l,l + d2
¯l,r, d2
r,¯r + d2
l,¯r

In particular, given the p −1 distances (d2
i,i+1)1≤i≤p−1 that determine the ﬁrst step of the
OCHAC algorithm, it is always possible to ﬁnd an adversarial dissimilarity yielding a
reversal at the second step, e.g., by choosing dl,¯r such that d2
l,¯r < 2d2
l,r −d2
r,¯r. This is the
case in the counter-example of Figure 1.
An example of relevant reversal for OCHAC.
Because of the possible presence
of crossovers in OCHAC even in a simple Euclidean setting, CCHAC may appear as
a deteriorated version of standard HAC, where the optimal merger is chosen within a
reduced set of possible mergers compared to the unconstrained version. One may then
expect that the total within-cluster inertia at a given step of the algorithm is larger
than for the unconstrained version that chooses the “optimal” merger at this step (that
is, the merger with the smallest increase of the total within-inertia). In addition, the
algorithm does not necessarily exhibit a clear and understandable monotonic evolution of
the objective criterion, (mt)t. However, it can be shown, even in a very simple example,
that OCHAC can lead to better solutions in terms of within-cluser intertia, when the
constraint is consistent to the spatial structure of the data. This fact is illustrated in
Figure 2 (detailed analysis of all examples and counter-examples of this section is provided
in Appendix C). In this example, 7 data points are displayed in R2 with an order constraint
illustrated by a line linking two points allowed to be merged. In this situation, (mt)t is
indeed non monotonic for OCHAC (bottom left ﬁgure) but leads to a better total within-
cluster inertia for k = 3 clusters (vertical green line), which is also more relevant for
17

## Page 18

the data conﬁguration (top ﬁgures). This is a typical case where the constraint forces
the algorithm to explore under-eﬃcient conﬁgurations but that can be aggregated into a
better solution, contrary to the unconstrained algorithm. This is explained by the fact
that even the unconstrained algorithm is greedy, by construction, and thus not optimal
compared to an exhaustive search of the best partition in k classes.
Figure 2: Simple conﬁguration in which OCHAC outperforms standard HAC.
Top left: Initial conﬁguration with the order constraint represented by straight lines. Top
right: Clustering with 3 clusters as produced by OCHAC (red) and standard HAC (blue).
Bottom: Evolution of (mt)t and of the total within-cluster inertia (also called, Error Sum
of Squares: (ESSt)t) along the clustering processes, the green line correspond to the 3
components clustering.
18

## Page 19

4.4
Monotonicity of alternative heights
Since reversals can occur in CCHAC dendrograms with Ward’s linkage, alternative deﬁ-
nitions of the height have been proposed to improve the interpretability of the result in
this case. They are deﬁned as quantities related to the heterogeneity of the partition. In
this section, we study the monotonicity of such alternative heights.
Grimm (1987) presents three alternative heights to the standard variation of within-
cluster inertia (mt):
• the within-cluster (pseudo-)inertia (or Error Sum of Squares) that corresponds to
the value of the objective function. In this case, the height at step t is given by:
ESSt =
n−t
X
u=1
I(Gt+1
u ),
where Pt+1 = {Gt+1
u }u=1,...,n−t is the partition obtained at step t of the algorithm.
This alternative height is very natural (and the one implemented in the R pack-
age rioja (Juggins 2012) for OCHAC) since it corresponds to the criterion whose
minimization is approximated by HAC (and OCHAC) in a greedy way;
• the (pseudo-)inertia of the current merger, which is deﬁned as:
It = I(Gt
u ∪Gt
v)
where Gt
u and Gt
v are the two clusters merged at step t. Grimm (1987) remarks that
this measure is very sensitive to the cluster size |Gt
u| + |Gt
v|.
• the average (pseudo-)inertia of the current merger, that has been designed so as to
avoid the bias related to the cluster size in It. It is deﬁned as:
It =
It
|Gt
u| + |Gt
v|
Standard HAC: Known properties of alternative heights.
Note that ESSt =
P
t′≤t mt′. As explained in Section 4, (mt)t is monotonic for standard HAC, both for Eu-
19

## Page 20

clidean and non Euclidean data. Since m0 = 0 by deﬁnition, this ensures the monotonicity
of (ESSt)t, for Euclidean and non Euclidean data in the case of standard HAC.
On the contrary, It and It may induce reversals even for standard HAC and Euclidean
data. More importantly, contrary to the case when the height of the dendrogram is mt,
even when the ultrametric property is satisﬁed, the monotonicity is not ensured for these
criteria. This is illustrated in Figure 3 (and in Figure 11 of the Appendix B), for It (and
for ¯It, respectively) and data in R2.
In this case, the dendrogram has a conventional look but the mergers are not ordered
by increasing heights. For instance, in Figure 3, the cluster merged at step 2 is above the
one at step 3. Hence, cutting the dendrogram at height h = 2.5 leads to a clustering into
{x1, x2}, {x3}, {x4, x5}, but this clustering does not belong to the sequence of clusterings
induced by the HAC (where the clustering in 3 clusters is the one obtained after the
second merger, that is, {x1, x2, x3}, {x4}, {x5}).
CCHAC: Known properties of alternative heights.
Figures 3 and 11 (the latter
in Appendix B) provide counter-examples for the monotonicity of (It)t and (¯It)t in the
Euclidean case for HAC. If the objects are pre-ordered as the nodes in these ﬁgures,
then OCHAC and standard HAC give identical hierarchical clusterings. Therefore, these
examples also provide counter-examples for the monotonicity of (It)t and (¯It)t in the
Euclidean case for OCHAC, and show that there is no guarantee for monotonicity in the
case of general CCHAC. The fact that (¯It)t is not necessarily monotonous for OCHAC
has already been mentioned by Grimm (1987).
CCHAC: Within-cluster pseudo-inertia for dissimilarity data.
The only unan-
swered case is whether (ESSt)t is monotonic or not for CCHAC and non Euclidean
data. We provide a counter-example that proves that the monotonicity is not ensured in
this case: Figure 4 shows that the dendrogram obtained from OCHAC on a given non-
Euclidean dissimilarity D contains a crossover (m4 < m3). In particular, the associated
sequence of heights is not monotonic. However, Proposition 1 ensures that (ESSt)t has the
nice property that the absence of crossovers is equivalent to its monotonicity. Indeed, as
20

## Page 21







x1
x2
x3
x4
x5






=






1
2
√
3
2
−1
2
√
3
2
0
−1
10
0
10
2.16






D ≈






0.00
1.00
1.93
9.54
9.59
1.00
0.00
1.93
10.54
10.58
1.93
1.93
0.00
10.05
10.49
9.54
10.54
10.05
0.00
2.16
9.59
10.58
10.49
2.16
0.00






Figure 3: A reversal for Euclidean standard HAC with height deﬁned as It.
Top left: Conﬁguration of the objects in R2. Top right: Coordinates of the objects and
Euclidean distance matrix corresponding to this conﬁguration. Bottom left: Represen-
tation of the values of the dissimilarity (dark colors correspond to larger values, so to
distant objects). Bottom right: dendrogram obtained from standard HAC. Only the ﬁrst
3 merges of the dendrogram is represented to ensure a comprehensive view of the sequence
of heights.
21

## Page 22

(ESSt)t corresponds to the cumulative sums of the linkage (mt)t, the mapping between mt
and ESSt is equal to the addition of ESSt−1. As, by deﬁnition, ESSt−1 is, as any I(Gt−1
u ),
positive, this ensures that this mapping is non-decreasing.
Table 1 summarizes the properties of the diﬀerent types of heights, respectively for
standard HAC and CCHAC. Note that the monotonicity of ESSt is a consequence of the
positivity of mt.
mt
ESSt
It
It
HAC
Euclidean
Ward (1963)
Ward (1963)
 [Fig. 3]
[Fig. 11]
Non Euclidean
Batagelj (1981)
Batagelj (1981)
 [Fig. 3]
[Fig. 11]
CCHAC
Euclidiean
Grimm (1987)
Grimm (1987)
 [Fig. 3]
Grimm (1987)
Non Euclidean
Grimm (1987)
 [Fig. 4]
 [Fig. 3]
Grimm (1987)
Table 1: Monotonicity of heights for standard HAC (top) and CCHAC (bottom).
22

## Page 23

D =









0
√
1.99
√
1.99
√
1.99
0.1
1
√
1.99
0
√
2
√
1.99
0.1
1
√
1.99
√
2
0
√
2
0.1
1
√
1.99
√
1.99
√
2
0
√
2
1
0.1
0.1
0.1
√
2
0
√
2
1
1
1
1
√
2
0









Figure 4: A reversal for non-Euclidean OCHAC with height deﬁned as ESSt.
Top: Dissimilarity matrix. Bottom left: Representation of the values of the dissimilarity D
(dark colors correspond to larger values, so to distant objects). Bottom right: Dendrogram
obtained from OCHAC (the ordering is indicated by the indices of objects) and with the
height corresponding to ESSt.
23

## Page 24

5
Simulation
HAC can be seen as a greedy algorithm to solve the problem of ﬁnding the partition with
minimal within-cluster inertia ESSt of n objects into n −t classes, for each t = 1 . . . n −1.
It may be expected that the inertia of the partitions will be lower for HAC than OCHAC,
since the possible mergers in OCHAC are chosen among a subset of the possible mergers in
HAC. Can we quantify the impact of the order constraint on the quality of the partitions
(as measured by ESS) obtained for HAC and OCHAC, depending on the strength of the
actual order structure in the data? In this section, we address this question by analyzing
Hi-C data (Dixon et al. 2012), which present a strong order structure, as illustrated by
Figure 5. We use a perturbation process to progressively break the consistency between
the data structure and the constraint imposed in OCHAC.
5.1
Data and method
Hi-C studies aim at characterizing proximity relationships in the 3D structure of a genome,
by measuring the frequency of physical interaction between pairs of genomic locations via
sequencing experiments. Formally, an Hi-C map is a symmetric matrix S = (sij)i,j in
which each entry sij is equal to the frequency of interaction between genomic loci i and
j. Here, a locus is a ﬁxed-size interval of genomic positions, also called a “bin”. Hi-C
maps are classically represented by the upper triangular part of the matrix, as shown in
Figure 5. The matrix has a strong diagonal structure that reﬂects the linear order of DNA
within chromosomes (loci that are close along the genome are more frequently interacting
than distant loci). An important question in Hi-C studies is to identify Topologically
Associating Domains (TADs), which are self-interacting genomic regions appearing to
be more compact than the rest of the genome. Indeed, TADs have been shown to play
an important role in gene regulation (Dixon et al. 2012). A number of TAD detection
methods have been proposed (see e.g., Zuﬀerey et al. (2018) for a review) and some are
based on HAC or OCHAC (Fraser et al. 2015; Haddad et al. 2017; Ambroise et al. 2019).
This is both natural, since Hi-C maps can be seen as similarity matrices, and formally
justiﬁed, as explained in Section 3.3.
24

## Page 25

Figure 5: Graphical representation of an Hi-C map. Horizontal position is deﬁned
by the indices of bins within a single chromosome. Intensities of the frequency of physical
interaction between bins are represented by levels of red.
The simulations in this section are based on a single chromosome (chromosome 3)
from an experiment in human embryonic stem cells (hESC; Dixon et al. (2012)1). The
downloaded Hi-C matrix contains 4,864 bins. It has been obtained with a bin size of
40kb and normalized using ICE (Imakaev et al. 2012).
We further performed a log-
transformation of the entries to reduce the distribution skewness prior clustering.
In order to assess the inﬂuence of the data structure on the quality of the partitions
obtained by OCHAC and standard HAC algorithms, we have used a perturbation process
to progressively remove the strong diagonal in the original Hi-C map. The perturbation
consists in swapping two entries, sij and si′j′ of the matrix, in which (i, j) and (i′, j′) have
been randomly sampled with uniform probability among the pairs {(u, v), (u′, v′)} for
which u ≤v, u′ ≤v′ and suv + su′v′ > 0, where the last condition avoids swapping entries
that are both zero. The proportion of such swapped pairs, which we call perturbation
level, varied from 0% up to 90% (Figure 6).
This process was repeated 50 times to allow assessing the variability. Since obtained
matrices are not necessarily positive deﬁnite, we translate their diagonal by a small quan-
1The pre-processed and normalized data have been downloaded from the authors’ website at http:
//chromosome.sdsc.edu/mouse/hi-c/download.html (raw sequence data are also published on the
GEO website, accession number GSE35156).
25

## Page 26

Figure 6: Illustration of the perturbation process. From left to right : example of
Hi-C maps corresponding to increasing perturbation levels.
tity that ensures the positivity of all d2
ij = sii + sjj −2sij as described in Section 3.2.
All simulations were performed with R. The results for standard HAC were computed
with the function hclust (from the stats package) and those for OCHAC were computed
with the function adjClust (from the adjclust package). Figures were obtained using
adjClust or ggplot2 (Wickham 2016).
5.2
Comparison of standard HAC and OCHAC results
In this section, the results of standard HAC and OCHAC are compared through the
corresponding height sequences the dendrograms, and through clusterings obtained by
horizontal cuts of the dendrograms. While the ﬁrst two are a direct output of the HAC
process, clusterings are obtained using a model selection strategy. We have considered
two such strategies: the broken stick (Bennett 1996), as implemented in adjclust, and
the slope heuristic (Arlot et al. 2016), as implemented in capushe. As both of them gave
similar results, we chose to report here only the results obtained for the broken stick
heuristic.
Height sequences.
Figure 7 shows the evolution of mt (normalized by its maximal
value among both methods at a given permutation level) and ESSt (normalized by the total
inertia of the set of bins) along the two clustering processes for increasing perturbation
levels. For the original dataset, which presents an organization strongly consistent with
the order constraint, the heights of standard HAC and OCHAC are very similar. However,
interestingly, OCHAC improves the objective criteria (ESSt and mt) for low perturbation
levels (15%-30%) across a wide range of merging levels.
26

## Page 27

More speciﬁcally, we compared the heights obtained for HAC and OCHAC at the
merger number selected by the broken stick heuristic (Bennett (1996); vertical lines in
Figure 7). At these numbers of clusters or in their close neighbourhood, ESSt is always
smaller for OCHAC, which we interpret as more homogeneous clusterings for OCHAC
than for HAC. The magnitude of the improvement achieved by OCHAC with respect to
HAC depends on the perturbation level: for the original data, it is close to 5%, whereas it
is much larger (25-30%) when the perturbation level is 15%-30%. It then decreases again
(< 20%) for larger perturbation levels (60%).
The fact that OCHAC can achieve lower values than HAC for ESSt and mt may be
counter-intuitive, since –as explained at the beginning of Section 5– possible mergers in
OCHAC are chosen among only a subset of the possible mergers in standard HAC. In
fact, HAC itself is a heuristic for the minimization of ESSt, because of its hierarchical
agglomerative nature; in contrast, the optimal clustering at step t in the sense of ESSt
may not necessary be obtained by merging two clusters of the optimal clustering at step
t −1. This result illustrates the robustness to noise of the constrained approach, which
is very interesting in practice: in Hi-C experiments, for instance, many biases (genomic,
experimental, etc.) are encountered. Thus, OCHAC has to be preferred in such contexts
and will additionally result in a lower computational cost.
For perturbation levels larger than 60%, the data structure is no more compatible with
the constraint (see Figure 6) and standard HAC seems to performs globally better than
OCHAC, as expected. In addition, in this extreme situation, OCHAC exibits very large
reversals in mt values (seen with the grey shadow in Figure 7), that are due to sudden
breaks in the quality of the clusterings, induced by the constraint. The presence of such
large reversals is a practical and visible indication that the constraint is not relevant for
the data and that OCHAC should not be used.
Dendrograms and clusterings.
The same type of conclusion can be drawn when
comparing not just the heights of the dendrograms but the dendrograms themselves or
the clusterings induced by these dendrograms. Figure 8 shows the distribution of Baker’s γ
coeﬃcients (Baker 1974) between the dendrograms of standard HAC and OCHAC versus
27

## Page 28

Figure 7: Comparison of the height sequences for standard HAC (red, solid)
and OCHAC (blue, dashed) for ESSt (top) and mt (bottom) with various levels of
perturbations of the original Hi-C matrix. The curves correspond to the average criteria
over 50 simulations and the grey shadows correspond to the minimum and maximum of
the criteria over 50 simulations. The vertical lines correspond to the average number of
clusters chosen by the broken stick heuristic, respectively for standard HAC and OCHAC
(red, solid and blue, dashed).
the perturbation level. This coeﬃcient corresponds to the Spearman correlation between
the pairwise values of the cophenetic distances between pairs of objects as induced by
the dendrogram. As the perturbation level increases, Baker’s γ linearly decreases from
a value close to 1 (implying very similar dendrograms) to a value close to 0 (implying
completely diﬀerent dendrograms).
Finally, we compared the clusterings obtained by the broken stick heuristic (Bennett
1996) as follows. For larger perturbation levels (more than 60%) of permuted coeﬃcients,
we obtained a trivial clustering with only one cluster, a strong indication that the cluster
structure had disappeared at these levels. For lower perturbation levels, the obtained
clusterings were compared using the Normalized Mutual Information (NMI, Danon et al.
(2005)). As for Baker’s γ, the NMI values obtained for the original data and low levels
of perturbations (up to 30%) are very close to 1, which shows a strong similarity of the
induced clusterings. As the perturbation level increases, the obtained partitions became
28

## Page 29

0.00
0.25
0.50
0.75
0
25
50
75
percentage of permuted coefficients
Baker's γ coefficient
Figure 8: Baker’s γ coeﬃcient between OCHAC and standard HAC dendro-
grams versus perturbation level.
more and more diﬀerent, with NMI values below 0.6 (results not shown).
5.3
Reversals for the diﬀerent heights
In this section, we investigate the reversals obtained for diﬀerent heights and for standard
HAC and OCHAC. Figure 9 gives the evolution of the percentage of reversals (relative to
the total number of simulations, 50), for standard HAC and OCHAC and for the diﬀerent
types of heights, along the hierarchical clustering process.
As expected from Section 3 (Table 1), (ESSt)t does not have reversals and (mt)t
only has reversals for OCHAC. When the perturbation level increases, the evolution of
the number of reversals in (It)t and (¯It)t is markedly diﬀerent from that of (mt)t. For
the smallest perturbation levels (up to 30%), the number of reversals of (mt)t is close
to 0, while it ranges from 10 to 50% for (It)t and (¯It)t. At these perturbation levels,
(mt)t almost never has a reversal at a merger number that corresponds to the number
of clusters chosen by the broken stick heuristic: most reversals are concentrated at a
merger number smaller than the merger chosen by the broken stick heuristic. Actually,
29

## Page 30

15% permuted
30% permuted
60% permuted
90% permuted
unconstrained (HAC)
constrained (OCHAC)
0
2500
50000
2500
50000
2500
50000
2500
5000
0.00
0.25
0.50
0.75
0.00
0.25
0.50
0.75
merger number
proportion of reversals (over 50 simulations)
heights
ESSt
mt
It
It
Figure 9: Evolution of the number of reversals for ESSt, mt, It and ¯It for standard
HAC (top) and OCHAC (bottom) for increasing levels of perturbation of the original Hi-C
matrix. The background shadow is the actual value and the strong line is a smoothed
value (box kernel, bandwith equal to 50). The dotted vertical line corresponds to the
average number of clusters chosen by the broken stick heuristic.
for small perturbation levels, these reversals in mt values help improve the quality of
further clusterings by choosing a solution that is less eﬃcient than that of standard HAC
but more consistent with the data (as already discussed in the example of Figure 2).
Hence, when the data structure is consistent with the constraint, (mt)t typically provides
an interpretable dendrogram. This nice property is, of course, lost when the constraint is
no more consistent with the data structure (above a perturbation level of 60%), which is
explained by the fact that the OCHAC has a poor performance in that context, as already
discussed in the previous section.
On the contrary, (It)t and (¯It)t exhibit larger numbers of reversals. This is partic-
ularly the case for the last mergers, even for small levels of perturbation and even in
the unconstrained case: 40-60% of the simulations have reversals for both OCHAC and
standard HAC at a number of clusters corresponding to the selected clustering. We also
observe that the percentage of simulations showing a reversal for standard HAC tends
to decrease when the perturbation level in the data increases for the ﬁrst steps of the
30

## Page 31

hierarchical process (the same can be observed, to a much lesser extent, for OCHAC).
This phenomenon is explained below.
Figure 10: Evolution of the average cardinal of mergers along the hierarchical
clustering process for standard HAC (top) and OCHAC (bottom), and diﬀerent levels
of perturbation. Note that the average is computed over the 50 simulations, whereas the
original data correspond to a unique value. Data are shown only for the ﬁrst 4,000 mergers
and for a cardinal smaller than 8 for the sake of readability. The two dotted vertical lines
correspond, respectively to n/2 and 3n/4.
Figure 10 displays the evolution of the merged cluster size thorough the hierarchical
clustering and provides an explanation for this fact. For standard HAC, the number of
clusters with a size equal to 2 during the ﬁrst steps of the algorithm is strongly increasing
when the perturbation level increases. For a permutation level of 90%, most of the mergers
have a size equal to 2 during half of the clustering process (for fusion numbers ranging from
1 to at least 2,000). However, for clusters with a size equal to 2, It is equal to mt which
explains the similiarities between mt and It curves during the ﬁrst steps of the clustering
process, as the perturbation level increases. Since (mt)t is increasing for standard HAC,
this explains why It has less reversals in standard HAC for the ﬁrst merger numbers when
the perturbation level is higher. The same holds for ¯It up to a ﬁxed size factor of 2.
31

## Page 32

6
Conclusion
In this article, we studied the applicability of HAC and its constrained version to a wide
range of input data. In particular, we have shown that these applications are justiﬁed
beyond the Euclidean framework.
We have also shown that the monotonicity of the
sequence of heights is not always ensured, although this property is necessary for the se-
quence of clusterings obtained by cutting dendrograms to be consistent with the sequence
of clusterings of the algorithm. We have clariﬁed which heights have this property de-
pending on the input data types and for the constrained and unconstrained HAC. We have
also pinpointed an important distinction between this monotonicity and the existence of
crossovers.
These results imply that the variance of the merged cluster, It, or the average variance
of the merged cluster, ¯It, are never ensured to be monotonic, and should thus not be
chosen to represent the dendrogram heights. Strikingly, we have also shown that the
constrained version of the HAC can provide more relevant and eﬃcient solutions than its
unconstrained versions, not only in terms of algorithmic complexity, but also in terms of
the values of the objective function ESSt. In such cases, a small number of reversals can
actually be beneﬁcial to explore intermediate solutions closer to the data and that lead
to more relevant clusters.
Acknowledgements
The authors would like to thank Marie Chavent for numerous instructive discussions on
this paper.
The authors are grateful to the GenoToul bioinformatics platform (INRA Toulouse,
http://bioinfo.genotoul.fr/) and its staﬀfor providing computing facilities.
32

## Page 33

Funding
The PhD thesis of N.R. is funded by the INRA/Inria doctoral program 2018.
This
work was also supported by the SCALES project funded by CNRS (Mission “Osez
l’interdisciplinarité”).
References
Ah-Pine, J. and Wang, X. (2016). Similarity based hierarchical clustering with an appli-
cation to text collections. In Boström, H., Knobbe, A., Soares, C., and Papapetrou, P.,
editors, Proceedings of the 15th International Symposium on Intelligent Data Analysis
(IDA 2016), Lecture Notes in Computer Sciences, pages 320–331, Stockholm, Sweden.
Ambroise, C., Dehman, A., Neuvial, P., Rigaill, G., and Vialaneix, N. (2019). Adjacency-
constrained hierarchical clustering of a band similarity matrix with application to ge-
nomics. arXiv preprint arXiv:1902.01596.
Arlot, S., Brault, V., Baudry, J.-P., Maugis, C., and Michel, B. (2016). capushe: CAli-
brating Penalities Using Slope HEuristics. R package version 1.1.1.
Aronszajn, N. (1950).
Theory of reproducing kernels.
Transactions of the American
Mathematical Society, 68(3):337–337.
Baker, F. B. (1974). Stability of two hierarchical grouping techniques case I: sensitivity
to data errors. Journal of the American Statistical Association, 69(346):440–445.
Batagelj, V. (1981). Note on ultrametric hierarchical clustering algorithms. Psychome-
trika, 46(3):351–352.
Bennett, K. D. (1996). Determination of the number of zones in a biostratigraphical
sequence. New Phytologist, 132(1):155–170.
Chavent, M., Kuentz-Simonet, V., Labenne, A., and Saracco, J. (2018). ClustGeo2: an R
package for hierarchical clustering with spatial constraints. Computational Statistics,
33(4):1799–1822.
33

## Page 34

Chen, J. and Ye, J. (2008). Training SVM with indeﬁnite kernels. In Cohen, W., McCal-
lum, A., and Roweis, S., editors, Proceedings of the 25th International Conference on
Machine Learning (ICML 2008), pages 136–146, Helsinki, Finland. ACM, New York,
NY, USA.
Chen, Y., Garcia, E., Gupta, M., Rahimi, A., and Cazzanti, L. (2009). Similarity-based
classiﬁcation: concepts and algorithm. Journal of Machine Learning Research, 10:747–
776.
Danon, L., Diaz-Guilera, A., Duch, J., and Arenas, A. (2005). Comparing community
structure identiﬁcation.
Journal of Statistical Mechanics: Theory and Experiment,
2005:P09008.
Dehman, A. (2015). Spatial Clustering of Linkage Disequilibrium Blocks for Genome-Wide
Association Studies. PhD thesis, Université Paris Saclay.
Dixon, J., Selvaraj, S., Yue, F., Kim, A., Li, Y., Shen, Y., Hu, M., Liu, J., and Ren, B.
(2012). Topological domains in mammalian genomes identiﬁed by analysis of chromatin
interactions. Nature, 485:376–380.
Ferligoj, A. and Batagelj, V. (1982). Clustering with relational constraint. Psychometrika,
47(4):413–426.
Fraser, J., Ferrai, C., Chiariello, A. M., Schueler, M., Rito, T., Laudanno, G., Barbieri,
M., Moore, B. L., Kraemer, D. C., Aitken, S., Xie, S. Q., Morris, K. J., Itoh, M., Kawaji,
H., Jaeger, I., Hayashizaki, Y., Carninci, P., Forrest, A. R., The FANTOM Consortium,
Semple, C. A., Dostie, J., Pombo, A., and Nicodemi, M. (2015). Hierarchical folding
and reorganization of chromosomes are linked to transcriptional changes in cellular
diﬀerentiation. Molecular Systems Biology, 11:852.
Grimm, E. C. (1987). CONISS: a FORTRAN 77 program for stratigraphically constrained
analysis by the method of incremental sum of squares.
Computers & Geosciences,
13(1):13–35.
34

## Page 35

Haddad, N., Vaillant, C., and Jost, D. (2017). IC-Finder: inferring robustly the hierar-
chical organization of chromatin folding. Nucleic Acids Research, 45(10):e81–e81.
Hartigan, J. A. (1967). Representation of similarity matrices by trees. Journal of the
American Statistical Association, 62(320):1140–1158.
Imakaev, M., Fudenberg, G., McCord, R., Naumova, N., Goloborodko, A., Lajoie, B.,
Dekker, J., and Mirny, L. (2012). Iterative correction of Hi-C data reveals hallmarks of
chromosome organization. Nature Methods, 9(10):999–1003.
Johnson, S. C. (1967). Hierarchical clustering schemes. Psychometrika, 32(3):241–254.
Juggins, S. (2012). rioja: Analysis of Quaternary Science Data. CRAN, Newcastle, UK.
Krislock, N. and Wolkowicz, H. (2012). Handbook on Semideﬁnite, Conic and Polynomial
Optimization, volume 166 of International Series in Operations Research & Manage-
ment Science, chapter Euclidean distance matrices and applications, pages 879–914.
Springer, New York, Dordrecht, Heidelberg, London.
Kruskal, Joseph, B. (1964). Multidimensional scaling by optimizing goodness of ﬁt to a
nonmetric hypothesis. Psychometrika, 29(1):1–27.
Lance, G. and Williams, W. (1967). A general theory of classiﬁcatory sorting strategies:
1. Hierarchical systems. The Computer Journal, 9(4):373–380.
Lebart, L. (1978). Programme d’agrégation avec contraintes. Les Cahiers de l’Analyse
des Données, 3(3):275–287.
Miyamoto, S., Abe, R., Endo, Y., and Takeshita, J.-I. (2015). Ward method of hier-
archical clustering for non-Euclidean similarity measures. In Proceedings of the VIIth
International Conference of Soft Computing and Pattern Recognition (SoCPaR 2015),
Fukuoka, Japan. IEEE.
Murtagh, F. and Legendre, P. (2014).
Ward’s hierarchical agglomerative clustering
method:
which algorithms implement Ward’s criterion.
Journal of Classiﬁcation,
31(3):274–295.
35

## Page 36

Qin, J., Lewis, D. P., and Noble, W. S. (2003). Kernel hierarchical gene clustering from
microarray expression data. Bioinformatics, 19(16):2097–2104.
Schleif, F.-M. and Tino, P. (2015).
Indeﬁnite proximity learning: a review.
Neural
Computation, 27(10):2039–2096.
Schoenberg, I. (1935). Remarks to Maurice Fréchet’s article “Sur la déﬁnition axioma-
tique d’une classe d’espace distanciés vectoriellement applicable sur l’espace de Hilbert”.
Annals of Mathematics, 36:724–732.
Schölkopf, B. and Smola, A. J. (2002). Learning with Kernels: Support Vector Machines,
Regularization, Optimization, and Beyond. MIT Press.
Strauss, T. and von Maltitz, M. J. (2017). Generalising Ward’s method for use with
Manhattan distances. PLoS ONE, 12:e0168288.
Székely, G. J. and Rizzo, M. L. (2005). Hierarchical clustering via joint between-within
distances: extending Ward’s minimum variance method.
Journal of Classiﬁcation,
22(2):151–183.
Ward, J. H. (1963). Hierarchical grouping to optimize an objective function. Journal of
the American Statistical Association, 58(301):236–244.
Wickham, H. (2016). ggplot2: Elegant Graphics for Data Analysis. Springer-Verlag, New
York, USA.
Wishart, D. (1969). An algorithm for hierarchical classiﬁcations. Biometrics, 25(1):165–
170.
Young, G. and Householder, A. (1938). Discussion of a set of points in terms of their
mutual distances. Psychometrika, 3:19–22.
Zuﬀerey, M., Tavernari, D., Oricchio, E., and Ciriello, G. (2018). Comparison of compu-
tational methods for the identiﬁcation of topologically associating domains. Genome
biology, 19(1):217.
36

## Page 37

Appendix
A
Proof of Proposition 2
Proof of Proposition 2. We begin by noting that by Proposition 1, the only reversals that
may occur are crossovers. With the notation of Proposition 2, a crossover at step t + 1
corresponds to the situation where
δ(Gl, Gr) ≥δ(Gl ∪Gr, G¯r) or δ(Gl, Gr) ≥δ(Gl ∪Gr, G¯l).
By symmetry we focus on the ﬁrst case. With the notation of Proposition 2, and using
the Lance-Willams formula (4), the ﬁrst condition is equivalent to
δ(Gl, Gr) ≥glr′δ(Gl, G¯r) + grr′δ(Gr, G¯r)
glr′ + grr′
while the second one is equivalent to
δ(Gl, Gr) ≥g¯llδ(G¯l, Gl) + g¯lrδ(G¯l, Gr)
g¯ll + g¯lr
hence the result.
37

## Page 38

B
Counter-example of the monotonicity of ¯It for stan-
dard HAC in the Euclidean case












x1
x2
x3
x4
x5












=












1
2
√
3
2
−1
2
√
3
2
0
−1
10
0
10
2.15












D ≈












0.00
1.00
1.93
9.54
9.59
1.00
0.00
1.93
10.54
10.58
1.93
1.93
0.00
10.05
10.48
9.54
10.54
10.05
0.00
2.15
9.59
10.58
10.48
2.15
0.00












Figure 11: A reversal for Euclidean standard HAC with height deﬁned as ¯It. Top
left: Conﬁguration of the objects in R2. Top right: Coordinates of the objects and Eu-
clidean distance matrix corresponding to this conﬁguration. Bottom left: Representation
of the values of the dissimilarity (dark colors correspond to larger values, so distant ob-
jects). Bottom right: dendrogram obtained from standard HAC. Only the ﬁrst 3 merges of
the dendrogram is represented to ensure a comprehensive view of the sequence of heights.
38

## Page 39

C
Step-by-step description of the counter-examples
In the following tables, red color is used to signal reversals. Green color in details of
Figure 2 is used to highlight the value of the objective function (ESSt) for the clustering
with 3 clusters.
Merger
cluster 1
cluster 2
mt
ESSt
It
It
1
{x1}
{x2}
1.000
1.000
1.000
0.500
2
{x1, x2}
{x3}
0.517
1.517
1.517
0.506
Table 2: Details of Figure 1
OCHAC
Merger
cluster 1
cluster 2
mt
ESSt
It
It
1
{x1}
{x2}
2.500
2.500
2.500
1.250
2
{x1, x2}
{x3}
2.167
4.667
4.667
1.556
3
{x6}
{x7}
2.500
7.167
2.500
1.250
4
{x5}
{x6, x7}
2.167
9.333
4.667
1.556
5
{x1, x2, x3}
{x4}
13.333
22.667
18.000
4.500
6
{x1, x2, x3, x4}
{x5, x6, x7}
20.762
43.429
43.429
6.204
HAC
Merger
cluster 1
cluster 2
mt
ESSt
It
It
1
{x2}
{x6}
0.500
0.500
0.500
0.250
2
{x1}
{x3}
2.000
2.500
2.000
1.000
3
{x5}
{x7}
2.000
4.500
2.000
1.000
4
{x2, x6}
{x1, x3}
6.250
10.750
8.750
2.188
5
{x4}
{x1, x2, x3, x6}
13.250
24.000
22.000
4.400
6
{x5, x7}
{x1, x2, x3, x4, x6}
19.429
43.429
43.429
6.204
Table 3: Details of Figure 2
39

## Page 40

Merger
cluster 1
cluster 2
mt
ESSt
It
It
1
{x1}
{x2}
0.50
0.50
0.50
0.25
2
{x1, x2}
{x3}
2.32
2.82
2.82
0.94
3
{x4}
{x5}
2.33
5.15
2.33
1.17
4
{x1, x2, x3}
{x4, x5}
120.84
125.99
125.99
25.20
Table 4: Details of Figure 3
Merger
cluster 1
cluster 2
mt
ESSt
It
It
1
{x1}
{x2}
0.995
0.995
0.995
0.498
2
{x1, x2}
{x3}
0.998
1.993
1.993
0.664
3
{x1, x2, x3}
{x4}
0.997
2.990
2.990
0.748
4
{x1, x2, x3, x4}
{x5}
-0.192
2.798
2.798
0.560
5
{x1, x2, x3, x4, x5}
{x6}
0.534
3.332
3.332
0.555
Table 5: Details of Figure 4
Merger
cluster 1
cluster 2
mt
ESSt
It
It
1
{x1}
{x2}
0.50
0.50
0.50
0.25
2
{x4}
{x5}
2.31
2.81
2.31
1.16
3
{x1, x2}
{x3}
2.32
5.13
2.82
0.94
4
{x1, x2, x3}
{x4, x5}
120.83
125.96
125.96
25.19
Table 6: Details of Figure 11
40
