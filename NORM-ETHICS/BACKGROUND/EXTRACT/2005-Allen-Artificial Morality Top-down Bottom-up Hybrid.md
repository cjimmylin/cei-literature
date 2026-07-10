---
title: "2005-Allen-Artificial Morality Top-down Bottom-up Hybrid - Background Extract"
source_pdf: "2005-Allen-Artificial Morality Top-down Bottom-up Hybrid.pdf"
source_folder: "02-external-papers"
pages: 7
extracted_at: "2026-04-03T10:25:00"
---

# Background Extract: 2005-Allen-Artificial Morality Top-down Bottom-up Hybrid

**Source PDF:** 2005-Allen-Artificial Morality Top-down Bottom-up Hybrid.pdf
**Source:** 02-external-papers
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

Artiﬁcial morality: Top-down, bottom-up, and hybrid approaches
Colin Allen1, Iva Smit2 and Wendell Wallach3
1Department of History and Philosophy of Science, 1011 E. Third Street, Bloomington, IN 47405, USA
2E&E Consultants, Slawijkseweg 11, 7077 AM, Netterden, The Netherlands
3Yale University Interdisciplinary Center for Bioethics, P.O. Box 208209, New Haven, CT 06520-8209, USA
E-mails: colallen@indiana.edu; iva.smit@planet.nl; wwallach@comcast.net
Abstract. A principal goal of the discipline of artiﬁcial morality is to design artiﬁcial agents to act as if they are
moral agents. Intermediate goals of artiﬁcial morality are directed at building into AI systems sensitivity to the
values, ethics, and legality of activities. The development of an eﬀective foundation for the ﬁeld of artiﬁcial
morality involves exploring the technological and philosophical issues involved in making computers into
explicit moral reasoners. The goal of this paper is to discuss strategies for implementing artiﬁcial morality and
the diﬀering criteria for success that are appropriate to diﬀerent strategies.
Key words: artiﬁcial morality, autonomous agents, ethics, machines, robots, values
Introduction
Artiﬁcial morality shifts some of the burden for eth-
ical behavior away from designers and users, and
onto the computer systems themselves. The task of
developing artiﬁcial moral agents becomes particu-
larly important as computers are being designed to
perform with greater and greater autonomy, i.e., with
less and less direct human supervision. The speed at
which computers execute tasks increasingly prohibits
humans from evaluating whether each action is per-
formed in a responsible or ethical manner. Imple-
menting software agents with moral decision-making
capabilities oﬀers the promise of computer systems
that are able to evaluate whether each action per-
formed is ethically appropriate. This in no way serves
as a substitute for the moral responsibility of those
who deploy or use computers. It merely means that it
will be easier to use computers in an ethical manner if
sensitivity to ethical and legal values is integral to the
software (Wallach 2004).
Regardless of whether artiﬁcial morality is genuine
morality, artiﬁcial agents act in ways that have moral
consequences. This is not simply to say that they may
cause harm – even falling trees do that. Rather, it is to
draw attention to the fact that the harms caused by
artiﬁcial agents may be monitored and regulated by
the agents themselves. While some aspects of the
insertion of intelligent artifacts into the moral land-
scape may be manageable without speciﬁc attention
to the software or mechanisms controlling their
behavior – i.e., by treating them as ethical ‘black
boxes’ – we
would
argue
that
artiﬁcial
morality
should also be approached proactively, as an engi-
neering design challenge for explicitly building ethi-
cally appropriate behavior into artiﬁcial agents. The
attempt to design artiﬁcial moral agents forces con-
sideration of the information required for ethical
decision making, and of the algorithms which may be
appropriately applied to the available information.
In this paper we discuss the philosophical roots
and computational possibilities of top-down and
bottom-up strategies for designing artiﬁcial moral
agents (AMAs). We pick up where Allen et al. (2000)
left oﬀwhen they wrote, ‘Essential to building a
morally praiseworthy agent is the task of giving it
enough intelligence to assess the eﬀects of its actions
on sentient beings, and to use those assessments to
make appropriate choices’. Top-down approaches to
this task involve turning explicit theories of moral
behavior into algorithms. Bottom-up approaches
involve attempts to train or evolve agents whose
behavior
emulates
morally
praiseworthy
human
behavior.
Top-down approaches
The idea behind top-down approaches to the design
of AMAs is that moral principles or theories may
be used as rules for the selection of ethically appro-
priate actions. Rule-based approaches to artiﬁcial
Ethics and Information Technology (2005) 7:149 – 155
 Springer 2006
