---
title: "Toward Non-Intuition-Based Machine Ethics - PDF Extract"
source_pdf: "2018-Kim-Toward Non-Intuition-Based Machine Ethics.pdf"
pages: 7
extracted_at: "2026-01-25T05:00:17.636780"
---

# PDF Extract: Toward Non-Intuition-Based Machine Ethics

**Source PDF:** 2018-Kim-Toward Non-Intuition-Based Machine Ethics.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

Toward Non-Intuition-Based Machine and Artiﬁcial Intelligence Ethics: A
Deontological Approach Based on Modal Logic
J. N. Hooker and Tae Wan Kim
Carnegie Mellon University, Pittsburgh, USA
twkim,jh38@andrew.cmu.edu
Abstract
We propose a deontological approach to machine (or AI)
ethics that avoids some weaknesses of an intuition-based
system, such as that of Anderson and Anderson. In particular,
it has no need to deal with conﬂicting intuitions, and it yields
a more satisfactory account of when autonomy should be
respected. We begin with a “dual standpoint” theory of action
that regards actions as grounded in reasons and therefore
as having a conditional form that is suited to machine in-
structions. We then derive ethical principles based on formal
properties that the reasons must exhibit to be coherent, and
formulate the principles using quantiﬁed modal logic. We
conclude that deontology not only provides a more satisfac-
tory basis for machine ethics but endows the machine with an
ability to explain its actions, thus contributing to transparency
in AI.
Introduction
No one has done more to develop machine/AI ethics than
Anderson and Anderson (2007, 2010, 2011, 2014, 2015a,
2015b; with Armen 2006; with Berenz 2017). Throughout
the debate between case- and principle-based approaches
(Wallach, Allen, and Smit 2008), Anderson and Anderson
(hereafter, A&A) show that it is better for machine ethics
to be principle-based (cf. Guarini 2011). In particular, they
show that any adequate machine ethics should have non-
consequentialist elements to respect the dignity of persons.
We build upon A&A’s work, but critically. They comput-
erize W. D. Ross’s (1930) prima facie duty approach for the
context of health-care scenarios (e.g., GENETH, EthEl). We
argue that their prima facie duty approach is inadequate for
machine ethics for two reasons: (i) it relies on human moral
intuition; (ii) its treatment of autonomy is inadequate.
We propose a non-intuition-based machine ethics that
rests, instead, on deontology. We show that ethical rules for
machines can be derived from ﬁrst principles and stated with
a reasonable degree of rigor. We formulate these rules in
the idiom of quantiﬁed modal logic, which is well suited to
formalize the role of rational belief in deontological ethics.
We show that this approach can avoid some of the pitfalls
of relying on moral intuition and yield a more adequate
analysis of autonomy.
We begin with a critique of A&A’s approach. We then
sketch a “dual standpoint” theory of action that regards
actions as necessarily grounded in reasons and therefore
having a conditional form, which is well suited to formu-
lating rules for machines. We then derive ethical principles
based on formal properties that the reasons for an action
must have in order to be coherent, and formulate the prin-
ciples using quantiﬁed modal logic. At this point we can
show how a healthcare example central to A&A’s discussion
is more adequately treated with deontological ethics. The
paper concludes by pointing out that the same approach
installs an ability for the machine to explain its actions, thus
contributing to transparency in AI.
A&A’s Prima Facie Duties Approach
A&A use inductive logic programming to discover a deci-
sion principle for a speciﬁc domain. To make this concrete,
consider one of A&A’s example scenarios:
A doctor has prescribed a medication that should be
taken at a particular time in order for the patient to
receive a small beneﬁt (i.e., the patient will be more
comfortable); but, when reminded, the patient doesn’t
want to take it at that time.
The normative question is:
Should the system notify the overseer that the patient
won’t take the medication at the prescribed time or not?
The system has two options: Notify and Don’t notify. Re-
lying upon the work of biomedical ethicists Buchanan
and Brock (1990), A&A assume that the correct answer
is Don’t notify. To analyze the rationale, drawing upon
the work of biomedical ethicists Beauchamp and Childress
(1979), A&A assume that three prima facie duties—non-
maleﬁcence, beneﬁcence, and autonomy—are relevant to
the scenario. A&A associate either option (Notify or Don’t
notify) with an ordered triple (v1, v2, v3) that indicates the
degree to which each of the three duties is satisﬁed.
Harm does not result from either option. Notify achieves
beneﬁcence but violates autonomy, while Don’t notify sac-
riﬁces beneﬁcence while respecting autonomy. Suppose we
set the value of beneﬁcence at +1 and its absence at −1, and
we set the value of respecting autonomy at +2 and violating
it at −2. Then the two options are associated with ordered
triples as follows:
Notify:
(0, 1, −2)
Don’t notify:
(0, −1, 2)

