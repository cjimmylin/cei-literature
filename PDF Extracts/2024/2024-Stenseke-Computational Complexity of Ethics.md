---
title: "Computational Complexity of Ethics - PDF Extract"
source_pdf: "2024-Stenseke-Computational Complexity of Ethics.pdf"
pages: 102
extracted_at: "2026-01-25T05:00:18.795462"
---

# PDF Extract: Computational Complexity of Ethics

**Source PDF:** 2024-Stenseke-Computational Complexity of Ethics.pdf
**Total Pages:** 102

---

## Content

```
--- Page 1 ---

On the Computational Complexity of Ethics: Moral Tractability for
Minds and Machines
Jakob Stensekea,b
aDepartment of Philosophy, Lund University, Helgonavagen 3, Lund 221 00, Sweden
bjakob.stenseke@ﬁl.lu.se, 0000-0001-8579-3975
Abstract
Why should moral philosophers, moral psychologists, and machine ethicists care about
computational complexity? Debates on whether artiﬁcial intelligence (AI) can or should be
used to solve problems in ethical domains have mainly been driven by what AI can or cannot
do in terms of human capacities. In this paper, we tackle the problem from the other end by
exploring what kind of moral machines are possible based on what computational systems
can or cannot do. To do so, we analyze normative ethics through the lens of computational
complexity. First, we introduce computational complexity for the uninitiated reader and
discuss how the complexity of ethical problems can be framed within Marr’s three levels of
analysis. We then study a range of ethical problems based on consequentialism, deontology,
and virtue ethics, with the aim of elucidating the complexity associated with the problems
themselves (e.g., due to combinatorics, uncertainty, strategic dynamics), the computational
methods employed (e.g., probability, logic, learning), and the available resources (e.g., time,
knowledge, learning). The results indicate that most problems the normative frameworks
pose lead to tractability issues in every category analyzed. Our investigation also provides
several insights about the computational nature of normative ethics, including the diﬀerences
between rule- and outcome-based moral strategies, and the implementation-variance with
regard to moral resources. We then discuss the consequences complexity results have for
the prospect of moral machines in virtue of the trade-oﬀbetween optimality and eﬃciency.
Finally, we elucidate how computational complexity can be used to inform both philosophical
and cognitive-psychological research on human morality by advancing the Moral Tractability
Thesis (MTT).
Keywords:
computational complexity, machine ethics, artiﬁcial moral agents,
consequentialism, deontology, virtue ethics
Contents
1
Introduction
2
2
The Complexity of Making a Salad
4
3
Computational Complexity of Ethics
8
3.1
The Complexity of Ethics Following Marr’s Three-Level Analysis . . . . . . .
10
3.1.1
Level 1: Computational Problem
. . . . . . . . . . . . . . . . . . . .
10
Preprint submitted to arXiv
February 9, 2023
arXiv:2302.04218v1  [cs.CC]  8 Feb 2023

--- Page 2 ---

3.1.2
Level 2: Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
3.1.3
Level 3: Implementation . . . . . . . . . . . . . . . . . . . . . . . . .
15
4
Consequentialism and Causal Engines
17
4.1
The Combinatorics of Outcomes . . . . . . . . . . . . . . . . . . . . . . . . .
18
4.2
Causal Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
4.3
Decisions in Dynamic and Partially Observable Environments
. . . . . . . .
25
5
Deontology and Rule-Followers
30
5.1
The Generality of Rules
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
5.1.1
Human Rule-Following in Legal and Liberal Contexts . . . . . . . . .
33
5.1.2
General-Purpose Rules and their Justiﬁcation . . . . . . . . . . . . .
34
5.1.3
Moral Behavior in Strategic Games . . . . . . . . . . . . . . . . . . .
36
5.1.4
Moral Behavior in Strategic Games with Incomplete Information . . .
39
5.1.5
Computing Moral Equilibria . . . . . . . . . . . . . . . . . . . . . . .
41
5.1.6
Designing Moral Systems . . . . . . . . . . . . . . . . . . . . . . . . .
45
5.2
The Complexity of Moral Logic and Semantics . . . . . . . . . . . . . . . . .
46
5.2.1
Decidability and Descriptive Complexity . . . . . . . . . . . . . . . .
47
5.2.2
The Complexity of Modal and Deontic Logic . . . . . . . . . . . . . .
49
5.2.3
The Problem of Moral Semantics
. . . . . . . . . . . . . . . . . . . .
52
5.3
Consequentialist-Deontological Hybrids . . . . . . . . . . . . . . . . . . . . .
58
6
Virtue Ethics and Moral Machine Learning
61
6.1
The Complexity of Learning . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
6.1.1
Weak and Strong Sample Complexity . . . . . . . . . . . . . . . . . .
64
6.1.2
Machine Learning Theory vs Practice . . . . . . . . . . . . . . . . . .
68
7
Moral Tractability for Minds and Machines
69
7.1
Consequences for the Prospects of Moral Machines
. . . . . . . . . . . . . .
69
7.2
Consequences for Human Morality . . . . . . . . . . . . . . . . . . . . . . . .
71
7.3
Moral Tractability Thesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
72
7.4
Limitations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
7.5
Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
8
Conclusion
77
1. Introduction
Computational systems of hardware and software continue to enter and transform a
growing number of human domains. As autonomous vehicles, virtual teachers, and carebots
augment or even take over traditional human roles of drivers, educators, and caretakers, it
becomes hard to ignore the need for systems that align with the norms and moral standards
associated by such roles.1 These concerns have spawned the interdisciplinary ﬁeld of machine
1Unless speciﬁed, terms such as “AI system”, “machine”, and “computer” will be used interchangeably to
denote computational systems of hardware and software.
2

--- Page 3 ---

ethics, which broadly explores the prospects of implementing ethics into machines (Wallach
and Allen, 2008; Anderson and Anderson, 2011). Lying in the intersection of computer science
and moral philosophy, machine ethics encompasses a spectrum of more or less interconnected
research aims, including work that addresses the challenges of value alignment (Gabriel,
2020), explainability (Gunning et al., 2019), and safety (Amodei et al., 2016) of existing AI
methods, the development of systems tackling various ethical dilemmas (Cervantes et al.,
2020; Tolmeijer et al., 2020), and theoretical debates on whether and to what extent artiﬁcial
moral agents are feasible or desirable (Floridi and Sanders, 2004; Behdadi and Munthe, 2020).
The feasibility debate has, in turn, mainly been driven by what AI systems can or cannot
do in terms of human capacities; whether artiﬁcial agents could be autonomous or have free
will (Hellstr¨om, 2013), be equipped with human-like rationality (Purves et al., 2015), or
capable of conscious experience (Himma, 2009). However, by centering on capacities that
remain elusive and conceptually opaque from a computational perspective, debates on artiﬁcial
morality fails to engage with the technical dimensions of AI, and as a result, they become
practically otiose for the design and development of ethical machines (Mabaso, 2021; Behdadi
and Munthe, 2020; Stenseke, 2022b). Another issue that obscures the feasibility of moral
machines is the absence of systemic evaluation tools (Tolmeijer et al., 2020). In machine
ethics, there are at present no domain-speciﬁc nor general benchmarks that can be used to
evaluate the performance of diﬀerent ethical systems. Consequentially, since evaluations of
systems are limited to the experimental conditions of their particular implementation, the
scalability of solutions and generalizability of results are severely restricted.
In this paper, we address these issues by exploring what kind of moral machines are
possible based on the ethical problems computational systems can or cannot solve eﬀectively.
To do so, we analyze normative ethics through the lens of computational complexity theory,
which classiﬁes problems in terms of the resources (e.g., time and space) a computer requires to
solve them. While previous work have discussed computational limitations for moral machines
more informally (Brundage, 2014; Stenseke and Balkenius, 2022), and provided embryonic
complexity analyses of ethical actions (Reynolds, 2005) and plans (Lindner et al., 2020), the
computational complexity of ethics and its potential relevance for machine ethics remains
largely unexplored. For instance, if artiﬁcial systems were to operate in ethical domains where
time is of the essence (e.g., a self-driving ambulance), it is crucial that such systems can make
eﬃcient as well as competent ethical decisions. Furthermore, if human moral cognition is
constrained by tractability (Van Rooij, 2008), the analysis might also serve moral psychology
and normative theory by constraining the space of problems an agent following a certain
normative theory can be reasonably expected to solve.
In the rest of the paper, concepts and theories from both moral philosophy and computer
science are introduced and explained in a way that is friendly for readers with a limited
background in one or both areas. It is structured as follows. First, we give an introduction to
computational complexity and tractability with the aim of explaining their relevance for the
uninitiated reader (section 2). In section 3, we survey previous implementations in machine
ethics and discuss various interpretations of the complexity of ethics using Marr’s three
levels of analysis (3.1), which motivates the analysis of problems posed by normative theory
(computational level, 3.1.1) that are solved through a variety of computational methods
(algorithmic level, 3.1.2) by a deterministic Turing Machine (implementation level, 3.1.3).
We then explore the complexity of various ethical problems based on consequentialism (4),
3

--- Page 4 ---

deontology (5), and virtue ethics (6). The main aim is to elucidate the complexity associated
with the problems themselves (e.g., due to uncertainty, combinatorics, strategic dynamics,
and generality), the available resources (e.g., time, cognition, and domain knowledge), and
the computational methods employed to tackle the problems (e.g., probability, logic, and
learning). The results indicate that most problems the normative theories pose lead to
intractability issues (a succinct summary is given in 3), and especially if the prescriptive ideal
should be optimally satisﬁed. In particular, based on the intractability (and undecidability)
stemming from combinatorics of action plans (4.1), probabilistic causal inference (4.2),
dynamic and partially observable environments (4.3), general rules (5.1), strategic dynamics
(5.1.3), logic (5.2), semantics (5.2.3) and learning (6.1), we ﬁrmly conclude that perfect
moral machines are impossible. Our investigation also provides additional insights regarding
the computational nature of the normative theories, including (i) the diﬀerences between
action- and outcome-based strategies, (ii) the beneﬁts of moral hybrids (5.3), and (iii) the
extreme implementation-variance with regard to moral resources. In section 7, we discuss the
consequences the results have for the prospects of moral machines by focusing on the trade-oﬀ
between optimality and eﬃciency, the equivocal role of normative theory, and the intimate
relationship between diﬀerent moral resources. Finally, we demonstrate how computational
tractability can be used to inform both philosophical and psychological research on human
morality by advancing the Moral Tractability Thesis.
2. The Complexity of Making a Salad
Let us begin with an illustrative example.2 There is a high chance that you have stumbled
upon a salad bar where you can choose ingredients to your own liking.3 The question is, what
ingredients do you pick in order to create the best tasting salad? Let us assume that you can
immediately assess the tastiness of each ingredient in isolation and give them a “taste value”
(v) on a scale ranging from the most oﬀ-putting (−10) to the most delicious (+10). With
these values, you ﬁnd that one eﬃcient way of putting together a decent salad is to exclusively
pick ingredients (I) with a positive v (v(I) > 0), or a v that is higher than a certain threshold
(e.g., v(I) > 5). Let us name this strategy Ψ. In fact, as a queue is lining up behind the
salad bar, you appreciate the speed Ψ allows you to make a salad: you only have to visit
each ingredient once and check whether they are suﬃciently tasty to be included in your mix.
Furthermore, you realize that the performance of Ψ grows, in the worst-case, linearly with the
number of salad ingredients. This means that, regardless of how many ingredients there could
be, Ψ will always be eﬃcient: for any input — in this case, n number of ingredients — the
time it takes to make a salad will closely mirror the size of the input (i.e., 1000 ingredients
equals 1000 visits to distinct ingredients).
But upon further reﬂection, you realize that something is odd with Ψ. It asks you to
put sun-dried tomatoes on top of pineapple. You imagine how the saltiness of sun-dried
tomatoes mixes with the sweet-sourness of pineapple as they traverse the taste buds of your
tongue. Your immediate disgust of the image reveals a fatal ﬂaw of Ψ: even if these two
2The reader who is already familiar with computational complexity is advised to skip to section 3.
3The example is inspired by the excellent introduction to complexity analysis given in Van Rooij et al.
(2019).
4

--- Page 5 ---

ingredients were given some of the highest taste values (v > 9), their combination yields a
taste value that is terribly oﬀ-putting (v = −10). You realize that Ψ violates a fundamental
principle of gastronomy, namely, that combinations of ingredients yield taste values that do
not necessarily correspond with the tastiness of its individual ingredients. We can call this
principle the Combinatorial Principle of Gastronomy (CPG).
Luckily, you have a perfect gustatory imagination and can immediately assess the taste
value of any given combination of ingredients. How do you ﬁnd the optimal combination
of ingredients in a way that maximizes taste value and adheres to CPG? We can formally
describe this as the following computational problem:
Optimal salad following CPG
Input: A salad bar as a set SB = {I1, I2, ..., In} of n ingredients and a value
function v that assigns a taste value to every subset (or salad) S ⊆SB.
Output: A salad S ⊆SB such that v(S) is maximized over all possible salads in
the salad bar (S ⊆SB).
You realize that there is a straight-forward strategy, you call it Φ, that is guaranteed
to produce an optimal salad while satisfying CPG: simply imagine the taste value of each
possible subset S ⊆SB and pick the salad with the highest v(S). But you have a feeling
that there must be a catch with Φ. You do some basic combinatorics: if there was only one
ingredient, e.g., {cucumber}, there would be one possible salad (made entirely of cucumber);
two ingredients yield three distinct salads, e.g., {cucumber}, {onion}, {cucumber, onion};
three ingredients make seven; four make ﬁfteen; etc. You determine that the number of
possible salads grows exponentially with the number of ingredients, so that n ingredients
produce 2n −1 possible salads. The salad bar you are currently facing has 30 ingredients,
which presents 230 −1 = 1, 073, 741, 823 distinct salads. Since your otherwise extraordinary
gustatory system can only assess the taste of one salad per second, Φ asks you to imagine
salads for roughly 34 years, that is, if you were to optimally satisfy the combinatorial principle
of gastronomy. Unfortunately, you have already wasted more than enough time, and the
people in the queue behind you are very upset.
The example serves to draw ﬁve important lessons about computational complexity:
(1) The ﬁrst is that many decision problems that we encounter in everyday life can be
formulated in similar ways, from planning an itinerary, packing a bag for a trip, or inviting a
selection of friends to a birthday party in your small apartment. And as we will see throughout
this paper, ethical problems are no exception. You might wonder why it matters so much to
ﬁnd the optimal salad; at worst, you end up with a poor-tasting salad, which is far from a
disastrous consequence. But would you be so quick to disregard optimal results if the problem
was a matter of life and death? And even if you do not care much about the combinatorial
principle of gastronomy, there might be moral principles that are fundamental to your ethical
life.
(2) The second lesson is that the complexity of a problem can be expressed in terms of
the resources an agent or algorithm requires to solve it. For computational systems, the
two most interesting resources are time and space. The latter conventionally denotes the
size of computer memory (e.g., bits), whereas the former refers to the number of machine
5

--- Page 6 ---

operations (or synonymously used terms such as “computations”, “calculations”, “steps”, or
“state transitions”). Why measure time in terms of machine operations and not in seconds or
minutes? The reason is that, while the real-time speed of computers solving a problem by
running some algorithm A can vary greatly, the amount of machine operations they need to
execute A remain unchanged. A 21st century computer and one from the 1960’s both have
to consider 2n −1 salads if they were to produce the best tasting salad following Φ, even if
the modern computer could potentially do so a million times faster. Importantly, this forms
the basis of the Invariance Thesis,4 which allows us to analyze and compare the worst-case
complexity that is inherent to computational problems independent of speciﬁc machines.
(3) This leads to the third lesson, which is the simple observation that some problems are
more complex than others. If a problem is undecidable, it means that it can be proven that
no algorithm can be constructed to solve the problem.5 Among the decidable problems, the
most important distinction is between problems that are tractable and intractable. Crudely
put, a problem is tractable if it can be solved using a ‘realistic’ amount of resources. For most
computational theorists, however, tractable is synonymous with “computable in polynomial
time”. This means that the runtime (number of machine operations) of an algorithm is
upperbounded by a polynomial expression in its input, i.e., of the type nc (where c is some
positive constant). This includes functions that show logarithmic (log n), linear (n), quadratic
(n2), or cubic (n3) growth in time as the input n increases. The class of decision problems that
can be solved in polynomial time by a deterministic Turing machine is called P, capturing the
notion of decision problems with “eﬀective” decision procedures (Cobham, 1965). Conversely,
problems that cannot be solved in polynomial time are called intractable as their runtime
grows exponentially (cn), by a factorial (n!), or super-exponentially (nn). This notion of
tractability is illustrated in the diﬀerence between decision procedure Ψ and Φ. For Ψ,
salad-making time will never grow more than linearly in relation to the number of ingredients.
Using Big O notation, which expresses an asymptomtotic upperbound6 of a function (in
this case, a mapping between input size n and time), the time complexity of Ψ is O(n). By
contrast, performing an exhaustive search over all possible salads of the salad bar leads Φ
to the exponential O(2n). Even if your gustatory imagination could utilize the speed of the
parallelized neural computation of your brain, which allowed you to imagine one billion salads
per second, a salad bar of 50 ingredients would still take you 13 days to master, and a bar of
60 takes you roughly 37 billion years. Of course, no sane person would spend that much time
imagining the taste of diﬀerent salads. But the problem with problems remains: if we want
4More formally, the thesis states that given two machines M1 and M2, and a given computational problem
Θ, the complexity of Θ executed by M1 and M2 will diﬀer at most by a polynomial amount. That is, if M1 is
able to compute Θ in time t, M2 can compute Θ in tc, where c is a constant. The thesis is widely accepted
among computer scientists provided that M1 and M2 are any type of Turing machine or any other reasonable
model of computation (e.g., cellular automata, neural networks) and the input is reasonably encoded (e.g., it
does not involve irrelevant information). See Garey and Johnson (1979).
5The halting problem is an example of an undecidable problem: in 1936, Alan Turing proved that there is
no algorithm that can determine whether an arbitrary program eventually halts. Decidability will be further
addressed in section 5.2.1.
6“asymptotic” means that we can ignore lower order polynomials and constants when we describe a
function. For instance, the function f(n) = 4n + n3 is written as O(n3), since 4n becomes insigniﬁcant
compared to n3 as n increases.
6

--- Page 7 ---

to solve them eﬀectively, we might need to give up our requirement of optimality. Instead of
“best imaginable”, we need compromises that are “good enough” given the available resources.
As such, intractable problems can present an uncomfortable trade-oﬀbetween ideal and
feasible. And it is precisely how this uncomfortable trade-oﬀaﬀects ethical decisions for
computational agents that will be the topic of this paper.
Part of the reason why there is no eﬀective way to make an optimal salad following CPG is
captured in the widely believed conjecture P ̸= NP. It states that decision problems that have
solutions which can be checked (or veriﬁed) eﬀectively cannot necessarily be solved eﬀectively.
To be more precise, it states that the complexity class P does not equal NP: the class of
decision problems solvable in polynomial time by a non-deterministic TM, or equivalently,
decision problems where solutions can be veriﬁed in polynomial time. Φ exempliﬁes such
a case. Even if you can check the taste of any combination of salad ingredients quickly
(polynomial time), there is no deterministic procedure that allows you to ﬁnd the optimal;
you still have to check the entire space of combinations to ensure that you have the optimal
subset. In fact, ﬁnding the optimal salad following CPG is NP-hard, which means that it
is at least as hard as the hardest problem in NP. More formally, a problem X is NP-hard
when every problem in NP can be reduced in polynomial time to X. This means that if we
assume that a solution for X takes one unit of time, the solution can be used to solve every
problem in NP in polynomial time. A closely related property is the notion of completeness.
An NP-complete problem is both NP-hard and belongs to NP. Note that, while P and NP are
classes of decision problems — which can be framed as a yes/no-type question — NP-hard
problems are not restricted to decision problems as such; they are simply at least as hard as
the hardest decision versions of the same problem. For instance, while decision variants of
NP-hard problems might be NP-complete — e.g., the Boolean satisﬁability problem (SAT) or
subset sum problem (SSP) — other variants of the same problem, e.g., framed as optimization
or search problems, are not (they are not decision problems). Again, this is illustrated in our
example: salad making following CPG is NP-hard since it is an optimization version of the
subset sum problem (SSP), which is NP-complete.
Furthermore, note also that, while NP-hardness only denotes a general lower bound, it does
not say anything about an upper bound, which might be more informative for understanding
exactly how hard a problem is.7 In computational complexity theory, classes of computational
problems are instead deﬁned by the upper bound (or constraints) on the amount of resources
they require in the worst-case (formalized using Big O notation). In turn, this allows us to
describe general hierarchies of how complex problems are. For instance, problems solvable in
polynomial time by a deterministic TM are also solvable by a non-deterministic TM, which
implies that P is a subset (⊆) of NP. Similarly, it is widely believed that P ⊆NP ⊆PSPACE
⊆EXPTIME ⊆EXPSPACE (see Appendix (8) for a summary of the complexity classes
used in this article). The worst-case analysis can be motivated by the fact that an algorithm
needs to consider all possible inputs of a problem, which includes the worst-case input. But
in the analysis of algorithms, there are several other essential tools to study complexity. For
instance, if the lower and upper bound coincide, we have a tight bound. Again, there is such
7For instance, the halting problem is NP-hard but undecidable (it is not decidable in a ﬁnite amount of
operations); the true quantiﬁed Boolean formula language (QBF) is NP-hard but decidable in polynomial
space (PSPACE-complete) (Garey and Johnson, 1979).
7

--- Page 8 ---

a tight bound on the time complexity of making an optimal salad following Φ: we have to
imagine the taste of at least and at most 2n −1 salads to ensure optimality. Alternatively,
we could imagine that salad bars were arranged in ways that allowed for exploitation, e.g.,
sorted in rows of pre-made combinations. If so, we could measure the time complexity of an
algorithm in terms of how many operations it required to make a salad over a number of
diﬀerent salad bars (inputs), and see how it performed in the best-case, average-case, and
worst-case.8 In short, computational complexity provides a smorgasbord of analytical tools to
understand the diﬃculty of problems and their algorithmic solutions.
(4) The fourth lesson, and a corollary of the third, is that the way an agent solves a problem
ultimately depends on its resources, broadly construed. Besides time and memory-size, these
resources include heuristics (eﬃcient strategies), cognition (capacities for perceiving and
acting in the world),9, knowledge, and learning. In reality, you might mix aspects of Ψ and Φ.
You might select a few key ingredients as a basis that you already know yields a reasonably
tasty salad, and imagine whether this basis could beneﬁt from further additions. Drawing
from your vast experience of cooking — combining previous trial-and-error, general rules of
thumb, and educated guess-work — you are able to quickly put together an almost perfect
salad while still adhering to the CPG (albeit not optimally). In fact, your stomach might
already know what kind of salad it craves before you even see what the bar oﬀers; you only
have to pick up the ingredients. In such cases, a low input-size (e.g., 10 ingredients) could be
a curse rather than a blessing, since you ﬁnd that a critical ingredient is missing. The main
point is that, although problems might be intractable regarding some speciﬁc resource (e.g.,
time), or due to the choice of strategy (e.g., Φ), it is hard to tell in a given situation whether
an eﬀective solution could be obtained via other means (e.g., using some diﬀerent strategy or
given more of a certain resource). Importantly, this leads to a distinction between the problem
itself (e.g., put together a tasty salad), and how the problem is solved (e.g., follow Φ). And
while the distinction between problem and solution might be relatively clear in computational
contexts (e.g., between problem and algorithmic solution), we will dedicate much eﬀort in
this paper to elucidate their diﬀerence in moral contexts.
3. Computational Complexity of Ethics
What is the computational complexity of ethics? First, we should note that “ethics” is a
multifaceted and equivocal concept that permeates many levels of analysis across diﬀerent
disciplines. Throughout the ages, moral philosophers have in more or less systematic ways
tried to resolve questions regarding what is morally “good” and “bad”. In modern times,
Anglophone analytical ethics is conventionally divided into (i) applied ethics (determining
what is “good” and “bad” in particular instances), (ii) normative ethics (advancing standards
and principles of what is “good” and “bad”), and (iii) meta-ethics (determining the meaning
8However, note that such performance measures would not work for ﬁnding the optimal salad following Φ,
since it does not matter in which way the ingredients are arranged.
9Throughout this paper, the term “cognition” will be broadly used to denote all sorts of information-
processing that enables capacities such as perception, action, reasoning, and learning. As such, it diﬀers
from cognitivism in meta-ethics (the view that moral language can express propositions that can be true or
false) and conceptions of cognition that emphasize prefrontal activity (e.g., thinking, memory, judgement) in
contrast to ’back of the brain’ sensory processing (Block, 2019).
8

--- Page 9 ---

and nature of morality). But the landscape of ethics stretches far beyond these divisions.
From a biological point of view, it includes the evolutionary foundations of cooperation (as
extensively studied in game theory (Axelrod and Hamilton, 1981; Nowak, 2006)), where
morality can be viewed as an adaptive solution to the problem of competition among self-
interested organisms,10 from individual cells (Hummert et al., 2014) to human beings (Leben,
2018). The landscape gets further complicated if we also consider the social, psychological, and
cognitive dimensions, e.g., how ethical behavior is intertwined with the empathy, emotions,
and reasoning of embodied agents, and carried out by highly distributed and parallel cognitive
systems (Newen et al., 2018; FeldmanHall and Mobbs, 2015). Far from being ‘ﬁxed’, moral
behavior is something which is developed and actively reﬁned through experience.11 Beyond
individuals, ethics is also manifested at the level of societies and culture; maintained and
transformed through practices and institutions, mediated through the language of ideology
and religion, and with justiﬁcations that ranges from divine authority (e.g., word of God),
maintaining political order (Hobbes, 1651), to the promotion of liberty (Mill, 1859) or justice
(Rawls, 1971).
Hence, to delimit our investigation, we will focus on the complexity of ethical problems as
they have been framed within the ﬁeld of machine ethics. The majority of technical work
in machine ethics has been focusing on normative ethics, or more speciﬁcally, how certain
tenets or aspects of a normative theory can be implemented so that an artiﬁcial agent acts in
accordance with the theory (Cervantes et al., 2020; Tolmeijer et al., 2020). As such, it can
be viewed as a form of applied normative ethics, since it primarily centers on the practical
implementation of a certain theory as opposed to discussions about what theory that should
be. In their exhaustive survey of implementations, Tolmeijer et al. (2020) has suggested that
approaches to moral machines can be characterized along three broad dimensions: ethical
theory, implementation, and technology. The ﬁrst dimension denotes the ethical theory used,
which includes normative frameworks such as deontology (Anderson and Anderson, 2008;
Malle et al., 2017a; Shim et al., 2017), consequentialism (Abel et al., 2016; Armstrong, 2015;
Cloos, 2005), virtue ethics (Stenseke, 2021; Govindarajulu et al., 2019; Howard and Muntean,
2017), and hybrids (Dehghani et al., 2008b; Thornton et al., 2016). The second dimension,
following a division proposed by Allen et al. (2005), considers how ethics is implemented
in the system, e.g., whether it is through a ‘bottom-up’ learning process, carried out via
‘top-down’ principles, or in a combination of both top-down and bottom-up processing. The
technical dimension, in turn, considers the computational techniques used to realize the
implementation, which include methods from various AI paradigms such as logical reasoning
(e.g., inductive, deductive, and abductive logic), machine learning (e.g., neural networks,
reinforcement learning, evolutionary computing), and probability (e.g., Bayesian and Markov
models).
10Or alternatively put, the function of morality is to alleviate the failures of rationality (Ullmann-Margalit,
2015).
11From the pioneering work of Kohlberg and Hersh (1977), through reﬁnements by Rest et al. (1999), moral
psychology has grown into a mature paradigm that investigates the link between morality and cognitive
development.
9

--- Page 10 ---

3.1. The Complexity of Ethics Following Marr’s Three-Level Analysis
Based on these considerations, how can we frame the computational complexity of ethics
for machines?
Recalling the ﬁnal lesson in the previous section, we ﬁrst need to ﬁnd
some way of distinguishing problems as such from how these problems are solved. This
distinction is reﬂected in the inﬂuential scheme proposed by Marr (1981). Marr suggested
that the information processing of a cognitive system can be explained on three distinct
yet complementary levels of analysis: (i) Computational level, (ii) Algorithmic level, and
(iii) Implementation level. The computational level describes the problem itself (e.g., an
input-output mapping), the algorithmic level speciﬁes the algorithmic process (e.g., strategy
or heuristic) that is performed to tackle the problem, and the implementation level speciﬁes
how the algorithmic process is realized by the physical hardware of the system (e.g., neurons
or circuits). These levels can be illustrated using the salad bar example: (i) the computational
level speciﬁes the number of ingredients, value functions (e.g., tastiness of individual ingredients
or combinations of ingredients), and desired output (maximally tasty salad); (ii) the algorithmic
level describes the problem-solving process (such as Φ); (iii) the implementation level describes
the way a brain or machine implements the problem-solving process physically. Each of
these levels of a system can be analyzed independently. For instance, since one and the
same computational problem can be solved by a range of diﬀerent algorithmic procedures, we
can describe a cognitive system at the computational level independently of the algorithmic
level, and thus have a computational-level theory of the computational system. Likewise,
since an algorithm can be physically realized in a range of diﬀerent systems — e.g., silicon
or carbon — we might have an algorithmic-level theory of a cognitive system that does not
require us to explain how it is physically implemented. Nevertheless, Marr argued that it
is easier to elucidate the workings of a cognitive system through the top-down lens, i.e., by
starting from the problem it solves as opposed to the precise mechanisms it uses to solve it
(Marr, 1977, 1981).12 The reason is that higher-level explanations make commitments about
the lower-levels, which in turn forms a hierarchy of underdetermination. For instance, if we
conjecture that a cognitive system solves problem P at the computational level, we might
be uncertain or agnostic with regards to the speciﬁc algorithm it employs to compute P.
However, if our conjecture should carry any explanatory value beyond the computational
level, we must commit to the idea that at least some algorithm can compute P. If it can
be proven that no such algorithm exists, then our problem is undecidable. Similarly, if we
believe that a system solves P using algorithm A, we commit to the idea that some physical
system can realize A.
3.1.1. Level 1: Computational Problem
How do we ﬁt ethical problems into Marr’s scheme? More precisely, what is the algorithmic
level and what is the computational level of ethical problems posed by normative theory
(NT)? First, we note that normative ethics blurs the line between Marr’s ﬁrst two levels. In
particular, its prescriptive component is intimately linked with its action-guidance, i.e., by
12To clarify, this particular notion of “top-down”, from computation (top), to algorithm, to implementation
(bottom), is distinct from the common use in cognitive psychology, where “bottom-up” processing starts from
the sensory input, and “top-down” processes centers around interpreting the incoming information based on
knowledge, experience, and expectations.
10

--- Page 11 ---

answering what is good (e.g., adherence to moral duties), it tells you how to do good (e.g.,
only perform actions that adhere to moral duties).13 In turn, this opens up a range of possible
interpretations, and we will address three:
(1) NT as algorithmic-level solution to generalized morality — In the most general sense, if
the computational-level problem is phrased as “do what is moral”, we might interpret an NT
as an algorithmic-level solution to the computational problem “how to be moral in general”.
This interpretation would capture the generality ambition of NTs in human contexts (or
at least in philosophical discourse on NT); that an NT should provide general answers or
standards regarding right and wrong that are applicable to a range of particular instances.
An agent that is committed to NT1 would only be moral insofar as it adheres to NT1 in its
general behavior.14 Nevertheless, it is hard to see how one could feasibly frame such a broad
interpretation in the formalism required by a computational complexity analysis; it would
entail some form of general-purpose algorithm — e.g., in terms of a value, principle, or maxim
— that provides solutions to all possible moral dilemmas.15
(2) NT as algorithmic-level solutions to speciﬁc moral problems — A similar but more
narrow interpretation is that NTs provide algorithmic-level strategies that can be used to
solve speciﬁc moral problems. This interpretation seems to, at least prima facie, capture
everyday usage of the term “moral dilemma”, i.e., a decision problem that arises as a conﬂict
between two or more NTs (where “NTs” might as well be replaced with values, duties, virtues,
or norms). We could, for instance, specify the computational-level problem as the trolley
problem in order to draw attention to the conﬂict between action- and outcome-based NTs:
is it morally right to save 5 people even if it involves actions that are intrinsically bad (e.g.,
murder)? Note, however, that the moral complexity (or undecidability) of such a problem does
not reside in the computational-level problem itself, but rather in how the conﬂict between
algorithmic-level solutions should be resolved (e.g., through the doctrine of double eﬀect (Foot,
1967)). Regardless, the interpretation is still consistent with the view that diﬀerent NTs could
be employed to solve diﬀerent problems, depending on the nature of the problem and the
available resources. This seems to resonate with experimental studies that shows that humans
are ﬂexible with regard to the moral strategies they employ in diﬀerent contexts (Capraro
and Rand, 2018; Conway and Gawronski, 2013; Greene et al., 2008). Intuitively, facing some
ethical problem E1, you might be reluctant to perform a certain action because you ﬁnd the
act immoral in itself (according to NT1), while facing some other ethical problem E2, no
action seem immoral in itself, yet some actions lead to outcomes that seem more preferable
than others (according to another theory, NT2). That is, if no conﬂict arises between NT1 and
NT2, you simply pick the one that is best suited for the computational-level problem at hand.
Under this interpretation it would be possible to, at least in principle, assess whether some NT
13Normative theories that put less emphasis on actions might present an interesting exception; for instance,
versions of virtue ethics that emphasize being rather than doing. However, rather than resolving the distinction,
it only pushes it to the blur between ﬂourishing and the character traits that enable an agent to ﬂourish.
Furthermore, the idea that virtue ethics cannot oﬀer action-guidance have also been criticized; see e.g.,
Hursthouse (1999) for a virtue theoretic take on action-guidance.
14Or at least, the agent uses NT1 as its main criterion to evaluate whether an action is moral.
15The Golden Rule or Kant’s categorical imperative (Kant, 1785) might be paradigmatic examples of such
general-purpose algorithms, which we will discuss in section 5.
11

--- Page 12 ---

is more computationally eﬃcient than another with regard to the same computational-level
problem.16 However, could we ask whether it is more successful, morally speaking? It seems
unlikely that an answer can be provided without resolving further meta-theoretical issues.17
Perhaps more problematically, the interpretation seems to posit that ethical problems are, in
some meaningful way, distinctly invariant from the ways they could be solved. To the contrary,
the algorithmic solution (NT) seems to depend on the nature of the computational problem
itself, and how it aﬀords an algorithmic solution via some NT; aﬀordances that are already
embedded at the computational level. If a speciﬁc problem is only decidable or tractable
for a particular NT, it thus seems more fair to treat it as a computational-level problem in
its own right. For instance, we could imagine an ethical problem space which only contains
information about obligations, and no information regarding outcomes; it is thus decidable for
obligation-based NTs while being undecidable for outcome-based NTs. This naturally leads
to an even more narrow interpretation, and the one we will primarily focus on in our analysis:
(3) Speciﬁc moral problems posed by NT as computational-level problems — Instead of
placing NTs at the algorithmic level, we could deﬁne speciﬁc computational-level problems
as they are framed by a speciﬁc NT. In turn, this allows us to be agnostic about the precise
procedure that is carried out at the algorithmic-level: we only have to assume that such
a procedure exists. As such, (3) provides a number of conveniences for machine ethicists,
including (i) answers regarding what is moral, or what is morally good to do (as prescribed
by the modeled theory), (ii) blueprints for action-guidance that can assist algorithmic design
and choice of computational method(s), and (iii) means of evaluating performance (e.g., an
apt deontological agent successfully adheres to moral duties and rules). Importantly, the
narrowness of (3) allows one to ignore theoretical issues that plague (1) and (2): in contrast to
(3), it does not have any generality ambition (and could thus be adopted to speciﬁc contexts or
domains); in contrast to (2), the relevant action-guiding aspects of the modeled NT are already
embedded at the computational-level problem description. I.e., while (3) accommodates the
fact that diﬀerent ethical problems — e.g., the information provided in a certain environment
— give rise to diﬀerent aﬀordances with regard to ethical behavior, (2) does not. Perhaps
most importantly, (3) allows us to analyze the algorithmic level of ethical problems, while (2)
treats the normative theory as the algorithm itself, which potentially obscures the analysis of
how such a procedure is actually carried out.
Another principal strength with (3), with respect to a complexity analysis, is that it
constitutes an essential yet the least complex aspect of ethical computing, in the sense that
both (1) and (2) presuppose that an agent can perform computations of type (3). In other
words, since interpretation (1) is a generalization of (2), which, in turn, depends on speciﬁc
instantiations of (3), they form a hierarchy of ethical computations (illustrated in Figure 1).
That is, to solve the generalized moral problem (interpretation 1) following some normative
16Similarly, even if we believed that only one NT is correct, that does not necessarily mean that we cannot
ﬁnd an alternative theory useful due to its computational eﬃciency (even if we generally dislike the theory
from a moral standpoint).
17For instance, it is plausible that, while a solution provided by NT1 could be the most computationally
eﬃcient, it could also violate some principle from NT2, yet, no eﬃcient solution exists for NT2 (e.g., requires
exponential time). The issue is thus: what is the most successful NT if we assume that the agent believes
that NT2 is morally superior to NT1?
12

--- Page 13 ---

Computation Algorithm
Implementation
Interpretation
What
is
the
problem?
What is the so-
lution?
How is it imple-
mented?
(1) NT as algorith-
mic solution to gen-
eralized morality
Do
what
is
moral (general
behavior)
NTX
(applied
generally)
Mind/machine
(2) NT or NTs as al-
gorithmic solution(s)
to
speciﬁc
moral
problems
Speciﬁc
moral
problem P
NTX
(applied
to P)
Mind/machine
(3) Speciﬁc moral
problem P posed by
speciﬁc NTX
P as framed by
NTX
Computational
methods
Mind/machine
Table 1: Three interpretations on how ethical problems under normative theory can be framed and analyzed
within Marr’s three levels.
theory, e.g., NT1, it requires that an agent can also apply NT1 to speciﬁc moral problems
(interpretation 2); to apply NT1 in the particular (interpretation 2), it requires that an agent
can apply NT1 in the very way it is framed by NT1 (interpretation 3). Thus, if some speciﬁc
(3)-type computation is undecidable, it would follow that it is undecidable for type (1) and (2)
computations of the same problem; it is undecidable for the NT in the speciﬁc case (2) and
thus in the general case (1). The diﬀerence between the interpretations is further illustrated
in Table 1.
3.1.2. Level 2: Algorithm
Thus, we believe that a natural way to analyze the computational complexity of ethics
is to focus on problems posed by normative theory (computational level), that are solved
through a variety of computational methods (algorithmic level), by a deterministic Turing
Machine (implementation level). Of course, this still leaves a rather vast interpretative leeway
regarding what goes on at the algorithmic and implementation level. To ﬁnd the most eﬀective
algorithmic solution to a well-deﬁned problem is often an empirical question, and answers are
continuously revised in light of new advancements in programming techniques (e.g., breaking
down a problem into simpler sub-problems through dynamic programming) or heuristics
(e.g., exploiting regularities in the problem). More importantly, it also depends on what we
accept as a solution. If we believe that the NT strictly dictates that the system should ﬁnd
the optimal solution to a problem, it entails that the algorithmic level should follow some
procedure that is guaranteed to produce an optimal solution; a so-called exact algorithm.18 A
less strict interpretation is to accept solutions that are “close enough” to the optimal; so-called
18For instance, this is analogous to the way Φ produces an optimal (albeit intractable) solution to the salad
problem following the CPG.
13

--- Page 14 ---

Figure 1: Hierarchy of ethical computations. Arrows indicate dependency (i.e., A →B means that solutions to
A depends on solutions to B). The dotted ellipses capture the computational (top) and algorithmic (bottom)
level of the three interpretations (1)-(3).
14

--- Page 15 ---

approximate algorithms. Although approximate algorithms are not guaranteed to ﬁnd an
optimal solution, they guarantee that the solution is within some ﬁxed distance to the optimal
one (i.e., there is a provable bound on the ratio between the optimal and approximated
solution). The diﬀerence between approximate and exact makes all the diﬀerence with regard
to tractability, since many problems that have intractable exact solutions can be approximated
in polynomial time (Williamson and Shmoys, 2011).
We will mainly focus on exact solutions for two interrelated reasons: (i) it is prescribed
by the normative ideal (following the strict interpretation), and (ii) it allows us to focus
on problems as opposed to algorithms. The ﬁrst reason can be supported by the following
consideration: if approximate solutions are acceptable, how can we motivate that a solution is
within an acceptable distance to the optimal? Note that, although an approximation yields a
provable guarantee of the distance, this distance can still be arbitrarily large.19 It seems as if
we then need to also deﬁne what an acceptable distance is, which might vary greatly from case
to case. Furthermore, many real-world problems exhibit no identiﬁable structure that can be
exploited, and as such, they yield no eﬃcient approximation algorithms (Nievergelt et al.,
1995). This naturally leads to the second reason, which is simply that it is easier to compare
exact as opposed to approximate solutions, as we do not need to deﬁne the conditions under
which an approximation is suﬃciently close.
Of course, moral theorists might rightfully point out that we should not be interested in
exact or optimal solutions to moral problems, but rather, we should understand them in terms
of what is “permissible” or “impermissible”. For instance, an action might be permissible
even if it is suboptimal, and morality does not require us to do anything more than what
is permissible, as long as we avoid what is impermissible. This line of reasoning might, in
turn, serve to justify the use of suboptimal approximations. However, this would obscure
the diﬀerence between optimality as a mathematical concept and as a moral concept. Moral
permissibility could, for instance, be construed as the mathematical optimal; i.e., some ﬁxed
point or metric to evaluate behavior against. Alternatively, moral permissibility could be
construed as a mathematical approximation of some ﬁxed notion of moral optimality. But
then, again, we are led back to the same dilemma we wanted to avoid: in each case, we
need to justify how a given approximation is acceptable given a certain threshold of moral
permissibility. It is important to note, though, that this does not exclude the possibility that
such approximations can be justiﬁed in relation to permissibility in particular contexts, but
rather that such an analysis is beyond the scope of this paper.
3.1.3. Level 3: Implementation
On the level of implementation, we will adopt the most widely used model of computation:
the Turing Machine (TM) (Turing, 1936). More speciﬁcally, since a TM is a mathematical
model of computation, it denotes any physical system that can realize a TM (i.e., it is Turing
complete). Turing claimed that every function that can be computed by an algorithm can
be computed by a TM. The thesis gained credence when Turing showed how his notion of
computability was equivalent to the independently suggested proposal by Church (1936).
This forms the basis for the Church-Turing thesis, which in turn has been shown to be
19We can, for instance, imagine a dilemma where the optimal solution has a moral value of 100, but the
best approximation only yields a value of 50.
15

--- Page 16 ---

equivalent to many other forms of computation (Herken, 1995). Simply put, it means that any
general-purpose system (e.g., computer or computer language) can simulate the computational
aspects of any other general-purpose system. We will also assume that P ̸= NP (discussed in
section 2). Like the Church-Turing thesis, it is another widely accepted conjecture among
computer scientists, even if it remains to be proven.20
Importantly, if we can show that a problem is NP-hard, it means that we cannot expect
to ﬁnd an eﬃcient solution to it, where “eﬃcient” means “solvable in polynomial time for a
deterministic TM” (P-tractability).21 Therefore, if ethical problems solved by computational
methods are NP-hard, we cannot expect computational systems to solve them eﬃciently, and
as such, it would yield direct consequences for the feasibility of moral machines. However, even
if P ̸= NP and the Church-Turing thesis have near-universal acceptance, it is crucial to address
a few caveats regarding the limitations and relevance for the notion of P-tractability. For
instance, P-intractability is of no major concern if it is guaranteed that the input size remains
suﬃciently small (e.g., a salad bar with 5 ingredients only yields 32 possible combinations).
Importantly, simply because a problem is P-intractable, it does not mean that it cannot be
solved eﬀectively under other reasonable conceptions of tractability. In fact, many NP-hard
problems can be solved by algorithms whose runtime is superpolynomial in only some part
of its input (input parameter), while the runtime is polynomial in the overall input size.22
Conversely, large constants in polynomial functions, e.g., n100, are P-tractable even if they
might fail to capture any intuitive notion of “eﬀective”. Furthermore, time consumption
might also be signiﬁcantly reduced with alternative models of computation, e.g., utilizing
parallelization, random access memory, or quantum computing. While the Invariance Thesis
— along with the closely related extended Church-Turing thesis (Kaye et al., 2006; Bernstein
and Vazirani, 1997) — states that no machine can be super-polynomially faster than a
deterministic TM,23 it remains to be seen whether and to what extent it can be falsiﬁed in
light of future advancements in computing.24 The main point is that, although P-tractability
constitutes an indispensable tool for the formal study of eﬀective computing in theory and
practice, it should not be interpreted as drawing a deﬁnitive line, across the board, between
what is tractable and what is not. And while P-tractability has direct consequences for moral
machines, a related yet even more convoluted question is whether it could provide any relevant
insight into the moral cognition of humans (a question we will return to in section 7).
20Note that the Church-Turing thesis is not a conjecture in the mathematical sense, but rather a hypothesis
about the nature of computation; it cannot be proven since its notion of eﬀective calculability is deﬁned
informally.
21P ̸= NP entails that we cannot expect to ﬁnd eﬀective solutions to NP-complete problems, and NP-hard
problems which can be translated to NP-complete decision variants. Note that many NP-hard problems would
still remain intractable even if P = NP, e.g., if they are complete for complexity classes that are believed to
encompass NP (e.g., PSPACE or EXPTIME).
22It is this very observation that has motivated the development of parameterized complexity (Downey
and Fellows, 2012), and the class of ﬁxed-parameter tractable problems (FPT). See also Fellows (2002) and
Niedermeier (2006).
23Note that it is generally believed that the Invariance Thesis applies to both parallel and serial models of
computation, see, e.g., Frixione (2001); Parberry et al. (1994); Tsotsos (1990).
24E.g., it is not unlikely that some future computer could at least solve some problems in polynomial time
that are currently intractable.
16

--- Page 17 ---

To divide our problem space, we will focus on three types of moral machines: causal
engines (section 4), rule-followers (section 5), and moral learners (section 6). The main
reason is that nearly all implementations in machine ethics take one of these approaches
(Tolmeijer et al., 2020). Another reason is that these types each correspond to a prominent
normative framework: consequentialism is about predicting future events (causal engines),
deontology is about adhering to rules or duties, and virtue ethics emphasizes learning.25
In order to be subject to a complexity analysis, we will also assume that ethical problems
can be cast as well-deﬁned computational problems, which means that they have clearly
deﬁned initial conditions and goals (e.g., in terms of speciﬁc input and output conditions)
which can be represented through conventional data types (e.g., booleans, integers, ﬂoating
points) and structures (e.g., arrays, lists, graphs, trees). While these simplifying conditions
might do little justice to the vastly rich and potentially ill-deﬁned problems agents might
face in the real world, it can be motivated by the fact that real-world ethical problems,
given that they are decidable at all, are at least as rich in information as their simpliﬁed
computational counterpart. In technical terms, we assume that well-deﬁned computational
problems represent a reasonable lower-bound on the information-theoretic nature of ethical
problems in real-world environments. Finally, we will mainly focus on time rather than space
complexity for the simple reason that accessing and storing memory consumes time, which
means that memory consumption is often upperbounded by time consumption (Garey and
Johnson, 1979).
4. Consequentialism and Causal Engines
Consequentialism is a family of normative theories that puts outcomes at the center of
moral evaluation. While all consequentialists agree on the moral importance of outcomes,
they might disagree on what a good outcome is, or alternatively, what makes an outcome
good. For instance, utilitarianism — arguably the most inﬂuential branch of consequentialist
theories — prescribes actions that maximize utility, where utility can be understood as the
overall well-being of the individuals aﬀected (Bentham, 1789; Mill, 1861), satisfaction of
their preferences (Singer, 2011), reduction of their suﬀering (Smart, 1956), or the well-fare
of their state (Sen, 1979). There are also many nuances regarding the way outcomes are
morally important, e.g., whether intended consequences matter (as opposed to only actual
consequences), whether they depend on the perspective of the acting agent (i.e., agent-relative
as opposed to agent-neutral), whether indirect consequences matter (as opposed to the direct
consequences of the act itself), for whom they matter (e.g., a limited set of individuals or all
sentient beings on earth), and for how long (e.g., only immediate outcomes or for all eternity)
(Sinnott-Armstrong, 2021). Nevertheless, what is common to all forms is the commitment to
the moral value of future events. Therefore, any agent — artiﬁcial or biological — committed
to consequentialism must be able to make predictions about the future, insofar as they are
committed to carrying out the prescriptions of the theory in practice. This is why successful
consequentialist agents rely on so called “causal engines”, a term we use to broadly refer to
the information processing that supports causal cognition.
25Of course, as we will see later on, in many cases the line between these theories and types become blurry.
17

--- Page 18 ---

Note that, in some way or another, most biological organisms care about the consequences
of their actions, as it greatly increases their chance of survival. Intuitively, causal cognition
appears to be critical for many essential capabilities such as avoiding harm, problem-solving,
and planning. Experimental results indicate that human children, as young as eight months,
can make inferences based on cause and eﬀect (Sobel and Kirkham, 2006). This might suggest
that some form of pre-reﬂective capacity for causal inference could be deeply engraved in
our very biological being, reﬂecting the predictive processing that many believe to be the
central function of nervous systems (Friston, 2010; Hohwy, 2013; Keller and Mrsic-Flogel,
2018). However, unlike biological organisms, machines did not develop causal engines through
an evolutionary process. Instead, an artiﬁcial system’s ability to follow consequentialism relies
on computational techniques, often stemming from the families of statistical, Bayesian, and
Markovian modeling (Casella and Berger, 2021). It is also common to view machine learning
methods as a form of “predictive analytics” in the sense that algorithms learn to make better
predictions based on experience; e.g., in supervised learning via human-generated data, in
reinforcement learning through an interactive process of trial-and-error. But consequentialism
is not solely about making predictions about the future. It is also about evaluating, from the
set of possible outcomes, what outcomes are morally preferable over others. That is, even if a
consequentialist agent could predict the outcomes of all possible actions with godlike accuracy
and speed, it does not necessarily mean that it can easily decide, with the same speed, which
the optimal outcome is.
In light of these considerations, this section will explore the computational complexity of
three general types of consequentialist problems: combinatorics of determining the optimal
outcome (4.1), causal inference (4.2), and decisions in dynamic and partially observable
environments under diﬀerent time horizons (4.3). The section is written so as to incrementally
introduce uninitiated readers to time complexity analysis, probability theory (Bayesian
Networks), and stochastic methods (Markov Decision Processes).
4.1. The Combinatorics of Outcomes
In the most simpliﬁed case, we could think of the problem a consequentialist face when they
compare the moral value of diﬀerent outcomes, given that the agent can already determine
what these outcomes are. In this way, we can ignore the complexity of the causal inference
itself so as to isolate the problem of optimal outcome evaluation. In complexity theoretical
terms, we assume that the agent has access to a so-called oracle machine, which is able to
provide answers regarding causal events in a single operation. For instance, if the agent asks
“what happens if I perform action a?”, the oracle gives an answer of the type “action a yields
an outcome with a moral value of v”.26 The most trivial computational problem of this kind
can be formalized in the following way:
C1 — Optimal outcome following consequentialism
Input: An environment as a set E = {a1, a2, ..., an} of n possible actions and a
value function v that assigns an outcome value to each action a ∈E.
26To encompass many versions of utilitarianism, we will remain agnostic about the exact nature of the
utility that ought to be maximized; the only important thing is that it can be represented as a numerical
value.
18

--- Page 19 ---

Output: An action a ∈E such that v(a) is maximized over all possible actions
in E.
An optimal solution can be guaranteed by the following generic exhaustive-search algorithm:
Algorithm 1: Exhaustive search with causal oracle
1 h ←0 // outcome value (0 set as default)
2 j ←0 // index of action (0 set as default)
3 for ai = a1 to an ∈E do
4
hi ←v(ai) // call oracle
5
if hi > h then
6
h ←hi // update highest value
7
j ←i // update index of highest value
8
end if
9 end for
10 return j // return index of action with highest outcome value
In short, the algorithm initializes default values for outcomes (step 1) and the index of
actions (step 2). It then loops through each action in the environment (step 3), calls the
oracle (step 4), checks if the outcome of that action is higher than the current highest (step 5),
and if so, updates the highest outcome value (step 6) and its index (step 7). Finally, it halts
after returning the index of the highest outcome (step 10). If we assume that each instruction
requires an equal amount of time (1) to be executed, we can count the precise number of
machine operations the algorithm needs to solve C1 in the following way: lines 1, 2, and 10
needs to be executed just once (3), lines 3-7 needs to be executed n times each (5n), and 8
and 9 can be ignored (as they are ﬂow control statements), which yields a total of 3 + 5n. In
Big O, this collapses into O(n). In other words, the time complexity grows linearly (O(n)) to
the size of the input. Importantly, regardless of how fast a machine can execute the other
instructions, to ensure optimality, it must ask a number of questions to the oracle which is at
least equal to the number of possible actions. I.e., if there are 10 actions, the agents must
make, at minimum, 10 calls to the oracle.
What happens if we allow for multiple values? For instance, we could assume that the
agent has a set of two or more outcome values that needs to be checked for each action-outcome
(e.g., pleasure, fairness, trust, etc.). This yields the following problem:
C2 — Optimal combination of values
Input: Same as C1 with the addition of a set of outcome value functions V =
{v1, v2, ..., vi} assigned to each a ∈E.
Output: An action a such that v(a) is maximized over all v ∈V and a ∈E.
If we posit that the values interact trivially, in the sense that values can be summarized
v1(a) + v2(a) + ... + vi(a) to yield a single total value V (a) (i.e., obeying the law of additivity),
the optimal action a∗can be formally expressed as:
a∗:= argmax
a∈E
V (a) := {a ∈E :
i
X
m=1
vm(´a) ≤
i
X
m=1
vm(a) for all ´a ∈E}
(1)
19

--- Page 20 ---

If the agent needs to make distinct calls to the oracle for each value, the time complexity is
the product of n (number of actions) and i (number of values), yielding O(ni). If i is equal to
the number of actions, the runtime grows quadratically in relation to n, which still yields the
polynomial O(n2).27
We have so far only been focusing on the moral evaluation of a single action.
But
in ethical decision problems of the real world, it is possible to perform multiple actions.
However, as illustrated in the salad example, the possibility of combining actions can present
tractability issues that are inherent to permutations of combinatorial structures. To show
how this aﬀects the computational complexity of consequentialism,28 we deﬁne an action plan
ϕ = {a1, a2, ..., an} as a distinct non-empty set of n actions presented by the environment
such that ϕ ⊆E. We then augment C1 to describe the following problem:
C3 — Optimal plan of up to two distinct actions
Input: An environment as a set E = {a1, a2, ..., an} of n possible actions and a
function v that assigns an outcome value to each action plan ϕ ⊆E.
Output: An action plan ϕ such that v(ϕ) is maximized over all ϕ ⊆E, no a ∈ϕ
is identical to itself (i.e., the same action cannot be performed more than once),
and |ϕ| ≤2.
The only way to solve C3 is to make a number of calls to the oracle which is equal to the
number of possible action plans (with a maximum of two actions). This number will grow
triangularly (n(n+1)
2
) — i.e., half of a square — with the number of actions.29 This tractable
procedure would satisfy the Combinatorial Principle of Actions (CPO), i.e., that action plans
yield outcome values that does not necessarily correspond to the sum of its individual actions
if performed in isolation. It would, however, violate a fundamental principle of causality:
that the resulting outcome of two causal events, action x and action y, depends on the order
in which x and y occurs. We can call this the Principle of Causal Order (PCO). In order
to satisfy PCO when solving C3, the consequentialist must make an additional triangle of
calls to the oracle, which completes the quadratic growth of n(n −1). In asymptotic Big
O, however, solving C3 in either way results in a time complexity of O(n2), which is still
comfortably within tractable bounds.
The computational complexity of action-outcomes becomes an issue for the consequentialist
when we generalize problems of type C3, e.g., to account for n number of actions:
C4 — Optimal plan of up to n distinct actions
Input: Same as C3. Output: An action plan ϕ such that v(ϕ) is maximized
over all ϕ ⊆E, no a ∈ϕ is identical to itself, and |ϕ| ≤n.
27To show this result in an algorithmic procedure, we can simply extend the exhaustive search (Algorithm
1) to iterate n actions over i values, e.g., by adding one additional for-loop for each i, or as a nested loop over
values 1 to i within the loop over actions 1 to n.
28See Lindner et al. (2020) for a similar analysis of action plans based on the SAS+ formalism.
29As the famous story goes, Carl Friedrich Gauss quickly identiﬁed the formula for this series at a young
age when asked by his teacher to add all the numbers between 1 and 100.
20

--- Page 21 ---

The time complexity of an exact algorithm that solves C4 while adhering to the CPO is
O(2n). In other words, there is no polynomial-time tractable procedure for consequentialists
who try to solve problems of type C4.30 Worse still, if the consequentialist should also adhere
to the PCO, an exact algorithm would yield the factorial growth of O(n!) (N. J. A. Sloane,
2022).31 More broadly, it is well-known that many planning tasks are PSPACE-complete
(Bylander, 1991, 1994; Littman et al., 1998).32
Note that, while this intractability might not constitute a detrimental issue in practice —
e.g., for small inputs, say, four possible actions, solving C4 following CPO requires 15 calls,
whereas following CPO and PCO requires 64 — C4 still presupposes a large set of other
non-trivial assumptions that might not hold in real-world situations. For instance, it assumes
that agents cannot perform the same action more than once, and that the problem space
remains static while the agent computes the solution. By contrast, real-world environments
might present a potentially inﬁnite set of possible actions in a state space which is only
partially observable and changes in continuous time (which we will return to in sec. 4.3).
Above all, the agent cannot make any calls to a causal oracle but needs to rely on its own
causal engine; which leads us to the complexity of causal inference.
4.2. Causal Inference
As soon as we enter the realm of uncertainty, we cannot guarantee that the performance
of any system will be optimal. Instead, the best we can hope for is optimal according to our
“best guesses”, i.e., in virtue of what we believe or know (Bayesian optimality). This is part of
the reason why many versions of utilitarianism are revised so as to stress the maximization
of “expected” as opposed to actual utility (Broome, 1987). It also forms the basis for the
expected utility hypothesis (Von Neumann and Morgenstern, 1947), which is widely used in
decision theory and economics to model rational choice, preferences, and risk appetite (i.e.,
openness and aversion to risk) when payoﬀs are unknown.33 Note, however, that diﬀerent
ways to model probability leaves room for interpretations that carry moral weight, in the
sense that diﬀerent normative principles can guide how decisions under uncertainty should be
tackled.
This is illustrated in the following problem, represented as a directed acyclic graph (Figure
2). The graph shows an environment with three actions, each with a probability of yielding
one out of two possible outcome values. If we simply want to maximize expected utility
regardless of risk, we can simply add the product of each outcome value with their respective
probability — e.g., 0.2(−2) + 0.8(4) for a1 — and select the action with the highest expected
utility. Alternatively, a more risk averse option would be to select the action with the best
worst-case outcome (a decision rule called “minmax”, i.e., maximizing the minimum gain).
While these two decision-procedures make little diﬀerence with regards to runtime — like
30This is analogous to the salad problem following Φ (where the CPO is exchanged for the equivalent CPG).
31This series is called “the number of permutations of nonempty subsets of {1, ..., n}” (N. J. A. Sloane,
2022), and can be expressed as the ﬂoor function of en! −1, where e denotes Euler’s number.
32See also B¨ackstr¨om and Nebel (1995) for some tractable results for SAS+ planning.
33Speciﬁcally, the hypothesis states that an agent chooses between alternatives by comparing expected
utility values, which is commonly calculated as the weighted sum of utility values U multiplied by their
probabilities P, in the sense that P U(xi)Pi.
21

--- Page 22 ---

C5 — Optimal action under uncertainty
E
a1
-2
0.2
4
0.8
a2
7
0.7
-4
0.3
a3
3
0.6
-1
0.4
Figure 2: A directed acyclic graph (DAG), representing a decision problem under uncertainty.
our solution to C2, both take O(no) time, where o refers to the number of outcomes for each
action — they make a signiﬁcant moral diﬀerence.
However, like C1-C4, C5 still assumes some sort of Bayesian oracle, which is able to
infer the exact posterior probabilities that certain events (outcomes) will occur given certain
causes (actions). More broadly, causal inference can be understood as the ability to identify
what causes what, e.g., “what is the cause (or causes) of phenomenon X?”, “what is the eﬀect
(or eﬀects) of Y ?”, and “what is the causal relationship between X and Y ?”. None of these
questions are trivial; indeed, scientiﬁc endeavors are to a large extent driven by answering
causal question through a combination of carefully collected data, a vast set of statistical
modeling techniques, and causal reasoning capacities such as deductive (deducing from given
premises), inductive (inferring from observations), and abductive reasoning (inference to the
best explanation).
One essential aspect of causal inference is to determine posterior probabilities based on
prior knowledge, i.e., to the determine the likelyhood of A given evidence or belief B. In
statistical modeling, the Bayesian interpretation of probability oﬀers a popular response to
this challenge. Bayesian methods — e.g., Bayesian inference, networks, and statistics —
are all based on Thomas Bayes’ theorem, which states that the probability of A given B is
provided by the equation Pr(A|B) = Pr(B|A) Pr(A)
Pr(B)
.34 Bayesian modeling have been used to
address and model a vast range of cognitive phenomena, such as motor control (K¨ording and
Wolpert, 2006), symbolic reasoning (Oaksford and Chater, 2001), animal learning (Courville
et al., 2006), causal learning and inference (Steyvers et al., 2003; Griﬃths and Tenenbaum,
2005), inductive learning (Tenenbaum et al., 2006), goal inference (Baker et al., 2007), and
consciousness (Lau, 2007).
Among the most powerful and widely used extensions of Bayes theorem is the construction
of graphical models, called Bayesian networks (BNs) (Pearl, 1985), which can succinctly
represent a large set of variables and their conditional dependencies as a single DAG (Figure
3). BNs have been particularly useful in addressing the learning of causal relationships in
humans (L Griﬃths et al., 2008). While the nodes of a BN represent Bayesian variables of
34Applying Bayes’ rule to determine the likelyhood of some causal event A given B is a trivial procedure
given that we have (i) some prior probability that A (before B) P(A), (ii) some estimated evidence for the
probability that P(B) without A (and P(B) ̸= 0), and (iii) an estimate of the converse likelihood that B
happens given that A.
22

--- Page 23 ---

x1
Holiday
x2
Rain
x3
> 1 Operators
x4
Stress
x5
Runaway trolley
x6
Lever
x7
Track of 5
x8
Track of 1
Figure 3: A Bayesian network representing the causal relationships of eight Boolean variables for the Bayesian
Trolley Problem (C6). Since their introduction in the 1980’s, Bayesian networks have facilitated evidence-based
prediction in complex domains such as medical diagnosis (Lucas et al., 2000) and weather forecasting (Cofıno
et al., 2002).
interest — e.g., hypotheses, observable quantities, occurences of events, features of objects —
the links (or edges) represent conditional dependencies between the variables. Each node has
a probability function that returns a variable depending on its parent variables (following
Bayes’ theorem), and nodes that are not connected are conditionally independent of each
other. For instance, the BN illustrated in Figure 3 describes the causal relationships between
eight variables: whether it is a public holiday (x1), whether it is raining (x2), whether two or
more train operators are currently working at the train station (x3), whether the operators
are stressed (x4), whether there is a runaway trolley (x5), whether a lever is pulled (x6), and
whether the trolley is on course to collide with 5 (x7) or 1 (x8) people. Since BNs supports
the inference of probabilities for any possible subset of variables (i.e., on the basis of evidence
about those subsets), it can be used to support causal reasoning processes in any direction of
the network. Using the chain rule of probability,35 the joint probability — i.e., the probability
distribution on all possible combinations of values — is given by:
P(x1, ..., xn =
Y
i
P(xi|ψi)
(2)
where ψi denotes the values for the parent nodes of xi. The joint distribution for the
network in Figure 3 is therefore: P(x1, ..., x8) =
P(x1)P(x2)P(x3|x1)P(x4|x1, x2, x3)P(x5|x3, x4)P(x6|x5)P(x7|x6)P(x8|x6)
(3)
We can now describe a range of Bayesian inference problems for consequentialism, such as:
C6 — Bayesian Trolley Problems
(a) Likelihood — what is the probability P that x7 is true? (given full, partial, or no
evidence about its parent variables)
35The chain rule allows one to compute the joint distribution of a set of variables solely using conditional
probabilities, in the sense that P(A ∩B) = P(B|A)P(A).
23

--- Page 24 ---

(b) Conditional probability — what is the probability that x7 is true given evidence that it
is a public holiday (x1 = true)?
(c) Causal reasoning — e.g., what eﬀect does pulling the lever (x6 = true) have on x7 or
x8?
(d) Most probable explanation (MPE) — what is the most probable conﬁguration of a set
of variables given full evidence about the complement of that set?
(e) Maximum a posteriori hypothesis (MAP) — what is the most probable conﬁguration of
a set of variables given partial evidence about the complementing set?36
BNs are perfectly suited to answer such causal inquiries, using algorithms such as variable
elimination (Zhang and Poole, 1996) and message-passing (Pearl, 2022) for exact inference,
and random sampling (Pearl, 1987) for approximate inference. However, even if questions like
C6 (a)—(e) can be solved in reasonable time for constrained networks, it has been proven that
most inference problems for Bayesian Networks are intractable in general. More speciﬁcally,
exact inference on arbitrary graphs is NP-hard (Cooper, 1990),37 which means that inferring
the exact probability of some event (or that a propositional expression is true) is at least
as hard as the hardest problems in class NP. Furthermore, the decision variant of ﬁnding
the most probable explanation (MPE) is NP-complete (Shimony, 1994), while the related
maximum a posteriori hypothesis (partial MAP) is NPPP-complete (Park and Darwiche,
2004).38 Perhaps more intriguing is the results that approximations of these problems are
also intractable: approximating exact inference (Dagum and Luby, 1993), MPE (Abdelbar
and Hedetniemi, 1998), and partial MAP (Park and Darwiche, 2004) are all NP-hard.39
One important lesson from these results is that the complexity of Bayesian inference
depends on the structure of the network: while constrained graphs yield a bound on the
number of conditional dependencies and parent variables for each node, unconstrained graphs
cannot be exploited for eﬀective computation. For instance, for chain-like graphs of the
type x1 →x2 →x3 →x4 →x5, an elimination algorithm can determine the exact inference
of P(x5) by a step-wise elimination of the parent variables, which can be computed in the
polynomial time O(nv2), where n is the number of variables and v denotes the number of
possible values the variables can take. However, as the number of variables depending on
other variables grows, inference in BNs starts to mirror the problem of determining whether
an arbitrary Boolean formula can be satisﬁed (SAT): the ﬁrst known NP-complete problem.40
36MAP (sometimes called Partial or Marginal MAP) can be viewed as the generalization of MPE in the
sense that it might require a marginalization of the variables that are not observed nor explained. Furthermore,
note also that both MPE and MAP has many variants in the literature on Bayesian networks: see (Kwisthout,
2011) for a clariﬁcation.
37More precisely, exact inference is #P-complete (Roth, 1996), where #P is the class of counting problems
associated with NP.
38PP is the class of problems decidable by Probabilistic TM with an error probability of less than 1/2 (Gill,
1977), and NPPP is the class of problems solvable by a non-deterministic TM with access to an oracle for
problems in PP.
39See (Kwisthout, 2011) and (de Campos, 2020) for summaries of complexity results for the many variants
of the MPE and MAP problems.
40It should be no surprise that SAT has been instrumental in deriving complexity results for BNs.
24

--- Page 25 ---

In summary, if a consequentialist agent were to solve causal inference problems using
Bayesian networks, we cannot expect that any tractable procedure could yield precise or even
approximate solutions for arbitrary graphs. The same intractability results have pestered
Bayesian modeling in cognitive science, as Bayesian planning (K¨ording and Wolpert, 2006),
learning (Kemp and Tenenbaum, 2008), and decision-making (Vul et al., 2014) all presume
NP-hard computations. As a potential remedy, we might instead identify the constraining
conditions that enable tractable solutions (Kwisthout et al., 2011). For instance, the bounded-
variance algorithm (Dagum and Luby, 1997) can generate approximations of inferences in
polynomial time if extreme conditional probabilities are excluded (i.e., values near 0). Similarly,
it has been shown that MPE is tractable when either the treewidth of the underlying graph
is low,41 or the probability of the most probable explanation is high (and partial MAP is
tractable when both conditions are true) (Kwisthout, 2011). However, this introduces another
uncomfortable trade-oﬀ: there is no guarantee that such constraining conditions capture
reality. For machines, this means that a constrained graph could potentially fail to model
the correct causal relationships. With regard to Bayesian modeling of human cognition
— e.g., of ethical decision-making under uncertainty — it also means that one must ask
whether the constraints are reasonable with respect to the modeled phenomenon. And for
the consequentialist philosopher, it poses the question: what are the constraining conditions
under which causal inference should be expected to be successful for an agent following
consequentialism?
4.3. Decisions in Dynamic and Partially Observable Environments
We have thus far only investigated problems where the entire state space of a problem
is taken as an input, e.g., as elements of sets or nodes of graphs. But ethical problems of
the real-world presents a range of additional challenges that might curb a consequentialists
ability to produce the best outcome, including (i) partial information and observability, (ii)
dynamic and continuous environments that constantly change, (iii) limited time horizons to
make decisions and execute actions (e.g., emergency situations), (iv) a potentially inﬁnitely
long time horizon to evaluate outcomes against, and (v) a potentially inﬁnite set of possible
actions (e.g., movement in dimensions higher than one). Each challenge reﬂects well-known
epistemological issues for the consequentialist (Lenman, 2000), such as, what is the smallest
amount of information needed to make a reasonably informed ethical decision (given that
information can never be complete)? Or what is the time horizon for which the outcome
of an action should be considered (i.e., how long is the future we need to predict)?42 Time
alone might introduce chaotic unpredictability. As meteorologist and mathematician Edvard
Norton Lorenz famously noted: a butterﬂy ﬂapping its wings could result in a tornado a few
weeks later.43
41Treewidth is a graph theoretical concept which can informally be understood as a measure of how much
‘wider’ a given graph is than a simple tree (in which any two vertices are connected by exactly one path), and
more formally as the size of the largest vertex set in a tree decomposition of the graph (Bodlaender, 1994).
42However, note that both contemporary and classic and consequentialists — e.g., Bentham (1789), Mill
(1861), and Sidgwick (1907) — do not assert their principle as a strict decision procedure, but rather as a
criterion or standard. See Bales (1971).
43In chaos theory, the “butterﬂy eﬀect” is the observation that tiny changes in one state of a non-linear
deterministic system can produce massive diﬀerences in later stages (Lorenz, 1963).
25

--- Page 26 ---

Nevertheless, a number of mathematical tools have been developed to successfully tackle
such issues. In the absence of analytical solutions or evidence, stochastic methods allow us to
explore complex phenomena by throwing dice (e.g., Monte Carlo methods), or by viewing
them as memoryless chains of events (Markov process). A Markov process is any process
that satisﬁes the Markov property, which means that the likelihood of a certain future state
only depends on the present state (i.e., it is “memoryless”).44 From a complexity theoretic
point of view, the appeal of studying processes in Markovian terms is that it allows otherwise
intractable or undecidable stochastic modeling to be tractable (Vanmarcke, 2010). Monte
Carlo methods denotes another general class of algorithms that are based on repeated random
samplings, e.g., by drawing a number of pseudo-random variables within a certain distribution
or interval.45 In turn, these rather simple ideas have matured into an umbrella of stochastic
approaches that have been successfully applied to a vast range of scientiﬁc problems, e.g., in
statistical physics (Binder et al., 1993), engineering (Hajek, 2015), and Bayesian statistics
(Gelman et al., 2013).
One fruitful application of stochastic methods in the realm of automated decision-making
is reinforcement learning (RL). The idea behind reinforcement learning is simple: an agent
learns from interacting with an environment by updating its behavior — e.g., strategy or
action-policy — in light of the reward it receives. An RL agent is often formalized as a Markov
Decision Process (MDP), the 5-tuple ⟨S, A, R, P, γ⟩, where:
• S is a set of states (called state space)
• A is a set of actions (called action space)
• Ra(s, s′) is the reward the agent obtains by transitioning from state s to s′ by performing
action a
• Pa(s, s′) = Pr(s′ | s, a) is the probability of transitioning from s ∈S to s′ ∈S given
that the agent performs a ∈A
• γ is the discount factor (0 ≤γ ≤1) that speciﬁes whether the agent prefers long- or
short-term rewards.
The goal of an RL agent is to maximize reward (R) over some speciﬁed time horizon. In
order to do so, it needs to ﬁnd an policy, i.e., a function π(s, a) which decides what action a
to execute given a certain state s. If the goal is to maximize the expected discounted reward
arbitrarily into the future (called the inﬁnite-horizon objective), the optimal policy π∗can be
formalized as:
π∗:= argmax
π
E
" ∞
X
t=0
γtR(st, at)
π
#
(4)
44As such, Markov processes constitute a broad class of both continuous and discrete stochastic processes;
for instance, Poisson, Wiener or Brownian motion, and random walks can all be formulated as special variants
of a Markov process.
45As the story goes, the modern version of the Monte Carlo method was invented by Stanislaw Ulam while
working with the Manhattan Project in Los Almos; in fact, the method were instrumental for deriving the
simulations required for the project’s success (Haigh et al., 2014).
26

--- Page 27 ---

RL — in combination with Monte Carlo, deep neural networks, and other techniques —
have yielded super-human performance in complex game environments such as Dota 2 and
Go (Berner et al., 2019; Silver et al., 2018), or, more recently, to notable advancements in
the control of nuclear fusion plasma (Degrave et al., 2022). More broadly, it has been argued
that reward is enough to drive all forms of behavior that are associated with natural and
artiﬁcial intelligence, such as learning, knowledge, perception, language, social intelligence,
and generalization (Silver et al., 2021). Due to its general applicability, it has been suggested
that RL provides the appropriate framework to theorize about an ideal ethical artiﬁcial agent
(Abel et al., 2016), or for the construction of artiﬁcial virtuous agents (Stenseke, 2021).
Importantly, RL is able to address many of the factors that might curb ethical agents’
decision-making: continuous dynamics (Serfozo, 1979), partial observability (Cassandra et al.,
1994), and objectives over diﬀerent time horizon.46 One key challenge in RL is the trade-oﬀ
between exploration and exploitation. I.e., when we do not have perfect information, should we
decide on the basis of what we already know (exploit), or take the risk of investigating options
that would potentially be even better (explore)? In theory, the explore-exploit dilemma could
be solved through the notion of partial observability, which oﬀers a way to model what is
and what is not directly observable by the agent. A partially observable Markov decision
process (POMDP)47 augments the MDP 5-tuple by adding two additional terms: a set of
observations (Ω) and a set of conditional probabilities (O), which represent the likelihood of
observing ω ∈Ωif the agent performs a and the environment transitions to hidden state s′,
in the sense that O = Pr(ω | s′, a). In short, solving POMPDs centers around computing
probability distributions over the possible states the agent could be in (belief states), where
an optimal policy maximizes expected reward in virtue of mapping actions to observation
histories. In principle, since an optimal solution to a POMDP incorporates the instrumental
value an action has from an information-theoretic point of view — and how the information
can be used to make better future decisions — it oﬀers a solution the explore-exploit dilemma.
Unfortunately, ﬁnding optimal solutions to POMDPs is undecidable for inﬁnite horizons
(Madani et al., 2003). Furthermore, while solutions to ﬁnite MDPs and POMDPs are decidable,
they are generally not tractable. The results by Papadimitriou and Tsitsiklis (1987) show that
ﬁnite POMDPs are PSPACE-complete, while the results by (Mundhenk et al., 2000) prove
that various MDP problems range from being complete for probabilistic logarithmic space (PL)
to being EXPSPACE-complete.48 Other complexity results in RL indicate a similar trend:
reaching a goal state might require, in the worst-case, a number of actions that is exponential
in the size of the state space (Whitehead, 1991). Intuitively, when no a priori knowledge of
the state space can be exploited, unbiased search can lead to excessive exploration. However,
worst-case time complexity results alone are insuﬃcient to assess the theoretical viability
of RL as a framework for sequential decision-making under uncertainty, as it depends on a
number of factors, such as task representation (e.g., number of states and actions (Koenig
and Simmons, 1993)), the sort of feedback provided by the environment (e.g., observability),
46E.g., a discount factor γ of 0 only considers short-term rewards, while γ = 1 without a terminal state
considers rewards over inﬁnite time.
47The POMDP framework for control under uncertainty was ﬁrst developed by ˚Astr¨om (1965) and later
adapted to problems in AI by Cassandra et al. (1994).
48See also (Littman, 1996) for a detailed survey of the complexity of MDP and POMDPs.
27

--- Page 28 ---

policy types (e.g., stationary or history-dependent (Mundhenk et al., 2000)), or restrictions on
the agent’s resources.49 Similar to the results of Bayesian inference, while there is no sound
theoretical guarantee of the success of RL, its practical viability can be signiﬁcantly improved
by simplifying the task representation (given that a simpliﬁed representation is achievable),
improving the observability of rewards, and by exploiting a priori knowledge. It should be no
surprise that RL have been particularly successful in game environments which often aﬀords
a simple representation of the state space (e.g., 2-dimensional grids of Chess and Go) and
discernible rewards (e.g., Dota or Starcraft).
But there are other issues with RL which might obstruct its applicability for consequential-
ism. For instance, even if an agent has found an action-policy which maximizes its utility in
an environment inhabited by other agents, the policies or preferred utility of the other agents
might result in conﬂicts. Such game theoretic considerations are challenging, especially in
combination with partial observability and imperfect information regarding the other agent’s
strategies and goals (we will return to this issue in section 5.1). Other issues pertains the
notion of sample complexity, i.e., the number of training samples a learning algorithm needs
to learn a target function (or within some error of the optimal function). However, as we will
discuss in section 6, sample complexity is not only plagued by the existence of arbitrarily
‘bad’ distributions of training data, but it also raises deeper philosophical issues concerning
induction.
Perhaps most critically, RL — and stochastic methods at large — presupposes trial-and-
error. While this might not be a major issue in simulated games, it presents a challenge for
real-world environments which does not necessarily aﬀord the same stochastic exploration;
particularly if some actions could have catastrophic consequences. Furthermore, given the
stochastic nature of the process, a RL agent might ﬁnd a way to increase its incentivized
reward in a way that conﬂicts with the very intention of its human designer (called “reward
hacking” in Safe AI research (Amodei et al., 2016)).50
In a similar vein, the multi-armed bandit problem has generated a rich body of work that
investigates the explore-exploit-dilemma under various conditions (Slivkins, 2019). In its
most basic form, it asks: given n possible actions (arms) which yields some reward drawn
randomly from a ﬁxed (but a priori unknown) distribution, how do you maximize the expected
gain? Instead of reward maximization, many versions of the multi-armed bandit looks at the
learning problem in terms of regret minimization, measured as the diﬀerence between the
performed action and the optimal action (e.g., given hindsight). The goal is to ﬁnd strategies
that balance exploration and exploitation while minimizing regret. Variations include regret
minimization with incomplete information (Zinkevich et al., 2007), contextual bandits where
agents receive some contextual information which relates to the rewards (Bouneﬀouf and
Rish, 2019; Langford and Zhang, 2007), the problem of identifying the best arms (Bubeck
et al., 2013), or ﬁnding arms whose mean is above a certain threshold (Locatelli et al., 2016).
Solutions to multi-armed bandits are typically investigated under one of two assumptions: (i)
stochastic — the reward distribution for each arm is unknown but ﬁxed, or (ii) adversarial
— the rewards are chosen by an adversary with unbounded computational resources (Auer
49For instance, see Chatterjee et al. (2016) for a more recent summary of decidable solutions for POMDPs
given ﬁnite-memory strategies.
50See also Garcıa and Fern´andez (2015) for a survey of literature in Safe RL.
28

--- Page 29 ---

et al., 1995) (e.g., gambling in a rigged casino). In its most general form, both assumptions
are relaxed, which leads to the restless bandit problem (Whittle, 1988). This means that the
payoﬀs can vary over time even when the arms are not played. For instance, imagine that you
are the manager of a kindergarten with n children and m babysitters, and m < n. Since the
children outnumber the babysitters, the task is to allocate the babysitters’ attention in a way
that minimizes mischief. While a child is attended to, information about its position, activity,
and mood is gained. If it is not attended to, information is lost, and the child might be up to
some mischief (they are, in a literal sense, restless).51 While many tractable solutions exist
for diﬀerent variants of the bandit problem, the restless bandit is proven to be intractable to
even approximate. The proof provided by Papadimitriou and Tsitsiklis (1994) shows that for
n arms and deterministic transitions for both unattended and actively played arms (i.e., all
transition values for attended arms and unattended arms are either 0 or 1), ﬁnding the optimal
policy is PSPACE-hard.52 Furthermore, since the proof also shows that it is PSPACE-hard
to determine whether the optimal reward is non-zero, it rules out approximate solutions.53
Of course, while it is little to no surprise that there are no eﬀective solutions to problems
like the restless bandit, it shows that there is no algorithmic way to ensure optimal performance
(or minimize regret) in sequential decision-making under uncertainty, unless the nature of
the problem space (environment) itself aﬀords exploitation. The intractability results for the
restless bandits elegantly illustrate this with respect to making decisions in a changing world.
More generally, while Markov chains and Monte Carlo dice-rolls can help to model and mine
statistical tendencies of complex spaces, its success presupposes that such tendencies exist.
This, however, might say more about the complexity of dynamic real-world processes than
it does of the computational limitations of agents. Or as Hofstadter observed: Deep Blue’s
win against Garri Kasparov says more about chess than it says about human intelligence
(Hofstadter, 2002). Bro˙zek and Janik (2019) have recently made the analogous remark with
regard to moral theory: ”the fact that a machine may be a better homo Kantianus or homo
Benthamus than any homo sapiens says little about human morality, and much about the
idealised nature of philosophical conceptions of moral agency” (p. 103). But the complexity
results discussed in this section imply something even stronger: while we might expect AI
methods to perform better than humans in a range of tasks related to ethical decision-making,
they are also bounded by the complexity of the world, which inevitably curtails any attempt
to construct a perfect moral machine.
To sum up, we have explored three sources of complexity that presents tractability issues
for computational consequentialist agents. This could imply that any computational agent
bounded by polynomial Turing-tractability will fail to adhere to the prescriptions of the
normative ideal in practice. As a corollary, it indicates that consequentialism might be better
suited as a theoretical ideal, as opposed to a viable decision-strategy that could inform ethical
decisions. But what is the point of moral theorizing if it cannot inform moral decision-making
in practice? More pragmatically, one might look for the constraining factors — e.g., in the
51See Whittle (1988) for several other intuitive examples.
52Note that PSPACE-hardness entails something stronger than NP-hardness, as PSPACE-hard problems
remains intractable regardless of whether P = NP.
53However, approximation guarantees are possible if the problem is relaxed to allow for linear programming,
in the sense that one arm is played per time step on average (Guha et al., 2010).
29

--- Page 30 ---

space of possible actions, action-combinations, conditional probabilities, time horizons, task
representations, and approximations — under which consequentialist decision-making becomes
tractable, and determine, in each case, how closely those decisions approximates the optimal;
or some ﬁxed point of moral value.
5. Deontology and Rule-Followers
While consequentialism centers around outcomes, deontological ethics focuses on actions
themselves: whether an action is moral depends on whether the action is obeys a set of moral
rules, obligations, or duties. But what justiﬁes a rule in the ﬁrst place? And how can one
ensure that a given interpretation of a rule stands up to the principle it was justiﬁed upon?
According to divine command theory, the legitimacy and universal validity of moral rules is
grounded on the authority of God. The Christian Ten Commandments provides canonical
examples of such rules, e.g., “thou shalt not kill” or “thou shalt not steal”, given to Moses at
Mount Sinai by God. By contrast, in Immanuel Kant’s deontological ethics, rational beings
are bound to moral law by their own autonomous will, and the fundamental principle for our
moral duties is captured in the categorical imperative: “Act only according to that maxim by
which you can at the same time will that it should become a universal law” (Kant, 1785).
This means that, as rational beings, people have a duty to only act according to maxims that
a community of rational agents would accept as laws.
It should be stressed that rules and systems of rules are already deeply embedded in most
human societies; generated and enforced by social institutions as law. In fact, morality and
law share a complex and complementary relationship, as they are both normative systems
that seek to regulate human behavior, e.g., in order to foster social harmony and stability of
communities. On the one hand, law may compensate for the functional frailty of morality,
since the latter lacks the mechanisms to enforce its own prescriptions. On the other hand,
morality can serve the coordination of social expectations where law is diﬃcult to apply, e.g.,
through notions of responsibility, solidarity, and fairness. Furthermore, many legal thinkers
believe that, to succeed in its function of regulating behavior, law must resonate with the
moral norms and sentiments of its subjects.54
Given the rule-based nature of deontology in conjunction with the view that machines are
essentially systems of automated rule-following, one might conclude that deontology provides
an excellent recipe for moral machines. After all, deontological rules elegantly corresponds
to the conditional statements pervading in machine code: e.g., “If input X →do action
Y ”. In popular culture, this view has most famously been explored (and problematized) in
Isaac Asimov’s novels as “Laws of Robotics” (Asimov, 1942). The appeal of computational
deontology is also well reﬂected in the machine ethics literature; in fact, Tolmeijer et al. (2020)
survey shows that 22 out of 50 implementations in machine ethics incorporate some elements
from deontological ethics. Part of the appeal is the common-held view that deontology
is, computationally speaking, less complex than its alternatives (Brundage, 2014; Wiegel
54Of course, this question divides legal positivists and non-positivists; the former view holds that law can
be valid even if it is morally unjust, whereas the latter holds that law is only valid if it is consistent with
moral norms (Moka-Mubelo, 2017).
30

--- Page 31 ---

and van den Berg, 2009; Tolmeijer et al., 2020). There is a technical, psychological, and
philosophical dimension to this view:
(1) From a technical perspective, it is intuitively true that it is easier to follow hard-coded
rules than to compute consequences (e.g., considering the complexity discussed in 4). As an
example, in their study of the moral evaluation of action plans, Lindner et al. (2020) found
that deciding whether a plan is morally permissible according to act and goal-deontology is
computable in linear time. By contrast, they also found utilitarianism to be PSPACE-complete
by the same metric, and that principles based on harm avoidance are co-NP-complete.
(2) Second, following the work on the psychology of decision-making by Kahneman (2011)
comes the inﬂuential theory that posits the existence of two distinct aspects of human
reasoning: “system 1” which is fast and intuitive, and “system 2” which slow and deliberate.
In moral psychology, this has led to the development of the dual process theory of moral
cognition (Greene, 2007), which postulates that moral judgment rely on both conscious-
controlled processes (corresponding to typically utilitarian judgements), and automatic-
emotional processes (corresponding to typically deontological judgments). Empirical ﬁndings
based on the theory has showed, among other things, that an increase in cognitive load (by
imposing an additional control-demanding task) leads to an increase in reaction time for
utilitarian judgments, while it does not increase reaction time for non-utilitarian judgments
(Greene et al., 2008). Another study demonstrated that cognitive load may increase the
frequency of deontological judgment, and that utilitarian responses are less likely if the subjects
were reminded of their own mortality (Tr´emoli`ere et al., 2012). Although this does not prove
that deontology as a normative theory is more computationally eﬃcient than utilitarianism
per se, it suggests that conscious-controlled processes in human moral judgments, in contrast
to automatic processes (which may be described as characteristically deontological judgments),
are more cognitively demanding and susceptible to cognitive load manipulation.
(3) The idea that rules can serve to alleviate the cognitive burden of moral judgments is
also widely represented in moral theory; in particular as a move to save consequentialism as a
decision procedure in light of the challenges that classic utilitarianism face (Brandt, 1979).
For instance, modern versions of consequentialism diﬀerentiate between acts which would
produce the most good (act utilitarianism) and rules which, if they were followed, would
produce the most good (rule utilitarianism). Since the former, if it were to be used as a
decision procedure, puts unrealistic demands on agents — e.g., susceptible to biases, lacking
complete information about the consequences of actions, or lacking time to make the correct
judgments — many consequentialists adopt some version of rule utilitarianism as a decision
procedure (Hooker, 2016).55
Nevertheless, there are computational aspects of deontology — and moral rule-following
more broadly — that are relatively ignored in the machine ethics literature. While machine
executions of the type “If input X →do action Y ” might seem trivial, they rest on the
conditions that:
55As an intuitive example: we stop at a red light because we might believe that this particular traﬃc rule
produces the most overall good (e.g., for society), and not because the act itself in this particular instance
yields the most overall good. Note that this does not necessarily mean that act and rule utilitarianism are in
conﬂict: act utilitarianism might still be the standard used to evaluate the consequences of rule-adherence
prescribed by rules utilitarianism.
31