DOI 10.1007/s10676-006-0004-4

--- Page 2 ---

intelligence have been appropriately criticized for
their unsuitability for providing a general theory of
intelligent action. Such approaches have proven to be
insuﬃciently robust for almost any real-world task.
Yet there remain speciﬁc domains where rule-based
approaches provide the best available technology,
and it is an open research question whether moral
behavior is one of these domains. Hence, even though
(we believe) the objections to rule-based approaches
are
rather
strong, it
is incumbent
on aspiring
designers of AMAs to consider the prospects and
problems inherent in top-down approaches. Speciﬁc
objections
to
top-down
approaches
to
artiﬁcial
morality (rather than general objections to rule-based
A.I. generally) are best understood after giving
careful consideration to the prospects for building
AMAs by implementing decision procedures that are
modeled on explicit moral theories.
Candidate principles for conversion to algorithmic
decision procedures range from religious ideals and
moral
codes
to culturally
endorsed
values
and
philosophical systems. The Golden Rule, The Ten
Commandments, utilitarianism, and Kantian deon-
tology are some of the possible sources of rules for
top-down ethical systems. When considering robots,
Asimov’s three laws (which he later expanded to four)
also come to mind as a top-down system of ethics.
While many of the same values are evident in diﬀer-
ing ethical systems, there are also signiﬁcant diﬀer-
ences
which would
make
the
selection
of any
particular theory for top-down implementation a
matter of obvious controversy. We will not enter that
controversy here – instead, our task is to be equal-
opportunity critics, pointing out strengths and limi-
tations of some major top-down approaches.
Abstractly considered, top-down morality is all
about having a set of rules to follow. In some ways
of thinking, the list of rules is a heterogeneous grab
bag of whatever needs to be speciﬁcally proscribed
or prescribed. This is the ‘commandment’ model of
morality, which, as well as having roots in the
Judaic tradition, also pops up in Asimov’s laws of
robotics. A strength of commandment models is that
they can have particular rules tailored to particular
types of ethically relevant behavior (one for killing,
one for stealing, etc.). However, a major trouble
with commandment models, thus conceived, is that
the rules often conﬂict. Such conﬂicts produce
computationally intractable situations unless there is
some further principle or rule for resolving the
conﬂict. Most commandment systems are silent on
how conﬂicts are to be resolved. Asimov’s initial
approach was to prioritize the rules so that the ﬁrst
law always trumped the second, which in turn
always trumped the third. Unfortunately, however,
the ﬁrst two of Asimov’s original laws are each
suﬃcient to produce intractable conﬂict on their
own. The addition of the ‘zeroth’ law, to protect
humanity as a whole, is unfortunately silent on what
counts as such a harm, and thus does not eﬀectively
arbitrate when
there
are
mutually
incompatible
duties to prevent harm to diﬀerent individuals, i.e.,
when protecting one will cause harm to the other
and vice versa.
Philosophers have attempted to ﬁnd more general
or abstract principles from which all the more speciﬁc
or particular principles might be derived. Both utili-
tarianism and Kantian deontology provide general
principles which may be relevant to the design of
ethical robots (Gips 1995).
A strength of utilitarianism in a computational
context is its explicit commitment to quantifying
goods and harms. This is also, of course, a weak-
ness – for it is a notorious problem of utilitarianism
that certain pleasures and pains appear to be
incommensurable. While some economists may think
that money provides a common measure (how much
one is willing to spend to obtain some good or avoid
some harm), this is controversial. But even if the
problem of measurement could be solved, any top-
down implementation of utilitarianism would have a
lot of computing to do. This is because many, if not
all, of the consequences of the available alternatives
must be computed in advance in order to compare
them. Consequences of acts will range over varying
types of members of the moral constituency (people,
perhaps some animals, and possibly even entire eco-
systems), and many secondary ‘ripple’ eﬀects will
have to be anticipated. The utilitarian AMA may also
have to decide whether and how to discount eﬀects in
the distant future.
In contrast to utilitarianism, deontological theo-
ries focus on the motives for action, and require
agents to respect speciﬁc duties and rights. To resolve
the problem that speciﬁc duties may appear to con-
ﬂict, all prima facie duties may be submitted to a
higher principle, such as Kant’s categorical impera-
tive. It turns out that a computational Kantian would
also have to do a lot of computing in order to achieve
a full moral evaluation of any action. This is because
Kant’s approach to the moral evaluation of actions
requires not only access to one’s motives, which an
AMA might not have, but also a full understanding
of how to characterize the motives behind the action,
and an assessment of whether there would be any
inconsistency
if
every
rational
agent,
including
humans, acted on the same motive. This requires a lot
of understanding of human psychology and of the
eﬀects of actions in the world. The problem is not
unique to Kant’s theory – other general deontological
COLIN
OLIN ALLEN
LLEN ET AL
ET AL
150

