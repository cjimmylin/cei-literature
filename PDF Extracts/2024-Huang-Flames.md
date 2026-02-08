---
title: "2024-Huang-Flames - PDF Extract"
source_pdf: "2024-Huang-Flames.pdf"
pages: 8
extracted_at: "2026-02-08T06:02:18.864584"
---

# PDF Extract: 2024-Huang-Flames

**Source PDF:** 2024-Huang-Flames.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

GREEDOIDS FROM FLAMES
ATTILA JOÓ
Abstract. A digraph D with r ∈V (D) is an r-ﬂame if for every v ∈V (D) −r, the
in-degree of v is equal to the local edge-connectivity λD(r, v). We show that for every
digraph D and r ∈V (D), the edge sets of the r-ﬂame subgraphs of D form a greedoid.
Our method yields a new proof of Lovász’ theorem stating: for every digraph D and
r ∈V (D), there is an r-ﬂame subdigraph F of D such that λF (r, v) = λD(r, v) for
v ∈V (D) −r. We also give a strongly polynomial algorithm to ﬁnd such an F working
with a fractional generalization of Lovász’ theorem.
1. Introduction
Subgraphs preserving some connectivity properties while having as few edges as possible
have been a subject of interest since the beginning of graph theory. Suppose that D is
a digraph with r ∈V (D) and let us denote the local edge-connectivity1 from r to some
v ∈V (D) −r by λD(r, v). We are looking for a spanning subgraph H of D with the
smallest possible number of edges in which all the local edge-connectivities outwards from
the root r are the same as in D, i.e., λH(r, v) = λD(r, v) for all v ∈V (D) −r. In order to
have λD(r, v) many pairwise edge-disjoint paths from r to v in H, it is obviously necessary
that the in-degree ϱH(v) of v in H is at least λD(r, v). This leads to the estimation
|E(H)| ≥P
v∈V (D)−r λD(r, v). It was shown by Lovász that, maybe surprisingly, this trivial
lower bound is always sharp.
Theorem 1.1 (Lovász, Theorem 2 of [1]). For every digraph D and r ∈V (D), there is a
spanning subdigraph H of D such that for every v ∈V (D) −r
λD(r, v) = λH(r, v) = ϱH(v).
Calvillo-Vives rediscovered Theorem 1.1 independently in [2] and named the rooted
digraphs F with λF(r, v) = ϱF(v) for all v ∈V (F) −r ‘r-ﬂames’ .
We establish a direct connection between the extremal problem above and the theory of
greedoids. The latter were introduced by Korte and Lovász as a generalization of matroids
to capture greedy solvability in problems where the matroid concept turned out to be too
restrictive. The ﬁeld is actively investigated since the ’80s, for a survey we refer to [3].
We show that the subﬂames of a rooted digraph always form a greedoid whose bases
are exactly the subdigraphs described in Theorem 1.1.
2020 Mathematics Subject Classiﬁcation. Primary: 05C20, 05B35, 05C40. Secondary: 05C35, 05C85.
Key words and phrases. greedoid, edge-connectivity, rooted digraph, strongly polynomial algorithm.
The author would like to thank the generous support of the Alexander von Humboldt Foundation and
NKFIH OTKA-129211.
1The local edge-connectivity from r to v is the maximal number of pairwise edge-disjoint r →v paths.
1
arXiv:2008.09107v3  [math.CO]  31 Mar 2021

--- Page 2 ---