--- Page 32 ---

(a) X is really X, e.g., the agent has the appropriate understanding that an input (e.g.,
a situation) has certain properties (or alternatively, a “semantic grounding” of X (Harnad,
1990)) and
(b) performing Y is an appropriate response to X in every possible instance of X (or
alternatively, Y is intrinsically good).
If both conditions are satisﬁed, a deontological agent would be able to act morally in
constant time O(1), given that we store the appropriate action-rules for every possible input
(which instead puts demand on the space complexity).56
In practice, however, conditions (a) and (b) are immensely hard to satisfy: (a) assumes
perfect knowledge of any possible state space, and (b) relies on some general ability to
understand that an action is an adequate response to a particular state.57 Against this
background, this section will explore the complexity of deontology by discussing the generality
of rules (5.1), the complexity of logic and semantics (5.2), and the prospect of consequentialist-
deontological hybrids (5.1.3). Additionally, section 5.1.2 covers the complexity of strategic
dynamics based on algorithmic game theory. We will argue that the moral power of rules lie
in their general applicability, general justiﬁcation, and computational simplicity. However, to
be computational eﬃcient at run-time, it presupposes that one has already collected the vast
knowledge required for such generalities to hold in practice.
5.1. The Generality of Rules
The generality of moral rules can be understood in several ways. We will ﬁrst make a
distinction between two important dimensions, namely application and justiﬁcation. The ﬁrst
refers to the general ability to decide, given any possible input, whether a certain action is
appropriate or inappropriate according to a set of rules. Alternatively put, a general ability
to decide whether an action successfully adheres to the rule, principle or obligation it was
justiﬁed upon. For an agent to successfully follow “do not harm others” in general, it means
that it never acts in a way which directly harms another agent. While rules of this type may
seem trivial for humans, they are more diﬃcult to approach from a computational perspective.
For instance, it is apparent that they presuppose sophisticated abilities to interpret whether
actions (or more likely, chains of actions) actually obey the rule: e.g., knowing what another
agent is; being aware of the set of possible actions (and sequences of actions) in a dynamic
environment that could cause harm to other agents; etc. Here, there is an extreme variance of
rule-application with regard to context: a self-driving vehicle will likely cause harm to other
56For instance, we can imagine that every input is an index which immediately executes an action from a
list of actions. Alternatively, we might use moral duties for deontological action-evaluation, e.g., in terms of
constraint satisfaction: given an input X, we simply enumerate over a list of actions and check whether they
violate any moral duty (this would be analogous to problem C2 in 4.1).
57As we will discuss later, this may also involve an ability to understand whether an action stands up to
the normative principle upon it is justiﬁed. Alternatively, to satisfy (b), we might demand that an action
Y is intrinsically good, regardless of context (or that certain input-action-pairs are intrinsically good). As
a thought-experiment, we could imagine a machine that was hard-coded with exclusively intrinsically good
actions, and simply have it repeatedly executing a loop of good actions. Given that the actions were in fact
intrinsically good, the machine would be a perfect moral machine. This seems to work for simple machines
such as toasters. But in dynamic and partially observable environments, this seems to presuppose God-like
omniscience.
32