--- Page 3 ---

principles that seek to resolve conﬂicts among prima
facie duties would face similar issues.
Both consequentialist (e.g., utilitarian) and deon-
tological (e.g., Kantian) approaches raise their own
speciﬁc computational problems, but they also raise a
common problem of whether any computer (or
human, for that matter) could ever gather and com-
pare all the information that would be necessary for
the theories to be applied in real time. This problem
seems
especially
acute
for
a
consequentialist
approach, since the consequences of any action are
essentially unbounded in space or time. The problem
does not go away for a deontologist because consis-
tency between the duties can typically only be asses-
sed through their eﬀects in space and time.
Of course humans apply consequentialist and
deontological reasoning to practical problems with-
out calculating endlessly the utility or moral ramiﬁ-
cations of an act in all possible situations. Our
morality, just as our reasoning, is bounded by time,
capacity, and inclination. In a similar vein, parame-
ters might also be set on the extent to which a com-
putational system analyzes the consequences or
imperative of a speciﬁc action. How might we set
those limits on the options considered by a computer
system, and will the course of action taken by such a
system in addressing a speciﬁc challenge be satisfac-
tory? In humans the limits on reﬂection are set by
heuristics and aﬀective controls. Both heuristics and
aﬀect can at times be irrational, but also tend to
embody the wisdom gained through experience. We
may well be able to implement heuristics in compu-
tational systems. Professional codes of conduct may
be of some help in this context (e.g., Floridi and
Sanders 2004 argue that Association of Computing
Machinery Code of Ethics may be adapted for arti-
ﬁcial agents). Nevertheless, heuristic rules of thumb
leave many issues of priority and consistency unre-
solved. The implementation of aﬀective controls
represents a much more diﬃcult challenge.
Bottom-up and developmental approaches
By ‘bottom-up’ approaches to the development of
AMAs we mean those that do not impose a speciﬁc
moral theory, but which seek to provide environ-
ments in which appropriate behavior is selected or
rewarded. These approaches to the development of
moral sensibility entail piecemeal learning through
experience, either by unconscious mechanistic trial
and failure of evolution, the tinkering of program-
mers or engineers as they encounter new challenges,
or
the
educational
development
of
a
learning
machine.
Each
of
these
methods
shares
some
characteristics with the manner in which a young
child acquires a moral education in a social context
which
identiﬁes
appropriate
and
inappropriate
behavior without necessarily providing an explicit
theory of what counts as such.
Bottom-up strategies hold the promise of giving
rise to skills and standards that are integral to the
over-all design of the system, but they are extremely
diﬃcult to evolve or develop. Evolution and learning
are ﬁlled with trial and error – learning from mistakes
and unsuccessful strategies. This can be a slow task,
even in the accelerated world of computer processing
and evolutionary algorithms.
Alan Turing reasoned in his classic paper ‘Com-
puting machinery and intelligence’ (Turing 1950) that
if we could put a computer through an educational
regime comparable to the education a child receives,
‘We may hope that machines will eventually compete
with men in all purely intellectual ﬁelds’. Presumably
this educational regime might include a moral edu-
cation similar to the manner in which we humans
acquire a sensibility regarding the moral ramiﬁca-
tions of our actions. But simulating a child’s mind is
only one of the strategies being pursued for designing
intelligent agents capable of learning. Simulations of
evolution, the design of computational learning
platforms, and associative learning techniques will all
play a role in the bottom-up development of AMAs.
We’ll begin with a discussion of the more primitive
approaches, for they might contribute to the design
of the more sophisticated learning platforms.
Artiﬁcial life and the emergence of social values
The platform for artiﬁcial life experiments (Alife) –
i.e., the simulation of evolution within computer
systems – is the unfolding of a genetic algorithm
within relatively simply deﬁned computer environ-
ments. An intriguing question is whether a computer
or Alife might be able to evolve ethical behavior. The
prospect that Alife could give birth to moral agents
derives from Wilson’s (1975) hypothesis that a science
of sociobiology might give rise to ‘a precise account
of the evolutionary origin of ethics’. If the founda-
tional values of human society are rooted in our
biological heritage, than it would be reasonable to
presume that these values could reemerge in a simu-
lation of natural selection.
The most promising Alife experiments derive from
game theory and involve iterated rounds of the pris-
oners’ dilemma game (Axelrod and Hamilton 1981).
Danielson (1992, 1998) and his colleagues at the
University of British Columbia’s Centre for Applied
Ethics constructed simulated environments in which
virtual organisms can change and adapt in response
ARTIFICIAL
RTIFICIAL MORALITY
ORALITY
151

