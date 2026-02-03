---
title: "Learning Social Welfare Functions - PDF Extract"
source_pdf: "2024-Pardeshi-Learning Social Welfare Functions.pdf"
pages: 10
extracted_at: "2026-01-24T17:05:40.097030"
---

# PDF Extract: Learning Social Welfare Functions

**Source PDF:** 2024-Pardeshi-Learning Social Welfare Functions.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

A complete characterization of graphs for which
mG(−1) = n −d −1
Songnian Xu, Wenhao Zhen, Dein Wong∗
School of Mathematics, China University of Mining and Tecnology, Xuzhou, China.
Abstract
Let G be a simple connected graph of order n with diameter d. Let mG(−1) denote the multiplicity
of the eigenvalue −1 of the adjacency matrix of G, and let P = Pd+1 be the diameter path of G. If −1 is
not an eigenvalue of P, then by the interlacing theorem, we have mG(−1) ≤n−d−1. In this article,
we characterize the extremal graphs where equality holds. Moreover, for the completeness of the
results, we also characterize the graphs G that achieve mG(−1) = n −d −1 when −1 is an eigenvalue
of P. Thus, we provide a complete characterization of the graphs G for which mG(−1) = n −d −1.
1
Introduction
In this paper, we consider only simple, connected and finite graphs. A simple undireted graph G is
denoted by G = (V (G), E(G)), where V (G) is the vertex set and E(G) is the edge set. A graph H is
called a subgraph of a graph G if V (H) ⊆V (G) and E(H) ⊆E(G). Further, if any two vertices of
V (H) are adjacent in H if and only if they are adjacent in G, we say that H is an induced subgraph of
G and denote this relation as H ≤G. The order of G is the number of vertices of G, denoted by |G|.
For V1 ⊆V (G) and H ≤G, NH(V1) = ∪v∈V1{u ∈V (H)|uv ∈E(G)}. Let K ⊆V (G), traditionally, the
subgraph of G induced by K, written as G[K]. And we sometimes write G −K or G −G[K] to denote
G[V (G)\V (K)]. A vertex v of G is said to be pendant if d(v) = 1, where d(v) denotes the number of
adjacent vertices of v in V (G). For x, y ∈V (G), distance d(x, y) represents the length of the shortest
path between x and y, and d(x, H) = min{d(x, y)|y ∈V (H)} for H ≤G. We denote by Km,n the
complete bipartite graph. Let A(G) denote the adjacency matrix of graph G, which is a square matrix
and aij = 1 if and only if vi ∼vj, otherwise aij = 0.
Let mG(µ) denote the multiplicity of the eigenvalue µ in the adjacency matrix A(G). In 2013, Wong
[10] characterize graphs with maximum diameter among all connected graph with rank n. In 2022, Wang
∗Corresponding author. E-mail address: wongdein@163.com.
Keywords: eigenvalue multiplicity; diameter; extremal graphs
1
arXiv:2410.15000v1  [math.SP]  19 Oct 2024

--- Page 2 ---