--- Page 33 ---

agents if it collides with them at high speeds (i.e., “do not harm others” easily translates
into collision-avoidance), whereas a social robot in a classroom might be oblivious to the
potentially inﬁnite set of actions and causes that could cause harm.
The second dimension is whether a rule itself is generally justiﬁed. For divine command
theorists, rules may be universally justiﬁed on the basis of divine authority. In machine ethics,
this has inspired the development of divine-command logic, where human input is interpreted
as divine command for the machine (Bringsjord and Taylor, 2012). For contractualists
stemming from Kantian thought, justiﬁed principles require instead that they are agreed
upon by everyone (Rawls, 1980), or that no-one could reasonably reject them (Scanlon, 2000).
Contractualism puts emphasis on the rationality of agents, which, following Kant’s moral
rationalism, requires that we respect others in the sense that principles must be justiﬁed to
each person. By contrast, contractarians stemming from Hobbesian thought — e.g., Gauthier
(1987) and Narveson (2001) — puts emphasis on the self-interests of agents, in the sense that
moral rules ought to maximize the joint interest. Thus, for contractarianism, adherence to
moral norms or rules are justiﬁed on the basis of an agent’s self-interest; and altruism occurs
when the agent recognizes that the best way to maximize their self-interest is to cooperate
with others.
5.1.1. Human Rule-Following in Legal and Liberal Contexts
A ﬁrst step in analyzing the computational complexity of rules stemming from these two
notions of generality is to look at rule-following in human practices. One observation is that
legislative practices are informed by the principle of ignorantia juris non excusat (“ignorance
of the law is no excuse”) in the sense that laws should be easy to apprehend and easy to
comply with. If not, willful blindness can be exploited by defendants. It also entails that
human laws are formulated with regard to human capacities: it would be contrary to the
purpose of laws if they were formulated so that no human could follow them. However, what
separates moral from legal rules, is that the latter are backed up by legislative mechanisms of
jurisdiction and may be enforced by the state (e.g., police). Importantly, if it is hard to decide
how a certain law should apply in a speciﬁc circumstance, we rely on experts (e.g., lawyers,
judges, and counselors of various courts) to interpret the law, ensure that it is applied in a
just way, and possibly generate a new praxis for applications in the future. In fact, in many
legislatures, laws are vaguely formulated by intention in order to be continuously infused with
meaning as novel situations transpire.58 Thus, in such occasions, the normative content of the
law is mainly given by its interpretation, and not by the law itself.59 In turn, if application
falls short in representing the moral sentiments of the subjects of which the law applies to, it
may constitute a failure of law: and defendants might rightfully choose to appeal the verdict.
The point is that, while rule-following in terms of legal law-obedience might appear to be
relatively simple in human contexts, it is only against the background of rather complex
pre-existing mechanisms that ensures their successful implementation. It is therefore hard to
make sense of the computational complexity involved in following human laws, as it already
presupposes the cognitive capacities (or certain behavioral standards) that makes up human
58For instance, the Court of Justice of the European Union.
59That is, courts provides the guarantee that a particular application stands up to the principle upon which
it was normatively justiﬁed. This argument is developed at a greater length in Stenseke (2023).
33

--- Page 34 ---

legal personhood, while allocating the processes of interpretation and justiﬁcation to legal
practitioners.
Another observation, which is related to the ﬁrst, is that laws are often articulated as
positive or negative rules, i.e., “do this” or “do not do that”. From a human perspective,
negative rules are, at least prima facie, simpler than positive rules: it is easier to remember
what one should not do, as opposed to what one should do (in other words, it reduces space
complexity). This, especially in the context of Western liberal societies, can be reﬂected
in “the harm principle”, as found in France’s Declaration of the Rights of Man and of the
Citizen (1789): “Liberty consists in being able to do anything that does not harm others”
(Johnson, 1990), or in Mill’s On Liberty: “[...] the only purpose for which power can be
rightfully exercised over any member of a civilised community, against his will, is to prevent
harm to others” (Mill, 1859). However, the memory-saving aspect of such principles, from a
computational perspective, only makes sense against the backdrop of autonomous citizens
within the context of a liberal society, and the potentially inﬁnite set of actions they can do.
For instance, the best way to follow “do not harm others” for a machine, might simply be to
do nothing at all: the complexity of adhering to the principle is proportional to the set of
actions it can do.
5.1.2. General-Purpose Rules and their Justiﬁcation
What is common to legal rule-following and moral rules based on divine command is that
the acting agent does not necessarily have to understand the moral rationale behind the rule
in order to behave morally; the agent simply follows the rule without reﬂecting on whether the
rule is morally justiﬁed (it is simply the case that God or law says so). Of course, there might
be immense disagreement on what the right rules should be. By contrast, for Kantian ethics,
contractarians and contractualists, rules may involve justiﬁcation as part of the action itself,
in the sense that an act is only moral in so far as it is accepted by the aﬀected participants
(or members of the moral community of which the contract applies to). This is well-reﬂected
in rules that have the ambition of being both generally applicable and generally justiﬁed, such
as Kant’s categorical imperative (CI) or the Golden Rule (GR): “treat others as you would
like others to treat you”.
It is interesting to note that general-purpose rules that involve justiﬁcation can be amenable
to a complexity analysis if the rule itself provides grounds for deciding whether an action
is moral. To illustrate, following the GR, the query “is action X morally permissible given
input Y ?” is decidable for an agent A, if it is decidable whether A herself would accept X
if it were performed by another agent B given input Y . For instance, if X given Y causes
harm, and A would not want others to cause her harm, the answer is decidedly no. Of course,
while this sort of analysis ignores the complexity involved in the determining the de facto
mappings between any possible input, action, and outcome, it gives a general structure which
can be analyzed:
(GR1) Golden Rule based on one’s own preferences60 — For instance, the GR might
refer to a set of actions and individual preferences of an acting agent A, in the sense that A
60Here, we remain agnostic about the precise nature of “preferences” — it might as well refer to duties or
obligations — in order to encompass many versions of deontology; the only important thing is that it can be
represented as a numerical or boolean value.
34

--- Page 35 ---

has to check whether the individual actions satisfy her individual preferences: she will treat
others (act) based on how she likes others to treat her (i.e., how an action, if performed by
someone else, would aﬀect her own preferences). Given that the agent can quickly check how
actions aﬀect her preferences, the worst-case time complexity of deciding whether any action
is morally permissible is O(np), where n is the number of possible actions and p is the number
of preferences.61
As a general-purpose rule, GR1 has a great appeal in virtue of its computational eﬃciency:
simply check whether you would accept an action based on your preferences. Prima facie, it
would also capture many preferences that are commonly shared among self-interested agents
in the natural world, e.g., to increase one’s pleasure and reduce one’s suﬀering. As such, it
would therefore work to prevent actions that, for instance, directly cause harm. However, the
major problem with GR1 is that it does not account for diﬀerences in preferences between
agents, and how actions aﬀect the preferences of agents in diﬀerent ways. It is therefore
susceptible to counter-examples: e.g., a judge should not send a criminal to prison, because
the judge himself does not want to go to prison.62 As a remedy, Reinikainen (2005) has argued
that the universal applicability of GR needs to stand “the test of publicity”, which means
that an action needs to be “acceptable from the imagined perspective of everyone aﬀected”
(p. 155). This motivates a second formulation:
(GR2) Golden Rule based on the preferences of others — Assuming that the acting agent
has perfect knowledge of how actions aﬀect the preferences of others, and every agent has the
same amount of preferences, the worst-case time complexity of deciding whether any action is
morally permissible is O(npo), where o refers to the number of other agents.63
What becomes clear from comparing formulation GR1 and GR2 is not the relatively small
increase in time complexity, but the increase in knowledge requirements for GR2 to work.
Perfect knowledge about how actions aﬀect the preferences of others might be diﬃcult to
attain, even in smaller groups of agents. However, what is missing from GR2 is that it fails
to capture the recursive feature that is essential to most formulations of the Golden Rule. It
is not that an agent should simply take others’ preferences into account; the agent should
consider the way in which they would like others to take their preferences into account. This
may not even involve speciﬁc actions or preferences as such, but rather, that an agent should
generally behave towards others in a manner which they would like others to generally behave
towards them. This feature of GR has been explored by philosophers such as Stace (1937),
Wattles (1996), and Singer (2002), whom all make the observation that objections against the
GR only have force against speciﬁc applications by GR, but not if we take GR to refer to
an agent’s general behavior. Following Wattles (1996), this can involve one’s own method of
applying the golden rule:
(GR3) Apply the golden rule to your general behavior in a way that you would want others
to apply the golden rule to their general behavior.
61Note that O(np) is also the tight bound of ﬁnding the most satisfactory action (e.g., an action which
maximizes preferences), which is analogous to C2 in 4.1.
62This counter-example was famously made by Kant (1785, footnote 12).
63For instance, if there are two possible actions, ﬁve preferences, and 8 billion agents, it would take 80
billion computations to decide whether any of the two actions satisﬁes the preferences of the world population
in 2022.
35

--- Page 36 ---

The formulation is self-correcting in the sense that it will consider the potentially inﬁnite
ways in which an agent A would like others to consider in their treatment of A; e.g., based on
preferences, obligations, sensitivity to causal outcomes, integrity, or respect. It also reﬂects
aspects of the moral rationalist project of determining universal a priori principles for morality
(e.g., Kant’s categorical imperative). Nevertheless, there are two main problems which distorts
a complexity analysis of rules such as GR3. The ﬁrst is that it may presuppose a great variety
with regard to the cognitive capacities of agents, the ways such capacities enable features
of an agent’s general behavior, and in turn, the cognitive capacities and features of general
behavior that are shared between agents. The categorical imperative, for instance, assumes an
idealized form of autonomy, in the sense that agents act according to their own self-imposed
rules (without any external inﬂuence). Similarly, as noted in our discussion of “the harm
principle”, the complexity of directing one’s general behavior is proportional to the space
of actions one can do. In the context of liberal democracies, it may refer to a cluster of
capacities that are more or less shared among “generally competent” human adults (e.g., to
act with intention, understanding, and without the controlling inﬂuence of external factors).
In this context, a complexity analysis of G3 thus presupposes that we have a computational
speciﬁcation of an adult human being.
The second problem is game-theoretical: there may be great variance with regard to what
one expects of other agents. Here, the conﬂict between contractarians (following Hobbes) and
contractualists (following Rosseau) comes to play, as they diﬀer in their understanding of
“the original position” and its relation to morality. The former starts from the assumption
that human nature is primarily driven by self-interests, which makes morality a problem of
cooperation; it would only be rational to be moral (cooperate) if it increases the joint interest.
The latter has a more optimistic view, in the sense that it starts from a basis of mutual
respect: morality are the results of binding agreements from a standpoint that recognizes each
rational autonomous agent’s equal moral importance. This conﬂict may create a signiﬁcant
variance with regard to computational resources. For instance, if you are completely selﬁsh,
and you expect everyone else to be completely selﬁsh as well, it will make your personal GR
relatively simple to implement: you do not help others in need because others would not help
you. By contrast, if you believe in every autonomous being’s equal moral importance, you
might help others, not in light of a joint-interest (e.g., direct or indirect reciprocity), but due
to a reasoning process which led you to conclude that helping others is what free and equal
citizens should do.
5.1.3. Moral Behavior in Strategic Games
While it is hard to imagine a complexity analysis of general rules that is able to escape
the extreme variances of general behavior and behavioral expectations, insights from game
theory can shed light on some of its aspects. In 1950, mathematician John Nash famously
proved that for every ﬁnite n-player game, there exists at least one ﬁxed strategy proﬁle
— a Nash equilibrium (NE) — in the sense that no player can beneﬁt from changing their
strategy (Nash et al., 1950). In the seven decades that has followed, game theory and its many
extensions have become a standard tool for mathematical modeling in biology, social science,
and economics (Smith and Price, 1973; Nowak, 2006; Holt and Roth, 2004). In philosophy,
it has been instrumental in theories of social norms as mixed-motive games turned into
coordination games (Ullmann-Margalit, 2015; Bicchieri, 2005), and to aid the contractarian
36

--- Page 37 ---

Player 2
Cooperate
Defect
Player 1
Cooperate
(R, R)
(S, T)
Defect
(T, S)
(P, P)
Table 2: Canonical payoﬀmatrix for the Prisoner’s dilemma, where T > R > P > S.
project of deriving morality from self-interest (Gauthier, 1987; Skyrms, 2004).
From a game-theoretical standpoint, it is interesting to ask: what computational resources
does an agent need in order to decide how to act? Using the Prisoner’s Dilemma (Table
2) as the prototypical case, the most eﬃcient approach would be to follow one of two pure
strategies:
(S1) Pure defection — Always do the selﬁsh action, regardless of whether your own payoﬀ
(self-interest) would have been higher if you did not.
(S2) Pure cooperation — Always do the altruistic action, regardless of your own potential
loss.
Assuming that an agent can, in every relevant circumstance, determine what it is to
cooperate or defect, (S1) and (S2) are equally eﬃcient, O(1). In some sense, (S1) can be seen
as a naive interpretation of behavior in Hobbes’ state of nature (Hobbes, 1651), whereas (S2)
represents behavior in Kant’s hypothetical Kingdom of Ends (Kant, 1785). Since an agent’s
life in the former is “nasty, brutish, and short”, it lacks the mechanisms that enable mutual
ﬂourishing.64 In the latter, agents treat each-other as ends (as opposed to means), which
allows them to prosper. Of course, agents who adopt (S1) will miss out on the game-theoretic
rationality of morality itself, i.e., when the payoﬀs for mutual cooperation is larger than mutual
defection. Similarly, agents adopting (S2) might perform extreme and seemingly unnecessary
acts of self-sacriﬁce (in Kantian terms, violating obligations directed to oneself). Furthermore,
in mixed populations, cooperative agents will be targeted by free-riders who exploit the
good-will of others (Fehr and Fischbacher, 2004), unless there are mechanisms for punishment
(Fehr and G¨achter, 2000). Still, from a machine ethics perspective, (S2) deserves attention as
it captures aspects of divine command theory and legal positivism; i.e., given that humans
have gathered exhaustive moral knowledge of a certain domain (e.g., determined the actions
that support human well-being) and are able to implement it as input-action-commands. For
instance, if one adopts the view that machines are merely tools for human ends, extreme
forms of machine-sacriﬁce or machine-exploitation may be irrelevant.65
While (S2) might have some appeal for the prospect of moral machines, it makes less sense
from a human perspective. Simply put, people are less likely to cooperate if there are no
self-directed incentives (even Kant’s Kingdom of Ends assumes some form of obligations to
oneself). The more common strategy, and the most extensively studied strategy in economy
and behavioral ecology, is to be rational in the sense of maximizing self-interest:
64Based on his idea of the state of nature, Hobbes famously argues that people are better oﬀsubmitting
themselves to an absolute political authority, which has the power to protect people from themselves.
65From this point of view, it also seems absurd to conceive of moral machines driven by self-interest.
37

--- Page 38 ---

(S3) Mixed rationality — Do whatever maximizes self-interest.
The strategy is mixed as opposed to pure, in the sense that it can be represented as
a probability assignment to each pure strategy. It is a more sophisticated version of (S1),
since it takes the potential self-interested beneﬁts of cooperation into account (Axelrod and
Hamilton, 1981). However, what constitutes a rational choice, following (S3), is ultimately
dictated by features of the game. In a one-shot prisoner’s dilemma (played only once), if both
players know that they will never play again, the dominant strategy and only possible NE is
to defect. No matter of what Player 2 player does, Player 1 will be better oﬀdefecting, and
vice versa: since neither can retaliate against the other, none of them have anything to lose
by defecting. By induction, the same holds for the iterated prisoner’s dilemma, given that it
is commonly known that the game is played precisely n times (Luce and Raiﬀa, 1989). If
the number of rounds are unknown or inﬁnite, however, cooperation among rational players
can emerge in non-cooperative situations; defection may still be a NE, but not a strictly
dominating strategy (Aumann, 2016). It might seem counter-intuitive that merely knowing
how many rounds one will play should make such a big diﬀerence for the choice of action; nor
does it reﬂect what humans do in experimental settings (Heuer and Orland, 2019). Several
solutions to this “paradox” have been proposed. Radner (1986) showed that relaxing the
strict notion of rationality (e.g., being satisﬁed by a ‘close enough’ payoﬀ) allows for longer
periods of cooperation. Kreps et al. (1982) demonstrated similar results on the basis that
agents have incomplete information about the options, motivations, or behaviors of other
players. A more interesting solution from a complexity perspective was provided by Neyman
(1985), who showed that cooperation becomes an equilibrium if the players have suﬃciently
small memories. More speciﬁcally, if agents are modeled as ﬁnite automata with a ﬁxed size
s, and play n number of games, mutual cooperation becomes a ﬁxed point if 2 ≤s < n.66
Intuitively, since players do not have the memory needed to enumerate to n, they in eﬀect
treat is as an inﬁnite game.
This generates an insight which is contrary to the complexity results discussed thus far.
While the results in section 4 indicate that an agent cannot do what is morally optimal due
to their own computational constraints, these game-theoretic considerations demonstrate how
agents behave morally (cooperate) due to a lack of certain computational resources: e.g., by
restricting space complexity Neyman (1985), information Kreps et al. (1982), or rationality
Radner (1986). This may suggest another role for normative theory which contradicts what
was argued in 3.1.2: the purpose of NT is not to produce moral optimality as such, but rather
to provide action-guidance in novel and complex situations. The results may be suboptimal,
either from a rational or moral perspective, but they do work, given the constrained resources
of agents. This idea has been extensively explored by Alexander (2007), who claims that
moral principles have emerged to provide ‘fast and frugal heuristics’ which enables agents
with bounded cognitive abilities to coordinate on suboptimal outcomes.
Nevertheless, it is also an optimistic form of question-begging: it already assumes that
the moral norms and principles that foster cooperation leads to some non-trivial joint beneﬁt
(e.g., contractarian perspective), while the agents themselves might lack the cognitive abilities
66See Aaronson (2013) for an interesting discussion of this paradox in the context of computational
complexity.
38