--- Page 4 ---

to the actions of other entities in the population.
Danielson calls his Alife simulations ‘moral ecolo-
gies’. As in the prisoners’ dilemma, these organisms
can cooperate or defect, act as predators or altruists.
They move about within the computer simulation,
and to Danielson’s surprise the mindless individual
entities began to form their own groups. The altruists
would group together with other altruists and the
predators would also hang out together. In tough
times, when the resources were limited, the predators
would die oﬀwhile the cooperators had a competitive
advantage. Danielson proposes a concept of ‘func-
tional’ morality in which rationality is the only pre-
requisite for an agent to be a moral agent (see also
Skyrms 1996, and Danielson and Harms’ Evolving
Artiﬁcial Moral Ecologies project, accessed at http://
www.ethics.ubc.ca/eame/ on September 17, 2005).
Alife simulations hold great promise in fostering
the emergence of moral agents that display at least
foundational values in their behavior. However, to
date, the mindless moral agents developed within
simulations of evolution are very simple and far from
being able to engage in reﬂection on abstract and
theoretical
issues,
which
is
a
hallmark
of
the
sophisticated moral sensibilities of humans. The
question is still outstanding whether Alife will prove
to be helpful in the development of artiﬁcial moral
agents
capable
of
engaging
the
more
complex
dilemmas that we encounter daily. We should not
forget, however, that evolution has also led to
immoral behavior.
Unbiased learning platforms
Noting the limitations inherent in systems designed
around rule-based ethics, Chris Lang1 recommends
‘quest ethics’, a strategy wherein the computer learns
about ethics through a never-ending quest to maxi-
mize its goal, whether that goal is to be ‘just’ or to be
‘moral’. By endlessly searching for a better and better
solution, such a machine will presumably develop
from a temporarily immature state to a level where
we might designate it a moral agent.
Lang’s ‘unbiased learning machines’ are designed
around a non-terminating learning algorithm or what
is sometimes called a ‘hill-climbing’ or a ‘greedy-
search’ algorithm. In straightforward applications,
these algorithms evolve to be smarter and demon-
strably faster than their human counterparts. Lang is
optimistic, but can a machine, whose actions are
determined by its previous state and inputs, gain the
freedom to choose between options, to model itself to
an environment, and act in accordance with human
values?
There are two central challenges in designing a
computer capable of continually questing for a higher
morality: specifying the goal or goals of the system,
and enabling an endless ﬂow of fresh real world data
that expand the domain the system peruses in its
quest. Although deﬁning the goals could lead to
considerable philosophical disagreement, the more
diﬃcult challenge in designing a morally praisewor-
thy agent lies in stimulating the system to expand its
realm of potential choices. For as von Foerster (1992)
pointed out, it is not just the question of being able to
choose, but also the expansion of the available
choices that is central to our ethics and our human
ability to invent ourselves.
Associative learning machines and humanoids
If morality is primarily learned, built up through
experience, trial and error, and honed through our
capacity for reason, then teaching an AMA to be a
moral agent may well require a similar process of
education. Associative learning techniques model the
education children receive in the form of rewards and
punishment,
approval
and
disapproval.
Finding
eﬀective counterparts to reward and punish, suitable
for training a robot or computer is a problematic
task. Lang recommends rewarding unbiased learning
machines with richer data when they behave ethically.
Simulating sensory pain is also an option. The intent
behind a reward and punishment system of moral
education may be that the child’s discovery of shared
ethical concerns or principles may be most eﬀectively
guided by a process of discovery that is guided by
parents and teachers who have at least a rudimentary
understanding of the trajectory the learning will fol-
low. Children naturally move on to the next level of
moral reasoning as they come to appreciate the lim-
itations of the reasons which they have identiﬁed. The
primary challenge of imbuing an AMA with such a
degree of insight lies in implementing feedback to the
computation system that goes beyond a simple binary
indicator that a justiﬁcation for an act is acceptable
or unacceptable.
In a controlled laboratory we would need to create
a series of learning situations through which the
AMA would work its way toward a level of moral
behavior acceptable by the standards we deﬁne. The
rich plethora of algorithms developed to facilitate
machine learning, case-based reasoning, data acqui-
sition, and data-mining are just beginning to be
combined into computational systems capable of
utilizing an array of learning tools. In principle there
1 C. Lang, Ethics for Artiﬁcial Intelligences, unpublished
ms. accessed at http://philosophy.wisc.edu/lang/AIEthics/
index.htm on September 17, 2005.
COLIN
OLIN ALLEN
LLEN ET AL
ET AL
152