[11] characterized the graphs for which mG(0) = n−d using the method of star complements. In the same
year, Chang and Li [2] characterized the graphs for which mG(0) = n −g −1. In 2023, Du and Fonseca
[4] extend the definition of minimal graphs on adjacency matrices to real symmetric matrices. They
characterize all the trees for which there is a real symmetric matrix with nullity n −d and n −d −1. In
2024, Zhang and Wong [6] provided a complete characterization of the graphs for which mG(−1) = n−d.
Therefor, we investigate the situation mG(−1) = n −d −1.
Let G be a graph and u, v ∈V (G). We introduce (see [5]) a binary relation ρ in V (G) in the following
way: uρv if and only if NG[u] = NG[v]. The relation ρ is symmetric and transitive. By this relation the
vertex set V (G) is divided to k disjoint subsets C1, C2, . . ., Ck, (1 ≤k ≤n, n = |V (G)|), such that
every graph induced by the set Ci (i = 1, . . . , k) is a complete graph. The graph Gc, obtained from G by
identification of all vertices from the same subset Ci (i = 1, . . . , k) is called the “C-canonical graph” of
the graph G. If V (G) does not have any pair of vertices which lie in relation ρ, then Gc = G and we say
that G is a C-canonical graph. For instance, all connected bipartite graphs distinct of P2 are C-canonical
graphs..
2
Preliminaries
Lemma 2.1. [1] Let v be a vertex of G, then mG(µ) −1 ≤mG(µ) ≤mG(µ) + 1
The eigenvalues of Pn are {2cos iπ
n+1|i = 1, 2, ..., n}, we have the following lemma.
Lemma 2.2. mPn+1(−1) ≤1, further, mPn+1(−1) = 1 if and only if n ≡1 (mod 3)
Lemma 2.3. ([7], Lemma 2.3) Let X be a star set for µ in G and let U be a proper subset of X. Then
X −U is a star set for µ in G −U.
Lemma 2.4. ([3], Proposition 5.1.4) Let X be a star set for µ in G, and let X = V (G)\X. If µ = 0,
then X is a dominating set for G.
Lemma 2.5. ([6, 3.1]) Let H be an induced subgraph of a connected graph G for which rank(A(H)+I) ≥
rank(A(G) + I) −1, and v ∈V (G)\V (H). If v ∼h and NH(v) = NH[h] for a vertex h ∈V (H), then
NG[v] = NG[h].
Lemma 2.6. ([6, 3.2]) Let H be an induced subgraph of a connected graph G for which rank(A(H)+I) ≥
rank(A(G) + I) −1, and u, v ∈V (G)\V (H). If u ∼v and NH(v) = NH(h), then NG[v] = NG[h].
Lemma 2.7. ([5, Theorem 5]) Let G be a graph. If two vertices u, v satisfy uρv, then mG(−1) =
mG−u(−1) + 1 = mG−v(−1) + 1.
Lemma 2.8. ([6, 3.4]) Let Gc be the C-canonical graph of a graph G. If G is not a complete graph,
then d(Gc) ≥1 and d(Gc) = d(G).
2

--- Page 3 ---

Lemma 2.9. Let Gc be the C-canonical graph of a graph G.
If G is not a complete graph, then
mG(−1) = n(G) −d(G) −1 if and only if mGc(−1) = n(Gc) −d(Gc) −1.
Proof. If G is not a complete graph, by Lemma 2.8, d(Gc) = d(G). Meanwhile, by Lemma 2.7, mG(−1) =
mGc(−1) + n(G) −n(Gc). So, mG(−1) = n(G) −d(G) −1 if and only if mGc(−1) + (n(G) −n(Gc) =
n(G) −d(G) −1 = n(G) −d(Gc) −1).
Then we have mG(−1) = n(G) −d(G) −1 if and only if
mGc(−1) = n(Gc) −d(Gc) −1.
By Lemmas 2.8 and 2.9, we know that for the eigenvalue −1, G and Gc possess identical properties;
therefore, in this article, we will only consider the case where G = Gc.
Lemma 2.10. [9, 2.2] Let G be a graph obtained from a given graph H and P3, disjoint with H, by
identifying one pendant vertex of P3 with a vertex w of H. Then mG(−1) = mG−w(−1)
Lemma 2.11. If mG(−1) = n −d −1 and Pd+1 is the diameter path of G with Pd+1 ≤H ≤G, then it
follows that rank(A(H) + I) ≥rank(A(G) + I) −1.
Proof. If -1 is not an eigenvalue of Pd+1, then by the interlacing theorem, we have rank(H + I) =
rank(Pd+1). If -1 is an eigenvalue of Pd+1, then rank(H + I) = rank(Pd+1 + I) or rank(Pd+1 + I) + 1.
This completes the proof.
For x ∈Rn, we denote by xu the component of x corresponding to u ∈V (G). With respect to a
subset U of V (G), we define
Z(U) = {x ∈Rn : xu = 0, ∀u ∈U}.
Lemma 2.12. [9, Lemma 2.1] Let G be a graph of order n and U be a subset of G. If V (G, µ))∩Z(U) = 0,
then mG(µ) ≤|U|.
Lemma 2.13. [8] Let G be a graph, V (G) = {1, 2, ..., n}, X ⊆V (G). Let F be the matrix which
represents the orthogonal projection of Rn onto the eigenspace EA(G)(µ) with respect to the standard
orthonormal basis {e1, e2, . . . , en} of Rn. Then
(i) X is a star set for µ in G if and only if the vectors Fei, i ∈X, form a basis for EA(G)(µ).
(ii)The matrix F is a polynomial in A and µFev = Σu∼vFeu.
3

--- Page 4 ---

3
mP(−1) = 0 and mG(−1) = n −d −1
After performing computations using a computer, it can be concluded that mHi(−1) = 0 for 1 ≤i ≤6.
4