--- Page 2 ---

Repeating the process for other variations that cover all
the possible cases, the system inductively seeks an equilib-
rium that coherently covers all the choices that A&A assume
to be as correct, based on Buchanan and Brock (1990). As a
result, the decision principle that A&A’s system discovers in
the above healthcare context is, “A healthcare worker should
challenge a patient’s decision if it isn’t fully autonomous and
there’s either any violation of non-maleﬁcence or a severe
violation of beneﬁcence.”
When a duty of beneﬁcence and a duty of autonomy
conﬂict as in the case above, A&A’s system relies upon the
moral intuition of ethicists, as advocated by the intuitionist
W. D. Ross (1930). Ross argued that ethics consists of vari-
ous duties that sometimes conﬂict with each other, and that
when there is conﬂict, we should rely on the moral intuitions
of “well-educated people.” He writes,
[M]oral convictions of thoughtful and well-educated
people are the data of ethics just as sense-perceptions
are the data of a natural science (1930: 41)
In the same vein, A&A (2011) write,
We used ethicists’ intuitions to tell us the degree
of satisfaction/violation of the assumed duties within
the range stipulated, and which actions would be
preferable, in enough speciﬁc cases from which a
machine-learning procedure arrived at a general prin-
ciple (479). . . We believe that there is an expertise that
comes from thinking long and deeply about ethical
matters. Ordinary human beings are not likely to be
the best judges of how one should behave in ethical
dilemmas (482).
Assuming the correctness of the ethicist’s intuition—that
Don’t notify is the right choice—A&A’s system analyzes
the rationale. That is, the system is trained to discover a
coherent set of principles using the ethicists’ moral intuition
as training data.
Problems of Moral Intuition in Machine Ethics
Relying on moral intuition is often problematic. Intuition
may be an important part of ethical reasoning (see, e.g.,
reﬂective equilibrium in Rawls 1971) but is not itself an ar-
gument (Dennett 2013). Furthermore, experimental philoso-
phers show that moral intuitions are not as consistent as
we think. For example, they are susceptible to morally
irrelevant situational cues (e.g., Alexander 2012, Appiah
2008, Sinnott-Armstrong 2006). A&A might respond that
their system relies on the intuition of a professional ethics
researcher. But evidence shows that professional intuitions
are not signiﬁcantly different from those of ordinary people
(for reviews, see Schwitzgebel and Rust 2016).1
Additionally, a major rationale behind developing ma-
chine ethics is inconsistent with reliance on human intuition.
1The cited paper does not survey works that directly study
the moral intuition of ethicists, but the consistency between their
ethical beliefs and behaviors. If it is plausible to believe that hu-
mans often use intuitions to guide behavior, the research implies
that ethicists’ moral intuitions are not more reliable than those of
ordinary people.
For example, a prime motivation for developing autonomous
vehicles is that human error is a leading cause of accidents,
and autonomous vehicles minimize human involvement.
Thus if human moral intuitions are not reliable, machine
ethics should be developed so as to avoid human moral
intuition.
Finally, A&A’s system is helpless in situations about
which professional ethicists’ intuitions do not have con-
sensus. In response, A&A argue that machines should not
be allowed to make a choice for such cases. But machines
may face scenarios in which they must make choices (not
making a choice is itself a choice). And, as A&A often
emphasize, one contribution of machine ethics should be
to make breakthroughs in dilemmas that human ethicists
cannot resolve. We therefore develop a non-intuition-based
approach.
A&A’s Treatment of Autonomy
In their earlier works (2007, 2006 with Armen), A&A con-
sidered the adequacy of hedonic utilitarianism for machine
ethics because the theory is straightforward to codify. The
machine need only maximize expected net pleasure. But
soon they turned to the prima facie duty approach because of
standard problems in utilitarianism: it demands sacriﬁcing
the good of one for the good of many, which means that
respect for an individual’s autonomy is not guaranteed.
We agree with A&A that machine ethics must possess
deontological elements that protect a person’s dignity. But
we believe that the way A&A computerize autonomy fails
to fulﬁll its expected role. It works in the above scenario
because there is only one patient, and the patient is the only
beneﬁciary. But imagine a case in which violating one per-
son’s autonomy maximizes beneﬁt for ten thousand others.
For example, a company might send a manager unjustly
accused of fraud to prison (by falsely testifying against her)
in order to satisfy the media and boost share prices. To
avoid endorsing this outcome, A&A’s system must say that
the value of autonomy violation in this case (and relevantly
similar cases) is −10,001 to counterbalance a total beneﬁ-
cence score of 10,000. Yet if there is only one stockholder,
the system would presumably set the value of autonomy
violation at −2 because the value of beneﬁcence is only 1.
We do not see why the value of the manager’s autonomy
should differ dramatically, depending upon the number of
parties who stand to beneﬁt. This problem occurs because
there is no adequate notion of autonomy in A&A’s system.
Deontological Ethics for Machines
The vagaries of intuition-based ethics can largely be avoided
by a rigorous development of deontological ethics for ma-
chines. “Deontological” literally means duty-oriented, but it
is normally interpreted as referring to rule-oriented ethics,
which encodes obligation as rules of conduct. While de-
ontology is inseparable from the name of Immanuel Kant,
it need not be bound to Kant’s historical theory. The basic
reasoning process one ﬁnds in Kantian ethics can give rise
to precise rules that are grounded in ﬁrst principles.