--- Page 5 ---

is no reason why these learning platforms cannot be
adapted for at least rudimentary moral reasoning. If
we hope to pursue a developmental path in creating
an AMA, whether our artiﬁcial agent actually learns
in the same manner as we humans is less important
than their ability to learn. The more serious consid-
eration is whether machines can be trained to work
with the kind of abstract principles that are the
hallmark of higher order moral reasoning.
Dangers inherent in learning systems
Chris Lang’s optimistic vision that unbiased learning
systems would develop naturally toward an ethical
sensibility that valued humans and human ethical
concerns sits in sharp contrast to the more dire
futuristic predictions regarding the dangers AI poses.
After all, any system which has the ability to learn
can also potentially undo any restraints built into the
system. The layered architecture of computational
systems commonly isolates lower level standards and
protocols from higher order functionality. Core
restraints can presumably be built into foundation
layers of the computer platform, which are inacces-
sible to those parts of the computer that learn and
revise the structures that ﬁlter new information. This
of course raises the question of what moral restraints
or moral grammar are to be encoded into these
‘deeper’ protocols.
The concept of a moral grammar plays a key role
in Josh Storrs Hall’s discussion of machine ethics.2 In
his view, moral codes are similar to language gram-
mars, for the vast majority of people ‘learn moral
rules by osmosis, internalizing them not unlike the
rules of grammar of their native language, structuring
every act as unconsciously as our inbuilt grammar
structures our sentences’. He argues that there are
structures in our brains that predispose us to learn
moral codes, and that determine within broad limits
the kinds of codes we can learn. Thus ‘while the
moral codes of human cultures vary within those
limits, they have many structural features in com-
mon’. Extensive studies notwithstanding, the innate
grammar of language has remained elusive, as, can be
argued, has the ‘moral deep structure’, or what the
philosophers of the Scottish Enlightenment called the
‘moral sense’. It would require a clear explication of
the code that governs our moral sensibility to pro-
gram this foundational grammar into the lower levels
of a system’s architecture.
Key restraints could also be programmed into a
computational system at a very low level. They would
act as something like a human conscience. In the
short-term we need not be concerned that a learning
system
will
root
out
these
deeply
embedded
restraints. But like the ability of humans to override
their conscience given the right goals, desire, or
motivation, learning computers might also ﬁnd ways
to circumvent restraints that got in the way of their
goals. In the meantime, the larger concern is that very
small
incremental
changes
made
to
structures
through which an AMA acquires and processes the
information it is assimilating will lead to subtle, dis-
turbing, and potentially destructive behavior. In sit-
uations requiring precision, even little errors could
potentially lead to dramatic consequences. Learning
systems may well be one of the better options for
developing sophisticated AMAs, but the approach
holds its own set of unique issues.
Hybrid approaches
The top-down approaches emphasize the importance
of explicit ethical concerns that arise from outside of
the entity, while the bottom-up approaches are
directed more at the cultivation of implicit values that
arise from within the entity. Top-down principles
represent broad controls, while values that emerge
through the bottom-up development of a system can
be understood as causal determinants of a system’s
behavior. Ethical principles such as justice and max-
imizing the aggregate good tend to restrict options –
they presume a context in which the actor has broad
freedoms in the manner he can act, but whose action
must be conﬁned to morally praiseworthy behavior.
Evolution and the learning of a machine are directed
toward the expansion of choices and ﬂexibility in
behavior. The ethical restraints the evolving system
learns to honor are those that will increase its choices
and its opportunity to survive and ﬂourish. The top-
down ethical restraints reinforce the principle that
moral behavior often requires limiting one’s freedom
of action and behaving in ways that may not be in
one’s short-term or self-centered interest for the good
of society. Both top-down and bottom-up approa-
ches embody diﬀerent aspects of what we commonly
consider a sophisticated moral sensibility.
If no single approach meets the criteria for desig-
nating an artiﬁcial entity as a moral agent, then some
hybrid will be necessary. Hybrid approaches pose the
additional problems of meshing both diverse philos-
ophies
and
dissimilar
architectures.
Genetically
acquired propensities, the rediscovery of core values
through experience, and the learning of culturally
2 J. Storrs Hall, Ethics for Machines, unpublished ms.
Accessed http://discuss.foresight.org/josh/ethics.html on
September 17, 2005.
ARTIFICIAL
RTIFICIAL MORALITY
ORALITY
153