--- Page 5 ---

Theorem 3.1. Let G be a connected graph and P = Pd+1 = v1 ∼v2 ∼· · · ∼vd+1 be the diameter path
of G. Given that -1 is not an eigenvalue of P, we have mG(−1) ≤n −d −1. The equality holds if and
only if P ≤G ≤Gi for 1 ≤i ≤3.
Proof. Since -1 is not an eigenvalue of P, we can deduce from Lemma 2.1 that mG(−1) ≤n −d −1,
with equality holding if and only if X = V (G −P) forms a star set.
From Lemma 2.4, we know
that P is a dominating set for G, which implies NG(P) = V (G −P).
Let NG(P) = ∪i≥1Ni and
Ni = {x : |NP (x)| = i}.
Claim 1: NG(P) = N1 ∪N2
If i > 3 and x ∈Ni, where x is adjacent to vj1, vj2, vj3, vj4 with j1 < j2 < j3 < j4, then the path
v1v2 . . . vj1xvj4 . . . vd+1 forms a path shorter than P, which contradicts the fact that P is a diameter
path. If i = 3 and x ∈N3, with x being adjacent to vj1, vj2, vj3, it follows that j3 = j1 + 2 = j2 + 1.
If this condition is not satisfied, then v1v2 . . . vj1xvj3 . . . vd+1 would again represent a path shorter than
P, leading to a contradiction. When j3 = j1 + 2 = j2 + 1, we find that NP (x) = NP [vj2]. According to
Lemma 2.5, this implies NG[x] = NG[vj2], which contradicts the assumption that G = Gc. Therefore, we
conclude that NG(P) = N1 ∪N2.
Claim 2: If x, y ∈V (G −P), then NP (x) ̸= NP (y).
If x ∼y, then NP [x] = NP [y]. According to Lemmas 2.6 and 2.11, it follows that NG[x] = NG[y],
which contradicts the condition G = Gc.
If x ≁y, consider P + x + y.
By Lemma 2.13, we have
Fex = Fey, which contradicts the fact that Fex and Fey are linearly independent.
Therefore, we
conclude that NP (x) ̸= NP (y).
Since mP (−1) = 0, we can infer from Lemma 2.2 that d ≡0 or 2 (mod 3) . Therefore, we will discuss
two cases in the following analysis.
Case 1: d ≡2 (mod 3)
Claim 1.1: N1 = ∅.
First, by the interlacing theorem, we know that mP +u(−1) = 1.
If N1 ̸= ∅, let x ∈N1 such that x ∼vm. If m ≡0 or 1 mod 3, then by Lemma 2.10, we have
mP +x(−1) = 0, leading to a contradiction. If m ≡2 mod 3, it follows that mP +x(−1) = mK1,3 = 0,
which also leads to a contradiction. Therefore, we conclude that N1 = ∅.
Claim 1.2: If u ∈N2 and u is adjacent to vi and vj with i < j, then it follows that j = i + 1.
If j −i > 2, then the path v1v2 . . . viuvj . . . vd+1 is shorter than P, leading to a contradiction.
When j = i + 2 and i ≡0 (mod 3), then mP +u(−1) = 0, resulting in another contradiction.
When j = i + 2 and i ≡1 (mod 3), then mP +u(−1) = mH4(−1) = 0, resulting in yet another
contradiction.
The case for j = i + 2 and i ≡2 (mod 3) can be similarly analyzed, leading to a contradiction. In
summary, we conclude that j = i + 1.
Claim 1.3: If u ∈N2 and u is adjacent to vm and vm+1, then m ≡0 or 1 (mod 3).
5

--- Page 6 ---