--- Page 3 ---

The key is to recognize that actions are necessarily based
on reasons (Anscombe 1957; Davidson 1963). While all
behavior is determined by physical and biological causes,
a “dual standpoint” theory allows one to distinguish action
from mere behavior by virtue of the fact that it has a second
kind of explanation, namely the agent’s reasons for under-
taking the action. Thus an action can be viewed from two
standpoints, namely as a result of physical causes, and as
the conclusion of a reasoning process.2
Because actions are always based on reasons, they have
a conditional form: “If such-and-such reasons apply, then
perform such-and-such an action.” Conditional rules of this
kind are naturally suited to be programmed into a machine.
We can also derive necessary conditions for an ethical rule
by requiring that the reasons satisfy certain formal consis-
tency properties, as is the tradition in deontological ethics.
For present purposes we do not regard machines as agents
that exercise autonomy in the full sense necessary to derive
ethical obligations for the machines themselves. They are
seen as autonomous only in the limited sense that they
operate according to internal rules and are not under constant
human control. Rather, the human programmer is the agent,
and rules encoded into the machine must be rules that the
human can ethically inject into a machine.
Action Plans
Because actions necessarily have conditional form, we will
refer to them as action plans. As an example, suppose I walk
into a department store and see a display of watches. The
watches are in an open case, and as I look around, I see that
there is nothing to prevent me from stealing one (no security
guards, no surveillance cameras, etc.). So I steal a watch.
Let’s suppose my action plan is a conditional statement:3
C1 ∧C2 ⇒A1
where the antecedents C1, C2 and consequent A1 are inter-
preted
C1 = “I would like to have a new watch.”
C2 = “I can get away with stealing one.”
A1 = “I will now steal the watch.”
2The phrase “dual standpoint” derives from Kant’s statement
that “the concept of a world of understanding is therefore only
a standpoint that reason sees itself constrained to take outside of
appearances in order to think of itself as practical” (“Der Begriff
einer Verstandeswelt is also nur ein Standpunkt, den die Vernunft
sich gen¨othigt sieht, außer den Erscheinungen zu nehmen, um
sich selbst als praktisch zu denken”) (Kant 1785, page 458). In
other words, to see oneself as taking action (in Kantian language,
to think of oneself as “practical”), one must interpret oneself as
existing outside the natural realm of cause and effect. Or to use
more modern language, one must be able to give one’s behavior a
second kind of explanation that is based on reasons one adduces
for it, rather than on cause and effect. This idea eventually evolved
into the dual standpoint theories of recent decades (Nagel 1986;
Korsgaard 1996; Bilgrami 1996), which have some parallels to the
theory adopted here.
3Properly speaking, an action plan is expressed or denoted by a
conditional statement, but we will blur the use/mention distinction
to simplify exposition. To avoid excessive parentheses, we will
write (C1 ∧C2) ⇒A1 as C1 ∧C2 ⇒A1.
The symbol ⇒means that I take the conditions C1, C2 to
be sufﬁcient reason to carry out action A1 when they are
satisﬁed. Thus C1, C2 are not psychological causes or moti-
vations for taking action A1, but conditions that I regard as
sufﬁcient reason for taking action A1 as part of my reasoning
process.
I must regard the antecedents of my action plan as jointly
sufﬁcient and individually necessary for the action. Sufﬁ-
ciency means that I have decided to take the action whenever
the reasons apply, since otherwise they are not a complete
list of reasons. Necessity means that I will not necessarily
take the action if any of the conditions are missing. I may,
of course, view additional conditions as necessary to justify
my theft: I believe no one at the shop is likely to be ﬁred as
a result of my theft, I do not expect to feel remorse, etc.
We also require that an action plan be maximal; that is,
as general as possible while remaining a valid description of
the agent’s reasoning. Suppose I am an ambulance driver
and ﬁnd that, due to heavy trafﬁc, I will be late for an
appointment with my boss. I therefore drive my ambulance
to the appointment while using siren and lights, even though
there is no medical emergency. I have what appears to be an
action plan C4 ∧C5 ∧C6 ⇒A2, where
C4 = “I am late for an appointment with my boss.”
C5 = “The trafﬁc is heavy enough to make me late
unless I use the siren and lights.”
C6 = “I can get away with using siren and lights when
there is no medical emergency.”
A2 = “I will use siren and lights.”
However, this is probably not a true account of my reasons.
Suppose that in another scenario, I must pick up my kids
at day care, and I am running late because I had problems
starting the engine. Why wouldn’t I use the siren and lights
in this case? If I have no particular reason for doing so in
one case and not the other, it is evident that my true reasons
are more general:
C′
4 = “It is really important to be on time.”
C′
5 = “I will be late unless I use the sirens and light.”
as well as C6. So my action plan is actually C′
4 ∧C′
5 ∧C6 ⇒
A2. We can express this formally as follows:
If C ⇒A is an action plan, and C′ →C but
C ̸→C′, then C′ ⇒A is not an action plan.
where C and C′ are conjunctions of conditions, and C′ →C
means that C′ implies C.
From Action Theory to Ethics
The next step is to derive necessary conditions for ethical
action plans that are based on the consistency of the ratio-
nales in the plans. This can be accomplished by appealing
to the universality of reason: the validity of one’s reasoning
process should not depend on who one is. If I take certain
reasons to justify my action, rationality requires me to take
them as justifying this action for anyone to whom the rea-
sons apply.
For example, suppose that I lie simply because it is con-
venient to deceive someone. Then when I decide to lie for