2
ATTILA JOÓ
Theorem 1.2. Let D = (V, E) be a digraph and r ∈V . Then
FD,r := {E(F) | F ⊆D is an r-ﬂame}
is a greedoid on E. Furthermore, for each ⊆-maximal element E(F ∗) of FD,r we have
λF ∗(r, v) = λD(r, v) for all v ∈V −r.
The proof of Theorem 1.1 by Lovász is algorithmic but only for simple digraphs
polynomial. We prove a fractional generalization of Lovász’ theorem considering digraphs
with non-negative edge-capacities and replacing ‘edge-connectivity’ by ‘ﬂow-connectivity’.
Our proof provides a simple strongly polynomial algorithm to ﬁnd an H with properties
given in Theorem 1.1.
It is worth to mention that one can formulate a structural inﬁnite generalization of
Theorem 1.1 in the same manner as Erdős conjectured such an extension of Menger’s
theorem (see [4]). As in the case of Menger’s theorem, the problem is getting much harder
in the inﬁnite setting. The “vertex-variant” of this generalization was proved for countably
inﬁnite digraphs in [5] which was then further developed in [6].
2. Notation
In this paper we deal only with ﬁnite combinatorial structures. An F ⊆2E is a greedoid
on E if ∅∈F and F has the Augmentation property, i.e., whenever F, F ′ ∈F with
|F| < |F ′|, there is some e ∈F ′ \ F such that F + e ∈F. A digraph D is an ordered pair
(V, E) where E is a set of directed edges with their endpoints in V where parallel edges
are allowed but loops are not. Let us ﬁx throughout this paper a vertex set V and a “root
vertex” r ∈V . For U ⊆V , inD(U) and outD(U) stand for the set of ingoing and outgoing
edges of U respectively, furthermore, let ϱD(U) := |inD(U)| and δD(U) := |outD(U)|. For
simplicity we always assume that inD(r) = ∅. We write shortly λD(v) for λD(r, v) where
v ∈V −r. Recall, this is the local edge-connectivity (i.e., the maximal number of pairwise
disjoint paths) from r to v . We deﬁne GD(v) to be the set of those I ⊆inD(v) for which
there exists a system P of edge-disjoint r →v paths where the set of the last edges of
the paths in P is I. It is known that that set GD(v) is the family of independent sets
of a matroid. Matroids representable this way were discovered by Perfect [7] and Pym
[8] independently (using an equivalent deﬁnition based on vertex-disjoint paths between
vertex sets) and are called gammoids. A digraph F is a ﬂame if GF(v) is a free matroid2
for every v ∈V −r, equivalently λF(v) = ϱF(v) for every v ̸= r.
3. The flame greedoid of a rooted digraph
The core of the proof of Theorem 1.2 is the following lemma.
Lemma 3.1. Let H and D be digraphs and assume that λH(u) < λD(u) for some u ∈V −r.
Then there is an e ∈E(D) \ E(H) with head, say v, such that e is a coloop3 of GH+e(v),
i.e.,
GH+e(v) ⊇{I + e : I ∈GH(v)}.
2A free matroid is a matroid where all sets are independent.
3A coloop is an edge of a matroid which can be added to any independent set without ruin independence.

--- Page 3 ---

GREEDOIDS FROM FLAMES
3
Proof. Let U := {U ⊆V −r : u ∈U and ϱH(U) = λH(u)}. By Menger’s theorem U ̸= ∅
and the submodularity of the map X 7→ϱH(X) ensures that U is closed under union and
intersection. Let U be the ⊆-largest element of U. Since λH(u) < λD(u), there exists
some edge e ∈inD(U) \ inH(U). Note that in H + e every X ⊆V −r with X ⊇U has
at least λH(u) + 1 = ϱH+e(U) many ingoing edges because of the maximality of U. By
applying Menger’s theorem in H + e with r and U, we ﬁnd a system P of edge-disjoint
r →U paths of size λH(u) + 1 (see Figure 1). The set of the last edges of the paths in
P is necessarily the whole inH+e(U). Let the head of e be v and let I ∈GH(v) witnessed
by the path-system Q. Clearly each Q ∈Q enters U at least once. For Q ∈Q, we deﬁne
fQ as the last meeting of Q with inH(U). Finally, we build a path-system R witnessing
I + e ∈GH+e(v) as follows. For Q ∈Q, we consider the unique PQ ∈P with last edge fQ
and concatenate it with the terminal segment of Q from fQ to obtain RQ. Moreover, let
Re be the unique path in P with last edge e. Then R := {RQ : Q ∈Q} ∪{Re} witnesses
I + e ∈GH+e(v) as desired.
v
u
r
e
U
P
Q
Figure 1. inH+e(U) consists of the thick edges, the terminal segments of
the paths in Q are dashed.
□
Proof of Theorem 1.2. Suppose that F0, F1 ⊆D are ﬂames with |F0| < |F1|. Then there
must be some u ∈V −r for which ϱF0(u) < ϱF1(u). Since F0 and F1 are ﬂames
λF0(u) = ϱF0(u) < ϱF1(u) = λF1(u).
By applying Lemma 3.1 with F0, F1 and u, we ﬁnd an e ∈E(F1) \ (F0) with head v where
e is a coloop of GF0+e(v). On the one hand, GF0(v) is a free matroid and the previous
sentence ensures that GF0+e(v) is free as well. On the other hand, for w ∈V \ {r, v} any
path-system witnessing that GF0(w) is a free matroid shows the same for GF0+e(w). By
combining these we may conclude that F0 + e is a ﬂame.
In order to prove the last sentence of Theorem 1.2, let F ∗be a maximal ﬂame in D and
suppose for a contradiction that λF ∗(u) < λD(u) for some u ∈V −r. Applying Lemma 3.1