--- Page 6 ---

endorsed rules all inﬂuence the moral development of
a child. During young adulthood those rules may be
reformulated into abstract principles that guide one’s
behavior. We should not be surprised if designing a
praiseworthy moral agent will also require compu-
tational systems capable of integrating diverse inputs
and inﬂuences, including top-down values informed
by a foundation moral grammar and a rich appreci-
ation of context. Von Neumann Machines and neural
networks, genetic and learning algorithms, rule and
natural
language
parsers,
virtual
machines
and
embodied robots, aﬀective computing and standards
for facilitating cooperative behavior between dissim-
ilar systems may all be enlisted in tackling aspects of
the challenge entailed in designing an eﬀective AMA.
Designers of AMAs cannot aﬀord to be theoretical
purists with respect to questions about how to
approach moral intelligence.
One central question is whether systems capable
of making moral-decisions will require some form
of emotions, consciousness, a theory of mind, an
understanding of the semantic content of symbols, or
need to be embodied in the world. While we feel that
hybrid systems without aﬀective or advanced cogni-
tive faculties will be functional in many domains, it
will be essential to recognize when additional capa-
bilities will be needed. Embodiment is both a goal
and a bottom-up strategy that is very evident in
subsumptive and evolutionary or epigenetic robotic
architecture. The promise that other advanced aﬀec-
tive and cognitive skills will emerge through the
evolution of complex embodied systems is highly
speculative. Nevertheless, facilitating the emergence
of advanced faculties or designing modules for com-
plex aﬀective and cognitive skills may well be
required for fully autonomous AMAs.
Evaluating machine morality
As we stated above, the goal of the discipline of
artiﬁcial morality is to design artiﬁcial agents to act
as if they are moral agents. Questions remain about
appropriate criteria for evaluating eﬀectiveness in this
area. Just as there is not one universal ethical theory,
there is no agreement on what it means to be a moral
agent, let alone a successful artiﬁcial moral agent. A
Moral Turing Test (Allen et al. 2000) is one possible
strategy for evaluating the adequacy of an AMA in
light of diﬀering theories of moral agency. Turing’s
test for machine intelligence is notoriously contro-
versial, and we would not endorse it as a criterion for
strong A.I. or genuine moral agency. Nevertheless,
some sort of ‘blind’ comparison to human perfor-
mance may be a useful tool in assessing the accept-
ability of AMA behavior.
It is important to keep in mind that the existing
ethical theories were developed with human beings in
mind, long before computers and autonomous intel-
ligent agents entered the scene. The engineering
requirements of artiﬁcial morality place the discor-
dant theories in a new context that forces us to re-
evaluate their signiﬁcance as speciﬁcations for moral
action. Computers and robots are largely a product
of a materialistic worldview which presupposes a set
of metaphysical assumptions that are not always
compatible with the spiritual worldviews which pro-
duced many of our ethical categories and much of
our ethical understanding. While this metaphysical
tension by no means obviates the project of intro-
ducing moral decision-making abilities into comput-
ers, it should sensitize us about being too facile in
reducing complex subjects, such as the need for a
conscience, to an easily manageable set of skills.
Honest people may diﬀer on the extent to which
human morality may be transplanted to machines.
But the challenges posed by our increasingly auton-
omous systems will not go away, even if they mean
that a new ethical theory has to be developed for
artiﬁcial morality. This is a topic which requires
further discussion.
Computers pose unique ethical considerations that
are of particular philosophical interest (Floridi 1999).
The ﬁeld of artiﬁcial morality extends that interest
beyond mere theory and analysis and towards an
actual engineering task. The objective of building
morally praiseworthy systems is complementary to
that of distributing and enforcing accountability
when things go wrong. However, possibilities for
‘creative stewardship’ of complex artifacts (Floridi
and Sanders 2004) will be enhanced if, rather than
viewing artiﬁcial moral agents as ethical black boxes,
engineers, programmers, and philosophers collabo-
ratively contribute to the analysis of the engineering
requirements
for
the
development
of
artiﬁcial
morality.
References
C. Allen, G. Varner and J. Zinser. A Prolegomena to Any
Future Artiﬁcial Moral Agent. Journal of Experimental
and Theoretical Artiﬁcial Intelligence, 12: 251 – 261, 2000.
R. Axelrod and W. Hamilton. The Evolution of Cooper-
ation. Science, 211: 1390 – 1396, 1981.
P. Danielson, Artiﬁcial Morality: Virtuous Robots for
Virtual Games. Routledge, New York, 1992.
P. Danielson, Modeling Rationality, Morality and Evolution.
Oxford University Press, New York, 1998.
COLIN
OLIN ALLEN
LLEN ET AL
ET AL
154