--- Page 4 ---

this reason, I decide that everyone should lie whenever de-
ception is convenient. Every choice of action for myself is a
choice for all agent. This leads to the famous generalization
principle, which is perhaps best stated as follows: I must
be rational in believing that the reasons for my action are
consistent with the assumption that everyone with the same
reasons takes the same action. An action plan that satisﬁes
this principle is generalizable. Onora O’Neill (2014) pro-
vides an excellent reconstruction of thought along this line.
Thus if I lie because it is convenient to deceive someone, I
am adopting this as a policy for everyone. Yet I am rationally
constrained to believe that if everyone in fact lied when
deception is convenient, no one would believe the lies, and
no one would be deceived. My reasons for lying would no
longer justify lying. So the reasons behind my decision to lie
are ungeneralizable and therefore self-contradictory.
Formalizing the Generalization Principle
We can formalize the generalization principle to a certain
degree by introducing elements of quantiﬁed modal logic.
First, we regard a condition Ci as a predicate that applies to
an agent. Thus Ci(a) states that agent a satisﬁes condition
Ci. It is also convenient to let C(a) serve as shorthand for the
conjunction V
C∈C C(a). If agent a adopts the action plan
C ⇒A, we write C(a) ⇒A(a).4
Consider again the theft of the watch, which we suppose
is carried out by agent a and represented by the action plan
C1(a) ∧C2(a) ⇒A(a). One of the reasons for the action
is C2(a): agent a can get away with the theft. However,
there are many customers entering the shop who would like
a new watch and could steal one with impunity. Rationality
constrains agent a to believe that if everyone were to adopt
this action plan, reason C2(a) would no longer apply. The
shop would crack down by displaying the watches under
glass, installing security systems, and so forth.
We can write this more formally by borrowing the opera-
tors □and ⋄from modal logic. We deﬁne □S to mean that
the agent is rationally constrained to believe proposition S;
that is, it is irrational for the agent to deny S. We deﬁne ⋄S
to mean ¬□¬S, or it is not irrational for the agent to believe
S. We will frequently express ⋄S by saying simply that the
agent can rationally believe S. Note that these deﬁnitions
differ somewhat from those normally used in epistemic and
doxastic logics.
To formulate generalizability, we adopt the notation P(S)
to mean that it is physically possible for proposition S to be
true. The action plan C1(a) ∧C2(a) ⇒A1(a) is generaliz-
able only if a can rationally believe that it is possible for a
to carry out the theft when everyone adopts this plan:
⋄P

C1(a) ∧C2(a) ∧A1(a)
∧∀x
 C1(x) ∧C2(x) ⇒A1(x)