When m ≡0 (mod 3), then by using Lemma 2.10, we obtain mP +u(−1) = 0, which leads to a
contradiction.
When m ≡1 (mod 3), then mP +u(−1) = 1, satisfying the condition.
When m ≡2 (mod 3), then mP +u(−1) = 1, satisfying the condition. Thus, the proof is established.
Claim 1.4: If u, v ∈N2 with u ∼vm, vm+1 and v ∼vh, vh+1, we may assume m < h. Then, u ̸∼v
and P ≤G ≤G1.
First, let us assume that u ∼v. When m ≡1 (mod 3), since P is a diameter path, we only need
to consider the case where h = m + 1. In this case, mP +u+v(−1) = 1, which leads to a contradiction.
Similarly, when m ≡2 (mod 3), we only need to consider the case where h = m + 2. In this situation,
mP +u+v(−1) = mH5(−1) = 0, which also results in a contradiction. Thus, it follows that u ̸∼v.
If m ≡1 (mod 3) and h ≡2 (mod 3), then mP +u+v(−1) = 2, which satisfies the conditions. If
m ≡2 (mod 3) and h ≡1 (mod 3), then mP +u+v(−1) = mH2(−1) = 0, leading to a contradiction.
If both m ≡1 (mod 3) and h ≡1 (mod 3) (or if m ≡2 (mod 3) and h ≡2 (mod 3)), we can apply
Lemmas 2.7 and 2.10, which yield mP +u+v(−1) = 2, satisfying the conditions. Therefore, based on the
above discussion, G1 is a maximal graph that satisfies the given conditions. Furthermore, by reapplying
Lemmas 2.7 and 2.10, we obtain mG1(−1) = t = n −d −1, which concludes the proof.
We will now begin to consider the case where d ≡0 (mod 3), while omitting certain proofs that are
similar to those in Case 1.
Caes2: d ≡0 (mod 3)
Claim 2.1: If x ∈N1 and x sin vm, then m ≡1 (mod 3).
If m ≡0 or 2 (mod 3), then mP +u(−1) = 0, leading to a contradiction.
If m ≡1 (mod 3), then mP +u(−1) = 1, satisfying the condition.
Claim 2.2: If x, y ∈N1, then x ∼y. Therefore, |N1| ≤2.
Let x ∼vm and y ∼vh. According to Claim 2.1, we know that m = 3t + 1 and h = 3l + 1. If x ̸∼y,
then mP +x+y(−1) = mP3(−1) = 0, which leads to a contradiction. If x ∼y, we may assume m < h, thus
h = m + 3. Otherwise, the sequence v1v2 . . . vmxyvh . . . vd+1 would constitute a path shorter than P. In
this case, we have mP +x+y(−1) = mC6(−1) = 2, which satisfies the conditions.
Claim 2.3: If u ∈N2 and u is adjacent to vi and vj with i < j, then it follows that j = i + 1.
Claim 2.4: If u ∈N2 and u is adjacent to vm and vm+1, m ≡0 or 1 (mod 3).
When m ≡0 (mod 3), then by using Lemma 2.10, we obtain mP +u(−1) = mP2(−1) = 1, satisfying
the condition.
When m ≡1 (mod 3), then mP +u(−1) = mP2(−1) = 1, satisfying the condition.
When m ≡2 (mod 3), then mP +u(−1) = mH1 = 0, leading to a contradiction;
Claim 2.5: Let u, v ∈N2 such that u ∼v3a, v3a+1, and v ∼v3b+1, v3b+2. If b ≥a, then it follows
that u ∼v and b = a. Conversely, if b < a, then u ≁v.
If b ≥a and u ̸∼v, then according to Lemma 2.10, we have mP +u+v(−1) = 0 < 2, which leads to a
contradiction. Furthermore, since P is a diameter path, we can conclude that a = b.
6

--- Page 7 ---

If b < a and u ∼v, considering that P is a diameter path, we have b = a −1. Thus, mP +u+v(−1) =
mH6(−1) = 0 < 2, which leads to a contradiction. Therefore, it follows that u ≁v.
Claim 2.6: If x ∈N1, u ∈N2, x ∼vi, u ∼vj, vj+1, and u ̸∼x, then if j > i, it follows that
j ≡0 (mod 3). Conversely, by symmetry, if j < i, then j ≡1 (mod 3).
From Claim 2.4, we know that j ≡0 or 1 (mod 3). If j > i and j ≡1 (mod 3), then mP +x+u(−1) =
mP3(−1) = 0, which leads to a contradiction. On the other hand, if j > i and j ≡0 (mod 3), then
mP +x+u(−1) = mC3(−1) = 2, satisfying the conditions. By symmetry, the proof is completed.
Claim 2.7: Let x ∈N1 and u ∈N2, with x ∼vi, u ∼vj, vj+1. If x ∼u, then it follows that j = i or
j = i −1.
By symmetry, it is sufficient to prove that when j ≥i, then j = i.
If j ≡1 (mod 3), then
i = j; otherwise, v1v2 . . . vixuvj+1 . . . vd+1 would form a path shorter than P ; when i = j, we have
mP +u+v(−1) = mC3(−1) = 2, which satisfies the conditions. If j ≡0 (mod 3), then j = i + 2; otherwise,
a path shorter than P would emerge. When j = i + 2, we find mP +u+v(−1) = mH3(−1) = 0, leading to
a contradiction. Therefore, the conclusion is established.
Claim 2.8: Let N1 = {x, y}. If there are two vertices u, v ∈N2 that are adjacent to vertices in N1,
then P + u + x + y ∼= H7.
According to claims 2.6 and 2.7, when there are two vertices u, v ∈N2 that are adjacent to vertices
in N1, it follows that P + u + v + x + y ∼= H7. Based on Lemmas 2.7 and 2.10, we have mH7(−1) =
2 + mC6(−1) = 4, which satisfies the conditions and thereby concludes the proof.
Claim 2.9: When d ≡0 (mod 3), P ≤G ≤G2 or G3.
Based on the above discussion, it can be concluded that G2 or G3 are maximal graphs that satisfy the
given conditions. Furthermore, according to Lemmas 2.7 and 2.10, we obtain mG2(−1) = mG3(−1) =
i + k + 4 = n −d −1, which satisfies the conditions. The proof is thereby established by the alternating
theorem.
7

