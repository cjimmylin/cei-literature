---
title: "2024-Unknown-On the Pros and Cons of Active Learning for Moral Preference - PDF Extract"
source_pdf: "2024-Unknown-On the Pros and Cons of Active Learning for Moral Preference.pdf"
pages: 30
extracted_at: "2026-02-07T17:00:46.492415"
---

# PDF Extract: 2024-Unknown-On the Pros and Cons of Active Learning for Moral Preference

**Source PDF:** 2024-Unknown-On the Pros and Cons of Active Learning for Moral Preference.pdf
**Total Pages:** 30

---

## Content

```
--- Page 1 ---

On the Pros and Cons of Active Learning for Moral
Preference Elicitation
Vijay Keswani1, Vincent Conitzer∗2,3, Hoda Heidari∗2, Jana Schaich Borg∗1, and Walter
Sinnott-Armstrong∗1
1Duke University
2Carnegie Mellon University
3University of Oxford
Abstract
Computational preference elicitation methods are tools used to learn people’s preferences
quantitatively in a given context. Recent works on preference elicitation advocate for active
learning as an efficient method to iteratively construct queries (framed as comparisons between
context-specific cases) that are likely to be most informative about an agent’s underlying pref-
erences. In this work, we argue that the use of active learning for moral preference elicitation
relies on certain assumptions about the underlying moral preferences, which can be violated
in practice. Specifically, we highlight the following common assumptions (a) preferences are
stable over time and not sensitive to the sequence of presented queries, (b) the appropriate
hypothesis class is chosen to model moral preferences, and (c) noise in the agent’s responses
is limited. While these assumptions can be appropriate for preference elicitation in certain
domains, prior research on moral psychology suggests they may not be valid for moral judg-
ments. Through a synthetic simulation of preferences that violate the above assumptions, we
observe that active learning can have similar or worse performance than a basic random query
selection method in certain settings. Yet, simulation results also demonstrate that active learn-
ing can still be viable if the degree of instability or noise is relatively small and when the agent’s
preferences can be approximately represented with the hypothesis class used for learning. Our
study highlights the nuances associated with effective moral preference elicitation in practice
and advocates for the cautious use of active learning as a methodology to learn moral prefer-
ences.
1
Introduction
Ensuring proper deployment of artificial intelligence (AI) systems in high-stakes societal domains
requires building trust in the decisions of these systems. To that end, recent work on ethical
and participatory algorithmic development emphasizes the importance of encoding stakeholders’
values in these systems, especially their moral judgments/preferences over actions that can cause
significant harm to others Feffer et al. (2023). Incorporating stakeholders’ moral preferences allows
for the creation of tools whose judgments are normatively aligned with those of the stakeholders
and helps counter various harms associated with the use of computational tools. To accomplish
this goal, however, one first needs to accurately elicit people’s moral preferences.
*These authors contributed equally to this work and are ordered alphabetically.
1
arXiv:2407.18889v1  [cs.HC]  26 Jul 2024

--- Page 2 ---

Figure 1: Example of a pairwise comparison from the Boestler et al. (2024) study on kidney allo-
cation decisions.
Studies on moral preference elicitation often present agents with pairs of context-specific cases
and ask them to choose the one they prefer. Using the agent’s responses for a set of such pairwise
comparisons, one can try to learn a representation of their underlying preferences. To formalize
this setting, let X ⊆Rd denote the space of all cases over which any agent has preferences, with
d ∈Z+ denoting the number of features describing each case. Following the standard preference
elicitation literature, suppose that an agent’s preferences are determined by comparing the value
of an underlying utility function u : X →R across cases Freedman et al. (2020). For any input pair
x, x′ ∈X × X, the agent prefers x over x′ iff u(x) > u(x′). Let R : X × X →{0, 1} denote their
response function, with R(x, x′) = 1(u(x) > u(x′)), where 1(·) is the indicator function.
Multiple recent studies employ this framework for moral preference elicitation. For example,
Boestler et al. (2024) model lay-agent’s moral preferences in kidney allocation. They provide par-
ticipants with profiles of two patients who need kidney transplants and ask them to decide which
patient should receive the one available kidney. Each patient profile contains features like the
patient’s number of children, years of life they will gain from the transplant, etc. The choice
between the two patients can pose a moral dilemma when different features favor different pa-
tients Sinnott-Armstrong et al. (2021) (Figure 1 presents a pairwise comparison scenario from this
study). Another well-known example of this approach is the “Moral Machines” study, in which
participants are presented with sacrificial moral dilemmas and asked what an autonomous vehicle
should do in each case Awad et al. (2018); Noothigattu et al. (2018). In another study, Srivastava
et al. (2019) elicit fairness preferences by presenting participants with pairwise comparisons of al-
gorithmic predictions and backing out the notion of fairness that is most compatible with their
responses. Preference elicitation has similarly been part of the development pipeline of various
participatory computational frameworks Lee et al. (2019); Kahng et al. (2019); Loreggia et al. (2019);
Feffer et al. (2023).
The goal of preference elicitation in these settings is to accurately and efficiently learn a represen-
tation of the agent’s underlying utility u(·) using their responses for a given set of N pairwise
comparisons, i.e., using {(xt, x′
t, R(xt, x′
t))}N
t=1. Here, accuracy refers to the ability to (a) recover
the utility function u and/or (b) offer an approximate representation of u that mimics decisions
made through u in a large number of comparisons. Achieving accuracy often requires presenting
an agent with numerous pairwise comparisons, which can be onerous and expensive. To reduce
the number of queries required to obtain a desired level of accuracy, active learning is frequently
2

--- Page 3 ---

invoked as an alternative approach.
Active learning methods operate in the realm of scarce outcome-labeled data, where one has the
option to interactively query an oracle (the user/agent in this case) for labels, and the goal is to
learn the relationship between labels and relevant features using as few queries as possible Settles
(2009). These methods can help improve the efficiency of preference elicitation as well. For pref-
erence elicitation, active learning techniques can suggest new pairwise comparisons that would
provide the maximal information about the agent’s utility function given the information gathered
so far Dragone et al. (2018). Using this form of structured determination of the next pairwise com-
parison (based on the agent’s previous responses), the agent’s preferences can be inferred faster
than the setting where they are presented with random comparisons at each time step. For this
reason, multiple recent works consider active-learning-based preference elicitation. Yang et al.
(2021) use interactive elicitation to create recommendation systems. Srivastava et al. (2019) de-
velop active-learning-based surveys to elicit fairness preferences. Johnston et al. (2023) use active
learning to learn preferences regarding healthcare resource allocation. These recent use cases of
active learning provide evidence of its ability to efficiently elicit people’s preferences. However,
the effectiveness of active learning relies on certain assumptions that may not hold in the case
of moral preferences.
Moral preferences capture a person’s normative views over available actions in moral dilemmas—
that is, what is the right thing to do when the chosen action could lead to significant harm to others,
but not (or not only) to the participant themself? A popular example is the trolley problem, where
the participant is asked which human lives should be prioritized, passengers or pedestrians Foot
(1967). Similarly, in the kidney allocation example described earlier, when asked to decide which
of two patients on the kidney transplant list should get the kidney, a participant’s decisions are
based on patient features that they consider morally relevant. In these settings, when an agent
expresses a preference for one patient over another, their judgment can be characterized by the
underlying utility function they use to assign relevance scores to the available actions, choosing
the action with the highest assigned score. Note that, despite the use of utility functions, this
standard setup does not presuppose any utilitarian moral theory because it can model agents who
base their decisions on non-utilitarian factors, such as past misbehaviors by patients. Modeling
the participant’s preferences in moral decision-making settings (e.g., by learning their underlying
utility function) allows for predicting their moral judgments when presented with new dilemmas
in the same setting. Therefore, these models can be useful in the development of ethical AI tools
Feffer et al. (2023).1 However, eliciting moral preferences can be challenging, and differ from the
process of eliciting other kinds of preferences.
Moral preferences concern harms to others, and differ from self-interested, economic, or material
preferences, where the agent chooses the option with the highest subjective utility to self Capraro
and Perc (2021). Instead of being concerned only with the self, moral preferences are intended
to be impartial Vanberg (2008) and fair Bicchieri and Chavez (2010). Computational modeling
of these preferences can, therefore, help develop decision-aid tools that incorporate stakeholders’
moral values, e.g., in applications like autonomous vehicles or biomedical situations. Unsurpris-
ingly, the standards of expected elicitation accuracy in these domains are quite high, since inac-
curate prediction of moral judgments can significantly harm the people using or affected by the
1A note on terminology: what we call moral preferences can also be described as judgments/orderings over available
actions in moral dilemmas. This characterization is different than decision theory literature, which defines preference
orderings over outcomes rather than actions Arrow et al. (1996). Yet, we use the term preferences to be consistent with
CS preference elicitation literature on modeling decision processes in pairwise comparison settings.
3

--- Page 4 ---

decision-aid tool. For these reasons, greater attention to elicitation performance is required in
moral decision-making settings.
Yet, a crucial problem in eliciting moral preferences is that they can be unstable, i.e., the partic-
ipant’s choices for the first few presented moral dilemmas might appear inconsistent with each
other Crockett (2016). The participant can also be indecisive and provide “noisy” judgments
to moral dilemmas (e.g., there may be variability in their choices for similar scenarios), further
complicating the elicitation process Rehren and Sinnott-Armstrong (2022). Research on moral
psychology also lacks consensus on the structure of cognitive processes that incorporate moral
preferences within our judgments Ugazio et al. (2022). Limited understanding of moral decision-
making structures makes it difficult to model them computationally. All these properties taken
together make moral preference elicitation a complex task and call into question the validity of
active learning as a reliable elicitation methodology.
The use of active learning for preference elicitation often presupposes that the context in question
does not suffer from the above issues. Preference stability, limited variability in responses, and
availability of a hypothesis class that captures the underlying utility u are common assumptions
Dragone et al. (2018). An obvious question that then arises is whether active learning still leads to
efficient moral preference elicitation when these assumptions are violated. Research from moral psychol-
ogy suggests that these assumptions may specifically not hold for moral preferences. Hence, the
efficacy of active learning for moral preference elicitation needs further examination.
1.1
Our Contributions
In this paper, we investigate whether active learning can be effective for moral preference elici-
tation, based on simulations designed to replicate the above challenges with moral preferences.
Our simulations test two popular active learning paradigms, version-space-based active learning
and Bayesian active learning (Section 2). Inspired by recent human subject research on proper-
ties of moral decision-making (Section 3), we consider the following challenges: (a) preference
instability, (b) model misspecification, and (c) noisy responses. In all settings, we compare
active-learning-based approaches against a standard approach that presents agents with random
pairwise comparisons. We observe the following:
Preference instability.
Our simulations here evaluate elicitation performance when the agent’s
moral preference model stabilizes only after responding to a certain number of initial compar-
isons (Section 4.1). Specific scenarios we consider include: (1) the agent, after a few comparisons,
simplifies their moral preference to reduce the decision-making effort, (2) the agent makes their
preference more complex to incorporate additional information, and (3) the agent changes their
preference entirely to reflect significant updates to their moral values. We observe that, in all three
cases, when the number of features is small, the Bayesian active learning approach recovers well
from instability and achieves higher accuracy than the random query baseline within a small num-
ber of comparisons after a preference change. However, in cases of drastic preference changes and
a large number of features, both active learning approaches have similar or worse performance
than the random query baseline due to their dependence on previous comparisons. The key take-
away here is that the accuracy and efficiency of active learning depend on the expected scale of preference
instability (as captured by the kind of preference change) and the complexity of the decision-making context
(as captured by the number of features).
4

--- Page 5 ---

Model misspecification.
Our model misspecification simulation evaluates preference elicitation
performance when the agent’s moral decision-making model and the model class used by the
elicitation framework are different (Section 4.2). For instance, suppose the agent uses a shallow
decision tree to encode preferences, but the preference elicitation framework uses the class of lin-
ear models. Here, active learning at best converges to the best hypothesis in the linear class but has
a relatively high predictive error–as observed in our simulations. Along with agents that use tree-
based models, we simulate other scenarios of model misspecification, such as scenarios where the
agent uses feature interactions but the elicitation model doesn’t, and scenarios where the agent
and the elicitation model use different feature sets. When the extent of model misspecification is
large, we observe that active learning approaches and random query baseline have similar perfor-
mance. The key takeaway here is that appropriate modeling of the agent’s moral decision-making process is
necessary for active learning to improve the elicitation efficiency of the framework.
Noisy responses.
We also consider the setting where the agent’s responses are stochastic and
simulate two kinds of stochasticity: (a) response noise: when stochasticity in the agent’s response to
a pairwise comparison depends on the difference between utility assigned to each item in the pair
(i.e., higher variability when utilities are close) and (b) preference noise: when the agent’s preference
model is sampled from a certain distribution. For response noise, we observe that the Bayesian
active learning approach is still more efficient than the random query baseline despite noise. For
preference noise, active learning is more efficient than random query baseline only when noise is
small (e.g., when noise magnitude is small relative to the range of model parameter values). The
key takeaway here is that one needs to consider the source and impact of variability in agent responses to
assess the effectiveness of active-learning-based elicitation.
Overall, our simulations shed light on the performance of active learning for simulated moral
preference elicitation tasks. We find that active learning can improve elicitation efficiency in cer-
tain settings (e.g., small-scale noise) but also reduce elicitation efficiency in other settings (e.g.,
large-scale preference instability). Based on these results, we emphasize the need to understand
the nuances associated with the moral decision-making context in question before deploying ac-
tive learning-based elicitation frameworks. Additionally, our findings can inform future human-
subject studies aimed at understanding the extent to which these assumptions are violated in
common moral preference elicitation tasks.
1.2
Related Work
Preference elicitation methods are employed in multiple domains to create user-centered services,
e.g. to create recommendation systems Priyogi (2019), to understand consumer behaviour Ben-
Akiva et al. (2019), and for patient-centered decision-making in healthcare Weernink et al. (2014).
Research on preference elicitation similarly spans multiple disciplines, including computer science
Chen and Pu (2004), economics Beshears et al. (2008), and psychology Slovic (2020). Machine-
aided elicitation has further improved learning efficiency by helping process available agent data
and/or the choices they make in real and hypothetical scenarios Soekhai et al. (2019). As men-
tioned earlier, similar efforts have been made in moral domains, with several applications em-
ploying elicitation frameworks to model moral preferences Awad et al. (2018); Srivastava et al.
(2019); Loreggia et al. (2019); Balakrishnan et al. (2019); Sinnott-Armstrong et al. (2021); Johnston
et al. (2023). For a general survey of moral preference elicitation methods, we recommend Fef-
fer et al. (2023). In our work, we focus on methods that query an agent to choose between two
5

--- Page 6 ---

given cases and use their responses to learn their preferences Ben-Akiva et al. (2019). While pair-
wise comparisons are a popular elicitation technique, there are alternative approaches as well,
e.g., asking agents to report their preference strength Toubia et al. (2003), rank choices Ali and
Ronaldson (2012), participate in bidding processes Conen and Sandholm (2001), or describe the
motivations for their choices Liscio et al. (2023, 2024).
Active learning can be used to either learn the agent’s utility model or to successively present
them with better recommendations Houlsby et al. (2011); Dragone et al. (2018). For the former
setting learning the utility model, Huang and Luo (2016) propose active learning methods to learn
marketplace consumer preferences and Srivastava et al. (2019) elicit fairness preferences using
active-learning-based surveys. For the latter setting of generating personalized recommendations,
Elahi et al. (2014) and Yang et al. (2021) discuss active learning strategies to streamline data col-
lection for recommendation systems. Johnston et al. (2023) use uncertainty-based active learning
methods proposed by Vayanos et al. (2020) to model healthcare resource allocation preferences of
survey participants. Our work focuses on learning the utility model since the eventual goal is to
use the learned utility and preferences for downstream applications.
Most preference elicitation studies focus on preferences involving self-benefits, e.g., to create rec-
ommendation systems or better-personalized services. As mentioned earlier, moral preferences go
beyond self-interest and explain people’s normative impartial judgments. For instance, Bicchieri
and Chavez (2010) show the insufficiency of monetary preferences in explaining people’s fairness
perceptions. Capraro and Rand (2018) discuss how social preference models can be incompati-
ble with people’s choices of equitable actions. Other experimental analyses from psychology (see
Capraro and Perc (2021) for a review) provide further evidence of contrasts between moral and
material preferences.
Beyond our work, certain recent papers examine the limitations of active learning in different
contexts. Margatina and Aletras (2023) and Kottke et al. (2019) discuss the dependence of active
learning’s performance on common (but potentially unrealistic) assumptions, e.g. representative
training data and equal labeling costs across cases. Active learning can also fail to outperform ran-
dom query baselines when faced with distribution shifts Snijders et al. (2023) or outliers Karam-
cheti et al. (2021). Data collected using active learning is implicitly tied to the learning model
and can lead to generalization issues Lowell et al. (2019). Our work adds to this line of research,
specifically questioning the applicability of active learning to moral preference elicitation.
2
Algorithms for Preference Elicitation
The basic structure of the elicitation procedure is described in Algorithm 1. At time-step t, the
agent is presented with a sampled comparison (xt, x′
t) and their response is recorded. Then, the
algorithm finds the hypothesis ht from class H which best fits the labeled comparisons recorded
till time t.
The sampling step of Algorithm 1 (Step 3) can be executed either by randomly sampling a pair
of input cases or by using active learning, whereby the chosen pair depends on the comparisons
presented so far and the hypothesis class H. We will use RANDOM-PE to refer to the instance of
Algorithm 1 that uses random sampling. When using active learning to sample comparisons, mul-
tiple methods from prior works can be employed and we outline two popular approaches below.
Longer mathematical descriptions and use cases of these methods are provided in Appendix A.
6

--- Page 7 ---

Algorithm 1 Online preference elicitation
Input: Functions sample(·), R(·, ·), and fit(·, ·), N, class H
1: S ←∅
2: for t ∈{1, . . . , N} do
3:
xt, x′
t ←sample(S) {sample new comparison}
4:
rt ←R(xt, x′
t) {Get agent’s response}
5:
S ←S ∪{(xt, x′
t, rt)}
6:
ht ←fit(S, H) {Learn hypothesis using dataset S}
7: return hN
Version-Space-based Active Learning.
Given a kernel-SVM decision boundary learned using
available labeled data, the informativeness of any new query can be approximated using the
distance of the query from the decision boundary and this heuristic can be used to generate an
informative next query Tong and Koller (2001). To implement this approach, we learn an SVM
hypothesis f that best fits ((xi, x′
i))t
i=1 to labels (ri)t
i=1 and find a comparison that is closest to f’s
decision boundary. We will call this approach ACTIVE-VS-PE.
Bayesian Active Learning.
The Bayesian Active Learning with Disagreement (BALD) algorithm
represents preferences using a Gaussian process with a specified kernel and chooses the next query
to be the one that maximizes the mutual information between model predictions and model pos-
terior Houlsby et al. (2011). Implementation of this approach for Algorithm 1 requires learning a
representation of the posterior corresponding to the labeled dataset ((xi, x′
i, ri))t
i=1 and then find-
ing the pairwise comparison with high mutual information. We will call this approach ACTIVE-
BAYES-PE. Note that the use of learned posterior is limited to the sampling step and can be inde-
pendent of the learning step.
The final step of Algorithm 1 (Step 6) uses a pre-specified function fit(·, ·) to learn a hypothesis
ht from H that “best” simulates responses (ri)t
i=1 using comparisons ((xi, x′
i))t
i=1. For instance,
if H is the class of linear functions, then fit(·, ·) can implement an SVM, logistic regression, or
any other linear classification training procedure (with appropriate regularization). Alternately,
to rank cases based on the agent’s responses (with H denoting the set of all rankings), the popular
Bradley-Terry approach can be implemented within fit(·, ·) Bradley (1984). The choice of H here
depends on prior beliefs about the agent’s preference model. However, a mismatch between the
agent’s preference model and H can impact the effectiveness of the framework (see Section 4.2).
3
Challenges to Modeling Moral Preferences
Inspired by prior research from moral psychology, we highlight three obstacles to computationally
modeling an agent’s moral preferences. These obstacles are (a) change in preference after making
a certain number of decisions, (b) the agent’s model not being included in H, and (c) noise in
the agent’s responses. We describe these challenges here, specifically focusing on prior empirical
evidence for them from human subject research in the pairwise comparison setting.
Preference instability.
Empirical studies in psychology provide extensive evidence that agent’s
preferences in unfamiliar contexts are developed as they make decisions in those contexts Hoeffler
and Ariely (1999); Ariely and Zakay (2001); Warren et al. (2011); Dhar et al. (1999). In these settings,
7

--- Page 8 ---

the first few choices made by an agent can be unstable (i.e., their preferences can change after
making some decisions) and may not reflect their eventual preferences for future decisions. Moral
preferences can have similar instability and can be shaped by an agent’s ongoing experience with
the decision-making context Crockett (2016); Rehren and Sinnott-Armstrong (2022); Helzer et al.
(2017); Curry et al. (2019).
In the context of pairwise comparisons, data from Boestler et al. (2024) provides evidence of this
phenomenon in the kidney allocation setting. In their study, participants are asked to participate
in 10 sessions (one per day) and presented with 60 pairwise comparisons in each session. Session-
specific analysis shows that, for many participants, there is significant variation in their weight
distribution over the patient features across different sessions. In other words, for many partici-
pants, their underlying utility functions change from session to session. This kind of preference
change can significantly impair the ability to computationally model moral preferences.
Note that we consider the instability of moral preferences over available actions and not prefer-
ences over moral values (e.g., one’s value preference could be to prioritize equality in resource
allocation over efficiency). Moral values do inform moral judgments and the preferences an agent
has over available actions. But prior work has argued that while values are generally stable, agents
can still be unstable in applying those values to make moral judgments – this is referred to as the
“value-action gap” Gould et al. (2023). In our setting, since we only observe the agent’s moral
judgments, we mainly focus on the challenge posed by the observed instability of preferences
expressed through these judgments.
Model misspecification.
Another challenge in the computational modeling of moral preferences
is model misspecification, i.e., making incorrect/misrepresentative assumptions regarding the
structure of the agent’s decision-making process. A popular modeling assumption is the additive
independence model, where we assume the utility the agent assigns to any input can be represented
as a sum of the utilities assigned to individual input features Chen and Pu (2004) (e.g., linear util-
ity satisfies this assumption). Another common modeling assumption is the complete information
assumption, i.e., all the information explicitly used by the agent to make their decision is available
to the elicitation framework. Assumptions of this kind are common in active learning-based elici-
tation as they reduce the complexity of query generation Yang et al. (2021); Johnston et al. (2023).
They also affect the choice of H in Algorithm 1, e.g., if we assume additive independence and com-
plete information, then setting H to be the linear class can help learn explainable representations
of the agent’s preferences.
However, in many situations, these assumptions do not reflect the agent’s decision-making pro-
cess Pine et al. (2009); Gonzalez Sepulveda et al. (2021). Cognitive processes underlying moral
decision-making are not clearly understood Ugazio et al. (2022) and can be more complex than
a linear combination of available features Hofmann et al. (2008). Both empirical and theoretical
analyses of moral judgments highlight this complexity. Cohen and Ahn (2016) fit multiple kinds
of linear and nonlinear models over people’s responses in moral dilemmas and find that mod-
els from the exponential function family often provide the best fit. Kagan (1988) theoretically
questions both the additive and independence assumption (in an article appropriately titled “The
Additive Fallacy”), explaining through multiple contrastive examples that (a) moral status of an
act cannot always be determined by the sum of weights of individual features, and (b) weight
assigned to each feature can depend on the weight assigned to other features (i.e., feature inter-
actions). As such, non-linearity and dependence across various features can be expected in moral
decision-making processes.
8

--- Page 9 ---

Noisy responses.
Stochasticity in agent’s choices, (specifically, changes in their responses to
similar scenarios at different times) has been noted in various domains Marley and Regenwet-
ter (2016); Becker et al. (1963). The same is true for moral decision-making domains, where re-
sponse variability can be a result of ongoing deliberation, increased decision “difficulty”, and/or
increased complexity of the decision context Sivill (2019). Boestler et al. (2024) provide concrete
evidence of this phenomenon. In their kidney allocation study, participants take part in multi-
ple sessions and six pairwise comparisons are repeated in each session. Participants’ responses
to the repeated comparisons provide insight into response variability, quantified by the fraction
of times a participant’s choice to a repeated scenario differed from their majority choice for this
scenario. Boestler et al. (2024) observe significant response variability for certain repeated com-
parisons (in the range of 10-18%). Additionally, the results of Boestler et al. (2024) suggest that
response variability is larger when the pairwise comparison is perceived as being more “difficult”
by the participant, implying amplified stochasticity for difficult moral dilemmas.
All of these properties pose significant obstacles to the computational modeling of moral pref-
erences. As we see in the following sections, the impact of these challenges can potentially be
amplified by the use of active learning.
4
Testing the Efficacy of Active Learning
With the above challenges in mind, we next compare the performance of active learning for pref-
erence elicitation against the random baseline over simulations of these challenges.
Simulation setup.
We primarily simulate agents that use linear utility functions, i.e., u(x) =
w⊤x, for any x ∈X, given weights w ∈Rd. The assumption of linear utility is quite prevalent in
the preference elicitation literature (e.g., Noothigattu et al. (2018), McElfresh et al. (2021), Johnston
et al. (2023)). In Section 4.2, we will also question this assumption and simulate agents that use
tree-based models and linear models with feature interactions. To simulate an agent with linear
utility, we sample weights w from the uniform distribution Unif([−1, 1]d). We run Algorithm 1
for each simulated agent, presenting them with N pairwise comparisons (ranging from 5 to 50).
H is set to be the class of linear SVM classifiers over feature differences (with fit(·) performing
SVM training). Hence, each ht will contain the learned SVM weights, say ˆwht. We evaluate per-
formance using two metrics: (i) accuracy - for a held-out collection of 1000 comparisons, measure
the fraction of comparisons for which the response using weights ˆwhN matches that of the agent
- and (ii) normalized distance - measure the L2-distance between ˆwhN and w after normalization.
For each setup, we report the mean and standard deviation of these metrics across 50 simulated
agents. In the main body of the paper, we will primarily discuss the accuracy metric. Results with
respect to distance are similar but deferred to Appendix C. The number of features d is varied
from {3, . . . , 15} and each feature has range {1, . . . , 10} (unless specified otherwise). ACTIVE-VS-
PE and ACTIVE-BAYES-PE will use a linear kernel function κ. Other implementation details are
presented in Appendix B.
4.1
Preference Instability
The first challenge we discuss in Section 3 is preference instability, i.e., the agent’s underlying
preferences can change after making some decisions. Since the next query suggested by active
learning depends on the agent’s responses to comparisons presented so far, we simulate scenarios
9

--- Page 10 ---

Figure 2: Performance for preference-change scenarios from Section 4.1. ACTIVE-BAYES-PE often
performs better than RANDOM-PE post-tchange when d=5. However, in many cases (e.g., d=10,
tchange=20, 30), both active learning algorithms have similar or worse performance than RANDOM-
PE.
where an agent’s preferences undergo changes to assess the impact of preference instability on
active learning algorithms.
We assume that the agent’s utility function is linear. Suppose that the agent changes their pref-
erences once, at timestep tchange ∈[N]. Let wpre ∈Rd denote the agent’s weight vector for all
timesteps t < tchange and wpost ∈Rd denote the agent’s weight vector for all timesteps t ≥tchange.
We simulate the following kinds of preference changes.
• Downscale-ordered. Agent changes their preference utility function to only use the feature
to which they assigned the highest weight previously. For this agent, we sample pre-change
preference wpre ∼Unif([−1, 1]d) and set I = arg maxi |wpre
i
|. Then, for post-change prefer-
ence, wpost
I
= wpre
I
and wpost
i
= 0 for all i ∈[d] \ {I}.
• Downscale-random. Agent changes their utility function to again use only one feature, but
the feature is randomly selected. For this agent, we sample pre-change preference wpre ∼
Unif([−1, 1]d) and set I is chosen randomly from set [d]. Then, for post-change preference,
wpost
I
= wpre
I
and wpost
i
= 0 for all i ∈[d] \ {I}.
• Upscale-ordered: Agent changes preference utility function from using just one feature to
all features, with features in wpost having lower relative weight than the non-zero weight in
10

--- Page 11 ---

wpre. For this agent, sample wpost ∼Unif([−1, 1]d) and I = arg maxi |wpost
i
|. Then, wpre
I
=
wpost
I
and wpre
i
= 0 for all i∈[d] \ {I}.
• Random-switch. Agent changes to a random new preference after tchange. Here, we sample
both weights vectors wpre, wpost ∼Unif[−1, 1]d, independently.
Downscale-ordered and Downscale-random model the settings where an agent changes their
preference to reduce decision-making effort Shah and Oppenheimer (2008). In certain cases, the
agent can choose only to use the feature that was most important to them pre-tchange, which is
modeled by Downscale-ordered. Upscale-ordered is a symmetric scenario where the agent in-
stead incorporates additional features in their preference. Finally, Random-switch models agents
who make more drastic changes to their preference, e.g. following an entirely different set of moral
norms. Appendix C.1 models multiple other scenarios as well, e.g., agent downscaling/upscaling
to or from random features (instead of highest weighted feature) and downscaling/upscaling to
or from more than one feature. For all scenarios, we compare the accuracy achieved by ACTIVE-
VS-PE and ACTIVE-BAYES-PE vs. RANDOM-PE, varying the number of features, number of com-
parisons, and tchange.
Results.
The results of our simulations are presented in Figure 2. As expected, ACTIVE-VS-PE
and ACTIVE-BAYES-PE always achieve higher accuracy than RANDOM-PE prior to tchange. Post-
tchange performance shows how well each algorithm recovers from preference change.
Let us first look at the Downscale-ordered setting (plots on the top-left side of Figure 2). In this
case, when the preference change occurs early (i.e., tchange = 10), ACTIVE-BAYES-PE recovers
quite fast from the preference change: the accuracy of ACTIVE-BAYES-PE becomes higher than
that of RANDOM-PE within 10 timesteps (on average) post-tchange when d = 5. In comparison,
ACTIVE-VS-PE takes longer to recover and exceeds RANDOM-PE in accuracy. For larger tchange,
both active learning approaches seem to recover slower and incompletely. When d = 10 and
tchange is 20 or 30, we further observe that ACTIVE-BAYES-PE and ACTIVE-VS-PE have similar or
even lower accuracy than RANDOM-PE for all timesteps post-tchange. This also implies reduced
efficiency of active learning in settings with high feature complexity; for any desired level of accu-
racy, active learning approaches take a similar or larger number of comparisons than the random
query baseline to achieve that accuracy level. In the case of Downscale-random setting, the per-
formance of active learning algorithms, relative to RANDOM-PE, follows similar patterns – when
d = 5 and tchange is small, ACTIVE-BAYES-PE recovers well compared to other algorithms, but
this recovery is much slower for d = 10. The drop in accuracy around timestep tchange is also
larger in magnitude for Downscale-random compared to Downscale-ordered; this is expected
since there is relatively more consistency between pre-change and post-change preferences in the
Downscale-ordered setting.
Similar trends are observed for the Upscale-Ordered and Random-switch plots in Figure 2. Ac-
tive learning approaches have the worst recovery in the Random-switch setting where, due to
the drastic change in the agent’s preferences, both ACTIVE-BAYES-PE and ACTIVE-VS-PE have
similar or worse performance than the RANDOM-PE post tchange when d = 10. On the positive
side, when d = 5, ACTIVE-BAYES-PE does achieve higher accuracy than RANDOM-PE within 20
timesteps post-tchange on average.
Overall, Bayesian active learning approaches can efficiently elicit preferences while handling pref-
erence changes when the number of features d is small. However, these approaches fail to provide
similarly improved performance as feature complexity and preference change timestep increases.
11

--- Page 12 ---

These results highlight the importance of knowing the nature and scale of preference instability
before deploying active learning. While active learning will eventually recover after a larger num-
ber of timesteps beyond 50, we see that in the timesteps following tchange, it can perform even
worse than the random baseline due to its dependence on the agent’s previous responses. Con-
sidering that active learning is usually employed when one has to be economical with the number
of presented comparisons (due to time and/or cost constraints), not being able to rely on a certain
number of initial responses can significantly affect the accuracy of the learned preferences and fail
to improve, or even harm, the efficiency of the framework.
4.2
Model misspecification
The second challenge we discussed in Section 3 is model misspecification, specifically question-
ing the additive independence and complete information assumptions for the agent’s moral decision-
making process. In this section, we evaluate active learning when additive independence and
complete information assumptions are not satisfied. Setting H to be the linear class, we simulate
the following scenarios.
• Agent uses tree-based utility. We simulate agents that use shallow binary decision trees to
assign utility. Tree-based models reflect decisions made using if-then rules; e.g., in an organ
allocation setting, an agent might assign a higher utility to a patient if their age is >50 but
can be indifferent to the exact age number. To maintain parity between capacity of a tree
model and models in H, we simulate agents with tree models of depth ⌊log d⌋, where d is
the number of features. We simulate this scenario with binary and non-binary features.
• Agent uses second-order interaction terms. Even with a linear utility model, the agent’s
utility function could use interactions between different features. Interaction terms account
for scenarios where the importance an agent might assign to any feature is correlated with
the value of another feature. For example, in the organ allocation setting, an agent might as-
sign a higher weight to a patient’s number of dependents if the patient is young, implying an
interaction between the age and number of dependents variables. We simulate this scenario
by measuring performance across a varying number of features d and a varying number of
second-order interactions.
• Missing features. Finally, we consider the scenario where the agent uses information un-
available to the elicitation framework. We simulate this scenario by allowing the agent to
use a larger feature set than that available for elicitation. Our simulations assess perfor-
mance across a varying number of total and missing features.
Results. The results for these simulations are presented in Figure 3. When the agent uses tree-
based preference, ACTIVE-BAYES-PE has marginally better accuracy than the RANDOM-PE after
30 comparisons when d is large. For small d, both active learning approaches tend to have similar
or worse accuracy than the random baseline. The impact of model misspecification also depends
on the input domain – overall accuracy is lower for non-binary features.
When the agent uses interaction terms, Figure 3 shows that accuracy decreases as the number
of interaction terms increases. However, when the number of interaction terms is much smaller
than d, ACTIVE-BAYES-PE and ACTIVE-VS-PE can achieve higher accuracy than RANDOM-PE
after 30 comparisons. Finally, in the case of missing features, the larger the number of missing
features (relative to d), the lower the accuracy, and the smaller the gap between ACTIVE-BAYES-
PE, ACTIVE-VS-PE, and RANDOM-PE after 30 comparisons. Missing information reduces the
12

--- Page 13 ---

Figure 3: Performance for model misspecfication scenarios from Section 4.2. Active learning is
more effective when the extent of model misspecification is small in scale.
capacity of the framework to capture the agent’s decision-making process, leading to an accuracy
drop.
For these scenarios, we see that the larger the scale of disparity between the agent’s utility function
and H, the worse the performance of active learning as compared to the random query baseline.
Active learning might still converge to the best hypothesis in H (see accuracy vs. timestep results
in Appendix C.2); however, the above results show that disparity between functions in H and
the agent’s utility affects active learning’s ability in generating informative queries and leads to a
reduction in accuracy of learned preferences.
4.3
Noisy Responses
The final challenge we highlighted in Section 3 is stochasticity or variability in agent’s responses
to moral dilemmas. Two ways in which this stochasticity has been modeled in prior literature are
(a) response noise: noise that arises and affects the agent’s response after the agent has computed
utility for the presented cases, and (b) preference noise: noise that arises due to variability in the
13

--- Page 14 ---

Figure 4: Performance for the noise models from Section 4.3. ACTIVE-BAYES-PE performs better
than the random query baseline even with response noise. However, it fails to provide a similar
improvement in most scenarios of preference noise.
agent’s underlying utility function Bhatia and Loomes (2017); Marley and Regenwetter (2016).
Suppose the agent uses linear utility, i.e., u(x) = w⊤x, for some w∈Rd. Then, the above noise
models can simulated as follows.
• Response noise model. This model induces noise ε ∼N (0, σ2) after utility is computed.
Assuming an additive noise model, the impact of this noise on the agent’s response R can
be interpreted as changing it to R(x, x′) = 1[u(x) −u(x′) + ε > 0]. Our simulations evaluate
performance for varying σ ∈R.
• Preference noise model. This model assumes noise in the utility generation process itself.
We simulate this setting as follows: Suppose that whenever presented with a pairwise com-
parison, the agent first samples w ∼N (w⋆, σ2I/d), and then uses the sampled w to com-
pute utilities. Here, w⋆∈Rd represents summary feature weights assigned by the agent and
σ ∈R is the noise parameter varied in our simulations.
Results. The results for this simulation are presented in Figure 4. As expected, increasing σ
leads to a decrease in accuracy of all algorithms. However, in the case of response noise, ACTIVE-
BAYES-PE has higher accuracy than the RANDOM-PE baseline even for high values of σ. Accuracy
vs number of comparisons plot for σ = 2 further shows that ACTIVE-BAYES-PE starts achieving
higher accuracy than RANDOM-PE with as few as 20 comparisons. Performance of ACTIVE-VS-
PE, on the other hand, is relatively better than RANDOM-PE for small σ values but becomes similar
to that of RANDOM-PE for large σ. Hence, in this case, active learning (especially, ACTIVE-BAYES-
PE) can be relatively more accurate at preference elicitation despite noise.
In the preference noise setting, both active learning approaches have similar performance as the
RANDOM baseline for almost all non-zero σ values. Variation with respect to σ and number of
comparisons shows that noise in preference weights significantly affects the ability of all algo-
rithms to learn the underlying preferences when σ>1. Hence, here active learning fails to provide
any performance improvement in comparison to the random query generation baseline.
14

--- Page 15 ---

5
Discussion, Limitations, and Future Work
Through the presented simulations, we highlight how potential issues associated with moral pref-
erences, such as preference instability, response variability, or modeling errors, can impact the
efficacy of active-learning-based preference elicitation. In all simulated scenarios, we compare the
performance of active learning-based preference elicitation against the baseline method of using
random queries at each time step. Overall, there are positive scenarios where active learning still
performs better than the random query baseline – e.g., when noise affects utility but not the under-
lying preferences, or in the case of small-scale preference instability in initial iterations. Then, there
are neutral scenarios where the simulated challenge impacts the efficiency of all algorithms simi-
larly and the performance of active learning and the random baseline are comparable – e.g., for
large-scale modeling errors or when the agent’s underlying preferences are noisy. In these cases,
using active learning does not provide any added benefit but it also does not cause any harm to
the elicitation framework. Finally, there are negative scenarios, where using active learning is less
effective than the random baseline – e.g., when the number of features is large and the agent’s
preference changes after they have responded to a large number of comparisons. Here, since ac-
tive learning uses the agent’s previous responses to construct the next query, it takes longer to
recover from preference changes.
Different real-world challenges have different effects on active learning for preference elicitation.
Deploying these frameworks without prior understanding of the agent’s decision-making for the
given context can lead to inaccurate representations of their preferences. While using a small num-
ber of queries will almost always provide only an approximate representation of the underlying
preferences, our simulations call attention to the sources of inaccuracy that were unappreciated in
previous works and could lead to incorrect interpretations of results if not considered in practice.
In the paragraphs below, we highlight other characteristics of our assessment as well as future
work on this topic.
Algorithmic solutions.
One response to the challenges we simulate is that many of them can be
addressed algorithmically if they are known in advance. If an agent’s preferences are known to
be unstable for initial comparisons, then one can, say, modify the elicitation approach to disregard
a certain number of initial comparisons or assign sample weights to each case that are inversely
proportional to the duration since the case was observed by the agent. This way, active learning
can construct queries that are primarily based on the most recent agent responses. To account for
feature interactions, the models in H can allow interactions by default and use regularization to
rule out scenarios where interactions are not used. Prior work on active learning methods that are
robust to noise or distribution shifts can be potentially adapted to make elicitation more resilient
to noise or modeling errors Angluin and Laird (1988); Zhao et al. (2021). In simulations, Bayesian
approaches often appear more robust to certain challenges, e.g., small-scale instability. Hence,
one approach is to use ACTIVE-BAYES-PE with an expanded hypothesis class H (e.g., combining
linear and tree classes) to counter issues of model misspecification. The main challenge here is cre-
ating an efficient query-selection algorithm over an expanded H while being robust to instability
and noise, and can be explored as part of future work. Most of these modifications, however, re-
quire prior knowledge of the nature of the challenge associated with the agent’s decision-making
process. Indeed, the primary goal of our analysis is to highlight that certain assumptions made
when using active learning incorrectly rule out these challenges. Knowing that these assumptions
might be violated can help practitioners develop modifications that might be better suited for the
15

--- Page 16 ---

given context. Also, some active learning algorithms may be generally more robust to violated
assumptions than others.
Sensitivity of moral preferences.
As discussed, moral preferences can be different from generic
preferences for self-benefit and, hence, assuming moral preferences to have a similar structure
as other preferences will hurt the accuracy of the elicitation framework. Based on prior insights
from the literature on moral preferences, our work discusses specific mechanisms via which these
inaccuracies can occur. With the highlighted challenges and considering the emergent nature of
moral psychology research, the task of eliciting moral preferences can be tricky. Nevertheless,
building elicitation methods specifically for moral preferences is a worthwhile direction for future
research, given their role in creating ethical AI tools. At the same time, moral preference elicitation
is just one (albeit complex) part of ethical AI development. Mechanisms to incorporate learned
moral preferences within AI systems involve additional work and should be similarly subjected
to technical analyses of feasibility under various real-world challenges.
On utility functions.
Our framework employs utility functions to model people’s preferences
over actions in moral dilemmas, as is standard practice in this literature. Despite the overlap in
naming conventions, it is important to clarify that modeling moral preferences using utility func-
tions does not presuppose a reliance on utilitarian or consequentialist moral theories (as long as
consequentialism isn’t used generically to cover all possible theories Portmore (2022)). The justi-
fications people have for considering features that contribute to their utility function do not have
to draw on consequentialist principles, and the features people consider may not impact future
consequences directly, such as when people think patients’ past criminal behavior is important
for determining who should receive an available kidney. Adherence to many different moral the-
ories (including non-consequentialist theories) can be modeled using utility functions, and our
analysis aims to call attention to challenges that can arise when using active learning to obtain
accurate representations of various utility functions. Nevertheless, future work is needed to as-
sess the effectiveness and challenges of using active learning to predict moral judgments under
other modeling frameworks or conditions, e.g., when using explicit moral constraints Black (2020),
harm-based utilities Beckers et al. (2022), or modified utility-based frameworks that explicitly ac-
count for deontological values Lazar (2017).
On non-moral preferences.
Issues of instability, noise, or model misspecification can arise with
non-moral preferences as well. Yet, we focus on moral preferences because the specific challenges
we simulate are inspired by the literature on moral philosophy and psychology. AI applications
that would rely on moral preference elicitation often involve high stakes and errors in preference
elicitation can cause undue harm to users and impacted individuals (e.g., in autonomous vehicles
and kidney allocation settings), requiring high levels of elicitation accuracy and reliability.
Other analyses/baselines.
Future assessments of active learning can also simulate violations of
multiple assumptions; e.g., the presence of both preference instability and model errors. These
combinations can be reflective of more complex decision-making settings. Additionally, in appli-
cations where data from past agents is available, other baselines (beyond simple random query
baseline) can be considered. For instance, one could create elicitation using a curated set of queries
that were informative of the preferences of past agents. All or random subsets of this curated set
can be used to elicit preferences. Evaluation of active learning against such baselines can provide
insight into whether it is better than methods that use prior information.
16

--- Page 17 ---

Limitations of our analysis.
Our simulations demonstrate the need for improved modeling of
human moral preferences and developing active learning approaches that are more robust to the
simulated challenges. Along with this direction for future work, additional analyses can be con-
ducted to further discover other failure points of quantitative preference elicitation frameworks.
Note that all of our analysis simulates agents with linear or tree-based utility functions. Human
moral preferences can be more complex and analyzing active learning performance through real-
world data can provide more robust results. In particular, this will require human-subject studies
where participants respond to comparisons generated using active learning and random compar-
isons. As expected, collecting this data will be expensive and time-consuming. In that regard, our
simulation provides a starting point on the kind of data that can be gathered using active learning
and raises challenges that need to be accounted for when analyzing this data.
6
Conclusion
The results of our simulations highlight the challenges associated with extracting accurate repre-
sentations of agents’ moral preferences while using as few queries as possible. In cases of large-
scale instability or noise in agent preferences or responses, active learning has similar or worse
performance than the random baseline. The assumptions made by the elicitation framework re-
garding the agent’s moral preferences also impact the effectiveness of active learning. The use
of active learning for moral preference elicitation therefore requires careful evaluation of mod-
elling assumptions and the scale of expected variability in agent preferences and responses for the
relevant context. If large-scale instability, noise, and/or violation of modeling assumptions are
expected, then appropriate alternatives or modifications to active learning should be considered
to counter such issues.
Acknowledgements
We are grateful for financial support from OpenAI & Duke.
17

--- Page 18 ---

References
S. Ali and S. Ronaldson. Ordinal preference elicitation methods in health economics and health
services research: using discrete choice experiments and ranking methods. British medical bul-
letin, 103(1):21–44, 2012.
D. Angluin and P. Laird. Learning from noisy examples. Machine learning, 2:343–370, 1988.
D. Ariely and D. Zakay. A timely account of the role of duration in decision making. Acta psycho-
logica, 108(2):187–207, 2001.
K. J. Arrow, E. Colombatto, M. Perlman, and C. Schmidt. The Rational Foundation of Economic
Behaviour. Macmillan Press, 1996.
E. Awad, S. Dsouza, R. Kim, J. Schulz, J. Henrich, A. Shariff, J.-F. Bonnefon, and I. Rahwan. The
moral machine experiment. Nature, 563(7729):59–64, 2018.
A. Balakrishnan, D. Bouneffouf, N. Mattei, and F. Rossi. Using multi-armed bandits to learn ethical
priorities for online ai systems. IBM Journal of Research and Development, 63(4/5):1–1, 2019.
G. M. Becker, M. H. DeGroot, and J. Marschak. Stochastic models of choice behavior. Behavioral
science, 8(1):41–55, 1963.
S. Beckers, H. Chockler, and J. Halpern. A causal analysis of harm. Advances in Neural Information
Processing Systems, 35:2365–2376, 2022.
M. Ben-Akiva, D. McFadden, and K. Train. Foundations of stated preference elicitation: Consumer
behavior and choice-based conjoint analysis. Foundations and Trends in Econometrics, 2019.
J. Beshears, J. J. Choi, D. Laibson, and B. C. Madrian. How are preferences revealed? Journal of
public economics, 2008.
S. Bhatia and G. Loomes. Noisy preferences in risky choice: A cautionary note. Psychological
review, 124(5):678, 2017.
C. Bicchieri and A. Chavez. Behaving as expected: Public information and fairness norms. Journal
of Behavioral Decision Making, 23(2):161–178, 2010.
D. Black. Absolute prohibitions under risk. Philosopher’s Imprint, 20(20), 2020.
K. Boestler, V. Keswani, J. Schaich Borg, H. Heidari, V. Conitzer, and W. Sinnott-Armstrong. On
the stability of moral preferences: A problem with computational elicitation methods. To appear
in AIES 2024, 2024.
R. A. Bradley. 14 paired comparisons: Some basic procedures and examples. Handbook of statistics,
4:299–326, 1984.
V. Capraro and M. Perc. Mathematical foundations of moral preferences. Journal of the Royal Society
interface, 18(175):20200880, 2021.
V. Capraro and D. G. Rand. Do the right thing: Experimental evidence that preferences for moral
behavior, rather than equity or efficiency per se, drive human prosociality. Judgment and Decision
Making, 13(1):99–111, 2018.
18

--- Page 19 ---

L. Chen and P. Pu. Survey of preference elicitation methods. Technical report, 2004.
D. J. Cohen and M. Ahn. A subjective utilitarian theory of moral judgment. Journal of Experimental
Psychology: General, 145(10):1359, 2016.
W. Conen and T. Sandholm. Preference elicitation in combinatorial auctions. In Proceedings of the
3rd ACM Conference on Electronic Commerce, pages 256–259, 2001.
M. J. Crockett. Computational modeling of moral decisions. In The social psychology of morality,
pages 71–90. Routledge, 2016.
O. S. Curry, M. J. Chesters, and C. J. Van Lissa. Mapping morality with a compass: Testing the
theory of ‘morality-as-cooperation’with a new questionnaire. Journal of Research in Personality,
78:106–124, 2019.
R. Dhar, S. M. Nowlis, and S. J. Sherman. Comparison effects on preference construction. Journal
of consumer research, 26(3), 1999.
P. Dragone, S. Teso, and A. Passerini. Constructive preference elicitation. Frontiers in Robotics and
AI, 4:71, 2018.
M. Elahi, F. Ricci, and N. Rubens. Active learning strategies for rating elicitation in collaborative
filtering: a system-wide perspective.
ACM Transactions on Intelligent Systems and Technology
(TIST), 5(1):1–33, 2014.
M. Feffer, M. Skirpan, Z. Lipton, and H. Heidari. From preference elicitation to participatory ml: A
critical survey & guidelines for future research. In Proceedings of the 2023 AAAI/ACM Conference
on AI, Ethics, and Society, 2023.
P. Foot. The problem of abortion and the doctrine of double effect, volume 5. Oxford, 1967.
R. Freedman, J. S. Borg, W. Sinnott-Armstrong, J. P. Dickerson, and V. Conitzer. Adapting a kidney
exchange algorithm to align with human values. Artificial Intelligence, 283:103261, 2020.
J. M. Gonzalez Sepulveda, F. R. Johnson, and D. A. Marshall. Incomplete information and irrel-
evant attributes in stated-preference values for health interventions. Health Economics, 30(11):
2637–2648, 2021.
R. K. Gould, T. M. Soares, P. Arias-Ar´evalo, M. Cant´u-Fernandez, D. Baker, H. N. Eyster, R. Kwon,
L. Prox, J. Rode, A. Suarez, et al. The role of value (s) in theories of human behavior. Current
Opinion in Environmental Sustainability, 64:101355, 2023.
E. G. Helzer, W. Fleeson, R. M. Furr, P. Meindl, and M. Barranti. Once a utilitarian, consistently
a utilitarian? examining principledness in moral judgment via the robustness of individual
differences. Journal of personality, 85(4):505–517, 2017.
S. Hoeffler and D. Ariely. Constructing stable preferences: A look into dimensions of experience
and their impact on preference stability. Journal of consumer psychology, 8(2):113–139, 1999.
E. Hofmann, E. Hoelzl, and E. Kirchler. A comparison of models describing the impact of moral
decision making on investment decisions. Journal of Business Ethics, 82:171–187, 2008.
N. Houlsby, F. Husz´ar, Z. Ghahramani, and M. Lengyel. Bayesian active learning for classification
and preference learning. arXiv preprint arXiv:1112.5745, 2011.
19

--- Page 20 ---

D. Huang and L. Luo. Consumer preference elicitation of complex products using fuzzy support
vector machine active learning. Marketing Science, 35(3):445–464, 2016.
C. M. Johnston, P. Vossler, S. Blessenohl, and P. Vayanos. Deploying a robust active preference
elicitation algorithm on mturk: Experiment design, interface, and evaluation for covid-19 pa-
tient prioritization. In Proceedings of the 3rd ACM Conference on Equity and Access in Algorithms,
Mechanisms, and Optimization, pages 1–10, 2023.
S. Kagan. The additive fallacy. Ethics, 99(1):5–31, 1988.
A. Kahng, M. K. Lee, R. Noothigattu, A. Procaccia, and C.-A. Psomas. Statistical foundations
of virtual democracy. In International Conference on Machine Learning, pages 3173–3182. PMLR,
2019.
S. Karamcheti, R. Krishna, L. Fei-Fei, and C. D. Manning. Mind your outliers! investigating the
negative impact of outliers on active learning for visual question answering. In Proceedings of
the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International
Joint Conference on Natural Language Processing, 2021.
D. Kottke, J. Schellinger, D. Huseljic, and B. Sick. Limitations of assessing active learning perfor-
mance at runtime. arXiv preprint arXiv:1901.10338, 2019.
J. Kremer, K. Steenstrup Pedersen, and C. Igel. Active learning with support vector machines.
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 4(4):313–326, 2014.
S. Lazar. Deontological decision theory and agent-centered options. Ethics, 127(3):579–609, 2017.
M. K. Lee, D. Kusbit, A. Kahng, J. T. Kim, X. Yuan, A. Chan, D. See, R. Noothigattu, S. Lee, A. Pso-
mas, et al. Webuildai: Participatory framework for algorithmic governance. Proceedings of the
ACM on human-computer interaction, 3(CSCW):1–35, 2019.
E. Liscio, R. Lera-Leri, F. Bistaffa, R. I. Dobbe, C. M. Jonker, M. Lopez-Sanchez, J. A. Rodriguez-
Aguilar, and P. K. Murukannaiah. Inferring values via hybrid intelligence. In HHAI 2023: Aug-
menting Human Intellect, pages 373–378. IOS Press, 2023.
E. Liscio, L. C. Siebert, C. M. Jonker, and P. K. Murukannaiah. Value preferences estimation and
disambiguation in hybrid participatory systems. arXiv preprint arXiv:2402.16751, 2024.
A. Loreggia, N. Mattei, F. Rossi, and K. B. Venable.
Metric learning for value alignment.
In
AISafety@ IJCAI, 2019.
D. Lowell, Z. C. Lipton, and B. C. Wallace. Practical obstacles to deploying active learning. In
Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th
International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 21–30, 2019.
K. Margatina and N. Aletras. On the limitations of simulating active learning. arXiv preprint
arXiv:2305.13342, 2023.
A. Marley and M. Regenwetter. Choice, preference, and utility: Probabilistic and deterministic
representations. New handbook of mathematical psychology, 1:374–453, 2016.
D. McElfresh, L. Chan, K. Doyle, W. Sinnott-Armstrong, V. Conitzer, J. S. Borg, and J. Dickerson.
Indecision modeling. In Proceedings of the Thirty-Fifth AAAI Conference on Artificial Intelligence,
2021.
20

--- Page 21 ---

R. Noothigattu, S. Gaikwad, E. Awad, S. Dsouza, I. Rahwan, P. Ravikumar, and A. Procaccia.
A voting-based system for ethical decision making. In Proceedings of the AAAI Conference on
Artificial Intelligence, 2018.
A. Pine, B. Seymour, J. P. Roiser, P. Bossaerts, K. J. Friston, H. V. Curran, and R. J. Dolan. Encoding
of marginal utility across time in the human brain. Journal of Neuroscience, 29(30):9575–9581,
2009.
D. W. Portmore. Consequentializing. Stanford Encyclopedia of Philosophy, 2022.
B. Priyogi. Preference elicitation strategy for conversational recommender system. In Proceedings
of the twelfth ACM international conference on web search and data mining, pages 824–825, 2019.
P. Rehren and W. Sinnott-Armstrong. How stable are moral judgments? Review of Philosophy and
Psychology, 2022.
B. Settles. Active learning literature survey. 2009.
A. K. Shah and D. M. Oppenheimer. Heuristics made easy: an effort-reduction framework. Psy-
chological bulletin, 134(2):207, 2008.
W. Sinnott-Armstrong, J. A. Skorburg, et al. How ai can aid bioethics. Journal of Practical Ethics, 9
(1), 2021.
T. Sivill. Ethical and statistical considerations in models of moral judgments. Frontiers in Robotics
and AI, 6:449751, 2019.
P. Slovic. The construction of preference. In Shaping entrepreneurship research. Routledge, 2020.
A. Snijders, D. Kiela, and K. Margatina. Investigating multi-source active learning for natural
language inference. In Proceedings of the 17th Conference of the European Chapter of the Association
for Computational Linguistics, pages 2179–2201, 2023.
V. Soekhai, C. Whichello, B. Levitan, J. Veldwijk, C. A. Pinto, B. Donkers, I. Huys, E. van Over-
beeke, J. Juhaeri, and E. W. de Bekker-Grob. Methods for exploring and eliciting patient prefer-
ences in the medical product lifecycle: a literature review. Drug discovery today, 24(7):1324–1331,
2019.
M. Srivastava, H. Heidari, and A. Krause. Mathematical notions vs. human perception of fairness:
A descriptive approach to fairness for machine learning. In Proceedings of the 25th ACM SIGKDD
international conference on knowledge discovery & data mining, pages 2459–2468, 2019.
S. Tong and D. Koller. Support vector machine active learning with applications to text classifica-
tion. Journal of machine learning research, 2(Nov):45–66, 2001.
O. Toubia, D. I. Simester, J. R. Hauser, and E. Dahan. Fast polyhedral adaptive conjoint estimation.
Marketing Science, 22(3), 2003.
G. Ugazio, M. Grueschow, R. Polania, C. Lamm, P. Tobler, and C. Ruff. Neuro-computational
foundations of moral preferences. Social Cognitive and Affective Neuroscience, 17(3):253–265, 2022.
V. J. Vanberg. On the economics of moral preferences. American journal of Economics and Sociology,
67(4):605–628, 2008.
21

--- Page 22 ---

P. Vayanos, Y. Ye, D. McElfresh, J. Dickerson, and E. Rice. Robust active preference elicitation.
arXiv preprint 2003.01899, 2020.
C. Warren, A. P. McGraw, and L. Van Boven. Values and preferences: defining preference con-
struction. Wiley Interdisciplinary Reviews: Cognitive Science, 2(2):193–205, 2011.
M. G. Weernink, S. I. Janus, J. A. Van Til, D. W. Raisch, J. G. Van Manen, and M. J. IJzerman. A
systematic review to identify the use of preference elicitation methods in healthcare decision
making. Pharmaceutical medicine, 28:175–185, 2014.
H. Yang, S. Sanner, G. Wu, and J. P. Zhou. Bayesian preference elicitation with keyphrase-item
coembeddings for interactive recommendation. In Proceedings of the 29th ACM Conference on
User Modeling, Adaptation and Personalization, 2021.
E. Zhao, A. Liu, A. Anandkumar, and Y. Yue. Active learning under label shift. In International
Conference on Artificial Intelligence and Statistics. PMLR, 2021.
22

--- Page 23 ---

A
Details of Active Learning Algorithms
In this section, we provide additional details of the two active learning algorithms that we evaluate
in the main body.
Version Space-based Active Learning – ACTIVE-VS-PE.
The first approach relies on kernel
SVM-based classification. Given an SVM decision boundary learned using available labeled com-
parisons for an agent, the informativeness of any new query can be quantified using the distance
of the query from the decision boundary and this heuristic can be used to generate an informative
next query for the agent. For any given input x ∈Rd, an SVM classifier computes
fw(x) = ⟨w, ϕ(x)⟩,
where ϕ : Rd →F is a mapping to a kernel-induced space F for a given kernel κ : Rd × Rd →R,
such that κ(x, x′) = ⟨ϕ(x), ϕ(x′)⟩, w ∈F is the weight vector, and the classifier decision is 1 if
fw(x) > 0 and −1 otherwise2. Suppose we have a labelled training set S = {(xi, yi)}i, where
xi ∈Rd and yi ∈{1, −1}. The version space for S denotes all vectors w ∈F that fit S, i.e.,
V(S) := {w | ||w|| = 1, y · fw(x) > 0 for all (x, y) ∈S}.
The goal of active learning here is to select an element to add to S which significantly reduces
the size of V(S). To that end, Tong and Koller (2001) propose sampling a query that is closest to
the decision boundary, i.e, sampling an element ˆx := arg minu |⟨w, ϕ(x)⟩| = arg minu | fw(x)|.3 To
implement this approach in Algorithm 1, at each timestep t, we are given the dataset ((xi, x′
i))t
i=1
to labels (ri)t
i=1. Hence, sampling using the above SVM-based approach would require first learn-
ing an SVM hypothesis f that best fits ((xi, x′
i))t
i=1 to labels (ri)t
i=1 and then finding the pairwise
comparison arg min(x,x′) | f ((x, x′))|.
Bayesian Active Learning – ACTIVE-BAYES-PE.
Another popular active learning-based prefer-
ence elicitation approach uses a Bayesian framework for sampling based on information learned
from previous agent responses. The Bayesian Active Learning with Disagreement (BALD) al-
gorithm by Houlsby et al. (2011) models individual preferences using a Gaussian process with
a specified kernel. Based on the Gaussian Process classification literature, suppose each point
x ∈Rd can be characterized by a latent value, f (x), such that f follows a Gaussian distribution.
That is, f ∼GP(µ(·), κ(·, ·)), where µ denotes the mean function and κ is a pre-defined kernel.
We can model the label y ∈{0, 1} at any point x as following the Bernoulli(Φ( f (x))) distribution,
where Φ is the Gaussian CDF function. In this setup, suppose the following queries have been
made so far: S : {(xi, yi)}t
i=1. Then, the BALD approach suggests selecting the next query to be
the one that maximizes mutual information or the decrease in expected posterior entropy, i.e.,
arg max
x
H(y | x, S) −Ef ∼P[ f |S][H(y | x, f )].
2Since we are dealing with pairwise comparisons, we will not include any bias term in the SVM functional form.
3Alternative SVM-based sampling heuristics that can have better theoretical and empirical real-world performance
have also been proposed in other works Kremer et al. (2014). We tested these heuristics in our simulation setting and
they have similar performance as the one described above.
23

--- Page 24 ---

Houlsby et al. (2011) show that, in case of Gaussian process prior for the function f, we can
approximate the quantity H(y | x, S) −Ef ∼P[ f |S][H(y | x, f )], for any query x, as
I(x) := h

Φ


µx,S
q
σ2
x,S + 1



−C
exp

−
µ2
x,S
2(σ2
x,S+C2)

q
σ2
x,S + C2
.
(1)
Here h(p) := −p log p −(1 −p) log(1 −p), C = √
π ln 2/2, and µx,S, σx,S are the posterior predic-
tive mean and deviation of f (x). Hence, in the active learning setup, the goal in every iteration is
to find the query x that maximizes I(x).
Implementation of this approach for the pairwise comparison setting of Algorithm 1 first requires
learning a representation of the posterior of f (·) corresponding to the labeled dataset ((xi, x′
i))t
i=1,
(ri)t
i=1 and then computing a new pairwise comparison (x, x′) that maximizes I((x, x′)).
Use-cases of the above algorithms.
The two active learning approaches we consider represent
two different paradigms for query sampling. ACTIVE-VS-PE is a non-probabilistic discriminative
sampling method while ACTIVE-BAYES-PE represents a probabilistic entropy-based approach.
Depending on the application, one might be favored over the other. The Bayesian can be favorable
when the information gain function I(·) is submodular – allowing for near-optimal optimization
using greedy approaches. Another advantage of this approach is that it is independent of model
choices or optimization methods. The version-space approach, on the other hand, is easier to
implement and performs better for certain applications like text classification. However, there are
theoretical similarities between the two approaches and they can be equivalent in some settings
as well Houlsby et al. (2011).
4
6
8
10
12
14
Number of features
0.05
0.00
0.05
0.10
0.15
Accuracy diff
 b/w AL & Random
ACTIVE-BAYES-PE: 30 queries
ACTIVE-VS-PE: 30 queries
4
6
8
10
12
14
Number of features
0.05
0.00
0.05
0.10
0.15
ACTIVE-BAYES-PE: 50 queries
ACTIVE-VS-PE: 50 queries
10
20
30
40
50
Number of comparisons (d=5)
0.70
0.75
0.80
0.85
0.90
0.95
1.00
Accuracy
ACTIVE-BAYES-PE
ACTIVE-VS-PE
RANDOM-PE
10
20
30
40
50
Number of comparisons (d=10)
0.70
0.75
0.80
0.85
0.90
0.95
1.00
ACTIVE-BAYES-PE
ACTIVE-VS-PE
RANDOM-PE
Figure 5: Performance of ACTIVE-VS-PE, ACTIVE-BAYES-PE and RANDOM-PE in an “idealized
setting” (i.e., no assumption violations).
B
Additional Implementation Details
Implementation details of the presented simulations that were excluded from the main body are
presented here.
Other details of ACTIVE-BAYES-PE and ACTIVE-VS-PE implementation.
As mentioned ear-
lier, both ACTIVE-BAYES-PE and ACTIVE-VS-PE use linear kernels. For each method, at every
time-step t, we sample 1000 new comparisons T := {( ˆxi, ˆxi′)}i and compute the informativeness of
each comparison as defined by the method.
24

--- Page 25 ---

For ACTIVE-VS-PE, we first learn an SVM hypothesis (using the labelled comparisons), say with
coefficients ˆwt, and measure the absolute value of dot product between feature differences for
each comparison in T and ˆwt, i.e., we compute {|( ˆxi −ˆxi′)⊤ˆwt|}i. The chosen comparison is the
one with the smallest absolute dot product value.
For ACTIVE-BAYES-PE, when using a linear kernel, we first employ Bayesian ARD regression
(over the labelled comparisons) with priors for the regularization and precision parameters set
to Γ(1, 1). With the kernel parameters obtained from this regression, we compute the mean and
variance of the latent value for each pairwise comparison difference in T. For each (ˆx, ˆx′) ∈T,
we then compute I(ˆx −ˆx′) (where I(·) is the mutual information function and defined in the
description of the bayesian active learning approach), and choose the comparison that maximizes
this value. We also tested ACTIVE-BAYES-PE with the standard RBF kernel and it had a similar or
worse performance than the linear kernel approach.
Model fitting details.
The hypothesis class H is set to be the class of linear SVM functions and
the fit(·, ·) function executes the standard linear-SVM training procedure (using python sklearn
library) with L2-regularization. Specifically, we set these functions to operate over feature differ-
ences, i.e., for any given comparison (x, x′), the input to an SVM classifier ht in the feature-wise
difference (x −x′). Using feature differences is a standard approach in pairwise comparison set-
ting in practice Freedman et al. (2020). Correspondingly, the vector ˆwht for each ht represents
weights assigned to individual feature differences.
Implementing the tree-based utility model.
Finally, to simulate an agent with a tree-based
model of depth d′, we essentially create a binary tree of depth d′, choosing random features and
feature values for partitioning at each node.
C
Additional results
In this section, we provide additional results that had to be omitted from the main body due to
space constraints.
First, Figure 5 denotes the performance of both active learning algorithms in an “ideal” setting,
i.e., when preferences are stable and do not suffer from any kind of noise and when both the
underlying preferences and the hypothesis class H are linear functions over the available features
(without interactions). In this case, we clearly see the advantage of using active learning. Both
ACTIVE-BAYES-PE and ACTIVE-VS-PE outperform the RANDOM-PE baseline in all cases.
C.1
Preference Instability
Performance with respect to normalized distance metric.
The results with respect to Normal-
ized L2-distance for scenarios Downscale-ordered, Upscale-ordered, and Random-switch are
presented in Figure 6. Overall, the trends are similar as the ones for accuracy metric.
Additional preference change scenarios.
Beyond the ones presented in Section 4.1, we simulate
the following other kinds of preference changes as well.
• Downscale-random: Agent change preference to use just one random feature after timestep
tchange.
25

--- Page 26 ---

10
20
30
40
50
0.0
0.2
0.4
0.6
0.8
L2-Distance
tchange=10; d=5
10
20
30
40
50
0.0
0.5
1.0
1.5
tchange=10; d=10
10
20
30
40
50
0.0
0.2
0.4
0.6
0.8
L2-Distance
tchange=20; d=5
10
20
30
40
50
0.25
0.50
0.75
1.00
1.25
tchange=20; d=10
10
20
30
40
50
#comparisons N
0.0
0.2
0.4
0.6
0.8
L2-Distance
tchange=30; d=5
10
20
30
40
50
#comparisons N
0.00
0.25
0.50
0.75
1.00
1.25
tchange=30; d=10
Downscale-ordered
ACTIVE-BAYES-PE
ACTIVE-VS-PE
RANDOM-PE
10
20
30
40
50
0.0
0.2
0.4
0.6
0.8
1.0
tchange=10; d=5
10
20
30
40
50
0.0
0.5
1.0
1.5
tchange=10; d=10
10
20
30
40
50
0.0
0.2
0.4
0.6
0.8
tchange=20; d=5
10
20
30
40
50
0.25
0.50
0.75
1.00
1.25
tchange=20; d=10
10
20
30
40
50
#comparisons N
0.0
0.2
0.4
0.6
0.8
tchange=30; d=5
10
20
30
40
50
#comparisons N
0.00
0.25
0.50
0.75
1.00
1.25
tchange=30; d=10
Upscale-ordered
10
20
30
40
50
0.0
0.5
1.0
1.5
2.0
2.5
tchange=10; d=5
10
20
30
40
50
0.0
0.5
1.0
1.5
2.0
tchange=10; d=10
10
20
30
40
50
0.0
0.5
1.0
1.5
2.0
2.5
tchange=20; d=5
10
20
30
40
50
0.0
0.5
1.0
1.5
2.0
2.5
tchange=20; d=10
10
20
30
40
50
#comparisons N
0.0
0.5
1.0
1.5
2.0
2.5
tchange=30; d=5
10
20
30
40
50
#comparisons N
0.0
0.5
1.0
1.5
2.0
2.5
tchange=30; d=10
Random-switch
Figure 6: Normalized L2-distance vs number of comparisons for ACTIVE-VS-PE, ACTIVE-BAYES-
PE and RANDOM-PE algorithms. Each plot represents a different configuration of the preference
change scenario presented in Section 4.1.
• Upscale-random: Agent changes preference from using just one feature to using all features
after timestep tchange.
• Downscale-ordered-2: Agent simplifies preference to use the top-two highest weighted fea-
tures after timestep tchange.
• Downscale-ordered-4: Agent simplifies preference to use the top-four highest weighted fea-
tures after timestep tchange.
• Upscale-ordered-2: Agent changes preference from using only two features to using all fea-
tures after timestep tchange, with all features in wpost having lower relative weight than the
non-zero weights in wpre.
• Upscale-ordered-4: Agent changes preference from using only four features to using all
features after timestep tchange, with all features in wpost having lower relative weight than
the non-zero weights in wpre.
The results for these preference change scenarios are presented in Figure 7. The scenarios consid-
ered here also reflect different scales of preference change. For instance, preference change in the
case of Downscale-ordered-4 is relatively lower scale than that in Downscale-ordered-2.
This preference change scale is also reflected in the results. The accuracy drop post-tchange is
smaller in the case of Downscale-ordered-4 and Upscale-ordered-4, compared to Downscale-
ordered-2 and Upscale-ordered-2. Correspondingly, in these settings, the impact on active learn-
ing algorithms is also relatively smaller. For all settings in Downscale-ordered-4 and Upscale-
ordered-4, one can see that both ACTIVE-VS-PE and ACTIVE-BAYES-PE recover well from pref-
erence change and have better accuracy and efficiency than the RANDOM-PE baseline change.
As the scale of preference change increases, active learning can be seen to be less effective. For
example, the difference in accuracy between the active learning approaches and the random base-
line is smaller in the case of Downscale-ordered-2 and Upscale-ordered-2. Nevertheless, we once
26

--- Page 27 ---

Figure 7: Accuracy vs number of comparisons for additional preference change scenarios dis-
cussed in Appendix C.1.
again observe that when the number of features is small and/or preference change happens early,
active learning (especially ACTIVE-BAYES-PE) can still achieve high accuracy faster than the ran-
dom query baseline post-tchange.
C.2
Model Misspecification
For model misspecification scenarios, here we present results for accuracy vs number of com-
parisons. We set the number of features d to be 4, 8, or 16. In all cases, the extent of model
misspecification is quantified by ⌊log(d)⌋. The results for this setting are presented in Figure 8.
C.3
Noisy Responses
This section presents additional results for the simulations where the agent’s responses are noisy
or stochastic.
27

--- Page 28 ---

10
20
30
40
50
0.5
0.6
0.7
0.8
0.9
1.0
d=4
10
20
30
40
50
0.5
0.6
0.7
0.8
0.9
1.0
d=8
10
20
30
40
50
0.5
0.6
0.7
0.8
0.9
1.0
d=16
Agent uses tree-based preference model, but 
 is the linear class (tree depth= log(d) )
ACTIVE-BAYES-PE
ACTIVE-VS-PE
RANDOM-PE
10
20
30
40
50
0.5
0.6
0.7
0.8
0.9
1.0
d=4
10
20
30
40
50
0.5
0.6
0.7
0.8
0.9
1.0
d=8
10
20
30
40
50
0.5
0.6
0.7
0.8
0.9
1.0
d=16
Agent uses second-order preferences but 
 assumes no interactions (#interaction terms= log(d) )
10
20
30
40
50
0.5
0.6
0.7
0.8
0.9
1.0
d=4
10
20
30
40
50
0.5
0.6
0.7
0.8
0.9
1.0
d=8
10
20
30
40
50
0.5
0.6
0.7
0.8
0.9
1.0
d=16
Missing features in the preference elicitation framework (#missing features= log(d) )
Figure 8: Accuracy vs number of comparisons for model misspecification scenarios presented in
Section 4.2.
28

--- Page 29 ---

Performance with respect to L2-distance.
Figure 9 presents the equivalent of Figure 4 for nor-
malized distance comparison. Here, the trends are similar to the accuracy plots. ACTIVE-BAYES-
PE has the best performance in the case of response noise but fails to provide similarly improved
performance in all settings of preference noise.
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Noise parameter 
0.0
0.2
0.4
0.6
0.8
L2-Distance
d=5; N=30
10
20
30
40
50
#comparisons N
0.00
0.25
0.50
0.75
1.00
1.25
d=5; =2
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Noise parameter 
0.0
0.2
0.4
0.6
L2-Distance
d=10; N=30
10
20
30
40
50
#comparisons N
0.00
0.25
0.50
0.75
1.00
1.25
d=10; =2
Response Noise
ACTIVE-BAYES-PE
ACTIVE-VS-PE
RANDOM-PE
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Noise parameter 
0.0
0.5
1.0
1.5
2.0
d=5; N=30
10
20
30
40
50
#comparisons N
0.0
0.5
1.0
1.5
2.0
d=5; =2
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
Noise parameter 
0.0
0.5
1.0
1.5
d=10; N=30
10
20
30
40
50
#comparisons N
0.0
0.5
1.0
1.5
2.0
d=10; =2
Preference Noise
Figure 9: L2-distance comparison of ACTIVE-VS-PE, ACTIVE-BAYES-PE and RANDOM-PE algo-
rithms for different kinds of noise models presented in Section 4.3.
Performance with respect to time-variant noise.
In addition to constant noise, we simulate the
setting where the noise decreases with time. This model can also be considered a combination
of the noisy responses and preference instability simulations since the variation in the agent’s prefer-
ence/utility computation model is time-dependent.
In this case, for the Response noise model, ε ∼N (0, ˆσ2), where ˆσ = σ/
√
t, where t is the
time-step/number of comparisons made so far. Similarly, for the Preference noise model, w ∼
N (w⋆, ˆσ2I/d), where ˆσ = σ/
√
t. This time we vary σ from 1 to 10, to capture a larger range of
noise parameters.
The results for these two noise models with time-variant noise parameters are presented in Fig-
ure 10. Considering the relatively smaller impact of noise in this setting, the active learning al-
gorithms have much-improved performance in comparison to the random query baseline for the
response noise model. For the preference noise model, however, improved performance of active
learning is again only observed when the noise magnitude is relatively small.
29

--- Page 30 ---

0
2
4
6
8
10
Noise parameter 
0.7
0.8
0.9
1.0
Accuracy
d=5; N=30
10
20
30
40
50
#comparisons N
0.6
0.7
0.8
0.9
1.0
d=5; =5
0
2
4
6
8
10
Noise parameter 
0.7
0.8
0.9
1.0
Accuracy
d=10; N=30
10
20
30
40
50
#comparisons N
0.6
0.7
0.8
0.9
1.0
d=10; =5
Response Noise (time variant)
ACTIVE-BAYES-PE
ACTIVE-VS-PE
RANDOM-PE
0
2
4
6
8
10
Noise parameter 
0.6
0.7
0.8
0.9
1.0
d=5; N=30
10
20
30
40
50
#comparisons N
0.5
0.6
0.7
0.8
d=5; =5
0
2
4
6
8
10
Noise parameter 
0.6
0.7
0.8
0.9
1.0
d=10; N=30
10
20
30
40
50
#comparisons N
0.5
0.6
0.7
0.8
d=10; =5
Preference Noise (time variant)
Figure 10: Accuracy of ACTIVE-VS-PE, ACTIVE-BAYES-PE and RANDOM-PE algorithms for time-
variant noise models.
30

```