Since a cannot rationally believe this, the action plan is
unethical. This leads to the rule
4The constant a may be absent from some or all of the condi-
tions, and other constants may appear to represent agents affected
by the action.
Action plan C(a) ⇒A(a) is generalizable only if
⋄P

C(a) ∧A(a) ∧∀x
 C(x) ⇒A(x)

We can now see the importance of requiring action plans
to be maximal. In the case of an ambulance driver a, the
(maximal) action plan {C′
4(a), C′
5(a), C6(a)} ⇒A2(a)
violates the generalization principle because
¬⋄P

C′
4(a) ∧C′
5(a) ∧C6(a) ∧A2(a)
∧∀x
 C′
4(x) ∧C′
5(x) ∧C6(x) ⇒A2(x)

It is not reasonable for a to believe that a can get away
with his mischief if all ambulance drivers used the siren and
lights whenever they are in a hurry to meet an important
engagement. The city would crack down on the practice
and carefully monitor drivers. However, the narrower rule
C3(a) ∧C4(a) ∧C5(a) ⇒A2 is generalizable because
circumstances C3 and C4 rarely occur, and a can rationally
believe that a could get away with it if ambulance drivers
always misbehaved in these circumstances. So if the nar-
rower rule were treated as an action plan, we would have
to conclude that misusing the ambulance is generalizable.
Respecting Autonomy
An agent violates autonomy when one of its action plans
interferes with action plans of one or more other agents.
Generally, this occurs when there is coercion, bodily injury
that impairs another agent, suppression of another’s rational
faculties, or death.
It is no violation of autonomy, however, to interfere with
behavior that has no coherent rationale, because in this case
the behavior is not action. This could occur if the agent
simply has not formulated a clear rationale, or the agent’s
rationale violates one of the conditions for ethical choice.
For example, it is no violation of autonomy for me to prevent
you from stealing a bicycle from a bicycle rack. This type of
coercion may be unethical for other reasons, but it is not a
violation of autonomy.
The conditional form of action plans also helps to dis-
tinguish ethical from unethical interference. Suppose, for
example, that you decide to cross the street to catch a bus
as soon as no cars are coming. You begin to cross, but I
grab you by the arm and pull you off the street. This is
an obvious violation of autonomy, because my action plan
interferes with yours. On the other hand, suppose there is a
car coming, I shout a warning that you cannot hear, and I
then pull you out of the path of the car. I prevent you from
crossing the street, but there is no violation of autonomy,
because my action does not interfere with your action plan.
Finally, the conditional form accommodates the principle
that no violation of autonomy occurs if there is informed
consent to interfere. If b has given informed consent to be
blocked from action A(b) under condition C(b), then any of
b’s rational action plans that result in action A(b) will have
the form ¬C(b) ∧C(b) ⇒A(b). Thus another agent b who
has obtained informed consent will not violate b’s autonomy
by interfering with A(b) under condition C(b). This will be
illustrated in our discussion of the medical example.

--- Page 5 ---

Formally, an action plan C1(a) ⇒A1(a) interferes with
an action plan C2(b) ⇒A2(b) when C1(a) ∧C2(b) is phys-
ically possible and A1(a) interferes with A2(b). We denote
interference with the special notation A1(a) ,→¬A2(b) to
reﬂect the fact that the contrapositive does not hold. Thus we
do not have A2(b) ,→¬A1(a), because we do not wish to
say that my crossing the street interferes with your pulling
me off the street. We do not further analyze the concept
of interference here but assume that it is clear enough for
practical purposes.
In general, we say that C(a) ⇒A(a) interferes with a set
{Ci(ai) ⇒Ai(ai) | i ∈I}
(1)
of action plans when a ̸= ai for all i ∈I and
P

C(a) ∧
^
i∈I
Ci(ai)

∧

A(a) ,→¬
^
i∈I
Ai(ai)

A joint autonomy principle can now be formulated. An
action plan C(a) ⇒A(a) violates the joint autonomy of
a set {ai | i ∈I} of agents when the agents have a set
(1) of action plans such that a is rationally constrained to
believe C(a) ⇒A(a) interferes with these action plans.
More precisely,
□

P
 C(a) ∧
^
i∈I
Ci(ai)

∧□

A(a) ,→¬
^
i∈I
Ai(ai)