--- Page 8 ---

4
mP(−1) = 1 and mG(−1) = n −d −1
Theorem 4.1. Let G be a connected graph and P = Pd+1 = v1 ∼v2 ∼· · · ∼vd+1 be the diameter path
of G. If mP (−1) = 1 and mG(−1) = n −d −1, then P < G ≤G4 and N1 ̸= ∅.
Proof. Initially, since mP (−1) = 1, we conclude from Lemma 2.2 that d = 3k + 1. Furthermore, there
cannot exist a point z that is at a distance of 3 from P. To illustrate this, suppose ( z ) is a point at
a distance of 3 from P, y is a vertex at a distance of 2 from P, and x is adjacent to P. According to
Lemma 2.10, we then have mP +x+y+z(−1) = mP (−1) = 1 < 2, which leads to a contradiction.
Claim 1: If x ∈N1 and x ∼vi, then mP +x(−1) = 1 and i ≡0 mod 3.
According to Lemma 2.11, we have mP +x(−1) ≤1 + dim(V (G, −1) ∩Z(v1). Since dim(V (G, −1) ∩
Z(v1)) = 0, it follows that mP +x(−1) ≤1. If mP +u(−1) = 0, then it would imply that mG(−1) ≤n−d−2,
which leads to a contradiction. Therefore, we conclude that mP +u(−1) = 1. This also indicates that
V (G −P −x) is a star set.
If i ≡0 (mod 3), then by utilizing Lemma 2.10, we obtain mP +x(−1) = mP2(−1) = 1, which satisfies
the condition. If m ≡1 or 2 (mod 3), then mP +u(−1) = 0, leading to a contradiction.
Claim 2: If x, y ∈N1 and x ∼v3a, y ∼v3b, then a ̸= b and u ∼v. Hence, it follows that |N1| ≤2.
First, we demonstrate that a ̸= b.
If a = b and x ∼y, then NP (x) = NP (y).
By Lemma 2.6,
this implies NG[x] = NG[y], which leads to a contradiction. Alternatively, if a = b and x ̸∼y, then
mP +x+y(−1) = 1 < 2, resulting in another contradiction.
If x ̸∼y, then by Claim 1 and Lemma 2.10, we have mP +x+y = mP2(−1) = 1 < 2, which leads to
a contradiction. Hence, it follows that x ∼y. Furthermore, considering that P is a diameter path, we
conclude that |N1| ≤2.
Claim 3: Let u ∈N2 and u ∼vm, vm+1. Then m ≡1 (mod 3) and mP +u(−1) = 2.
8

--- Page 9 ---

First, we know that 1 ≤mP +u(−1) ≤2. If m ≡0 (mod 3) or m ≡2 (mod 3) , then mP +u(−1) = 0,
which leads to a contradiction. If m ≡1 (mod 3), then mP +u(−1) = mC3(−1) = 2, thus proving the
claim. Similar to Claim 2, for u, v ∈N2, we have NP (u) ̸= NP (v).
Claim 4: Let x ∈N1 and u, v ∈N2. Then x ̸∼N2 and u ̸∼v.
Assume u ∼v. According to Claim 3, we may assume u ∼v3a+1, v3a+2, and v ∼v3b+1, v3b+2.
Considering that P is a diameter path, we have |b −a| = 1. Thus, mP +u+v(−1) = mH8(−1) = 1 < 2,
which leads to a contradiction. If x ∼N2, we may assume x ∼v3c and u. Given that P is a diameter
path, we have |b −c| = 1. Therefore, mP +x+u(−1) = 1 < 2, which results in another contradiction.
Next, we begin to consider the vertices that are at a distance of 2 from P.
Claim 5: If d(z, P) = 2, then z ∼N1 and z ̸∼N2.
If x ∈N1 and z ∼x, then mP +x+z(−1) = 2, satisfying the condition. On the other hand, if u ∈N2
and z ∼u, then mP +u+z(−1) = 1 < 2, which leads to a contradiction.
Claim 6: Let N 2 = {z | d(z, P) = 2}. Then it follows that |N 2| ≤1.
If z, w ∈N, by Claim 5, we know there exist x, y ∈N1 such that x ∼z and y ∼w. If x = y and
z ∼w, let H = P + x; then NH(z) = NH(w). By Lemma 2.5, we have NG[z] = NG[w], which leads
to a contradiction. If x = y and z ̸∼w, then mP +x+z+w(−1) = 1 < 3, which is also a contradiction.
Thus, we conclude that x ̸= y. At this point, based on Claim 1 and Claim 2, we can assume without
loss of generality that x ∼v3a and y ∼v3a+3. If z ̸∼y, then mP +x+y+z(−1) = 1 < 2, which is again
a contradiction.
If z ∼y, then mP x+y+z(−1) = 1 + mC3(−1) = 3, satisfying the condition, which
implies z ∼x, y.
Similarly, we can conclude that w ∼x, y.
If z ∼w, let H = P + x + y); then
NH(z) = NH(w). By Lemma 2.6, we know NG[z] = NG[w], leading to a contradiction. If z ̸∼w, then
mP +x+y+z+w(−1) = 2 < 4, which is also a contradiction. In summary, we have |N 2| ≤1. If z ∈N 2 and
x, y ∈N1, then it follows that z ∼x, y.
Claim 7: P < G ≤G4 and N1 ̸= ∅.
First, based on the discussion above, we know that G4 is a maximal graph that satisfies the conditions.
Furthermore, by applying Lemmas 2.7 and 2.10, we can conclude that mG4(−1) = m + 3 = n −d −1,
which satisfies the required conditions. If N1 = ∅, then V (G) = V (P) ∪N2, leading to mG(−1) = n −d,
which presents a contradiction. Therefore, we conclude that N1 ̸= ∅, and the theorem is proven.
References
[1] A. Brouwer, W. Haemers, Spectra of Graphs, Springer, New York, 2011.
[2] S. Chang, J. Li, Graphs G with nullity n(G) −g(G) −1, Linear Algebra Appl. 642 (202) 251-263.
[3] D. Cvetkovi´c, P. Rowlinson, S. Simi´c, An Introduction to the Theory of Graph Spectra, Cambridge
University Press, Cambridge, 2010.
9