--- Page 7 ---

L. Floridi. Information Ethics: On the Philosophical
Foundation of Computer Ethics. Ethics and Information
Technology, 1: 37 – 56, 1999.
L. Floridi and J.W. Sanders. On the Morality of Artiﬁcial
Agents. Minds and Machines, 14: 349 – 379, 2004.
H. Foerster. Ethics and Second-order Cybernetics. Cyber-
netics & Human Knowing, 1: 9 – 25, 1992.
J. Gips.
Towards the Ethical Robot. In K. Ford, C.
Glymour and P. Hayes, editors, Android Epistemology,
pp. 243 – 252. MIT Press, Cambridge, MA, 1995.
B. Skyrms, Evolution of the Social Contract. Cambridge
University Press, New York, 1996.
A. Turing. Computing Machinery and Intelligence. Mind,
59: 433 – 460, 1950.
W. Wallach. Artiﬁcial Morality: Bounded Rationality,
Bounded Morality and Emotions. In I. Smit, G. Lasker
and W. Wallach, editors, Proceedings of the Intersymp
2004 Workshop on Cognitive, Emotive and Ethical Aspects
of Decision Making in Humans and in Artiﬁcial Intelli-
gence, pp. 1 – 6, Baden-Baden, Germany, IIAS, Windsor,
Ontario, 2004.
E.O. Wilson, Sociobiology: The New Synthesis. Harvard/
Belknap, Cambridge, MA, 1975.
ARTIFICIAL
RTIFICIAL MORALITY
ORALITY
155
```