(2)
Your action plan in the example is something like C7(b)∧
¬C8(b) ⇒A3(b), where you are agent b and
C7(b) = “Agent b wishes to go to the bus stop across
the street,”
C8(b) = “There are cars approaching that would en-
danger agent b,” and
A3(b) = “Agent b will cross the street now.”
In the scenario in which I violate your autonomy, I have the
action plan C7(b) ∧¬C8(b) ∧A3(b) ⇒A4(a, b), where I
am agent a and
A4(a, b) = “Agent a will pull agent b off the street.”
I violate your autonomy because
□P
 C7(b) ∧¬C8(b) ∧A3(b)

∧□
 A4(a, b) ,→¬A3(b)

In the scenario in which I pull you out of the path of a car,
my action plan is C8(b) ∧A3(b) ⇒A4(a, b). Even though
we still have the interference A4(a, b) ,→¬A3(b), I do not
violate your autonomy because
¬□P
 C7(b) ∧¬C8(b) ∧C8(b) ∧A3(b)

In fact, the conjunction is logically as well as physically
impossible.
The deontological argument for the joint autonomy prin-
ciple stems again from the fact that an agent legislates for
all agents, due to the universality of reason. A set of action
rules for agents in general can be rational only if they are
compatible with each other, meaning that none can interfere
with another. Thus if an agent adopts an action plan that
interferes with the action plans of others, the agent intro-
duces incompatability into the set of action rules for agents
in general. This is irrational and therefore unethical.
Utilitarian Principle
Utilitarianism is normally conceived as a consequentialist
theory but can be formulated deontologically as well. That
is, rather than judging an act by the net expected utility
it actually creates, the principle can require that an agent
take actions that it can rationally believe maximize what it
regards as utility. Utility is deﬁned as a state of affairs that
the agent regards as an end in itself rather than a means to
some other end, such as happiness.
We might formalize the utilitarian principle as follows.
We suppose there is a utility function u(A(a), C(a)) that
measures the total net expected utility of action A(a) under
conditions C(a). Then an action plan C(a) ⇒A(a) satisﬁes
the utilitarian principle only if agent a can rationally believe
that it creates at least as much utility as any ethical action
plan that is available under the same circumstances. That is,
C(a) ⇒A(a) satisﬁes the utilitarian principle only if
⋄∀A′
u(A(a), C(a)) ≥u(A′(a), C(a))

where A′ ranges over all actions that are available under
conditions C(a) and satisfy the generalization and joint
autonomy principles. Note that we are now quantifying
over predicates and have therefore moved into second-order
logic.
The Medical Example
We can now return to the medical example posed by A&A
and ask how a machine should be programmed to respond
when a patient refuses to take medication at the prescribed
time, based on the deontological criteria developed above.
We will again suppose that there are two options, Notify and
Don’t notify, meaning that the machine will or will not notify
the supervisor of the patient’s refusal.
The scenario is set up in such a way neither option causes
harm to the patient. Since taking the medication on time cre-
ates some beneﬁt (it makes the patient “more comfortable”),
we will assume that Notify results in greater expected utility
that Don’t notify.
There is no clear reason to believe that either option
violates the generalization principle. In any case, we will
assume there is no violation, since the main focus of our
analysis in this scenario is on autonomy.
We cannot accept A&A’s assumption that notifying the
supervisor violates patient autonomy. They base this judg-
ment on Buchanan and Brock’s book (1990), but on ex-
amination of the book, we can ﬁnd no justiﬁcation for it
other than the fact that it reﬂects the expert opinion of these
authors.
Indeed, it is clear that notifying the supervisor does not, in
and of itself, interfere with any of the patient’s action plans.
The patient may prefer that the supervisor not be notiﬁed,
but a preference is not an action plan. The patient may have
an action plan of not personally notifying the supervisor, but
there is no interference with this plan. There could be a vi-
olation of autonomy if notiﬁcation triggers some restriction
of privileges the patient plans to exercise, but this is not part
of the scenario.

--- Page 6 ---