--- Page 10 ---

[4] Z. Du, C. Fonseca, The characterization of the minimal weighted acyclic graphs, Linear Algebra
Appl. 672 (2023) 75–92.
[5] M. Petrovi´c, On graphs with exactly one eigenvalue less than 1, J. Comb. Theory, Ser. B 52 (1991)
102–112.
[6] Y. Zhang, W. Zhen, D. Wang, Minimal graphs with eigenvalue multiplicity of n −d, Linear Algebra
Appl. 699 (2024) 47–58.
[7] P. Rowlinson, An extension of the star complement technique for regular graphs, Linear Algebra
Appl. 557 (2018) 496–507.
[8] P. Rowlinson, On multiple eigenvalues of trees, Linear Algebra Appl. 432 (2010) 3007–3011.
[9] X. Wang, D. Wong, L. Wei, F. Tian, On the multiplicity of -1 as an eigenvalue of a tree with given
number of pendant vertices, Linear and Multilinear Algebra, 70:17, 3345-3353.
[10] D. Wong, M. Zhu, W. Lv, A characterization of long graphs of arbitrary rank, Linear Algebra Appl.
438 (2013) 1347–1355.
[11] Z. Wang, The multiplicities of eigenvalues of a graph, Appl. Math. Comput. 421 (2022) 126957.
10

```