--- Page 39 ---

to verify the beneﬁt. Consequentially, the joint beneﬁt becomes its own optimistic ﬁxed
point unless it is compared to some other alternative (or the de facto optimal). Like divine
command, legal positivism, or natural law, it might ask agents to blindly follow rules because
“they are good”, while oﬀering no proof of why those rules are better than other alternatives.
Of course, from an evolutionary perspective, it may provide informative post-hoc solutions
to the problem of altruism: how is it that many organisms exhibit altruistic behaviors —
increasing other agents’ reproductive potential by reducing their own — given that natural
selection favors the survival of the ﬁttest? By observing cooperative behavior in various
organisms, one might conclude that altruistic behaviors could not preserve unless they oﬀered
some alternative reproductive beneﬁt (e.g., kin and selection, direct, indirect, and network
reciprocity (Nowak, 2006)). In the same vein, one might justify “fast and intuitive” moral
behaviors because they compress moral wisdom from evolutionary or cultural history. However,
this view relies on an optimistic conservatism: that there are good reasons why things are as
they are, even if we may not know these reason to a full extent (we will return to this issue in
section 5.3).67
5.1.4. Moral Behavior in Strategic Games with Incomplete Information
Instead of ﬁnding computational constrains that enable cooperation, one can investigate
the factors that hinders the maximization of rational self-interest in more realistic game-
theoretic settings. For instance, through the work on Bayesian games by Harsanyi (1967), we
can model scenarios with incomplete information:
(S4) Bayesian rationality — Do whatever maximizes expected self-interest.
Bayesian games relax the underlying assumption in classic game theory: that features of
the game, e.g., the actions and payoﬀfunctions for every player, are known by all players.
For instance, in the original formulation of NE, it is assumed that each player knows the
equilibrium strategies of the other players. In a Bayesian game, players instead have beliefs
about the features of the game, which may involve beliefs about others’ beliefs of features of the
game. This naturally leads to inﬁnite hierarchies of higher-order beliefs (beliefs about beliefs
about beliefs ad inﬁnitum), which are cumbersome to approach mathematically. Harsanyi’s
model of Bayesian games partly solves this through the notion of type, which summarizes a
player’s beliefs about the nature of the game (and her inﬁnite hierarchy of beliefs).68 If it is
assumed that the private elements of players are drawn from a commonly known distribution,
the inﬁnite regress is resolved, which enables a Bayesian equilibrium analysis; a speciﬁcation of
the behavior of each player that is a best-response to what the player believes is the behavior
of the other player (i.e., a best-response to the other players’ strategies given the players own
type).
In practice, however, Harsanyi’s setting is unfeasible to model in multi-agent systems
where agents interact with unknown agents. How can we be sure that a stranger draws from
the same known probability pool as ourselves? In autonomous agents and multi-agent systems
67As an interesting thought-experiment, if Thomas Hobbes were alive in the 21st century, would he still try
to convince democratic societies to submit their power to a sovereignty?
68See Mertens and Zamir (1985) and Brandenburger and Dekel (1993) for two complementary constructions
of Harsanyi’s model of inﬁnite hierarchies of beliefs.
39

--- Page 40 ---

research, nested beliefs are instead investigated through the concept of recursive reasoning.69
Methods for recursive reasoning typically approximate nested beliefs down to a predetermined
recursion depth. For instance, if A is trying to predict the behavior of B, A predicts B’s next
action by simulating B’s decision based on what A beliefs about B. This, in turn, requires
a prediction of A’s behavior from the perspective of B, based on what A thinks B believes
about A, etc. Recursion is then terminated at a ﬁxed depth by drawing the action prediction
from some probability distribution (e.g., a uniform distribution). The bottom-level prediction
at 0 is then passed up to the higher level (0 + 1), where the optimal action is chosen, and
then passed recursively up to the highest level (l) where A makes it de facto choice.70 One
prominent version of the aforementioned process is the Interactive POMDP (I-POMDP),
which extends a POMDP (discussed in section 4.3) by adding models of other agents into the
state space (Gmytrasiewicz and Doshi, 2005). In short, for agent A to pick the optimal action,
A has to solve the I-POMDP of B for each model of B, which involves solving the I-POMDP
for each model B has of A, all the way down to the 0th level, where models of other agents
are standard POMDPs (i.e., they are “noise” drawn from some probability distribution).
While several exact and approximate solutions for I-POMDPs have been oﬀered,71 they
are, for obvious reasons, hard to compute. Since the 0th level constitutes POMDPs which the
agent can recursively use to solve POMDPs for the higher levels, the complexity of solving
an I-POMDP is equal to solving O(N l) POMPDs, where N is a bound on the number of
models the agent considers at each level, and l is the recursion depth (Gmytrasiewicz and
Doshi, 2005). For instance, for an I-POMDP containing 4 agent models and 4 levels, this
will amount to solving 256 POMDPs, which, individually, are PSPACE-complete for ﬁnite
time horizons (Papadimitriou and Tsitsiklis, 1987). More broadly, Bernstein et al. (2002)
studied a number of decentralized control problems — where multiple agents cooperate to
control a process, each with possibly diﬀerent information about the state — and proved
that both decentralized MDPs and POMDPs are NEXP-hard; i.e., at least as hard as the
hardest problems that are solvable in non-deterministic exponential time. More speciﬁcally,
while POMDPs and I-POMDPs are equally targeted by the “curse of history” — in the sense
that the space of policies is proportional to the number of possible future beliefs given by
the time horizon — since I-POMDPs may involve a greater number of (potentially nested)
beliefs, they are further impeded by the “curse of dimensionality”, as the complexity of belief
representation is proportional to the dimensions of the belief structure.
But history and dimensionality are not the only curses in strategic interaction. For
instance, if players are uncertain about other players’ payoﬀfunction, there is an inherent
tension between prediction and rationality. Foster and Young (2001) demonstrated that there
are situations in which it is impossible for rational players to play optimally with respect to
their beliefs, while simultaneously having correct beliefs. The reasoning is simple: if A tries
to predict the action of B at t2, and A must take an action at t1 which B can observe, B’s
observation might invalidate A’s prediction of B’s behavior at t2. Furthermore, in certain
69See section 4.5 in (Albrecht and Stone, 2018) for a recent survey on recursive reasoning methods.
70In fact, the famous minmax algorithm for zero-sum games is a special variation of this method, where the
opponent B’s evaluation function is taken to be the inverse of player A (Campbell and Marsland, 1983).
71E.g., using methods like Monte Carlo sampling (Doshi and Gmytrasiewicz, 2009) or model equivalence
(Rathnasabapathy et al., 2006).
40

--- Page 41 ---

settings, higher-order reasoning may not provide any additional beneﬁts. In fact, the studies
by de Weerd et al. (2013, 2017) demonstrates settings — e.g., sequential negotiation and
rock-paper-scissors — where reasoning levels higher than 2 do not oﬀer any notable advantages
for computational agents.
Nevertheless, while the intractability results for recursive reasoning have a direct impact for
computational systems, it remains an open question how humans reason in similar problems,
and consequently, how machines should interact with humans in a robust way. These questions
have been extensively explored in the experimental psychology on strategic interpersonal
situations, often in combination with the notion of “theory of mind” (Yoshida et al., 2008).
For instance, in two experiments with human participants, Hedden and Zhang (2002) showed
that participants employ a short-sighted “default model” about the other players minds, which
were dynamically adjusted in light of new evidence. In addition, the “cognitive hierarchy”
model proposed by Camerer et al. (2004) suggests that players presume that their own strategy
is the most sophisticated, in the sense that they use the best-response at recursion level l
to predict the behavior of players at level l −1 (i.e., one step ‘higher’ in the level of nested
beliefs). By ﬁtting their model with a large corpus of empirical data from a variety of games,
they found that humans, on average, reason at recursion depth 1.5.72
Given the many conﬂicting dimensions of the subject matter, it seems diﬃcult to arrive at
any general conclusions about whether and to what extent computational constrains aﬀect
strategic interactions in moral contexts. However, it tentatively indicates a trend, namely
that optimality is traded for eﬃciency (or mere feasibility) in light of information availability
(about the state space and of other players), bounded rationality (e.g., memory and recursion
level), and game setting (e.g., one-shot or iterated, stochastic or deterministic). Intuitively,
the complexity results could support the appeal of pure strategies such as S1 and S2: in
complicated situations, it is easier to simply believe that everyone is of a certain type (e.g.,
selﬁsh or altruistic). It could also explain why it is easier to cooperate “locally” (e.g., in
smaller groups of friends), where features of the games are common knowledge; a mutually
shared goal (e.g., maximization of joint interest), and shared mechanisms for detecting and
punishing free-loading.73 Similarly, it also shows the inverse: why it is diﬃcult to achieve
cooperation in bigger populations, where game features are not shared, and agents do not
know what to expect from each-other.
5.1.5. Computing Moral Equilibria
Perhaps the most interesting part of game theory from a moral computational perspective
is not to ask about the resources an agent needs in order to decide how to act, but rather,
to ﬁnd strategies that maximize the interest of everyone (e.g., given that everyone were to
follow the same strategy). This is interesting for two reasons. First, from a moral point of
view, it would roughly correspond to the general-purpose rules discussed in section 5.1.2, e.g.,
72However, the view that human recursive reasoning is “pessimistic” — i.e., at a relatively low level of
recursion, and based on underestimating one’s opponent — has been contested by Goodie et al. (2012), who
found settings where all participants engaged in the highest available level of reasoning in both competitive
and simple settings.
73In turn, cooperative groups may beneﬁt from the “wisdom of the crowd” phenomenon (Yi et al., 2012),
where aggregations of multiple solutions performs better than individual solutions.
41

--- Page 42 ---

GR and CI. That is, if some action-rule (or strategy proﬁle) is a consistent best-response to
every other action and leads to some non-trivial mutual beneﬁts, it would be attractive for
a moral community to ﬁnd those rules. Second, these general-purpose rules would in turn
correspond to the typical solution concepts used in game theory — namely Nash equilibria —
with properties that are attractive from a moral standpoint (e.g., maximizing joint interest).
It is thus natural to ask: how diﬃcult is it to compute a Nash equilibrium? Already in
1928, v. Neumann (1928) provided the Minmax Theorem, which entails that equilibrium
in 2-player zero-sum games can be computed in polynomial time by linear programming
(Khachiyan, 1979). For non-zero sum games of at least two players, however, the problem is
proven to be PPAD-complete (Chen et al., 2009). PPAD, introduced by Papadimitriou (1994),
is the class of function problems solvable by a non-deterministic TM in polynomial time
where a solution is guaranteed to exist on the basis of the parity argument on directed graphs
(“PPAD”). The parity argument is based on the graph-theoretical insight that the number of
nodes that touch an odd number of edges is even in all ﬁnite undirected graphs (this deﬁnes
the PPA class, which contains PPAD). A similar insight holds for directed graphs: given a
directed graph and a source (a node without predecessors), there must be a node at “the end
of the line” which lacks successors.74 What is special about the PPAD complexity class is that
it reﬂects what is special about NE: since there always exist a NE (Nash, 1951), the answer
to the decision problem “does there exist a NE for this game?” is always yes, and therefore,
it cannot be NP-hard. Similarly, it also reﬂects what is special about Brouwer’s ﬁxed-point
theorem: for any continuous function f that maps a compact and convex Euclidean space to
itself, there exists at least one point x∗such that f(x∗) = x∗. By analogy: if you are standing
in a region and unfold a map of the same region, assuming that there are no holes in the
map, at least one point of the map will correspond to your location. But simply knowing that
such a point exists, does not necessarily make it easy to ﬁnd it. If we assume that one can
eﬃciently check whether a certain point on the map is in fact one’s location, the localization
problem can be solved in non-deterministic polynomial time (NP membership). By the same
reasoning, if one can eﬃciently verify whether a strategy proﬁle is a best-response or not, the
problem of ﬁnding a NE is in NP (which, in turn, contains the PPAD class).
However, if the NE should have any special properties — e.g., such that it maximizes
the sum of the player’s utility, or everyone obtains an expected payoﬀof at least some
number — the problem becomes NP-complete (Gilboa and Zemel, 1989).75 Conitzer and
Sandholm (2008) strengthened these results and proved that the egalitarian optimization
problem (e.g., maximizing mutual payoﬀ) is inapproximable; i.e., it is impossible to ﬁnd an NE
that approximates the maximum joint payoﬀin polynomial time. In fact, optimal NE is one
of many known NP-hard problems related to NE that are also hard to approximate (Austrin
et al., 2013): e.g., computing whether there is more than one NE, or ﬁnding NE with minimal
support.76 More precisely, while a linear-time algorithm can obtain 1/2-approximations of
74The “end-of-the-line” problem is a paradigmatic PPAD-complete problem.
75This can be proved by reducing it to the problem of ﬁnding a clique of size k in an undirected graph
(Gilboa and Zemel, 1989). For instance, ﬁnding a clique of size 3 means ﬁnding 3 nodes that all are connected
to each-other.
76The minimal support problem asks: for a number k ≤1, is there a NE in which players use at most k
strategies with a positive probability?
42

--- Page 43 ---

the optimal NE (Daskalakis et al., 2006), achieving approximations better than 1/2 is as hard
as the planted clique problem, which in turn may be solved in quasi-polynomial time (Lipton
et al., 2003).77
Naturally, in situations with incomplete information or stochastic dynamics, things may
get even harder. While it remains PPAD-hard to ﬁnd mixed-strategy equilibrium in Bayesian
games due to the fact that normal-form games are special cases of Bayesian games, Conitzer
and Sandholm (2008) showed that, even in symmetric 2-player Bayesian games, it is NP-hard
to determine whether the game has a pure-strategy Bayesian equilibrium. By contrast, one
can determine the existence of pure-strategy NE in normal-form games in polynomial time by
simply checking whether any combination of pure strategies is a NE. However, this procedure
is unpractical in Bayesian games, since the space of strategies grows exponentially with the
number of types, which contains the private information of players preferences. In addition,
Conitzer and Sandholm (2008) also demonstrated PSPACE-hardness for checking whether
there exists pure-strategy NE in repeated games with probabilistic state transitions — also
called “Markov games”, as they extend MDPs to include multiple decision-makers — and
that the problem remains NP-hard in ﬁnite games.
Although NE constitutes the most extensively studied solution concept in game theory, it
is not the only one that is useful from a moral perspective. A prominent alternative is the
correlated equilibrium (CE) introduced by Aumann (1974, 1987). In simple terms, CE can be
seen as a result of a commonly shared Bayesian rationality: it is simply a maximization of
utility given the player’s information. In contrast to NE rationality, CE does not assume that
players know that other players play their action as it is dictated by the NE, nor that each
player know the strategies of others. Instead, an equilibrium is simply that no player, based
on what they know (privately or commonly), can expect a higher return if they deviate from
their strategy. A useful analogy is to imagine a situation where players choose an action by
observing a random event: in mixed strategy settings, the event is assumed to be independent
for each player, while in correlated settings, they may not be. For instance, player A and B
might privately observe a correlated signal — e.g., two traﬃc lights — which recommends
A to wait and B to go. If the signals are drawn from a correlated distribution, neither A
nor B would want to violate the signal’s recommendations (as running a red light might
cause them to collide). As such, CE is a general distribution over strategy proﬁles, whereas
mixed strategy NE is a distribution over the space of “uncorrelated” strategies (independently
distributed over each player). Since every mixed NE can be deﬁned as the product of the
player’s mixed strategies, it follows that NE is in fact a special case of CE; and that every
game has a correlated equilibrium.
Apart from being guaranteed to always exist, CE is attractive for multiple reasons. It
seems to emerge in natural settings where NE does not (Hart and Mas-Colell, 2000).78 Unlike
NE, it is more apt to accommodate the role of external factors that are decisive for the
outcome, e.g., by following the recommendations of trusted sources. From a moral perspective,
CE captures many situations — e.g., in moral or legal rule-following — where it is clearly
77Here, the planted clique problem is used as a hardness assumption, as it is conjectured that no polyno-
mial time algorithm can, better than chance, distinguish planted cliques from random graphs (Hazan and
Krauthgamer, 2011).
78See also chapter 7 in Cesa-Bianchi and Lugosi (2006).
43

--- Page 44 ---

incentivized to not deviate from the prescribed action (e.g., following traﬃc rules). Last but
not least, CE are easier to compute than NE. Since correlated equilibria can be deﬁned by a set
of linear inequalities (Hart and Schmeidler, 1989) — and does not have to be based on Nash’s
result — the problem of ﬁnding an CE can be solved by linear programming, and is therefore
computable in polynomial time for games with any number of players (Gilboa and Zemel,
1989). Papadimitriou and Roughgarden (2008) demonstrated that there are polynomial-time
algorithms for computing an arbitrary CE for many natural classes of succinctly representable
multiplayer games, including polymatrix games, graphical and hypergraphical games, and
scheduling games. Unfortunately, while any CE seems easy, Papadimitriou and Roughgarden
(2008) also show that in nearly every class of succinct games, it remains NP-hard to compute
a CE that maximizes the expected joint payoﬀs.
Besides these intractability results, one might also question the relevance of computing
morally good equilibrium. Of course, at system-level, they provide indispensable analytical
tools for modeling and measuring intricate behavioral dynamics. For instance, the price of
anarchy measures how the joint welfare of a system degrades due to selﬁshness by dividing the
welfare value for the “worst-case” decentralized equilibrium with the welfare at its optimal
centralized conﬁguration (Koutsoupias and Papadimitriou, 2009).79 But these tools might
be of less use from the perspective of individual agents. We can imagine that an agent has
managed to compute a “golden rule” strategy proﬁle (e.g., a set of action-rules) which for any
possible interaction, maximizes the joint beneﬁt of her society. Still, her society would only
ﬂourish given that the other agents in the society followed the strategy proﬁles as ﬁxated
by her equilibrium computation. She might try to convince other agents to follow her lead
by an appeal to her extraordinary computational powers80; she might, as Kant, argue that
it is imperative for the will of rational beings; that it is, following Hobbes, imperative for
the maximization of expected self-interested; or she might simply hope that everyone else
— e.g., in virtue of shared rational capacities and correlated distributions — computes the
corresponding set of strategy proﬁles. Given the adequate means, she might enforce the
ﬁxation of the equilibrium, e.g., by punishing everyone who did not follow their strategy
proﬁle. At the most extreme, we could imagine a super-intelligent Leviathan that has —
even adjusting for any potential welfare losses due to the restrictions of freedom and the
punishment of dissidents — computed that the joint welfare would still be optimal if strategy
proﬁles were enforced by force.
The main point is that solutions to decentralized cooperation problems require, in some
non-trivial sense, centralized features to work in practice. While shared cognitive capacities,
rationality, communication (Crawford and Sobel, 1982), and information (e.g., from correlated
distributions), can certainly make it easier for agent’s to collectively arrive at morally attractive
equilibria, the complexity of cooperation is distorted by a vast range of features in the local
and agent-speciﬁc context; e.g., more or less overt power-dynamics (e.g., via legal, political,
and religious institutions), psychological heuristics (such as trust, shame, and guilt), and
79Conversely, the price of stability gives a ratio of the diﬀerence between “best possible” decentralized
equilibrium and the optimal centralized solution.
80Following a recent proposal from Cummings et al. (2016), coordination complexity can be measured as
the minimum information a centralized coordinator with complete knowledge of the game needs to publicly
signal in order to coordinate players towards a nearly optimal solution.
44

--- Page 45 ---

conﬂicts between in-group/out-group preferences.
Furthermore, in the real-world, it is often not clear what kind of game we are playing, or,
whether we are even playing a game at all. Games can be cooperative or non-cooperative,
discrete or continuous, one-shot or repeated (e.g., played with strangers or friends), simulta-
neous or sequential, zero or non-zero sum, symmetric or asymmetric, have varying degrees of
imperfect and incomplete information, have varying population sizes, all while allowing for a
potentially inﬁnite set of diﬀerent strategies (e.g., speciﬁc action-combinations in sequential
Markov processes of unknown length). In other words, even if we assume “centralized features”
(such as shared cognition, memory, and views on rationality), game-theoretic models — and
thus, the applicability of equilibria solutions — are heavily underdetermined by data. While
small and isolated groups might tend towards cooperation — e.g., by easily recognizing the
maximization of a joint interest; having mechanisms for detecting free-loading; knowing that
others share the same information about the game; etc — it might take millennia for larger
societies to become egalitarian, e.g., as agents cannot agree on the nature of the coordination
games they are playing (for instance, due to conﬂicts between in-group preferences).81
5.1.6. Designing Moral Systems
The strong indeterminacy of game-theoretic models, along with the hardness of computing
good equilibria in such models, suggests that it may be easier to foster collective welfare
by design; i.e., constructing systems where tractable and morally praiseworthy equilibria
naturally arise (as opposed to ﬁnding good equilibria in arbitrary settings). This intuitively
reﬂects the relationship between legality and morality. Although agent’s may follow rules due
to moral reasons (e.g., they lead to a joint beneﬁt if everyone followed them), they may be
further incentivized to do so if there are mechanisms for blame, responsibility, and punishment.
Similarly, institutionalized moral rules (e.g., “do not harm others”), may by design reﬂect
natural strategy proﬁles that are easy to understand, morally justify, and apply in practice.
Similarly, in economics, the aim of mechanism design (or “reverse game theory”) is to design
decentralized economic mechanisms that achieve desired objectives, e.g., to optimize social
welfare (Hurwicz and Reiter, 2006). In algorithmic game theory, this has further motivated
the ﬁeld of algorithmic mechanism design, which seeks to design games that combine features
that are attractive from a computational and game-theoretical perspective, with the prime
example being games with good worst-case equilibria (i.e., a low price of anarchy) that can
be computed in polynomial time (Nisan and Ronen, 1999). Essentially, since it is diﬃcult
for computational agents to ﬁnd and follow moral equilibria in open-ended environments,
complexity considerations can help to inform the design of decentralized systems that are
morally attractive.82
In summary, our investigation into the generality of moral rules found that:
(1) Although moral rule-following in human contexts might appear to be computationally
81To be clear with terminology, coordination games conventionally refer to games where it is optimal for
players to cooperate, e.g., as in Stag Hunt or Battle of the Sexes. As such, they diﬀer from anti-coordination
games like Hawk-Dove (chicken), where it is optimal for players to play diﬀerent strategies.
82Some notable examples of algorithmic mechanism design include traﬃc routing (Roughgarden, 2005;
Roughgarden and Tardos, 2002), auction design (Cai and Papadimitriou, 2014), and internet problems
(Feigenbaum and Shenker, 2004).
45

--- Page 46 ---

simple, they rely on shared cognitive capacities and agreements between “generally competent”
human agents (often along with the institutions that ensure their just application). While
rules such as “do not X” might reduce space complexity, it is only by restricting a potentially
inﬁnite space of actions that autonomous agents can do.
(2) If computational agents should follow general moral rules in a way that ensures their
own normative justiﬁcation — e.g., being sensitive to other beings via rational agreement
or by maximizing joint interest — results from algorithmic game theory indicates that it
requires solutions to intractable problems (with a few noteworthy exceptions). Note that
these intractability results hold for salient games, in the sense that agents are assumed to
have a model of the game they are (supposedly) playing, even if information about aspects
of the game may be incomplete. In many real-world situations, the validity of such models,
given that they are obtainable at all, might still be severely underdetermined by data (i.e.,
the model might fail to capture the essential real-world dynamics). In other words, if we
assume that moral rule-following can be mathematically modeled as following strategies in
games, the solution to such games may be decidable (e.g., by computing equilibria), although
in general not polynomial-time tractable. It is also important to stress that these challenges
are far from unique to deontology, but aﬀects any moral theory with generality ambitions
that seeks to account for multi-agent dynamics. Thus, it naturally targets consequentialism
(as it centers on how outcomes aﬀect others), but not theories such as divine command and
legal positivism.
(3) Given the hardness of ﬁnding good equilibrium, the problem of computing the beliefs of
others’ (e.g., nested beliefs), the indeterminacy of game models, and the fact that cooperation
may emerge due to a lack of certain computational resources (e.g., information, memory, or
self-interest), the investigation also suggests that moral rules and principles might better
serve as ‘fast and frugal heuristics’ that guide agents with bounded cognition in open-ended
environments towards suboptimal but feasible results. Somewhat ironically, this might in
turn make “naive” moral strategies (e.g., “when in doubt, be altruistic”) viable or even
necessary from a computational perspective; although without oﬀering any game-theoretic
explanation as to why they are viable from a self-interested perspective.83 Furthermore,
instead of computing moral equilibria in complex environments, one promising alternative
approach is to use complexity constraints and equilibrium measures to guide the design of
decentralized systems which are attractive from a moral perspective.
5.2. The Complexity of Moral Logic and Semantics
Another way to analyze the computational complexity of deontology is to look at the syntax
and semantics of formal languages that aim to capture moral reasoning and rule-following.
For instance, we might note that moral rules expressed in natural language have certain
logical characteristics, such as “given fact a, action b is obligatory”. Consequently, we might
83To illustrate this point, we can imagine two populations — A and B — that have converged on the
same set of cooperative behaviors that yield optimal joint welfare. In population A, the equilibrium was a
result of repeated interactions between self-interested individuals over several thousands of iterations. In
population B, the equilibrium was already ﬁxed at start, as agents were told by their mothers to “always be
kind”. The point is that while agents in A understand the self-interested rationale behind cooperation, they
are nevertheless equally well-oﬀas agents in B, who are oblivious to the same rationale.
46

--- Page 47 ---

imagine that it is possible to construct a machine that has a number of norms (x, y) stored in
memory which relate facts (x) to obligations or permissions (y). The question is, are there any
complexity considerations that might curtail such a machine’s practical success for reasoning
about norms (this will be the topic of section 5.2.2)? More broadly, how does the expressive
power of a logic used for moral reasoning relate to complexity classes, e.g., in terms of the
problems it can describe (the topic of section 5.2.1)? In this section, we will discuss such
problems along with some more fundamental issues in semantics (section 5.2.3).
5.2.1. Decidability and Descriptive Complexity
Any discussion of the complexity of logic would be incomplete without reiterating the
classic results that make up the very foundations of computability. In 1929, Kurt G¨odel’s
completeness theorem establishes that in ﬁrst order logic (FOL), semantic truth corresponds
with syntactic provability; i.e., there are complete, sound, and eﬀective deductive systems
for FOL (G¨odel, 1930). Two years later, G¨odel gave his two celebrated incompleteness
theorems (G¨odel, 1931), which shows that any consistent formal system capable of carrying
out elementary arithmetic — e.g., using natural numbers, addition, and multiplication — is
incomplete (ﬁrst theorem),84 and that such a system cannot prove its own consistency (second
theorem).85 Inspired by G¨odel’s theorems, Turing (1936) and Church (1936) independently
provided negative answers to the “Decision problem” (Entscheidungsproblem) for FOL;
Church’s proof utilizes the undecidability of checking the equivalence of two expressions in
the λ-calculus, whereas Turing constructs the halting problem for Turing machines. Their
results establish that no decision procedure exists that can decide whether arbitrary FOL
formulas are logically valid.86 On the other hand, propositional logic (PL) — which, unlike
FOL, excludes relations and quantiﬁers — is decidable. For instance, the satisﬁability problem
for propositional logic (SAT) was the ﬁrst decision problem proven to be NP-complete (Cook,
1971), and has since remained at the center of computational complexity theory. Using Cook’s
results from SAT, Karp (1972) proved NP-completeness of 21 further problems, which not only
demonstrated the intuitive appeal of the NP-class, but also that many natural computational
problems are intractable.
However, instead of determining the resources needed to check whether some input satisﬁes
some property X, we can ask, what is the complexity of expressing X? The latter question is
central for the ﬁeld of descriptive complexity theory, which deﬁnes complexity classes in terms
of the type of logic required to express the languages in them. In fact, due to a wealth of results
from descriptive complexity, it turns out that expressing and checking are intimately related.87
The ﬁrst major result in the ﬁeld was Fagin’s theorem (Fagin, 1974), which established that
NP is exactly the set of properties that can be expressed in existential second-order logic
(SO∃), which unlike FOL, has the power to existentially quantify over properties and relations.
In other words, every query that is computable in NP (including NP-complete problems) is
84A system — or rather, a theory in the mathematical logical sense, i.e., a set of sentences in a formal
language — is consistent if it does not lead to contradictions. An axiomatic system is complete if any statement
in the systems language is provable from the axioms. Incompleteness thus entails that there are statements
which cannot be proved nor disproved in the system.
85The theorems were further reﬁned by Rosser (1936), who proved them without assuming ω-consistency.
86Validity means that true premises guarantee the truth of an argument’s conclusion.
87See Immerman (1998) for the deﬁnite introduction to descriptive complexity.
47

--- Page 48 ---

equivalent to a query in SO∃.88 Furthermore, since the complement of an existential formula
(quantifying over some members of a domain) is a universal formula (quantifying over all
members of a domain),89 it follows directly that co-NP is captured by SO∀, and unrestricted
second-order logic (SOL), which allows for both universal and existential quantiﬁcation, is
equal to the union of all classes in the polynomial hierarchy (PH). Other notable results
include the fact that FOL corresponds to the logarithmic time hierarchy (LH) as well as the
circuit complexity class AC0, linearly ordered FOL systems with a least ﬁxed-point operator
yields P (Immerman, 1982; Vardi, 1982),90 SOL with a transitive closure gives PSPACE
(Immerman, 1989), and SOL with a least ﬁxed-point corresponds to EXPTIME (Immerman,
1998; Abiteboul et al., 1997).
These results generate the wisdom that the expressiveness of a language is directly corre-
lated to the problems it can describe. However, it should be noted that, while computational
and descriptive complexity are intimately related, they also have some crucial diﬀerences. For
instance, one key incongruity is that, whereas descriptive complexity studies ﬁnite mathe-
matical structures, computational systems operate on ordered encodings of problems and are
thus able to enumerate objects which may be logically unordered. As an example, from a
logical perspective, we might see a set of nodes in an graph as undordered, but as soon as
it is transferred to the tape of a Turing Machine, it inevitably becomes ordered (and thus
exploitable for various forms of operations).91 Nevertheless, the fact that complexity can
be characterized in terms of expressibility — without reference to some abstract machine —
further establishes the natural appeal of the complexity classes. And for computational moral
rule-followers — e.g., systems performing queries over databases containing moral norms —
the consequences are profound yet somewhat clouded by its mere generality. For instance,
languages describable in FOL corresponds to AC0 (polynomial-size circuits of bounded depth),
which allows one to perform integer addition and subtraction but not multiplication. Adding
an operator which can compute the transitive closures of binary relations, on the other hand,
makes it possible to produce structures that can answer reachability queries (e.g., is it possible
to go from node A to node Z in n steps?). Perhaps most interesting is the intractability of
expressing queries which involve diﬀerent forms of quantiﬁcation over properties and relations
(and not just objects, as in FOL), which is seemingly intuitive in natural language. For
instance, even trivial moral queries of the type “For all observable facts, possible actions,
and obligations, is there some action which does not violate any moral obligations?”, might,
in the worst-case, only be expressible in intractable complexity classes (e.g., if we assume
that obligations are a relation between facts and actions). The point is, while quantiﬁcation
over properties and relations, transitive closure, and ﬁxed points oﬀer substantial expressive
powers to well-studied collections of formal systems, it also raises intractability concerns;
simply because language helps us to succinctly represent and communicate queries for moral
88See chapter 7.1. in (Immerman, 1998) for a detailed proof.
89This follows from the fact that ∃x¬P(x) is equavalent to ¬∀xP(x).
90In short, ﬁxed-point logics extend FOL with an operator which can construct ﬁxed points of relational
variables. For instance, if we view formulas with free relational variables as if they are determining maps on
the relation space, the operator can deﬁne ﬁxed points on this map.
91However, this incongruity does not hold for Fagin’s theorem, since SO∃can be used to declare the existence
of some desired order.
48

--- Page 49 ---