This outcome illustrates the risk of relying on moral
intuition. Notiﬁcation may “go against patient wishes” in
some colloquial sense, perhaps in the sense that the patient
doesn’t want the supervisor to know. Yet notiﬁcation is not
a violation of autonomy, because autonomy is assessed only
with respect to the patient’s actions.
For illustrative purposes, however, we will modify the
scenario so that notiﬁcation does in fact result in a restriction
of privileges the patient wishes to exercise. Even so, there is
no violation of autonomy if the patient has given informed
consent. That is, if the patient entered the institution with the
understanding that refusal to follow medical advice could
result in restriction of certain privileges.
A rule that respects autonomy is therefore
C9(b) ∧¬C10(b) ⇒A5(a, b)
(3)
where
C9(b) = “Patient b has given informed consent to
notiﬁcation,”
C10(b) = “Patient b takes medication at the prescribed
time,” and
A5(a, b) = “The system a will inform a supervisor
that patient b failed to take medication at the prescribed
time.”
We can verify as follows that policy (3) respects autonomy.
Two relevant and coherent action plans are available to pa-
tients in an institution that adopts policy (3), assuming they
are aware of the policy:
C10(b) ∧C11(b) ⇒A6(b)
(4)
¬C9(b) ∧¬C10(b) ∧C11(b) ⇒A6(b)
(5)
where
C11(b) = “Patient b wants to exercise privileges that
are revoked after failure to take medication at the pre-
scribed time,” and
A6(b) = “Patient b will exercise privileges that are re-
voked after failure to take medication at the prescribed
time.”
Action plan (4) is relevant when the patient has taken medi-
cation as prescribed. It is coherent because the patient knows
that, in this case, he/she can exercise privileges regardless of
prior consent. Action plan (5) is relevant if the patient has
refused to take medication as prescribed. As noted earlier, a
rational action plan must include the condition ¬C9(b).
Although we are rationally constrained to believe that
A5(a, b) ,→¬A6(b), policy (3) interferes with action plan
(4) if and only if (2) holds. That is, both of the following
must hold:
□P
 C9(b) ∧¬C10(b) ∧C10(b) ∧C11(b)

(6)
□
 A5(a, b) ,→¬A6(b)

(7)
While (7) is satisﬁed, (6) is clearly violated due to the logical
contradiction between ¬C10(b) and C10(b), and so there
is no violation of autonomy. Similarly, (3) interferes with
action plan (5) if and only if (7) and
□P
 C9(b) ∧¬C9(b) ∧¬C10(b) ∧C11(b)

The latter is violated, and policy (3) therefore respects au-
tonomy.
On the other hand, a policy of notifying without informed
consent is
¬C10(b) ⇒A5(a, b)
which interferes with action plan (5). The policy is therefore
unethical if any patients have this action plan.
Naturally, informed consent must be both informed and
consensual. The institution staff must satisfy themselves that
the patient understands the consequences of notiﬁcation if
the patient fails to take medication as prescribed. This might
be accomplished by discussing the issue with the patient
rather than simply giving a patient a sheaf of papers to
sign. Also the patient must have realistic options other than
giving consent, so that there is no coercion (and violation of
autonomy) in process of obtaining consent.
Conclusion
We have shown how deontological ethics can give rise to
reasonably well-deﬁned and objective principles for ethi-
cally evaluating a machine’s rule base. In particular, we
formulated generalization, joint autonomy, and utilitarian
principles in quantiﬁed modal logic. We indicated how such
a formulation can address some weaknesses of inductive
logic and moral intuitions as a basis for machine ethics.
While we have not removed the human element entirely
from ethical reasoning, we have removed any reliance on
human moral intuitions. At the current stage of research, the
application of ethical principles remains a task for the hu-
man programmer, because they are based partly on the pro-
grammer’s factual knowledge base and what is rational for
the programmer to believe. Humans must also identify the
maximal action plans that are submitted to ethical scrutiny.
Nonetheless, we have shown how deontological principles
can objectively evaluate machine instructions, while calling
on human judgment only in matters of fact.
Furthermore, precise moral principles are a ﬁrst step to-
ward the automation of ethical reasoning. A second step
would be to implement an “ethical blocks world,” in which
all agents have precisely deﬁned action plans and ethical
assessment becomes a purely computational problem. This
may point the way to the automation of ethics in more
complex domains.
An additional advantage of a deontological approach is
that it installs reason-responsiveness, and therefore trans-
parency, in the machine. The machine can explain why it
took a certain action simply by citing the maximal action
plan that generates the particular rule that prompted the
action. The importance of machine transparency has been
much discussed in the AI literature (e.g., Fischer and Rav-
izza 1998; Coates and Swenson 2013; Castelvecchi 2016;
Mueller 2016; Wortham, Theodorou, and Bryson 2016b;
Wortham, Theodorou, and Bryson 2016b). The identiﬁca-
tion of maximal action plans is a systematic approach to
developing it.

--- Page 7 ---