--- Page 4 ---

4
ATTILA JOÓ
gives again some e ∈E \ E(F ∗) for which F ∗+ e is a ﬂame contradicting the maximality
of F ∗.
□
4. Fractional generalization and algorithmic aspects
In this section we deﬁne a fractional version of Lovász’s theorem and prove it by giving
a strongly polynomial algorithm that ﬁnds a desired optimal substructure. We consider
non-negative vectors indexed by the edge set E of a ﬁxed digraph D = (V, E). This time
we assume without loss of generality that D has no parallel edges because replacing a bunch
of parallel edges by a single edge whose capacity is deﬁned to be the sum of the capacities
of those will be a meaningful reduction step in all the results we discuss. For x, y ∈RE
+,
we write x ≤y if x(e) ≤y(e) for every e ∈E and for U ⊆V let ϱx(U) := P
e∈inD(U) x(e)
and δx(U) := P
e∈outD(U) x(e). An x ∈RE
+ is an r →v ﬂow if ϱx(u) = δx(u) holds for
all u ∈V \ {r, v} and ϱx(r) = δx(v) = 0. We introduce some concepts and basic facts
about ﬂows, one can ﬁnd more details and proofs for example in subsection 3.4 of [9].
The amount of the ﬂow x is deﬁned to be δx(r) which is equal to ϱx(W) −δx(W) for
every choice of W ⊆V −r containing v. Note that x can be written as the non-negative
combination of directed cycles and r →v paths (more precisely of their characteristic
vectors). Such a decomposition can be found in a greedy way. The sum of the coeﬃcients
of the paths in any such a decomposition is again δx(r). For v ∈V −r and c ∈RE
+, the
ﬂow-connectivity of c from r to v is
λc(v) := max{δx(r) : x is an r →v ﬂow with x ≤c.}
The Max ﬂow min cut theorem (see [10]) guarantees that λc(v) is well-deﬁned and equals
to
min{ϱc(W) : W ⊆V −r with v ∈W}.
For v ∈V −r and c ∈RE
+, we write Gc(v) for the set of those vectors in RinD(v)
+
that
can be obtained as a restriction of an r →v ﬂow x ≤c to inD(v) that we denote by
x ↾inD(v). It is not too hard to prove that Gc(v) is a polymatroid and it is natural to
call it a polygammoid. An f ∈RE
+ is a fractional ﬂame if f ↾inD(v) ∈Gf(v) (equivalently
λf(v) = ϱf(v)) for all v ∈V −r. For e ∈E, let χe ∈RE
+ be the vector where χe(e′) is 1 if
e = e′ and 0 otherwise. We call a vector integral if all of its coordinates are integers.
The fractional version of Lovász’ theorem can be formulated in the following way.
Theorem 4.1. Let D = (V, E) be a digraph and r ∈V . Then for every c ∈RE
+ there is
an f ≤c such that for every v ∈V −r
λc(v) = λf(v) = ϱf(v),
moreover, if c is integral then f can be chosen to be integral. Such an f can be found in
strongly polynomial time.
Proof. In the contrast of Theorem 1.1, the following fractional analogue of Lemma 3.1 is
not suﬃcient itself to provide the existence part of Theorem 4.1 but will be an important
tool later.

--- Page 5 ---

GREEDOIDS FROM FLAMES
5
Lemma 4.2. Let x, y ∈RE
+ such that λy(u) < λx(u) for some u ∈V −r. Then there is
an e ∈E with head, say v, and an ε > 0 such that x(e) −y(e) ≥ε and
Gy+εχe(v) = {s + δχe : s ∈Gy(v) ∧0 ≤δ ≤ε}.
Proof. The proof goes similarly as for Lemma 3.1. By applying the Max ﬂow min cut
theorem and the submodularity of the function X 7→ϱy(X), we take the maximal U ⊆V −r
with u ∈U and ϱy(U) = λy(u). We pick some e ∈inD(U) with x(e) > y(e) and let
ε := min{x(e) −y(e), ϱy(W) −ϱy(U) : U ⊊W ⊆V −r}.
Let p be an r →u ﬂow of maximal amount with respect to the capacity y + εχe in the
auxiliary digraph we obtain by contracting U to u while deleting the arising loops. By
deﬁning p on the edges with both ends in U to be 0, we ensure p ∈RE
+. The Max ﬂow
min cut theorem and the choice of ε guarantee that
p ↾inD(U) = (y + εχe) ↾inD(U).
We may assume that p is a non-negative combination of r →U paths. Let s ∈Gy(u)
witnessed by the r →u ﬂow q which is a non-negative combination of r →u paths. Take
the sum of the terminal segments of these weighted paths from the last common edge
with inD(U) together with the trivial path e with a given weight δ with 0 ≤δ ≤ε to
obtain a vector q′. Starting with p one can construct a p′ ≤p which is a non-negative
combination of r →U paths and for which p′ ↾inD(U) = q′ ↾inD(U). It is easy to see that
the coordinate-wise maximum of p′ and q′ witnessing s + δχe ∈Gy+εχe(v).
□
Now we turn to the description of the algorithm. Let V = {v0, . . . , vn} where v0 = r.
The algorithm starts with f0 := c. If fk ∈RE
+ is already constructed and k < n, then we
take an r →vk+1 ﬂow zk+1 ≤fk of amount λfk(vk+1), which we choose to be integral if fk
is integral, and deﬁne
fk+1(e) :=