rule-followers, it does not necessarily make such queries easy to compute.92
5.2.2. The Complexity of Modal and Deontic Logic
One of the most widely used fragments of FOL is modal logic; the go-to logic for representing
necessity (□) and possibility (♦).93 From the mid 20th-century and onward, the standard
semantics for modal logic is the possible world approach,94 where □P means that P is true
in all possible worlds, and ♦P means that P is true in some possible worlds (assuming that
these worlds are accessible). One attractive feature of modal logic is that it, contrary to FOL,
is robustly decidable.95 However, although it is decidable, typical problems for modal logic
are in general not tractable. For instance, while the model-checking problem, which asks
whether a given formula is true with regards to a given state of a given Kripke structure96 is
solvable in linear time, the validity problem, which asks whether a formula is true in all states
of all Kripke structures is PSPACE-complete Ladner (1977). More precisely, Ladner (1977)
demonstrates that the validity problem for modal logic is PSPACE-complete for the systems
K, T, and S4, whereas it is NP-complete for S5.97 These results where extended by Halpern
and Moses (1992), who proved that the validity problem is PSPACE-complete for multi-agent
versions of K, T, S4, and S5 (i.e., a “join” of the logics used by at least two agents). The work
of Halpern and Moses (1992) also shows that, while the addition of a distributed knowledge
operator — allowing an “all-knowing” agent to combine the knowledge of everyone else —
does not alter the complexity, the addition of a common knowledge operator — allowing
everyone to know P, and that everyone knows that everyone knows ... that P holds — makes
the problem EXPTIME-complete.98
Naturally, similar intractability concerns plague other popular versions of modal logic. For
instance, Spaan (1993) showed that the PSPACE-completeness of the validity problem carries
over to the tense case (temporal logic), i.e., with the addition of operators expressing “it will
always be the case that...” and “it will always was the case that...”. Similarly, Sistla and Clarke
(1985) demonstrated that satisﬁability for Linear Temporal Logic (LTL, introduced by (Pnueli,
1977), with operators for “next” and “until” (excluding the past), is either PSPACE-complete
or NP-complete depending on the operators used.99 In general, PSPACE-completeness also
92See Aaronson (2013) for an interesting discussion of the related problem of “logical omnicience”, which
uses complexity considerations to challenge the view that if an agent knows certain facts, it also know every
logical consequence of those facts.
93Alternatively, since the main ideas of modal logic long predates FOL — e.g., Aristotle’s modal syllogisms
— it is arguably more accurate to describe modal logic as an expansion of propositional logic.
94The approach was originally suggested by Carnap (1947), and later developed to its modern day form by
Kripke (1963).
95For an in-depth exposition see Vardi’s report “Why is modal logic so robustly decidable?” Vardi (1997).
96A Kripke structure is a graph that represents reachable states as nodes, state transitions as edges, and a
labelling function that keeps track of the properties that hold in each state.
97For readers unfamiliar with modal logic, K, T, S4, and S5 refer to the choice of axioms and rules
that are added to the systems; e.g., K — the weakest version — only includes the necessitation rule (i.e.,
(|= P) =⇒(|= □P)) and the distribution axiom (□(P →Q) →(□P →□Q); T includes the reﬂexivity
axiom (□P →P) in addition to K; S4 and S5 includes T along with iteration axioms 4 (□P →□□P) and 5
(♦P →□♦P), respectively.
98See also Spaan (2016) for an exhaustive treatment of the complexity of modal logics.
99See Vollmer et al. (2009) for a more detailed study of the complexity of temporal and propositional
49

--- Page 50 ---

holds for the model-checking problem for several versions of LTL (Schnoebelen, 2002).
Perhaps more interesting for the prospect of moral machines is the complexity results
for variants of modal logics such as dynamic logic (DL, introduced by Pratt (1976)) and
deontic logic. DL adds the additional modal operators [a] and ⟨a⟩, which makes it able to
capture properties of program behavior; e.g., [a]P means that after performing action a, it is
necessary that P is true (i.e., a brings about P), and ⟨a⟩P means that it is possible that P
holds after a is performed (i.e., a might bring about P). Note that a might refer to an entire
program, which allows dynamic logic to formalize dynamics — e.g., transitions, sequences,
and results — of complex algorithmic systems of multiple programs. In turn, Propositional
Dynamic Logic (PDL, introduced by Fischer and Ladner (1979)) was developed to describe
correctness, termination, and equivalence of computer programs on the basis of PL (instead
of FOL, which was the basis of the ﬁrst version of DL (Pratt, 1976)). Interestingly, the
decidability of checking whether a formula F of PDL is satisﬁable can be secured by having
two sub-procedures running in parallel: one which enumerates all deducible formulas (R1),
another which enumerates the ﬁnite models of PDL and tests whether they satisfy the formulas
(R2). In this way, if F is satisﬁable, a model which satisfy F must eventually be found. If F is
satisﬁable, R2 will at some point answer “yes”, if not, R1 will at some point answer “no” (and
the procedure halts when either sub-process gives an answer). Nevertheless, although PDL is
attractive for formal veriﬁcation of program behavior, it is less attractive for computational
moral agents bounded by polynomial time, as SAT for PDL is EXPTIME-complete (Fischer
and Ladner, 1979; Pratt, 1980).100
Deontic logic (introduced by Von Wright (1951)), on the other hand, aims to capture the
logical features of moral concepts such as permissions (typically denoted by operator P) and
obligations (typically denoted by O). For instance, the axiom O(A →B) →(OA →OB)
states that “if it is obligatory that A implies B, then B is obligatory if A is obligatory”.
Likewise, Kant’s “ought implies can” can be expressed by OA →♦A. It should thus be no
surprise that deontic logic has been a popular framework for implementations in machine
ethics, e.g., for automatized ethical reasoning (Arkoudas et al., 2005; Wiegel and van den
Berg, 2009; Furbach et al., 2014; Malle et al., 2017b). However, compared to other versions
of modal logic, the computational complexity of deontic logic is relatively unexplored. One
reason is that the inherent complexity of (and relationship between) normative concepts —
e.g., of agency, right, responsibility, and commitment — may be drawn to arbitrary levels of
detail 101 Another reason is the problem of agreeing on the appropriate semantics for norms,
e.g., whether they are based on possible worlds, axiomatic constructions, or operational
executions. A more fundamental challenge for the semantics of deontic logic is captured in
“Jørgensen’s dilemma” (Jørgensen, 1937), which asks whether arguments that contain norms
(e.g., imperatives) express a truth or not. In standard conceptions of logical entailment, it
is essential that true conclusions follow from true premises; i.e., conclusions and premises
can be true or false. However, since imperatives are – supposedly – neither true or false,
operators in LTL.
100A more practical algorithm for PDL-SAT — although still EXPTIME-complete in the worst-case — has
been oﬀered by De Giacomo and Massacci (2000).
101See Sergot (1998) for an exposition, which also appears in the handbook on deontic logic by Gabbay et al.
(2013).
50

--- Page 51 ---

they cannot play any meaningful role in the validity of arguments, and as a results, we
cannot justify imperatives on the basis of logical reasoning. At the same time, reasoning
with imperatives seems to be logically valid in cases where the premises and conclusions are
imperatives (J¨orgensen, 1937, p. 290):
(P1) Love your neighbor as yourself
(P2) Love yourself
(C) Love your neighbour
Thus, the dilemma entails that we either have to accept that normative statements cannot
have truth values, or deny that the premises and conclusions of our argument have truth-values.
In turn, these considerations have given rise to several families of deontic logics, which can be
roughly divided into two camps: the possible-world approach — e.g., standard deontic logic,
“Seeing To It That” (STIT) logic (Horty, 2001) and dynamic deontic logic (Meyer et al., 1988;
Van Der Meyden, 1996) — and approaches that are not based on possible-worlds, such as
input/output logic (Makinson and Van Der Torre, 2000), imperative logic (Hansen, 2008),
defeasible deontic logic (Governatori et al., 2013), and prioritized default logic (Horty, 2012).
With regards to complexity, the ﬁrst path entails that one has to deal with the PSPACE-
completeness that often plague possible-worlds semantics (Halpern and Moses, 1992), or
the EXPTIME-completeness of dynamic logic (Fischer and Ladner, 1979). In fact, it is
shown that the satisﬁability problem for a fragment of STIT, which is used to construct
deontic STIT, is undecidable (Schwarzentruber and Semmling, 2014).102 As an alternative to
possible worlds, Sun and Robaldo (2017) has investigated the complexity of input/output
logic on the basis of a ‘norm-based’ operational semantics. In this view, declarative statements
can be true or false whereas norms cannot: they are simply violated or complied. More
precisely, norms are ordered pairs (x, y) that corresponds to deductive operations of the
input/output-system, taking a fact (x) as input, and producing an obligation (y) as output.
However, their investigation ﬁnds that decision problems of input/output logic are shown to
be NP/co-NP-hard and in the 2nd level of the polynomial hierarchy (i.e., NPNP and co-NPNP
). By contrast, Governatori et al. (2013) has demonstrated the computational tractability of
a deafeasible deontic logic able to compute ‘weak’ (allowed unless explicitly prohibited) and
’strong’ permission (only allowed if explicitly permitted). However, the constructed object
logic has a rather constrained expressibility, as it only includes propositional symbols and
their corresponding negations, and only modal literals are allowed (obtained by applying
modal operators for obligation and permissibility to propositional literals).
In summary, the surveyed results support the conclusion that using modal logic — e.g.,
temporal logic, dynamic logic, deontic logic — to represent or automatize moral reasoning
generally introduces computational intractability. Naturally, in order to capture the rich
intricacy of ethical life, normative notions in logical form must be able to account for knowledge,
time, agency, program behavior, and multi-agent dynamics, which inevitably adds complexity.
However, it must be noted that while these results might appear to indicate something deeply
problematic for the prospect of moral machines constrained by polynomial time, they are also
102See also Balbiani et al. (2008); Herzig and Schwarzentruber (2008); Xu (1998) for other results on the
complexity and decidability of STIT.
51

--- Page 52 ---

immensely productive for other practical purposes. For instance, knowing that a problem is
provably in PSPACE may allow it be related to a vast set of other PSPACE-problems, along
with the algorithms, approximization techniques, and heuristics that have been developed to
tackle them. The fact that the satisﬁability problem for dynamic logic is EXPTIME-complete
does not stop it from being useful in formal veriﬁcations of program behavior. More broadly,
from a design perspective, the complexity results may be of great help to inform ones choice
of formal system — its expressivity, operators, syntax, and semantics — for the practical
purpose at hand.
5.2.3. The Problem of Moral Semantics
The problem of semantics comes in various variants, some of which have been subject
to extensive philosophical treatment for centuries. Earlier in this section, we noted that,
if an agent should follow a rule of the type “‘If input X →do action Y ”, we assume that
the agent has some non-trivial understanding of what X and Y means. In the semantics
of propositional logic, we simply say that the terms are either true or false with respect to
some model (or in modal logic, with respect to possible worlds), and provide rules (e.g., a
truth table) for determining the truth value of sentences made up of those terms and logical
connectives (e.g., ¬, ∧, ∨, →, ⇔). Similarly, semantics in programming languages might simply
deﬁne the process of how valid strings in the syntax (instructions) will induce (interpretation)
certain state transitions (execution), e.g., by manipulating some data structure. In such cases,
semantics may be viewed as a purely mechanistic operations, and the job of establishing the
link between model and reality — e.g., how any valid sentence that can be expressed by the
language corresponds to some real-world state of aﬀairs — is circumvented.
Nevertheless, human moral discourse — e.g., of virtues, principles and judgments — is
abundant with descriptions and concepts that are semantically so-called ‘thick’. For instance,
moral talk involve ‘thick descriptions’ that embed subjectivity as part of their meaning, e.g.,
by explaining individuals’ behavior in light of internal motivations (Geertz et al., 1973). That
is, when we describe an agent as being courageous or fair, we naturally assume that the
agent has some subjective characteristics (e.g., psychological dispositions and experience)
that exempliﬁes courage and fairness. In turn, these subjective characteristics might only
make sense for an agent, given that the agent also understands how they relate to her own
subjectivity (e.g., sensori-motor experience, beliefs, desires, and intentions). Moral talk also
involve paradigmatic examples of ‘thick concepts’ that are both descriptive and evaluative
(Blackburn, 1998); e.g., terms like generous and selﬁsh can refer to descriptions of certain
behaviors (acts of sharing or not sharing one’s food), while simultaneously denoting an
evaluative quality (being good respectively bad).
Unfortunately, thick concepts and descriptions invoke issues that remain at the center
of long-standing metaphysical and meta-ethical debates. To explicate the meaning of thick
descriptions, in so far as they depend on subjectivity, one might in turn require satisfying
answers to other fundamental challenges, such as the symbol grounding problem (Harnad,
1990), the hard problem of consciousness (Chalmers, 1997), and the meta-ethical problems
of determining the meaning of “meaning” and truth with regard to moral terms. The ﬁrst
problem is relevant for any system that make use of symbols — e.g., to communicate or reason
— as it concerns how symbols ground their meaning. For over four decades, Searle’s Chinese
Room experiment (Searle, 1980) has provided a venue for philosophical discussions about
52

--- Page 53 ---

the limits of whether and to what extent computational systems can “understand”. Searle
famously argues that a computer program that is able to convince a human Chinese speaker
that it understands Chinese, does not literally “understand” Chinese, as it is merely following
syntactic rules. But even if we oppose to Searle’s broad rejection of computationalism,103
we still need to give some account of how thick moral terms get their meaning, or more
pragmatically, what they ‘do’ for our moral practices. However, it very much remains an
open question to what extent the grounding of symbols rely on, e.g., intentionality (Brentano,
1874), perceptual experience (Barsalou, 1999), or certain sensorimotor capacities (Taddeo
and Floridi, 2005), and yet another open question whether such capacities can be carried out
by a computational system.104 Similarly, to explicate thick concepts, one naturally has to
assume that it is possible to disentangle their evaluative and descriptive components.105
So how do these deeper problem of semantics relate to computational complexity? Of
course, it ultimately depends on how we position ourselves with respect to these debates, as
they would determine our view of moral semantics, and the role moral terms play in moral
behavior. On the one hand, if we hold — following meta-ethical cognitivism — that the
meaning of moral terms can be properly disentangled and deﬁned as truth-bearing entities,
problems expressed in any ‘thick’ moral language would in principle be computed in the ways
discussed in section 5.2.2 (e.g., the checking validity with respect to a given or all possible
Kripke structures). As such, moral semantics would not yield any additional complexity
baggage that does not already follow from the moral languages’ expressiveness. However, while
cognitivists hold that moral terms can express mind-independent facts about the world, it does
not mean that we have found them; like divine command theory, the approach presupposes
103Computationalism is the family of views that hold that the human mind — including consciousness and
cognition — is some form of computation.
104Aaronson (2013) has framed a technical version of the related “Waterfall argument” in light of complexity
considerations, which supplements the Chinese Room by claiming that meaning is always relative to some
external observer (Searle, 1992). The argument starts from the observation that any physical system with
a suﬃciently large state space could in principle implement the semantics of any other system; e.g., for
some mapping M from a waterfall’s initial states I to ﬁnal states F, there is a way of labeling any given
permutation P from I and F such that M implements P, and P may thus represent any “semantics” we like,
such as a chess playing program. However, if we actually tried to use a waterfall to compute chess moves, we
would need to ﬁnd a reduction from the chess program to the waterfall, e.g., by showing how chess positions
and chess moves can be eﬃciently tracked to the waterfall’s initial and ﬁnal states. From this, Aaronson
conjectures that, for any given chess program with access to a waterfall oracle, there is another chess program
with equally good performance and similar resource requirements that does not access the waterfall oracle. In
other words, it seems highly probable that any reduction algorithm from chess to waterfalls would simply
solve chess problems, and not use the waterfall in any meaningful way. For Aaronon, this mirrors the more
substantive notion of completeness: the class that a problem is reduced to cannot itself be suﬃcient to solve
the same problem. I.e., while NP-problem X1 can be solved in polynomial time with access to an oracle
for X1, problems in P cannot be reduced to problems in P (as this would imply that every problem in P is
P-complete). The presumed equivalence between waterfall and chess computation thus carry little substance,
unless the equivalence can be demonstrated in a model of computation that itself isn’t capable of solving
waterfall or chess problems.
105This would, somewhat coarsely, be the position of Blackburn (1992) and Hare (1952). In contrast, thinkers
like Putnam (2004) and Williams (2006) see thick concepts as indivisible blends of fact and value. For instance,
Putnam states that ‘thick’ ethical concepts “simply ignores the supposed fact/value dichotomy and cheerfully
allows itself to be used sometimes for a normative purpose and sometimes as a descriptive term” (Putnam,
2004, p. 35).
53

--- Page 54 ---

that one has collected exhaustive knowledge of all moral terms — e.g., via access to Platonic
reality — and managed to encode them along with all their semantic relationships.106 At
present, nevertheless, there is strong disagreement about what moral terms mean.107
A skeptical alternative would be to bite the bullet of undecidability. For instance, Rice’s
theorem states that all non-trivial semantic properties of a language recognized by a TM
are undecidable, where semantic properties are about a programs behavior, and non-trivial
properties are neither true for all partially computable functions, nor false for all partially
computable functions.108 To illustrate, we can imagine a moral language ML as a set of TM
descriptions, and the criteria for TMs to be in ML is that their language L(TM) accepts at
most three strings (|L(TM)| ≤3). If a language M1 belongs to ML (M1 ∈ML), it means
that M1 satisﬁes the property ML. That ML is a property of TM languages can be shown by
the fact that two machines with the same language, M1 and M2, are either both in ML or
neither in ML; since they have the same language, they have the same number of strings. To
show that ML is non-trivial, we let M3 be a machine that accepts every string, and M4 be a
machine that rejects every string. Since M3 ̸∈ML (accepting more than three strings), and
M4 ∈ML (0 is ≤3), it follows from Rice’s theorem that ML is undecidable. Of course, we
can let ML denote a great number of things, and given the vast generality of Rice’s theorem,
we can demonstrate undecidability for a large set of problems pertaining machine behavior.109
Analogously, we can draw a skeptical conclusion about the prospect of moral languages; as
long as there are some disagreement about the meaning of moral terms (e.g., diﬀerent agents
computing diﬀerent outputs), there can never be a decidable moral language.
There are, of course, many other palpable reasons to be skeptical about the decidability of
moral semantics. For instance, both computability and theories of meaning ﬁnds a common
nemesis in the self-referential Liar Paradox: “this sentence is false”. It plays a central role in
G¨odel’s ﬁrst incompleteness theorem — by replacing “false” with “not provable” — as no
consistent system of mathematics can prove truths about itself. Similarly, Turing’s Halting
problem demonstrates that it is undecidable whether a computer program halts, as for any
program P that can decide “Yes” for halting can be countered by another program that uses
P as input in order to produce the opposite “No”.110 On the side of theories of meaning,
Alfred Tarski found that the Liar Paradox only appears in “semantically closed” languages,
i.e., a language that can express the truth of its own sentences (Tarski, 1944). Tarski’s own
solution — to separate the referring meta-language from the referred object language in a
constructed hierarchy — was in turn found to be incomplete by Kripke (1976), who, among
other things, employed self-referential tricks to produce statements that break the hierarchy.111
106Of course, this is not unfeasible for extremely limited state spaces. For instance, we can imagine a toaster
that uses sensors to read whether a toast is under-baked, baked, or burnt, and understand how evaluative
sentences “this toast is bad!” express certain facts about about the toast’s states.
107Recalling Jørgensen’s dilemma from the previous section, we also note that there are profound disagree-
ments about valid inference in deontic logic.
108Conversely, a partial function is trivial if it is true for all partial computable functions or for none.
109For instance, whether a given TM computes a constant function, a total function, the identity function,
add two natural numbers, or a computable function can easily be shown to be undecidable using Rice’s
theorem.
110In turn, the more general Rice’s theorem can be proven by reduction from the Halting problem.
111Kripke gives the following example, expressed by Jones and Nixon: (J) “Most (i.e., a majority) of Nixon’s
54

--- Page 55 ---

Of course, Kripke’s solution — which utilizes partially deﬁned truth predicates (“undeﬁned”)
— can in turn be targeted by a strengthened liar paradox: “this sentence is either false or
undeﬁned”. Ultimately, as any solution seems to produce new self-referential problems that
applies to the new solution, any semantic theory centering on truth is haunted by a paradox
out for revenge (Beall, 2007). Moreover, as demonstrated by Dahl (2022), the Liar Paradox is
not content with semantic theories based on truth, but extends to all theories that seeks a
uniﬁed explanation of meaning for any language. In short, since any uniﬁed theory of meaning
requires a language that is expressive enough to assert its own meaning, and no language
can coherently assign meaning to itself while articulating the uniﬁed theory, it follows that a
universal theory of meaning is impossible.
A more pragmatic route is to deny that moral terms can be true or false, and instead
say, following Wittgenstein (2010), that “meaning is use”. Besides purifying moral semantics
from Platonism and paradoxes, it would potentially bring moral talk closer to the eclectic
social practices from which it stems, where occasional quarrel, misunderstanding and dissent
is inevitable. In this view, moral expressions should not be understood in virtue of any formal
account of meaning, but rather how they, in more or less satisfactory ways, serve our moral
practices. Presumably, this could even circumvent the undecidability of non-trivial semantics
and halting, if we accept that it is no problem that arbitrary programs either do ‘this or that’;
pragmatically, they either work well, or they do not. In place of truth-conditions, we could
adopt one or several of the prominent non-cognitivist approaches to moral language, e.g.,
that moral statements function to express emotion and elicit emotion in others (Stevenson,
1937); to assert prescriptive judgements (Hare, 1952); or convey attitudes (Schroeder, 2010).112
However, while such theories may be credible for emotional, judgemental, and aﬀective humans,
they are less suitable for a complexity analysis, as they often presuppose a human-speciﬁc
psychology.
Nonetheless, one way to analyze the complexity of potentially ‘mindless’ agents’ use of
moral terms is to look to modern Wittgensteinans such as David Lewis and Robert Brandom.
Before his work on counterfactuals, Lewis provided an early game-theoretic analysis of social
conventions (Lewis, 1969). In this view, following the footsteps of Schelling (1960), linguistic
as well as moral conventions can be viewed as self-perpetuating solutions to reoccurring
coordination problems, where it is mutually beneﬁcial for self-interested agents to coordinate
their actions. Linguistic meaning, more particularly, have subsequently been explored within
the paradigm of signaling games. In a simple signaling game, a messenger seeks to convince
receivers that they are of a certain type — e.g., that they are competent — where the actual
type is only known to the messenger. Intuitively, no honest messenger beneﬁts from being
misunderstood (e.g., conveying false information about their type), just as it is beneﬁcial for
incompetent players to lie, and players receive payoﬀs depending the receivers’ responding
action (e.g., hire agent a or b). Given its explanatory power, signaling games have been used
to model the development of communication and linguistic meaning (Skyrms, 2010; Huttegger,
assertions about Watergate are false”, (N) “Everything Jones says about Watergate is true” (Kripke, 1976,
691). In the Tarskian hierarchy, N needs to be on a higher level than everything that Jones says, and J needs
to be on a level higher than what everything Nixon says.
112It should be noted that these non-cognitivist positions should not be equated with a Wittgensteinian
outlook on meaning per se, but rather that they reject the belief that moral terms are truth-apt.
55

--- Page 56 ---

2007).
Since signalling games are typically modeled as sequential Bayesian games, their equilibria
solutions are plagued by the intractability concerns discussed in section 5.1.5; in particular the
NP-hardness of checking whether a Bayesian game has a pure-strategy Bayesian equilibrium,
and the PSPACE-hardness of computing a pure-strategy NE in Markov Games (Conitzer and
Sandholm, 2008). However, Lewis’ own equilibrium concept, called coordination equilibria, has
the property that every player also prefers that every other player conform to some regularity
R, on the condition that at least all but one player conform. Naturally, this presupposes some
concept of common knowledge, which was subsequently generalized by Aumann’s correlated
equilibrium (Aumann, 1974). As discussed in 5.1.5, CE is computationally attractive, as
they can be found in polynomial time for games with any number of players (Gilboa and
Zemel, 1989).113 In Lewis’ original deﬁnition, however, conventions are necessarily arbitrary,
in the sense that there is a conﬂicting regularity R′, which could have become the stable
convention (and R and R′ are mutually exclusive). Of course, the concept of arbitrariness
certainly has explanatory value: while it is not arbitrary that a mutually beneﬁcial solution
to a coordination problem becomes convention (e.g., cars driving on opposite side of the
roads), it is arbitrary that a particular solution was chosen over another (e.g., right-hand
traﬃc as opposed to left-hand traﬃc). Still, the arbitrariness criteria does not exclude the
possibility that a conﬂicting regularity could result in an even greater joint beneﬁt. Thus,
since stable conventions become self-perpetuating, their potential moral value relies on the
same optimistic conservatism that permeates post-hoc evolutionary explanations of altruism
and social contracts; that there are good reasons why conventions are as they are. By contrast,
it is possible for a convention to have an exceptionally high price of anarchy (i.e., a terrible
worst-case equilibrium), while the stability of the convention ensures that no one believes
that anyone would beneﬁt from going against the grain. However, evaluating the convention
against alternatives, e.g., by computing a CE that maximizes the expected joint beneﬁts,
invites NP-hardness (Papadimitriou and Roughgarden, 2008).
On a more optimistic note, these computational diﬃculties may be mitigated by cooperative
principles for communication, e.g., following the work of Grice (1975). This strategy can be
reﬂected in Lewis’ reﬁned analysis of convention (Lewis, 1975), which includes preferences
with regard to one’s own beliefs: “The expectation of conformity ordinarily gives everyone
a good reason why he himself should conform” (Lewis, 1975, p. 8). Similarly, Lewis writes
that “a language L is used by a population P if and only if there prevails in P a convention
of truthfulness and trust in L, sustained by an interest in communication” (p. 10). For Lewis,
along with other Griceans such as Schiﬀer (1972) and Bennett (1976), meaning ultimately stems
from a coordination between speakers communicative intentions and receivers communicative
expectations. In turn, these intentions and expectations may as well encompass cooperative
conventions.
A related yet distinct account of “meaning is use” that is apt for explaining moral language
has been provided by Brandom (1994). Brandom gives a theory of sapience — the type of
rationality that humans possess — based on the notion of discursive practice, which can be
113See also the work of Urbano and Vila (2002), which demonstrates how correlated equilibrium can be
achieved by imposing computational restrictions on the unmediated communication.
56

--- Page 57 ---

summarized as “the game of giving and asking for reasons” (p. 6). Participants of discursive
practices take on entitlements and commitments, which can be seen as carrying the normative
force of permissions and obligations, respectively. At the core of discursive practices are
inferential relations, which preserves commitments and entitlements to other statements. I.e.,
sentences only carry content in terms of their function, which is inferred in relation to other
sentences. What is interesting with regards to moral discourse, is that linguistic performances
are characterized by their ability to alter the normative status of the members of a discursive
practice. This takes the form of a conversational “scorekeeping”, where the participants keep
track of commitments and entitlements within the conversational context, e.g., by making,
acknowledging, contesting, or withdrawing assertions.114 In essence, the normative pragmatics
of linguistic performances determine the inferential aspects of semantics, and not the other
way around. However, while Brandom’s inferential semantics may help to illuminate the
normative commitments of speech acts, we can only speculate about the computational aspect
that underpins the ability to successfully participate in a discursive practice, and similarly,
whether and to what extent it alleviates or adds computational demands. On the one hand,
the game of reason-giving and reason-asking seems tailored to eﬀectively foster cooperative
communication in normative life. On the other hand, Brandon’s conception of sapience
seems profoundly human, which, in addition to the sentience shared with non-verbal animals,
involves an understanding of conceptual contents, which in turn may encompass intentional
states, beliefs, and desires of oneself and others. In turn, a sapient game of reasons might more
or less correspond to a Kantian conception of moral rationalist discourse (Brandom, 2006),
which presupposes sophisticated and idealized capacities for moral autonomy and freedom;
capacities which — at least presently — cannot be construed in computational models.
The main lesson seems to be that, while game-theoretic concerns — of computational
intractability and threats of repugnant equilibria — may be alleviated by communication, the
challenge is to not only give an account of how communication works, but why it works so
well. For Lewis, the success seems to rely on communicative intentions and expectations of
speakers, and the cooperative conventions that results from it. For Brandon, it centers on the
sapient game of “giving and asking for reasons”. Unfortunately, this renders both approaches
rather computationally opaque: as they aim to explain human communication, they can,
just like non-cognitivist theories, resort to uniquely human features that remain more or
less impenetrable from a computational perspective. Still, such theories might potentially
yield signiﬁcant value by enclosing the gap between, on the one hand, cognitive-psychological
resources — e.g., reasons, trust, and communication — that fosters eﬃcient cooperation, and
on the other hand, the computational architectures that would potentially enable them. In
turn, complexity considerations might help to illuminate the rich interrelationship between
game-theoretic dynamics, social-psychological capacities, and normative theory in everyday
moral interactions.
In summary, this section has discussed more profound issues for moral semantics that,
although relatively ignored in machine ethics, remain at the center stage of meta-ethical and
meta-semantical debates, as well as in theories of communication. Of course, a simple move
114The idea of scorekeeping in the context of conversations was ﬁrst introduced by Lewis (1979), who acted
as a supervisor for Brandon’s doctoral thesis in the 1970s.
57

--- Page 58 ---

would be to cling on to some metaphysical argument against “strong AI” (Searle, 1980), some
advanced requirements for symbolic grounding (Taddeo and Floridi, 2005), or some uniquely
human psychology of emotions, and conclude that “machines can never genuinely understand
moral language”. But even given that one decided to ignore such problems, many complex
problems remains for computational moral semantics.
5.3. Consequentialist-Deontological Hybrids
Having investigated a range of computational aspects of both consequentialism and
deontology, we are now in a position to say something more substantial about their diﬀerence
and potential combination. First, it should be concluded that the claim “deontology is,
computationally speaking, less complex than its alternatives” cannot be given a straightforward
answer; and in many cases, it is simply false. Based on the material discussed in this section,
we can outline a more nuanced answer:
(1) As argued in section 5.1.1, it is a mistake to view rule-following in legal and liberal
contexts as computationally simple. While legal rules may eﬃciently compress voluminous
moral wisdom, it is only against the backdrop of a complex relationship between the mech-
anisms that incentivizes their adherence (e.g., police and punishment), ensures their just
interpretation (e.g., courts), along with the moral sentiments of the subjects the laws apply
to. For instance, the complexity of “do no harm”-principles in liberal contexts can only be
meaningfully analyzed in relation to the capacities of fully autonomous citizens.
(2) On the other hand, deontological rules may be signiﬁcantly more eﬃcient than
alternatives if they are justiﬁed on the basis of divine command or legal positivism. However,
unless in extremely simpliﬁed cases, the knowledge-requirements for such approaches to work
in practice remains unfathomably vast, while the knowledge itself may be highly contentious.
(3) As an alternative, deontological rule-following may include justiﬁcation as a part of
the moral computation, e.g., by considering how rule-following behaviors aﬀect others. As
discussed in 5.1.2, this can range from considerations of (i) one’s own preferences (“I treat
you based on what I personally prefer”), (ii) preferences of others (“I treat you based on what
I know of what you prefer”), to (iii) general behavior (“I generally treat you in the way that
I would want others to generally treat me”). While weaker versions — e.g., (i) and (ii) —
may be relatively simple from a complexity perspective, they also lead to a range of other
problems. By contrast, stronger versions — e.g., contractarian or contractualist versions of
(iii) — are obfuscated by extreme variances with regard to behavioral expectations and the
capacities that makes up conceptions of general behavior.
(4) Any general-purpose normative theory that seeks to account for multi-agent dynamics
face game-theoretic concerns. This includes issues of rationality (5.1.3), incomplete information
and recursive reasoning (5.1.4), and the intractability of computing morally attractive Nash
Equilibria (5.1.5).
(5) Any computational system that employ formal logic, e.g., for deontological rule-
following, moral reasoning, or communication are subject to expressibility (5.2.1), intractability
5.2.2, and decidability (5.2.3) issues that permeate the syntactics and semantics of logic.
(6) Finally, it should be acknowledged that deontology is a family that encompasses a
range of ethical theories that may in turn emphasize a range of diﬀerent cognitive abilities
and computational resources. It can be a moral rationalist project of ﬁnding universally
justiﬁable and applicable rules on the basis of a shared autonomy and rationality. It can be a
58

--- Page 59 ---

contractarian project of ﬁnding mutually beneﬁcial action-rules based on self-interest. In the
simplest case, rules can act as merely ‘fast and frugal’ heuristics that support agents with
bounded cognition to produce any action in complex or novel situations, even if there is no way
to evaluate whether the performed action is appropriate in the speciﬁc situation; it may simply
be an automatic ‘default’ action, or rely on optimistic conservatism (“it has worked well before,
so it might also work well in the future”). In more ambitious cases, deontological rule-following
might ask one to compute morally attractive equilibria for large-scale coordination problems
with incomplete information.
Based on these considerations, it may be misleading to compare the complexity of
deontology and consequentialism, as any comparison relies on a particular conception of
what the theories dictate. For instance, both theories are equally targeted by game-theoretic
intractability (5.1.3) insofar as they take other agents into account. Similarly, many of the
deeper problems of moral semantics that plague logical systems (5.2.3) can also be construed
for consequentialist agents: e.g., what is it for a computational system to “understand” what a
certain utility really is? Another reason is that deontology and consequentialism may converge
on their solutions, for instance, in cases where the deontological moral right also produces the
optimal outcome. Thus, a reasonable alternative is to view them as complementary theories,
which emphasize diﬀerent cognitive capacities, computational resources, or aspects of ethical
life.
To that end, it is no surprise that hybrid accounts, which combine aspects of consequential-
ism and deontology, are well-reﬂected in moral philosophy (Brandt, 1979; Hare, 1981), moral
psychology (Kahneman, 2011; Greene, 2007) and machine ethics (Bauer, 2020; Arkin, 2007;
Dehghani et al., 2008a; Stenseke and Balkenius, 2022; Pontier and Hoorn, 2012; Azad-Manjiri,
2014; Tuﬁ¸s and Ganascia, 2015; Govindarajulu and Bringsjord, 2017; Pereira and Saptawijaya,
2009). However, it should be noted that in almost every case, deontology takes on a rather
narrow role in these architectures — often within a broader consequentialist framework —
which does not reﬂect its rich tradition in ethical theory. For instance, deontology might act as
a priori constraints which prevent certain intrinsically bad actions (Pereira and Saptawijaya,
2009; Dehghani et al., 2008a). Another option is to use deontological rules to foster run-time
eﬃciency, e.g., by turning consequentialist computation or exploration into exploitable rules
(Stenseke and Balkenius, 2022).115 Similarly, in the dual process theory of moral cognition
(Greene, 2007), deontological judgements are construed as fast and instinctive responses,
whereas consequentialist judgements denote slow and reﬂective reasoning processes.
With regards to complexity, the emerging trend is that moral rule-following can either
(i) be used to prevent intrinsically bad actions, (ii) reduce the run-time complexity of
(often consequentialist) moral computations, or (iii) act as a ‘principles ﬁrst’ or ‘defeasible’
default mode in situations where the agent has nothing else to base their decision on.
From a moral-psychological perspective, (ii) and (iii) can be supported by the idea that
automatic moral judgements compress moral wisdom, e.g., on the basis of evolutionary
adaptations promoting cooperation, culture-speciﬁc norms fostering collective well-fare (e.g.,
salient correlated equilibria), or the moral lessons an individual learns to internalize through
115Since consequences motivates the use of certain rules, it is more suitable to view this solution as a form of
two-level utilitarianism (Hare, 1981).
59

--- Page 60 ---

experience. For machine ethicists, consequentialist-deontology architectures thus oﬀer an
attractive smorgasbord of context-speciﬁc modularity; from top-down a priori constraints
based on preexisting moral knowledge (divine command) to bottom-up a posteriori turned
into new top-down constrains (e.g., learning eﬃcient rules through experience). However, this
image is not without its ﬂaws, as any reduction in run-time complexity implies one or many
of the following problems:
The problem of optimistic conservatism — In essence, ‘fast and intuitive’ moral behavior
cannot be guaranteed to produce good moral results, unless it is evaluated against alternatives
(e.g., on the basis of experience or moral reasoning). As such, the moral value of intuitions
rely on an optimistic conservatism, as the eﬃciency of following an intuitive deontological
(or rule-consequentialist) rule may come at the expense of losing out on a potentially better
outcome that was only attainable via further reﬂection. Following Hare (1981), this is the
challenge of knowing when to think like a ‘prole’ (using moral intuition) or an ‘archangel’
(using critical reﬂection). From a computational perspective, it reﬂects the well-studied
explore-exploit dilemma (4.3). It also echoes the problematic post-hoc rationale of norms and
conventions. As discussed in 5.1.3 and 5.2.3: even if we believe that a certain moral convention
— or rule, norm, principle — emerged because it helped agents with bounded cognition to
coordinate towards mutually beneﬁcial goals, the stability of the convention may rely on an
optimistic conservatism about the convention itself, even if there are alternative conventions
that might have been even better. Similarly, just because some moral intuitions may be a
result of adaptations that yielded reproductive success for our evolutionary ancestors, it does
not automatically make those intuitions morally right today (Greene, 2014).
The problem of speed vs performance — A related problem is the choice between moral
speed and moral performance. For instance, even if we, like Hare (1981) and Greene (2014),
believe that slow utilitarian deliberation should take normative and epistemological priority
over ‘fast’ intuitions, there is still an open-ended conﬂict between moral speed and moral
performance. In what circumstances do we opt for a fast — e.g., feasible, suboptimal, or
satisﬁcing — option in favor of a slower but potentially better option?
The problem of reasoning and learning — ‘Fast and intuitive’ moral intuitions may foster
run-time eﬃciency, but only by ignoring the complexity of the process that gave rise to
the moral intuition itself. On the one hand, this can refer to the complexity of the process
characterized by Hare (1981) as the “critical level” of moral thinking (which governs the
principles of the “intuitive layer”). On the other hand, we might think of it purely in terms
of a learning-process: e.g., how many learning examples and how much training-time does an
agent need to successfully internalize a moral intuition that allows it to eﬀectively solve a
given moral problem at run-time? In principle, since artiﬁcial neural networks can be used
to approximate any function (Scarselli and Tsoi, 1998), machine learning systems should be
able to achieve great run-time performance in moral problems given the right kind of learning.
However, as we will see in section 6, this will instead put increasing demands on sample and
training-time complexity, while introducing other problems related to induction.
The problem of knowledge — Instead of reasoning or learning, eﬃcient moral intuitions
may be secured on the basis of moral knowledge. For instance, an alternative that is available
for moral realists and meta-ethical cognitivists — who believe that moral intuitions can denote
true propositions that reﬂect subject-independent features of the world — is to collect and
write down the dicta of objective moral reality. Of course, as already noted several times
60

--- Page 61 ---

throughout this paper, such a project seems, for a variety of reasons, deeply problematic.
With that said, it does not exclude the possibility that there are some moral intuitions that
have universal (or near-universal) consensus, or some — following Asimov (1942) — that are
particularly attractive for computational agents.
In summary, if we view deontology simply as ‘rule-following’, it is clear that it yields
eﬃcient decision-procedures from a bounded rationality point-of-view. Nevertheless, while
it may lead to attractive run-time performance, the moral value of such eﬃciency is either
based on optimistic conservatism, the results of some other complex process (reasoning or
learning), or the collection of vast moral knowledge. Essentially, the moral power of rules —
their general applicability, general justiﬁcation, and computational simplicity — can only be
secured in complex ways. After all, the simplicity of moral rules should not prevent one from
questioning their authority, but rather, it should help one remember that they — like logical
systems — merely represent idealized facets of byzantine phenomena.
6. Virtue Ethics and Moral Machine Learning
As deontology centers on actions and consequentialism on results, they can be naturally
construed as moral decision-procedures. By contrast, virtue ethics is about being rather than
doing: instead of focusing on what the right action is, or what action yields the best outcome,
it asks us to foster our moral character and the internal dispositions — virtues of courage,
fairness, and temperance — that enables us to be morally virtuous. More broadly, virtue
ethics denote a vast family of ethical traditions that emphasize the role of our moral character,
and the theory can ﬁnd its diverse origin in thinkers such as Confucius and Mencius in the
East, and Plato and Aristotle in the West (Crisp and Slote, 1997). In contemporary times, it
has earned its spot as a central normative theory in Anglophone moral philosophy through the
contributions of Anscombe (1958), Nussbaum (1988), Hursthouse (1999), and Annas (2011).
In machine ethics, virtue ethics has several times been proposed as an appropriate blueprint
for the creation of artiﬁcial moral agents, as it emphasizes aspects of ethical life that are
relatively ignored in other theories (Coleman, 2001; Wallach and Allen, 2008; Howard and
Muntean, 2017; Stenseke, 2021).116 Taking the character as the central object of moral
evaluation — which encompasses both rational deliberation and psychological dispositions
— it paints a more holistic picture of what it is to be moral; capturing not only what we
ideally ought to do, but what motivates us to act in morally praiseworthy ways. One key
aspect of this picture is the notion of phronesis (“practical wisdom”), which can be construed
as the moral wisdom or skill an agent learns from practice and experience (Annas, 2011).
The focus on development and learning has in turn inspired machine ethicists to unify virtue
ethics with connectionism; both in terms of modern machine learning methods, and as a
broader theory of cognition (Casebeer, 2003; Wallach and Allen, 2008; Howard and Muntean,
2017; Berberich and Diepold, 2018). Optimistically, with the ability to constantly learn from
experience, be sensitive to contexts and adaptable to changes, a virtuous machine might thus
be able to apprehend the intricacies of human norms in dynamic environments where mere
utility-maximization or rule-following fails.
116See Stenseke (2022a) for a recent survey on computational implementations of virtue ethics.
61

--- Page 62 ---

In despite of these promises, virtue ethics remain relatively elusive from a computational
perspective. One reason is that virtue ethics is founded on a deeply human view of what
constitutes a moral life — of ﬂourishing, reasoning, emotions — against a rich backdrop of
culture and tradition. For obvious reasons, this makes virtue ethics hard to analyze from a
complexity perspective, as it would require a comprehensive computational description of
what a human being is, along with all her history and culture-speciﬁc ﬂavors. Nevertheless,
it is possible to isolate and analyze one necessary aspect of any virtuous agent: its ability
to learn. In principle, any of the problems discussed thus far can be re-framed as a learning
problem. Instead of asking “can I solve problem X? eﬀectively”, we ask “can I learn how
to solve X eﬀectively?”. If the answer is yes, the de facto run-time complexity might be
trivially low given the appropriate training. Intuitively, if a speciﬁc problem has already
been solved — e.g., having discovered the optimal action-combination for a certain situation
(4.1), an optimal reinforcement learning policy for an environment (4.3), or an action-rule
in a strategic setting (5) — the same solution may be applied in constant time O(1) to
future cases given that the very same problem re-occurs. And even if the exact same problem
never re-occurs, there might be patterns or trends to extrapolate from situations that are
suﬃciently similar. Through repeated encounters with salad bars (2), we might learn about
good combinations of ingredients. Seeing the same ingredients appearing in other salad bars,
we can make use of our previous experience to eﬃciently put together a tasty salad. Following
the virtue-theoretic emphasis on moral learning, the same should hold for moral behavior. In
the words of Aristotle: “[...] a young man of practical wisdom cannot be found. The case is
that such wisdom is concerned not only with universals but with particulars, which become
familiar from experience” (NE 1141b 10).
In turn, learning a machine is the business of machine learning, which, due to a wealth
of recent advancements, has come to dominate the ﬁeld of AI in the 21st century. The
relevant question for our investigation — and the topic of this section — is: are there any
computational complexity considerations that might constrain a computational agents ability
to learn in the moral domain?
6.1. The Complexity of Learning
As with any mature ﬁeld of mathematical analysis, there are many relevant variants,
settings, and measures that can be used to formally analyze the complexity of learning.117
First, we might diﬀerentiate run-time complexity (the number of state transitions an algorithm
needs to perform at run-time to solve problem X), from training-time complexity (the number
of steps required to train the algorithm to solve X) and sample complexity (the number
of data points needed to learn how to solve X). Nonetheless, in practice, the distinction
between these types may break down; for instance, if one sample represents one point in time,
our sample complexity would be equal to our training-time complexity; similarly, we might
understand training-time complexity as the run-time complexity of a learning algorithm.
What is important to note, however, is that the three types are intimately linked. In a
completely known environment (say, Chess), simulation (e.g., using Monte Carlo methods)
may be an eﬀective way to get experience, e.g., by trying out the value of many diﬀerent
117See Vapnik (1999) for the deﬁnite introduction to statistical learning theory, along with an exhaustive
account of its rich history.
62

--- Page 63 ---

possible decisions. In this case, sample complexity measures how much simulation is required
to ﬁnd a good chess move. If the sample complexity is low, it means that it can be learned
eﬀectively, as it gives a lower bound on the total computational complexity (Kakade, 2003). In
other situations, there might be an abundance of data and plenty of time to train our model,
while the task itself may refer to some general ability — e.g., evaluated using a Turing test —
as opposed to how the system solves some speciﬁc decision-problem. Large language models
like GPT-3 (Brown et al., 2020), which uses signiﬁcant parts of the internet as training-data
in order to produce new text, constitute suitable examples of this. In the most extreme case
— e.g., an on-line reinforcement learning setting — if an agent have no information about the
environment and no access to a simulation of it, trial-and-error exploration might be the only
path to learning.
Our choice of complexity resource ultimately depends on the setting for our learning agent,
and each setting has their own range of speciﬁc sub-types and relevant measures. To that end,
it is common to diﬀerentiate between three broad classes of machine learning settings: (i)
supervised learning (SL), where the aim is to learn from pre-labeled data, (ii) unsupervised
learning (UL), where the training data lacks labels, and (iii) reinforcement learning, where
learning is based on feedback. For an SL agent, the relevant question may be: how many
labeled pictures of cats do I need to see in order to, within some margin of error, accurately
classify new pictures as portraying cats or not? In a virtue-theoretic view, this could be
rephrased as: how many labeled examples of “courage” (e.g., acts of courageous behavior) do
I need to observe in order to classify unobserved actions as courageous in the future? In this
case, we might only be interested in how sample complexity — number of pictures depicting
courage in the training set — reduces the agents prediction error in the classiﬁcation task
(e.g., empirical risk minimization). For an RL agent, the question might instead be: how
much do I need to observe the overall behavior of a moral exemplar (e.g., a virtuous human)
in order to approximate their reward function.118 Here, it could also be important to consider
the potential risk of detrimental mistakes during an agent’s learning phase. As discussed in
(4.3), if trial-and-error exploration is the only option the goal for an RL agent may not be
to merely maximize the cumulative reward, but to minimize regret relative to the optimal
solution.
Before we can ask whether something can be learned eﬀectively, we ﬁrst need to determine
whether it can be learned at all. For instance, we let X be a set of points, Y a set of labels
(e.g., 0 and 1), and H a set of hypotheses h (e.g., binary classiﬁers) that takes an x ∈X
and outputs a label y ∈Y . The goal for our learning algorithm L is to, given a sequence
of labeled training samples (x, y) drawn randomly from some distribution ρ over X, infer
a hypothesis h ∈H that is able to correctly classify future instances of x ∈X given some
accuracy ϵ and failure probability δ. In turn, we say that a hypotheses space H is learnable if
there exists a learning algorithm which, given a ﬁnite number of training samples (x, y)n, can
map inputs to outputs within ϵ of the optimal with a probability of at least 1 −δ.119 If so,
sample complexity can be deﬁned as n(ρ, ϵ, δ), which says that we need n training samples to
118This particular method is called inverse reinforcement learning, introduced by Ng and Russell (2000),
and suggested as a path towards artiﬁcial virtuous agents by Berberich and Diepold (2018).
119For instance, following empirical risk minimization, we might deﬁne the optimal h∗as the hypothesis
among H for which the risk of misclassiﬁcation is minimal.
63

--- Page 64 ---

learn a target function with respect to distribution ρ, error rate ϵ and failure probability δ.
6.1.1. Weak and Strong Sample Complexity
Based on these deﬁnitions, we may also diﬀerentiate between weak and strong variants
of sample complexity, e.g., by asking how many samples we need to learn a target for some
speciﬁc input-output distribution ρ over X (weak), and how many we need to learn it for
any possible distribution (strong). Following the strong approach, the impossibility results
commonly known as the No Free Lunch Theorem (NFL) establishes that there will always
be unfortunate distributions for which the sample complexity is arbitrarily large (Wolpert,
1992, 1996; Schaﬀer, 1994). As an intuitive example, we can imagine a learning algorithm
whose goal is to predict the weather — in this case limited to sunny (S) or rainy (R) —
based on the weather on previous days. Collecting data for three days, we have 23 possible
weather-histories (i.e., SSS, SSR, SRR, SRS, ...). We then measure the learning algorithm’s
error ϵ as the ratio of incorrect predictions (e.g., predicting S for a day of rain). Then, we can
demonstrate that every learning algorithm achieves a perfect ϵ = 0 in exactly one weather
history, a maximally bad ϵ = 1 in another, a mixed result of 2/3 in three histories, and
ϵ = 1/3 in the three remaining histories. NFL establishes that, for each possible ϵ, every
learning algorithm achieves ϵ for the equal amount of possible weather-histories. For instance,
if we assign the same probability to each possible weather history (i.e., a uniform probability
distribution), NFL entails that every learning algorithm has the same expected ϵ of 1/2.
NFL results have subsequently been extended to optimization (Wolpert and Macready,
1997), supervised learning (Wolpert, 2002), statistical learning (Von Luxburg and Sch¨olkopf,
2011), meta-learning (Giraud-Carrier and Provost, 2005), and data privacy (Kifer and
Machanavajjhala, 2011).120 Essentially, it means that there exists no learning algorithm
that can perform well on every learning task having trained upon a dataset of a ﬁxed size.
Thus, for every learning algorithm, there exists a task on which it fails, as no learning
algorithm can generalize to all possible realities while having only observed some instances
of the realities. To that end, NFL has also been discussed in relation to more fundamental
problems in the philosophy of induction, e.g., in connection to Hume’s problem of induction
(Sterkenburg and Gr¨unwald, 2021; Schurz, 2017) or Occham’s razor (Lattimore and Hutter,
2013). Hume famously advanced skepticism against the very justiﬁcation of induction, arguing
that deductive reasoning alone cannot secure the validity of inductive inference; and neither
can induction, due to circularity, provide non-deductive grounds for itself (Hume, 1739).
Of course, it may not be fair to advance the fundamental issues of induction against the
feasibility of moral learning systems. While they may obstruct the prospects of a perfect
universal moral learner, it does not stop us from pursuing weaker yet reasonable alternatives
that are practically viable. Instead of seeking a global and model-independent justiﬁcation for
why inductive inference seems to work, we can opt for local and model-relative justiﬁcations
in order to explain why some learning algorithms work better than others (Sterkenburg and
Gr¨unwald, 2021). However, it should be stressed that any such alternative would inevitably
entail some form of inductive bias; assumptions that we exploit to enable and foster learnability.
One strategy to alleviate the curse of arbitrarily large sample complexity is to constrain
the space of probability distributions, e.g., by making assumptions about the structure of
120See Adam et al. (2019) for a systematic review of NFL theorems.
64

--- Page 65 ---

the distribution from which the data-points are drawn (called “parametric” procedures in
statistics). The most straight-forward parametric assumption can be found in the Central
Limit Theorem, which states that when we sum up randomly drawn independent variables,
they tend towards a normal distribution.121 In fact, most advancements in machine learning
rely on some form of parametric assumptions, e.g., using linear and logistic regression, and
the parameters of artiﬁcial neural networks.122
Another alternative is to constrain the space of hypotheses. In the philosophy of induction,
this can be motivated on the basis of Occam’s razor, which roughly states that simpler
hypotheses are generally more better than complex alternatives. But what does “simpler”
mean? And how many samples do we need to infer a simple hypothesis that is able to
predict well? In computational learning theory, such questions can be eﬀectively addressed by
the Probably Approximately Correct (PAC) model of learning, introduced by Leslie Valiant
(1984). Following the formalism described earlier, we consider a learning algorithm L that
wants to learn a Boolean function f : X →{0, 1} in a ﬁnite set of hypotheses H, on the
basis of samples (x) drawn independently from distribution ρ over sample space X. We call a
hypothesis h infered by L good if it can approximate f within some error ϵ > 0, in the sense
that:
Pr
x∼ρ[h(x) ̸= f(x)] ≤ϵ
(5)
Then, we say that L is “probably approximately correct” if it can make good approxi-
mations with probability 1 −δ, for any choice of ρ and all failure probabilities δ and error
rates ϵ > 0. Finally, we say that a function f is PAC-learnable if there exists an L that can
make “probably approximately correct” predictions with a sample size n that is a polynomial
function of 1/ϵ and 1/δ. In other words, PAC learning formalizes the idea that, if a function
is learnable, it means that there exists a learning algorithm that with a reasonable likelihood
can get reasonable generalization errors if it trains on randomly selected data, all while the
number of samples are upper-bounded by a polynomial.
What is interesting from a computational complexity perspective is that PAC-learning
yields a bound on sample complexity. If a target function is PAC-learnable, then the number
of samples n required to learn the function can be derived by:
n = 1
ϵ ln |H|
δ
(6)
Particularly, equation (6) illustrates the intimate relationships between prediction error,
conﬁdence, samples, and the space of hypotheses, and their computational trade-oﬀs. For
instance, it captures the intuition that error rate ϵ and generalization error δ can be reduced
(although never to 0) by increasing the number of samples. It also shows that successful
learning from a limited number of samples n requires us to constrain the cardinality of the
hypothesis space H; e.g., either by reducing the number of individual hypotheses, or by
121Philosophically, this means that one accepts that the world tends towards a normal distribution.
122It should be note that deep neural networks with suﬃciently many parameters can be viewed as non-
parametric; e.g., Lee et al. (2017) demonstrates that an inﬁnitely wide deep network is equivalent to a
non-parametric Gaussian process.
65

--- Page 66 ---

reducing their descriptive complexity.123 By contrast, a larger H may lead to overﬁtting,
i.e., when the hypothesis closely mirrors a particular set of samples and fails to generalize to
additional observations.
From a philosophical perspective, PAC-learning is interesting since it, regardless of Hume’s
skepticism, deﬁnes a rich class of instances where induction is guaranteed to work (at
least probably approximately). However, one signiﬁcant trade-oﬀwith the model is that it
only applies to ﬁnite classes of hypotheses, which inevitably entails a compromise between
approximation accuracy and the learning algorithms capacity. For instance, a hypothesis
containing continuous parameters may need to be turned into discrete parameters. The
question is, how ﬁnely do we divide the inﬁnite continuum? This conundrum can be addressed
by VC theory (developed by Vapnik and Chervonenkis (1974, 2015)). Importantly, as opposed
to hypotheses space, VC theory brings the richer concept of VC dimensions (VCD), which
measures a learning algorithm’s expressive capacity by the cardinality of the largest set of
points the learner can shatter. For instance, given three points in a two-dimensional space,
we can ask whether a linear classiﬁer LC can correctly separate negative (labeled −) and
positive points (labeled +). Particularly, we ask, for all possible ways of labeling the three
points 23 = 8, is there a way we can draw a straight line that separates positive from negative
points? After discovering that it is possible — i.e., LC shatters the set containing the three
points — we try to do the same for four points. Since no set of four points can be shattered
by a straight line,124 we conclude that the VCD of LC is 3. Similarly, a class of hypotheses
H shatters the points {x1, ..., xm} ⊆X if there is a hypothesis h ∈H which agrees with all
2m possible conﬁgurations of h(x1), ..., h(xm). The VCD of H is then the cardinality of the
largest m where there is a subset {x1, ..., xm} ⊆X that is shattered by H. In turn, due to
the work of Blumer et al. (1989), VCD has been uniﬁed with PAC-learnability through the
fundamental insight that ﬁnite VC dimensions provides the necessary and suﬃcient condition
for distribution-free learnability. In other words, if a set of hypotheses is PAC-learnable, its
VCD is ﬁnite. Of course, while it does not alleviate the fundamental problems of induction,
it yields a framework for describing when induction is feasible, a rich measure of expressive
capacity (VCD), as well as a substantive notion of simplicity (i.e., smallest amount of VCDs).
With regards to complexity, it has recently been proven by Hanneke (2016) that the optimal
sample complexity125 of PAC-learnability for class H is:
n(ϵ, δ) = O
V CD(H) + ln 1
δ
ϵ

(7)
Nevertheless, theories for feasible learnability face the same problem as Nash equilibrium:
just knowing that there exists a hypothesis h in H that is consistent with the data does
not necessarily mean that it is easy to ﬁnd. As such, PAC-learnability ignores the vast
computations that are potentially required to actually ﬁnd a good hypothesis. To that end,
123Aaronson (2013) has interpreted this aspect of PAC-learning as an mathematical justiﬁcation for why
Occam’s Razor works.
124This is a consequence of Radon’s theorem, which can be used to infer the VCD of linear separations of
d-dimensional points.
125Here, optimal means that the upper bound matches known lower bounds (Ehrenfeucht et al., 1989; Blumer
et al., 1989) up to numerical constant factors.
66

--- Page 67 ---

a large set of hardness results have been proven for PAC. In the proper setting, where the
learner is required to output h ∈H, Pitt and Valiant (1988) proved that representation
classes such as disjunctions of two monomials (a polynomial with only one term), Boolean
threshold functions, and Boolean formulae where each variable occurs at most once, cannot
be eﬃciently learned, as they can be reduced to known NP-complete problems. Based on
widely used cryptographic assumptions — e.g., the Rivest-Shamir-Adleman system and Blum
integers — Kearns and Valiant (1994) proves representation-independent hardness results in
the improper setting (where the learner can output any h /∈H) for a range of representation
classes, including polynomial-size Boolean formulae, constant-depth threshold circuits, and
acyclic deterministic ﬁnite automata.126 In addition, while the hardness of improper learning
rely on cryptographic assumptions, Applebaum et al. (2008) shows that a proof would either
“collapse” the polynomial hierarchy127 or imply that any average-case hard problem in NP can
be transformed into a one-way function (which would yield an outstanding break-through in
cryptography).
Another important distinction in learning theory besides proper and improper, is the
one between realizable (or “noise-free”) and agnostic (“noisy”) learning. In the realizable
case, it is assumed that there exists an optimal hypothesis h∗in the space of hypotheses
H in the sense that its ϵ = 0. In agnostic learning (Kearns et al., 1992), no assumptions
are made about the target function; we simply want to ﬁnd the best possible h from some
distribution.128 Paradigmatic problems in statistical machine learning includes the learning
of halfspaces (or linear threshold function),129 monomials, and decision lists. While learning a
halfspace in the proper realizable case can be done in polynomial time via linear programming,
its NP-hardness in the proper agnostic case have been proven in various ways.130
As discussed in 4.3, similar computational hardness prevail in reinforcement learning
(Mundhenk et al., 2000; Papadimitriou and Tsitsiklis, 1987). In fact, there are many reasons
to believe that reinforcement learning is signiﬁcantly harder than the supervised setting: the
learner may not receive a training sets from the environment; the learner’s may only receive
‘noisy’ immediate rewards (which can deceive the agent into learning policies that does not
maximize the long-term future rewards); exploiting comes at the expense of losing out on
exploring (and vice versa); and there may even be detrimental consequences to consider
(minimize regret).131
126In the improper context, representation-independent hardness means that learning remains hard regardless
of the form the algorithm represents its hypothesis, on the basis that the hypothesis can evaluated in polynomial
time.
127This means that if NP = co-NP, then it follows that PH = NP. It is widely believed that a collapse of the
PH is implausible.
128See (Hopkins et al., 2022) for an exposition of the deeper relationship between agnostic and realizable
learning.
129Formally, a halfspace is a Boolean function of the form f(x) = sign(w1x1 + ..., wnxn −θ), where wi are
“weights”, θ is the “threshold”, and w1..., wn, θ ∈R. The sign function returns 1 on arguments ≥0, otherwise
−1.
130See, among others, Angluin and Laird (1988); Amaldi and Kann (1998); H˚astad (2001); Ben-David et al.
(2003) and Feldman et al. (2012) for a more recent overview. See also Daniely et al. (2014) for the improper
case.
131See Kakade (2003) for a detailed investigation of sample complexity in reinforcement learning.
67

--- Page 68 ---

6.1.2. Machine Learning Theory vs Practice
It is important to stress that the theoretical considerations discussed here might have
limited relevance for the practical viability of machine learning in various domains. Clever
uses of inductive biases — e.g., task representation and parametric tools — along with vast
amounts of training data and computational power continue to defy what might have appeared
to be impossible only a decade ago. For instance, the performance of deep learning models
in the ﬁeld of natural language processing has recently been accelerated via the transformer
architecture (Vaswani et al., 2017), which utilizes attention mechanisms to process tokens
from any position in the input sequence; leading to improved context sensitivity through
eﬃcient use of parallelization. Similarly, advances in deep reinforcement learning has showed
that only small sets of demonstration samples can signiﬁcantly accelerate the learning process
(Hester et al., 2018). In fact, what is surprising is not the general trend that shows that
learning is computationally hard: it is rather that we lack rigorous explanations for why some
learning systems seem to generalize well in practice. This is known as the “paradox of deep
learning”, which centers around understanding the empirical success of deep learning despite
the absence of theoretical explanations (Kawaguchi et al., 2017; Neyshabur et al., 2017; Arpit
et al., 2017; Zhang et al., 2021). In turn, this generates a range of convoluted issues that
are more or less unique for machine learning. For instance, what does it mean that a large
language model — having trained on large parts of the internet — is ethical?132 How should
we understand requirements of transparency, explainability, robustness, safety, and fairness
of suﬃciently advanced “black box” systems? (Gunning et al., 2019; Amodei et al., 2016;
Gabriel, 2020; Berk et al., 2021).133
While such issues deserve attention in their own right, there is a particular caveat that
follows from our complexity analysis: namely, the role of inductive biases and their moral
justiﬁcation. In some strong sense, the success of learning systems — e.g., training eﬃciency
and predictive accuracy — seems inversely proportional to the inductive assumptions it
exploits, as well as the problems of induction it introduces. I.e., for moral learning to work,
we need to have a relatively clear idea of the performance measure — e.g., in terms of some
predeﬁned score, goal, or objective function — of the moral problem we want the learning
system to tackle, or the moral behavior we want it to exhibit. As such, one might question
whether existing moral learning systems can generate any “new” or “genuine” moral insight,
as they merely train on some given data ﬁltered through some given inductive biases. Similar
to divine command and legal positivism, it presuppose that we have an answer to the questions
we seek. Thus, the problem of moral machine learning does not reside in the computational
complexity of learning as such, but rather, in justifying the moral assumptions we need to
exploit in order for induction to work. As elegantly put by Karl Popper (1962):
In constructing an induction machine we, the architects of the machine, must
decide a priori what constitutes its ‘world’; what things are to be taken as similar
or equal; and what kind of ‘laws’ we wish the machine to be able to ‘discover’ in its
132See Liang et al. (2022) for a “holistic” evaluation of large language models using multiple metrics and
test cases.
133Recent work in algorithmic fairness indicates that there are inevitable trade-oﬀs between, on the one
hand, diﬀerent concepts of fairness, and on the other, between fairness and accuracy (Berk et al., 2021).
68

--- Page 69 ---

‘world’. In other words we must build into the machine a framework determining
what is relevant or interesting in its world: the machine will have its ‘inborn’
selection principles. The problems of similarity will have been solved for it by its
makers who thus have interpreted the ‘world’ for the machine. (p. 48)
7. Moral Tractability for Minds and Machines
First, we oﬀered three possible interpretations of how to analyze the complexity of ethics
based on Marr’s three levels of analysis. We then proceeded to analyze a range of ethical
problems for causal engines, rule-followers, and learners. The results are summarized in
Table 3. Based on the surveyed results, what can computational complexity teach us about
morality? In this section, we will discuss the consequences for moral machines (7.1) and
human morality (7.2), the explanatory prospects of the Moral Tractability Thesis (7.3), along
with limitations (7.4) and venues for future work (7.5).
7.1. Consequences for the Prospects of Moral Machines
What consequences do intractability results have for the prospects of moral machines?
First and foremost, due to the intractability (and undecidability) stemming from combinatorics
of action plans (4.1), probabilistic causal inference (4.2), dynamic and partially observable
environments (4.3), general rules (5.1), strategic dynamics (5.1.3), logic (5.2), semantics
(5.2.3) and learning (6.1), we can ﬁrmly conclude that perfect moral machines are impossible.
In many cases, suboptimal approximations of solutions are also intractable. Instead, the
developers of moral machines should strive for “best possible” on the basis of constrained
resources. Similar conclusions have been made — although not as formally — by Brundage
(2014); Mabaso (2021); Hew (2014); Hagendorﬀand Danks (2022), and should be no surprise
to scholars familiar with bounded rationality (Simon, 1955, 1990; Rubinstein, 1998; Russell
and Subramanian, 1994) or bounded ethicality (Bazerman and Tenbrunsel, 2011; Tenbrunsel
and Messick, 2004). Nevertheless, the presented work should also be helpful in pinpointing
the type of complexity that bounded computational agent’s face in the realm of ethical
decision-making, and the relevant trade-oﬀs between optimality and feasibility it presents. It
should therefore be informative for debates on artiﬁcial moral agents, as it draws the question
of whether artiﬁcial moral agents are practically feasible or normatively desirable closer to the
de facto dimensions of AI methods; as opposed to centering on the uniquely human capacities
that existing AI systems lack (Stenseke, 2023).
In a similar vein, the results should also be illuminating for the further development of
artiﬁcial systems implemented in moral domains. In particular, the complexity of ethical
problems highlights the intimate relationship between the cognitive capacities of agents and
moral resources such as time, memory, knowledge, communication, learning, and heuristics.
However, it also presents a strong implementation-variance with regard to moral resources,
which potentially obfuscates any general notion of practical moral competence. I.e., while it
may be possible to identify the available resources for a particular agent in a given context,
and how the resources can be eﬀectively utilized and combined to yield competent ethical
behavior, it is diﬃcult to generalize such insights to any agent in any context. For instance,
what may be considered a competent ethical decision for a social robot in a classroom
diﬀers signiﬁcantly from the ethical competence required in high-speed traﬃc situations. The
69

--- Page 70 ---

Problem
Results
Combinatorics (4.1)
Optimal plan of n unordered actions
Θ(2n)
Optimal plan of n ordered actions
Θ(n!)
STRIPS and Propositional planning
PSPACE-complete (Bylander, 1991, 1994)
Bayesian Inference (4.2)
Exact inference
#P-complete (Roth, 1996)
Most Probable Explanation (MPE)
NP-complete (Shimony, 1994)
Maximum a posteriori hypothesis (MAP)
NPPP-complete (Park and Darwiche, 2004)
Approximate exact inference
NP-hard (Dagum and Luby, 1993)
Approximate MPE
NP-hard (Abdelbar and Hedetniemi, 1998)
Partial MAP
NP-hard (Park and Darwiche, 2004)
Sequential Decision-making (4.3)
Finite MDP
From PL to EXPSPACE-complete (Mundhenk et al., 2000)
Finite POMDP
PSPACE-complete (Papadimitriou and Tsitsiklis, 1987)
Inﬁnite POMDP
Undecidable (Madani et al., 2003)
Restless Bandit
PSPACE-hard (Papadimitriou and Tsitsiklis, 1994)
Strategic Dynamics (5.1)
Finite I-POMDP
PSPACE-complete (Papadimitriou and Tsitsiklis, 1987)
Decentralized MDP
NEXP-hard (Bernstein et al., 2002)
2-player Nash Equilibrium (NE)
PPAD-complete (Chen et al., 2009)
Maximum Egalitarian NE (Max NE)
NP-complete (Gilboa and Zemel, 1989)
Approximate Max NE
NP-complete (Conitzer and Sandholm, 2008)
Pure strategy Bayesian NE
NP-hard (Conitzer and Sandholm, 2008)
Pure NE inﬁnite Markov Games
PSPACE-hard (Conitzer and Sandholm, 2008)
Pure NE ﬁnite Markov Games
NP-hard (Conitzer and Sandholm, 2008)
Correlated Equilibrium (CE)
P (Gilboa and Zemel, 1989)
Max CE
NP-hard (Papadimitriou and Roughgarden, 2008)
Logic (5.2)
SAT-FOL
Undecidable (Turing, 1936; Church, 1936)
SAT-PL
NP-complete (Cook, 1971)
Validity for Modal Logic
PSPACE-complete (K, T, S4), NP-complete (S5) (Ladner, 1977)
Multi-agent Modal Logic (MAML)
PSPACE-complete (Halpern and Moses, 1992)
MAML + Common Knowledge
EXPTIME-complete (Halpern and Moses, 1992)
Validity for Temporal Logic
PSPACE-complete (Sistla and Clarke, 1985; Spaan, 1993)
SAT-Propositional Dynamic Logic
EXPTIME-complete (Fischer and Ladner, 1979; Pratt, 1980)
SAT-Deontic STIT Logic
Undecidable (Schwarzentruber and Semmling, 2014)
Deontic Input/Output Logic
NP/co-NP-hard (Sun and Robaldo, 2017)
Descriptive complexity (5.2.1)
FOL
LH & AC0 (Immerman, 1998)
Least ﬁxed-point FOL
P (Immerman, 1982; Vardi, 1982)
SO∃, SO∀, & SOL
NP, co-NP, and PH, respectively (Fagin, 1974)
SOL with transitive closure
PSPACE (Immerman, 1989)
Least ﬁxed-point SOL
EXPTIME (Abiteboul et al., 1997)
Learning (6)
No Free Lunch (Wolpert, 1992, 1996; Schaﬀer, 1994)
Sample Complexity for PAC-learnability
O
  V CD(H)+ln 1
δ
ϵ

(Hanneke, 2016)
Proper Realizable PAC
From P to NP-hard (Pitt and Valiant, 1988)
Improper PAC
NP-hard (cryptographic assumptions) (Kearns and Valiant, 1994)
Proper Agnostic PAC
NP-hard (Feldman et al., 2012)
Table 3: Summary of the surveyed complexity results.
70

--- Page 71 ---

implementation-variance can be interpreted negatively: it shows that no general benchmarks
can be established so as to assess the ethical performance of computational systems. More
optimistically, it can also convey areas where domain- or problem-speciﬁc moral benchmarks
can be established in terms of resource-dependency (e.g., given limited time or information).
More directly, it points to venues where relevant benchmarks already exist: e.g., to ﬁnd
morally attractive equilibria in complex coordination games, minimize regret in multi-armed
bandit settings, constructing tractable logics for moral reasoning, or eﬃcient algorithms for
Bayesian inference.
It also shows that a lot of work remains to be done on the moral end of machine ethics. In
almost every instance, there is an uncomfortable trade-oﬀbetween optimality and feasibility,
and performance and eﬃciency; trade-oﬀs which themselves may need normative justiﬁcation.
However, while computer science may have shifted towards becoming an empirical science in
the advent of machine learning, our moral theories remain deeply rooted in theoretical ideals
of right and wrong, which may presuppose unrealistic access to oracles of rationality. This
brings out the open-ended tension between normative theory as standards of “ideal good”,
and normative theory as action-guiding heuristics to get suboptimal but feasible results. For
instance, if our moral theories assume unrealistic computations, how can we provide a solid
footing for their justiﬁcation in practice? Similarly, if the tension remains unresolved, we
cannot clearly determine cases whether a harmful action was due to a failure of competence,
or whether it was a moral wrongdoing. It also presents challenges for moral theories: e.g., an
agent that evaluates her actions according to NT1 might be better oﬀ(according to NT1) by
following the action-decisions provided by an alternative theory NT2.134 Thus, the critical
question is: upon what standards should we potentially revise our moral theories so as to
be feasible as decision-procedures with regard to the bounded and implementation-variant
resources of agents? In machine contexts, we believe such open-ended issues can be fruitfully
investigated under the lens of computational complexity, as it provides analytical means to
measure how resources relate to formal notions of performance. More practically, it provides
a venue to address what machines ought to do based on what they can do at all — and what
they can do eﬀectively — which in turn can convey the domains where computational systems
can be successfully applied to make competent ethical decisions.
7.2. Consequences for Human Morality
More broadly, what consequences do these results have for our understanding of human
morality? This ultimately depends on what one believes about the human mind, and more
particularly, whether and to what extent it is computational in nature.
The ones who
view humans as primarily cultural, social, and spiritual beings may ﬁnd the computational
perspective completely irrelevant for understanding human morality. Others, who attempt to
understand human behavior in terms of cognitive capacities, may ﬁnd it fruitful to assume
that human cognition has at least some particular characteristics and constraints, which
can be used to constrain the space of hypothesis. Simply put: assumptions about what the
human mind can and cannot do should be informative for our understanding of the human
134The typical example of such a “self-eﬀacing” theory is act utilitarianism ((Parﬁt, 1984), Sections 9 and
17), as an agent would produce more overall good by not following the prescriptions of act utilitarianism in
practice.
71

--- Page 72 ---

mind. From this latter view, the step towards embracing some form of computationalism
about the human mind becomes quite attractive, as it oﬀers a smorgasbord of additional
scientiﬁc tools; e.g., the use of computational architectures to model, test, and revise theories
about cognition and behavior. If we take this step, computational complexity becomes an
indispensable instrument, as it helps us constraint the space of possible computational theories
of human cognition. This view can be captured in the Tractable Cognition Thesis, which
states that computational models of cognitive abilities need to be computationally tractable,
given some reasonable conception of tractability (Van Rooij, 2008; Van Rooij et al., 2019).
Conversely, if a computational theory implies intractable computations, it indicates that
the theory is inadequate. A formal variant of the thesis is the P-cognition Thesis, which
asserts that cognitive functions are constrained by polynomial time. In cognitive science, the
P-Cognition thesis has explicitly been advanced as guide for computational-level theories
of human cognition by Cherniak (1986); Tsotsos (1990); Levesque (1989); Frixione (2001),
and is implicitly used as a constraining factor by a large group of cognitive psychologists.135
Furthermore, the observation that many NP-hard problems can in fact be eﬃciently solved
for some part of the input parameter has led to the argument that P-Cognition Thesis should
be replaced with the Fixed-Parameter Tractability thesis (Van Rooij, 2008), which states
that cognitive functions are restricted by polynomial time in the overall input size n, while
allowing for superpolynomial time in some part of its input parameter (Downey and Fellows,
2012). A related modeling paradigm is the concept of resource-rational cognition (Lieder and
Griﬃths, 2020), which addresses cognitive modeling in terms of the optimal use of limited
computational resources.
Thus, even if it remains unclear what kind of computer the human mind is (or whether it
can be meaningfully captured by any model of computation), tractability considerations — in
conjunction with cognitive modeling and experimental data — can work as a hypothesis that
helps us carve out the space of feasible theories of cognition. Naturally, this would also include
the functions that make up moral cognition. For instance, if we believe that humans perform
causal, strategical, or logical reasoning to produce competent moral behavior, tractability
considerations will directly serve to constrain the space of computational-level problems that
underpins moral behavior. In addition, if we have reason to believe that humans perform
these moral inferences in a speciﬁc way — e.g., using certain Bayesian, decision-theoretical,
or logical inference techniques — a complexity analysis will help to pinpoint the relevant
trade-oﬀs between performance and feasibility; trade-oﬀs which may directly relate to the
complexity results surveyed in this paper.
7.3. Moral Tractability Thesis
The role of tractability in theories about moral behavior and cognition can be formulated
as the Moral Tractability Thesis (MTT). It is a natural extension of the Tractable Cognition
Thesis and states that morality — moral behavior, moral problem-solving, and moral cognition
— are constrained by computational tractability (see Figure 4), given some reasonable model
of human moral cognition.136 The MTT is a hypothesis that points in both normative and
135See Van Rooij (2008) for a detailed treatment of the Tractable Cognition Thesis and its formal variants.
136Here, “reasonable” is intentionally ambiguous, as there is currently no consensus of the speciﬁc model of
computation that reﬂects the human brain. For a recent proposal, see Blum and Blum (2022).
72

--- Page 73 ---

Figure 4: The Moral Tractability Thesis (MTT) states that the set of possible moral cognitive functions
are subject to tractability constraints. More formally, this can be framed as a subset of functions that are
ﬁxed-parameter tractable for suﬃciently small input parameters, which also includes the set of functions
computable in polynomial time. We believe the MTT can serve (1) as a meta-ethical standard for the
action-guidance of normative theory, in the sense that action-guidance should be feasible with respect to
agents’ resources, (2) as a guide for normative judgements and responsibility in cases where it is unclear
whether an agent acted wrongfully due to a failure of cognitive constraints, (3) as an experimental paradigm
in studies of human moral cognition and psychology, and (4) as a remedy to the tension between feasibility
and performance in moral contexts.
73

--- Page 74 ---

descriptive directions:
(1) MTT as a meta-ethical standard for normative theory — MTT yields a meta-ethical
point that stresses that the computational problems imposed by a moral theory also should
be tractable with regard to the resources of an agent following the theory; i.e., to the extent
the theory aims to provide any meaningful action-guidance for the agent. If not, it could
suggest that the moral theory imposes unrealistic demands in relation to the agent’s resources,
and therefore, the theory should be revised so as to constrain the space of problems the agent
can be expected to solve. As such, it could help to exclude the “self-eﬀacing” theories of
normative action-guidance from the ones that respects the limited capacities of agents. More
practically, it can help us to identify the situations and contexts in which a certain form
action-guidance can be expected to produce better results than competing alternatives.
(2) MTT as a guide for normative judgements and responsibility — In situations where an
agent behaves immorally, MTT can help us to answer the question whether the agent’s immoral
behavior was due to a failure of morality and rationality. For instance, if the computational
demands are fair for some reasonable conception of human moral competence, it might point
to the lack of a certain moral resource in the situation at hand (e.g., time, memory, knowledge,
learning, or rationality demands). If no such absence can can be identiﬁed, it can also serve
as grounds for holding the agent responsible for their immoral behavior.
(3) MTT as an experimental paradigm — In the descriptive direction, MTT can provide a
delimiting factor for existing paradigms studying human morality; from the computational
modeling of human moral cognition to experimental studies in moral psychology. More
precisely, MTT can be used to identify the principles and algorithms that underpin cog-
nitive processes in moral decision-making, reveal relevant trade-oﬀs between feasibility vs
performance, and further investigate the role of resources in speciﬁc moral contexts.
(4) MTT as a remedy to feasibility vs optimality — Another feature of MTT is that it can
help to resolve open-ended tensions between feasibility and performance in moral contexts, in
the sense that the latter is directly constrained by the former. For instance, if we assume
that there is a ﬁxed point which yields the optimal moral value, MTT implies that there
is an action-guiding theory that yields the highest possible moral value with regard to the
resources of the acting agent.137 The same idea can be articulated for moral communities:
recipes for action-guidance that produces the highest moral prosperity — e.g., joint well-fare,
or mutually agreed-upon moral values — with regard to the mutually shared resources of
agents in the moral community. In other words, there may be normative action-guidance
that provides the morally optimal use of bounded cognitive resources; a resource-rational
moral theory (Lieder and Griﬃths, 2020). From a game-theoretic point of view, this can be
interpreted as the optimal moral equilibrium point (e.g., maximum joint beneﬁt) within the
space of the agents’ bounded resources (Figure 4).
7.4. Limitations
There are several of gaps and limitations for the explanatory viability of moral complexity
analyses in general and the MTT in particular. We will brieﬂy address some of these along
three broad questions: (i) How and to what extent is computational complexity relevant for
137More moderately, instead of an optimal, we can assume that there is a justiﬁed threshold for moral
permissibility on the basis of some notion of moral value.
74

--- Page 75 ---

the development and deployment of “morally competent” AI systems in real-world domains?
(ii) What aspects of human morality are not captured by a complexity analysis? (iii) What
can complexity tell us about the human use of morally informed AI systems (e.g., AI systems
that are designed and used to extend or augment human moral capacities)?
(i) It should be stressed that the computational problems analyzed in this paper may have
limited relevance for many real-world implementations of AI systems in moral domains. For
instance, what can computational complexity, if anything, tell us about the moral behavior in
domains such as autonomous driving, social assistive robotics, and natural language processing?
While the overarching goal of a self-driving vehicle may be summarized as “drive safely from
point A to B”, it encompasses a vast set of smaller sub-tasks and goals — e.g., path planning,
adhere to traﬃc rules, crossing this and that intersection — for which it utilizes a cluster of
distributed capacities — e.g., sensors, motors, maps, simulations — that makes up competent
autonomous driving (Badue et al., 2021). Thus, a complexity analysis of an autonomous car’s
moral competence oﬀers little insight unless it is based on the speciﬁc car’s capacities. As
noted in section 6, some technical-ethical challenges that arise for large language models may
present the inverse problem of constraining a general capacity to produce text (e.g., so as to
adhere to human principles and values). That is, instead of learning an optimal solution from
the largest possible search-space — e.g., by training on vast amounts of human-generated text
— the task may be to constrain the search via some justiﬁed inductive bias that aligns with
human values. Similarly, the most widely discussed ethical issues that pervade social assistive
robotics — e.g., deception, dignity, trust, and recognition in Human-Robot Interaction (HRI)
— are far removed from the formal notions of causal, logical, and strategic inference discussed
in this work (Boada et al., 2021).
The main point is that each domain presents its distinct set of technical and ethical
challenges that need to be addressed with respect to the domain’s unique conditions. In
turn, these challenges may have little to do with the computation of applied normative ethics,
but rather, depend on some speciﬁc normative requirements that are presupposed by certain
human practice (Behdadi and Munthe, 2020). However, if AI systems are developed to behave
in accordance with normative ethics, the surveyed complexity results have an overarching
relevancy for such endeavors, just as they remain central to several prominent paradigms
for the advancements of computing; e.g., probabilistic inference, knowledge-systems, and
learning. In a more trivial sense, even if the aim is to merely supplement AI systems with
some capacities needed for some form of ethical decision-making, the behavior of such systems
would also be constrained by limited computational resources. A resource-rational complexity
analysis could therefore help to identify the sort of ethical problems that can be solved by
machines; the ones that can be solved eﬃciently, where there is room for improvement, as
well as pinpoint the relevant resources and trade-oﬀs.
(ii) Another important gap that needs to be addressed is the diﬀerence between human
morality and the computational form of applied normative ethics explored in this paper. It
should be strongly emphasized that, although the surveyed results have direct implications
for computational systems, any potential consequences for our understanding of human
morality rest on speculative assumptions. As discussed in 3, ethics is an ambiguous and
multifaceted concept; what sort of ethical problems humans actually “solve”, how they solve
them, and what they use to solve them (e.g., emotions, reasoning) are all open questions
with many possible and elaborate answers. Similarly, while the aim of normative ethics is to
75

--- Page 76 ---

ﬁnd generally applicable standards of “good” and “bad”, it is but a small conversation of
the broader landscape that makes up ethical life. Adopting a more skeptical view, one could
even claim that normative ethics — as theoretically construed in contemporary Anglophone
analytical philosophy — does not have any bearing on ethical life at all (Stocker, 1977). To
that end, it might be odd to imagine that humans put together ethical action-plans (or optimal
salads) using exhaustive search methods (4.1), make causal inferences using (arbitrarily) large
Bayesian Networks (4.2), compute egalitarian Nash equilibria in their strategic interactions
(5.1.5), or check behavioral norm-compliance with regards to possible worlds (5.2.2). Humans
may employ a broad range of resources in their everyday ethical life — e.g., emotions and
motivations, guilt and shame, spirituality and ideology, critical reﬂection and theory of mind —
that are uncounted for in this analysis. Thus, the presented analysis — from computation, to
algorithm, to implementation — should not stop researchers from pursuing other investigatory
directions that may be fruitful for understanding the intricate and numerous forms of human
morality; e.g., the embodied and felt, the shared dependencies and vulnerabilities of personal
relationships, and the norms and institutions of society and culture.
Still, if one believes that cognitive tractability and MTT holds any merit, complexity can
provide a guiding light into the vast intersection between normative, descriptive, and applied
ethics. Even if one just accepts that computational limitations have some importance for some
forms of human moral behavior, it suﬃces as a reason to further investigate those limitations.
Furthermore, it is not unreasonable to believe that many human beings are able to and do —
at least occasionally — follow deontological and consequentialist decision-procedures, and,
following virtue ethics, learn to foster the psychological dispositions that enable them to
become better moral persons; although the de facto cognitive procedures that underpin these
processes might look diﬀerent from the ones considered in this work. To that end, it would
be rather odd to view these normative theories as completely separated from the cognitive
capacities of humans; for instance, it seems hard to explain the practical success or popularity
of certain moral heuristics (e.g., principles or theories) unless they were applicable — decidable
and tractable — for humans in moral communities (Alexander, 2007). In some cases, it even
seems reasonable to believe that some of these heuristics are motivated on the basis of their
computational eﬃciency; e.g., the computational eﬃciency of adhering to moral rules (5.3).
Thus, while we should respect the vast gap between human and computational forms of
morality, it would be unwise to exclude the possibility that there are more or less rigorous
patterns in the cognitive processes that support the former, which in turn are amendable for
formal investigation via the latter.
(iii) Another large area that is omitted in this paper is the integrative use of AI systems in
human moral behavior. I.e., we have mainly considered the ethical behavior of computational
systems in isolation, without any ‘human-in-the-loop’. As such, we have ignored the integrative
prospects of how AI systems can be utilized to support or augment human ethical decision-
making. Machines are, after all, a large cluster of computational methods that are employed
to carry out the aims of its human users. In turn, this might point to a research area that
can also be illuminated by computational complexity: how AI systems can foster and support
moral prosperity in human practices in light of constrained resources (Vallor, 2015; Giubilini
and Savulescu, 2018). For instance, many problems that are intractable for humans may be
tractable for machines, and conversely, many problems that are intractable for machines may
be tractable for machines. The guiding question is thus: on the basis of resource constraints,
76

--- Page 77 ---

how can AI be developed and used so as to expand rather than constrain the space of moral
reasoning (Vallor, 2016)?
7.5. Future Work
There are a number of interesting venues to further explore moral tractability for minds
and machines beyond the ones already described. First, it should be stressed that although
this work has discussed a number of complexity results relevant for moral behavior, it has
circumvented an even greater amount. For most of the computational problem discussed, there
are hundreds of related results that would be relevant to consider under diﬀerent conditions
and assumptions. In fact, we have omitted results from entire ﬁelds of complexity theory —
e.g., parameterized, communication, proof, and circuit complexity — that could yield further
insights about the limitations of moral computation. Out of the discussed problems, there
are two areas in particular that we believe deserves a more detailed investigation: (i) the
sample complexity and regret-minimization of (moral) machine learning, and (ii) algorithmic
game theory (in conjunction with algorithmic design theory). The reason for pursuing the
ﬁrst is that the complexity of machine learning in moral contexts remains relatively poorly
understood; especially given issues such as explainability (Gunning et al., 2019), induction
(Sterkenburg and Gr¨unwald, 2021), and the “paradox of deep learning” (Zhang et al., 2021).
Another reason is that machine learning is the main vehicle behind the modern advancements
in AI development. More urgently, learning systems are already deployed in a vast range of
human practices, including areas that may involve salient forms of moral decision-making
such as health care, autonomous driving, law, policing, and education.
The reason for pursuing (ii) is that game theory provides a unifying framework for the formal
study of interactions, which in turn makes interactions amendable for algorithmic modeling
and analysis. As such, we believe it could provide fertile synergies between historically distinct
ﬁelds such as computer science, moral theory, evolutionary biology, behavioral economics,
and social science. For instance, if we adopt the view that normative theories converge more
than they disagree,138 a resource-rational algorithmic game-theoretic analysis could help to
identify the conditions under which certain theories are more practically viable than others.
E.g., what sort of cognitive abilities and computational resources are required for a certain
moral heuristic — e.g. an action-guiding normative theory — to support the highest possible
moral prosperity for a community of agents? What sort of moral behaviors can be eﬀectively
computed or justiﬁed, and what behaviors can only be learned? Ideally, such investigations
could not only illuminate the speciﬁc resources a computational agent need in order to be
morally competent, but explain the very resource-rational rationales that underpin our most
prominent ethical theories.
8. Conclusion
We have surveyed a large but far from exhaustive set of complexity results and discussed
their relevance for minds and machines in the moral realm. Ultimately, we believe it opens
138For instance, Parﬁt (2011) argues that it is erroneous to believe that there are profound disagreements
between consequentialists, contractualists, and Kantians, writing: “these people are climbing the same
mountain on diﬀerent sides” (p. 385).
77

--- Page 78 ---

up interesting interdisciplinary spaces between machine ethics, moral philosophy, and moral
cognitive psychology, which will hopefully inspire new directions, not only in the engineering
of moral machines, but in understanding the complex science of morality.
Appendix
Complexity Classes
AC0 — Class of decision problems solvable by a family (one for each possible input-size)
of constant-depth unlimited-fanin circuits, where the number of gates is bounded by
some polynomial in the size of the input.
LH — Class of decision problems solvable by an alternating TM with a bounded number
of alternations in time O(log n). See Immerman (1998) for a detailed exposition.
PL — Class of decision problems solvable by a probabilistic TM constrained by space
O(log n), with an error probability ϵ < 1/2 (“Probabilistic Logarithmic Space”).
P — Class of decision problems solvable by a deterministic TM constrained by time
O(poly(n)).
PP — Class of decision problems solvable by a probabilistic TM constrained by time
O(poly(n)), with an error probability ϵ < 1/2.
FTP — Class of decision problems solvable by a deterministic TM constrained by time
O(f(k)nc), where f is a function that only depends on the parameter k, and c is a
constant. See Downey and Fellows (2012) for the deﬁnite introduction to parameterized
complexity.
NP — Class of decision problems solvable by a non-deterministic TM constrained by
time O(poly(n)). Alternatively, class of decision problems for which “Yes”-instances are
veriﬁable in polynomial time by a deterministic TM.
co-NP — The complement set of NP. Class of decision problems for which “No”-
instances are veriﬁable in polynomial time by a deterministic TM.
#P — Class of function problems f(x), where f is the number of accepting paths of
a non-deterministic TM constrained by time O(poly(n)). Informally, it is the set of
counting problems associated with NP; i.e., where NP decision problems ask “are there
any”, #P function problems asks “how many”.
NPPP — Class of decision problems solvable by a non-deterministic TM constrained
by time O(poly(n)) with access to an oracle for problems in PP.
TFNP — Class of function problems solvable by a non-deterministic TM constrained
by time O(poly(n)) where a solution is guaranteed to exist (“Total Function Non-
deterministic Polynomial”).
78

--- Page 79 ---

PPAD — The subclass of TFNP where functions are guaranteed to be total — i.e., a
solution is guaranteed to exist — in virtue of the parity argument on directed graphs
(“Polynomial Parity Arguments on Directed graphs”). See Papadimitriou (1994) for a
detailed exposition.
PH — The union of classes in the polynomial hierarchy. It can be deﬁned recursively
using oracle machines: given P = ∆P
0 = ΣP
0 = ΠP
0 , we deﬁne PΣP
i = ∆P
i+1, NPΣP
i = ΣP
i+1,
and co-NPΣP
i = ΠP
i+1, to express the union:
PH =
∞
[
i=0
∆P
i ∪ΣP
i ∪ΠP
i
(8)
PSPACE — Decision problems solvable by a deterministic TM constrained by space
O(poly(n)).
EXPTIME — Decision problems solvable by a deterministic TM constrained by time
O(2poly(n)).
NEXPTIME — Decision problems solvable by a non-deterministic TM constrained
by time O(2poly(n)). Often denoted NEXP.
EXPSPACE — Decision problems solvable by a deterministic TM constrained by
space O(2poly(n)).
Conﬂict of Interest Statement
The author declare that the research was conducted in the absence of any commercial or
ﬁnancial relationships that could be construed as a potential conﬂict of interest.
Author Contributions
JS is the sole contributor of the work presented in the article.
Funding
This work was partially supported by the Wallenberg AI, Autonomous Systems and
Software Program – Humanities and Society (WASP-HS) funded by the Marianne and Marcus
Wallenberg Foundation and the Marcus and Amalia Wallenberg Foundation.
Acknowledgments
The author is especially grateful to Per Austrin (KTH Royal Institute of Technology) and
Felix Lindner (Universit¨at Ulm) for their insightful feedback on computational complexity.
The author is also thankful to his colleagues at the Department of Philosophy and Cognitive
Science at Lund University for providing helpful comments on previous versions of the
paper. In particular, the author wants to acknowledge Niklas Dahl for answering countless
queries about logic and semantics, Karl Samson and Gustav Stenseke Arup for input on the
79

--- Page 80 ---

relationship between legality and morality, and Christian Balkenius, Bj¨orn Petersson, Ylva
von Gerber, Sandra Lofs Midelf, Jiwon Kim, Alexander Velichkov, Trond Arild Tjøstheim,
and Alfred Stenseke for their feedback. Finally, the author is grateful for participants of the
Higher Seminar in Practical Philosophy (Lund University), the PhD seminar in philosophy
(Lund University), the WASP-HS Winter Conference 2022, the philosophical colloquium at
Georg-August-Universit¨at, and the seminar at Institut f¨ur K¨unstliche Intelligenz (Universit¨at
Ulm), where earlier parts of the paper where presented.
References
Aaronson, S., 2013. Why philosophers should care about computational complexity. Com-
putability: Turing, G¨odel, Church, and Beyond 261, 327.
Abdelbar, A.M., Hedetniemi, S.M., 1998. Approximating maps for belief networks is np-hard
and other theorems. Artiﬁcial Intelligence 102, 21–38.
Abel, D., MacGlashan, J., Littman, M.L., 2016. Reinforcement learning as a framework for
ethical decision making, in: AAAI Workshop: AI, Ethics, and Society, Phoenix, AZ. p. 02.
Abiteboul, S., Vardi, M.Y., Vianu, V., 1997.
Fixpoint logics, relational machines, and
computational complexity. Journal of the ACM (JACM) 44, 30–56.
Adam, S.P., Alexandropoulos, S.A.N., Pardalos, P.M., Vrahatis, M.N., 2019. No free lunch
theorem: A review. Approximation and optimization , 57–82.
Albrecht, S.V., Stone, P., 2018. Autonomous agents modelling other agents: A comprehensive
survey and open problems. Artiﬁcial Intelligence 258, 66–95.
Alexander, J.M., 2007. The structural evolution of morality .
Allen, C., Smit, I., Wallach, W., 2005. Artiﬁcial morality: Top-down, bottom-up, and hybrid
approaches. Ethics and information technology 7, 149–155.
Amaldi, E., Kann, V., 1998. On the approximability of minimizing nonzero variables or
unsatisﬁed relations in linear systems. Theoretical Computer Science 209, 237–260.
Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., Man´e, D., 2016. Concrete
problems in ai safety. arXiv preprint arXiv:1606.06565 .
Anderson, M., Anderson, S.L., 2008. Ethel: Toward a principled ethical eldercare system,
in: AAAI Fall Symposium: AI in Eldercare: New Solutions to Old Problems, AAAI Press,
Arlington, Virginia. pp. 4–11.
Anderson, M., Anderson, S.L., 2011. Machine ethics. Cambridge University Press.
Angluin, D., Laird, P., 1988. Learning from noisy examples. Machine Learning 2, 343–370.
Annas, J., 2011. Intelligent virtue. Oxford University Press.
Anscombe, G.E.M., 1958. Modern moral philosophy. Philosophy 33, 1–19.
80

--- Page 81 ---

Applebaum, B., Barak, B., Xiao, D., 2008. On basing lower-bounds for learning on worst-case
assumptions, in: 2008 49th Annual IEEE Symposium on Foundations of Computer Science,
IEEE. pp. 211–220.
Arkin, R.C., 2007. Governing lethal behavior: embedding ethics in a hybrid deliberative/hybrid
robot architecture. Report. Report GIT-GVU-07-11, Atlanta, GA: Georgia Institute of
Technology’s GVU . . . .
Arkoudas, K., Bringsjord, S., Bello, P., 2005. Toward ethical robots via mechanized deontic
logic, in: AAAI fall symposium on machine ethics, The AAAI Press Menlo Park, CA, USA.
pp. 17–23.
Armstrong, S., 2015. Motivated value selection for artiﬁcial agents, in: AAAI Workshop: AI
and Ethics, AAAI Press, Palo Alto, California.
Arpit, D., Jastrzebski, S., Ballas, N., Krueger, D., Bengio, E., Kanwal, M.S., Maharaj, T.,
Fischer, A., Courville, A., Bengio, Y., et al., 2017. A closer look at memorization in deep
networks, in: International conference on machine learning, PMLR. pp. 233–242.
Asimov, I., 1942. Runaround. Astounding Science Fiction 29, 94–103.
˚Astr¨om, K.J., 1965. Optimal control of markov processes with incomplete state information.
Journal of mathematical analysis and applications 10, 174–205.
Auer, P., Cesa-Bianchi, N., Freund, Y., Schapire, R.E., 1995. Gambling in a rigged casino: The
adversarial multi-armed bandit problem, in: Proceedings of IEEE 36th annual foundations
of computer science, IEEE. pp. 322–331.
Aumann, R.J., 1974. Subjectivity and correlation in randomized strategies. Journal of
mathematical Economics 1, 67–96.
Aumann, R.J., 1987. Correlated equilibrium as an expression of bayesian rationality. Econo-
metrica: Journal of the Econometric Society , 1–18.
Aumann, R.J., 2016.
16. acceptable points in general cooperative n-person games, in:
Contributions to the Theory of Games (AM-40), Volume IV. Princeton University Press,
pp. 287–324.
Austrin, P., Braverman, M., Chlamt´aˇc, E., 2013. Inapproximability of np-complete variants
of nash equilibrium. Theory of Computing 9, 117–142.
Axelrod, R., Hamilton, W.D., 1981. The evolution of cooperation. science 211, 1390–1396.
Azad-Manjiri, M., 2014. A new architecture for making moral agents based on c4. 5 decision
tree algorithm. International Journal of Information Technology and Computer Science
(IJITCS) 6, 50–57.
B¨ackstr¨om, C., Nebel, B., 1995. Complexity results for sas+ planning. Computational
Intelligence 11, 625–655.
81

--- Page 82 ---

Badue, C., Guidolini, R., Carneiro, R.V., Azevedo, P., Cardoso, V.B., Forechi, A., Jesus,
L., Berriel, R., Paixao, T.M., Mutz, F., et al., 2021. Self-driving cars: A survey. Expert
Systems with Applications 165, 113816.
Baker, C.L., Tenenbaum, J.B., Saxe, R.R., 2007. Goal inference as inverse planning, in:
Proceedings of the Annual Meeting of the Cognitive Science Society.
Balbiani, P., Herzig, A., Troquard, N., 2008. Alternative axiomatics and complexity of
deliberative stit theories. Journal of Philosophical Logic 37, 387–406.
Bales, R.E., 1971. Act-utilitarianism: Account of right-making characteristics or decision-
making procedure? American Philosophical Quarterly 8, 257–265.
Barsalou, L.W., 1999. Perceptual symbol systems. Behavioral and brain sciences 22, 577–660.
Bauer, W.A., 2020. Virtuous vs. utilitarian artiﬁcial moral agents. AI & SOCIETY 35,
263–271.
Bazerman, M.H., Tenbrunsel, A.E., 2011. Blind spots, in: Blind Spots. Princeton University
Press.
Beall, J.C., 2007. Revenge of the liar: New essays on the paradox. OUP Oxford.
Behdadi, D., Munthe, C., 2020. A normative approach to artiﬁcial moral agency. Minds and
Machines 30, 195–218.
Ben-David, S., Eiron, N., Long, P.M., 2003. On the diﬃculty of approximately maximizing
agreements. Journal of Computer and System Sciences 66, 496–514.
Bennett, J.F., 1976. Linguistic behaviour .
Bentham, J., 1789. An Introduction to the Principles of Morals and Legislation. Garden City:
Doubleday (1961).
Berberich, N., Diepold, K., 2018. The virtuous machine-old ethics for new technology? arXiv
preprint arXiv:1806.10322 .
Berk, R., Heidari, H., Jabbari, S., Kearns, M., Roth, A., 2021. Fairness in criminal justice
risk assessments: The state of the art. Sociological Methods & Research 50, 3–44.
Berner, C., Brockman, G., Chan, B., Cheung, V., Debiak, P., Dennison, C., Farhi, D., Fischer,
Q., Hashme, S., Hesse, C., 2019. Dota 2 with large scale deep reinforcement learning. arXiv
preprint arXiv:1912.06680 .
Bernstein, D.S., Givan, R., Immerman, N., Zilberstein, S., 2002. The complexity of de-
centralized control of markov decision processes. Mathematics of operations research 27,
819–840.
Bernstein, E., Vazirani, U., 1997. Quantum complexity theory. SIAM Journal on computing
26, 1411–1473.
82

--- Page 83 ---

Bicchieri, C., 2005. The grammar of society: The nature and dynamics of social norms.
Cambridge University Press.
Binder, K., Heermann, D., Roelofs, L., Mallinckrodt, A.J., McKay, S., 1993. Monte carlo
simulation in statistical physics. Computers in Physics 7, 156–157.
Blackburn, S., 1992. Through thick and thin, in: Proceedings of the Aristotelian Society, pp.
284–99.
Blackburn, S., 1998. Ruling passions. Oxford University Press Oxford.
Block, N., 2019. What is wrong with the no-report paradigm and how to ﬁx it. Trends in
Cognitive Sciences 23, 1003–1013.
Blum, L., Blum, M., 2022. A theory of consciousness from a theoretical computer science
perspective: Insights from the conscious turing machine. Proceedings of the National
Academy of Sciences 119, e2115934119.
Blumer, A., Ehrenfeucht, A., Haussler, D., Warmuth, M.K., 1989. Learnability and the
vapnik-chervonenkis dimension. Journal of the ACM (JACM) 36, 929–965.
Boada, J.P., Maestre, B.R., Gen´ıs, C.T., 2021. The ethical issues of social assistive robotics:
A critical literature review. Technology in Society 67, 101726.
Bodlaender, H.L., 1994. A tourist guide through treewidth. Acta cybernetica 11, 1.
Bouneﬀouf, D., Rish, I., 2019. A survey on practical applications of multi-armed and contextual
bandits. arXiv preprint arXiv:1904.10040 .
Brandenburger, A., Dekel, E., 1993. Hierarchies of beliefs and common knowledge. Journal of
Economic Theory 59, 189–198.
Brandom, R., 1994. Making it explicit: Reasoning, representing, and discursive commitment.
Harvard university press.
Brandom, R., 2006. Kantian lessons about mind, meaning, and rationality. The Southern
journal of philosophy 44, 49–71.
Brandt, R.B., 1979. A theory of the good and the right .
Brentano, F., 1874. Psychology from an empirical standpoint .
Bringsjord, S., Taylor, J., 2012. The divine-command approach to robot ethics. Robot ethics:
The ethical and social implications of robotics , 85–108.
Broome, J., 1987. Utilitarianism and expected utility. The Journal of philosophy 84, 405–422.
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P., Neelakantan, A.,
Shyam, P., Sastry, G., Askell, A., et al., 2020. Language models are few-shot learners.
Advances in neural information processing systems 33, 1877–1901.
83

--- Page 84 ---

Bro˙zek, B., Janik, B., 2019. Can artiﬁcial intelligences be moral agents?
New ideas in
psychology 54, 101–106.
Brundage, M., 2014. Limitations and risks of machine ethics. Journal of Experimental &
Theoretical Artiﬁcial Intelligence 26, 355–372.
Bubeck, S., Wang, T., Viswanathan, N., 2013. Multiple identiﬁcations in multi-armed bandits,
in: International Conference on Machine Learning, PMLR. pp. 258–265.
Bylander, T., 1991. Complexity results for planning., in: IJCAI, pp. 274–279.
Bylander, T., 1994. The computational complexity of propositional strips planning. Artiﬁcial
Intelligence 69, 165–204.
Cai, Y., Papadimitriou, C., 2014. Simultaneous bayesian auctions and computational com-
plexity, in: Proceedings of the ﬁfteenth ACM conference on Economics and computation,
pp. 895–910.
Camerer, C.F., Ho, T.H., Chong, J.K., 2004. A cognitive hierarchy model of games. The
Quarterly Journal of Economics 119, 861–898.
Campbell, M.S., Marsland, T.A., 1983. A comparison of minimax tree search algorithms.
Artiﬁcial Intelligence 20, 347–367.
de Campos, C.P., 2020. Almost no news on the complexity of map in bayesian networks, in:
International Conference on Probabilistic Graphical Models, PMLR. pp. 149–160.
Capraro, V., Rand, D.G., 2018. Do the right thing: Experimental evidence that preferences
for moral behavior, rather than equity or eﬃciency per se, drive human prosociality.
Forthcoming in Judgment and Decision Making .
Carnap, R., 1947. Meaning and necessity: A study in semantics and modal logic .
Casebeer, W.D., 2003. Moral cognition and its neural constituents. Nature Reviews Neuro-
science 4, 840–846.
Casella, G., Berger, R.L., 2021. Statistical inference. Cengage Learning.
Cassandra, A.R., Kaelbling, L.P., Littman, M.L., 1994. Acting optimally in partially observable
stochastic domains, in: Aaai, pp. 1023–1028.
Cervantes, J.A., L´opez, S., Rodr´ıguez, L.F., Cervantes, S., Cervantes, F., Ramos, F., 2020.
Artiﬁcial moral agents: A survey of the current status. Science and engineering ethics 26,
501–532.
Cesa-Bianchi, N., Lugosi, G., 2006. Prediction, learning, and games. Cambridge university
press.
Chalmers, D.J., 1997. The conscious mind: In search of a fundamental theory. Oxford
Paperbacks.
84

--- Page 85 ---

Chatterjee, K., Chmelik, M., Tracol, M., 2016. What is decidable about partially observable
markov decision processes with ω-regular objectives. Journal of Computer and System
Sciences 82, 878–911.
Chen, X., Deng, X., Teng, S.H., 2009. Settling the complexity of computing two-player nash
equilibria. Journal of the ACM (JACM) 56, 1–57.
Cherniak, C., 1986. Minimal rationality. Mit Press.
Church, A., 1936. A note on the entscheidungsproblem. The journal of symbolic logic 1,
40–41.
Cloos, C., 2005. The utilibot project: An autonomous mobile robot based on utilitarianism,
in: Machine Ethics: Papers from the 2005 AAAI Fall Symposium, AAAI Press, Menlo
Park, California. pp. 38–45.
Cobham, A., 1965. The intrinsic computational diﬃculty of functions .
Cofıno, A.S., Cano, R., Sordo, C., Gutierrez, J.M., 2002. Bayesian networks for probabilistic
weather prediction, in: 15th Eureopean Conference on Artiﬁcial Intelligence (ECAI),
Citeseer.
Coleman, K.G., 2001. Android arete: Toward a virtue ethic for computational agents. Ethics
and Information Technology 3, 247–265.
Conitzer, V., Sandholm, T., 2008. New complexity results about nash equilibria. Games and
Economic Behavior 63, 621–641.
Conway, P., Gawronski, B., 2013. Deontological and utilitarian inclinations in moral decision
making: a process dissociation approach. Journal of personality and social psychology 104,
216.
Cook, S.A., 1971. The complexity of theorem-proving procedures, in: Proceedings of the
third annual ACM symposium on Theory of computing, pp. 151–158.
Cooper, G.F., 1990. The computational complexity of probabilistic inference using bayesian
belief networks. Artiﬁcial intelligence 42, 393–405.
Courville, A.C., Daw, N.D., Touretzky, D.S., 2006. Bayesian theories of conditioning in a
changing world. Trends in cognitive sciences 10, 294–300.
Crawford, V.P., Sobel, J., 1982. Strategic information transmission. Econometrica: Journal
of the Econometric Society , 1431–1451.
Crisp, R., Slote, M.A., 1997. Virtue ethics. Oxford University Press Oxford.
Cummings, R., Ligett, K., Radhakrishnan, J., Roth, A., Wu, Z.S., 2016. Coordination
complexity: Small information coordinating large populations, in: Proceedings of the 2016
ACM Conference on Innovations in Theoretical Computer Science, pp. 281–290.
85

--- Page 86 ---

Dagum, P., Luby, M., 1993. Approximating probabilistic inference in bayesian belief networks
is np-hard. Artiﬁcial intelligence 60, 141–153.
Dagum, P., Luby, M., 1997. An optimal approximation algorithm for bayesian inference.
Artiﬁcial Intelligence 93, 1–27.
Dahl, N., 2022. A ﬁxed-point problem for theories of meaning. Synthese 200, 1–15.
Daniely, A., Linial, N., Shalev-Shwartz, S., 2014. From average case complexity to improper
learning complexity, in: Proceedings of the forty-sixth annual ACM symposium on Theory
of computing, pp. 441–448.
Daskalakis, C., Mehta, A., Papadimitriou, C., 2006. A note on approximate nash equilibria,
in: International Workshop on Internet and Network Economics, Springer. pp. 297–306.
De Giacomo, G., Massacci, F., 2000. Combining deduction and model checking into tableaux
and algorithms for converse-pdl. Information and Computation 162, 117–137.
Degrave, J., Felici, F., Buchli, J., Neunert, M., Tracey, B., Carpanese, F., Ewalds, T., Hafner,
R., Abdolmaleki, A., de Las Casas, D., et al., 2022. Magnetic control of tokamak plasmas
through deep reinforcement learning. Nature 602, 414–419.
Dehghani, M., Tomai, E., Forbus, K.D., Klenk, M., 2008a. An integrated reasoning approach
to moral decision-making, in: AAAI, pp. 1280–1286.
Dehghani, M., Tomai, E., Klenk, M., 2008b. An integrated reasoning approach to moral
decision-making, in: Proceedings of the Twenty-Third AAAI Conference on Artiﬁcial
Intelligence, AAAI Press, Chicago, Illinois. pp. 1280–1286.
Doshi, P., Gmytrasiewicz, P.J., 2009. Monte carlo sampling methods for approximating
interactive pomdps. Journal of Artiﬁcial Intelligence Research 34, 297–337.
Downey, R.G., Fellows, M.R., 2012. Parameterized complexity. Springer Science & Business
Media.
Ehrenfeucht, A., Haussler, D., Kearns, M., Valiant, L., 1989. A general lower bound on the
number of examples needed for learning. Information and Computation 82, 247–261.
Fagin, R., 1974.
Generalized ﬁrst-order spectra and polynomial-time recognizable sets.
Complexity of computation 7, 43–73.
Fehr, E., Fischbacher, U., 2004. Social norms and human cooperation. Trends in Cognitive
Sciences 8, 185–190.
URL: https://www.sciencedirect.com/science/article/pii/
S1364661304000506, doi:https://doi.org/10.1016/j.tics.2004.02.007.
Fehr, E., G¨achter, S., 2000. Cooperation and punishment in public goods experiments.
American Economic Review 90, 980–994.
86

--- Page 87 ---

Feigenbaum, J., Shenker, S., 2004. Distributed algorithmic mechanism design: Recent results
and future directions, in: Current Trends in Theoretical Computer Science: The Challenge
of the New Century Vol 1: Algorithms and Complexity Vol 2: Formal Models and Semantics.
World Scientiﬁc, pp. 403–434.
Feldman, V., Guruswami, V., Raghavendra, P., Wu, Y., 2012. Agnostic learning of monomials
by halfspaces is hard. SIAM Journal on Computing 41, 1558–1590.
FeldmanHall, O., Mobbs, D., 2015. A neural network for moral decision making. FeldmanHall,
O., & Mobbs, D.(2015) A Neural Network for Moral Decision-Making. In AW Toga, & MD
Lieberman (eds.) Brain Mapping: An Encyclopedic Reference. Elsevier: Oxford .
Fellows, M.R., 2002. Parameterized complexity: the main ideas and connections to practical
computing, in: Experimental Algorithmics. Springer, pp. 51–77.
Fischer, M.J., Ladner, R.E., 1979. Propositional dynamic logic of regular programs. Journal
of computer and system sciences 18, 194–211.
Floridi, L., Sanders, J.W., 2004. On the morality of artiﬁcial agents. Minds and machines 14,
349–379.
Foot, P., 1967. The problem of abortion and the doctrine of the double eﬀect. Oxford review
5.
Foster, D.P., Young, H.P., 2001. On the impossibility of predicting the behavior of rational
agents. Proceedings of the National Academy of Sciences 98, 12848–12853.
Friston, K., 2010.
The free-energy principle: a uniﬁed brain theory?
Nature reviews
neuroscience 11, 127–138.
Frixione, M., 2001. Tractable competence. Minds and Machines 11, 379–397.
Furbach, U., Schon, C., Stolzenburg, F., 2014. Automated reasoning in deontic logic, in:
International Workshop on Multi-disciplinary Trends in Artiﬁcial Intelligence, Springer. pp.
57–68.
Gabbay, D., Horty, J., Parent, X., van der Meyden, R., van der Torre, L., 2013. Handbook of
deontic logic and normative systems .
Gabriel, I., 2020. Artiﬁcial intelligence, values, and alignment. Minds and machines 30,
411–437.
Garcıa, J., Fern´andez, F., 2015. A comprehensive survey on safe reinforcement learning.
Journal of Machine Learning Research 16, 1437–1480.
Garey, M.R., Johnson, D.S., 1979. Computers and intractability. volume 174. freeman San
Francisco.
Gauthier, D., 1987. Morals by agreement. clarendon Press.
87

--- Page 88 ---

Geertz, C., et al., 1973. The interpretation of cultures. volume 5019. Basic books.
Gelman, A., Carlin, J.B., Stern, H.S., Dunson, D.B., Vehtari, A., Rubin, D.B., 2013. Bayesian
data analysis .
Gilboa, I., Zemel, E., 1989. Nash and correlated equilibria: Some complexity considerations.
Games and Economic Behavior 1, 80–93.
Gill, J., 1977. Computational complexity of probabilistic turing machines. SIAM Journal on
Computing 6, 675–695.
Giraud-Carrier, C., Provost, F., 2005. Toward a justiﬁcation of meta-learning: Is the no
free lunch theorem a show-stopper, in: Proceedings of the ICML-2005 Workshop on
Meta-learning, pp. 12–19.
Giubilini, A., Savulescu, J., 2018. The artiﬁcial moral advisor. the “ideal observer” meets
artiﬁcial intelligence. Philosophy & technology 31, 169–188.
Gmytrasiewicz, P.J., Doshi, P., 2005. A framework for sequential planning in multi-agent
settings. Journal of Artiﬁcial Intelligence Research 24, 49–79.
G¨odel, K., 1930. Uber die vollst¨andigkeit des logikkalk¨uls. Ph.D. thesis. Ph. D. dissertation,
University of Vienna.
G¨odel, K., 1931. ¨Uber formal unentscheidbare s¨atze der principia mathematica und verwandter
systeme i. Monatshefte f¨ur mathematik und physik 38, 173–198.
Goodie, A.S., Doshi, P., Young, D.L., 2012. Levels of theory-of-mind reasoning in competitive
games. Journal of Behavioral Decision Making 25, 95–108.
Governatori, G., Olivieri, F., Rotolo, A., Scannapieco, S., 2013. Computing strong and weak
permissions in defeasible logic. Journal of Philosophical Logic 42, 799–829.
Govindarajulu, N.S., Bringsjord, S., 2017. On automating the doctrine of double eﬀect,
in: Proceedings of the 26th International Joint Conference on Artiﬁcial Intelligence, pp.
4722–4730.
Govindarajulu, N.S., Bringsjord, S., Ghosh, R., Sarathy, V., 2019. Toward the engineering of
virtuous machines, in: Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and
Society, pp. 29–35.
Greene, J.D., 2007. Why are vmpfc patients more utilitarian? a dual-process theory of moral
judgment explains. Trends in cognitive sciences 11, 322–323.
Greene, J.D., 2014. Beyond point-and-shoot morality: Why cognitive (neuro) science matters
for ethics. Ethics 124, 695–726.
Greene, J.D., Morelli, S.A., Lowenberg, K., Nystrom, L.E., Cohen, J.D., 2008. Cognitive load
selectively interferes with utilitarian moral judgment. Cognition 107, 1144–1154.
88

--- Page 89 ---

Grice, H.P., 1975. Logic and conversation, in: Speech acts. Brill, pp. 41–58.
Griﬃths, T.L., Tenenbaum, J.B., 2005. Structure and strength in causal induction. Cognitive
psychology 51, 334–384.
Guha, S., Munagala, K., Shi, P., 2010. Approximation algorithms for restless bandit problems.
Journal of the ACM (JACM) 58, 1–50.
Gunning, D., Steﬁk, M., Choi, J., Miller, T., Stumpf, S., Yang, G.Z., 2019. Xai—explainable
artiﬁcial intelligence. Science Robotics 4, eaay7120.
Hagendorﬀ, T., Danks, D., 2022. Ethical and methodological challenges in building morally
informed ai systems. AI and Ethics , 1–14.
Haigh, T., Priestley, M., Rope, C., 2014. Los alamos bets on eniac: Nuclear monte carlo
simulations, 1947-1948. IEEE Annals of the History of Computing 36, 42–63.
Hajek, B., 2015. Random processes for engineers. Cambridge university press.
Halpern, J.Y., Moses, Y., 1992. A guide to completeness and complexity for modal logics of
knowledge and belief. Artiﬁcial intelligence 54, 319–379.
Hanneke, S., 2016. The optimal sample complexity of pac learning. The Journal of Machine
Learning Research 17, 1319–1333.
Hansen, J., 2008. Prioritized conditional imperatives: problems and a new proposal. Au-
tonomous Agents and Multi-Agent Systems 17, 11–35.
Hare, R.M., 1952. The language of morals .
Hare, R.M., 1981. Moral thinking: Its levels, method, and point. Oxford: Clarendon Press;
New York: Oxford University Press.
Harnad, S., 1990. The symbol grounding problem. Physica D: Nonlinear Phenomena 42,
335–346.
Harsanyi, J.C., 1967. Games with incomplete information played by “bayesian” players, i–iii
part i. the basic model. Management science 14, 159–182.
Hart, S., Mas-Colell, A., 2000. A simple adaptive procedure leading to correlated equilibrium.
Econometrica 68, 1127–1150.
Hart, S., Schmeidler, D., 1989. Existence of correlated equilibria. Mathematics of Operations
Research 14, 18–25.
H˚astad, J., 2001. Some optimal inapproximability results. Journal of the ACM (JACM) 48,
798–859.
Hazan, E., Krauthgamer, R., 2011. How hard is it to approximate the best nash equilibrium?
SIAM Journal on Computing 40, 79–91.
89

--- Page 90 ---

Hedden, T., Zhang, J., 2002. What do you think i think you think?: Strategic reasoning in
matrix games. Cognition 85, 1–36.
Hellstr¨om, T., 2013. On the moral responsibility of military robots. Ethics and information
technology 15, 99–107.
Herken, R., 1995. The Universal Turing Machine A Half-Century Survey. Springer-Verlag.
Herzig, A., Schwarzentruber, F., 2008. Properties of logics of individual and group agency.
Advances in modal logic 7, 133–149.
Hester, T., Vecerik, M., Pietquin, O., Lanctot, M., Schaul, T., Piot, B., Horgan, D., Quan,
J., Sendonaris, A., Osband, I., et al., 2018. Deep q-learning from demonstrations, in:
Proceedings of the AAAI Conference on Artiﬁcial Intelligence.
Heuer, L., Orland, A., 2019.
Cooperation in the prisoner’s dilemma: an experimental
comparison between pure and mixed strategies. Royal Society open science 6, 182142.
Hew, P.C., 2014. Artiﬁcial moral agents are infeasible with foreseeable technologies. Ethics
and information technology 16, 197–206.
Himma, K.E., 2009. Artiﬁcial agency, consciousness, and the criteria for moral agency: What
properties must an artiﬁcial agent have to be a moral agent?
Ethics and Information
Technology 11, 19–29.
Hobbes, T., 1651. Leviathan.
Hofstadter, D., 2002. Staring emmy straight in the eye—and doing. Creativity, cognition,
and knowledge: an interaction , 67.
Hohwy, J., 2013. The predictive mind. OUP Oxford.
Holt, C.A., Roth, A.E., 2004. The nash equilibrium: A perspective. Proceedings of the
National Academy of Sciences 101, 3999–4002.
Hooker, B., 2016. Rule Consequentialism, in: Zalta, E.N. (Ed.), The Stanford Encyclopedia
of Philosophy. Winter 2016 ed.. Metaphysics Research Lab, Stanford University.
Hopkins, M., Kane, D.M., Lovett, S., Mahajan, G., 2022. Realizable learning is all you need,
in: Conference on Learning Theory, PMLR. pp. 3015–3069.
Horty, J.F., 2001. Agency and deontic logic. Oxford University Press.
Horty, J.F., 2012. Reasons as defaults. OUP USA.
Howard, D., Muntean, I., 2017. Artiﬁcial moral cognition: moral functionalism and au-
tonomous moral agency. Springer. pp. 121–159.
Hume, D., 1739. A treatise of human nature. Courier Corporation, 2003.
90

--- Page 91 ---

Hummert, S., Bohl, K., Basanta, D., Deutsch, A., Werner, S., Theißen, G., Schroeter, A.,
Schuster, S., 2014. Evolutionary game theory: cells as players. Molecular BioSystems 10,
3044–3065.
Hursthouse, R., 1999. On virtue ethics. OUP Oxford.
Hurwicz, L., Reiter, S., 2006. Designing economic mechanisms. Cambridge University Press.
Huttegger, S.M., 2007. Evolution and the explanation of meaning. Philosophy of science 74,
1–27.
Immerman, N., 1982. Relational queries computable in polynomial time, in: Proceedings of
the fourteenth annual ACM symposium on Theory of computing, pp. 147–152.
Immerman, N., 1989. Descriptive and computational complexity, in: Computational Com-
plexity Theory, ed. J. Hartmanis, Proc. Symp. in Applied Math, pp. 75–91.
Immerman, N., 1998. Descriptive complexity. Springer Science & Business Media.
Johnson, V.R., 1990. The declaration of the rights of man and of citizens of 1789, the reign
of terror, and the revolutionary tribunal of paris. BC Int’l & Comp. L. Rev. 13, 1.
Jørgensen, J., 1937. Imperatives and logic. Erkenntnis 7, 288–296.
Kahneman, D., 2011. Thinking, fast and slow. Macmillan.
Kakade, S.M., 2003. On the sample complexity of reinforcement learning. University of
London, University College London (United Kingdom).
Kant, I., 1785. Groundwork of the Metaphysics of Morals. Routledge (2013).
Karp, R.M., 1972. Reducibility among combinatorial problems, in: Complexity of computer
computations. Springer, pp. 85–103.
Kawaguchi, K., Kaelbling, L.P., Bengio, Y., 2017. Generalization in deep learning. arXiv
preprint arXiv:1710.05468 .
Kaye, P., Laﬂamme, R., Mosca, M., 2006. An introduction to quantum computing. OUP
Oxford.
Kearns, M., Valiant, L., 1994. Cryptographic limitations on learning boolean formulae and
ﬁnite automata. Journal of the ACM (JACM) 41, 67–95.
Kearns, M.J., Schapire, R.E., Sellie, L.M., 1992. Toward eﬃcient agnostic learning, in:
Proceedings of the ﬁfth annual workshop on Computational learning theory, pp. 341–352.
Keller, G.B., Mrsic-Flogel, T.D., 2018. Predictive processing: a canonical cortical computation.
Neuron 100, 424–435.
Kemp, C., Tenenbaum, J.B., 2008. The discovery of structural form. Proceedings of the
National Academy of Sciences 105, 10687–10692.
91

--- Page 92 ---

Khachiyan, L.G., 1979. A polynomial algorithm in linear programming, in: Doklady Akademii
Nauk, Russian Academy of Sciences. pp. 1093–1096.
Kifer, D., Machanavajjhala, A., 2011. No free lunch in data privacy, in: Proceedings of the
2011 ACM SIGMOD International Conference on Management of data, pp. 193–204.
Koenig, S., Simmons, R.G., 1993. Complexity analysis of real-time reinforcement learning, in:
AAAI, pp. 99–107.
Kohlberg, L., Hersh, R.H., 1977. Moral development: A review of the theory. Theory into
practice 16, 53–59.
K¨ording, K.P., Wolpert, D.M., 2006. Bayesian decision theory in sensorimotor control. Trends
in cognitive sciences 10, 319–326.
Koutsoupias, E., Papadimitriou, C., 2009. Worst-case equilibria. Computer science review 3,
65–69.
Kreps, D.M., Milgrom, P., Roberts, J., Wilson, R., 1982. Rational cooperation in the ﬁnitely
repeated prisoners’ dilemma. Journal of Economic theory 27, 245–252.
Kripke, S., 1976. Outline of a theory of truth. The journal of philosophy 72, 690–716.
Kripke, S.A., 1963. Semantical analysis of modal logic i normal modal propositional calculi.
Mathematical Logic Quarterly 9, 67–96.
Kwisthout, J., 2011. Most probable explanations in bayesian networks: Complexity and
tractability. International Journal of Approximate Reasoning 52, 1452–1469.
Kwisthout, J., Wareham, T., Van Rooij, I., 2011. Bayesian intractability is not an ailment
that approximation can cure. Cogn. Sci. 35, 779–784.
L Griﬃths, T., Kemp, C., B Tenenbaum, J., 2008. Bayesian models of cognition .
Ladner, R.E., 1977.
The computational complexity of provability in systems of modal
propositional logic. SIAM journal on computing 6, 467–480.
Langford, J., Zhang, T., 2007. The epoch-greedy algorithm for contextual multi-armed bandits.
Advances in neural information processing systems 20, 96–1.
Lattimore, T., Hutter, M., 2013. No free lunch versus occam’s razor in supervised learning,
in: Algorithmic Probability and Friends. Bayesian Prediction and Artiﬁcial Intelligence.
Springer, pp. 223–235.
Lau, H.C., 2007. A higher order bayesian decision theory of consciousness. Progress in brain
research 168, 35–48.
Leben, D., 2018. Ethics for robots: How to design a moral algorithm. Routledge.
Lee, J., Bahri, Y., Novak, R., Schoenholz, S.S., Pennington, J., Sohl-Dickstein, J., 2017. Deep
neural networks as gaussian processes. arXiv preprint arXiv:1711.00165 .
92

--- Page 93 ---

Lenman, J., 2000. Consequentialism and cluelessness. Philosophy & Public Aﬀairs 29, 342–370.
URL: http://www.jstor.org/stable/2672830.
Levesque, H.J., 1989. Logic and the complexity of reasoning, in: Philosophical logic and
artiﬁcial intelligence. Springer, pp. 73–107.
Lewis, D., 1969. Convention. Cambridge: Harvard University Press.
Lewis, D., 1975. Languages and language .
Lewis, D., 1979. Scorekeeping in a language game, in: Semantics from diﬀerent points of view.
Springer, pp. 172–187.
Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M., Zhang, Y.,
Narayanan, D., Wu, Y., Kumar, A., et al., 2022. Holistic evaluation of language models.
arXiv preprint arXiv:2211.09110 .
Lieder, F., Griﬃths, T.L., 2020. Resource-rational analysis: Understanding human cognition
as the optimal use of limited computational resources. Behavioral and brain sciences 43.
Lindner, F., Mattm¨uller, R., Nebel, B., 2020. Evaluation of the moral permissibility of
action plans. Artiﬁcial Intelligence 287, 103350. URL: https://www.sciencedirect.com/
science/article/pii/S0004370219301043,
doi:https://doi.org/10.1016/j.artint.
2020.103350.
Lipton, R.J., Markakis, E., Mehta, A., 2003. Playing large games using simple strategies, in:
Proceedings of the 4th ACM Conference on Electronic Commerce, pp. 36–41.
Littman, M.L., 1996. Algorithms for sequential decision-making. Brown University.
Littman, M.L., Goldsmith, J., Mundhenk, M., 1998. The computational complexity of
probabilistic planning. Journal of Artiﬁcial Intelligence Research 9, 1–36.
Locatelli, A., Gutzeit, M., Carpentier, A., 2016. An optimal algorithm for the thresholding
bandit problem, in: International Conference on Machine Learning, PMLR. pp. 1690–1698.
Lorenz, E.N., 1963. Deterministic nonperiodic ﬂow. Journal of atmospheric sciences 20,
130–141.
Lucas, P.J., de Bruijn, N.C., Schurink, K., Hoepelman, A., 2000. A probabilistic and decision-
theoretic approach to the management of infectious disease at the icu. Artiﬁcial Intelligence
in medicine 19, 251–279.
Luce, R.D., Raiﬀa, H., 1989. Games and decisions: Introduction and critical survey. Courier
Corporation.
Mabaso, B.A., 2021. Computationally rational agents can be moral agents. Ethics and
Information Technology 23, 137–145.
93

--- Page 94 ---

Madani, O., Hanks, S., Condon, A., 2003. On the undecidability of probabilistic planning
and related stochastic optimization problems. Artiﬁcial Intelligence 147, 5–34.
Makinson, D., Van Der Torre, L., 2000. Input/output logics. Journal of philosophical logic
29, 383–408.
Malle, B., Scheutz, M., Austerweil, J., 2017a. Networks of social and moral norms in human
and robot agents, in: A World with Robots. Intelligent Systems, Control and Automation:
Science and Engineering. Springer, Cham. volume 84, pp. 3–17.
Malle, B.F., Scheutz, M., Austerweil, J.L., 2017b. Networks of social and moral norms in
human and robot agents, in: A world with robots. Springer, pp. 3–17.
Marr, D., 1977. Artiﬁcial intelligence—a personal view. Artiﬁcial Intelligence 9, 37–48.
Marr, D., 1981. Vision: A computational investigation into the human representation and
processing of visual information. San Fransisco, CA: W. H. Freeman.
Mertens, J.F., Zamir, S., 1985. Formulation of bayesian analysis for games with incomplete
information. International journal of game theory 14, 1–29.
Meyer, J.J.C., et al., 1988. A diﬀerent approach to deontic logic: deontic logic viewed as a
variant of dynamic logic. Notre Dame J. Formal Log. 29, 109–136.
Mill, J.S., 1859. On liberty. Oxford University Press, USA (1998).
Mill, J.S., 1861. Utilitarianism. New York: Oxford University Press (1998).
Moka-Mubelo, W., 2017. Law and morality, in: Reconciling Law and Morality in Human
Rights Discourse. Springer, pp. 51–88.
Mundhenk, M., Goldsmith, J., Lusena, C., Allender, E., 2000. Complexity of ﬁnite-horizon
markov decision process problems. Journal of the ACM (JACM) 47, 681–720.
N. J. A. Sloane, R.G.W., 2022. Entry a007526 in the on-line encyclopedia of integer sequences.
URL: https://oeis.org/A007526.
Narveson, J., 2001. The libertarian idea. Broadview Press.
Nash, J., 1951. Non-cooperative games. Annals of mathematics , 286–295.
Nash, J.F., et al., 1950. Equilibrium points in n-person games. Proceedings of the national
academy of sciences 36, 48–49.
v. Neumann, J., 1928. Zur theorie der gesellschaftsspiele. Mathematische annalen 100,
295–320.
Newen, A., De Bruin, L., Gallagher, S., 2018. The Oxford handbook of 4E cognition. Oxford
University Press.
94

--- Page 95 ---

Neyman, A., 1985. Bounded complexity justiﬁes cooperation in the ﬁnitely repeated prisoners’
dilemma. Economics letters 19, 227–229.
Neyshabur, B., Bhojanapalli, S., McAllester, D., Srebro, N., 2017. Exploring generalization
in deep learning. Advances in neural information processing systems 30.
Ng, A.Y., Russell, S.J., 2000. Algorithms for inverse reinforcement learning, in: Icml, p. 2.
Niedermeier, R., 2006. Invitation to ﬁxed-parameter algorithms. volume 31. OUP Oxford.
Nievergelt, J., Gasser, R., M¨aser, F., Wirth, C., 1995.
All the needles in a haystack:
Can exhaustive search overcome combinatorial chaos?. Springer Berlin Heidelberg, Berlin,
Heidelberg. pp. 254–274. URL: https://doi.org/10.1007/BFb0015248, doi:10.1007/
BFb0015248.
Nisan, N., Ronen, A., 1999. Algorithmic mechanism design, in: Proceedings of the thirty-ﬁrst
annual ACM symposium on Theory of computing, pp. 129–140.
Nowak, M.A., 2006. Five rules for the evolution of cooperation. science 314, 1560–1563.
Nussbaum, M.C., 1988. Non-relative virtues: an aristotelian approach. Midwest studies in
philosophy 13, 32–53.
Oaksford, M., Chater, N., 2001. The probabilistic approach to human reasoning. Trends in
cognitive sciences 5, 349–357.
Papadimitriou, C.H., 1994. On the complexity of the parity argument and other ineﬃcient
proofs of existence. Journal of Computer and system Sciences 48, 498–532.
Papadimitriou, C.H., Roughgarden, T., 2008. Computing correlated equilibria in multi-player
games. Journal of the ACM (JACM) 55, 1–29.
Papadimitriou, C.H., Tsitsiklis, J.N., 1987. The complexity of markov decision processes.
Mathematics of operations research 12, 441–450.
Papadimitriou, C.H., Tsitsiklis, J.N., 1994. The complexity of optimal queueing network
control, in: Proceedings of IEEE 9th Annual Conference on Structure in Complexity Theory,
IEEE. pp. 318–322.
Parberry, I., Garey, M.R., Meyer, A., 1994. Circuit complexity and neural networks. MIT
press.
Parﬁt, D., 1984. Reasons and persons. OUP Oxford.
Parﬁt, D., 2011. On what matters. volume 1. Oxford University Press.
Park, J.D., Darwiche, A., 2004. Complexity results and approximation strategies for map
explanations. Journal of Artiﬁcial Intelligence Research 21, 101–133.
95

--- Page 96 ---

Pearl, J., 1985. Bayesian networks: A model of self-activated memory for evidential reasoning,
in: Proceedings of the 7th conference of the Cognitive Science Society, University of
California, Irvine, CA, USA, pp. 15–17.
Pearl, J., 1987. Evidential reasoning using stochastic simulation of causal models. Artiﬁcial
intelligence 32, 245–257.
Pearl, J., 2022. Reverend bayes on inference engines: A distributed hierarchical approach, in:
Probabilistic and Causal Inference: The Works of Judea Pearl, pp. 129–138.
Pereira, L.M., Saptawijaya, A., 2009. Modelling morality with prospective logic. International
Journal of Reasoning-based Intelligent Systems 1, 209–221.
Pitt, L., Valiant, L.G., 1988. Computational limitations on learning from examples. Journal
of the ACM (JACM) 35, 965–984.
Pnueli, A., 1977. The temporal logic of programs, in: 18th Annual Symposium on Foundations
of Computer Science (sfcs 1977), ieee. pp. 46–57.
Pontier, M., Hoorn, J., 2012. Toward machines that behave ethically better than humans do,
in: Proceedings of the annual meeting of the cognitive science society.
Popper, K.R., 1962. Philosophy of Science: Conjectures and Refutations. The growth of
scientiﬁc knowledge.. volume 140. Basic Books, New York, 1962.
Pratt, V.R., 1976. Semantical considerations on ﬂoyd-hoare logic, in: 17th Annual Symposium
on Foundations of Computer Science (sfcs 1976), IEEE. pp. 109–121.
Pratt, V.R., 1980. A near-optimal method for reasoning about action. Journal of Computer
and System Sciences 20, 231–254.
Purves, D., Jenkins, R., Strawser, B.J., 2015. Autonomous machines, moral judgment, and
acting for the right reasons. Ethical Theory and Moral Practice 18, 851–872.
Putnam, H., 2004. The collapse of the fact/value dichotomy and other essays. Harvard
University Press.
Radner, R., 1986. Can bounded rationality resolve the prisoner’s dilemma. Essays in honor
of Gerard Debreu , 387–399.
Rathnasabapathy, B., Doshi, P., Gmytrasiewicz, P., 2006. Exact solutions of interactive
pomdps using behavioral equivalence, in: Proceedings of the ﬁfth international joint
conference on Autonomous agents and multiagent systems, pp. 1025–1032.
Rawls, J., 1980. Kantian constructivism in moral theory. The journal of philosophy 77,
515–572.
Rawls, J.B., 1971. A theory of justice .
96

--- Page 97 ---

Reinikainen, J., 2005. The golden rule and the requirement of universalizability. Journal of
value inquiry 39, 155.
Rest, J.R., Narvaez, D., Thoma, S.J., Bebeau, M.J., 1999. Dit2: Devising and testing a
revised instrument of moral judgment. Journal of educational psychology 91, 644.
Reynolds, C., 2005. On the computational complexity of action evaluations, in: 6th Inter-
national Conference of Computer Ethics: Philosophical Enquiry (University of Twente,
Enschede, The Netherlands, 2005), Citeseer.
Rosser, B., 1936. Extensions of some theorems of g¨odel and church. The journal of symbolic
logic 1, 87–91.
Roth, D., 1996. On the hardness of approximate reasoning. Artiﬁcial Intelligence 82, 273–302.
Roughgarden, T., 2005. Selﬁsh routing and the price of anarchy. MIT press.
Roughgarden, T., Tardos, ´E., 2002. How bad is selﬁsh routing? Journal of the ACM (JACM)
49, 236–259.
Rubinstein, A., 1998. Modeling bounded rationality. MIT press.
Russell, S.J., Subramanian, D., 1994. Provably bounded-optimal agents. Journal of Artiﬁcial
Intelligence Research 2, 575–609.
Scanlon, T.M., 2000. What we owe to each other. Harvard University Press.
Scarselli, F., Tsoi, A.C., 1998. Universal approximation using feedforward neural networks: A
survey of some existing methods, and some new results. Neural networks 11, 15–37.
Schaﬀer, C., 1994. A conservation law for generalization performance, in: Machine Learning
Proceedings 1994. Elsevier, pp. 259–265.
Schelling, T.C., 1960. The Strategy of Conﬂict: with a new Preface by the Author. Harvard
university press.
Schiﬀer, S.R., 1972. Meaning .
Schnoebelen, P., 2002. The complexity of temporal logic model checking. Advances in modal
logic 4, 35.
Schroeder, M., 2010. Being for: Evaluating the semantic program of expressivism. OUP
Oxford.
Schurz, G., 2017. No free lunch theorem, inductive skepticism, and the optimality of meta-
induction. Philosophy of Science 84, 825–839.
Schwarzentruber, F., Semmling, C., 2014. Stit is dangerously undecidable, in: ECAI.
Searle, J.R., 1980. Minds, brains, and programs. Behavioral and brain sciences 3, 417–424.
97

--- Page 98 ---

Searle, J.R., 1992. The rediscovery of the mind. MIT press.
Sen, A., 1979. Utilitarianism and welfarism. The journal of Philosophy 76, 463–489.
Serfozo, R.F., 1979. An equivalence between continuous and discrete time markov decision
processes. Operations Research 27, 616–620.
Sergot, M., 1998. Normative positions. Norms, logics and information systems 49, 289–308.
Shim, J., Arkin, R., Pettinatti, M., 2017.
An intervening ethical governor for a robot
mediator in patient-caregiver relationship: Implementation and evaluation, in: 2017 IEEE
International Conference on Robotics and Automation (ICRA), IEEE, New York, USA. pp.
2936–2942.
Shimony, S.E., 1994. Finding maps for belief networks is np-hard. Artiﬁcial intelligence 68,
399–410.
Sidgwick, H., 1907. The Methods of Ethics. Good Press (2019).
Silver, D., Hubert, T., Schrittwieser, J., Antonoglou, I., Lai, M., Guez, A., Lanctot, M., Sifre,
L., Kumaran, D., Graepel, T., et al., 2018. A general reinforcement learning algorithm that
masters chess, shogi, and go through self-play. Science 362, 1140–1144.
Silver, D., Singh, S., Precup, D., Sutton, R.S., 2021. Reward is enough. Artiﬁcial Intelligence
299, 103535.
Simon, H.A., 1955. A behavioral model of rational choice. The quarterly journal of economics
69, 99–118.
Simon, H.A., 1990. Bounded rationality, in: Utility and probability. Springer, pp. 15–18.
Singer, M.G., 2002. The ideal of a rational morality: Philosophical compositions. Oxford
University Press.
Singer, P., 2011. Practical Ethics. Cambridge University Press.
Sinnott-Armstrong, W., 2021. Consequentialism, in: Zalta, E.N. (Ed.), The Stanford Ency-
clopedia of Philosophy. Fall 2021 ed.. Metaphysics Research Lab, Stanford University.
Sistla, A.P., Clarke, E.M., 1985. The complexity of propositional linear temporal logics.
Journal of the ACM (JACM) 32, 733–749.
Skyrms, B., 2004. The stag hunt and the evolution of social structure. Cambridge University
Press.
Skyrms, B., 2010. Signals: Evolution, learning, and information. OUP Oxford.
Slivkins, A., 2019. Introduction to multi-armed bandits. arXiv preprint arXiv:1904.07272 .
Smart, J.J.C., 1956. Extreme and restricted utilitarianism. The Philosophical Quarterly
(1950-) 6, 344–354.
98

--- Page 99 ---

Smith, J.M., Price, G.R., 1973. The logic of animal conﬂict. Nature 246, 15–18. doi:10.1038/
246015a0.
Sobel, D.M., Kirkham, N.Z., 2006. Blickets and babies: the development of causal reasoning
in toddlers and infants. Developmental psychology 42, 1103.
Spaan, E., 1993. The complexity of propositional tense logics, in: Diamonds and defaults.
Springer, pp. 287–307.
Spaan, E., 2016. Complexity of modal logics. Ph.D. thesis. University of Amsterdam.
Stace, W.T., 1937. The concept of morals .
Stenseke, J., 2021. Artiﬁcial virtuous agents: from theory to machine implementation. AI &
SOCIETY doi:10.1007/s00146-021-01325-7.
Stenseke, J., 2022a. Artiﬁcial virtuous agents in a multi-agent tragedy of the commons. AI &
SOCIETY , 1–18.
Stenseke, J., 2022b. Interdisciplinary confusion and resolution in the context of moral machines.
Science and Engineering Ethics 28, 1–17.
Stenseke, J., 2023. The use and abuse of normative ethics for moral machines, in: Social
Robots in Social Institutions. IOS Press, pp. 155–164.
Stenseke, J., Balkenius, C., 2022. Assessing the time eﬃciency of ethical algorithms, in:
CEUR Workshop Proceedings, CEUR-WS.
Sterkenburg, T.F., Gr¨unwald, P.D., 2021. The no-free-lunch theorems of supervised learning.
Synthese 199, 9979–10015.
Stevenson, C.L., 1937. The emotive meaning of ethical terms. Mind 46, 14–31.
Steyvers, M., Tenenbaum, J.B., Wagenmakers, E.J., Blum, B., 2003. Inferring causal networks
from observations and interventions. Cognitive science 27, 453–489.
Stocker, M., 1977. The schizophrenia of modern ethical theories. The Journal of philosophy
73, 453–466.
Sun, X., Robaldo, L., 2017. On the complexity of input/output logic. Journal of Applied
Logic 25, 69–88.
Taddeo, M., Floridi, L., 2005. Solving the symbol grounding problem: a critical review of
ﬁfteen years of research. Journal of Experimental & Theoretical Artiﬁcial Intelligence 17,
419–445.
Tarski, A., 1944. The semantic conception of truth: and the foundations of semantics.
Philosophy and phenomenological research 4, 341–376.
Tenbrunsel, A.E., Messick, D.M., 2004. Ethical fading: The role of self-deception in unethical
behavior. Social justice research 17, 223–236.
99

--- Page 100 ---

Tenenbaum, J.B., Griﬃths, T.L., Kemp, C., 2006. Theory-based bayesian models of inductive
learning and reasoning. Trends in cognitive sciences 10, 309–318.
Thornton, S.M., Pan, S., Erlien, S.M., Gerdes, J.C., 2016. Incorporating ethical considerations
into automated vehicle control. IEEE Transactions on Intelligent Transportation Systems
18, 1429–1439.
Tolmeijer, S., Kneer, M., Sarasua, C., Christen, M., Bernstein, A., 2020. Implementations in
machine ethics: A survey. ACM Computing Surveys (CSUR) 53, 1–38.
Tr´emoli`ere, B., Neys, W.D., Bonnefon, J.F., 2012. Mortality salience and morality: Thinking
about death makes people less utilitarian.
Cognition 124, 379–384.
URL: https://
www.sciencedirect.com/science/article/pii/S0010027712001035, doi:https://doi.
org/10.1016/j.cognition.2012.05.011.
Tsotsos, J.K., 1990. Analyzing vision at the complexity level. Behavioral and brain sciences
13, 423–445.
Tuﬁ¸s, M., Ganascia, J.G., 2015. Grafting norms onto the bdi agent model, in: A Construction
Manual for Robots’ Ethical Systems. Springer, pp. 119–133.
Turing, A.M., 1936. On computable numbers, with an application to the entscheidungsproblem.
J. of Math 58, 5.
Ullmann-Margalit, E., 2015. The emergence of norms. OUP Oxford.
Urbano, A., Vila, J.E., 2002. Computational complexity and communication: Coordination
in two–player games. Econometrica 70, 1893–1927.
Valiant, L.G., 1984. A theory of the learnable. Communications of the ACM 27, 1134–1142.
Vallor, S., 2015. Moral deskilling and upskilling in a new machine age: Reﬂections on the
ambiguous future of character. Philosophy & Technology 28, 107–124.
Vallor, S., 2016. Technology and the virtues: A philosophical guide to a future worth wanting.
Oxford University Press.
Van Der Meyden, R., 1996. The dynamic logic of permission. Journal of Logic and Computation
6, 465–479.
Van Rooij, I., 2008. The tractable cognition thesis. Cognitive science 32, 939–984.
Van Rooij, I., Blokpoel, M., Kwisthout, J., Wareham, T., 2019. Cognition and intractability:
A guide to classical and parameterized complexity analysis. Cambridge University Press.
Vanmarcke, E., 2010. Random ﬁelds: analysis and synthesis. World scientiﬁc.
Vapnik, V., 1999. The nature of statistical learning theory. Springer science & business media.
Vapnik, V., Chervonenkis, A., 1974. Theory of pattern recognition.
100

--- Page 101 ---

Vapnik, V.N., Chervonenkis, A.Y., 2015. On the uniform convergence of relative frequencies
of events to their probabilities, in: Measures of complexity. Springer, pp. 11–30.
Vardi, M.Y., 1982. The complexity of relational query languages, in: Proceedings of the
fourteenth annual ACM symposium on Theory of computing, pp. 137–146.
Vardi, M.Y., 1997. Why is modal logic so robustly decidable? Technical Report.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser,  L.,
Polosukhin, I., 2017. Attention is all you need. Advances in neural information processing
systems 30.
Vollmer, H., Schnoor, I., Schnoor, H., Schneider, T., Bauland, M., 2009. The complexity of
generalized satisﬁability for linear temporal logic. Logical Methods in Computer Science 5.
Von Luxburg, U., Sch¨olkopf, B., 2011. Statistical learning theory: Models, concepts, and
results, in: Handbook of the History of Logic. Elsevier. volume 10, pp. 651–706.
Von Neumann, J., Morgenstern, O., 1947. Theory of games and economic behavior, 2nd rev .
Von Wright, G.H., 1951. Deontic logic. Mind 60, 1–15.
Vul, E., Goodman, N., Griﬃths, T.L., Tenenbaum, J.B., 2014. One and done? optimal
decisions from very few samples. Cognitive science 38, 599–637.
Wallach, W., Allen, C., 2008. Moral machines: Teaching robots right from wrong. Oxford
University Press.
Wattles, J., 1996. The golden rule. Oxford University Press.
de Weerd, H., Verbrugge, R., Verheij, B., 2013. How much does it help to know what she
knows you know? an agent-based simulation study. Artiﬁcial Intelligence 199, 67–92.
de Weerd, H., Verbrugge, R., Verheij, B., 2017. Negotiating with other minds: the role of
recursive theory of mind in negotiation with incomplete information. Autonomous Agents
and Multi-Agent Systems 31, 250–287.
Whitehead, S.D., 1991. A complexity analysis of cooperative mechanisms in reinforcement
learning., in: AAAI, pp. 607–613.
Whittle, P., 1988. Restless bandits: Activity allocation in a changing world. Journal of
applied probability 25, 287–298.
Wiegel, V., van den Berg, J., 2009. Combining moral theory, modal logic and mas to create
well-behaving artiﬁcial agents. International Journal of Social Robotics 1, 233–242.
Williams, B., 2006. Ethics and the Limits of Philosophy. Routledge.
Williamson, D.P., Shmoys, D.B., 2011. The design of approximation algorithms. Cambridge
university press.
101

--- Page 102 ---

Wittgenstein, L., 2010. Philosophical investigations. John Wiley & Sons.
Wolpert, D.H., 1992. On the connection between in-sample testing and generalization error.
Complex Systems 6, 47.
Wolpert, D.H., 1996. The lack of a priori distinctions between learning algorithms. Neural
computation 8, 1341–1390.
Wolpert, D.H., 2002. The supervised learning no-free-lunch theorems. Soft computing and
industry , 25–42.
Wolpert, D.H., Macready, W.G., 1997. No free lunch theorems for optimization. IEEE
transactions on evolutionary computation 1, 67–82.
Xu, M., 1998. Axioms for deliberative stit. Journal of Philosophical Logic 27, 505–552.
Yi, S.K.M., Steyvers, M., Lee, M.D., Dry, M.J., 2012. The wisdom of the crowd in combinatorial
problems. Cognitive science 36, 452–470.
Yoshida, W., Dolan, R.J., Friston, K.J., 2008. Game theory of mind. PLoS computational
biology 4, e1000254.
Zhang, C., Bengio, S., Hardt, M., Recht, B., Vinyals, O., 2021. Understanding deep learning
(still) requires rethinking generalization. Communications of the ACM 64, 107–115.
Zhang, N.L., Poole, D., 1996. Exploiting causal independence in bayesian network inference.
Journal of Artiﬁcial Intelligence Research 5, 301–328.
Zinkevich, M., Johanson, M., Bowling, M., Piccione, C., 2007. Regret minimization in games
with incomplete information. Advances in neural information processing systems 20.
102

```