References
Alexander, J. 2012. Experimental Philosophy. Cambridge:
Polity Press.
Anderson, M., and Anderson, S. L. 2007. Machine ethics:
Creating an ethical intelligent agent. AI Magazine (winter)
15–26.
Anderson, M., and Anderson, S. L. 2010. Robot be good.
Scientiﬁc American (October) 72–77.
Anderson, S. L., and Anderson, M. 2011. A prima facie duty
approach to machine ethics: Machine learning of features of
ethical dilemmas, prima facie duties, and decision principles
through a dialogue with ethicists. In Anderson, M., and An-
derson, S. L., eds., Machine Ethics. New York: Cambridge
University Press. 476–492.
Anderson, S. L., and Anderson, M. 2014. GenEth: A general
ethical dilemma analyzer.
In Proceedings of the Twenty-
Eighth AAAI Conference on Artiﬁcial Intelligence, 253–261.
Anderson, M., and Anderson, S. L.
2015a.
Toward en-
suring ethical behavior from autonomous systems: A case-
supported principle-based paradigm. Industrial Robot: An
international Journal 42:324–331.
Anderson, S. L., and Anderson, M.
2015b.
Towards a
principle-based healthcare agent. In van Rysewyk, S. P., and
Pontier, M., eds., Machine medical ethics. Springer. 67–78.
Anderson, M.; Anderson, S. L.; and Armen, C. 2006. An
approach to computing ethics.
IEEE Intelligent Systems
21:2–9.
Anderson, M.; Anderson, S. L.; and Berenz, V.
2017.
A value driven agent: Instantiation of a case-supported
principle-based behavior paradigm. In Proceedings of the
AAAI Workshop on AI, Ethics, and Society, 72–80.
Anscombe, G. 1957. Intention. Oxford: Basil Blackwell.
Appiah, K. A. 2008. Experiments in Ethics. Cambridge,
MA: Harvard University Press.
Beauchamp, T. J., and Childress, J. F. 1979. Principles of
Biomedical Ethics. New York: Oxford University Press.
Bilgrami, A. 1996. Self-Knowledge and Resentment. Cam-
bridg, MA: Harvard University Press.
Buchanan, A. E., and Brock, D. W. 1990.
Deciding for
Others: The Ethics of Surrogate Decision Making.
New
York: Cambridge University Press.
Castelvecchi, D. 2016. Can we open the black box of AI?
Nature 538:20–23.
Coates, D. J., and Swenson, P.
2013.
Reasons-
responsiveness and degrees of responsibility. Philosophical
Studies 165:629–645.
Davidson, D. 1963. Actions, reasons, and causes. Journal
of Philosophy 60:685–700.
Fischer, J. M., and Ravizza, M.
1998.
Reasons-
responsiveness and degrees of responsibility. Cambridge:
Cambridge University Press.
Guarini, M.
2011.
Computational neural modeling and
the philosophy of ethics: Reﬂections on the particularism-
generalism debate. In Anderson, M., and Anderson, S. L.,
eds., Machine Ethics. New York: Cambridge University
Press. 20–23.
Kant, I.
1785.
Grundlegung zur Metaphysik der Sit-
ten (Foundations of the Metaphysics of Morals), volume 4
of K¨oniglichen Preußischen Akademie der Wissenschaften:
Kants gesammelte Schriften. Berlin: Georg Reimer (1900).
Korsgaard, C. M.
1996.
The Sources of Normativity.
Cambridge: Cambridge University Press.
Mueller, E. T. 2016. Transparent Computers: Designing Un-
derstandable Intelligent Systems. CreateSpace Independent
Publishing Platform.
Nagel, T. 1986. The View from Nowhere. Oxford: Oxford
University Press.
O’Neill, O. 2014. Acting on Principle: An Essay on Kantian
Ethics, 2nd ed. Cambridge: Cambridge University Press.
Rawls, J.
1971.
A Theory of Justice.
Cambridge, MA:
Harvard University Press.
Ross, W. D. 1930. The Right and the Good. Oxford: Oxford
University Press.
Schwitzgebel, E., and Rust, J.
2016.
The behavior of
ethicists.
In A Companion to Experimental Philosophy.
Malden, MA: Wiley Blackwell.
Sinnott-Armstrong, W.
2006.
Moral intuitionism meets
empirical psychology.
In Metaethics after Moore. New
York: Oxford University Press.
Wallach, W.; Allen, C.; and Smit, I. 2008. Machine morality:
Bottom-up and top-down approaches for modeling human
moral faculties. AI & Society 565–582.
Wortham, R. H.; Theodorou, A.; and Bryson, J. J. 2016a.
Robot transparency, trust and utility.
In Principles of
Robotics Workshop. Shefﬁeld, UK: Proceedings of AISB.
Wortham, R. H.; Theodorou, A.; and Bryson, J. J. 2016b.
What does the robot think? Transparency as a fundamental
design requirement for intelligent systems.
In Ethics for
Artiﬁcial Intelligence Workshop. New York: IJCAI.

```