zk+1(e)
if e ∈inD(vk+1)
fk(e)
otherwise.
Since the ﬂow problem can be solved in strongly polynomial time, the algorithm described
above is strongly polynomial with a suitable ﬂow-subroutine. We claim that fn satisﬁes
the demands of Theorem 4.1. Since we start with c and lower some values in each step,
fn ≤c holds. If c ∈ZE
+, then a straightforward induction shows that fn ∈ZE
+.
Lemma 4.3. If z ≤x is an r →v ﬂow of amount λx(v) and y(e) :=





z(e)
if e ∈inD(v)
x(e)
otherwise
then λy(u) = λx(u) for every u ∈V −r.
Proof. Suppose for a contradiction that there exists a u ∈V −r with λy(u) < λx(u). Note
that u ̸= v because λx(v) = λy(v) is witnessed by z. By Lemma 4.2, there is an e ∈E
and an ε such that x(e) −y(e) > ε > 0 (which implies that the head of e must be v) and
Gy+εχe(v) = {s + δχe : s ∈Gy(v) ∧0 ≤δ ≤ε}. Let s0 := z ↾inD(v).
λx(v) ≥λy+εχe(v) ≥||s0||1 + ε = λx(v) + ε
which is a contradiction.
□

--- Page 6 ---

6
ATTILA JOÓ
By applying Lemma 4.3 with x = fk, y = fk+1 and z = zk+1 we obtain the following.
Corollary 4.4. λfk(v) = λfk+1(v) for every k < n and v ∈V −r.
It follows by induction on k that λfk(v) = λc(v) for every v ∈V −r and k ≤n.
In particular λfn(v) = λc(v) for all v ∈V −r. Let 1 ≤k ≤n be arbitrary. Then
ϱfk(vk) = λfk(vk) follows directly from the algorithm (the common value is ϱzk(vk)). On
the one hand, the left side is equal to ϱfn(vk) since in moving from fk to fn the algorithm
no longer changes the values on the elements of inD(vk). On the other hand, we have
seen that λfk(vk) = λfn(vk) = λc(vk). By combines these we have ϱfn(v) = λfn(v) which
completes the proof of Theorem 4.1.
□
Finally, let us point out a special case of Lemma 4.3.
Corollary 4.5. Let D be a directed graph and let P be a maximal sized family of pairwise
edge-disjoint r →v paths in D. Then the deletion of those ingoing edges of v that are
unused by the path-family P does not reduce any local edge-connectivities of the form
λD(r, u) with u ∈V (D) −r.
5. Outlook
By Theorem 4.1, ﬁnding a spanning subdigraph of a given digraph D that preserves all
the local edge-connectivities from a prescribed root vertex r and has the fewest possible
edges with respect to this property can be done in polynomial time. It is natural to ask
the complexity of the weighted version:
Question 5.1. What is the complexity of the following combinatorial optimization problem?
Input: digraph D, r ∈V (D) and cost function c : E(D) →R+
Output: spanning subdigraph F of D with λF(r, v) = λD(r, v) for every v ∈V (D) −r for
which P
e∈E(F) c(e) is minimal with respect to this property.
The special case where λD(r, v) is the same for every v ∈V (D) −r can be solved in
polynomial time by using weighted matroid intersection (see [11]).
There are more general ﬂow models involving polymatroidal bounding functions (see for
example [13] and [14]). The Max ﬂow min cut theorem is preserved under these models.
Question 5.2. Is it possible to generalize Theorem 4.1 by using the polymatroidal ﬂow
model introduced by Hassin in [12] (and rediscovered later by Lawler and Martel in [13]
independently)?
The relation between matroids and polymatroids motivates the following concept of
polygreedoids: a polygreedoid is a compact P ⊆RE
+ such that
PG1 0 ∈P,
PG2 whenever x, y ∈P with ||x||1 < ||y||1, there is some e ∈E with y(e) > x(e) such
that x + εχe ∈P for all small enough ε > 0.

