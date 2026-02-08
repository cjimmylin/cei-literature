---
title: "Black Box Deployed - PDF Extract"
source_pdf: "2025-Brophy-Black Box Deployed.pdf"
pages: 23
extracted_at: "2026-01-24T16:38:23.906832"
---

# PDF Extract: Black Box Deployed

**Source PDF:** 2025-Brophy-Black Box Deployed.pdf
**Total Pages:** 23

---

## Content

```
--- Page 1 ---

Higher-Order Pattern Unification Modulo
Similarity Relations
Besik Dundua1,2 and Temur Kutsia3
1 VIAM, Tbilisi State University, Georgia
2 Kutaisi International University, Georgia
bdundua@gmail.com
3 RISC, Johannes Kepler University, Linz, Austria
kutsia@risc.jku.at
Abstract. The combination of higher-order theories and fuzzy logic can
be useful in decision-making tasks that involve reasoning across abstract
functions and predicates, where exact matches are often rare or unnec-
essary. Developing efficient reasoning and computational techniques for
such a combined formalism presents a significant challenge. In this pa-
per, we adopt a more straightforward approach aiming at integrating two
well-established and computationally well-behaved components: higher-
order patterns on one side and fuzzy equivalences expressed through
similarity relations based on minimum T-norm on the other. We propose
a unification algorithm for higher-order patterns modulo these similarity
relations and prove its termination, soundness, and completeness. This
unification problem, like its crisp counterpart, is unitary. The algorithm
computes a most general unifier with the highest degree of approximation
when the given terms are unifiable.
Keywords: Unification · Higher-order patterns · Fuzzy similarity rela-
tions
1
Introduction
Approximate reasoning involves making decisions or performing inferences based
on vague or imprecise information, which is often modeled using fuzzy logic.
Fuzzy similarity (and proximity) relations are key tools in this type of reasoning,
allowing for working with uncertain or imprecise data. Fuzzy similarity refers
to the degree to which two elements or objects are alike, using a value in the
range of 0 to 1, where 0 represents no similarity and 1 represents complete
similarity. These relations can be used to determine how similar a new situation
is to past experiences or data. This is particularly useful in scenarios where
precise comparisons are impossible or where “similar enough” is acceptable. (See,
e.g., [8, 13, 18, 20, 23, 28, 30, 31] in the context of using similarity relations in
automated approximate reasoning.)
Fuzzy similarity and proximity relations have been incorporated into knowl-
edge representation and inference processes in the area of logic programming [7,
arXiv:2507.13208v1  [cs.AI]  17 Jul 2025

--- Page 2 ---

2
B. Dundua and T. Kutsia
9,11,12,15,17,31], making it possible to reason or compute with vague concepts
having imprecise boundaries. It helps to deal with the ambiguity inherent in
real-world data, where exact matches are rare, and allows systems to make rea-
sonable inferences even with imprecise or incomplete information. In order for
this approach to work, one needs a fundamental computational mechanism such
as unification to make an “approximate inference step”. Motivated by this ap-
plication, first-order unification with fuzzy relations has been investigated both
from theoretical and practical points of view, see, e.g., [1,5,8,10,14,16,18,19,22,
28,29,31–33]. In [6], this technique was studied in a more general setting where
the quantitative approximate information is specified using quantales, having
the fuzzy quantale as a special case.
The cited works focus on fuzzy reasoning and computation within a first-
order framework. However, decision-making often requires higher-order reason-
ing across abstract layers of functions and predicates, where exact matches are
rare or even unnecessary. For instance, when two functions are not identical
but exhibit a high degree of similarity in behavior or output, fuzzy similarity
relations would enable the system to recognize this resemblance and apply ap-
proximate reasoning for inference or prediction. This can be especially useful in
fields such as natural language processing, knowledge representation, and com-
plex decision-making systems, where human-like reasoning and the handling of
uncertainty are essential. This idea is a primary motivation for our work.
It is important to note that the existing higher-order fuzzy logics (e.g.,
[21,27]) are highly expressive formalisms, but because of this expressive power,
developing efficient reasoning and computational techniques for them is a sig-
nificant challenge. We adopt a more straightforward approach, concentrating
on the integration of established and computationally well-behaved fragments:
higher-order patterns on one hand, and fuzzy equivalences expressed through
minimum-T-norm-based similarity relations on the other. The first step in sup-
porting reasoning for this integration is the development of fundamental com-
putational techniques, such as unification, which is the subject of this paper.
Our contribution. We define the notion of similarity for simply-typed lambda
terms and study the unification problem for higher-order patterns à la Miller [24].
In this framework, the equality relation modulo αβη-equivalence is replaced by
fuzzy similarity modulo αβη with the minimum T-norm (Gödel T-norm). We
develop a rule-based unification algorithm for such problems and prove its ter-
mination, soundness, and completeness. The unification problem, like its crisp
counterpart, is unitary, that is, any unifiable problem has a single (modulo αβη-
equivalence) most general unifier (mgu) with respect to fuzzy similarity using
minimum T-norm. The algorithm returns such an mgu for the given terms,
along with an associated approximation degree, which indicates how similar the
instances of the terms are under the unifier. Importantly, the computed unifier
has the maximal possible approximation degree. This degree must meet or ex-
ceed a user-defined threshold (also known as a cut value). When the threshold is
set to the maximal value 1, the algorithm computes standard (i.e., crisp) unifiers.

--- Page 3 ---

Higher-Order Pattern Unification Modulo Similarity Relations
3
In this case, it can be viewed as a rule-based version of the standard higher-order
pattern unification algorithm.
Our presentation differs from traditional accounts of higher-order pattern
unification and fuzzy unification by introducing a dedicated subalgorithm for
variable elimination. This design has two main benefits. First, it simplifies the
termination proof. Second, it enhances modularity, making it easier to integrate
alternative T-norms: only the subalgorithm requires modification in such cases.
Organization. Section 2 introduces the basic notions and establishes fundamental
properties. The core of the paper is Section 3, where we define the algorithm
and prove its termination, soundness, and completeness. In Section 4, we discuss
two topics: (a) the crisp counterpart of our algorithm and its relation to existing
higher-order pattern unification algorithms; and (b) possible extensions using T-
norms other than the minimum (Gödel) T-norm employed in this work. Section 5
concludes the paper.
2
Preliminaries
Term Language. Given a set of basic types, whose elements are denoted by
δ, simple types are constructed using the grammar τ ::= δ | τ →τ, where τ is
associative to the right. The alphabet of our language consists of the set V of
variables and F of constants. They are disjoint and countably infinite and their
elements have assigned types. It is assumed that for each basic type, there is at
least one function symbol (types are not empty). Variables are typically denoted
by F, G, H, X, Y, Z, x, y, z, . . . and constants by f, g, a, b, c, . . .. The set of terms
over F and V, denoted by T (F, V), is defined by the grammar
t ::= x | c | λx.t | (t1 t2),
where λx.t is called an abstraction and (t1 t2) is called an application. We denote
terms by t, s, r.
The following standard abbreviations are used: (t1 t2 t3 · · · tn), n ≥3, for
(· · · ((t1 t2) t3) · · · tn), and λx1, . . . , xn.t, n ≥2, for λx1.(λx2.(. . . (λxn.t))).
A term t is said to have the type τ if either
– t is a constant or a variable of type τ,
– t = λx.s, the variable x has type ρ, the term s has type ϕ, and τ = ρ →ϕ,
– t = (s r), where the term s has type ρ →τ and the term r has type ρ for
some ρ.
The standard concepts of the simply-typed λ-calculus, such as bound and
free occurrences of variables, position in a term, α-conversion, β-reduction, and
η-long β-normal form, are defined in the usual way, see, e.g., [2, 4]. The set of
positions of a term t is denoted by Pos(t). The η-long β-normal form of a term t
is denoted by t ↕η
β. For any t, the term t ↕η
β has the form λx1, . . . xn.(h t1 · · · tm),
where n, m ≥0, the symbol h (called the head of the term) is either a constant

--- Page 4 ---

4
B. Dundua and T. Kutsia
or a variable, and each ti (for i = 1, . . . , m) follows the same structural form.
Moreover, the term (h t1 · · · tm) has a basic type. We follow the standard con-
vention of writing terms in η-long β-normal form as λx1, . . . , xn.h(t1, . . . , tm).
When we write an equality between two λ-terms, we mean that they are equiv-
alent modulo α-, β-, and η-equivalence. The size of a term t, denoted size(t), is
defined recursively as size(x) = size(f) = 1, size((t1 t2)) = size(t1) + size(t2),
and size(λx.t) = 1 + size(t).
The sets of free and bound variables of a term t are denoted by fv(t) and
bv(t), respectively. As a convention and for the sake of clarity, in what follows, we
distinguish bound and free variables syntactically. In particular, we use lowercase
letters x, y, z for bound variables and capital letters X, Y, Z, F, G, H for free
variables. A term is called rigid if its head symbol is a constant or a bound
variable, and it is called flexible, if its head symbol is a free variable.
Definition 1 (Higher-order patterns). A higher-order pattern is a term
where, when written in η-long β-normal form, all free variable occurrences are
applied to lists of pairwise distinct (η-long forms of) bound variables.
A substitution σ is a mapping from variables to terms such that for each
variable x of type τ, the term σ(x) is of type τ, and all but finitely many variables
are mapped to themselves (modulo αβη). Greek letters σ, ϑ, φ, τ, ε are used for
substitutions, where ε denotes the identity substitution. Each substitution σ
is represented as a finite set of pairs {x1 7→σ(x1), . . . , xn 7→σ(xn)} where
the x’s are variables for which σ(xi) ̸= xi. The sets Dom(σ) = {x1, . . . , xn}
and Ran(σ) = {σ(x1), . . . , σ(xn)} are called the domain and the range of σ,
respectively. The set fv(σ) is defined as fv(σ) = Dom(σ) ∪fv(Ran(σ)) where
fv(Ran(σ)) = ∪n
i=1fv(σ(xi))
The application of a substitution σ to t replaces each free occurrence of a
variable x in t with σ(x). It is defined inductively:
xσ = σ(x),
if x ∈Dom(σ).
xσ = x,
if x /∈Dom(σ).
fσ = f.
(λx.t)σ = λx.tσ,
if x /∈fv(σ).
(λx.t)σ = λy.t{x 7→y}σ,
if x ∈fv(σ) and y is fresh.
(t s)σ = (tσ sσ).
Fuzzy Relations. We define basic notions about fuzzy relations following [31].
A binary fuzzy relation on a set S is a mapping from S × S to the real interval
[0, 1]. If R is a fuzzy relation on S and µ is a number 0 < µ ≤1 (called cut
value), then the µ-cut of R on S, denoted Rµ, is an ordinary (crisp) relation on
S defined as Rµ := {(s1, s2) | R(s1, s2) ≥µ}.
A T-norm ∧is an associative, commutative, non-decreasing binary operation
on [0, 1] with 1 as the unit element. Some of the most prominent T-norms are
– Gödel (or minimum) T-norm: s1 ∧s2 = min(s1, s2),

--- Page 5 ---

Higher-Order Pattern Unification Modulo Similarity Relations
5
– Product T-norm: s1 ∧s2 = s1 ∗s2,
– Łukasiewicz T-norm: s1 ∧s2 = max(0, s1 + s2 −1).
Definition 2 (Similarity relation). A fuzzy relation R on a set S is called
a proximity relation, if it is reflexive (R(s, s) = 1 for all s ∈S) and symmet-
ric (R(s1, s2) = R(s2, s1) for all s1, s2 ∈S). A proximity relation is called a
similarity relation if it is ∧-transitive: R(s1, s2) ≥R(s1, s) ∧R(s, s2) for any
s1, s2, s ∈S.
In the role of S, we take the set of terms of our language. First, we assume
a fuzzy relation RA to be defined on the alphabet F ∪V in such a way that
– RA(x, y) = 0 for all x, y ∈V with x ̸= y,
– RA(f, g) = 0 for all f, g ∈F such that f and g have different types.
– RA(x, f) = RA(f, x) = 0 for all x ∈V and f ∈F.
Definition 3 (Fuzzy relation on terms). Given a fuzzy relation RA on the
alphabet F ∪V, we define a fuzzy relation R on the set of terms T (F, V) using
the T-norm ∧.
1. If t and s are in η-long β-normal form, then R(t, s) is defined as follows:
R(a, b) = RA(a, b), where a, b ∈F ∪V,
R((t1 s1), (t2 s2)) = R(t1, t2) ∧R(s1, s2),
R(λx.t, λy.s) = R(t{x 7→z}, s{y 7→z}),
where x, y, and z have the same type and z is a fresh variable,
R(t, s) = 0 otherwise.
2. Otherwise, R(t, s) = R(t ↕η
β, s ↕η
β).
It is easy to see that if RA is a proximity relation on the alphabet, then R is
a proximity relation on terms for any T-norm. This definition also implies that
if R(t, s) > 0, then
– t and s have the same type,
– Pos(t ↕η
β) = Pos(s ↕η
β),
– for each p ∈Pos(t ↕η
β), symbols occurring at position p in t ↕η
β and s ↕η
β have
the same type,
– a variable (resp. a constant) occurs at position p in t ↕η
β iff a variable (resp.
a constant) occurs at position p in s ↕η
β,
– a free variable X occurs at position p in t ↕η
β iff the same variable X occurs
at position p in s ↕η
β.
Note that if the T-norm is not idempotent, one can find a substitution σ
such that R(t, s) > 0 does not imply R(t, s) = R(tσ, sσ). For instance, for the
product T-norm, R(a, b) = 0.5, and σ = {X 7→λx.f(x, x)} we have
R(X(a), X(b)) = 0.5,

--- Page 6 ---

6
B. Dundua and T. Kutsia
R(X(a)σ, X(b)σ) = R(f(a, a), f(b, b)) = 0.5 ∗0.5 = 0.25.
However, this problem does not arise when the T-norm is idempotent, or
when terms are higher-order patterns:
Proposition 1. Let R be a similarity relation on terms using the T-norm ∧,
t and s be terms, and σ be a substitution. Then R(t, s) > 0 implies R(t, s) =
R(tσ, sσ) if (a) ∧is idempotent, or (b) t and s are higher-order patterns.
Proof. Assume without loss of generality that t and s are in η-long β-normal
form. They have the same structure, since R(t, s) > 0. We proceed by structural
induction.
t and s are variables. Then t = s, tσ = sσ, and R(tσ, sσ) = R(t, s) = 1.
t and s are constants. Then tσ = t, sσ = s, and R(tσ, sσ) = R(t, s).
t = λx1, . . . , xn.h1(t′
1, . . . , t′
m) and s = λx1, . . . , xn.h2(s′
1, . . . , s′
m), where h1
and h2 are either both variables or both constants. Then R(t, s) = RA(h1, h2) ∧
R(t′
1, s′
1) ∧· · · ∧R(t′
m, s′
m). By the induction hypothesis, R(t′
i, s′
i) = R(t′
iσ, s′
iσ)
for all 1 ≤i ≤m.
– If h1 and h2 are constants or bound variables, then h1σ = h1, h2σ = h2 and
R(tσ, sσ) = R(t, s).
– If h1 and h2 are free variables, then they should be the same (since R(t, s) >
0), say X. We consider two cases:
• t and s are patterns. Then t′
i = s′
i ∈{x1, . . . , xn}. Therefore, t = s and
R(tσ, sσ) = R(t, s) = 1.
• t and s are not patterns. If X /∈Dom(σ), then the reasoning is like for
bound variables above. If X ∈Dom(σ), then let Xσ = λy1, . . . , ym.r.
Then
tσ = λx1, . . . , xn.r{y1 7→t′
1} · · · {ym 7→t′
m},
sσ = λx1, . . . , xn.r{y1 7→s′
1} · · · {ym 7→s′
m}.
If r is linear (i.e., no yi occurs in it more than once), then R(tσ, sσ) =
R(t′
1, s′
1)∧· · ·∧R(t′
m, s′
m) = R(t, s). Now let ∧be idempotent and assume
without loss of generality that y1 appears in r twice. Then R(tσ, sσ) =
R(t′
1, s′
1) ∧R(t′
1, s′
1) ∧· · · ∧R(t′
m, s′
m) =
(by idempotence of ∧)
=
R(t′
1, s′
1) ∧· · · ∧R(t′
m, s′
m) = R(t, s).
⊓⊔
Theorem 1. If RA is a similarity relation on the alphabet, then R is a simi-
larity relation on terms for any T-norm.
Proof. We only need to show that for arbitrary terms t, s, r in η-long β-normal
form and a T-norm ∧, the ∧-transitivity property holds: R(t, r) ≥R(t, s) ∧
R(s, r). Assume without loss of generality that R(t, s) ∧R(s, r) > 0. Then
by the monotonicity of T-norms we have R(t, s) > 0 and R(s, r) > 0, which
implies that t, s, and r have the same structure. We proceed by induction on
this structure.

--- Page 7 ---

Higher-Order Pattern Unification Modulo Similarity Relations
7
– When {t, s, r} ∈F ∪V, the property follows from the assumption that RA
is a similarity.
– Let t = (t1 t2), s = (s1 s2), and r = (r1 r2). By definition of R, we have
R(t, r) = R(t1, r1) ∧R(t2, r2), R(t, s) = R(t1, s1) ∧R(t2, s2), and R(s, r) =
R(s1, r1) ∧R(s2, r2). By the induction hypothesis, we know R(ti, ri) ≥
R(ti, si) ∧R(si, ri), i = 1, 2. Then, by monotonicity of T-norms, we get
R(t1, r1) ∧R(t2, r2) ≥R(t1, s1) ∧R(s1, r1) ∧R(t2, s2) ∧R(s2, r2), from
which, by associativity and commutativity of ∧and the definition of R, we
get R((t1 t2), (r1 r2)) ≥R((t1 t2), (s1 s2))∧R((s1 s2), (r1 r2)) for any T-norm
∧.
– Let t = λx.t′, s = λy.s′, and r = λz.r′, where x, y, z have the same type.
By definition of R, without loss of generality, we can choose a fresh variable
u of the same type such that R(λx.t′, λz.r′) = R(t′{x 7→u}, r′{z 7→u}),
R(λx.t′, λy.s′) = R(t′{x 7→u}, s′{y 7→u}), and R(λy.s′, λz.r′) = R(s′{y 7→
u}, r′{z 7→u}). By the induction hypothesis, we have R(t′{x 7→u}, r′{z 7→
u}) ≥R(t′{x 7→u}, s′{y 7→u}) ∧R(s′{y 7→u}, r′{z 7→u}) for any T-norm,
which implies R(λx.t′, λz.r′) ≥R(λx.t′, λy.s′) ∧R(λy.s′, λz.r′) for any T-
norm.
⊓⊔
Given a similarity relation R, cut value µ, and two terms t, s, we write
t ≃R,µ s if R(t, s) ≥µ. The number R(t, s) is called the R-similarity degree of
t and s.
We say σ is (R, µ)-more general than ϑ with variable restriction V , written
σ ⪯V
R,µ ϑ, if there exists a substitution τ such that xστ ≃R,µ xϑ for all x ∈V .
Definition 4 (Unification problem, unifier, unification degree, mgu).
An (R, µ)-unification equation between terms t and s is written as t ≃?
R,µ s,
where R is a similarity relation and µ is a cut value. An (R, µ)-unification
problem is a finite set of (R, µ)-unification equations. A substitution σ is a
unifier (or a solution) of an (R, µ)-unification problem {t1 ≃?
R,µ s1, . . . , t1 ≃?
R,µ
s1} with unification degree d if R(t1σ, s1σ) ∧· · · ∧R(tnσ, snσ) = d ≥µ.
Given an (R, µ)-unification problem P, we say that its (R, µ)-unifier σ is
a most general (R, µ)-unifier of P if for any (R, µ)-unifier ϑ of P we have
σ ≾fv(P )
R,µ
ϑ.
We consider a special case of this problem: all terms that appear in the
unification problems and unifiers should be higher-order patterns. In the rest of
the paper, we make the following assumptions (those related to terms follow [26]):
– min: T-norm ∧is the minimum T-norm,
– α: α-equivalent terms are identified,
– β: terms are β-normalized by default,
– η: terms are in η-expanded form except for the arguments of free variables,
which are in η-normal form, i.e., bound variables.

--- Page 8 ---

8
B. Dundua and T. Kutsia
Example 1. Higher-order pattern (R, µ)-unification problems may have most
general unifiers that are or are not degree-maximal, and may have degree-
maximal unifiers that are or are not most general. We illustrate it with an
(R, µ)-unification problem between
t = λx.λy.f(F(x), F(y)) and
s = λx.λy.g(a(G(y, x)), b(G(x, y))),
where R is defined as R(f, g) = 0.8, R(a, b) = 0.6, R(b, c) = R(a, c) = 0.5,
and the cut value is µ = 0.4. Consider the following (R, µ)-unifiers of t and s
together with their unification degrees:
σ1 = {F 7→λx.a(H(x)), G 7→λy.λx.H(x)},
d1 = 0.6.
σ2 = {F 7→λx.b(H(x)), G 7→λy.λx.H(x)},
d2 = 0.6.
σ3 = {F 7→λx.c(H(x)), G 7→λy.λx.H(x)},
d3 = 0.5.
σ4 = {F 7→λx.a(a(x)), G 7→λy.λx.a(x)},
d4 = 0.6.
σ5 = {F 7→λx.c(a(x)), G 7→λy.λx.a(x)},
d5 = 0.5.
From these unifiers, σ1, σ2 and σ3 are most general ones on V = {F, G}. (They
are equivalent to each other modulo similarity.) Hence, we have two most general
unifiers σ1, σ2 with the maximum degree, and one with a lower degree. The unifier
σ4 is strictly less general on V than the first three, yet its unification degree is
maximal. As for σ5, it is neither most general nor degree-maximal unifier.
Our goal is to design an algorithm that computes a degree-maximal most
general unifier. Hence, for this problem, computing either σ1 or σ2 would be the
desired outcome.
3
Similarity-based unification of higher-order patterns
In this section, we formulate a similarity-based unification algorithm in a rule-
based manner. The rules operate on triples P; σ; d, referred to as unification
configurations, where P is a similarity-based unification problem, σ is the sub-
stitution computed so far, and d is the approximation degree, also computed so
far. The similarity relation R and the cut value µ are implicit parameters, and
it is assumed that d ≥µ in configurations.
The rules are given below. The symbol ⊎stands for disjoint union. The rule
LF calls an auxiliary function VarElim (which is also defined below) with the
sides of the selected equation as arguments.
Abs: Abstraction
{λx.t ≃?
R,µ λx.s} ⊎P; σ; d ⇝{t ≃?
R,µ s} ∪P; σ; d.
Dec: Decomposition
{f(t1, . . . , tn) ≃?
R,µ g(s1, . . . , sn)} ⊎P; σ; d ⇝
{t1 ≃?
R,µ s1, . . . , tn ≃?
R,µ sn} ∪P; σ; d ∧R(f, g),
where n ≥0 and (d ∧R(f, g)) ≥µ.

--- Page 9 ---

Higher-Order Pattern Unification Modulo Similarity Relations
9
SV: Same variables
{F(x1, . . . , xn) ≃?
R,µ F(y1, . . . , yn)} ⊎P; σ; d ⇝Pϑ; σϑ; d,
where n ≥0 and
– {z1, . . . , zm} = {xi | xi = yi, 1 ≤i ≤n}, m ≥0 (i.e., each z is a variable that
appears in the same position in both the sequences x1, . . . , xn and y1, . . . , yn),
– ϑ = {F 7→λx1, . . . , xn.H(z1, . . . , zm)} for a fresh variable H of the appro-
priate type.
Ori: Orient
{a(s1, . . . , sm) ≃?
R,µ F(x1, . . . , xn)} ⊎P; σ; d ⇝
{F(x1, . . . , xn) ≃?
R,µ a(s1, . . . , sm)} ∪P; σ; d,
where n, m ≥0, F is a free variable and a is a constant or a ∈{x1, . . . , xn}.
LF: Left-flex
{F(x1, . . . , xn) ≃?
R,µ a(s1, . . . , sm)} ⊎P; σ; d ⇝Pϑ; σϑ; d
where n, m ≥0 and
– F /∈fv(a(s1, . . . , sm)),
– a is a constant, free variable, or a ∈{x1, . . . , xn},
– VarElim(F(x1, . . . , xn), a(s1, . . . , sm)) = φ,
– ϑ = φ|V , where V = {F} ∪fv(a(s1, . . . , sm)).
Fail: Failure
{t ≃?
R,µ s} ⊎P; σ; d ⇝⊥,
if no other rule applies to the selected equation t ≃?
R,µ s.
For our minimum T-norm, it would suffice to have R(f, g) ≥µ instead of
(d ∧R(f, g)) ≥µ in the condition of the Dec rule. However, we decided to keep
this more general requirement since it can be used with any T-norm. See also
Section 4 for related discussion.
Analyzing the rules, it is not hard to see that when the failure rule applies,
we have one of the following three cases:
– t and s have different types,
– t = f(t1, . . . , tn), s = g(s1, . . . , sn), and (d ∧R(f, g)) < µ, or
– t = F(x1, . . . , xn), s = a(s1, . . . , sm), and F ∈fv(a(s1, . . . , sm)).
In each of these cases, t ≃?
R,µ s is unsolvable, which justifies the name of the
rule.
In the LF rule, if a is a free variable, then s1, . . . , sm are distinct bound
variables (since we work only with higher-order patterns). By this rule, in order
to unify a flexible term t and a term s, the auxiliary function VarElim(t, s) is
called, which creates an initial configuration {t ≃? s}; ε and applies the VE1 and
VE2 rules below as long as possible. If the process stops with the configuration
∅; φ, we say that φ is the answer computed by VarElim for t and s and write

--- Page 10 ---

10
B. Dundua and T. Kutsia
VarElim(t, s) = φ. Note that φ might contain bindings for variables introduced
in the process of VarElim, which appear neither in t nor in s. Therefore, in ϑ,
we keep only those bindings from φ that are relevant to t and s. Note also that
VarElim is independent of R and does not involve the degree computation.
VE1: Variable elimination 1
{F(x1, . . . , xn) ≃? a(s1, . . . , sm)} ⊎P; σ ⇝
{H1(x1, . . . , xn) ≃? s1, . . . , Hm(x1, . . . , xn) ≃? sm} ∪P; σϑ,
where n, m ≥0 and
– a is a constant or a ∈{x1, . . . , xn},
– ϑ = {F 7→λx1, . . . , xn.a(H1(x1, . . . , xn), . . . , Hm(x1, . . . , xn))} where the
variables H1, . . . , Hm are fresh and have appropriate types.
– (Note that if si for 1 ≤i ≤m, is of function type, the term Hi(x1, . . . , xn)
must be η-expanded in both the new configuration and the substitution.)
VE2: Variable elimination 2
{F(x1, . . . , xn) ≃? G(y1, . . . , ym)} ⊎P; σ; ⇝Pϑ; σϑ,
where n, m ≥0, and
– {x1, . . . , xn} ∩{y1, . . . , ym} = {z1, . . . , zk},
– ϑ = {F 7→λx1, . . . , xn.H(z1, . . . , zk), G 7→λy1, . . . , ym.H(z1, . . . , zk)} with
H being a fresh variable of the appropriate type.
Note that when VarElim is invoked, it is always called with terms t and s
where t has the form F(x1, . . . , xn) such that the variable F does not occur in s.
Applying VE1 or VE2 to the initial configuration {F(x1, . . . , xn) ≃? s}; ε creates
a new configuration in which F does not appear anymore, and if the variables
introduced instead of it appear on the left-hand sides, then they are unique
again. Hence, the configurations P; σ to which VE1 and VE2 apply satisfy the
following invariant:
– If an equation of the form F(x1, . . . , xn) ≃? s appears in P, then F is unique.
Consequently, in VE1, it does not make sense to apply the generated substi-
tution to the remaining unification problem. That is why we have P and not Pϑ
on the right-hand side of VE1. On the other hand, we need Pϑ in VE2, because
P might contain G.
Given a similarity relation R, the cut value µ, and two terms t and s, to find
an (R, µ)-unifier of t and s, the algorithm Hops creates the initial configuration
{t ≃?
R,µ s}; ε; 1 and applies the rules above as long as possible. It means that
Hops can be defined as the following strategy where nf stands for normal form:
Hops := nf(Step).
Step := choice(Abs, Dec, SV, Ori, LF, Fail).
It is easy to see that for each selected equation, only one rule applies. Hence,
Step is deterministic in the sense that it transforms a given configuration C in
only one way. We refer to the result of transformation as Step(C).

--- Page 11 ---

Higher-Order Pattern Unification Modulo Similarity Relations
11
Example 2. We illustrate the algorithm to solve an (R, µ)-unification problem
from Example 1. We create the initial configuration
{λx.λy.f(F(x), F(y)) ≃?
R,0.4 λx.λy.g(a(G(y, x)), b(G(x, y)))}; ε; 1
and apply the transformation rules as follows:
{λx.λy.f(F(x), F(y)) ≃?
R,0.4 λx.λy.g(a(G(y, x)), b(G(x, y)))}; ε; 1 ⇝Abs
{λy.f(F(x), F(y)) ≃?
R,0.4 λy.g(a(G(y, x)), b(G(x, y)))}; ε; 1 ⇝Abs
{f(F(x), F(y)) ≃?
R,0.4 g(a(G(y, x)), b(G(x, y)))}; ε; 1 ⇝Dec
{F(x) ≃?
R,0.4 a(G(y, x)), F(y) ≃?
R,0.4 b(G(x, y))}; ε; 0.8 ⇝LF
Application of LF requires steps of the VarElim:
{F(x) ≃? a(G(y, x))}; ε ⇝VE1
{H1(x) ≃? G(y, x)}; {F 7→λx.a(H1(x))} ⇝VE2
∅; {F 7→λx.a(H2(x)), G 7→λyλx.H2(x), H1 7→λx.H2(x)}
VarElim returns {F 7→λx.a(H2(x)), G 7→λyλx.H2(x)} and we continue:
{a(H2(y)) ≃?
R,0.4 b(H2(y))};
{F 7→λx.a(H2(x)), G 7→λyλx.H2(x)}; 0.8 ⇝Dec
{H2(y) ≃?
R,0.4 H2(y)}; {F 7→λx.a(H2(x)), G 7→λyλx.H2(x)}; 0.6 ⇝SV
∅; {F 7→λx.a(H(x)), G 7→λyλx.H(x), H2 7→λx.H(x)}; 0.6
Hence, we obtained the substitution {F 7→λx.a(H(x)), G 7→λyλx.H(x), H2 7→
λx.H(x)} and the degree 0.6. It is easy to check that the substitution is indeed a
unifier of the given terms with degree 0.6. Note also that not all the bindings from
the substitution are relevant: we can restrict it only to the free variables of the
given terms, getting {F 7→λx.a(H(x)), G 7→λyλx.H(x)}, which corresponds to
σ1 from Example 1. If we applied the LF rule to the second equation F(y) ≃?
R,0.4
b(G(x, y)) instead of the first one, we would get the unifier σ2 from Example 1.
If we increase the cut value to, say, 0.7, the problem does not have a solution
and the algorithm reaches a configuration to which the failure rule applies:
{a(H2(y)) ≃?
R,0.7 b(H2(y))}; {F 7→λx.a(H2(x)), G 7→λyλx.H2(x)}; 0.8 ⇝Fail ⊥.
When µ = 1, the problem is a crisp (i.e., standard) higher-order pattern
unification problem, which obviously is not solvable due to the mismatch between
f and g. The algorithm detects it, stopping with failure after the application of
the abstraction steps.
Theorem 2 (Termination of Hops). Hops terminates for any input either
with ∅; σ; d or with ⊥.
Proof. We first establish that VarElim(t, s) always terminates. This procedure
starts by constructing the initial configuration {t ≃?
R,µ s}; ε and then repeat-
edly applies the VE1 and VE2 rules. To each configuration P; σ we associate a

--- Page 12 ---

12
B. Dundua and T. Kutsia
complexity measure as the multiset of the sizes of equations in P, denoted by
ms(P) := {{size(t) + size(s) | t ≃?
R,µ s ∈P}}. To order the measures, we use the
multiset extension of the standard ordering on natural numbers (Dershowitz-
Manna ordering [3]). Both VE1 and VE2 rules strictly decrease this measure,
ensuring that the reduction process cannot continue indefinitely. Consequently,
VarElim(t, s) must terminate.
Now we show termination of Hops. For this, we define a complexity measure
cm(C) for a configuration C = (P; σ; d), and show that cm(C) > cm(Step(C))
holds. The measure is the triple cm(C) = ⟨N1, N2, N3⟩defined as follows:
– N1 is the number of distinct variables in P,
– N2 := ms(P),
– N3 is the number of equations in P with a rigid left-hand side and a flexible
right-hand side (rigid-flex equations).
We treat ⊥as a special configuration and define its measure as cm(⊥) =
⟨0, ∅, 0⟩. Measures are compared lexicographically. For N2, we use the Dershowitz-
Manna ordering. The table below shows which rule reduces which component of
the measure.
Rule
N1 N2 N3
LF
>
Abs, Dec, SV, Fail
≥>
Ori
≥≥>
Hence, each rule strictly reduces cm(C). Since the ordering is well-founded, it
implies the termination of the algorithm. It is obvious that there are only two
alternatives for the final configuration: either the first component is empty, or it
is ⊥. It finishes the proof.
⊓⊔
When Hops stops with ∅; σ; d, we say that Hops succeeds with the computed
answer (σ, d) (or computes (σ, d)). If it stops with ⊥, we say that Hops fails. For
a similarity relation R, a cut value µ, and two terms t and s, if Hops computes
(σ, d), we write Hops(t, s, R, µ) = (σ, d).
Lemma 1. Let R be a similarity relation, µ a cut value and P; σ; d a configu-
ration. If Step(P; σ; d) = (P ′; σϑ; d ∧d′) and τ is an (R, µ)-unifier of P ′ with
degree d′′, then ϑτ is an (R, µ)-unifier of P with degree d′ ∧d′′.
Proof. First, we prove the soundness of VarElim. This will be needed to show the
soundness of the LF rule. Note that the rules VE1 and VE2 are the standard vari-
able elimination rules used in the crisp higher-order pattern unification [24,26]
under the condition that the free variables in the left-hand side of the equations
are unique in the problem. Then their soundness follows from the soundness of
the corresponding rules in the standard higher-order pattern unification.
Further, we proceed by case distinction on the inference rules of Hops. We
illustrate here three cases when the selected rules are Dec, SV, and LF. For the
other rules, the lemma can be shown similarly.

--- Page 13 ---

Higher-Order Pattern Unification Modulo Similarity Relations
13
– Step transforms the given configuration by the Dec rule, i.e., we have
{f(t1, . . . , tn) ≃?
R,µ g(s1, . . . , sn)} ⊎P; σ; d ⇝Dec-SU
{t1 ≃?
R,µ s1, . . . , tn ≃?
R,µ sn} ∪P; σ; d ∧R(f, g).
Then ϑ = ε and d′ = R(f, g) ≥µ. Let τ be an (R, µ)-unifier of the problem
{t1 ≃?
R,µ s1, . . . , tn ≃?
R,µ sn} ∪P with the degree d′′. This means,
d′′ = R(t1τ, s1τ) ∧· · · ∧R(tnτ, snτ) ∧d ≥µ,
where d = V
(t≃?
R,µs)∈P R(tτ, sτ). Since d′ ≥µ and d′′ ≥µ, we have d′ ∧d′′ ≥
µ. Moreover,
d′ ∧d′′ = d′ ∧R(t1τ, s1τ) ∧· · · ∧R(tnτ, snτ) ∧d
= R(f, g) ∧R(t1τ, s1τ) ∧· · · ∧R(tnτ, snτ) ∧d
= R(f(t1, . . . , tn)τ, g(s1, . . . , sn)τ) ∧d,
which implies that τ = ϑτ is an (R, µ)-unifier of the unification problem
{f(t1, . . . , tn) ≃?
R,µ g(s1, . . . , sn)} ⊎P with degree d′ ∧d′′.
– Step transforms the given configuration by the SV rule, i.e., we have
{F(x1, . . . , xn) ≃?
R,µ F(y1, . . . , yn)} ⊎P; σ; d ⇝SV Pϑ; σϑ; d.
where ϑ = {F 7→λx1, . . . , xn.H(z1, . . . , zm)}, {z1, . . . , zm} = {xi | xi =
yi, 1 ≤i ≤n}. We also have d′ = 1. Let τ be an (R, µ)-unifier of Pϑ with
the degree d′′. This means that d′′ = V
(tϑ≃?
R,µsϑ)∈P ϑ R(tϑτ, sϑτ) ≥µ. Then
ϑτ is also unifier of {F(x1, . . . , xn) ≃?
R,µ F(y1, . . . , yn)} ⊎P with degree d′′.
Indeed, we have
R(F(x1, . . . , xn)ϑτ, F(y1, . . . , yn)ϑτ) ∧
^
(t≃?
R,µs)∈P
R(tϑτ, sϑτ)
= R(H(z1, . . . , zm)τ, H(z1, . . . , zm)τ) ∧
^
(tϑ≃?
R,µsϑ)∈P ϑ
R(tϑτ, sϑτ)
= 1 ∧d′′ = d′′.
– Step transforms the given configuration by the LF rule, i.e., we have
{F(x1, . . . , xn) ≃?
R,µ a(s1, . . . , sm)} ⊎P; σ; d ⇝LF Pϑ; σϑ; d,
where ϑ is an (R, µ)-unifier of F(x1, . . . , xn) ≃?
R,µ a(s1, . . . , sm) with de-
gree d′ = 1. Let τ be an (R, µ)-unifier of Pϑ with degree d′′. Hence, d′′ =
V
(tϑ≃?
R,µsϑ)∈P ϑ R(tϑτ, sϑτ) ≥µ. Then, since ϑ is an (R, µ)-unifier of the
problem F(x1, . . . , xn) ≃?
R,µ a(s1, . . . , sm) with degree d′, so is ϑτ. Hence,
we get
R(F(x1, . . . , xn)ϑτ, a(s1, . . . , sm)ϑτ) ∧
^
(t≃?
R,µs)∈P
R(tϑτ, sϑτ)

--- Page 14 ---

14
B. Dundua and T. Kutsia
= d′ ∧
^
(tϑ≃?
R,µsϑ)∈P ϑ
R(tϑτ, sϑτ) = 1 ∧d′′ = d′′,
which means that the substitution ϑτ is an (R, µ)-unifier of the unification
problem {F(x1, . . . , xn) ≃?
R,µ a(s1, . . . , sm)} ⊎P with degree d′′.
⊓⊔
Theorem 3 (Soundness of Hops).
Given a similarity relation R, a cut
value µ, and two terms t and s, if Hops(t, s, R, µ) = (σ, d), then d ≥µ and
R(tσ, sσ) = d, i.e., σ is an (R, µ)-unifier of t and s with degree d.
Proof. From Hops(t, s, R, µ) = (σ, d) we have the derivation
P0; σ0; d0 ⇝P1; σ0ϑ1; d0 ∧d1 ⇝∗Pn; σ0ϑ1 · · · ϑn; d0 ∧d1 ∧· · · ∧dn,
where
P0 = {t ≃?
R,µ s},
σ0 = ε,
d0 = 1,
Pn = ∅,
σ = σ0ϑ1 · · · ϑn = ϑ1 · · · ϑn,
d = d0 ∧d1 ∧· · · ∧dn = d1 ∧· · · ∧dn.
Therefore, we get the desired result using induction on the length of the deriva-
tion with Lemma 1.
⊓⊔
Lemma 2. Let R be a similarity relation, µ a cut value and P0; σ0; d0 a configu-
ration. Assume τ is an (R, µ)-unifier of P0 with degree dτ ≥µ and σ0 ⪯Dom(τ)
R,µ
τ.
Then we can make a step Step(P0; σ0; d0) = (P1; σ1; d1) such that
– d1 = d0 ∧d′
1 for some d′
1,
– there exists a substitution φ1 such that
• Dom(φ1) = fv(P1) \ fv(P0) (the set of new free variables in P1),
• fv(Ran(φ1)) ∩Dom(τ) = ∅,
• φ1τ is an (R, µ)-unifier of P1 with degree dφ1τ ≥µ such that dτ ≤
d′
1 ∧dφ1τ, and
• σ1 ≾Dom(φ1τ)
R,µ
φ1τ.
Proof. Assume without loss of generality that τ is idempotent. We prove the
lemma by case distinction on the rules applied by Step. For rules Abs and Ori
it is simple. The Fail rule cannot apply, because it handles cases for which P is
not solvable, while by assumption, τ is a solution of P. We concentrate on the
remaining rules.
Dec: In this case, P0 = {f(t1, . . . , tn) ≃?
R,µ g(s1, . . . , sn)} ⊎P and the applica-
tion of the rule gives P1; σ1; d1, where P1 = {t1 ≃?
R,µ s1, . . . , tn ≃?
R,µ sn}∪P,
σ1 = σ0, and d1 = d0 ∧R(f, g). We take R(f, g) as d′
1 and φ1 = ε. Assume
τ is an (R, µ)-unifier of P0 with degree µ ≤dτ and σ0 ⪯Dom(τ)
R,µ
τ. Then τ is
also an (R, µ)-unifier of P and we denote its degree by dP . It implies that
µ ≤dτ = R(f(t1τ, . . . , tnτ), g(s1τ, . . . , snτ)) ∧dP

--- Page 15 ---

Higher-Order Pattern Unification Modulo Similarity Relations
15
= R(f, g) ∧R(t1τ, s1τ) ∧· · · ∧R(tnτ, snτ) ∧dP
= d′
1 ∧R(t1φ1τ, s1φ1τ) ∧· · · ∧R(tnφ1τ, snφ1τ) ∧dP .
Denote R(t1φ1τ, s1φ1τ) ∧· · · ∧R(tnφ1τ, snφ1τ) ∧dP by dφ1τ. Then the
previous inequality can be written as µ ≤d′
1 ∧dφ1τ, from which we get
µ ≤dφ1τ, implying that φ1τ is an (R, µ)-unifier of {t1 ≃?
R,µ s1, . . . , tn ≃?
R,µ
sn} ∪P with degree dφ1τ. Hence, we got that φ1τ is an (R, µ)-unifier of
P1 with degree µ ≤dφ1τ such that dτ = d′
1 ∧dφ1τ. Finally, from σ1 = σ0,
Dom(φ1τ) = Dom(τ), and σ0 ⪯Dom(τ)
R,µ
τ, we conclude σ1 ⪯Dom(φ1τ)
R,µ
τ.
SV: In this case, P0 = {F(x1, . . . , xn) ≃?
R,µ F(y1, . . . , yn)} ⊎P and the applica-
tion of the rule gives P1; σ1; d1 where P1 = Pϑ, σ1 = σ0ϑ, and d1 = d0 for the
substitution ϑ = {F 7→λx1, . . . , xn.H(z1, . . . , zm)} where {z1, . . . , zm} =
{xi | xi = yi, 1 ≤i ≤n}, m ≥0.
Since τ is an (R, µ)-unifier of P0, we have Fτ = λx1, . . . , xn.t, where t
is such a term that if some xi or yi, 1 ≤i ≤n, occurs in t, then this
variable should belong to {z1, . . . , zm}, otherwise τ would not be a unifier
of F(x1, . . . , xn) ≃?
R,µ F(y1, . . . , yn). It implies that Fτ can be actually
represented as
Fτ = (λx1, . . . , xn.H(z1, . . . , zm)){H 7→λz1, . . . , zm.t}.
(1)
We take d′
1 = 1 and φ1 = {H 7→λz1, . . . , zm.t}. Then
– d1 = d0 = d0 ∧d′
1,
– Dom(φ1) = {H} = fv(P1) \ fv(P0),
– fv(Ran(φ1)) ∩Dom(τ) = ∅, since τ is idempotent.
What remains to show is
– φ1τ is an (R, µ)-unifier of P1 with degree µ ≤dφ1τ such that dτ ≤
d′
1 ∧dφ1τ = dφ1τ, and
– σ1 ≾Dom(φ1τ)
R,µ
φ1τ.
To show the first of them, we prove that ϑφ1τ is an (R, µ)-unifier of P0 with
degree dτ. For this, take a variable X ∈fv(P0). If X ̸= F, then Xϑφ1τ = Xτ
since Xϑφ1 = X. As for X = F, we have
Fϑφ1τ =
 λx1, . . . , xn.H(z1, . . . , zm)

φ1τ = (by equality (1))
= Fττ = (by the idempotence of τ) = Fτ.
Hence, we can conclude that ϑφ1τ is an (R, µ)-unifier of P0 with degree
µ ≤dϑφ1τ = dτ, implying that φ1τ is an (R, µ)-unifier of P1 = Pϑ with
degree dτ.
Now we should prove σ1 ≾Dom(φ1τ)
R,µ
φ1τ. First, note that from σ0 ≾Dom(τ)
R,µ
τ,
there exists a substitution ψ0 (whose domain is disjoint from the free vari-
ables in the range of τ) such that Xσ0ψ0 ≃R,µ Xτ for all X ∈Dom(τ). De-
fine ψ1 = φ1∪ψ0. (Note that ψ0 can be chosen so that Dom(ψ0)∩(Dom(φ1)∪
fv(Ran(φ1))) = ∅and Dom(φ1) ∩(Dom(ψ0) ∪fv(Ran(ψ0))) = ∅.) Take a
variable X ∈Dom(φ1τ) = {H}⊎Dom(τ) and show that Xσ1ψ1 ≃R,µ Xφ1τ.

--- Page 16 ---

16
B. Dundua and T. Kutsia
1. X = H. Then Xσ1ψ1 = Xψ1 = Xφ1 = λz1, . . . , zm.t, where t is such
a term that Fτ = λx1, . . . , xn.t. But then, fv(t) ∩Dom(τ) = ∅and we
have λz1, . . . , zm.t = λz1, . . . , zm.tτ = Xφ1τ. Hence, Xσ1ψ1 = Xφ1τ.
2. X = F. Then
Xσ1ψ1 = Xσ0ϑψ1 = Xϑψ1 = λx1, . . . , xn.H(z1, . . . , zm)ψ1
= λx1, . . . , xn.H(z1, . . . , zm)φ1 = λx1, . . . , xn.t.
Xφ1τ = Xτ = λx1, . . . , xn.t.
Hence, also in this case, Xσ1ψ1 = Xφ1τ.
3. X ∈Dom(τ) \ {F}. We have two subcases:
– Xσ0ϑ = Xσ0. Then
Xσ1ψ1 = Xσ0ϑψ1 = Xσ0ψ1
= ≃R,µ Xτ (by the assumption on ψ0)
= Xφ1τ (since X /∈Dom(φ1)).
– Xσ0ϑ ̸= Xσ0, then we should show Zσ1ψ1 ≃R,µ Zφ1τ for all Z ∈
fv(Xσ0ϑ), which implies Xσ1ψ1 ≃R,µ Xφ1τ.
Proving Zσ1ψ1 ≃R,µ Zφ1τ for all Z ∈fv(Xσ0ϑ). From Xσ0ϑ ̸=
Xσ0 we have F ∈fv(Xσ0) and, therefore, H ∈fv(Xσ0ϑ). However,
for H we already saw that Hσ1ψ1 = Hφ1τ. For any other Y ∈
fv(Xσ0ϑ) (i.e., Y ̸= H, Y ̸= F) we should have Y ∈fv(Xσ0),
implying Y
/∈Dom(σ0) (since Y appears in the range of σ0 and
σ’s are idempotent). From Y /∈Dom(σ0) and Y ̸= F we get Y /∈
Dom(σ1) and, consequently, Y σ1ψ1 = Y ψ1. Then we have
Y σ1ψ1 = Y ψ1 = (since Y ̸= H) Y ψ0 = (since Y /∈Dom(σ0))
= Y σ0ψ0 ≃R,µ Y τ = Y φ1τ.
It proves Zσ1ψ1 ≃R,µ Zφ1τ for all Z ∈fv(Xσ0ϑ).
In both cases, we get Xσ1ψ1 ≃R,µ Xφ1τ.
Hence, in all three cases, we proved Xσ1ψ1 ≃R,µ Xφ1τ. It implies that
σ1 ≾Dom(φ1τ)
R,µ
φ1τ.
LF: Here P0 = {F(x1, . . . , xn) ≃?
R,µ a(s1, . . . , sm)} ⊎P and the application
of the rule gives P1; σ1; d1 where P1 = Pϑ, σ1 = σ0ϑ, and d1 = d0 for the
substitution ϑ where ϑ is computed by VarElim(F(x1, . . . , xn), a(s1, . . . , sm)).
Note that VarElim applies (crisp) rules VE1 and VE2. From [26] it follows
that repeated application of them leads to a most general pattern unifier
of F(x1, . . . , xn) and a(s1, . . . , sm). Therefore, ϑ is such an mgu and we
have F(x1, . . . , xn)ϑ = a(s1, . . . , sm)ϑ and ϑ ≾Dom(ϑ)
R,µ
τ, where Dom(ϑ) =
{F} ∪fv(a(s1, . . . , sm)). Note that all variables that appear in the range
of ϑ are new because none of the rules retain the original variables from
a(s1, . . . , sm). Then there exists a substitution φ1 such that
– Dom(φ1) = fv(P1) \ fv(P0) = fv(Ran(ϑ)),

--- Page 17 ---

Higher-Order Pattern Unification Modulo Similarity Relations
17
– fv(Ran(φ1)) ∩Dom(τ) = ∅, and
– Xϑφ1 ≃R,µ Xτ for all X ∈Dom(ϑ).
Therefore, by the idempotence of τ, we get Xϑφ1τ ≃R,µ Xτ for all X ∈
fv(P0). Moreover, we have
– R(Fϑφ1τ, a(s1, . . . , sm)ϑφ1τ) ≥R(Fτ, a(s1, . . . , sm)τ), and
– Xϑφ1τ = Xτ for all X ∈fv(P0) \ Dom(ϑ).
Therefore, ϑφ1τ solves P with the degree dϑφ1τ that is better than dτ. Note
that dϑφ1τ and the unification degree of φ1τ for Pϑ (i.e., dφ1τ) are the same
since s ≃?
R,µ t ∈P iff sϑ ≃?
R,µ tϑ ∈Pϑ and we have
dτ ≤dϑφ1τ =
^
s≃?
R,µt∈P
R(sϑφ1τ, tϑφ1τ)
=
^
sϑ≃?
R,µtϑ∈P ϑ
R(sϑφ1τ, tϑφ1τ) = dφ1τ.
From d1 = d0 = d′
1 ∧d0 for d′
1 = 1, this implies that φ1τ solves P1 = Pϑ
with degree dτ ≤dφ1τ.
The last thing to prove is σ1 ≾Dom(φ1τ)
R,µ
φ1τ. From σ0 ≾Dom(τ)
R,µ
τ, there
exists a substitution ψ0 such that
– Xσ0ψ0 ≃R,µ Xτ for all X ∈Dom(τ),
– Dom(ψ0) ∩fv(Ran(τ)) = ∅,
– Dom(ψ0) ∩(Dom(φ1) ∪fv(Ran(φ1))) = ∅, and
– Dom(φ1) ∩(Dom(ψ0) ∪fv(Ran(ψ0))) = ∅.
Let ψ1 = φ1 ∪ψ0. To prove σ1 ≾Dom(φ1τ)
R,µ
φ1τ, we show Xσ1ψ1 ≃R,µ Xφ1τ
for all X ∈Dom(φ1τ). We have the following cases:
– X ∈Dom(φ1). Then Xσ1ψ1 = Xσ0ϑψ1 = Xϑψ1 = Xψ1 = Xφ1 =
Xφ1τ (since fv(Ran(φ1) ∩Dom(τ) = ∅).
– X ∈Dom(ϑ). Then Xσ1ψ1 = Xσ0ϑψ1 = Xϑψ1 = Xϑφ1 ≃R,µ Xτ =
Xφ1τ.
– If X ∈Dom(τ) \ Dom(ϑ). We have two subcases:
• If Xσ0ϑ = Xσ0. then Xσ1ψ1 = Xσ0ϑψ1 = Xσ0ψ1 = Xσ0ψ0 ≃R,µ
xτ = xφ1τ.
• If Xσ0ϑ ̸= Xσ0, then we should show Zσ1ψ1 ≃R,µ Zφ1τ for all
Z ∈fv(Xσ0ϑ), which implies Xσ1ψ1 ≃R,µ Xφ1τ.
Proving Zσ1ψ1 ≃R,µ Zφ1τ for all Z ∈fv(Xσ0ϑ). For each Y ∈
fv(Ran(ϑ)) = Dom(φ1) we already saw that Y σ1ψ1 = Y φ1τ. For
each Y ∈fv(Ran(σ0))\(Dom(ϑ)) we have Y σ0ψ0 ≃R,µ Y τ = Y φ1τ.
On the other hand, for such a Y we have Y σ0ψ0 = Y ψ0 = Y =
Y ψ1 = Y σ1ψ1. Hance, in both cases we got Y σ1ψ1 ≃R,µ Y φ1τ,
which proves that Zσ1ψ1 ≃R,µ Zφ1τ for all Z ∈fv(Xσ0ϑ).
Hence, in all cases, we get Xσ1ψ1 ≃R,µ Xφ1τ. It implies that σ1 ≾Dom(φ1τ)
R,µ
φ1τ.
⊓⊔
Theorem 4 (Completeness of Hops). Given a similarity relation R, a cut
value µ, and two terms t and s, if there exists an (R, µ)-unifier τ of t and s
with degree dτ ≥µ, then Hops(t, s, R, µ) computes an answer (σ, d) such that
σ ≾Dom(τ)
R,µ
τ and d ≥dτ.

--- Page 18 ---

18
B. Dundua and T. Kutsia
Proof. First note that for any configuration P; σ; d, if P is (R, µ)-unifiable then
Step(P; σ; d) ̸= ⊥. This is based on the observation that Step gives ⊥in only
three cases: if P contains an equation between terms of different types, or an
equation f(t1, . . . , tn) ≃?
R,µ g(s1, . . . , sn) with d ∧R(f, g) < µ, or an equation
F(t1, . . . , tn) ≃?
R,µ a(s1, . . . , sn) with F ∈fv(a(s1, . . . , sn)). But in none of these
cases is P (R, µ)-unifiable.
Hence, for the initial configuration P0; σ0; d0 = {t ≃?
R,µ s}; ε; 1 we have that
τ is an (R, µ)-unifier of P0 with degree dτ ≥µ and σ0 ≾Dom(τ)
R,µ
τ. By Lemma 2,
we can make Step(P0; σ0; d0) = (P1; σ1; d1) such that
– d1 = d0 ∧d′
1 for some d′
1,
– there exists a substitution φ1 such that
• Dom(φ1) = fv(P1) \ fv(P0) (the set of new free variables in P1),
• fv(Ran(φ1)) ∩Dom(τ) = ∅,
• φ1τ is an (R, µ)-unifier of P1 with degree d′
τ ≥µ such that dτ ≤d′
1 ∧d′
τ,
and
• σ1 ≾Dom(φ1τ)
R,µ
φ1τ.
The obtained configuration P1; σ1; d1 and φ1τ satisfy the conditions of Lemma 2.
Hence, we can iterate applications of Step (finitely many times, due to The-
orem 2), obtaining the maximal chain of configurations P1; σ1; d1 ⇝· · · ⇝
Pn; σn; dn. Then
– Pn = ∅, otherwise it would contradict the fact that it has a solution;
– σn ≾Dom(φ1···φnτ)
R,µ
φ1 · · · φnτ;
– dn = d0 ∧d′
1 ∧· · · ∧d′
n, where d0 = 1 and for all 1 ≤i ≤n, d′
i is such that
di = di−1 ∧d′
i.
Hence, we obtained Hops(t, s, R, µ) = (σn, dn), where σn ≾Dom(φ1···φnτ)
R,µ
φ1 · · · φnτ, and there exists d′
τ such that dτ ≤d′
1 ∧· · · ∧d′
n ∧d′
τ = dn ∧d′
τ ≤
dn. Since Dom(φ1 · · · φn) ∩Dom(τ) = ∅and fv(Ran(φ1 · · · φn)) ∩Dom(τ) =
∅, the composition φ1 · · · φnτ can be also represented as the disjoint union of
the set representations of these substitutions: (φ1 · · · φn) ⊎τ. Therefore, from
σn ≾Dom(φ1···φnτ)
R,µ
φ1 · · · φnτ we get σn ≾Dom(τ)
R,µ
τ. We can take σn and dn in
the role of σ and d, respectively, which finishes the proof.
⊓⊔
4
Discussion
From fuzzy to crisp. When µ = 1, we are essentially in the crisp case, and
our algorithm can be seen as a rule-based variant of the higher-order pattern
unification algorithm [24,26]. It is closer to Nipkow’s version [26] as our use of
VarElim introduces a form of configuration transformation strategy. On the other
hand, our approach is more flexible in selecting which equations to transform,
since our rules operate on sets rather than lists. In [26], it was noted that using
sets instead of lists would lead to divergence, but with our rules and control,

--- Page 19 ---

Higher-Order Pattern Unification Modulo Similarity Relations
19
it does not happen. We imitate Nipkow’s requirement to work at the head of
the list, but only when the left-hand side of the selected equation is a flexible
term. Below is an example demonstrating how our algorithm handles problematic
equations {F =? c(G), G =? c(F)} from [26]:
{F ≃?
R,1 c(G), G ≃?
R,1 c(F)}; ε; 1 ⇝LF
Calling VarElim :
{F ≃? c(G)}; ε ⇝VE1
{H ≃? G}; {F 7→c(H)} ⇝VE2
∅; {F 7→c(G), H 7→G}
{G ≃?
R,1 c(c(G))}; {F 7→c(G)}; 1 ⇝Fail
⊥.
Hence, Hops fails, as expected.
It should also be mentioned that our rules allow a rather simple termination
measure that facilitates the direct termination proof (instead of translating the
problem into first-order unification).
T-norms. Note that using the minimum T-norm (in fact, its idempotence prop-
erty) is important for the completeness of the algorithm as well as for com-
puting unifiers with the maximum approximation degree. (This is not specific
to the higher-order case: it holds even in the first-order case.) The condition
(d ∧R(f, g)) > µ in the decomposition rule (which is the rule actually com-
puting degrees) is general and applies to any T-norm. For nonidempotent T-
norms, we should treat unification problems as multisets. However, even under
this modification, the algorithm would be incomplete. To illustrate this, con-
sider a simple similarity relation R(a, b) = 0.5 and the product T-norm defined
as s1 ∧s2 = s1 ∗s2. Let t = f(X, X, X), s = f(a, b, b), and the cut value
µ = 0.3. Then the unification problem t ≃?
R,µ s has a unifier {X 7→b}, because
R(f(b, b, b), f(a, b, b)) = 0.5 > 0.3. However, the (modified) algorithm fails to
compute it:
{{f(X, X, X) ≃?
R,0.3 f(a, b, b)}}; ε; 1 ⇝Dec
{{X ≃?
R,0.3 a, X ≃?
R,0.3 b, X ≃?
R,0.3 b}}; ε; 1 ⇝LF
{{a ≃?
R,0.3 b, a ≃?
R,0.3 b}}; {X 7→a}; 1 ⇝Dec
{{a ≃?
R,0.3 b}}; {X 7→a}; 0.5 ⇝Fail
⊥
The computation stops with failure because the decomposition attempt of a and
b would involve the check 0.5 ∗R(a, b) ≥0.3, which fails since 0.5 ∗R(a, b) =
0.5 ∗0.5 = 0.25 < 0.3.
For a lower cut value, e.g., µ = 0.1, the algorithm would compute a solution
{X 7→a} with degree 0.25, failing to discover that there exists another unifier,
{X 7→b}, with a better degree 0.3.

--- Page 20 ---

20
B. Dundua and T. Kutsia
However, if we consider only linear unification problems (i.e., those where no
free variable occurs more than once), the modified algorithm is complete and
computes a unifier with the highest degree even for nonidempotent T-norms.
It is possible to regain completeness for nonidempotent T-norms for the gen-
eral case by modifying the subprocedure VarElim: In the VE1 rule, allow the
variable F to be replaced not only by the term
λx1, . . . , xn.a(H1(x1, . . . , xn), . . . , Hm(x1, . . . , xn)),
but by any term (non-deterministically)
λx1, . . . , xn.b(H1(x1, . . . , xn), . . . , Hm(x1, . . . , xn))
where b is similar to a (provided that it still keeps the degree computed so far
above the cut value). The computed degree should be also changed accordingly.
Such a modification would lead to multiple (finitely many) most general unifiers,
out of which one would need to keep only those that have the highest unification
degrees. A detailed discussion of this algorithm goes beyond the scope of this
paper, though.
5
Conclusion
We studied unification of higher-order patterns modulo fuzzy similarity relations,
using the minimum T-norm. This problem, like its classical (crisp) counterpart,
is unitary. We developed a rule-based unification algorithm and proved its ter-
mination, soundness, and completeness. The computed most general unifier has
the best approximation degree. Our work extends, on one hand, the well-known
higher-order pattern unification [24, 26] to accommodate fuzzy similarity rela-
tions. On the other hand, it generalizes the weak unification algorithm [31] from
first-order terms to simply-typed lambda terms.
There are some interesting directions for future work, which involve both
practical applications and further theoretical developments:
– Incorporating the unification algorithm developed in this paper into a higher-
order fuzzy logic programming formalism combining the powers of languages
like Lambda-Prolog [25] and FASILL [12]. It can serve as a foundation of a
flexible higher-order knowledge-based system.
– Relaxing similarity relations to adapt to more diverse scenarios. One possi-
bility is, e.g., lifting the transitivity requirement and considering proximity
relations. This can lead to the generalization of block-based [14] or class-
based [19,29] approximate unification algorithms to the higher-order setting.
Another option is defining approximation based on (Lawverean) quantales
like in quantitative algebras and generalizing the results from [6] to a higher-
order case.
Acknowledgement. This work was supported by the Austrian Science Fund
(FWF) project P 35530, and NATO Science for Peace and Security (SPS) Pro-
gramme G6133.

--- Page 21 ---

Higher-Order Pattern Unification Modulo Similarity Relations
21
References
1. Aït-Kaci, H., Pasi, G.: Fuzzy lattice operations on first-order terms over signatures
with similar constructors: A constraint-based approach. Fuzzy Sets Syst. 391, 1–46
(2020). https://doi.org/10.1016/J.FSS.2019.03.019
2. Barendregt, H., Manzonetto, G.: A Lambda Calculus Satellite. College Publica-
tions (2022)
3. Dershowitz, N., Manna, Z.: Proving termination with multiset orderings. Commun.
ACM 22(8), 465–476 (1979). https://doi.org/10.1145/359138.359142
4. Dowek, G.: Higher-order unification and matching. In: Robinson, J.A., Voronkov,
A. (eds.) Handbook of Automated Reasoning (in 2 volumes), pp. 1009–1062. Else-
vier and MIT Press (2001). https://doi.org/10.1016/B978-044450813-3/50018-7
5. Dundua, B., Kutsia, T., Marin, M., Pau, C.: Constraint solving over multi-
ple similarity relations. In: Ariola, Z.M. (ed.) 5th International Conference on
Formal Structures for Computation and Deduction, FSCD 2020, June 29-July
6, 2020, Paris, France (Virtual Conference). LIPIcs, vol. 167, pp. 30:1–30:19.
Schloss Dagstuhl - Leibniz-Zentrum für Informatik (2020). https://doi.org/10.
4230/LIPICS.FSCD.2020.30
6. Ehling, G., Kutsia, T.: Solving quantitative equations. In: Benzmüller, C., Heule,
M.J.H., Schmidt, R.A. (eds.) Automated Reasoning - 12th International Joint
Conference, IJCAR 2024, Nancy, France, July 3-6, 2024, Proceedings, Part II.
Lecture Notes in Computer Science, vol. 14740, pp. 381–400. Springer (2024).
https://doi.org/10.1007/978-3-031-63501-4_20
7. Fontana, F.A., Formato, F.: Likelog: A logic programming language for flexible
data retrieval. In: Bryant, B.R., Lamont, G.B., Haddad, H., Carroll, J.H. (eds.)
Proceedings of the 1999 ACM Symposium on Applied Computing, SAC’99, San
Antonio, Texas, USA, February 28 - March 2, 1999. pp. 260–267. ACM (1999).
https://doi.org/10.1145/298151.298348
8. Fontana, F.A., Formato, F.: A similarity-based resolution rule. Int. J. Intell. Syst.
17(9), 853–872 (2002). https://doi.org/10.1002/int.10067
9. Formato, F., Gerla, G., Sessa, M.I.: Extension of logic programming by similar-
ity. In: Meo, M.C., Vilares Ferro, M. (eds.) 1999 Joint Conference on Declarative
Programming, AGP’99, L’Aquila, Italy, September 6-9, 1999. pp. 397–410 (1999)
10. Formato, F., Gerla, G., Sessa, M.I.: Similarity-based unification. Fundam. Inform.
41(4), 393–414 (2000). https://doi.org/10.3233/FI-2000-41402
11. Guerrero, J.A., Moreno, G., Riaza, J.A., Sanchez, J.: Smart design of similarity
relations for fuzzy logic programming environments. In: IEEE Symposium Series on
Computational Intelligence, SSCI 2018, Bangalore, India, November 18-21, 2018.
pp. 220–227. IEEE (2018). https://doi.org/10.1109/SSCI.2018.8628871
12. Julián Iranzo, P., Moreno, G., Riaza, J.A.: The fuzzy logic programming language
FASILL: design and implementation. Int. J. Approx. Reason. 125, 139–168 (2020).
https://doi.org/10.1016/J.IJAR.2020.06.002
13. Julián Iranzo, P., Moreno, G., Riaza, J.A.: Some properties of substitutions in
the framework of similarity relations. Fuzzy Sets Syst. 465, 108510 (2023). https:
//doi.org/10.1016/J.FSS.2023.03.013
14. Julián-Iranzo, P., Rubio-Manzano, C.: Proximity-based unification theory. Fuzzy
Sets and Systems 262, 21–43 (2015). https://doi.org/10.1016/j.fss.2014.07.006
15. Julián Iranzo, P., Rubio-Manzano, C.: A sound and complete semantics for a
similarity-based logic programming language. Fuzzy Sets and Systems 317, 1–26
(2017). https://doi.org/10.1016/j.fss.2016.12.016

--- Page 22 ---

22
B. Dundua and T. Kutsia
16. Julián Iranzo, P., Sáenz-Pérez, F.: An efficient proximity-based unification al-
gorithm. In: 2018 IEEE International Conference on Fuzzy Systems, FUZZ-
IEEE 2018, Rio de Janeiro, Brazil, July 8-13, 2018. pp. 1–8. IEEE (2018).
https://doi.org/10.1109/FUZZ-IEEE.2018.8491593
17. Julián Iranzo, P., Sáenz-Pérez, F.: Bousi∼Prolog: Design and implementation of a
proximity-based fuzzy logic programming language. Expert Syst. Appl. 213(Part),
118858 (2023). https://doi.org/10.1016/J.ESWA.2022.118858
18. Krajci, S., Lencses, R., Medina, J., Ojeda-Aciego, M., Vojtás, P.: A similarity-
based unification model for flexible querying. In: Andreasen, T., Motro, A., Chris-
tiansen, H., Larsen, H.L. (eds.) Flexible Query Answering Systems, 5th Interna-
tional Conference, FQAS 2002, Copenhagen, Denmark, October 27-29, 2002, Pro-
ceedings. Lecture Notes in Computer Science, vol. 2522, pp. 263–273. Springer
(2002). https://doi.org/10.1007/3-540-36109-X_21
19. Kutsia, T., Pau, C.: Solving proximity constraints. In: Gabbrielli, M. (ed.) Logic-
Based Program Synthesis and Transformation - 29th International Symposium,
LOPSTR 2019, Porto, Portugal, October 8-10, 2019, Revised Selected Papers.
Lecture Notes in Computer Science, vol. 12042, pp. 107–122. Springer (2019).
https://doi.org/10.1007/978-3-030-45260-5_7
20. Loia, V., Senatore, S., Sessa, M.I.: Similarity-based SLD resolution and its role for
web knowledge discovery. Fuzzy Sets Syst. 144(1), 151–171 (2004). https://doi.
org/10.1016/J.FSS.2003.10.018
21. Maruyama, Y.: Higher-order fuzzy logics and their categorical semantics: Higher-
order linear completeness and Baaz translation via substructural tripos theory.
In: 30th IEEE International Conference on Fuzzy Systems, FUZZ-IEEE 2021,
Luxembourg, July 11-14, 2021. pp. 1–6. IEEE (2021). https://doi.org/10.1109/
FUZZ45933.2021.9494453
22. Medina, J., Ojeda-Aciego, M., Vojtás, P.: Similarity-based unification: a multi-
adjoint approach. Fuzzy Sets and Systems 146(1), 43–62 (2004). https://doi.org/
10.1016/j.fss.2003.11.005
23. Milanese, G.C., Pasi, G.: Similarity-based reasoning with order-sorted feature
logic. IEEE Trans. Fuzzy Syst. 32(5), 2797–2810 (2024). https://doi.org/10.1109/
TFUZZ.2024.3362897
24. Miller, D.: A logic programming language with lambda-abstraction, function
variables, and simple unification. J. Log. Comput. 1(4), 497–536 (1991). https:
//doi.org/10.1093/LOGCOM/1.4.497
25. Miller, D., Nadathur, G.: Programming with Higher-Order Logic. Cambridge Uni-
versity Press (2012). https://doi.org/10.1017/CBO9781139021326
26. Nipkow, T.: Functional unification of higher-order patterns. In: Proceedings of the
Eighth Annual Symposium on Logic in Computer Science (LICS ’93), Montreal,
Canada, June 19-23, 1993. pp. 64–74. IEEE Computer Society (1993). https://doi.
org/10.1109/LICS.1993.287599
27. Novák, V.: Elements of model theory in higher-order fuzzy logic. Fuzzy Sets Syst.
205, 101–115 (2012). https://doi.org/10.1016/J.FSS.2012.03.006
28. Pau, C.: Symbolic Techniques for Approximate Reasoning. Ph.D. thesis, Research
Institute for Symbolic Computation, Johannes Kepler University Linz, Austria
(2022)
29. Pau, C., Kutsia, T.: Proximity-based unification and matching for fully fuzzy sig-
natures. In: 30th IEEE International Conference on Fuzzy Systems, FUZZ-IEEE
2021, Luxembourg, July 11-14, 2021. pp. 1–6. IEEE (2021). https://doi.org/10.
1109/FUZZ45933.2021.9494438

--- Page 23 ---

Higher-Order Pattern Unification Modulo Similarity Relations
23
30. Sandri, S.A., Mendonça, J., Martins-Bedé, F.T., Guimarães, R., Carvalho, O.S.:
Weighted fuzzy similarity relations in case-based reasoning: A case study in clas-
sification. In: FUZZ-IEEE 2012, IEEE International Conference on Fuzzy Sys-
tems, Brisbane, Australia, June 10-15, 2012, Proceedings. pp. 1–7. IEEE (2012).
https://doi.org/10.1109/FUZZ-IEEE.2012.6251149
31. Sessa,
M.I.:
Approximate
reasoning
by
similarity-based
SLD
resolution.
Theor. Comput. Sci. 275(1-2), 389–426 (2002). https://doi.org/10.1016/S0304-
3975(01)00188-8
32. Virtanen, H.: Vague domains, S-unification, logic programming. Electr. Notes
Theor.
Comput.
Sci.
66(5),
86–103
(2002).
https://doi.org/10.1016/S1571-
0661(04)80516-4
33. Vojtás, P.: Declarative and procedural semantics of fuzzy similarity based unifi-
cation. Kybernetika 36(6), 707–720 (2000), http://www.kybernetika.cz/content/
2000/6/707

```
