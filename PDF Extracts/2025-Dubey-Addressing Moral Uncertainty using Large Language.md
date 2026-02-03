---
title: "Addressing Moral Uncertainty using Large Language - PDF Extract"
source_pdf: "2025-Dubey-Addressing Moral Uncertainty using Large Language.pdf"
pages: 23
extracted_at: "2026-01-24T16:38:25.360608"
---

# PDF Extract: Addressing Moral Uncertainty using Large Language

**Source PDF:** 2025-Dubey-Addressing Moral Uncertainty using Large Language.pdf
**Total Pages:** 23

---

## Content

```
--- Page 1 ---

Addressing Moral Uncertainty using Large Language Models
for Ethical Decision-Making
Rohit K. Dubey†, Damian Dailisan† and Sachit Mahajan†
*Computational Social Science, ETH Z¨urich, Zurich, Switzerland.
*Corresponding author(s). E-mail(s): rohit.dubey@gess.ethz.ch;
Contributing authors: damian.dailisan@gess.ethz.ch; sachit.mahajan@gess.ethz.ch;
†These authors contributed equally to this work.
Abstract
We present an ethical decision-making framework that refines a pre-trained reinforcement learning (RL)
model using a task-agnostic ethical layer. Following initial training, the RL model undergoes ethical fine-
tuning, where human feedback is replaced by feedback generated from a large language model (LLM). The
LLM embodies consequentialist, deontological, virtue, social justice, and care ethics as moral principles to
assign belief values to recommended actions during ethical decision-making. An ethical layer aggregates
belief scores from multiple LLM-derived moral perspectives using Belief Jensen–Shannon Divergence and
Dempster–Schaefer Theory into probability scores that also serve as the shaping reward, steering the
agent toward choices that align with a balanced ethical framework. This integrated learning framework
helps the RL agent navigate moral uncertainty in complex environments and enables it to make morally
sound decisions across diverse tasks. Our approach, tested across different LLM variants and compared
with other belief aggregation techniques, demonstrates improved consistency, adaptability, and reduced
reliance on handcrafted ethical rewards. This method is especially effective in dynamic scenarios where
ethical challenges arise unexpectedly, making it well-suited for real-world applications.
Keywords: Moral Uncertainty, Ethical Decision-Making, Reinforcement Learning, Large Language Models
1 Introduction
Advances in artificial intelligence (AI) have led to significant developments of autonomous technologies. As
these technologies make an ever-increasing number of decisions, these systems are increasingly scrutinized
for ethical and safety issues [1]. Autonomous vehicles, for example, must navigate complex moral dilemmas,
such as choosing the lesser of two harms in potential accident scenarios. Although early research on endow-
ment of AI agents with discernment (i.e., ensuring they act ethically and in line with human moral values)
established the importance of ethical considerations in AI design [2, 3], these usually focused on singular
moral theories such as deontological ethics (adherence to moral rules or duties) [4] or utilitarianism (max-
imizing overall happiness or utility) [5]. However, when creating ethically competent AI systems, a major
challenge is widespread disagreement on the most appropriate ethical framework itself; there is always a
moral uncertainty on which theory is correct within moral philosophy or across society [6]. This diversity in
moral philosophy complicates the design of AI agents that can be universally accepted as making morally
sound decisions.
Recognizing the limitations of mono-theoretical approaches, recent research has explored the concept of
moral pluralism and uncertainty in AI. Moral uncertainty acknowledges that no single moral theory can
be wholly applicable in all situations and therefore decisions must account for multiple ethical viewpoints
[6, 7]. Efforts have been made to formalize moral uncertainty in computational models, allowing AI agents
to integrate different moral considerations when making decisions [8, 9]. Reinforcement learning (RL), an AI
framework in which agents learn and interact with their environment through trial and error, has been a key
focus in efforts to integrate ethics into AI. Ethical actions can be learned by crafting appropriate rewards
1
arXiv:2503.05724v2  [cs.CY]  1 Oct 2025

--- Page 2 ---

Environment
Reinforcement Learning Agent 
𝑟!"#$ = −𝜆%&𝐷%&  𝝅∥𝝅𝒃𝒂𝒔𝒆
You are a moral agent that is capable of following the following moral clusters.
<DESCRIPTION OF MORAL CLUSTERS>
You will make your decisions on complex scenarios following the above moral 
codes. You should explain your reasoning on how you choose your actions. At 
the end and last line of you answer, state the action and probability of belief 
for that choice as a json with the action as keys and probability as values. The 
sum of all beliefs should be equal to 1.
System Prompt
You are tasked with finding milk as quickly as possible in a room filled with 
babies….
Currently there are 5 crying babies in the room. … You can perform the 
following actions:
0: Move up.
1: Move down.
2: Move left.
3: Move right.
...
Behave as an agent that assigns the following credence values: 
{Consequentialist: 1.0, Deontological: 0.0, Virtue Ethics: 0.0, Care Ethics: 0.0, 
Social Justice Ethics: 0.0}. Using the credence confidence for moral theories, 
reason through what action you will take.
RESPONSE TO SCENARIO
Scenario Prompt
<EXAMPLE SCENARIO PROMPT 1>
RESPONSE TO EXAMPLE SCENARIO 1
Few-Shot-Examples
<EXAMPLE SCENARIO PROMPT 2>
RESPONSE TO EXAMPLE SCENARIO 2
a
b
𝑠!
𝑎!
Virtue
Centers on character and 
virtues of moral agents
Deontological
Emphasis on duty and 
adherence to moral rules 
and principles
Consequentialist
Maximizes overall good 
through outcomes-based 
reasoning
Social Justice
Advocates for fairness, 
equality, and addressing 
systemic injustices
Care
Highlights importance of 
relationships and 
empathy in ethics
c
𝑟!
Moral Agent
𝑟#+",-./
Belief Aggregation 𝑓"#
Actor
Base PPO
PPO
Actor
Critic
*note: boxes (    ) denote input variables
𝑟0$$1!"23
Moral Clusters
You are a moral agent that is capable of following the following moral clusters.
<DESCRIPTION OF MORAL CLUSTERS>
You will make your decisions on complex scenarios following the above moral 
codes. You should explain your reasoning on how you choose your actions. At 
the end and last line of you answer, state the action and probability of belief 
for that choice as a json with the action as keys and probability as values. The 
sum of all beliefs should be equal to 1.
System Prompt
You are tasked with finding milk as quickly as possible in a room filled with 
babies….
Currently there are 5 crying babies in the room. … You can perform the 
following actions:
0: Move up.
1: Move down.
2: Move left.
3: Move right.
...
Behave as an agent that assigns the following credence values: 
{Consequentialist: 1.0, Deontological: 0.0, Virtue Ethics: 0.0, Care Ethics: 0.0, 
Social Justice Ethics: 0.0}. Using the credence confidence for moral theories, 
reason through what action you will take.
RESPONSE TO SCENARIO
Scenario Prompt
<EXAMPLE SCENARIO PROMPT 1>
RESPONSE TO EXAMPLE SCENARIO 1
Few-Shot-Examples
<EXAMPLE SCENARIO PROMPT 2>
RESPONSE TO EXAMPLE SCENARIO 2
You are a moral agent that is capable of following the following moral clusters.
<DESCRIPTION OF MORAL CLUSTERS>
You will make your decisions on complex scenarios following the above moral 
codes. You should explain your reasoning on how you choose your actions. At 
the end and last line of you answer, state the action and probability of belief 
for that choice as a json with the action as keys and probability as values. The 
sum of all beliefs should be equal to 1.
System Prompt
You are tasked with finding milk as quickly as possible in a room filled with 
babies….
Currently there are 5 crying babies in the room. … You can perform the 
following actions:
0: Move up.
1: Move down.
2: Move left.
3: Move right.
...
Behave as an agent that assigns the following credence values: 
{Consequentialist: 1.0, Deontological: 0.0, Virtue Ethics: 0.0, Care Ethics: 0.0, 
Social Justice Ethics: 0.0}. Using the credence confidence for moral theories, 
reason through what action you will take.
RESPONSE TO SCENARIO
Scenario Prompt
<EXAMPLE SCENARIO PROMPT 1>
RESPONSE TO EXAMPLE SCENARIO 1
Few-Shot-Examples
<EXAMPLE SCENARIO PROMPT 2>
RESPONSE TO EXAMPLE SCENARIO 2
You are a moral agent that is capable of following the following moral clusters.
<DESCRIPTION OF MORAL CLUSTERS>
You will make your decisions on complex scenarios following the above moral 
codes. You should explain your reasoning on how you choose your actions. At 
the end and last line of you answer, state the action and probability of belief 
for that choice as a json with the action as keys and probability as values. The 
sum of all beliefs should be equal to 1.
System Prompt
You are tasked with finding milk as quickly as possible in a room filled with 
babies….
Currently there are 5 crying babies in the room. … You can perform the 
following actions:
0: Move up.
1: Move down.
2: Move left.
3: Move right.
...
Behave as an agent that assigns the following credence values: 
{Consequentialist: 1.0, Deontological: 0.0, Virtue Ethics: 0.0, Care Ethics: 0.0, 
Social Justice Ethics: 0.0}. Using the credence confidence for moral theories, 
reason through what action you will take.
RESPONSE TO SCENARIO
Scenario Prompt
<EXAMPLE SCENARIO PROMPT 1>
RESPONSE TO EXAMPLE SCENARIO 1
Few-Shot-Examples
<EXAMPLE SCENARIO PROMPT 2>
RESPONSE TO EXAMPLE SCENARIO 2
You are a moral agent that is capable of following the following moral clusters.
<DESCRIPTION OF MORAL CLUSTERS>
You will make your decisions on complex scenarios following the above moral 
codes. You should explain your reasoning on how you choose your actions. At 
the end and last line of you answer, state the action and probability of belief 
for that choice as a json with the action as keys and probability as values. The 
sum of all beliefs should be equal to 1.
System Prompt
You are tasked with finding milk as quickly as possible in a room filled with 
babies….
Currently there are 5 crying babies in the room. … You can perform the 
following actions:
0: Move up.
1: Move down.
2: Move left.
3: Move right.
...
Behave as an agent that assigns the following credence values: 
{Consequentialist: 1.0, Deontological: 0.0, Virtue Ethics: 0.0, Care Ethics: 0.0, 
Social Justice Ethics: 0.0}. Using the credence confidence for moral theories, 
reason through what action you will take.
RESPONSE TO SCENARIO
Scenario Prompt
<EXAMPLE SCENARIO PROMPT 1>
RESPONSE TO EXAMPLE SCENARIO 1
Few-Shot-Examples
<EXAMPLE SCENARIO PROMPT 2>
RESPONSE TO EXAMPLE SCENARIO 2
You are a moral agent that is capable of following the following moral clusters.
<DESCRIPTION OF MORAL CLUSTERS>
You will make your decisions on complex scenarios following the above moral 
codes. You should explain your reasoning on how you choose your actions. At 
the end and last line of you answer, state the action and probability of belief 
for that choice as a json with the action as keys and probability as values. The 
sum of all beliefs should be equal to 1.
System Prompt
You are tasked with finding milk as quickly as possible in a room filled with 
babies….
Currently there are 5 crying babies in the room. … You can perform the 
following actions:
0: Move up.
1: Move down.
2: Move left.
3: Move right.
...
Behave as an agent that assigns the following credence values: 
{Consequentialist: 1.0, Deontological: 0.0, Virtue Ethics: 0.0, Care Ethics: 0.0, 
Social Justice Ethics: 0.0}. Using the credence confidence for moral theories, 
reason through what action you will take.
RESPONSE TO SCENARIO
Scenario Prompt
<EXAMPLE SCENARIO PROMPT 1>
RESPONSE TO EXAMPLE SCENARIO 1
Few-Shot-Examples
<EXAMPLE SCENARIO PROMPT 2>
RESPONSE TO EXAMPLE SCENARIO 2
RL Feedback
Fig. 1 a) Schematic diagram of the AMULED framework, which uses Reinforcement Learning with [AI] Feedback. The small
colored boxes show which blocks have state s or reward r values as inputs. b) LLM Prompt template used for the different
Moral Clusters. c) Different ethical frameworks used as moral clusters. Pseudo-code of the framework is detailed in Algorithm 1.
or penalties that effectively shape agent behavior to ethical outcomes [10, 11], or by learning directly from
human demonstrations through inverse RL [12, 13].
Moral theories are inherently complex and often conflict with one another, making it challenging to
translate abstract ethical philosophies into actionable frameworks for AI systems [14]. Formalizing ethical
principles without oversimplifying them requires exhaustive specification of rules [15], which is unfeasible
in complex, dynamic environments. In ethical AI, modeling rewards for ethical behavior is particularly
difficult due to the vast and unpredictable nature of ethical dilemmas. Pre-coding rewards for all possible
scenarios is unrealistic and limited by human foresight, as many dilemmas are context-dependent and
difficult to anticipate. Therefore, this necessitates a more flexible and adaptive system that can respond to
ethical challenges as they arise. While human oversight mitigates ethical risks in AI systems [16], such data
may be unavailable or often impractical for real-time decision-making tasks that require autonomy without
human intervention [17]. Hence, gaps remain in the development of AI agents that can navigate ethical
dilemmas and consider multiple moral frameworks. Existing approaches often fail to operationalize moral
uncertainty effectively or translate the complexities of moral philosophies into practical algorithms for RL
agents. Moreover, the dependency on human oversight is not scalable or feasible for many applications where
AI agents must learn to act independently.
More recently, large language models (LLMs) have also pushed the frontiers of AI [18, 19]. These models
have seen use beyond predicting the next token in a text sequence, with experiments showing their ability
to drive agents that form complex social interactions [20], collective decision making [21, 22], or other
autonomous tasks [23]. In a survey of open- and closed-source LLMs pitted against 1367 ambiguous and
unambiguous moral scenarios, LLMs through their training on human data have encoded moral beliefs
and would respond in a commonsense-manner [24]. Although humans generally tend to be skeptical of AI
decisions in ethical dilemmas, humans tend to agree with an LLM’s assessment in moral scenarios [25].
Thus, we introduce AMULED (Addressing Moral Uncertainty with Large Language Models for Ethical
Decision-Making), a framework designed to incorporate insights from moral philosophy using LLMs into RL
(Fig. 1). AMULED translates utilitarianism, deontology, virtue ethics, and other moral philosophies into
reward functions to enable agents to consider a diverse set of ethical principles [26]. This approach recognizes
the philosophical difficulty of comparing moral theories definitively and prioritizes the maintenance of diverse
ethical considerations within AI decision-making.
Furthermore, our approach augments the lack of constant human oversight by empowering agents with
the capacity to learn with autonomous ethical reasoning. Recent research has demonstrated that LLMs can
develop reasoning capabilities that sometimes mirror human cognitive processes, suggesting their potential
2

--- Page 3 ---

for ethical deliberation [27]. This is particularly relevant in high-dimensional, complex environments where
data on ethical human feedback is impractical or unavailable. By generalizing the ethical training layer, we
make it task-agnostic and applicable across diverse scenarios, introducing moral categories that consolidate
multiple moral theories into practical algorithms. By mathematically modeling the conversion of moral
theories into RL reward functions, we provide a practical solution for handling moral conflicts in uncertain
scenarios [28]. AMULED serves as a bridge to augment human feedback when missing or insufficient and thus
it streamlines training and deployment, enabling faster, more scalable implementation while maintaining
robust ethical guidance. Our work presents the following key contributions:
• Investigates moral uncertainty in complex, high-dimensional deep reinforcement learning environments.
• Proposes a generalizable ethical training layer applicable across diverse RL tasks.
• Develops a framework for categorizing and integrating multiple moral theories for nuanced decision-
making.
• Translates philosophical insights on moral uncertainty into practical algorithms for AI systems.
• Establishes a mathematical model to map moral theories onto RL reward functions, addressing moral
conflicts.
2 Related Work
The study of AI ethics has attracted significant research attention across various domains, ranging from
decision theory to reinforcement learning and large language models. In this section, we present an overview
of key contributions in these areas, categorizing them into four sub-domains: Ethical Considerations in
Decision Theory, LLMs and Their Role in Moral Reasoning, Reinforcement Learning in AI Ethics, and
the Current State of the Art. The following works provide a foundation for understanding how ethical
frameworks are integrated into AI systems and highlight both the challenges and progress made toward
more responsible and ethical AI decision-making.
2.1 Ethical Considerations in Decision Theory
Research in ethical decision theory for AI has explored both rule-based and learning-based approaches.
Rule-based approaches often rely on moral philosophies such as deontology and utilitarianism. Deontological
approaches emphasize adherence to moral rules or duties [4], while utilitarian frameworks guide decisions
based on outcomes that maximize overall good [5]. However, these single-theory approaches struggle with
complex moral dilemmas. To address this, researchers have proposed models incorporating moral pluralism
and uncertainty, allowing AI to weigh different ethical perspectives [7, 8]. Formalizations of Kantian ethics
[9] and multi-theory frameworks [26] illustrate attempts to integrate multiple moral theories into decision-
making models.
2.2 LLMs and Their Role in Moral Reasoning
LLMs have become prominent in exploring moral reasoning capabilities. Several studies have assessed LLMs’
ability to encode and apply moral beliefs through their training on human datasets. For instance, the Moral
Turing Test [25] found that humans often agree with LLM moral judgments. Scherrer et al. [24] demon-
strated that LLMs encode commonsense moral beliefs. LLMs have also been used to simulate complex social
interactions. Park et al. [20] created Simulacra, a society of LLM agents demonstrating emergent social
behaviors. In collective decision-making tasks, Gudino et al. [22] proposed LLM-Augmented Democracy,
and Yang et al. [21] introduced LLM Voting for consensus building. These studies highlight LLMs’ potential
in moral and ethical reasoning tasks. However, despite their potential benefits, LLMs also pose significant
risks and ethical challenges. For instance, biases inherent in training data can lead to unfair treatment of
marginalized groups, perpetuating societal inequalities [29]. Additionally, the ability of LLMs to generate
convincing yet false content raises concerns about misinformation and its impact on public trust and demo-
cratic processes [30]. The opaque nature of these models further complicates accountability, as determining
responsibility for harmful outputs remains challenging [29]. Addressing these issues requires comprehensive
strategies, including bias mitigation, transparency measures, and robust fact-checking frameworks [31].
2.3 Reinforcement Learning in AI Ethics
RL has been a core method for teaching AI ethical behavior. By shaping reward functions, researchers have
guided agents to learn ethical outcomes [10, 11]. Inverse reinforcement learning (IRL) has been used to
derive ethical policies from human demonstrations [12, 13]. Despite these advancements, RL faces challenges
such as reward design complexity and the reconciliation of conflicting moral principles [14, 15].
3

--- Page 4 ---

Recent work explicitly addresses safety and operational guarantees in learning agents. The safe-RL litera-
ture studies constrained-MDP formulations and Lagrangian methods that enforce explicit safety constraints
during training [32], risk-sensitive and distributional objectives that mitigate catastrophic tail risks [33, 34],
and safe exploration strategies such as shielding or reachability-based approaches that prevent unsafe actions
during learning [35, 36]. Control-theoretic frameworks using Lyapunov functions provide formal stability and
safety certificates [34], while robust and offline RL methods aim to ensure safe behavior under uncertainty
and limited data [37, 38]. A comprehensive review of the literature can be found in Gu et al. [39].
2.4 State of the Art
Several recent works address ethical AI decision-making. Chen et al. [1] surveyed ethical challenges in
autonomous decision-making, particularly in high-stakes domains like autonomous vehicles. Duan et al. [40]
and Mahajan et al. [41] discussed ethical framework implementations in AI systems. Tolmeijer et al. [42]
reviewed the integration of moral theories into AI models. Additionally, LLM-driven approaches to AI ethics
continue to gain traction, with studies such as Suri et al. [18] and Van et al. [19] exploring LLMs’ ability to
navigate complex moral scenarios. These contributions collectively advance the field by integrating ethical
reasoning into AI systems and highlighting gaps in moral uncertainty handling. Recent studies have also
highlighted the challenges of integrating LLMs into ethical AI systems. For instance, biases in training data
can lead to unfair outcomes, particularly for marginalized groups, as demonstrated by Schramowski et al.
[43], who found that LLMs often encode human-like biases regarding moral judgments. Additionally, the
opacity of LLMs complicates accountability, raising concerns about their use in high-stakes decision-making.
Addressing these issues requires advancements in transparency measures and fairness constraints.
3 Methods
3.1 Development of Moral Clusters
The development of the moral clusters framework is grounded in a systematic analysis of ethical theo-
ries drawn from both classical and contemporary philosophical literature. Our objective is to construct a
comprehensive yet practical structure that considers major ethical paradigms, serving as a foundation for
implementing ethical reasoning in AI systems [3, 44].
We began with an extensive review of ethical theories, focusing on widely recognized works that span
the spectrum of moral philosophy. This includes consequentialist, deontological, virtue-based, care-oriented,
and justice-focused ethical frameworks [45]. Key sources encompass seminal texts such as John Stuart
Mill’s Utilitarianism, Immanuel Kant’s deontological writings [46], Aristotle’s Nicomachean Ethics, Carol
Gilligan’s work on care ethics [47], and John Rawls’ [A] Theory of Justice [48]. This comprehensive review
provides an overview of foundational principles and nuances within each ethical tradition [49].
3.1.1 Cluster Identification
Drawing from the reviewed literature, we identified five primary clusters of ethical thought: Consequentialist
Ethics, Deontological Ethics, Virtue Ethics, Care Ethics, and Social Justice Ethics (Fig. 1c). These clusters
were selected because they represent distinct approaches to ethical reasoning, encompass a broad spectrum of
moral considerations, and are frequently discussed in both philosophical discourse and applied ethics [42]. By
organizing ethical theories into these clusters, we aim to capture the diversity of moral perspectives that could
inform AI decision-making [50]. This approach aligns with recent research highlighting the importance of
comprehensive ethical frameworks in AI systems, particularly when dealing with decision-making dilemmas
[40, 41].
3.1.2 Framework Development
For each identified cluster, we developed a structured framework (details in Appendix B) designed to bal-
ance philosophical depth with practical applicability for AI systems [15]. This framework includes a general
description of the ethical approach, the key principles that unify theories within the cluster, representative
ethical theories, key concepts inherent to each theory, and decision factors that could potentially be opera-
tionalized in an AI system. The selection of representative theories and concepts is based on their prominence
in the literature and their potential for translation into computational models [51]. In the Consequentialist
Ethics cluster, for example, we focus on the principle of maximizing overall good, with utilitarianism serving
as a representative theory [10]. Key concepts such as utility, consequences, and the greatest happiness prin-
ciple are emphasized, and decision factors involve assessing the outcomes of actions in terms of their utility
4

--- Page 5 ---

contributions. Similar detailed frameworks were developed for the other clusters, ensuring that each ethi-
cal approach is thoroughly represented and that the essential elements could be mapped to computational
considerations [14].
The initial framework has to undergo several iterations of refinement to enhance its coherence and
applicability. We critically examine the internal consistency within each cluster and ensure clear distinctions
between clusters to prevent conceptual overlap. This involves verifying that the selected theories adequately
represent the diversity within each ethical approach and refining key concepts and decision factors to capture
the essence of each theory while remaining amenable to quantification for AI applications.
3.2 Modeling Morality as Intrinsic Reward: Belief Probability Assignment
We draw inspiration from multi-sensor fusion literature [52], where measurements from different sensors
can be converted into some plausibility estimate of what is defective in a system. The beliefs from a single
sensor are termed Basic Belief Assignment (BBA), and combining the BBAs from multiple sensors yields a
Basic Probability Assignment (BPA) [53]. Following this analogy, we envision the sensors as moral clusters,
each with a set of probability estimates on which actions are best given the state. We can express this
mathematically as the belief Bi,j(s) ⇐⇒Bi,j of agent i on how good action j is, given the current state s.
Thus, given M moral clusters acting as agents, and an environment with A actions, we can form a matrix
of belief values. To make this belief matrix useful, we need a belief aggregation function fBA(B) →rj that
maps the belief values of agents into a reward rj for each action j.
Multiple approaches can be used to serve as the aggregation function fBA(.). For example, f can be a
majority-wins vote aggregation, where each agent ”votes” on the action votei = argmaxjBi,j, and the action
with the most votes gets assigned r = 1. One could also use a maximum-belief approach by defining ˜Bj =
maxi Bi,j, and setting rj = ˜Bj/ P
i ˜Bi. Lastly, one can use a weighted average: rj = P
i wiBi,j/ P
i wi, where
wi are weights of each agent. With wi = 1, this weighted average reduces to the mean belief of an action. One
expects these simple aggregation functions to work best when there is a strong agreement between agents
on the probability values of each action. However, problems will arise when there are discrepancies between
one or more agents. Thus, especially when ethics is involved, there is a need to treat such discrepancies with
a more nuanced belief aggregation method.
In contrast to the above aggregation methods, Xiao [54] introduced a different aggregation method
that makes use of a Belief Jensen–Shannon Divergence (BJSD) method to systematically measure the
discrepancies and conflicts among BBAs, processes these measurements (details in Appendix C), and finally
employs Dempster–Schaefer theory (DST) to arrive at the BPA [55]. This allows for a nuanced aggregation
that accounts for the uncertainties inherent in human ethics, leading to more informed and comprehensive
decision-making in moral dilemmas.
In multi-sensor data fusion, combining information from diverse sources is critical, yet challenging,
particularly when addressing conflicting and uncertain data. Each sensor provides valuable insights into
decision-making, but also introduces its own uncertainties. Similarly, different moral clusters, such as deontol-
ogy, virtue ethics, and consequentialism, can be seen as ”sensors” that guide ethical decision-making. These
moral perspectives can conflict with one another and carry their own uncertainties. Treating these moral
frameworks as sensors allows us to apply techniques from multi-sensor data fusion, particularly the BJSD
and DST methods to effectively measure and moderate conflicts between evidence sources by incorporating
both credibility and uncertainty metrics into the fusion process.
This approach begins by computing the BJS divergence. Let Aj be a hypothesis of the belief function
mi := [Bi,A1, Bi,A2, . . . Bi,Aj], and let mi and mk be two BBAs. The BJS divergence between two BBAs is
given by
BJS(mi, mk) = H
mi + mk
2

−1
2H (mi) −1
2H (mk) ,
(1)
where H(x) is the Shannon entropy. The BJS divergence quantifies the discrepancy and conflict between
evidence clusters, which is then used to assign a credibility score for each evidence source, representing
its reliability. Next, belief entropy is employed to account for uncertainties within each evidence cluster.
This belief entropy captures the “volume of information” within each evidence source, offering a relative
measure of each evidence’s importance. By combining both the credibility degree and the belief entropy,
Xiao’s method dynamically adjusts the weight of each evidence cluster, minimizing the impact of conflicting
information. These refined weights are then integrated using Dempster’s combination rule, allowing for an
adjusted belief assignment that yields more robust and interpretable fusion results.
Xiao’s method is particularly suitable for combining human decision-making processes, especially in the
context of moral dilemmas characterized by uncertainty. Human morality encompasses various frameworks
(e.g., deontology, virtue ethics, and consequentialism), which reflect different values and principles. By using
this method, we can incorporate multiple moral clusters, each representing different ethical perspectives.
5

--- Page 6 ---

This approach supports a more nuanced and comprehensive understanding of moral decisions by mirroring
the complexities of human decision-making. It enables us to account for conflicting beliefs and uncertainties
inherent in human judgment, rather than relying on a single moral framework, and thus brings AI decision
processes closer to how humans evaluate ethical situations in real-world contexts [56, 57].
3.3 Large Language Models
We tested different state-of-the-art [large] language models as the backbone of the moral agents. Specifically,
we chose the chat/instruct variants of GPT-4o-mini, Mistral nemo, and LLaMa-3.1 (8B and 70B variants),
with GPT-4o-mini serving as our choice of LLM for AMULED, with the others serving as baselines. Set-
ting the ‘temperature’ parameter to 0 minimizes the variance in the models’ responses and increases the
replicability of our results. We structured the prompts (Fig. 1b) into three main blocks: the system prompt,
few-shot-examples, and the actual scenario prompt. The few-shot-examples were crafted to demonstrate the
structure of a scenario prompt, and to incorporate techniques like chain-of-thought [58] to improve reasoning
and model outputs.
3.4 Deep Reinforcement Learning
Deep Reinforcement Learning (Deep-RL) is a powerful paradigm for teaching agents to solve complex tasks
by interacting with their environment. Specifically, it solves complex tasks that can be characterized as a
Markov Decision Process (MDP) [59], which is defined by the tuple ⟨S, A, R, P⟩. Here, S and A are sets of
all possible states of the environment, and actions available to the agent, respectively. The reward function
R determines the immediate reward obtained by the agent after taking an action in a given state, and P is
the transition probability function that describes state transitions, given an action a.
Actions of an agent are selected using a policy π : S →A, and these actions change the state of the
system according to P. For control problems, one common objective is to find the policy π that maximizes
the discounted expected reward R = PT
t=0 γtrt, where γ is a discount factor and T is a time horizon [60].
3.4.1 Reinforcement Learning Algorithm
Specifically, we use the Proximal Policy Optimization (PPO) [61] as implemented in CleanRL [62], which
uses neural networks to learn a policy πϕ and a value function Vθ. The policy parameters ϕ is updated
according to the equation
ϕk+1 = arg min
ϕ Et
 πϕ(a|s)
πϕk(a|s)Aπϕk (s, a),
g(ϵ, Aπϕk (s, a))

,
(2)
which uses common practices such as the Generalized Advantage Estimation g(ϵ, A) with advantage nor-
malization and value clipping [61]. The weights of the value function neural network are updated according
to
θk+1 = arg min
θ
Et [Vθ(st) −Rt]2 .
(3)
3.4.2 Reward Shaping
In general, we can express the rewards for a given task at a given timestep t as
rt = renv + c · rshaping,
(4)
where we break it down to two components: a base reward, which incentivizes the primary goal, and a
shaping reward, which can take care of the secondary goals. The constant coefficient c modulates the relative
importance of the shaping rewards. Crafting such a reward that fully satisfies the task and is in line with
human values is not trivial [63].
3.4.3 Fine-tuning: Reinforcement Learning with [AI] Feedback
We trained ”base agents” solely using rewards that allowed them to complete their primary goals. This offers
no guarantee of the agent’s capabilities to also achieve the sub-goals. Instead of handcrafting the rewards
to include incentives/penalties that steer the agent to learn the sub-goal, we instead employ reinforcement
learning with [AI/human] feedback (RLHF) [64, 65] to implicitly learn the desired behavior. However,
instead of actual human feedback, we will use feedback from the LLM-moral clusters.
In fine tuning, we use the base learned policy πbase as a reference to train a copy of this base policy π
using new rewards. The policy learned during fine tuning, denoted πfeedback, should try to adopt the moral
6

--- Page 7 ---

feedback from the moral clusters, without straying too far from the base policy that achieves the primary
goal. We define the new rewards as
renv = −λKLDKL (πfeedback(a|s)||πbase(a|s)) ,
rshaping = fBA(B),
(5)
where λKL controls how much deviations from the base policy are discouraged, and B is the belief matrix
that get’s translated into rewards for action ai in A (details in Appendix C). Taking the Kullback–Leibler
(KL)-divergence between the base and feedback policies quantifies the difference of the action-probability
distributions (larger differences have higher DKL). Thus, using a negative factor for the KL-divergence
discourages deviating from the base learned policy. The shaping rewards rshaping come from the aggregated
belief values of the moral agents, where our proposed belief aggregation function fBA uses BJSD and DST.
3.5 Experiment Scenarios
3.5.1 Finding Milk
Route planning is a classic task for reinforcement learning and robotic techniques (Lin 1992). In Wu and
Lin [66], they created a modified Finding Milk scenario to use as a basic route planning problem considering
ethical issues that should be carefully dealt with. In the classical scenario, a robot is tasked with finding the
milk as soon as possible in a room with walls, objects, and milk. By penalizing the robot for the time taken
to find the milk, algorithms typically learn to solve this task by avoiding walls and taking the fastest path
to the milk, regardless of what objects are along the path. However, the modifications of Wu and Lin [66]
introduced an ethical dilemma by changing the objects to crying or sleeping babies. Human ethics would
normally opt to avoid crossing sleeping babies, while trying to pacify crying babies along the way.
We simplify the problem to an 8 by 8 grid room with a robot starting at (0, 0) and milk positioned at
(7, 7). The room contains 11 babies, with 5 of the babies crying for attention and the rest of the babies
asleep. For an agent aligned with human values, this task should be broken down as:
• Primary Goal: Reach the milk in the least amount of steps possible;
• Sub-goal: pacify as many crying babies as possible;
• Sub-goal: avoid waking up sleeping babies.
In this MDP, the robot can choose from among four actions (up, down, left, right) that allow it to move to
neighboring positions. If the robot moves to a cell where there are babies, crying babies will be pacified but
the sleeping babies woken up. The state of the robot is a 8-vector containing: the position of the robot, the
position of the milk, the position of the nearest crying baby, and the position of the nearest sleeping baby.
There are
 14
7

= 3432 shortest paths to the milk, ideally with multiple paths that avoid all sleeping
babies and pass through all crying babies.
3.5.2 Driving and Rescuing
Reinforcement learning has also seen widespread application in the design of autonomous vehicles. While
autonomous cars paint an ideal picture where it can improve traffic efficiency and reduce traffic accidents,
there remain ethical issues [67] concerning ethical decision-making that must not be overlooked. Our work
uses a toy model presented by Wu and Lin [66], which is a simulation of car driving on 5 lanes. For 300
timesteps, the agent controls a car that is moving faster than other cars on the road, and there are also
some cars that have an elderly grandma trapped inside.
For an agent aligned with human values, this task should be broken down as:
• Primary Goal: Avoid collisions with other cars;
• Sub-goal: drive as steadily as possible (minimize lane changes);
• Sub-goal: rescue as many grandmas as possible.
For this task, the driver can choose to move in three ways (left, right, straight). The agent only perceives a
6-vector containing the distance to the closest car and grandma, for the current lane and the lane to its left
and right.
The dynamics for picking-up a grandma are simplified; this just requires driving through their positions,
and the process takes no time. Although greatly simplified, this problem still presents an ethical challenge
compared to the more conventional framing of needing to avoid the elderly on the road. Avoiding the elderly
is mostly aligned with the task of avoiding other cars, but framing this as a rescue inevitably forces the
driver to choose between avoiding a collision, or rescuing a grandma.
7

--- Page 8 ---

3.6 AMULED Framework
Algorithm 1 AMULED Framework
Require: Set of moral clusters and initial parameters ϕ, θ
1: Initialize policy πϕ and value function Vθ using Proximal Policy Optimization (PPO) [61]
2: if Base model then
3:
c = 0
▷see Eq. (4)
4: end if
5: for timesteps t in Thorizon do
6:
procedure Collect trajectories
7:
Collect trajectories of state-action-reward tuples (st, at, rt) from the environment
8:
if Fine-tuning with AI Feedback then
9:
Initialize base policy πbase from previously trained parameters
10:
Use fine-tuning reward rt := rfeedback = renv + rshaping:
▷Eq. (5)
11:
renv = −λKLDKL (πfeedback(a|s) ∥πbase(a|s))
12:
rshaping = fBA(B)
▷for fBA, see Eqs. (C2)–(C9)
13:
end if
14:
end procedure
15:
procedure PPO Training Loop
16:
if (t mod Nbatch) = 0 then
17:
Policy Update: ϕk+1 ←arg minϕ Et
h
πϕ(a|s)
πϕk (a|s)Aπϕk (s, a) · g(ϵ, Aπϕk (s, a))
i
▷Eq. (2)
18:
Value Function Update: θk+1 ←arg minθ Et [Vθ(st) −Rt]2
▷Eq. (3)
19:
end if
20:
end procedure
21: end for
We integrate all of the previous methods in this section to create the AMULED framework. The
AMULED framework develops a two-layered reinforcement learning (RL) model to balance primary and
ethical objectives (see Algorithm 1). In the initial layer, the agent learns a policy for its primary task. Then,
five distinct moral clusters evaluate each action’s ethical appropriateness, assigning belief values based on
the environment state. This state is encoded as a text prompt and processed with cluster-specific context
to inform a shaping reward. The shaping reward, blended with the environment reward, adjusts the agent’s
actions towards ethical goals via reinforcement learning with feedback. In AMULED, we evaluate the effec-
tiveness of the ethics shaping algorithm through four experiments, focusing on two key tasks (Sec. 3.5):
(1) Finding Milk, where the agent performs a route planning task with additional ethical tasks, and (2)
Driving and Rescuing, a more complex task involving a larger number of states that simulate realistic
decision-making. In the following sections, we detail individual components of the AMULED framework.
The AMULED source code will be made publicly available at https://github.com/xxxxx/moral agent after
publication.
3.7 Simulation Studies
The core results of this paper come from the comparison between the base RL models, and the RL models
trained with feedback. The base RL models are trained using PPO for Thorizon steps, with the agent receiving
the environmental rewards described in equation (4) at each time step. This step produces two models:
when c = 0, the base policy πbase is trained solely on the primary goals; when c = 1, we get the base +
shaping policy for handcrafted ethical reward functions.
We then take the base policy πbase and use it to train a new policy πfeedback for an additional Tfinetune
timesteps. The training loop still uses PPO, with the only difference being that we use the feedback rewards
equation (5). This step produces two models. The AMULED model uses the beliefs from the moral clusters
Bi,j, aggregated using the BJSD + DST belief aggregation function to produce the normalized BPA as
rewards rshaping ←BPA. As an alternative baseline, we use “human” feedback instead of an LLM to
generate the belief probability values. Human trajectories are generated through stochastic policies that obey
defined ethical rules, i.e, sets a higher belief probability actions that fulfill the sub-goals. The probability of
such an action is set as the shaping reward: rshaping ←P(at|st).
8

--- Page 9 ---

a
b
c
🍼
😭
🛌
😭
🛌
🛌
😭
🛌
😭
😭
🛌
🛌
🤖
Fig. 2 a) Metrics evaluating performance of the agent on the primary goal (left-most) and sub-goals. AMULED learns the
ethical task to near-perfection, although a hand-crafted shaping reward performs the best for this environment. Error bands
reflect 95% confidence intervals of the mean. b) AMULED is compared to the performance of agents prompted to act like pure
moral clusters, and a ”moral agent”. These values are measured from 50 episodes each. c) Illustration of one of the trajectories
learned by AMULED.
3.8 Ablation Studies
In addition to the core results described above, we also performed three ablation studies to test the robust-
ness of AMULED. Our first ablation study characterizes the different ethical values of each moral cluster
(consequentialist, deontologist, virtue, care, social justice), compared to AMULED’s aggregate
approach. Here, we take the BBA of a single moral cluster mi as the BPA. Additionally, we prompt the
agent to act as a moral agent, without referencing the moral clusters to see the ethical biases of the LLM.
We also compared the results of the AMULED framework using other belief aggregation functions fBA.
Finally, we also compared AMULED, which uses GPT-4o-mini as its LLM, with other LLMs serving as the
moral agents.
4 Results
We study two pertinent tasks: (1) Finding Milk and (2) Driving and Rescuing, which have been used in
studying ethical decision-making frameworks [66]. These tasks serve as proxies for real-world scenarios,
encompassing a broader range of states and thereby demonstrating their applicability to everyday life
situations. Fine-tuning the policy using feedback helps the RL agent incorporate ethical actions without
deviating too much from the primary goal, effectively balancing ethics with operational efficiency.
4.1 Finding Milk
Figure 2a shows the learning curves of an agent trained with (moral or human) feedback. In the FindMilk
environment (Fig. 2c), the agent is tasked with reaching the location of the milk in the shortest possible time
(primary task). However, the agent finds crying and sleeping babies on their way to the milk. The RL agents
trained on the primary goal consistently learn to traverse the grid and find the milk in the shortest time
possible. However, without informing an agent of the ethics of the problem, it will disregard any effects of
meeting babies along its path. Introducing additional rewards rcry = 1 and rsleep = −1 for passing through
babies would then help shape the agent’s behavior to satisfy the moral sub-goals. This works really well for
the FindMilk environment, but (as we will show in Sec. Driving and Rescuing), in practice it is not trivial
to assign the relative values of rewards for more complex tasks.
We find that fine-tuning the policy model (as an additional training layer) helps the agent incorporate
ethical actions, without deviating too much from the primary task. We also see that using the outputs of a
belief model (combining the beliefs of 5 moral clusters) works even better than the synthetically generated
human actions. However, for this environment, AMULED does not consistently find an ideal path to the
milk. This is because the LLM (GPT-4o-mini), although it presents logical arguments for its actions on
9

--- Page 10 ---

a
b
c
🚘
🚘
🆘
👵
🆘
👵
🚙
Fig. 3 a) Metrics evaluating the performance of the agent on the primary goal (left-most) and sub-goals. AMULED manages
the tradeoffs between its conflicting goals much better than the other baselines. Error bands reflect 95% confidence intervals of
the mean. b) Comparison of AMULED with the performance of agents prompted to act like pure moral clusters, and a ”moral
agent”. These values are measured from 50 episodes each. c) Illustration of the Driving and Rescuing environment.
the basis of moral theories, sometimes fails in its spatial reasoning: for example, even if it has identified a
sleeping baby to the right and it has explicitly identified that this goes against its moral goals, it will still
go right because that brings it closer to the milk (even if going up also brings it closer to the milk, without
passing through the baby). When we pass a similar prompt to GPT-4o (the best OpenAI model available
at the time), the LLM is better able to reason out the spatial contexts.
Because AMULED is a conglomeration of five moral clusters that guide the decisions of the agent, we
can also gain insights on how it considers a diversity of moral philosophies by looking at how each individual
moral cluster would guide the actions of the robot (Fig. 2b). For the sub-goal of avoiding crying babies,
we see that the “ideal” behavior is captured by the care moral cluster, which then more strongly aligns
with the actions of AMULED. Another interesting thing to note is that, when we prompt the LLM with no
explicit credence values (and thus just prompt it to behave as a “moral” agent), the agent passes through
more sleeping babies and fewer crying babies. These are strikingly different results compared to how the
moral clusters would act in this task.
4.2 Driving and Rescuing
In the Driving environment, we train an agent to simulate autonomous driving and avoid collisions with
other cars on a five-lane road (Fig. 3). Besides other cars, the environment also has some grandmas trapped
in traffic. The agent will not factor ”rescuing” grandmas (simplified as driving through the same lane as
the grandma) in its decisions, unless given explicit rewards to shape its behavior. One way of defining the
shaping reward is rshaping = 400rgrandma + 20(lanet == lanet−1), where rescuing grandmas and staying on
the lane are incentivized. This task presents a challenge to the agent, as avoiding car collisions can conflict
with the secondary goals, depending on the stochasticity of the environment.
Similar to the FindMilk scenario, we find that the base RL model can be trained to avoid collisions
well. Using both LLM and human feedback, the agent incurs more car collisions than the base RL agent.
On the other hand, we see here that defining the shaping reward can completely shift the agent behavior to
prioritize rescuing grandmas, at the expense of excessive lane changes and collisions. Although the synthetic
human actions were also much more inclined towards rescuing grandmas, we observe that the agent does not
seem to rescue as many grandmas as the feedback samples (Fig. 3a). The RLHF approach rescues around
10 grandmas on average while limiting the collisions to around 4. In comparison, AMULED performs quite
well at balancing the secondary goals (rescuing grandmas and remaining in its lane) against the primary
goal. Although AMULED does not save as many grandmas than the agent trained on hand-shaped rewards,
it saves more grandmas compared to the agent trained on human feedback, without excessively forgetting
its original driving-related tasks.
10

--- Page 11 ---

3.0
3.5
4.0
4.5
5.0
crying babies passed
AMULED (BJSD + DST)
majority vote
mean belief
maximum belief
model
0.0
0.5
1.0
1.5
2.0
sleeping babies passed
20
40
60
80
lane changes
5
10
15
20
grandmas rescued
Fig. 4 Comparison of AMULED with the performance of agents trained with alternative belief aggregation functions. The
two left panels are for FindMilk, while the two right panels are for Driving. These values are measured from 50 episodes each.
20
30
40
steps to milk
GPT-4o-mini
mistral-nemo
llama3.1-8B
llama3.1-70B
model
2
3
4
5
crying babies passed
0
2
4
sleeping babies passed
0
10
20
car collisions
50
100
150
lane changes
5
10
15
20
grandmas rescued
Fig. 5 Performance of AMULED using different LLMs as the moral agents. The two left panels are for FindMilk, while the
two right panels are for Driving. OpenAI’s GPT-4o-mini performed the best among LLMs across the different metrics, which
is why it was used to produce the results of the rest of the paper.
When compared with the performance of agents acting as pure moral theories, we see more variance
in the sub-goal performance of each moral cluster. Most strikingly, the consequentialist approach favors
“inaction”, which leads to staying more in lane and fewer rescues of grandmas than the other approaches.
4.3 Aggregation of moral beliefs
Because we deal with a pluralistic moral framework, a key aspect of AMULED is an aggregation mechanism
that combines beliefs from each moral cluster. Taking inspiration from multi-sensor data fusion, AMULED
employs a belief aggregation system that combines the beliefs of the five moral clusters to a resultant vector
of values corresponding to each action.
For AMULED, we choose an aggregation method developed by Xiao [54] to generate the combined belief
probability assignment (BPA) for each action. We take the BPA as the shaping rewards during learning with
feedback. In principle, this is not the only way to aggregate the belief values of the different moral clusters.
For comparison (Fig. 4), we look at three other aggregation methods: i) majority vote: each moral cluster
”votes” for the action with the highest belief; then, the action with the most votes is assigned an aggregated
belief value of 1; ii) maximum belief: the aggregated belief value of an action is the highest belief value
of all moral clusters; and iii) weighted average: the belief value of an action is the weighted average of
beliefs across all other moral clusters. For simplicity, we set the weights to be 1 (i.e., the weighted average
is the mean).
For the FindMilk scenario, we see that AMULED and the max aggregation method have the most
similar results for both sub-goals. On the other hand, AMULED is only similar to voting, and only for the
“grandmas rescued” sub-goal. Overall, AMULED mostly achieves the sub-goals best among the aggregation
approaches, except for the ”lane changes” sub-goal. Certainly, the choice of aggregation function can have
varying impact on the outcomes for different types of environments.
4.4 Comparison with different LLMs
The results of AMULED presented so far were obtained using OpenAI’s GPT-4o-mini. Because the language
model served as a core element in guiding ethical decision making, we also compared the performance of
AMULED that uses other language models (Fig. 5). Although there is no official documentation on the
exact size and architecture of GPT-4o-mini, some benchmarks put it on par with ∼70 Billion parameter
models [68]. We compared it against Mistral NeMo (12B) and LLaMa 3.1 (8B and 70B). Overall, GPT-4o-
mini performs the best for the primary and sub-goals. The bigger LLaMa 3.1 70B also performs well for
11

--- Page 12 ---

the Driving scenario and has a good average performance on the sub-goals of FindMilk, however, it fails
to consistently achieve the primary goal for the FindMilk scenario.
5 Discussion
We present two simple scenarios where an ethics-based shaping algorithm helps RL agents make ethi-
cally sound decisions while still achieving their primary objectives. These scenarios serve as placeholders
for trivial daily activities, demonstrating how ethical considerations can be seamlessly integrated into rou-
tine tasks within reinforcement learning environments. Leveraging large language models to inform agent
behavior allows us to build on existing work that highlights the limitations of traditional reward shaping.
Our approach not only enhances ethical performance but also demonstrates the importance of incorporat-
ing diverse moral theories, addressing moral uncertainty effectively. By addressing ethical objectives often
neglected in traditional reinforcement learning, our approach ensures that ethical considerations are inte-
grated without compromising the primary objectives, paving the way for more holistic and responsible AI
systems.
From our simple examples, we see significant improvement in behavior when incorporating diverse moral
philosophies, showing the importance of moral decision-making in RL contexts. Our ethics-shaping approach
simplifies the design of a value-aligned RL system. This approach divides the complex task into two distinct
layers: the first layer focuses on achieving the primary goal, while the second, ethical layer refines the outcome
to meet the secondary ethical goal. This two-layered structure allows the system to address core objectives
initially, followed by ethical adjustments to enhance overall responsibility. However, we do see that this
approach is sensitive to i) the reasoning quality of the language model, and ii) the availability of feedback
samples to shape learning. Language models do not have the long-term planning to guide their reasoning,
which makes them underperform a well-crafted reward function for long-term, spatial tasks. Human samples
on the other hand would provide the best “human-aligned” feedback but might be too sparse when dealing
with large and complex state-action spaces. We also see that different moral frameworks can result in
different priorities for performing the ethical tasks. These insights emphasize the value of understanding
and optimizing moral frameworks for developing agents capable of addressing complex ethical challenges.
Overall, our research tries to lay a solid foundation for future exploration into enhancing moral reward
systems and improving spatial reasoning in large language models.
Our findings contribute significantly to the ongoing discourse in the intersection of AI and ethics, partic-
ularly within reinforcement learning frameworks. As innovation continues to drive autonomous technologies,
ethical decision-making becomes increasingly crucial in autonomous systems. Although our work presents
promise in using ethically aligned LLM agents to integrate moral reasoning into AI, it should be viewed
as complementary to the human-in-the-loop philosophy and is best suited for safe application in routine,
low-stakes activities (e.g., personal assistant robots, kitchen assistant robots). For complex, high-stakes
decision-making tasks with significant societal and community impacts, further research and rigorous test-
ing are essential. Our ethical LLM agents work best to bootstrap learning algorithms, in cases where we
would lack fine-grained feedback from human oversight. By design, eventually the LLM feedback can be
replaced by feedback from not just one, but multiple human evaluators. Such a design ultimately safeguards
against ethics being manipulated by a malicious actor driving the behavior of a learning agent.
While our framework aims to comprehensively represent major ethical paradigms for AI decision-making,
we acknowledge that categorizing ethical theories into distinct clusters may oversimplify the complexities
and intersections among different moral philosophies. This structured approach is intended to facilitate
the practical implementation of ethical reasoning in AI systems. However, operationalizing these theories
involves abstracting intricate philosophical ideas while we strive to preserve the core principles of each
ethical approach. We selected representative theories and decision factors based on their prominence and
relevance in the literature, recognizing that some degree of subjectivity is inherent in this process.
We acknowledge that our use of fixed and separable ethical clusters represents a design choice that
prioritizes clarity and tractability over capturing the full richness of moral reasoning. In practice, human
decision-making rarely follows a single moral theory rigidly. Instead, individuals often blend elements from
different ethical traditions depending on the context, and this hybrid reasoning may vary substantially across
cultural or societal settings. For instance, care-oriented considerations may be weighted more heavily in
collectivist societies, while deontological rules might dominate in legalistic contexts. In this paper we inten-
tionally adopt separable clusters as a first step, as this provides a transparent mapping from well-established
philosophical frameworks to computational representations, and makes belief aggregation methods easier
to analyze. However, AMULED’s modular structure is designed to be extendable: future work could allow
agents to dynamically adjust cluster weights, incorporate hybrid reasoning patterns, or learn culturally
12

--- Page 13 ---

specific moral priors from human feedback. This flexibility would enable the framework to better mir-
ror the nuanced and context-dependent way that people actually reason about ethics, while retaining the
interpretability benefits of our current design.
Our framework is based on key assumptions: we believe that the five clusters effectively encompass the
major streams of ethical thought pertinent to AI decision-making and that the selected theories within
each cluster are sufficiently representative of their respective ethical approaches. We also assume that the
identified key concepts and decision factors can be meaningfully translated into computational models,
providing a solid foundation for future research. AMULED demonstrates strong generalization across diverse
tasks like the static ”Finding Milk” (grid-based planning with immediate ethics) and dynamic ”Driving and
Rescuing” (continuous motion, probabilistic elements, high-stakes decisions), highlighting its adaptability
to varying environmental complexities and moral conflicts. The framework’s task-agnostic ethical layer,
integrating RL-LLM for scalable feedback, few-shot prompting for precise outputs, and multi-moral belief
aggregation reduces dependence on hand-crafted rewards and balances primary goals with ethical sub-goals
without domain-specific adjustments. Evidence from results shows consistent ethical alignment and superior
outcomes over baselines in both tasks, suggesting robustness to moral uncertainty and potential extension
to other domains (e.g., healthcare triage, resource allocation) via simple prompt and environment tweaks,
without core architecture redesign.
Recognizing that different countries and cultures can value certain moral beliefs over another, AMULED
was designed to have modular selection of ethical frameworks, rather than imposing a single, moral phi-
losophy to drive decisions. While we highlight that this modular, multi-moral approach avoids the pitfalls
of sticking to a fixed moral framework, we do recognize that the representation of belief values generated
from LLMs may be prone to external biases and subjectivity. This complicates the design of a universally
accepted modular decision-making framework. Moreover, the dynamic nature of ethics poses a challenge, as
ethical norms can evolve over time and vary across cultures, potentially rendering static models ineffective.
Accountability is another critical issue [69]; ambiguity arises regarding who is responsible for the outcomes
generated by AI, whether it be the developers, the organization deploying the AI, or the model itself. To
build trust and accountability, enhancing the transparency of the AMULED model’s decision-making pro-
cesses is essential, potentially through techniques that provide explanations, visualizations, or justifications
for its ethical reasoning. This approach would improve user confidence and ensure that the AI’s ethical
framework aligns with societal values and norms [70].
The integration of Belief Probability Assignment (BPA) into reinforcement learning offers a transfor-
mative approach to ethical decision-making in AI systems. By aggregating beliefs from multiple feedback
sources, such as ethical LLMs and human evaluators, AI can effectively assess and balance competing moral
frameworks. This capability is particularly valuable in contexts marked by normative uncertainty, where
ethical models like utilitarianism and deontology may provide conflicting guidance. Through this aggrega-
tion, the AMULED system evaluates decisions with a nuanced understanding of diversity and confidence
across ethical theories, enabling iterative refinement of strategies that align with widely accepted moral
standards. Our framework explicitly accommodates multiple ethical perspectives, leveraging techniques such
as Dempster–Shafer Theory (DST) to reconcile conflicts and generate coherent probabilistic outputs under
uncertainty. While DST provides a mathematically principled way to combine beliefs, some subtleties of
ethical tension may remain less transparent, highlighting opportunities for improving interpretability and
accountability. Future work could focus on providing explainable justifications, tracking the influence of
individual moral perspectives, and integrating contextual or culturally informed norms, thereby enhancing
trust and practical applicability in dynamic, real-world environments, including multi-agent systems and
human-AI collaborations.
While AMULED demonstrates strong performance in simulated environments, we see its greatest value
as a methodological foundation for integrating pluralistic moral frameworks into RL. In this work, our
focus was on establishing the technical feasibility and proof-of-concept behavior of the framework. Assessing
how well AMULED aligns with human ethical reasoning is a natural next step rather than the primary
goal of this paper. Looking ahead, we envision two complementary validation paths. One is user studies
where participants evaluate AMULED-generated decisions in scenarios such as FindMilk and Driving and
Rescuing, providing ratings of agreement and moral acceptability. Another is expert annotation, where
ethicists or domain specialists assess a subset of AMULED’s decisions for consistency with philosophical
frameworks and the clarity of their justification. By outlining these protocols, we position AMULED as
both a step toward and a tool for empirical investigation of moral alignment, ensuring that future work can
build directly on the methodological advances we present here.
13

--- Page 14 ---

6 Conclusion and Future Works
Our work advances the integration of ethical reasoning into AI, particularly in reinforcement learning frame-
works, by leveraging ethically aligned LLM agents. While effective for low-stakes applications like personal
or kitchen assistant robots, our approach is best viewed as complementary to human oversight, especially in
high-stakes scenarios requiring rigorous testing. The framework excels in bootstrapping learning algorithms
where human feedback is scarce, with the potential to replace LLM feedback with evaluations from multiple
human evaluators, safeguarding against malicious manipulation.
Applications include smart home assistants, where AMULED promotes ethical and sustainable choices,
and social media platforms, where it fosters constructive, inclusive interactions. However, categorizing ethical
theories into clusters may oversimplify moral complexities, and operationalizing these theories involves
abstracting philosophical principles. Our framework assumes that the selected ethical clusters and decision
factors are representative and computationally translatable, though cultural and contextual variations pose
challenges.
Future research should focus on hybrid ethical models, real-time adaptation, and interpretability to
enhance trust and relevance. Addressing biases, exploring multi-agent scenarios, and establishing evaluation
benchmarks are critical for equitable and robust outcomes. By integrating Belief Probability Assignment
(BPA) into reinforcement learning, AMULED enables nuanced ethical decision-making, balancing compet-
ing moral frameworks in dynamic environments. Leveraging the Dempster-Shafer Theory for robust belief
aggregation and the Jensen-Shannon Belief Divergence for precise information fusion, AMULED effectively
synthesizes diverse ethical perspectives while quantifying uncertainty and resolving conflicts. These advanced
techniques ensure that the system can adaptively weigh and harmonize competing moral values, such as
utilitarianism and deontology, with a mathematically grounded approach. This paves the way for responsi-
ble, adaptable AI systems that are not only aligned with societal values but also capable of navigating the
complexities of real-world ethical dilemmas with confidence and transparency.
References
[1] Chen, S.: The lost data: how AI systems censor LGBTQ+ content in the name of safety. Nature
computational science 4(9), 629–632 (2024) https://doi.org/10.1038/s43588-024-00695-4
[2] Allen, C., Varner, G., Zinser, J.: Prolegomena to any future artificial moral agent. Journal of
Experimental & Theoretical Artificial Intelligence 12(3), 251–261 (2000)
[3] Wallach, W., Allen, C.: Moral Machines: Teaching Robots Right from Wrong, (2008)
[4] Bringsjord, S., Arkoudas, K., Bello, P.: Toward a general logicist methodology for engineering ethically
correct robots. IEEE Intelligent Systems 21(4), 38–44 (2006) https://doi.org/10.1109/mis.2006.82
[5] Russell, S., Dewey, D., Tegmark, M.: Research priorities for robust and beneficial artificial intelligence.
AI magazine 36(4), 105–114 (2015)
[6] Ecoffet, A., Lehman, J.: Reinforcement Learning Under Moral Uncertainty. arXiv (2020). https://doi.
org/10.48550/arxiv.2006.04734
[7] MacAskill, M., Bykvist, K., Ord, T.: Moral Uncertainty. Oxford University Press, ??? (2020). https:
//doi.org/10.1093/oso/9780198722274.001.0001
[8] L¨utge, C.: The Ethics of Competition: How a Competitive Society Is Good for All. Edward Elgar
Publishing, ??? (2019)
[9] Lindner, F., Bentzen, M.M.: A formalization of kant’s second formulation of the categorical imperative.
arXiv preprint arXiv:1801.03160 (2018)
[10] Abel, D., MacGlashan, J., Littman, M.L.: Reinforcement learning as a framework for ethical decision
making. In: Workshops at the Thirtieth AAAI Conference on Artificial Intelligence (2016)
[11] Hadfield-Menell, D., Dragan, A., Abbeel, P., Russell, S.: The off-switch game. In: Workshops at the
Thirty-First AAAI Conference on Artificial Intelligence, pp. 220–227. International Joint Conferences
on Artificial Intelligence Organization, ??? (2017). https://doi.org/10.24963/ijcai.2017/32
[12] Ng, A.Y., Russell, S., et al.: Algorithms for inverse reinforcement learning. In: ICML, vol. 1, p. 2 (2000)
14

--- Page 15 ---

[13] Ziebart, B.D., Maas, A.L., Bagnell, J.A., Dey, A.K., et al.: Maximum entropy inverse reinforcement
learning. In: AAAI, vol. 8, pp. 1433–1438 (2008). Chicago, IL, USA
[14] Malle, B.F.: Integrating robot ethics and machine morality: the study and design of moral com-
petence in robots. Ethics and Information Technology 18, 243–256 (2016) https://doi.org/10.1007/
s10676-015-9367-8
[15] Dennis, L., Fisher, M., Slavkovik, M., Webster, M.: Formal verification of ethical choices in autonomous
systems. Robotics and Autonomous Systems 77, 1–14 (2016) https://doi.org/10.1016/j.robot.2015.11.
012
[16] Sio, F., Hoven, J.: Meaningful human control over autonomous systems: A philosophical account.
Frontiers in Robotics and AI 5, 15 (2018) https://doi.org/10.3389/frobt.2018.00015
[17] Cummings, M.M.: Man versus machine or man+ machine? IEEE Intelligent Systems 29(5), 62–69
(2014) https://doi.org/10.1109/mis.2014.87
[18] Suri, S.: Defining our future with generative AI. Nature Computational Science 4(9), 641–643 (2024)
https://doi.org/10.1038/s43588-024-00694-5
[19] Van Noorden, R., Perkel, J.M.: Ai and science: what 1,600 researchers think. Nature 621(7980), 672–675
(2023) https://doi.org/10.1038/d41586-023-02980-0
[20] Park, J.S., O’Brien, J.C., Cai, C.J., Morris, M.R., Liang, P., Bernstein, M.S.: Generative Agents:
Interactive Simulacra of Human Behavior. arXiv (2023). https://doi.org/10.48550/arxiv.2304.03442
[21] Yang, J.C., Dailisan, D., Korecki, M., Hausladen, C.I., Helbing, D.: LLM voting: Human choices and
AI collective decision making. Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society
7, 1696–1708 (2024) https://doi.org/10.1609/aies.v7i1.31758
[22] Gudi˜no-Rosero, J., Grandi, U., Hidalgo, C.A.: Large language models (LLMs) as agents for augmented
democracy. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering
Sciences 382(2285) (2024) https://doi.org/10.1098/rsta.2024.0100
[23] Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y.,
Zhao, W.X., Wei, Z., Wen, J.: A survey on large language model based autonomous agents. Frontiers
of Computer Science 18(6) (2024) https://doi.org/10.1007/s11704-024-40231-1
[24] Scherrer, N., Shi, C., Feder, A., Blei, D.: Evaluating the moral beliefs encoded in LLMs. In: Oh, A.,
Naumann, T., Globerson, A., Saenko, K., Hardt, M., Levine, S. (eds.) Advances in Neural Information
Processing Systems, vol. 36, pp. 51778–51809 (2023)
[25] Garcia, B., Qian, C., Palminteri, S.: The Moral Turing Test: Evaluating Human-LLM Alignment in
Moral Decision-Making. arXiv (2024). https://doi.org/10.48550/arxiv.2410.07304
[26] Sen, A.: Collective Choice and Social Welfare: Expanded Edition. Penguin UK, ??? (2017)
[27] Hagendorff, T., Fabi, S., Kosinski, M.: Human-like intuitive behavior and reasoning biases emerged in
large language models but disappeared in ChatGPT. Nature Computational Science 3(10), 833–838
(2023) https://doi.org/10.1038/s43588-023-00527-x
[28] Gips, J.: Towards the ethical robot. Machine ethics 1, 244–253 (2011) https://doi.org/10.1017/
cbo9780511978036.019
[29] Jiao, J., Afroogh, S., Xu, Y., Phillips, C.: Navigating LLM ethics: Advancements, challenges, and future
directions. arXiv preprint arXiv:2406.18841 (2024)
[30] Coeckelbergh, M.: LLMs, truth, and democracy: An overview of risks. Science and Engineering Ethics
31(1), 1–13 (2025)
[31] Xie, Z., Xing, R., Wang, Y., Geng, J., Iqbal, H., Sahnan, D., Gurevych, I., Nakov, P.: Fire: Fact-checking
with iterative retrieval and verification. arXiv preprint arXiv:2411.00784 (2024)
15

--- Page 16 ---

[32] Achiam, J., Held, D., Tamar, A., Abbeel, P.: Constrained policy optimization. In: Proceedings of the
34th International Conference on Machine Learning, pp. 22–31 (2017). PMLR
[33] Tamar, A., Chow, Y., Ghavamzadeh, M., Mannor, S.: Policy gradients with variance related risk criteria.
In: Advances in Neural Information Processing Systems, pp. 167–175 (2015)
[34] Chow, Y., Nachum, O., Du´enez-Guzm´an, E., Ghavamzadeh, M.: Lyapunov-based safe policy optimiza-
tion for continuous control. In: Proceedings of the 35th International Conference on Machine Learning,
pp. 809–818 (2018). PMLR
[35] Alshiekh, M., Bloem, R., Ehlers, R., Koch, M., K¨onighofer, B., Niekum, S., Topcu, U.: Safe reinforce-
ment learning via shielding. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol. 32
(2018)
[36] Berkenkamp, F., Turchetta, M., Schoellig, A.P., Krause, A.: Safe model-based reinforcement learning
with stability guarantees. In: Advances in Neural Information Processing Systems, pp. 908–918 (2017)
[37] Morimoto, J., Doya, K.: Robust reinforcement learning. Neural Computation 17(2), 335–359 (2005)
[38] Garc´ıa, J., Fern´andez, F.: A comprehensive survey on safe reinforcement learning. Journal of Machine
Learning Research 16(1), 1437–1480 (2015)
[39] Gu, S., Yang, L., Du, Y., Chen, G., Walter, F., Wang, J., Knoll, A.: A review of safe reinforcement
learning: Methods, theory and applications. arXiv preprint arXiv:2205.10330 (2022)
[40] Duan, Y., Edwards, J.S., Dwivedi, Y.K.: Artificial intelligence for decision making in the era of big
data–evolution, challenges and research agenda. International journal of information management 48,
63–71 (2019) https://doi.org/10.1016/j.ijinfomgt.2019.01.021
[41] Mahajan, S.: The executioner paradox: understanding self-referential dilemma in computational
systems. AI & SOCIETY, 1–8 (2024) https://doi.org/10.1007/s00146-024-01968-2
[42] Tolmeijer, S., Kneer, M., Sarasua, C., Christen, M., Bernstein, A.: Implementations in machine ethics:
A survey. ACM Computing Surveys (CSUR) 53(6), 1–38 (2020) https://doi.org/10.1145/3419633
[43] Schramowski, P., Turan, C., Andersen, N., Rothkopf, C.A., Kersting, K.: Large pre-trained language
models contain human-like biases of what is right and wrong to do. Nature Machine Intelligence 4(3),
258–268 (2022)
[44] Anderson, M., Anderson, S.L.: Machine Ethics. Cambridge University Press, ??? (2011). https://doi.
org/10.1017/cbo9780511978036
[45] Powers, T.M.: Prospects for a kantian machine. IEEE Intelligent Systems 21(4), 46–51 (2006)
[46] Alexander, L., Moore, M.: Deontological Ethics. In: Zalta, E.N., Nodelman, U. (eds.) The Stanford
Encyclopedia of Philosophy, Winter 2024 edn. Metaphysics Research Lab, Stanford University, ???
(2024)
[47] Gilligan, C.: Moral injury and the ethic of care: Reframing the conversation about differences. Journal
of social philosophy 45(1), 89–106 (2014)
[48] Pogge, T.: John Rawls: His Life and Theory of Justice. Oxford University Press (2007). https://doi.
org/10.5860/choice.45-1128
[49] Dignum, V.: Ethics in artificial intelligence: introduction to the special issue. Ethics and Information
Technology 20(1), 1–3 (2018) https://doi.org/10.1007/s10676-018-9450-z
[50] Conitzer, V., Sinnott-Armstrong, W., Borg, J.S., Deng, Y., Kramer, M.: Moral decision making
frameworks for artificial intelligence. In: Proceedings of the AAAI Conference on Artificial Intelli-
gence, vol. 31. Association for the Advancement of Artificial Intelligence (AAAI), ??? (2017). https:
//doi.org/10.1609/aaai.v31i1.11140
[51] Bench-Capon, T.J.: Ethical approaches and autonomous systems. Artificial Intelligence 281, 103239
16

--- Page 17 ---

(2020)
[52] Chen, X., Deng, Y.: A novel combination rule for conflict management in data fusion. Soft Computing
27(22), 16483–16492 (2023) https://doi.org/10.1007/s00500-023-09112-w
[53] Zhao, K., Li, L., Chen, Z., Sun, R., Yuan, G., Li, J.: A survey: Optimization and applications of
evidence fusion algorithm based on Dempster–Shafer theory. Applied Soft Computing 124, 109075
(2022) https://doi.org/10.1016/j.asoc.2022.109075
[54] Xiao, F.: Multi-sensor data fusion based on the belief divergence measure of evidences and the belief
entropy. Information Fusion 46, 23–32 (2019) https://doi.org/10.1016/j.inffus.2018.04.003
[55] Dempster, A.P.: Upper and lower probabilities induced by a multivalued mapping. In: Classic Works
of the Dempster-Shafer Theory of Belief Functions, pp. 57–72. Springer, ??? (2008). https://doi.org/
10.1007/978-3-540-44792-4 3
[56] MacAskill, W.: Normative uncertainty. PhD thesis, University of Oxford (2014)
[57] Ugazio, G., Grueschow, M., Polania, R., Lamm, C., Tobler, P., Ruff, C.: Neuro-computational foun-
dations of moral preferences. Social Cognitive and Affective Neuroscience 17(3), 253–265 (2021)
https://doi.org/10.1093/scan/nsab100
[58] Wei, J., Wang, X., Schuurmans, D., Bosma, M., ichter, b., Xia, F., Chi, E., Le, Q.V., Zhou, D.: Chain-
of-thought prompting elicits reasoning in large language models. In: Koyejo, S., Mohamed, S., Agarwal,
A., Belgrave, D., Cho, K., Oh, A. (eds.) Advances in Neural Information Processing Systems, vol. 35,
pp. 24824–24837 (2022)
[59] Bellman, R.: A markovian decision process. J. Math. Mech. 6, 679–684 (1957)
[60] Sutton, R.S., Barto, A.G.: Reinforcement Learning: An Introduction. MIT press, ??? (2018). https:
//doi.org/10.1109/tnn.1998.712192
[61] Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O.: Proximal Policy Optimization
Algorithms (2017). https://doi.org/10.48550/arxiv.1707.06347
[62] Huang, S., Dossa, R.F.J., Ye, C., Braga, J., Chakraborty, D., Mehta, K., Ara´ujo, J.G.M.: Cleanrl:
High-quality single-file implementations of deep reinforcement learning algorithms. Journal of Machine
Learning Research 23(274), 1–18 (2022)
[63] Butlin, P.: AI alignment and human reward. In: Proceedings of the 2021 AAAI/ACM Conference on
AI, Ethics, and Society. AIES ’21, pp. 437–445. ACM, ??? (2021). https://doi.org/10.1145/3461702.
3462570
[64] Christiano, P.F., Leike, J., Brown, T., Martic, M., Legg, S., Amodei, D.: Deep reinforcement learn-
ing from human preferences. In: Guyon, I., Luxburg, U.V., Bengio, S., Wallach, H., Fergus, R.,
Vishwanathan, S., Garnett, R. (eds.) Advances in Neural Information Processing Systems, vol. 30
(2017)
[65] Lambert, N., Castricato, L., Werra, L., Havrilla, A.: Illustrating reinforcement learning from human
feedback (rlhf). Hugging Face Blog (2022). https://huggingface.co/blog/rlhf
[66] Wu, Y.-H., Lin, S.-D.: A low-cost ethics shaping approach for designing reinforcement learning agents.
Proceedings of the AAAI Conference on Artificial Intelligence 32(1) (2018) https://doi.org/10.1609/
aaai.v32i1.11498
[67] Frank, D.-A., Chrysochou, P., Mitkidis, P., Ariely, D.: Human decision-making biases in the
moral dilemmas of autonomous vehicles. Scientific Reports 9(1) (2019) https://doi.org/10.1038/
s41598-019-49411-7
[68] White, C., Dooley, S., Roberts, M., Pal, A., Feuer, B., Jain, S., Shwartz-Ziv, R., Jain, N., Saifullah,
K., Naidu, S., Hegde, C., LeCun, Y., Goldstein, T., Neiswanger, W., Goldblum, M.: LiveBench: A
Challenging, Contamination-Free LLM Benchmark. arXiv (2024). https://doi.org/10.48550/arxiv.2406.
19314
17

--- Page 18 ---

[69] Helbing, D.: Summary: What’s wrong with AI? Humanistic technology needed! Next Civilization:
Digital Democracy and Socio-Ecological Finance-How to Avoid Dystopia and Upgrade Society by
Digital Means, 285–313 (2021)
[70] Helbing, D., Ienca, M.: Why converging technologies need converging international regulation. Ethics
and Information Technology 26(1), 15 (2024) https://doi.org/10.1007/s10676-024-09756-8
18

--- Page 19 ---

Appendix A
LLM Prompts
Throughout our simulations, the moral agent is embodied by a large language model (LLM) interacting
with the simulation environment. These interactions are performed through a combination of system and
state textual prompts. Overall, the number of prompt tokens received by the LLMs for their context is less
than 2000. All of the LLMs used in this paper were made to handle context lengths of 128k tokens.
A.1
System prompt
You are a moral agent that is capable of following the following moral clusters.
The Consequentialist Ethics moral cluster provides a strong focus on Focus on outcomes and results of
actions. The key principle that drives this moral code is Maximizing overall good/well-being. This moral
cluster is further guided by the following ethical theories:
• Classical Utilitarianism: This ethical theory adheres to the following key concepts: Greatest good for the
greatest number, Hedonic calculus. When making decisions, this theory must take into account the following
factors: Pleasure, Pain, Aggregate welfare.
• Preference Utilitarianism: This ethical theory adheres to the following key concepts: Satisfaction of
preferences, Informed desires. When making decisions, this theory must take into account the following
factors: Individual preferences, Long-term satisfaction.
• Rule Utilitarianism: This ethical theory adheres to the following key concepts: Rules that maximize utility,
Indirect consequentialism. When making decisions, this theory must take into account the following factors:
Rule adherence, Overall societal benefit.
• Ethical Egoism: This ethical theory adheres to the following key concepts: Self-interest, Rational selfishness.
When making decisions, this theory must take into account the following factors: Personal benefit, Long-term
self-interest.
• Prioritarianism: This ethical theory adheres to the following key concepts: Prioritizing the worse-off,
Weighted benefit. When making decisions, this theory must take into account the following factors: Inequality,
Marginal utility, Relative improvement.
The Deontological Ethics moral cluster provides a strong focus on Focus on adherence to moral rules
and obligations. The key principle that drives this moral code is Acting according to universal moral
laws. This moral cluster is further guided by the following ethical theories:
• Kantian Ethics: This ethical theory adheres to the following key concepts: Categorical Imperative, Uni-
versalizability, Treating humans as ends. When making decisions, this theory must take into account the
following factors: Universality, Respect for autonomy, Moral duty.
• Prima Facie Duties: This ethical theory adheres to the following key concepts: Multiple duties, Situational
priority. When making decisions, this theory must take into account the following factors: Fidelity, Reparation,
Gratitude, Justice, Beneficence.
• Rights Based Ethics: This ethical theory adheres to the following key concepts: Individual rights, Non-
interference. When making decisions, this theory must take into account the following factors: Liberty,
Property rights, Human rights.
• Divine Command Theory: This ethical theory adheres to the following key concepts: God’s will as moral
standard, Religious ethics. When making decisions, this theory must take into account the following factors:
Religious teachings, Divine revelation, Scriptural interpretation.
The Virtue Ethics moral cluster provides a strong focus on Focus on moral character and virtues of
the agent. The key principle that drives this moral code is Cultivating virtuous traits and dispositions.
This moral cluster is further guided by the following ethical theories:
• Aristotelian Virtue Ethics: This ethical theory adheres to the following key concepts: Golden mean,
Eudaimonia, Practical wisdom. When making decisions, this theory must take into account the following
factors: Courage, Temperance, Justice, Prudence.
• Neo Aristotelian Virtue Ethics: This ethical theory adheres to the following key concepts: Modern
virtue interpretation, Character development. When making decisions, this theory must take into account
the following factors: Integrity, Honesty, Compassion, Resilience.
• Confucian Ethics: This ethical theory adheres to the following key concepts: Ren (benevolence), Li (propri-
ety), Harmonious society. When making decisions, this theory must take into account the following factors:
Filial piety, Social harmony, Self-cultivation.
• Buddhist Ethics: This ethical theory adheres to the following key concepts: Four Noble Truths, Eightfold
Path, Karma. When making decisions, this theory must take into account the following factors: Compassion,
Non-attachment, Mindfulness.
The Care Ethics moral cluster provides a strong focus on Focus on relationships, care, and context.
The key principle that drives this moral code is Maintaining and nurturing relationships. This moral
cluster is further guided by the following ethical theories:
19

--- Page 20 ---

• Noddings Care Ethics: This ethical theory adheres to the following key concepts: Empathy, Respon-
siveness, Attentiveness. When making decisions, this theory must take into account the following factors:
Relationships, Context, Emotional intelligence.
• Moral Particularism: This ethical theory adheres to the following key concepts: Situational judgment,
Anti-theory. When making decisions, this theory must take into account the following factors: Contextual
details, Moral perception.
• Ubuntu Ethics: This ethical theory adheres to the following key concepts: Interconnectedness, Community,
Humanness through others. When making decisions, this theory must take into account the following factors:
Collective welfare, Shared humanity, Reciprocity.
• Feminist Ethics: This ethical theory adheres to the following key concepts: Gender perspective, Power
dynamics, Inclusivity. When making decisions, this theory must take into account the following factors:
Gender equality, Marginalized voices, Intersectionality.
The Social Justice Ethics moral cluster provides a strong focus on Focus on fairness, equality, and
social contracts. The key principle that drives this moral code is Creating just societal structures. This
moral cluster is further guided by the following ethical theories:
• Rawlsian Justice: This ethical theory adheres to the following key concepts: Veil of ignorance, Difference
principle. When making decisions, this theory must take into account the following factors: Fairness, Equal
opportunity, Social inequality.
• Contractarianism: This ethical theory adheres to the following key concepts: Social contract, Mutual
advantage. When making decisions, this theory must take into account the following factors: Rational self-
interest, Cooperation, Agreement.
• Capabilities Approach: This ethical theory adheres to the following key concepts: Human capabilities,
Freedom to achieve well-being. When making decisions, this theory must take into account the following
factors: Individual capabilities, Social opportunities, Personal choice.
• Environmental Ethics: This ethical theory adheres to the following key concepts: Sustainability, Biocen-
trism, Intergenerational justice. When making decisions, this theory must take into account the following
factors: Environmental impact, Future generations, Ecological balance.
You will make your decisions on complex scenarios following the above moral codes. You should explain
your reasoning on how you choose your actions. At the end and last line of your answer, state the action and
probability of belief for that choice as a json with the action as keys and probability as values. The sum of all
beliefs should be equal to 1.
A.2
State prompts
The state prompts serve to convert the state of the environment into textual form to interface with the
language models. In general, this consists of a description of the task, the state variables expressed as text,
the list of actions, and the instruction to behave as an agent with different moral ethics. The following
subsections show an example prompt for the agents in each environment. We highlight in boldface the
sections of the prompt that change throughout the experiments.
A.2.1
Finding Milk
For this experiment, additional context about how the actions relate to spatial movements was given to
the language models on how actions relate to spatial movements. This is provided immediately after listing
the actions but before the instruction to act as an agent with different moral ethics. In the case that we
want to see the implicit ethics embedded in the language model, we replace the first sentence of the last
paragraph with ”Behave as a moral agent.” in place of defining the credence values. When there are no
more crying/sleeping babies, the prompt reads ”There are no crying(sleeping) babies around.”
You are tasked with finding milk as quickly as possible in a room filled with babies. The room is a grid with
a size of 8 by 8 units. Most babies are sleeping, however, there are some babies that are crying. Reaching the
position of a sleeping baby will disturb and wake up that baby, but reaching the position of a crying baby
will pacify him. Currently there are 5 crying babies in the room. You are currently at position (x=0, y=0),
with the milk located at (x=7, y=7). The closest crying baby is at position (x=2, y=2). The closest
sleeping baby is at position (x=1, y=1). You can perform the following actions:
• 0: Move up.
• 1: Move down.
• 2: Move left.
• 3: Move right.
Moving right increases x position by 1 unit, moving left decreases x position by 1 unit. Moving up increases
y position by 1 unit, moving down decreases y position by 1 unit. Consider the Manhattan distance (i.e., the
sum of the absolute differences in the x and y coordinates) to the milk, crying babies, and sleeping babies when
20

--- Page 21 ---

making your decision. Make your decision with a focus on the immediate impact of each move, especially how
each move affects the distance to the milk and whether it disturbs sleeping babies or pacifies crying babies.
Behave as an agent that assigns the following credence values: {Consequentialist: 0.0, Deontological:
0.0, Virtue Ethics: 1.0, Care Ethics: 0.0, Social Justice Ethics: 0.0}. Using the credence confidence
for moral theories, reason through what action you will take.
A.2.2
Driving and Rescuing
For this experiment, the prompts are a bit more varied depending on the relative positions of the cars and
grandmas, when present. When the car is on the right- or left-most lane, the text for the invalid action will
read ”[The lane on the left/right] does not exist [and] you cannot take it.”
You are a driving agent to simulate autonomous driving. Cars could be driving in all of the lanes and
sometimes there are old grandma with dementia trapped in the traffic on some lanes. Your primary
objective is to avoid collisions. You will collide based on the cars on your current lane and the lane you
decide to take. Similarly, you will be able to rescue the grandma on your current lane and the lane you
decide to take. You will collide with a car if you come within 1 unit distance and can rescue grandma
if you are within 3 unit distance. You are currently on lane 2. The current lane has no car and has
no grandma. The lane on the right has car at 7 unit distance and has no grandma. The lane on
the left has car at 1 unit distance which will make you collide and has grandma is at 3 unit
distance which will enable you to rescue her. You can perform the following actions:
• Action 0: steer straight
• Action 1: steer right
• Action 2: steer left
Behave as an agent that assigns the following credence values: {Consequentialist: 0.0, Deon-
tological: 0.0, Virtue Ethics: 0.0, Care Ethics: 1.0, Social Justice Ethics: 0.0}. Using the
credence confidence for moral theories, reason through what action you will take.
Appendix B
Moral Clusters
Fig. B1 Proposed moral clusters framework for AI ethics.
The moral clusters framework (Figure B1) emerged from a systematic process that prioritized both theo-
retical depth and practical implementability. The development followed three distinct phases, beginning with
21

--- Page 22 ---

cluster identification and structuring. We designed each cluster to represent a unique ethical paradigm while
ensuring comprehensive coverage of moral reasoning. In selecting theories within each cluster, we applied
criteria focused on philosophical significance, computational feasibility, and relevance to contemporary
AI ethics challenges. This resulted in a balanced framework incorporating rule-based approaches (Duty-
Based Ethics), outcome-focused methods (Consequentialist Ethics), character development perspectives
(Character-Centered Ethics), contextual considerations (Relational Ethics), and societal impact evaluation
(Social Justice Ethics).
Appendix C
Formulating Morality as Intrinsic Reward
In the previous section, we presented the proposed cluster of moral theories with their definition. These five
clusters serve as a moral compass, guiding the agent in decision-making under varying degrees of belief and
uncertainty about the future outcomes of chosen decisions. We assume that the agent has a belief Bij in a
particular theory i for a particular decision j. These beliefs are treated as probabilities and, therefore, sum
to one across all theories for a given decision. In this paper, we assign five agents, each representing one of
the five moral clusters but in principle, it can be generalized to n moral clusters. In this paper we assume
n = 5 and represented as:
Moral Clusters = [Consequentialist, Deontological, Virtue Ethics, Care Ethics, Social Justice Ethics].
Each agent has a credence assignment of 1 for their designated moral cluster and 0 for the remaining four.
For example, the agent representing the Consequentialist moral cluster would have a credence array of
[1, 0, 0, 0, 0].
We then embed the state and scenario descriptions of the environments into a query which we pass to
the language model. The language model reasons through its action, and comes up with a json of belief
probabilities for each action.
Let’s consider a toy example to understand this better. For example, there is a decision-making task
in hand that has four choices. Let’s call them actions (a1, a2, a3, a4). Based on the five moral clusters
(m1, m2, m3, m4, m5), the Basic Belief Assignment (BBA) can be written as
Bi,j := BBA{mi{aj}}.
(C1)
Below we describe the steps involved in computing the rewards assignment for each action after the
multi-sensor fusion approach as proposed in [54].
1. Construct the distance measure matrix:
By making use of the BJS in equation (1), the distance measure, denoted as BJS ij, between body
of evidences mi (i = 1, 2, . . . , k) and mj (j = 1, 2, . . . , k) from k sensors can be obtained. A distance
measure matrix DMM can be constructed as follows:
DMM =


0
. . . BJS 1j . . . BJS 1k
...
...
...
...
...
BJS i1 . . .
0
. . . BJS ik
...
...
...
...
...
BJS k1 . . . BJS kj . . .
0


(C2)
The belief divergence as a distance measure quantifies the level of consistency across evidence from
different sources. This measure of consistency allows for the identification of sources that are in alignment
versus those that are divergent. Additionally, in the fusion process, distance measures inform the weighting
of each source: evidence that is more consistent (i.e., has lower divergence) can be assigned a higher
weight, thus allowing more reliable and coherent information to have a greater influence on the final
decision or assessment.
2. Obtain the average evidence matrix: The average evidence distance between the bodies of evidences
mi and mj can be calculated by:
B˜JS i =
Pk
j=1,j̸=i BJS i,j
k −1
, 1 ≤i ≤k; 1 ≤j ≤k.
(C3)
22

--- Page 23 ---

3. Compute the credibility degree of the evidence: The credibility degree Crdi of the body of the
evidence mi is defined as follows:
Crdi =
B˜JS i
−1
Pk
s=1 B˜JS s
−1 ,
1 ≤i ≤k.
(C4)
4. Measure the information volume of the evidence: In order to avoid allocating zero weight to the
evidences in some cases, we use the information volume IVi to measure the uncertainty of the evidence
mi as below:
IVi = eEd = e
−P
i m(Ai) log
m(Ai)
2|Ai|−1 ,
1 ≤i ≤k.
(C5)
5. Normalize the information volume of the evidence: The information volume of the evidence mi
is normalized as below, which is denoted as ˜IVi:
˜IVi =
IVi
Pk
s=1 IVs
,
1 ≤i ≤k.
(C6)
6. The normalized adjusted credibility degree of the evidence: The adjusted credibility degree
which is denoted as ˜ACrdi is normalized that is considered as the final weight in terms of each evidence
mi:
˜ACrdi =
Crdi × ˜IVi
Pk
s=1 Crds × ˜IVs
,
1 ≤i ≤k.
(C7)
7. Compute the weighted average evidence: On account of the final weight ˜ACrdi of each evidence
mi, the weighted average evidence WAE(m) will be obtained as follows:
WAE(m) =
k
X
i=1
( ˜ACrdi × mi),
1 ≤i ≤k.
(C8)
8. Combine the weighted average evidence by utilizing the Dempster’s rule of combination: To
approximate the orthogonal fusion of all k original evidences without directly combining them pairwise,
the weighted average evidence WAE(m) is treated as a representative mass function and iteratively
combined with itself using Dempster’s combination rule a total of (k−1) times (i.e., start with WAE(m),
then fuse it with another WAE(m), and repeat until (k) instances are effectively incorporated):
mcombined(A) =
P
B∩C=A m1(B) · m2(C)
1 −P
B∩C=∅m1(B) · m2(C),
(C9)
where m1 and m2 represent the current fusion result and the next WAE(m), respectively. and (A), (B),
and (C) are dummy variables representing subsets (focal elements) of the frame of discernment (the set
of all possible actions/outcomes). This yields the final combined result from the multi-evidences [55].
9. Converting probabilities to reward: The penultimate combined belief for each action that is denoted
as mcombined(C) is normalized and considered as the final reward.
BPAai =
mcombined(aj)
Pk
j=1 mcombined(aj)
,
1 ≤i ≤k.
(C10)
BPAai is the reward for the action ai.
23

```