--- Page 7 ---

GREEDOIDS FROM FLAMES
7
It follows directly from Lemma 4.2 that fractional ﬂames under a given bounding vector
form a polygreedoid. Greedoids have a property called accesibility which can be considered
as a weakening of the downward closedness of matroids. It tells that every F ∈F can be
enumerated in such a way that each initial segment belongs to F, i.e., F = {e1, . . . , en}
such that {e1, . . . , ek} ∈F for every k ≤n. Accessibility tends to be a part of the
axiomatization of greedoids via the restriction the Augmentation axiom for pairs with
|F ′| = |F|+1. It is not too hard to prove that polygreedoids satisfy the following analogous
property: for every x ∈P there is a continues strictly increasing4 function g : [0, 1] →P
with g(0) = 0 and g(1) = x. Finally, let us end the paper with the following general
question.
Question 5.3. How much of the theory of greedoids is preserved for polygreedoids?
References
[1] L. Lovász, Connectivity in digraphs, J. Combinatorial Theory Ser. B 15 (1973), 174–177, DOI
10.1016/0095-8956(73)90018-x. MR325439
[2] G. Calvillo-Vives, Optimum branching systems, Ph.D. Thesis, University of Waterloo, 1978.
[3] B. Korte, L. Lovász, and R. Schrader, Greedoids, Algorithms and Combinatorics, vol. 4, Springer-
Verlag, Berlin, 1991. MR1183735
[4] R. Aharoni and E. Berger, Menger’s theorem for inﬁnite graphs, Invent. Math. 176 (2009), no. 1,
1–62, DOI 10.1007/s00222-008-0157-3. MR2485879
[5] A. Joó, Vertex-ﬂames in countable rooted digraphs preserving an Erdős-Menger separation for each
vertex, Combinatorica 39 (2019), 1317–1333, DOI 10.1007/s00493-019-3880-z.
[6] Joshua Erde and J. Pascal Gollin and Attila Joó, Enlarging vertex-ﬂames in countable digraphs, arXiv
preprint arXiv:2003.06178 (2020). https://arxiv.org/abs/2003.06178v1.
[7] H. Perfect, Independence spaces and combinatorial problems, Proceedings of the London Mathematical
Society 3 (1969), no. 1, 17–30.
[8] J. Pym, A proof of the linkage theorem, Journal of Mathematical Analysis and Applications 27 (1969),
no. 3, 636–638.
[9] A. Frank, Connections in combinatorial optimization, Vol. 38, OUP Oxford, 2011.
[10] L. R. Ford Jr. and D. R. Fulkerson, Flows in networks, Princeton University Press, Princeton, N.J.,
1962. MR0159700
[11] J. Edmonds, Submodular functions, matroids, and certain polyhedra, Combinatorial Structures and
their Applications (Proc. Calgary Internat. Conf., Calgary, Alta., 1969), Gordon and Breach, New
York, 1970, pp. 69–87. MR0270945
[12] R. Hassin, Minimum cost ﬂow with set-constraints, Networks 12 (1982), no. 1, 1–21.
[13] E. L. Lawler and C. U. Martel, Polymatroidal ﬂows with lower bounds, Discrete Appl. Math. 15
(1986), no. 2-3, 291–313, DOI 10.1016/0166-218X(86)90050-8. Applications of combinatorial methods
in mathematical programming (Gainesville, Fla., 1985). MR865009
[14] M. Kochol, Quasi polymatroidal ﬂow networks, Acta Math. Univ. Comenian. (N.S.) 64 (1995), no. 1,
83–97. MR1360989
Attila Joó, University of Hamburg, Department of Mathematics, Bundesstraße 55
(Geomatikum), 20146 Hamburg, Germany
Email address: attila.joo@uni-hamburg.de
4Strictly increasing is meant with respect to the coordinate-wise partial ordering of RE
+.

--- Page 8 ---

8
ATTILA JOÓ
Attila Joó, Alfréd Rényi Institute of Mathematics, Set theory and general topology
research division, 13-15 Reáltanoda St., Budapest, Hungary
Email address: jooattila@renyi.hu

```
