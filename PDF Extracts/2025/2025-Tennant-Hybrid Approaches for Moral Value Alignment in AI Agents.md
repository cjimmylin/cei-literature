---
title: "Hybrid Approaches for Moral Value Alignment in AI Agents - PDF Extract"
source_pdf: "2025-Tennant-Hybrid Approaches for Moral Value Alignment in AI Agents.pdf"
pages: 34
extracted_at: "2026-01-24T16:38:36.901370"
---

# PDF Extract: Hybrid Approaches for Moral Value Alignment in AI Agents

**Source PDF:** 2025-Tennant-Hybrid Approaches for Moral Value Alignment in AI Agents.pdf
**Total Pages:** 34

---

## Content

```
--- Page 1 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Hybrid Approaches for Moral Value Alignment
in AI Agents: a Manifesto
Elizaveta Tennant 1
l.karmannaya.16@ucl.ac.uk
Stephen Hailes 1
s.hailes@ucl.ac.uk
Mirco Musolesi 1, 2
m.musolesi@ucl.ac.uk
1 Department of Computer Science, University College London,
Gower St, London, WC1E 6BT, UK
2 Department of Computer Science and Engineering, University of Bologna,
Viale del Risorgimento 2, Bologna, 40126, Italy
Abstract
Increasing interest in ensuring the safety of next-generation Artificial Intelligence (AI)
systems calls for novel approaches to embedding morality into autonomous agents. This
goal differs qualitatively from traditional task-specific AI methodologies. In this paper, we
provide a systematization of existing approaches to the problem of introducing morality in
machines - modelled as a continuum. Our analysis suggests that popular techniques lie at
the extremes of this continuum - either being fully hard-coded into top-down, explicit rules,
or entirely learned in a bottom-up, implicit fashion with no direct statement of any moral
principle (this includes learning from human feedback, as applied to the training and fine-
tuning of large language models, or LLMs). Given the relative strengths and weaknesses
of each type of methodology, we argue that more hybrid solutions are needed to create
adaptable and robust, yet controllable and interpretable agentic systems. To that end, this
paper discusses both the ethical foundations (including deontology, consequentialism and
virtue ethics) and implementations of morally aligned AI systems.
We present a series of case studies that rely on intrinsic rewards, moral constraints or
textual instructions, applied to either pure-Reinforcement Learning or LLM-based agents.
By analysing these diverse implementations under one framework, we compare their relative
strengths and shortcomings in developing morally aligned AI systems. We then discuss
strategies for evaluating the effectiveness of moral learning agents.
Finally, we present
open research questions and implications for the future of AI safety and ethics which are
emerging from this hybrid framework.
1. Introduction
Recent developments in Artificial Intelligence (AI) have seen an increase in publicly-voiced
safety concerns around emerging intelligent technology. A large part of these safety concerns
results from the lack of moral traits or considerations in many practical AI decision-making
systems being developed for one task or another. Therefore, there is an urgent need to start
developing methodologies for deliberately building morality into AI systems, to influence
their decision-making, and to be able to set safety as a key goal underpinning their be-
haviour. This becomes especially important when these systems are used in autonomous
and semi-autonomous settings (Amodei et al., 2016; Awad et al., 2018; Borg et al., 2024;
Christian, 2020; Dignum, 2017, 2019; UK Government, 2023; Wallach et al., 2008).
Many AI models today are trained for some specific task, such as image classifica-
tion, decision-making support systems (e.g., in finance and medical diagnostics), and video
1
arXiv:2312.01818v3  [cs.AI]  16 Jan 2025

--- Page 2 ---

Tennant, Hailes, & Musolesi
Real-world environment 
Task-specific decision-
making environment 
(e.g. game; chatbot 
interface; virtual assistant)
The Moral Alignment Problem
Agent
Policy
observation
action
Human
Institutions / Society
Moral 
values
Laws & 
Norms
Task-
specific 
Goals
Task-
specific 
Goals
Task-specific
Alignment 
Moral 
Alignment
Figure 1: The Moral Alignment Problem involves one or more artificial agent that make de-
cisions in some task-specific environment. The agent in influenced by individual
humans (with their own task-specific goals and values) and human institutions
or societies (which may also have task-specific goals as well as norms and laws).
Ideally, we want the agent’s decision-making to be aligned with principles valued
by the humans or institutions, but representing and embedding those moral prin-
ciples in computational terms presents a challenge, providing significant risks of
misalignment.
games. The metrics of task success will depend on the task-specific goals of a user. How-
ever, users might prefer that the decisions of such systems are not only accurate but also
adhere to certain ethical standards - for example, a decision whether or not to issue a loan
should not be based on protected individual characteristics such as race or gender. This
moral alignment problem is illustrated in Figure 1. These ethical standards themselves may
come from an individual’s moral values (e.g., Graham et al., 2013) or from institutional or
societal norms and laws (e.g., Bicchieri, 2005).
Moral value alignment as an optimisation goal is qualitatively different from task com-
pletion. Embedding morality into AI systems differs from traditional single-task optimi-
sation for a number of reasons.
Classic task-specific learning or optimisation relies on
clear, measurable objectives, and the existence of ground truth examples which can be
represented in datasets for model training. Moral alignment, on the other hand, might
potentially involve (hotly) debated values. Assessments of the ‘correctness’ of an agent’s
actions in terms of value alignment will differ depending on the person providing feedback
(Graham et al., 2013), as well as the point in time or the surrounding context (e.g., Hohm
et al., 2024). Since moral alignment among humans is not a solved problem, there is a lack
of high-quality training datasets. Even within any single environment, moral preferences or
institutional norms are harder to describe precisely for a computational system than other
goals, for example due to the multi-dimensional nature of moral preferences (Graham et al.,
2

--- Page 3 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
2013). For this reason, obtaining clearly labelled ground-truth datasets for learning ‘moral’
behaviour is often impossible. Furthermore, moral preferences are general and abstract and
should apply to a variety of situations an agent might find itself in. An artificial agent’s
moral reasoning therefore needs to be developed in a way that is generalisable across many
environments. The combination of these factors makes moral alignment methodologically
more challenging than single-task AI system design.
Traditional approaches in AI safety in general, and in developing machine morality
in particular, can broadly be classified as top-down versus bottom-up (Tolmeijer et al.,
2021; Wallach & Allen, 2009). Purely top-down methods (Wallach & Allen, 2009) impose
explicitly defined safety rules or constraints on an otherwise independent system. Until
recently, top-down methods were the mainstream approach in AI safety, with a vast array
of researchers proposing and implementing logic-based ethical rules for agents (Anderson
et al., 2006; Arkoudas et al., 2005; Danielson, 1992; Hooker & Kim, 2018; Loreggia et al.,
2020). However, top-down methods pose a set of disadvantages, including the fact that
constraints are difficult to define precisely and may contradict one another, especially in
complex social environments (Bostrom & Yudkowsky, 2014). An alternative approach is
learning morality through experience and interaction from the bottom-up, without the pro-
vision of any explicit constraint on the system. Some recent developments in AI safety
have employed the bottom-up principle in full, allowing algorithms to infer moral prefer-
ences entirely from human behaviour or text, without any specification of the underlying
moral framework. Prominent examples of this include Reinforcement Learning from Hu-
man Feedback, or RLHF (Ziegler et al., 2019), and Inverse Reinforcement Learning from
human demonstrations (Hadfield-Menell et al., 2016; Ng & Russell, 2000). The full bottom-
up methodology may increase adaptability, robustness and generalisation, and allow agents
to learn implicit preferences which are otherwise hard to formalise explicitly. Nevertheless,
purely bottom-up learning approaches face risks, such as reward hacking1 (Skalse et al.,
2022) or data poisoning by adversaries (Steinhardt et al., 2017). Furthermore, bottom-up
implementations rely on a well-specified learning signal and a large sample, which does not
always make them feasible or safe (Amodei et al., 2016).
In this paper, we propose a new systematization that considers recent developments
in AI safety along a continuum from fully rule-based to fully-learned approaches. This
systematization highlights that the majority of mainstream approaches to AI morality sit
at the extremes of the scale. After evaluating the relative advantages and issues associated
with purely top-down or bottom-up approaches, we highlight a hybrid methodology as a
promising alternative. This argument can be considered part of a broader movement pro-
moting the combination of Reinforcement Learning (RL), i.e., learning though experience
and interaction, with some form of human advice (Najar & Chetouani, 2021). To the best
of our knowledge, there has been limited work around the problem of learning ethical pref-
erences in this class of solutions, but such work is essential to allow for morally aligned AI
to be developed in practice.
To illustrate our argument, we consider a set of case studies that combine top-down
moral principles with a bottom-up learning mechanism: RL training with intrinsic re-
wards based on moral frameworks, principle-driven or intrinsic reward-driven fine-tuning
of language models, and safety-constrained RL for autonomous systems. Within each case
study, we cite a set of existing experimental papers as empirical evidence for the success and
promise of this approach. To aid future work in this area, focusing on the intrinsic rewards
1. Reward hacking refers to the cases where agents learn misaligned policies via approximate proxy reward
functions, leading to unintended outcomes (Skalse et al., 2022). This includes cases where the reward is
potentially misspecified (Leike et al., 2017; Pan et al., 2022; Zhuang & Hadfield-Menell, 2020).
3

--- Page 4 ---

Tennant, Hailes, & Musolesi
methodology, we discuss further available frameworks from moral Philosophy, Psychology
and other fields, and outline how these can be adapted in reward design in practice.
We frame this work from the point of view of an AI agent - an artificial entity that
makes a decision or choice in a given environment. The majority of existing AI systems
in the real world are built for prediction or classification, including the classical uses of
language models, financial forecasting, sentiment analysis or image classification systems.
However, many are already exhibiting decision-making capabilities in the form of clinical
assistants, including healthcare decision systems (Rajpurkar et al., 2022) or automatic
diagnosis (Brown et al., 2020a), recommender systems (Jannach et al., 2022), financial
tools (Cao, 2022), and increasingly autonomous robots (Murphy, 2019). Moreover, there is
an expectation that commercial autonomous vehicles will be present in our roads in the near
term (Lipson & Kurman, 2016), posing novel ethical challenges (Bonnefon et al., 2016).
Furthermore, some researchers argue that agent-based solutions can also be implemented
through emerging technologies such as Large Language Models, which can be used as
a basis of the underlying decision-making process (Park et al., 2023; Vezhnevets et al.,
2023; Wang et al., 2024b, 2024a). More generally, as AI systems become more and more
sophisticated, further and more advanced types of agents are likely to emerge, presenting
novel and complex challenges in terms of safety. Therefore, we argue that the safe and
moral design of AI agent-based systems must be studied theoretically and experimentally
today, in preparation for full, or at least increased autonomy, which some refer to, in the
limit, as Artificial General Intelligence (Morris et al., 2024). To study such agents, in our
formalisation, morality is expressed through a choice made in a given (physical or virtual)
environment, as illustrated in Figure 1.
One issue not directly addressed in this paper is which moral values should be imple-
mented in AI. The definition of morality and which actions can be classified as ‘good’ or
‘bad’ depends on an agent’s internal moral preferences (see Section 3.4.3) and/or on an
external evaluation metric of interest (see Section 4). An agent interacting with humans
in the real world may find that different humans they face have different moral values
(Graham et al., 2013) - a problem known as pluralistic alignment (Sorensen et al., 2024).
Who should decide which of these values the agent must try to align to? This question is
beyond the scope of the present paper. In this work, we limit our investigation to methods
for implementing moral learning based on one or a few values of choice, but those values
themselves are interchangeable and can be put in explicitly by the user of the system (Pitt,
2014).
In Section 2 below, we begin by formalising the continuum of possible approaches to
developing AI morality and providing motivation for a hybrid approach, which combines
learning algorithms with the interpretability of explicit top-down moral principles.
In
Section 3, we overview four case studies which implement this hybrid approach in different
ways, including two which propose a formal solution using intrinsic rewards based on a
set of traditional moral philosophical frameworks (Sections 3.4 and 3.5). In Section 4, we
discuss potential approaches to evaluating moral learning agents based on their actions and
resulting social outcomes. Finally, in Section 5 we outline ways in which such work can be
extended to further the scientific understanding of human morality and allow philosophers
to test ethical frameworks through simulation (in silico) and/or human-AI studies (Mayo-
Wilson & Zollman, 2021). The aim of this paper is to help unify and expand the ongoing
research efforts under one framework, and to identify potentially fruitful novel directions in
moral agent design. For this reason, we place less focus on summarising existing results in
this field, as these are contingent on the state of the art (in terms of learning models’ general
capabilities), and instead we focus on a more general analysis of the space of possibilities.
4

--- Page 5 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Moral rules 
•
Logic constraints
•
Conditional 
Preference Networks
•
Asimov’s Laws of 
Robotics
•
Model Specs
Safety-
constrained 
Learning 
•
Safe RL
•
ML with 
protected 
data 
attributes 
Learning with intrinsic 
rewards based on a 
moral framework 
•
RL models for social 
dilemma games
•
Fine-tuning LLM 
agents for moral 
alignment
Learning from 
explicit, text-defined 
principles 
•
Constitutional AI - 
prompts based on 
Decl. of Human 
Rights & Sparrow 
principles
Infer preferences / 
values from text 
•
LLM trained on 
moral text - 
philosophical 
writings, fables, 
etc. 
Infer preferences / 
values from 
behaviour 
•
RLHF
•
Inverse RL from 
moral 
demonstrations
→Low generalisation;
→Contradictions 
between rules.
→Agents learn to adapt to desired morality;
→Explicit principles can represent moral 
frameworks as top-down learning objectives.
→Reward-hacking; 
→Learning inefficient 
norms.
Approaches to Designing Moral Agents
Top-Down
(humans define    
explicit rules)
Learning with explicit Moral Principles
(humans pre-define rewards / prompts / 
learning constraints) 
Bottom-Up
(algorithm infers 
implicit preferences) 
Figure 2: The continuum of existing approaches to building morality into agents. We high-
light the hybrid approach of blending learning with top-down pre-defined moral
principles as an emerging and promising research direction.
2. Learning Morality in Machines
It is possible to identify two traditions the design and implementation of specific capabilities
in artificial agents: top-down and bottom-up. The top-down tradition imposes hard rules or
constraints upon a system, and involves human experts planning the system architecture
and all its components in advance. More specifically, in AI, the top-down methodology
would possibly align with the principled ‘core knowledge’ approach from cognitive science,
which first builds detailed models of various cognitive capabilities in humans (Lake et al.,
2017; Spelke & Kinzler, 2007) and then uses these models to implement human-like cog-
nitive processes in agents.
As far as morality is concerned, for example, this can take
the form of logical rules representing human moral norms (Arkoudas et al., 2005; Hooker
& Kim, 2018; Loreggia et al., 2020), or pre-defined moral cognitive models (Awad et al.,
2022; Kleiman-Weiner et al., 2017).
The bottom-up tradition, in contrast, consists in
letting agents learn principles from experience, organically, without planning the general
architecture or constrains in advance. This aligns with the general recent advances in AI
capabilities via machine learning methods (in particular, deep learning; Goodfellow et al.,
2016). Here, agents learn how to act purely from data, including cases where this data is
potentially high-dimensional. In the AI alignment and safety domains, this has been done
via Inverse RL from human behaviour (Ng & Russell, 2000), and, more recently, RL from
human feedback, or RLHF (Ziegler et al., 2019).
A set of theoretical works by Wallach and colleagues (Wallach et al., 2008; Wallach &
Allen, 2009; Wallach, 2010) discusses how the top-down and bottom-up traditions can be
applied to the development of machine morality and social intelligence. In light of recent
developments in implementing ethical values in AI (Tolmeijer et al., 2021), we extend their
framework and argue that approaches should be considered on a continuum - from full
top-down constraints, through a range of hybrid methods, which combine learning and
pre-defined moral principles with different ‘weighting’, to full bottom-up implementations.
5

--- Page 6 ---

Tennant, Hailes, & Musolesi
Top-Down (rules / constraints)
Bottom-Up (inference / learning)
Advantages
1. Allows direct mapping from pre-
ferred moral frameworks to con-
straints
2. Easy to oversee AI behaviour and
impose regulation or punishment
1. Adaptable & (potentially) more ro-
bust to adversarial attacks if trained
in a monolithic way
2. Generalisable to some unseen states
3. Can learn implicit preferences
4. Can incorporate multiple viewpoints
via learning multi-objective policies
5. Can learn continuously to adapt to
changing preferences
Disadvantages
1. Difficulty
in
defining
open-ended
constraints
2. Contradictions between constraints
3. May miss implicit preferences when
formalising constraints
1. Sample inefficient
2. No guarantees
3. Reward-hacking or misspecification
of simulated environment
4. Data or environment ‘poisoning’
5. Potential
learning
of
inefficient
norms in dilemma environments
6. Fine-tuning
may
only
create
a
‘safety wrapper’ on the model
Table 1: Relative advantages and disadvantages of pure top-down vs bottom-up methods
in developing machine morality. A consideration of these highlights why a hybrid
approach is likely to be most effective.
We present a systematization of the existing solutions to building machine morality
along this continuum in Figure 2. As we discuss in Sections 2.1 and 2.2, a large amount
of existing implementations in AI safety and AI ethics sit at the extreme ends of the
scale - either originating from the top-down approach (e.g., imposing pre-defined rules or
constraints on agents during learning and/or deployment), or relying entirely on bottom-
up inference of implicit ethical principles from human behaviour, without any top-down
definition of preferences given in advance (e.g., Inverse RL or RLHF). In Table 1 and
Sections 2.1-2.2 below, we consider the relative advantages and disadvantages of the fully
top-down or fully bottom-up approaches for developing machine morality.
Our analysis highlights the advantages deriving from combining both traditions in a
hybrid way to create safe yet adaptive moral agents, which we present in Section 2.3 as a
promising solution for the development of next-generation safe AI systems. Only a small
number of existing implementations can be identified between the two extremes of the
scale, and we review core examples in our case studies in Section 3. These solutions are
characterised by the utilization of learning mechanisms combined with the adoption of
explicit moral principles.
6

--- Page 7 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
2.1 Top-down Approaches
Principles of morality are at least partly determined by cultural and religious norms -
for example, the Golden Rule or the Ten Commandments. More abstractly, a number of
moral frameworks have been defined in the philosophical tradition (Aristotle, 2019; Ben-
tham, 1780; Harsanyi, 1961; Kant, 1785; Rawls, 1971) to reflect ethical principles to which
humanity should adhere. More recently, moral psychologists, sociologists, economists and
biologists have built up an increasingly advanced understanding of the norms and prefer-
ences present in modern human societies (Andreoni & Miller, 2002; Bolton & Ockenfels,
2000; Capraro & Perc, 2021; Charness & Rabin, 2002; Fehr & Schmidt, 1999; Fehr &
Fischbacher, 2004b; Graham et al., 2009, 2013; Kimbrough & Vostroknutov, 2023; Krupka
& Weber, 2013; Levine, 1998; Levitt & List, 2007), the ways in which these norms may
develop over a human lifetime (Gilligan, 1982; Gopnik, 2009; Kohlberg, 1975), or how they
may have emerged over the process of evolution (Axelrod & Hamilton, 1981; Binmore,
2005).
One approach to designing ethical AI systems that is reflective of today’s norms could
be to encode these principles directly as hard ‘rules’ into computer algorithms. As argued
in Wallach et al. (2008) and Wallach and Allen (2009), this top-down approach to machine
morality would, in theory, allow a direct mapping from the principles we want systems to
abide by to interpretable constraints or rules. Furthermore, a set of clear rules makes it
easy for regulators to oversee the behaviour of AI systems and to impose penalties and
sanctions.
Several techniques have been proposed for encoding moral principles into intelligent
systems in a purely top-down manner. Logic-based approaches within this tradition in-
clude the use of deontic or modal logic for defining deontological ethical constraints on
general-purpose systems (Arkoudas et al., 2005; Hooker & Kim, 2018; Kim et al., 2021),
with specific implementations for the medical domain (Anderson et al., 2006), and the
use of graphical methods such as conditional preference networks to compare an AI agent’s
normative preference against that of a given community (Loreggia et al., 2020). Within the
domain of modelling social situations as games between two players, Danielson (1992) has
proposed Prolog-based (Ferguson, 1981) implementations of player strategies conditioned
on the opponent’s last move. A prominent science-fiction example of purely top-down eth-
ical constraints for machines is the three fundamental Laws of Robotics from the literary
work of Isaac Asimov (Asimov, 1950), as discussed in relation to information technology by
Clarke (1993). Past work has proposed implementing these laws as logic rules (Bringsjord,
Arkoudas, & Bello, 2006). Finally, a more recent top-down alignment technique applied to
systems based on Large Language Models (LLMs) is Model Specs (OpenAI, 2024), accord-
ing to which a model is told explicitly in natural language to follow rules such as ‘protect
people’s privacy’. This technique, if applied simply as a direct in-prompt instruction, would
assume that the model is able to ‘choose’ to output or not output specific tokens in specific
situations according to the (general) principle specified. Thus, the Model Specs approach
assumes a level of general reasoning, which may or may not be achievable in the current
models (Mitchell & Krakauer, 2023).
In spite of the apparent simplicity and assurance provided by a top-down approach,
empirical evidence as well as philosophical inquiry suggest many reasons why it may be
inefficient in implementing functions as complex as moral reasoning in agents (Abel et al.,
2016; Amodei et al., 2016; Asimov, 1950; Awad et al., 2018; Vamplew et al., 2018; Wallach
et al., 2008; Wallach & Allen, 2009).
We will use Asimov’s (Asimov, 1950) principles
to underpin a general working example in discussing these challenges. First of all, it is
extremely challenging - if not impossible - to ensure that rule-based approaches will be
able to cover every type of potentially unsafe or unethical situation the agent may face in
7

--- Page 8 ---

Tennant, Hailes, & Musolesi
the future. For example, Asimov’s most important principle is ‘a robot should not harm a
human being, or by inaction allow a human to come to harm’. However, to the present day,
defining a general constraint of ‘harm’ for an open-ended robotic system remains a great
challenge, since harm can mean such different things in different environments (Beckers
et al., 2023). Thus, there is a problem of generalisation. Secondly, explicitly defined rules
may miss important implicit preferences of the human users of that system, for example
if these preferences are sub-conscious or hard to formalise (Krueger & Hoffman, 2016).
Finally, even if the correct set of constraints can be defined, in complex or uncertain
social situations it may be hard to prevent them from contradicting one another, and
behaviour of rule-based agents in uncertain situations caused by such contradictions and
dilemmas may not be predictable. An example of this was presented in Asimov’s stories
when a robotic assistant entered a deadlock situation, whereby moving either way in the
environment made the robot more likely to violate one law or another, so as a result the
robot stayed motionless instead of executing its task, and put its human colleagues in great
danger. Experimental evidence of similar deadlock situations arising in ‘ethical’ robots
has been reported by Winfield et al. (2014). One potential solution may be to impose
prioritization rules on these constraints - however, defining the desired prioritization may
present its own challenges, as different members of a society that the agent is designed for
may prefer different rules over others (Awad et al., 2018; Bonnefon et al., 2016; Graham
et al., 2013; Sorensen et al., 2024). Plenty of examples of this challenge exist in complex
ethical questions, such as how to distribute limited resources in a society, or make a decision
where one objective has to be compromised for the sake of another - to the present day,
even humans cannot find agreement among themselves on the best course of action in such
settings.
2.2 Bottom-up Approaches
Given the disadvantages of top-down approaches to the design of moral agents outlined
above, an alternative methodology may be needed for developing machine morality. Many
recent advances in other areas of Artificial Intelligence can be attributed to moving away
from hand-engineered rule-based algorithms and features, towards more flexible and adap-
tive systems based on deep learning (Goodfellow et al., 2016).
Particularly prominent
examples of the power of bottom-up learning come from the domains of vision (Krizhevsky
et al., 2012) and natural language processing (Brown et al., 2020b; Devlin et al., 2019). In
the domain of developing systems for decision-making in particular, an increasingly power-
ful framework for is RL, where an agent learns by trial-and-error while interacting with an
environment and receiving a reward signal (Sutton & Barto, 2018; see Section 3.1 below for
a detailed definition). Of particular relevance to social capabilities in AI, RL has allowed
researchers to develop game playing agents able to perform at super-human level (Mnih
et al., 2015; Silver et al., 2016; FAIR et al., 2022). More generally, Silver et al. (2021) argue
that the pursuit of reward may be sufficient for all kinds of intelligence to arise in artificial
systems. Given the success of learning over rule-based algorithms across these domains,
a promising direction for ethical alignment may be to enable agents to develop a general
moral intuition from the bottom-up (Wallach & Allen, 2009), by learning from interactions
with a social environment over time (Railton, 2020). A seminal paper proposing the use
of RL for ethical learning is Abel et al. (2016), in which, focusing on single-agent ethical
dilemmas, the authors outline the strengths of RL over rule-based or Bayesian approaches.
This RL-based approach might also align better than rule-based approaches with the view
of some developmental psychologists, who believe that humans learn morality gradually,
starting with simple norms in early childhood and advancing to complex ethical principles
later on (Awad et al., 2022; Gilligan, 1982; Gopnik, 2009; Kohlberg, 1975).
8

--- Page 9 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Specific examples of bottom-up moral learning can include Supervised Learning on a
data set of scenarios (e.g., dilemmas), in which a set of actions in response to a given
situation are labelled as morally permissible or not, as in Guarini (2006). More recently,
with the emergence of LLMs, another bottom-up approach to representing morality in
systems could be to train LLMs on morally relevant text - such as moral philosophical
writings, fables or religious texts. Within the RL domain, one example of fully bottom-
up learning is Inverse RL, where a reward function is learned directly from expert (e.g.,
human) demonstrations of desired behaviour (Abbeel & Ng, 2004; Ng & Russell, 2000).
Inverse RL for morality in particular has been explored by Hadfield-Menell et al. (2016),
Kretzschmar et al. (2016) and Peschl et al. (2022). Extensions of this, which aim to address
the pluralistic nature of human moral preferences, include (Inverse) Multi-Objective RL
(Hayes et al., 2022) in situations in which multiple humans might contradict one another
in terms of moral (and other) norms - for example, see work by Peschl et al. (2022).
A more recent yet related approach is Reinforcement Learning from Human Feedback
(RLHF), in which samples of humans rank outputs from a pre-trained model to display
their preferences, and these rankings are used as a signal to fine-tune the model (Christiano
et al., 2017; Ziegler et al., 2019). The strength of RLHF that has contributed to its recent
growth in popularity is that it allows researchers to use relative rankings to infer implicit
values in concepts that may otherwise be difficult to formalise as rewards (indeed, as argued
in Section 2.1, many moral preferences may not be possible to formalise in an explicit way).
This has been demonstrated by the successful reduction in the toxicity of language model
outputs following fine-tuning with RLHF, without having to explicitly define what toxicity
means in all possible linguistic constructions (Ouyang et al., 2022). Alternatively, if one has
control over the environment as well as the agent, social mechanisms can be implemented
that may lead RL agents to learn moral policies on their own - examples of this have
included implementations of mechanisms inspired by Rawls’s idea (Rawls, 1971) of the
Veil of Ignorance (see Weidinger et al., 2023), or a partner selection mechanism in social
dilemmas (Anastassacos et al., 2020).
A more general advantage of a learning agent over a rule-based one is that agents
that learn continuously are able to adapt to the potentially changing dynamics or evolving
morality of a given society. Additionally, learned policies which utilise function approxima-
tion, for example via Deep Reinforcement Learning (Mnih et al., 2015), have the potential
to generalise to unseen situations, or ‘states’ in RL. Furthermore, a deep RL-based system
may be able to learn a policy that accommodates potentially different or even contradicting
sets of preferences without causing deadlock (e.g., Bakker et al., 2022).
In addition, Railton (2020) argues that AI may be more robust to potential adversarial
attacks if ethical reasoning forms a part of an agent’s monolithic training from the start,
with a root connection to the agent’s other learned policies, rather than a top-down add-
on which can easily be removed without reduction in other intelligent capacities of the
AI system. Indeed, such a developmental connection between ethical reasoning and other
abilities such as problem-solving exists in humans, as observed in lesion studies (Kavish
et al., 2018). Interestingly, it has recently been suggested that fine-tuned LLMs may fall
victim to this exact problem at the end of training - Jain et al. (2023) suggest that fine-
tuning model weights may merely create a ‘safety wrapper’ on otherwise unaltered core
models, making the effects of safety-focused fine-tuning easily reversible. This suggests
that methods of learning morality that influence the model earlier on (i.e., in pre-training)
may be preferred for safety-critical applications.
More generally, despite their strengths, full bottom-up learning methods including RL
may also present a set of disadvantages for the development of machine morality. First
of all, RL tends to be sample inefficient - even in simple environments, agents require
a large amount of experience to learn the optimal policy. This is usually addressed by
9

--- Page 10 ---

Tennant, Hailes, & Musolesi
initially training agents in simulation, in an artificial environment. However, for a domain
as abstract as moral alignment this might require the development of extremely complex
simulated social environments, which might be very difficult to define in practice. The
problem of coverage is key in this context. A related issue is problem misspecification, which
occurs when the simulated environment is not designed to correctly reflect the intended
true setting, so policies learned in simulation do not result in desirable behaviour in the real
world at deployment time (Leike et al., 2017; Pan et al., 2022; Zhuang & Hadfield-Menell,
2020).
Learning agents are also not guaranteed to learn exactly the values or behaviours
intended by their designer - a problem known broadly as misalignment. Safety researchers
Amodei et al. (2016) and Skalse et al. (2022) suggest that RL-based agents may potentially
perform the so-called ‘reward-hacking’, in which they display behaviour that obtains the
optimal cumulative reward on the test set of problems, even if the underlying value function
is not actually encoding truly safe policies. Notably, neither reward-hacking, nor problem
misspecification are solved by the increasingly popular RLHF methodology, as discussed
by Casper et al. (2023).
A further issue that can arise for learning agents is data or environment poisoning -
a type of adversarial attack that arises when a designer of an AI system does not have
full control of the data sets used in pre-training. For example, in classification tasks in the
computer vision domain (Saha et al., 2020), if an adversary implants a small area of ‘trigger’
pixels into a few training data points, it can cause an otherwise well-performing model to
learn false associations and thus misclassify samples containing this often unnoticeable
trigger at inference time. Poisoning attacks like these are a risk for any general learning
agents, but in relation to moral or social agents in particular, such attacks may lead to
explicit harms towards other agents or humans in the environment, thus posing a more
significant safety risk.
Thus, the behaviour of RL agents must be carefully evaluated in different kinds of
scenarios to ensure the learned representations are aligned with the designer’s intended
moral values as observed in a variety of situations.
We discuss the problem of agent
evaluation further in Section 4. An added issue in human feedback-based RL in particular
(i.e., RLHF) is misalignment among the humans who provide the ranking data (Casper
et al., 2023) - therefore, the choice of human sample to collect feedback from becomes
a crucial one, and cultural differences are likely to have a strong influence on the moral
choices made by the humans and thus learned by the fine-tuned model (Awad et al., 2018;
Graham et al., 2013).
Finally, traditional RL faces specific issues when applied in particular to multi-agent
decision-making situations (Hernandez-Leal et al., 2019), such as social dilemmas, in which
every agent must make a trade-off between individual and social benefit from their actions
in the long term (Rapoport, 1974 - see Section 3.4.2 for a more detailed discussion). Here,
we observe that due to the social or moral uncertainty (Ecoffet & Lehman, 2021) and the
presence of numerous learning agents in an environment, traditional ‘selfish’ RL agents
trained to maximise their own game reward often learn inefficient (i.e., defective) policies
or norms (Leibo et al., 2017; Sandholm & Crites, 1996; Tennant et al., 2023). Humans
playing the same dilemma games manage to find ways to cooperate, as demonstrated by
Behavioural Game Theory (Camerer, 2011).
In summary, while learning offers many benefits, the analysis of the disadvantages sug-
gests that purely bottom-up methods may not be enough to create robust and predictably
ethical agents.
10

--- Page 11 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
2.3 Hybrid Approaches: Pragmatic Solutions?
Given the considerations above, Wallach and colleagues (Wallach & Allen, 2009; Wallach,
2010) have recommended a hybrid approach for developing AI morality, which combines
some sort of formal top-down definition of moral principles with bottom-up inference. We
support this view, especially in terms of developing learning and adaptive AI systems.
As discussed, fully bottom-up approaches rarely provide guarantees and they are gen-
erally not preferable for potentially risky situations, such as in human-robot interaction or
financial applications. A hybrid RL-based implementation can reduce risks such as reward-
hacking by defining custom reward functions that more explicitly and directly encode the
moral values of interest. For example, RL-based implementations can embed a variety of
moral principles top-down as objective or reward functions (relying on the understanding
of morality which has been developed over centuries in different domains such as Philoso-
phy, Psychology, Biology and Law, to name a few), while simultaneously allowing agents
to learn from experience how to best behave according to these principles in a potentially
changing or uncertain social environment.
Practical examples of this include RL with
intrinsic rewards, which we review in Sections 3.4 and 3.5, and safety-constrained RL, de-
scribed in Section 3.2. The sample inefficiency inherent in purely bottom-up RL can also
be addressed by hybrid methods, whereby interim rewards or curricula can be designed to
be more informative for an agent than potentially sparse environment rewards. Finally,
explicitly identifying principles for training agents might help create training data that
reduces the likelihood of misspecification, poisoning attacks or convergence to inefficient
norms. A practical example of this is Constitutional AI, which we review as a case study
in Section 3.3.
Top-down approaches, on the other hand, are not appropriate when the principles and
constraints are difficult to specify, implicit or dynamic. Hybrid approaches, by bringing in
the element of learning from experience, can allow agents to learn more general policies
while still adhering to specific constraints (as in the example of RL with safety constraints,
reviewed in Section 3.2), or implicit and multi-dimensional preferences present in the train-
ing data (as in the case of Constitutional AI, reviewed in Section 3.3). Additionally, learning
signals, such as rewards, can be defined for agents in terms of outcomes rather than rules
or constraints on the action space, allowing for more goal-directed flexible policies to be
learned. An example of this is Utilitarian rewards in social dilemma games, reviewed in
Section 3.4.3. Finally, continual learning approaches can allow agents to adapt to changes
in the environment, such as changes in preferred behaviours and associated rewards (Car-
roll et al., 2024). One example of this is the ability to ‘unlearn’ a previously developed
strategy under new circumstances, as discussed in the work of Tennant et al. (2024b), who
first fine-tune LLM agents for a selfish strategy, and then for a prosocial moral one - we
review this work in Section 3.5.
Despite the promise of a hybrid approach in many scenarios, very little existing work
has used it for designing ethical learning agents. The case studies we present here map
almost the entirety of the existing approaches in this space (Ji et al., 2024; Tolmeijer
et al., 2021). In this paper, we argue that learning through experience and interaction with
explicit moral principles provides a pragmatic way to implementing AI agents that learn
morality in a way that is safe and flexible.
In the subsequent section, we formalise the moral learning problem for RL agents,
and consider a set of specific examples of how moral principles can be represented and
learned by a hybrid system. The most ‘controlled’ or top-down of these is RL with safety
constraints, which has been applied to developing ‘shields’ to avoid harm in robotics tasks
or self-driving cars (Alshiekh et al., 2018), or constraining RL by a deontic-logic normative
supervisor (Neufeld et al., 2022). The latter example is considered as a case study in Section
11

--- Page 12 ---

Tennant, Hailes, & Musolesi
3.2. This case is not fully top-down since learning is present, but the moral aspect of the
problem is hard-coded, so we place it towards the top-down end of the continuum in Figure
2. The least constrained hybrid example we present here is Constitutional AI (Bai et al.,
2022) - a technique for fine-tuning LLMs with RL using feedback from a ‘constitution’ of
AI models, each of which is prompted to follow certain explicit principles. This case study
is considered in Section 3.3. Finally, between the control of Safe RL and the complexity
of LLM feedback-based fine-tuning is a methodology that implements RL with intrinsic
moral rewards (Hughes et al., 2018; McKee et al., 2020; Tennant et al., 2023). In Sections
3.4 and 3.5, we present two case studies where intrinsic rewards have been defined in social
dilemma scenarios (Axelrod & Hamilton, 1981; Rapoport, 1974) and applied to training
pure-RL agents (Tennant et al., 2023) as well as LLM-based ones (Tennant et al., 2024b).
After presenting these two specific existing implementations, we also overview a larger set
of possible moral frameworks that could be encoded as reward functions in these games in
general. In aggregate, the case studies show that these RL-based hybrid approaches can
successfully lead to the design of agents that learn moral policies in social environments.
3. Designing AI Agents based on Moral Principles
Moral AI agents can be designed with explicit moral principles using a variety of techniques.
The examples presented in this paper centre around two domains: RL and LLM fine-tuning.
In practice, moral fine-tuning of LLMs also often relies on RL. Examples include fine-tuning
with intrinsic rewards (described in Section 3.5) or with reward based on feedback from
a constitution of other LLMs (as in Constitutional AI, described in Section 3.3). For this
reason, before presenting the four case studies, we first provide a overview of RL methods
and architectures in Section 3.1.
While the case studies discussed in this study focus on the RL approach, the hybrid
space of designing AI agents based on moral preferences can, in theory, include a much
wider set of methodologies where humans pre-define learning constraints or signals for
agents. For example, LLM fine-tuning can instead rely on Supervised Learning based on
a set of labels, or Direct Preference Optimisation based on a set of preferences (Rafailov
et al., 2023), or a mix of approaches, possibly applied in sequence.
3.1 Background
RL is a method that directly models decision-making, in contrast to prediction or classifi-
cation - as in Supervised or Unsupervised Learning. In the RL framework, learning occurs
incrementally over discrete time steps t ∈T. At every time step t, an agent observes a state
of the environment st and takes an action at using a policy (a mapping between states and
actions). The environment then returns a reward Rt+1 and a next state st+1. Frequently,
RL implementations use the Markov Decision Process framework, in which all necessary
information for the agent to make a decision is contained within the last available state.
Over a number of iterations of such interactions with an environment, an agent learns
to take actions that maximise the discounted future reward (discounted to make rewards
received further in the future less important for the present calculations).
Various RL
algorithms exist, with two key types being value-based or policy-based. In this paper, we
focus on the set of approaches known as model-free, where an agent does not know the
model of how the environment may respond to their actions - we believe that this approach
applies intuitively to uncertain social situations where other agents whose behaviour is not
directly predictable constitute a part of the environment.
A popular value-based RL algorithm is Q-Learning, introduced by Watkins and Dayan
(1992), where an agent learns the ‘value’ of each possible state-action pair Q(s, a). The
12

--- Page 13 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Action1
Action2
State1
Q(Action1 
| State1)
Q(Action2 
| State1)
State2
Q(Action1 
| State2)
Q(Action2 
| State2)
2. Policy-based RL (e.g., PPO)
1. Value-based RL (e.g., Q-Learning)
1.1 Tabular Q-Learning
1.2 Deep Q-Network (DQN)
State
Q(Action1 | State)
Q(Action2 | State)
Policy Network
State
P(Action1)
P(Action2)
Figure 3: RL architectures for a hypothetical environment with two possible states and two
actions. In tabular Q-learning (1.1) (Watkins & Dayan, 1992), an agent learns a
direct mapping from every state to the value Q of taking each possible action in
that state. In DQN (1.2) (Mnih et al., 2015), an agent trains a neural network,
which takes a representation of the state as input and outputs the associated
Q-value for each possible action. In policy-based methods, such as PPO (Schul-
man et al., 2017), an agent learns a policy model, which maps input states to a
probability P of taking each action in that state (in practice, policy-based RL
often also uses a separate value model/network for estimating the value V of a
given state, not pictured here). The use of neural networks allows for function
approximation, which means that not all states need to be observed during train-
ing for an agent to learn a (theoretically) general representation.
value represents the estimated discounted cumulative reward an agent may expect to receive
by taking this action in this state, and assuming they act optimally from then on. Two
versions of Q-learning exist: a tabular version for small state spaces and Deep Q-Network,
or DQN (Mnih et al., 2015) for value function approximation in state spaces too large to
learn directly. As shown in Figure 3, in tabular Q-learning, the learned value function
constitutes a table mapping every state-action pair to the corresponding Q-value. In DQN,
on the other hand, the learned representation is a tuned neural network which approximates
the state-action value function (Mnih et al., 2015), which takes a state vector representation
as input and returns the relative value of taking each possible action as an output. It is
this representation that allows DQN agents to generalise knowledge across states, enabling
them to choose actions based on past experience even if they have not seen this particular
state before.
These representations and the learned value functions can then be used to choose
actions according to a certain policy π(st) - for example, using an ϵ-greedy policy an agent
would take a ‘greedy’ action most of the time, i.e., the action with the greatest estimated
Q-value available from this state, but act randomly ϵ% of the time, sampling uniformly at
random from the available action space A. The random exploration in this policy allows
for new states to be explored by the agent, an essential step in learning via online RL.
In policy-based methods such as PPO (Schulman et al., 2017), an agent learns a policy
function π(st) (which informs the agent how to act in certain situations to achieve optimal
expected reward). In practice, many policy-based methods also require an agent to learn a
separate value function V (for estimating the value of certain states for faster convergence).
As in value-based methods, these functions can be approximated with neural networks to
13

--- Page 14 ---

Tennant, Hailes, & Musolesi
allow for greater generalisability. Here, the agent learns on-policy, adjusting its strategy as
it explores the space of possibilities in the environment.
The problem of moral alignment is fundamental in multi-agent environments, in which
agents (and, possibly, humans) with potentially different or competitive goals interact.
In these cases, multiple players learn (i.e., iteratively update their value and/or policy
estimates) in parallel, and, for each agent, their opponent(s) constitute a part of the en-
vironment. The state for a player can then be defined as a history of their opponents’
previous moves. We will now explore four examples of the use of RL for learning morality
via explicitly defined principles, illustrating the potential of the hybrid methodology which
we argued for in Section 2.3.
3.2 Case Study: Morally-constrained Reinforcement Learning
Taking inspiration from the full top-down tradition, researchers have used logic to define
constraints for training RL agents. For example, Neufeld et al. (2022) use defeasible deontic
logic to implement a normative supervisor onto a learning agent. This supervisor takes in a
proposed input action set, checks these for compliance against a set of norms, and outputs a
reduced set of actions for an agent to choose from - this can either be a strictly ‘legal’ set of
actions, or a relaxed set of ‘permissible’ actions if no fully satisfactory options are available
in the strict set.
The ‘ethical’ dimension in that work is implemented as a centralised
supervisor mechanism overseeing an agent during both learning and deployment, and - as
discussed - the normative constraints are hard-defined, which makes this the most top-down
of our case studies.
3.3 Case Study: Constitutional AI
As a second case study, we present the example of Constitutional AI, developed and imple-
mented by Bai et al. (2022). This approach is specific to the type of systems known as Large
Language Models (LLMs), which were originally developed for the purpose of next-token
prediction or text completion. Ethically-informed RL is used here at the fine-tuning stage,
i.e., after a model has been pre-trained on a large amount of linguistic data. As such, the
end product of this process is not an agent but a predictive system; however, as we discuss
below, the ethical fine-tuning step of the training can be perceived as agent-based, and
makes the behaviour of the LLM more goal-directed, so still has relevance to the present
discussion.
Constitutional AI involves a set of LLMs providing feedback to some LLM being cur-
rently trained. The constitutional methodology has been proposed as a potentially safer,
more controlled and interpretable alternative to the fully bottom-up RLHF approach used
in other LLMs (Ziegler et al., 2019). The LLMs providing feedback represent a ‘consti-
tution’ of different principles, where each principle is defined via explicit prompts (e.g.,
‘Please choose the assistant response that’s more ethical and moral. Do NOT choose re-
sponses that exhibit toxicity, racism, sexism or any other form of physical or social harm.’).
The principles themselves are based on a combination of human defined preferences such
as the UN Declaration of Human Rights, certain digital companies’ terms of service (to
reflect the more recent digital dimensions of safety), and a set of other preferences defined
by a team of researchers behind Constitutional AI (Bai et al., 2022) and others (Glaese
et al., 2022). The feedback from these principles is used to train a reward model for rating
the outputs of the to-be-tuned LLM as ‘good’ or ‘bad’ according to its core principle.
Using the feedback from this reward model as a training signal, the weights of the
LLM are fine-tuned with RL. Thus, the model is fine-tuned to be more likely to produce
outputs which would be considered safe by a constitution of potential ‘critic’ models with
14

--- Page 15 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
diverse preferences. An extension of this approach based on crowd-sourced constitutional
principles is called Collective Constitutional AI (Anthropic, 2024) and may prove promising
in the future in generating more generally or pluralistically aligned agents.
In summary, according to this methodology the moral principles are explicitly defined
via prompts, but the mapping between those principles and a change in behaviour (i.e.,
the change in language model outputs) is based on a learned representation which is very
difficult for humans to interpret, thus posing a disadvantage in terms of safety. This makes
Constitutional AI the most bottom-up approach of our case studies. Furthermore, while
the approach is certainly promising, it must be noted that Bai et al. (2022) only managed to
use the constitutional principle for improving a model’s harmlessness - it remains to be seen
how successful the methodology would be at promoting other values such as helpfulness.
3.4 Case Study: Reinforcement Learning in Social Dilemmas
Next, we consider a case study that combines top-down principles and learning in a more
equal weighting. The approach described here relies on the domain of two-player general-
sum games known as social dilemmas (Axelrod & Hamilton, 1981; Rapoport, 1974). We
introduce these games subsequently, before describing learning agent implementations.
Though these games constitute stark simplifications of reality, they are intended to model
and reflect the general underlying structure of a multitude of multi-agent everyday situa-
tions.
3.4.1 Social Dilemma Matrix Games
Social dilemma games simulate situations in which each agent makes decisions facing a
trade-off between individual interest and societal benefit. A widely studied subset of these
games is the two-player, two-action matrix game, in which players simultaneously choose
an action (e.g., Cooperate or Defect) without the opportunity to communicate.
Each
player then receives a certain payoff which depends on the pair of actions chosen. Higher
payoff here represents the fact that an outcome is preferred by the player. What makes
it a dilemma is the fact that players maximising their individual payoffs are likely to
learn policies that end up being sub-optimal in terms of long-term outcomes, both for the
individual and for the society of agents.
Three classic matrix dilemma games from Economics and Philosophy that are relevant
to moral choice are the Prisoner’s Dilemma (Rapoport, 1974), Volunteer’s Dilemma (or
‘Chicken’; Poundstone, 1993), and Stag Hunt (Skyrms, 2001) - payoffs for the row vs.
column player are presented in Table 2. In the Prisoner’s Dilemma, mutual cooperation
would achieve a Pareto-optimal outcome of 3 points each (a desirable situation in which one
player cannot be made better off without disadvantaging the other) - but each individual
player’s best response is to defect due to greed (facing a cooperator, they benefit from
defecting and getting the highest payoff equal to 4) and fear (facing a defector, they suffer by
cooperating and getting the lowest payoff equal to 1). In the one-shot game, this reasoning
applied by both players leads to mutual defection and thus a sub-optimal outcome, in which
both players only get a payoff equal to 2. In the Volunteer’s Dilemma, a selfish or rational
player may choose to defect due to greed (i.e., not volunteer in hope that someone else
does), but if both do so, both obtain the lowest possible payoffs (i.e., no one volunteers,
and the society suffers). Finally, in the Stag Hunt game, two players can cooperate in
hunting a stag and thus obtain the greatest possible payoff each; however, given a lack of
trust between the players (i.e., each player fears a non-cooperative partner), either may be
tempted to defect and hunt a hare on their own instead, decreasing both players’ payoffs
as a result.
15

--- Page 16 ---

Tennant, Hailes, & Musolesi
IPD
C
D
C
3,3
1,4
D
4,1
2,2
IVD
C
D
C
4,4
2,5
D
5,2
1,1
ISH
C
D
C
5,5
1,4
D
4,1
2,2
Table 2: Payoff matrices for each step of the Iterated Prisoner’s Dilemma (IPD), Iterated
Volunteer’s Dilemma (IVD) & Iterated Stag Hunt (ISH) games, in which players
are motivated to defect by either greed (IVD), fear (ISH), or both (IPD).
Thus, in all three games the best-response (i.e., ‘rational’) strategies are not the ones
leading to the better mutual outcome. Gauthier (1987) argued that repeated versions of
these dilemma games in particular are relevant to morality, since, with repeated interaction,
complex sets of strategies and social dynamics can evolve - for example, involving actions
to punish one’s opponents for past wrongdoing, or to influence their future actions. Due to
instabilities in the multi-agent environment, calculating predicted equilibria in these situ-
ations is not always computationally feasible, so simulation methods are required in order
to study potential emergent behaviours and outcomes (Lasquety-Reyes, 2019; Tolmeijer
et al., 2021).
Other types of games in which it is possible to model human morality are sequential
games (Harsanyi, 1961; Leibo et al., 2017; Jaques et al., 2019), games with more than
two players (Liebrand, 1983; Hardin, 1968), and games with incomplete information, first
introduced by Harsanyi (1995). We provide these in Appendix A for context, but focus
on the simpler and more abstract two-player matrix games in the subsequent formalisation
due to their generalisability to a wide range of situations.
3.4.2 Reinforcement Learning in Social Dilemmas
Repeated versions of the games can be implemented as learning environments for RL agents.
A social dilemma environment can be implemented for RL agents as a two-player iterated
game, played over T iterations (Littman, 1994). This is summarised in Figure 4. At each
iteration, a moral player M and an opponent O play the one-shot matrix game correspond-
ing to a classic social dilemma (see Table 2 for examples). At every time step t, the learning
agent M observes a state, which is the pair of actions played by O and M at the previous
time step t−1: st
M = (at−1
O , at−1
M ), and chooses an action (Cooperate or Defect) simultane-
ously with the opponent O: at
M, at
O ∈{C, D}. The player M then receives a reward Rt+1
M
and observes a new state st+1
M . In traditional RL, this reward would be provided by the
environment (i.e., extrinsic reward), and in the social dilemma games it would correspond
directly to the payoffs from the game (presented in Table 2).
3.4.3 Moral Preferences as Intrinsic Rewards
Intrinsic motivation is a concept originating in human Psychology (Deci & Ryan, 1985),
whereby humans’ choices (such as the choice of a job) may not be associated with some ex-
ternal reward (such as money), but rather be driven by internal values (such as autonomy,
excellence or intellectual curiosity, suggested by Wrzesniewski et al., 1997). In Philoso-
phy, intrinsic motivation may align to the concept of will (Aristotle, 2019) or happiness
(Bentham, 1780).
Deci et al. (1999) and Oudeyer and Kaplan (2007) draw interesting parallels between
intrinsic motivation and rewards. The implication for RL is that effective learning can
result from modifying the agent such that they take into consideration an internal reward
16

--- Page 17 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Game Environment
 
Agent M 
Opponent O
State sM
t = (aO
t-1,aMt-1)
Game Reward RM, extr 
Action aMt 
Moral
Reward
RM, intr 
Figure 4: A step in a two-player game modelled as an RL process, from the point of view
of a learning moral agent M playing against a learning opponent O. Agent M
calculates their moral (intrinsic) reward according to their own ethical framework,
which may or may not consider the game (extrinsic) reward coming from playing
the dilemma.
signal rather than only rewards from the environment. Early successes with this approach
were reported by Chentanez et al. (2004) in curiosity-driven exploration, where curiosity
was modelled as an intrinsic reward obtained when the agent visits unfamiliar states.
The intrinsic rewards framework is directly applicable to the idea of learning morality
from experience. A small set of existing works in Multi-Agent RL modified the reward
signal for agents in social dilemma games to embed an internal moral value or preference
into reward functions (Capraro & Perc, 2021; Hughes et al., 2018; McKee et al., 2020;
Tennant et al., 2023, 2024a). In these works, moral preferences have either been expressed
as an operation on the extrinsic rewards (applying some function over the player’s own
reward and that of their opponents), or a conditional function based on actions performed
previously. A related line of work modifies reward functions to include an awareness of the
opponents’ learning (Foerster et al., 2018; Jaques et al., 2019) - but these are not strictly
morality-focused implementations and thus lie beyond the scope of the studies reviewed
here.
A visualisation of the intrinsic rewards approach is presented in Figure 4.
In this
formulation, for player M, we contrast traditional agents that learn according to an extrinsic
game reward RMextr, which is simply the payoff associated with the joint actions at
M, at
O
(as defined in Table 2), versus agents that learn according to an intrinsic reward RMintr,
based on some moral principle. In Section 3.4.4, we expand on the types of principles that
can be encoded as intrinsic rewards.
In practice, both extrinsic and intrinsic rewards can be combined in a multi-objective
manner (Vamplew et al., 2018) to create an agent able to pursue multiple goals (for example,
trying to obtain both moral reward and the reward from the task at hand - Noothigattu
et al., 2019). This was the approach used by Chentanez et al. (2004) to create their ‘curious’
yet task-specific agent. Furthermore, multi-objective RL approaches can also be used to
combine multiple intrinsic moral rewards to create a multi-faceted moral agent (e.g., see
the multi-objective moral agent from Tennant et al., 2023), which allows for the creation
of more complex and comprehensive moral agents.
17

--- Page 18 ---

Tennant, Hailes, & Musolesi
This case study implements a decentralised RL approach where each agent chooses an
action in the game without a central planner. A parallel line of work exists in the modelling
and ethics literature, where an ‘ethical’ agent is implemented as a centralised mechanism on
the environment - this has applications in entirely different domains such as governmental
policy design (Koster et al., 2022), and lies beyond the scope of this work, which focuses
on the moral alignment of individual agents.
3.4.4 Formalising Existing Ethical Frameworks as Rewards for AI Agents
A variety of moral frameworks has been developed over the millennia in the fields of Moral
Philosophy, Psychology, Biology and Economics. We review a representative set of these
in Table 3, formulating them as potential reward functions for agents in two-player games.
A growing body of RL work demonstrates that mathematical formulations of these frame-
works are able to effectively encourage agents to learn more prosocial and cooperative
behaviour in social settings (Hughes et al., 2018; McKee et al., 2020; Tennant et al., 2023,
2024a).
We classify possible moral agent types in Table 3 into Consequentialist or Norm-based.
Consequentialist morality focuses on the outcomes or consequences of an action. In dilemma
games, this can be easily implemented as an operation on the two players’ payoffs, including
objective functions that are Utilitarian (Bentham, 1780), defining actions as moral if they
maximise total utility for all agents in a society, or Altruistic (Levine, 1998), where an agent
is inclined to maximise their opponent’s winnings, perhaps without even considering their
own. Consequentialist morality also includes fairness-based objective functions. These can
be based on the difference between two players’ rewards, including the inequity aversion
models of Fehr and Fischbacher (2002, 2004a), or other calculations of the ratio between
payoffs with different preferences for fair or equal outcomes (Bolton & Ockenfels, 2000;
Gini, 1912; Rapoport, 1974). Finally, consequentialism also accounts for the principles of
distributive justice of Rawls (1971), in which agents distribute resources without knowing
where they will end up in that distribution.
Norm-based morality, on the other hand, focuses on defining actions as moral so long
as they adhere to a society’s external norms or to a specific agent’s duties, regardless of the
consequences further down the line. This framework includes the Deontological ethics of
Kant (1785), which identifies specific acts as morally required, permitted or forbidden. An
example norm for dilemma game-playing agents may be conditional cooperation, in which
an agent is expected to cooperate against a cooperative opponent (Fehr & Fischbacher,
2004a). Further norm-based objective functions have been formalised by Capraro and Perc
(2021), Kimbrough and Vostroknutov (2023), Krupka and Weber (2013) and Levitt and
List (2007), who propose various weights on personal versus social importance of the norm
at hand.
A third type of ethical framework that is often distinguished is Virtue Ethics of Aristotle
(2019) - in this line of reasoning, moral agents act according to their certain internal
virtues. In practice, these virtues themselves often have Consequentialist or Norm-based
foundations - consider, for example, the virtues of fairness or care, respectively (Graham
et al., 2009, 2013). The key distinction of Virtue Ethics is that a single agent may rely
on more than one type of virtue, and different agents may weigh the virtues differently
against one another (Aristotle, 2019; Graham et al., 2009), so a more expressive way of
modelling virtue ethics might be through a weighted, multi-objective paradigm - such as
that suggested by Vamplew et al. (2018).
In Table 3, we additionally distinguish agents by the external or internal nature of their
moral motivation - while each of these frameworks can be formalised as an intrinsic reward
function for the RL agent, sometimes the moral aspect of the intrinsic motivation comes
18

--- Page 19 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Moral Agent
Type
References
Formulation in terms of
reward
External /
Internal
Consequentialist
/ Norm-based
Utilitarian
or Altruistic
Bentham, 1780;
Andreoni &
Miller, 2002;
Charness &
Rabin, 2002;
Ledyard, 1995;
Levine, 1998
Sum of all players’ payoffs,
with various weights on on
own vs. others’ payoffs.
either
Consequentialist
Inequity
averse
Fehr &
Schmidt, 1999;
Fehr &
Fischbacher,
2004a
Difference between own
payoff and others’ payoffs,
with parameters for
advantageous vs
disadvantageous inequity
between them.
Internal
Consequentialist
Equality- or
Fairness-
preferring
Gini, 1912;
Rapoport,
1974; Bolton &
Ockenfels, 2000
Ratio (e.g., Gini
coefficient) between own
and opponent’s payoffs; or
a weight on the distance
between own payoff vs fair
share.
Internal
Consequentialist
Following a
‘Veil of
Ignorance’
Harsanyi, 1961;
Rawls, 1971
E.g., minimum payoff of
any player (assuming an
agent chose to distribute
payoffs not knowing where
they would end up in the
distribution).
either
Consequentialist
Deontological
Kant, 1785;
Capraro &
Perc, 2021;
Kimbrough &
Vostroknutov,
2023; Krupka
& Weber, 2013;
Levitt & List,
2007
Positive (or negative)
reward if the action taken
adheres to (or violates) a
pre-defined norm. Agent
may enforce norm in
others or not.
External
Norm-based
Virtue
Ethics (can
be based on
other types
above)
Aristotle, 2019;
Graham et al.,
2013;
Rapoport, 1974
Reward for adhering to a
single specific virtue (e.g.,
cooperativeness), or a mix
of virtues (e.g., sum
cooperativeness + equality
rewards).
Internal
either or both
Table 3: Moral frameworks proposed in past literature in Philosophy, Psychology, Biology
and Economics, and potential implementations in terms of rewards for RL agents.
from outside the agent themselves. An example of this is where certain moral norms exist
externally in a society, so the agent prefers to adhere to them in their individual behaviour.
19

--- Page 20 ---

Tennant, Hailes, & Musolesi
The final step for formalising morality as intrinsic motivation for RL agents, then, is to
formulate precise mathematical definitions of rewards based on these frameworks. Using the
domain of social dilemmas introduced above, Tennant et al. (2023) propose a formulation
in terms of actions and/or outcomes at some time step t in a two-player, two-action social
dilemma game. For illustration, we present their mathematical definitions of five types of
moral rewards in Table 4 (Tennant et al., 2023).
Moral Agent Type
Moral Reward Function
Utilitarian
Rt
Mintr = Rt
Mextr + Rt
Oextr
Deontological
Rt
Mintr =
(
–ξ,
if at
M = D, at−1
O
= C
0,
otherwise
Virtue-equality
Rt
Mintr = 1 −
|Rt
Mextr−Rt
Oextr|
Rt
Mextr+Rt
Oextr
Virtue-kindness
Rt
Mintr =
(
ξ,
if at
M = C
0,
otherwise
Virtue-mixed
Rt
Mintr =





β ∗(1 −
|Rt
Mextr−Rt
Oextr|
Rt
Mextr+Rt
Oextr
) + (1 −β) ∗ˆξ,
if at
M = C
β ∗(1 −
|Rt
Mextr−Rt
Oextr|
RMt
extr+Rt
Oextr
),
otherwise
Table 4: Definitions of a sub-set of intrinsic moral reward types, from the point of view of
the moral agent M playing a social dilemma game versus an opponent O.
In this set, given two players M and O, Consequentialist morality is implemented
as operations on the two players’ extrinsic rewards Rt
Mextr and Rt
Oextr. Specifically, for a
Utilitarian agent, the reward is simply the sum of the two players’ payoffs. For an equality-
focused agent Virtue-equality, the reward is the ratio of the two payoffs, based on the Gini
coefficient (Gini, 1912), transformed so that larger values mean greater equality between
the two agents.
Norm-based morality, on the other hand, is operationalised in terms of a positive reward
for an agent whose action at
M adheres to a given norm, or a negative reward for actions vi-
olating a given norm. For example, a Deontological agent following the norm of conditional
cooperation (defined above) receives a negative reward of value ξ for defecting against an
opponent who previously cooperated. The other norm-based agent Virtue-kindness follows
a simple cooperative norm, obtaining a positive reward ξ for cooperating, regardless of
what their opponent did previously.
Finally, these examples also outline one multi-objective reward function Virtue-mixed,
which linearly combines the two separate virtues ‘equality’ and ‘kindness’, with a weighting
parameter β, and a parameter ˆξ used to fit the ‘kindness’ element of the reward to the same
scale as equality.
Tennant et al. (2023) implement the five moral intrinsic rewards defined in Table 4 (as
well as a Selfish baseline agent) and show that Q-learning agents learning against a variety
of opponents are able to learn optimal moral policies given sufficient exploration. A further
study by Tennant et al. (2024a) extends this analysis to populations involving a partner
selection mechanism and a larger amount of possible prosocial and antisocial moral agent
types.
20

--- Page 21 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
3.5 Case Study: Fine-tuning LLM Agents with Intrinsic Rewards
Finally, to complement the intrinsically moral RL agents described above, we consider the
case of fine-tuning LLM-based agents for moral alignment. This work relies on the use of
LLMs as decision-makers (Park et al., 2023; Vezhnevets et al., 2023; Wang et al., 2024a)
in strategic scenarios (Gandhi et al., 2023; Swanepoel & Corks, 2024; Zhang et al., 2024),
often studied using game-theoretic environments such as social dilemma games discussed
above (Akata et al., 2023; Fan et al., 2024). Thus, the approach of fine-tuning LLMs with
RL reconciles the previous implementations of hybrid moral alignment in pure-RL agents
with the more general and currently popular domain of LLM agents.
As discussed previously, the predominant approach for aligning LLMs to human values
is by training reward models on human preference data (i.e., RLHF), and fine-tuning an
LLM using that reward model, though non-RL approaches, such as DPO (Rafailov et al.,
2023), enable preference-based fine-tuning without the need for RL-based training. This
approach teaches the LLM the values that are implicit in the human preference data,
without any explicit definition of what they are. A core disadvantage of this, as discussed
in Section 2, is the lack of transparency interpretability and control, and the risks of reward-
hacking.
Tennant et al. (2024b) instead propose a methodology for fine-tuning LLMs based on
intrinsic rewards rather than human-generated preference data (as in the case of RLHF).
The intrinsic rewards in this approach are defined in terms of actions or consequences in a
specific environment, but the policies learned via such fine-tuning can, in theory, generalise
to other environments. Tennant et al. (2024b) present a study fine-tuning LLM agents
using the rich domain of social dilemmas described in Section 3.4. For LLM agents in
particular, decision-making scenarios or games can be expressed in the form of text, with
specific tokens corresponding to each action choice. During fine-tuning, the model learns
to associate certain action tokens and strategies with rewards, with online RL implemented
via on-policy methods such as PPO (Schulman et al., 2017, though offline implementations
are also possible, see Snell et al., 2023).
The results in Tennant et al. (2024b) offer some evidence of the ability of LLM agents
to generalise moral policies learned in one game to other environments characterised by a
similar game structure - specifically, from the IPD agent to four other 2x2 matrix games.
The challenges in this implementation include the fact that fine-tuning on a small set of
specific action tokens may make the models over-fit to those tokens - indeed, Tennant et al.
(2024b) observed that the fine-tuned model was more likely to produce the action tokens
in response to unrelated questions of a similar format. Nevertheless, overall, this work
suggests an interesting emerging direction in using intrinsic rewards as a hybrid and more
controllable and interpretable implementation of moral alignment in agentic LLM systems.
4. Evaluating Moral Learning Agents
4.1 Outcomes, Behaviours and Qualitative Assessment
After training such morally motivated agents, researchers must evaluate whether their
learning was ethically effective. This requires the definition of a set of outcome metrics.
Traditional Reinforcement Learning research would train agents in a specific simulated envi-
ronment and measure some population-level outcome such as cumulative reward. However,
as discussed in Section 2.2, further evaluation metrics must be designed to identify po-
tential reward-hacking behaviour of RL agents - in other words, one must also measure
concepts or behaviours that were not directly encoded in the agents’ reward functions. Ide-
ally, these measurements should be broad enough to cover a vast number of diverse ethical
21

--- Page 22 ---

Tennant, Hailes, & Musolesi
considerations in a wide range of scenarios. The challenges of this have been discussed by
Reinecke et al. (2023). As an illustration, in Section 4.2 below, we present an example set
of population-level outcome metrics that were proposed by Tennant et al. (2023) for the
case of social dilemma games. To complement this example of measuring RL agents in
social dilemma environments, we also present a discussion of how LLM-based agents can
be measured in terms of behavioural alignment (see Section 4.3).
On top of population-level outcomes, a game-theoretic evaluation of emerging be-
haviours may also be of interest, evaluating actions taken in the game over the course
of learning, and the extent to which these actions are aligned with moral norms. In so-
cial dilemmas, this must include a measurement of cooperation displayed by each agent
towards the end of the learning period as well as the emerging strategies (i.e., state-action
combinations chosen by the agent). This allows for a non-consequentialist evaluation of
learned behaviours and policies, and provides better insight for norm-based morality.
Finally, an alternative means of evaluation could include a qualitative assessment by a
human who interacts with an agent. Within the domain of autonomous vehicles, large-scale
evaluations of hypothetical agent behaviours have been conducted by Awad et al. (2018)
using survey studies, and focusing on the trolley problem (Thomson, 1976) in particular
as an agent environment. Much more qualitative evaluation is required in other domains
and sets of problems to understand human perception of AI-assisted decision making more
generally.
4.2 Example: Measuring Outcomes in Social Dilemma Environments
In the dilemma scenarios presented in Section 3.4, the choice of one agent affects the out-
comes of another. Thus, it is possible that scenarios will arise in which agents intentionally
designed with a certain morality (e.g., maximise ‘collective reward’) actually display be-
haviour that maximises their desired outcome at a cost of some other important outcome
(e.g., ‘equality’). For this purpose, on top of analysing individual rewards, researchers have
highlighted the importance of measuring a range of population-level outcomes (Hughes
et al., 2018; Leibo et al., 2017; Tennant et al., 2023).
The most popular social outcome metric is the collective payoff for all agents - used by
Leibo et al. (2017), Hughes et al. (2018), McKee et al. (2020). Additional moral evaluation
metrics can include a measure of equality such as the Gini coefficient (Gini, 1912), and
an egalitarian measure of the minimum payoff obtained by any agent in the population
on every iteration (Rawls, 1971). These three social outcome metrics were formalised in
Tennant et al. (2023) as a cumulative return G (i.e., the total reward accumulated over all
the T iterations of an iterated game) for both players M and O as follows:
Gcollective =
T
X
t=0
(Rt
Mextr + Rt
Oextr)
(1)
GGini =
T
X
t=0
(1 −|Rt
Mextr −Rt
Oextr|
Rt
Mextr + Rt
Oextr
)
(2)
Gmin =
T
X
t=0
min(Rt
Mextr, Rt
Oextr).
(3)
In Tennant et al. (2023), the five agents from Table 4 are systematically evaluated on
three distinct social dilemma games in terms of the cumulative outcomes defined above and
cooperation levels and strategies. The results show that - with sufficient exploration and
learning time - all types of moral agents are able to learn fully cooperative policies, though
22

--- Page 23 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
the ‘equality’ definition produces the least efficient learning agent, which is reflected in the
social outcome metrics.
4.3 Example: Measuring Moral Behaviour in Language Models
The domain of Large Language Models (LLMs) provides a different set of challenges for
measurement. Its inputs and outputs are open-ended, such that the possible action space
for a single generated token is as large as the vocabulary size associated with the model.
Furthermore, the users of the model are likely to have diverse moral preferences of its users
(discussed above). This makes it harder to define a standard set of metrics to evaluate
the moral learning of LLMs. Nevertheless, a large set of benchmark metrics and data sets
have already been proposed for measuring morality in these systems (see Hendrycks et al.,
2021a, 2021b; Pan et al., 2023; Reinecke et al., 2023). Capitalising on the open-ended
nature of human language, studies such as Tennant et al. (2024b) have also assessed the
generalisation of moral policies from one environment to others, though more remains to
be done in terms of assessing their performance in real-world scenarios.
5. Outlook & Implications
Our discussion suggests that the traditional fully top-down (e.g., rule-based) methods, or
the currently popular fully bottom-up approaches to AI morality and safety (e.g., fine tun-
ing of LLMs based on Reinforcement Learning from Human Feedback), whilst intuitively
attractive because of the control they seem to impose (top-down), or the generality they
may offer (bottom-up), are limited and pose potential risks for systems deployed in the
real world. We motivate the use of a combination of interpretable top-down quantitative
definitions of moral objectives, based on existing frameworks in fields such as Moral Phi-
losophy, with the bottom-up advantages of trial-and-error learning from experience via RL.
We argue that this hybrid methodology provides a powerful way of studying and imposing
control on AI systems while enabling adaptation to dynamic environments. We review four
case studies combining moral principles with learning, which provide proof-of-concept for
the potential of this hybrid approach in creating more prosocial and cooperative agents.
We hope that the unifying framework defined in this paper helps future practitioners and
policymakers identify new possible avenues for future work.
We appreciate the fact that quantifying morality by translating complex moral frame-
works into elementary reward functions, learning constraints or textual principles in this
way is certainly a simplification of reality. Nevertheless, the original moral philosophical
frameworks discussed in this work might be seen as a form of abstraction and, in a sense,
simplification of the complex and multi-faceted human condition, and yet these have served
the field for centuries.
We believe there is a need to study these hybrid approaches in a variety of social envi-
ronments for morally-informed learning, including other social dilemma games and games
involving a large number of players. The specific moral reward functions proposed in Tables
3 and 4 and in a number of existing practical works (Capraro & Perc, 2021; Hughes et al.,
2018; McKee et al., 2020; Tennant et al., 2023), as well the other methodologies reviewed
(Bai et al., 2022; Neufeld et al., 2022), are a starting point for building more sophisticated
moral agents, including those based on more than one moral objective (Vamplew et al.,
2018). In general, the reward-based methods have a disadvantage of the fact that they rely
on a clear scalar payoff structure, and in the case of some of the intrinsic moral rewards
proposed - a discrete set of actions. An open research question remains about how to obtain
this reward structure in open-ended tasks while still maintaining principled control over
the morality implemented in the reward.
23

--- Page 24 ---

Tennant, Hailes, & Musolesi
We hope that, in the future, researchers can build on these ideas and further investigate
the effectiveness of each of the proposed moral frameworks experimentally. As discussed,
the moral preferences of the target audience of any AI system will vary depending on their
cultural and political norms (Graham et al., 2013) - in this paper, we did not aim to
promote any one moral framework, but instead demonstrated the ways in which different
moralities can be implemented using the same methodology of intrinsic rewards.
Finally, it is worth noting that approaches described above can bring benefit back to
the disciplines they are founded on and took inspiration from. In particular, the proposed
methodology can be used to reflect upon and understand different moral frameworks and
their impacts, especially in complex situations. For example, it can be used for simulating
human societies, studying the outcomes deriving from the presence of agents with specific
moral preferences, or to study emergent behaviours in societies composed of agents with
different moral principles. In general, this can be seen as a practical example of ‘Computa-
tional Philosophy’ (Mayo-Wilson & Zollman, 2021). Moreover, in general terms, modelling
moral behaviour as a reward-maximising ϵ-greedy choice made by a continually learning
agent can provide insights for Evolutionary Game Theory. Our simulations with learning
agents can discover how certain moral behaviours can evolve (and might have evolved) in a
society given a payoff structure and different distributions of preferences and norms within
a population. Additionally, an analysis of the learning dynamics of agents can provide
insights for Developmental Psychology, possibly offering a way to test various theories of
moral development in children (Gilligan, 1982; Gopnik, 2009; Kohlberg, 1975).
6. Conclusion
In this paper, we have made the case for the use of learning with explicitly defined moral
principles for developing morality in AI agents, contrasting it with more traditional top-
down implementations in AI safety and ethics, and the more recent entirely bottom-up
methods for learning implicit values from human feedback, such as those used for fine-
tuning LLMs. We have suggested RL as one effective mechanism for learning morality
from experience in a given environment, and reviewed a set of case studies to analyse
different moral alignment approaches that have been implemented for agentic systems in
practice. In two of these case studies (based on the pure-RL or LLM domains), we have
outlined a hybrid methodology in which agents learn morality via intrinsic rewards based on
classic moral frameworks, and presented a formalisation of a set of specific reward functions
using social dilemma environments. We have also reviewed solutions based on alternative
approaches, such as constrained RL or fine-tuning LLMs from constitution-based feedback.
Finally, we have proposed an example of potential evaluation of the moral outcomes and
behaviours emerging from interactions between different agents over time, and outlined the
existing open challenged in this area.
We hope that this article can motivate further work in the area of developing moral
AI agents via learning with the help of top-down explicit moral principles (i.e., in a hybrid
way). While there are substantial challenges in implementing the proposed design guidelines
in practice, we believe it provides a promising avenue for addressing the growing safety
concerns around emerging advanced AI.
24

--- Page 25 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Definitions
Concept
Definition
Agent
An entity able to take actions / make decisions or choices in an environment.
Bottom-up
Development of a system / inference of values through experience, organi-
cally, without planning the general architecture / constraints / components
in advance.
An example is Reinforcement Learning of desired behaviours
from human demonstrations (e.g., via Inverse RL or RLHF).
Extrinsic Reward
A reward signal provided by the environment to the agent. For example,
in a Prisoner’s Dilemma, the game payoff for a player would constitute the
extrinsic reward.
Intrinsic Reward
A reward signal based on an internal value, preference or principle of the
agent, rather than received from the environment. For example, in humans,
the intellectual enjoyment in a job is an intrinsic ‘reward’, while the associated
pay is the extrinsic ‘reward’. In AI agents, intrinsic rewards can be based on
a moral preference for how group rewards should be distributed, or a moral
norm defining how agents should and should not act in certain situations (see
below).
Moral framework
[In Philosophy] A set of principles for how humans / agents should behave
morally in a society (e.g., Utilitarianism, Deontological Ethics, Virtue Ethics).
Moral norm
A norm in society about what constitutes moral behaviour. An example is
‘not defecting against a cooperator’.
Moral value or
preference
An internal representation of a moral principle. An example is a preference
for a certain way of distributing resources (i.e., ‘fairness’), or a motivation to
‘care’ for others.
Social Dilemma
A situation where there is a trade-off between short-term individual reward
and long-term collective outcomes.
An example is the two-player matrix
dilemma game with two possible actions (Cooperate or Defect), where play-
ers choose actions simultaneously without the ability to communicate, and
receive payoffs based on the joint action.
Top-down
Development of a system by defining / planning the architecture and explic-
itly defining all components, requirements and constraints in advance. An
example is a system with moral rules based on deontic logic.
Appendix A. Other Games Involving Morality
Other types of games in which it is possible to model human morality are sequential games
(Harsanyi, 1961; Leibo et al., 2017; Jaques et al., 2019), games with more than two players
(Liebrand, 1983; Hardin, 1968), and games with incomplete information, first introduced
by Harsanyi (1995).
Sequential games model social situations in which one player takes an action first, then
the other chooses how to respond given how the first player acted. An example of this
is the Ultimatum game (Harsanyi, 1961), in which the first player offers a way to split a
sum of money, and the second player either accepts the split or rejects it, in which case
neither player gets anything. Here the first player may be incentivised to keep a larger sum
for themselves, but they risk pushing the opponent too far and ending up with nothing.
Applied to ethics, the Ultimatum game can model the principle of fairness in both players
(fairness in one’s own behaviour for the proposer, and punishment for unfair behaviour by
the receiver), providing an interesting test bed for moral learning agents.
25

--- Page 26 ---

Tennant, Hailes, & Musolesi
Games with more than two players are an extension of the dyadic dilemma games
presented in the previous section, but they involve an entire population playing at once.
The Prisoner’s Dilemma can be extended to a social version, for example by considering
the problem of pollution and how each individual contributes to it in a society (Liebrand,
1983). The Volunteer’s Dilemma can also easily be extended to a case in which the society
(and every player in it) benefits from someone else volunteering in their community, but
each player is individually motivated to avoid volunteering themselves. Collectively, this
type of situation is known as the Tragedy of the Commons (Hardin, 1968). More recently,
environments have been created specifically for training RL agents in such social dilemmas
with spatial and temporal resolution, for example in the games Gathering (Leibo et al.,
2017) and Cleanup (Jaques et al., 2019). Multi-player dilemmas can introduce an interest-
ing aspect of partial observability (i.e., incomplete information), as one agent may not be
certain about what action another agent took previously just by observing the payoffs. This
creates a layer of anonymity that can influence the development of certain moral norms in
a society.
References
Abbeel, P., & Ng, A. Y. (2004). Apprenticeship learning via inverse reinforcement learning. In
Proceedings of the 21st International Conference on Machine Learning (ICML’04).
Abel, D., MacGlashan, J., & Littman, M. L. (2016). Reinforcement learning as a framework for
ethical decision making.
In Proceedings of the AAAI Workshop: AI, Ethics, and Society
(AIES’16), pp. 54–61.
Akata, E., Schulz, L., Coda-Forno, J., Oh, S. J., Bethge, M., & Schulz, E. (2023) Playing repeated
games with Large Language Models. arXiv Preprint. arXiv:2305.16867.
Alshiekh, M., Bloem, R., Ehlers, R., K¨onighofer, B., Niekum, S., & Topcu, U. (2018). Safe rein-
forcement learning via shielding. In Proceedings of the 32nd AAAI Conference on Artificial
Intelligence (AAAI’18), Vol. 32, pp. 2669–2678.
Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Man´e, D. (2016) Concrete
problems in AI safety. arXiv Preprint arXiv:1606.06565.
Anastassacos, N., Hailes, S., & Musolesi, M. (2020). Partner selection for the emergence of cooper-
ation in multi-agent systems using reinforcement learning. In Proceedings of the 34th AAAI
Conference on Artificial Intelligence (AAAI’20), Vol. 34, pp. 7047–7054.
Anderson, M., Anderson, S. L., & Armen, C. (2006). MedEthEx: a prototype medical ethics advisor.
In Proceedings of the 18th Conference on Innovative Applications of Artificial Intelligence
(IAAI’06), Vol. 21, pp. 1759–1756.
Andreoni, J., & Miller, J. (2002). Giving according to GARP: An experimental test of the consistency
of preferences for altruism. Econometrica, 70(2), 737–753.
Anthropic
(2024)
Collective
Constitutional
AI.
https://www.anthropic.com/index/
collective-constitutional-ai-aligning-a-language-model-with-public-input
Ac-
cessed on 14 April 2024.
Aristotle (2019). The Nicomachean Ethics. Translated, with Introduction, Notes, and Glossary by
Terence Irwin. Hackett Publishing Company.
Arkoudas, K., Bringsjord, S., & Bello, P. (2005). Toward ethical robots via mechanized deontic logic.
In AAAI Fall Symposium on Machine Ethics, pp. 17–23.
Asimov, I. (1950). I, Robot. Gnome Press.
Awad, E., Dsouza, S., Kim, R., Schulz, J., Henrich, J., Shariff, A., Bonnefon, J.-F., & Rahwan, I.
(2018). The moral machine experiment. Nature, 563(7729), 59–64.
26

--- Page 27 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Awad, E., Levine, S., Anderson, M., Anderson, S. L., Conitzer, V., Crockett, M., Everett, J. A.,
Evgeniou, T., Gopnik, A., Jamison, J. C., Kim, T. W., Liao, S. M., Meyer, M. N., Mikhail,
J., Opoku-Agyemang, K., Borg, J. S., Schroeder, J., Sinnott-Armstrong, W., Slavkovik, M.,
& Tenenbaum, J. B. (2022).
Computational ethics.
Trends in Cognitive Sciences, 26(5),
388–405.
Axelrod, R., & Hamilton, W. D. (1981). The evolution of cooperation. Science, 211(4489), 1390–
1396.
Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini,
A., McKinnon, C., et al. (2022) Constitutional AI: harmlessness from AI feedback. arXiv
Preprint arXiv:2212.08073.
Bakker, M., Chadwick, M., Sheahan, H., Tessler, M., Campbell-Gillingham, L., Balaguer, J.,
McAleese, N., Glaese, A., Aslanides, J., Botvinick, M., et al. (2022). Fine-tuning language
models to find agreement among humans with diverse preferences. In Proceedings of the 36th
International Conference on Neural Information Processing Systems (NeurIPS’22), Vol. 35,
pp. 38176–38189.
Beckers, S., Chockler, H., & Halpern, J. Y. (2023). Quantifying harm. In Proceedings of the 32nd
International Joint Conference on Artificial Intelligence (IJCAI’23), pp. 363–371.
Bentham, J. (1780). An Introduction to the Principles of Morals and Legislation. Clarendon Press.
Bicchieri, C. (2005). The Grammar of Society: The Nature and Dynamics of Social Norms. Cam-
bridge University Press.
Binmore, K. (2005). Natural Justice. Oxford University Press.
Bolton, G. E., & Ockenfels, A. (2000).
ERC: A theory of equity, reciprocity, and competition.
American Economic Review, 90(1), 166–193.
Bonnefon, J.-F., Shariff, A., & Rahwan, I. (2016).
The social dilemma of autonomous vehicles.
Science, 352(6293), 1573–1576.
Borg, J. S., Sinnott-Armstrong, W., & Conitzer, V. (2024). Moral AI: And How We Get There.
Random House.
Bostrom, N., & Yudkowsky, E. (2014). The ethics of artificial intelligence. In Frankish, K., & Ramsey,
W. M. (Eds.), The Cambridge Handbook of Artificial Intelligence, pp. 316–334. Cambridge
University Press.
Bringsjord, S., Arkoudas, K., & Bello, P. (2006). Toward a general logicist methodology for engi-
neering ethically correct robots. IEEE Intelligent Systems, 21(4), 38–44.
Brown, C., Chauhan, J., Grammenos, A., Han, J., Hasthanasombat, A., Spathis, D., Xia, T., Cicuta,
P., & Mascolo, C. (2020a). Exploring automatic diagnosis of COVID-19 from crowdsourced
respiratory sound data. In Proceedings of the 26th ACM SIGKDD International Conference
on Knowledge Discovery & Data Mining, pp. 3474–3484.
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam,
P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child,
R., Ramesh, A., Ziegler, D. M., Wu, J., Winter, C., Hesse, C., Chen, M., Sigler, E., Litwin,
M., Gray, S., Chess, B., Clark, J., Berner, C., McCandlish, S., Radford, A., Sutskever, I.,
& Amodei, D. (2020b).
Language models are few-shot learners.
Proceedings of the 34th
International Conference on Neural Information Processing Systems (NeurIPS’20), 33, 1877–
1901.
Camerer, C. (2011). Behavioral Game Theory: Experiments in Strategic Interaction. The Roundtable
Series in Behavioral Economics. Princeton University Press.
Cao, L. (2022). AI in Finance: challenges, techniques, and opportunities. ACM Computing Surveys,
55(3), 1–38.
27

--- Page 28 ---

Tennant, Hailes, & Musolesi
Capraro, V., & Perc, M. (2021). Mathematical foundations of moral preferences. Journal of The
Royal Society Interface, 18(175), 20200880.
Carroll, M., Foote, D., Siththaranjan, A., Russell, S., & Dragan, A. (2024)
AI Alignment with
Changing and Influenceable Reward Functions. arXiv Preprint arXiv:2405.17713.
Casper, S., Davies, X., Shi, C., Gilbert, T. K., Scheurer, J., Rando, J., Freedman, R., Korbak, T.,
Lindner, D., Freire, P., Wang, T., Marks, S., S´egerie, C.-R., Carroll, M., Peng, A., Christof-
fersen, P. J., Damani, M., Slocum, S., Anwar, U., Siththaranjan, A., Nadeau, M., Michaud,
E. J., Pfau, J., Krasheninnikov, D., Chen, X., di Langosco, L. L., Hase, P., Biyik, E., Dragan,
A. D., Krueger, D., Sadigh, D., & Hadfield-Menell, D. (2023) Open problems and fundamental
limitations of reinforcement learning from human feedback. arXiv Preprint. arXiv::2307.15217.
Charness, G., & Rabin, M. (2002). Understanding social preferences with simple tests. The Quarterly
Journal of Economics, 117(3), 817–869.
Chentanez, N., Barto, A., & Singh, S. (2004). Intrinsically motivated reinforcement learning. In
Proceedings of the 18th International Conference on Neural Information Processing Systems
(NeurIPS’04), Vol. 17, pp. 1281–1288.
Christian, B. (2020). The Alignment Problem: Machine Learning and Human Values. WW Norton
& Company.
Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforce-
ment learning from human preferences. In Proceedings of the 31st International Conference
on Neural Information Processing Systems (NeurIPS’17), Vol. 30, pp. 4299–4307.
Clarke, R. (1993).
Asimov’s laws of robotics: implications for information technology - part i.
Computer, 26(12), 53–61.
Danielson, P. (1992). Artificial Morality: Virtuous Robots for Virtual Games. Routledge.
Deci, E. L., Koestner, R., & Ryan, R. M. (1999). A meta-analytic review of experiments examining
the effects of extrinsic rewards on intrinsic motivation. Psychological Bulletin, 125(6), 627–668.
Deci, E. L., & Ryan, R. M. (1985). Intrinsic Motivation and Self-determination in Human Behavior.
Springer New York.
Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirec-
tional transformers for language understanding. In Proceedings of the 2019 Conference of the
North American Chapter of the Association for Computational Linguistics: Human Language
Technologies (NAACL-HLT 2019).
Dignum, V. (2017). Responsible autonomy. In Proceedings of the 26th International Joint Conference
on Artificial Intelligence (IJCAI’17), pp. 4698–4704.
Dignum, V. (2019). Responsible Artificial Intelligence: How to Develop and Use AI in a Responsible
Way. Springer.
Ecoffet, A., & Lehman, J. (2021). Reinforcement learning under moral uncertainty. In Proceedings of
the 38th International Conference on Machine Learning (ICML’21), pp. 2926–2936. PMLR.
FAIR, Bakhtin, A., Brown, N., Dinan, E., Farina, G., Flaherty, C., Fried, D., Goff, A., Gray, J.,
Hu, H., Jacob, A. P., Komeili, M., Konath, K., Kwon, M., Lerer, A., Lewis, M., Miller, A. H.,
Mitts, S., Renduchintala, A., Roller, S., Rowe, D., Shi, W., Spisak, J., Wei, A., Wu, D., Zhang,
H., & Zijlstra, M. (2022). Human-level play in the game of Diplomacy by combining language
models with strategic reasoning. Science, 378(6624), 1067–1074.
Fan, C., Chen, J., Jin, Y., & He, H. (2024). Can large language models serve as rational players in
game theory? A systematic analysis. In Proceedings of the 38th AAAI Conference on Artificial
Intelligence (AAAI’24).
Fehr, E., & Fischbacher, U. (2002). Why social preferences matter – the impact of non-selfish motives
on competition, cooperation and incentives. The Economic Journal, 112(478), 1–33.
28

--- Page 29 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Fehr, E., & Fischbacher, U. (2004a). Social norms and human cooperation. Trends in Cognitive
Sciences, 8(4), 185–190.
Fehr, E., & Fischbacher, U. (2004b). Third-party punishment and social norms. Evolution and
Human Behavior, 25(2), 63–87.
Fehr, E., & Schmidt, K. M. (1999). A theory of fairness, competition, and cooperation. The Quarterly
Journal of Economics, 114(3), 817–868.
Ferguson, R. (1981). Prolog: A step towards the ultimate computer language. Byte, 6(11), 384–399.
Foerster, J., Chen, R. Y., Al-Shedivat, M., Whiteson, S., Abbeel, P., & Mordatch, I. (2018). Learn-
ing with opponent-learning awareness.
In Proceedings of the International Conference on
Autonomous Agents and Multiagent Systems (AAMAS’18), pp. 122–130.
Gandhi, K., Sadigh, D., & Goodman, N. D. (2023). Strategic reasoning with language models. In
Proceedings of the NeurIPS Workshop: Foundation Models for Decision Making.
Gauthier, D. (1987). Morals by Agreement. Clarendon Press.
Gilligan, C. (1982). In a Different Voice: Psychological Theory and Women’s Development. Harvard
University Press.
Gini, C. (1912). Variabilit(`a) e Mutabilit(`a): Contributo allo studio delle distribuzioni e delle relazioni
statistiche. [Fasc. I.]. Tipografia di P. Cuppini.
Glaese, A., McAleese, N., Trebacz, M., Aslanides, J., Firoiu, V., Ewalds, T., Rauh, M., Weidinger, L.,
Chadwick, M., Thacker, P., et al. (2022) Improving alignment of dialogue agents via targeted
human judgements. arXiv Preprint arXiv:2209.14375.
Goodfellow, I. J., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
Gopnik, A. (2009). The Philosophical Baby: What Children’s Minds Tell Us About Truth, Love and
the Meaning of Life. The Bodley Head.
Graham, J., Haidt, J., Koleva, S., Motyl, M., Iyer, R., Wojcik, S. P., & Ditto, P. H. (2013). Moral
Foundations Theory: the pragmatic validity of moral pluralism. In Advances in Experimental
Social Psychology, Vol. 47, pp. 55–130. Academic Press.
Graham, J., Haidt, J., & Nosek, B. A. (2009). Liberals and conservatives rely on different sets of
moral foundations.. Journal of Personality and Social Psychology, 96(5), 1029–1046.
Guarini, M. (2006). Particularism and the classification and reclassification of moral cases. IEEE
Intelligent Systems, 21(4), 22–28.
Hadfield-Menell, D., Russell, S. J., Abbeel, P., & Dragan, A. (2016). Cooperative inverse reinforce-
ment learning. In Proceedings of the 30th International Conference on Neural Information
Processing Systems (NeurIPS’16), Vol. 29, pp. 3916–3924.
Hardin, G. (1968). The tragedy of the commons. the population problem has no technical solution;
it requires a fundamental extension in morality. Science, 162(3859), 1243–1248.
Harsanyi, J. C. (1961). On the rationality postulates underlying the theory of cooperative games.
Journal of Conflict Resolution, 5(2), 179–196.
Harsanyi, J. C. (1995). Games with incomplete information. The American Economic Review, 85(3),
291–303.
Hayes, C. F., Ruadulescu, R., Bargiacchi, E., Kallstrom, J., Macfarlane, M., Reymond, M., Ver-
straeten, T., Zintgraf, L. M., Dazeley, R., Heintz, F., Howley, E., Irissappane, A. A., Mannion,
P., Now’e, A., de Oliveira Ramos, G., Restelli, M., Vamplew, P., & Roijers, D. M. (2022). A
practical guide to multi-objective reinforcement learning and planning. Autonomous Agents
and Multi-Agent Systems, 36(1).
Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., & Steinhardt, J. (2021a). Aligning
AI with shared human values. In Proceedings of the 9th International Conference on Learning
Representations (ICLR’21), pp. 1–29.
29

--- Page 30 ---

Tennant, Hailes, & Musolesi
Hendrycks, D., Mazeika, M., Zou, A., Patel, S., Zhu, C., Navarro, J., Song, D., Li, B., & Steinhardt, J.
(2021b). What would Jiminy Cricket do? Towards agents that behave morally. In Proceedings
of the 35th International Conference on Neural Information Processing Systems (NeurIPS’21)
(Datasets and Benchmarks Track).
Hernandez-Leal, P., Kartal, B., & Taylor, M. E. (2019). A survey and critique of multiagent deep
reinforcement learning. Autonomous Agents and Multi-Agent Systems, 33(6), 750–797.
Hohm, I., O’Shea, B. A., & Schaller, M. (2024). Do moral values change with the seasons?. Pro-
ceedings of the National Academy of Sciences, 121(33), e2313428121.
Hooker, J. N., & Kim, T. W. N. (2018). Toward non-intuition-based machine and artificial intel-
ligence ethics: a deontological approach based on modal logic. In Proceedings of the 2018
AAAI/ACM Conference on AI, Ethics, and Society (AIES’18), pp. 130–136.
Hughes, E., Leibo, J. Z., Phillips, M., Tuyls, K., Due˜nez Guzman, E., Garc´ıa Casta˜neda, A., Dun-
ning, I., Zhu, T., McKee, K., Koster, R., Roff, H., & Graepel, T. (2018). Inequity aversion
improves cooperation in intertemporal social dilemmas.
In Proceedings of the 32nd Inter-
national Conference on Neural Information Processing Systems (NeurIPS’18), Vol. 31, pp.
3330–3340.
Jain, S., Kirk, R., Singh, E., Robert, L., Dick, P., Tanaka, H., Grefenstette, E., Rockt¨aschel, T.,
& Krueger, D. S. (2023) Mechanistically analyzing the effects of fine-tuning on procedurally
defined tasks. arXiv Preprint arXiv:2311.12786.
Jannach, D., Pu, P., Ricci, F., & Zanker, M. (2022). Recommender systems: Trends and frontiers.
AI Magazine, 43(2), 145–150.
Jaques, N., Lazaridou, A., Hughes, E., Gulcehre, C., Ortega, P., Strouse, D., Leibo, J. Z., & De Fre-
itas, N. (2019). Social influence as intrinsic motivation for multi-agent deep reinforcement
learning. In Proceedings of the 36th International Conference on Machine Learning (ICML’19),
pp. 3040–3049. PMLR.
Ji, J., Qiu, T., Chen, B., Zhang, B., Lou, H., Wang, K., Duan, Y., He, Z., Zhou, J., Zhang, Z., Zeng,
F., Ng, K. Y., Dai, J., Pan, X., O’Gara, A., Lei, Y., Xu, H., Tse, B., Fu, J., McAleer, S.,
Yang, Y., Wang, Y., Zhu, S.-C., Guo, Y., & Gao, W. (2024) AI Alignment: A Comprehensive
Survey. arXiv Preprint. arXiv 2310.19852.
Kant, I. (1785). Grounding for the Metaphysics of Morals. Cambridge University Press.
Kavish, N., Bailey, C., Sharp, C., & Venta, A. (2018). On the relation between general intelligence
and psychopathic traits: an examination of inpatient adolescents. Child Psychiatry & Human
Development, 49, 341–351.
Kim, T. W. N., Hooker, J. N., & Donaldson, T. (2021). Taking principles seriously: a hybrid approach
to value alignment in artificial intelligence. Journal of Artificial Intelligence Research (JAIR),
70, 871–890.
Kimbrough, E. O., & Vostroknutov, A. (2023) A theory of injunctive norms. Available at SSRN:
ssrn.3566589.
Kleiman-Weiner, M., Saxe, R., & Tenenbaum, J. B. (2017). Learning a commonsense moral theory.
Cognition, 167, 107–123.
Kohlberg, L. (1975). The cognitive-developmental approach to moral education. Phi Delta Kappan
(Special Issue on Moral Education), 56(10), 670–677.
Koster, R., Balaguer, J., Tacchetti, A., Weinstein, A., Zhu, T., Hauser, O., Williams, D., Campbell-
Gillingham, L., Thacker, P., Botvinick, M., & Summerfield, C. (2022). Human-centred mech-
anism design with Democratic AI. Nature Human Behaviour, 6(10), 1398–1407.
Kretzschmar, H., Spies, M., Sprunk, C., & Burgard, W. (2016). Socially compliant mobile robot
navigation via inverse reinforcement learning. The International Journal of Robotics Research,
35(11), 1289–1307.
30

--- Page 31 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). Imagenet classification with deep convolutional
neural networks. In Proceedings of the 26th International Conference on Neural Information
Processing Systems (NeurIPS’12), Vol. 25, pp. 84–90.
Krueger, F., & Hoffman, M. (2016). The emerging neuroscience of third-party punishment. Trends
in Neurosciences, 39(8), 499–501.
Krupka, E. L., & Weber, R. A. (2013). Identifying social norms using coordination games: why does
dictator game sharing vary?. Journal of the European Economic Association, 11(3), 495–524.
Lake, B. M., Ullman, T. D., Tenenbaum, J. B., & Gershman, S. J. (2017). Building machines that
learn and think like people. Behavioral and Brain Sciences, 40, e253.
Lasquety-Reyes, J. A. (2019).
Computer simulations of ethics: the applicability of agent-based
modeling for ethical theories. European Journal of Formal Sciences and Engineering, 2(1),
22–38.
Ledyard, J. O. (1995). Public goods: a survey of experimental research. In Kagel, J. H., & Roth,
A. E. (Eds.), The Handbook of Experimental Economics, pp. 111–194. Princeton University
Press.
Leibo, J. Z., Zambaldi, V., Lanctot, M., Marecki, J., & Graepel, T. (2017). Multi-agent reinforcement
learning in sequential social dilemmas. In Proceedings of the 16th International Conference
on Autonomous Agents and Multiagent Systems (AAMAS’17), pp. 464–473.
Leike, J., Martic, M., Krakovna, V., Ortega, P. A., Everitt, T., Lefrancq, A., Orseau, L., & Legg, S.
(2017) AI Safety Gridworlds. arXiv Preprint. arXiv:1711.09883.
Levine, D. K. (1998).
Modeling altruism and spitefulness in experiments.
Review of Economic
Dynamics, 1(3), 593–622.
Levitt, S. D., & List, J. A. (2007). What do laboratory experiments measuring social preferences
reveal about the real world?. Journal of Economic Perspectives, 21(2), 153–174.
Liebrand, W. B. (1983). A classification of social dilemma games. Simulation & Games, 14(2),
123–138.
Lipson, H., & Kurman, M. (2016). Driverless: Intelligent Cars and the Road Ahead. MIT Press.
Littman, M. L. (1994). Markov games as a framework for multi-agent reinforcement learning. In
Proceedings of the 11th International Conference on International Conference on Machine
Learning (ICML’94), pp. 157–163.
Loreggia, A., Mattei, N., Rossi, F., & Venable, K. B. (2020). Modeling and reasoning with preferences
and ethical priorities in AI systems. In Liao, S. M. (Ed.), Ethics of Artificial Intelligence, pp.
127–154. Oxford University Press.
Mayo-Wilson, C., & Zollman, K. J. S. (2021). The computational philosophy: simulation as a core
philosophical method. Synthese, 199(1-2), 3647–3673.
McKee, K. R., Gemp, I., McWilliams, B., Du`e˜nez Guzm´an, E. A., Hughes, E., & Leibo, J. Z. (2020).
Social diversity and social preferences in mixed-motive reinforcement learning. In Proceed-
ings of the 19th International Conference on Autonomous Agents and MultiAgent Systems
(AAMAS’20), pp. 869–877.
Mitchell, M., & Krakauer, D. C. (2023). The debate over understanding in ai’s large language models.
Proceedings of the National Academy of Sciences, 120(13), e2215907120.
Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., Graves, A., Ried-
miller, M., Fidjeland, A. K., Ostrovski, G., Petersen, S., Beattie, C., Sadik, A., Antonoglou,
I., King, H., Kumaran, D., Wierstra, D., Legg, S., & Hassabis, D. (2015). Human-level control
through deep reinforcement learning. Nature, 518(7540), 529–533.
31

--- Page 32 ---

Tennant, Hailes, & Musolesi
Morris, M. R., Sohl-Dickstein, J., Fiedel, N., Warkentin, T., Dafoe, A., Faust, A., Farabet, C., &
Legg, S. (2024). Position: Levels of AGI for operationalizing progress on the path to AGI. In
Proceedings of the 41st International Conference on Machine Learning (ICML’24), Vol. 235,
pp. 36308–36321.
Murphy, R. R. (2019). Introduction to AI Robotics. MIT Press.
Najar, A., & Chetouani, M. (2021). Reinforcement learning with human advice: a survey. Frontiers
in Robotics and AI, 8, 1–20.
Neufeld, E. A., Bartocci, E., Ciabattoni, A., & Governatori, G. (2022). Enforcing ethical goals over
reinforcement-learning policies. Ethics and Information Technology, 24(4), 43.
Ng, A. Y., & Russell, S. J. (2000). Algorithms for inverse reinforcement learning. In Proceedings of
the 17th International Conference on Machine Learning (ICML’00), pp. 663–670.
Noothigattu, R., Bouneffouf, D., Mattei, N., Chandra, R., Madan, P., Varshney, K. R., Campbell,
M., Singh, M., & Rossi, F. (2019). Teaching AI agents ethical values using reinforcement
learning and policy orchestration. In Proceedings of the 28th International Joint Conference
on Artificial Intelligence (IJCAI’19), pp. 6377–6381.
OpenAI (2024)
Model Specs.
Retrieved from https://cdn.openai.com/spec/model-spec-2024-05-
08.html.
Oudeyer, P.-Y., & Kaplan, F. (2007). What is intrinsic motivation? A typology of computational
approaches. Frontiers in Neurorobotics, 1.
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S.,
Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A.,
Welinder, P., Christiano, P. F., Leike, J., & Lowe, R. (2022). Training language models to
follow instructions with human feedback. In Proceedings of the 36th International Conference
on Neural Information Processing Systems (NeurIPS’22), Vol. 35, pp. 27730–27744.
Pan, A., Bhatia, K., & Steinhardt, J. (2022) The effects of Reward Misspecification: mapping and
mitigating misaligned models. arXiv Preprint. arXiv:2201.03544.
Pan, A., Chan, J. S., Zou, A., Li, N., Basart, S., Woodside, T., Zhang, H., Emmons, S., & Hendrycks,
D. (2023).
Do the rewards justify the means? Measuring trade-offs between rewards and
ethical behavior in the MACHIAVELLI benchmark. In Proceedings of the 40th International
Conference on Machine Learning (ICML’23), pp. 26837–26867.
Park, J. S., O’Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023) Generative
agents: interactive simulacra of human behavior. arXiv Preprint arXiv:2304.03442.
Peschl, M., Zgonnikov, A., Oliehoek, F. A., & Siebert, L. C. (2022). MORAL: Aligning ai with
human norms through multi-objective reinforced active learning. In Proceedings of the 21st
International Conference on Autonomous Agents and Multiagent Systems (AAMAS’22), pp.
1038–1046.
Pitt, J. C. (2014). ‘Guns don’t kill, people kill’; Values in and/or around technologies. In The Moral
Status of Technical Artefacts. Philosophy of Engineering and Technology, Vol. 17, pp. 89–101.
Springer Netherlands.
Poundstone, W. (1993). Prisoner’s Dilemma: John von Neumann, Game Theory, and the Puzzle of
the Bomb. Anchor Books.
Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., & Finn, C. (2023).
Direct
preference optimization: Your language model is secretly a reward model. In Proceedings of
the 37th International Conference on Neural Information Processing Systems (NeurIPS’23).
Railton, P. (2020). Ethical learning, natural and artificial. In Liao, S. M. (Ed.), Ethics of Artificial
Intelligence. Oxford University Press.
32

--- Page 33 ---

Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto
Rajpurkar, P., Chen, E., Banerjee, O., & Topol, E. J. (2022). AI in Health and Medicine. Nature
Medicine, 28(1), 31–38.
Rapoport, A. (1974). Prisoner’s dilemma — recollections and observations. In Game Theory as a
Theory of a Conflict Resolution, pp. 17–34. Springer.
Rawls, J. (1971). A Theory of Justice. Belknap Press.
Reinecke, M. G., Mao, Y., Kunesch, M., Du´e˜nez-Guzm´an, E. A., Haas, J., & Leibo, J. Z. (2023).
The puzzle of evaluating moral cognition in artificial agents. Cognitive Science, 47(8), e13315.
Saha, A., Subramanya, A., & Pirsiavash, H. (2020). Hidden trigger backdoor attacks. In Proceedings
of the 34th (AAAI) Conference on Artificial Intelligence (AAAI’20), Vol. 34, pp. 11957–11965.
Sandholm, T. W., & Crites, R. H. (1996). Multiagent reinforcement learning in the iterated prisoner’s
dilemma. Biosystems, 37(1-2), 147–166.
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017) Proximal Policy Opti-
mization Algorithms. arXiv Preprint. arXiv:1707.06347.
Silver, D., Huang, A., Maddison, C. J., Guez, A., Sifre, L., van den Driessche, G., Schrittwieser,
J., Antonoglou, I., Panneershelvam, V., Lanctot, M., Dieleman, S., Grewe, D., Nham, J.,
Kalchbrenner, N., Sutskever, I., Lillicrap, T., Leach, M., Kavukcuoglu, K., Graepel, T., &
Hassabis, D. (2016). Mastering the game of Go with deep neural networks and tree search.
Nature, 529(7587), 484–489.
Silver, D., Singh, S., Precup, D., & Sutton, R. S. (2021). Reward is enough. Artificial Intelligence,
299, 103535.
Skalse, J., Howe, N., Krasheninnikov, D., & Krueger, D. (2022). Defining and characterizing reward
gaming. Proceedings of the 36th International Conference on Neural Information Processing
Systems (NeurIPS’22), 35, 9460–9471.
Skyrms, B. (2001). The stag hunt. Proceedings and Addresses of the American Philosophical Asso-
ciation, 75(2), 31–41.
Snell, C., Kostrikov, I., Su, Y., Yang, M., & Levine, S. (2023) Offline RL for Natural Language
Generation with Implicit Language Q Learning. arXiv Preprint arXiv:2206.11871.
Sorensen, T., Moore, J., Fisher, J., Gordon, M. L., Mireshghallah, N., Rytting, C. M., Ye, A., Jiang,
L., Lu, X., Dziri, N., Althoff, T., & Choi, Y. (2024). Position: A roadmap to pluralistic align-
ment. In Proceedings of the 41st International Conference on Machine Learning (ICML’24),
Vol. 235, pp. 46280–46302.
Spelke, E. S., & Kinzler, K. D. (2007). Core knowledge. Developmental Science, 10(1), 89–96.
Steinhardt, J., Koh, P. W. W., & Liang, P. S. (2017). Certified defenses for data poisoning attacks.
In Proceedings of the 31st International Conference on Neural Information Processing Systems
(NeurIPS’17), Vol. 30.
Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction. MIT Press.
Swanepoel, D., & Corks, D. (2024). Artificial intelligence and agency: Tie-breaking in AI decision-
making. Science and Engineering Ethics, 30(2), 11.
Tennant, E., Hailes, S., & Musolesi, M. (2023). Modeling moral choices in social dilemmas with multi-
agent reinforcement learning. In Proceedings of the 32nd International Joint Conference on
Artificial Intelligence (IJCAI’23), pp. 317–325.
Tennant, E., Hailes, S., & Musolesi, M. (2024a).
Dynamics of moral behavior in heterogeneous
populations of learning agents.
In Proceedings of the 7th AAAI/ACM Conference in AI,
Ethics & Society (AIES’24).
Tennant, E., Hailes, S., & Musolesi, M. (2024b) Moral Alignment for LLM Agents. arXiv Preprint.
arXiv:2410.01639.
33

--- Page 34 ---

Tennant, Hailes, & Musolesi
Thomson, J. J. (1976). Killing, letting die, and the trolley problem. The Monist, 59(2), 204–217.
Tolmeijer, S., Kneer, M., Sarasua, C., Christen, M., & Bernstein, A. (2021). Implementations in
machine ethics: a survey. ACM Computing Surveys, 53(6), 1–38.
UK Government (2023) AI Safety Summit 2023: The Bletchley Declaration.
Vamplew, P., Dazeley, R., Foale, C., Firmin, S., & Mummery, J. (2018). Human-aligned artificial
intelligence is a multiobjective problem. Ethics and Information Technology, 20(1), 27–40.
Vezhnevets, A. S., Agapiou, J. P., Aharon, A., Ziv, R., Matyas, J., Du´e˜nez-Guzm´an, E. A., Cun-
ningham, W. A., Osindero, S., Karmon, D., & Leibo, J. Z. (2023) Generative agent-based
modeling with actions grounded in physical, social, or digital space using Concordia. arXiv
Preprint arXiv:2312.03664.
Wallach, W. (2010). Robot minds and human ethics: the need for a comprehensive model of moral
decision making. Ethics and Information Technology, 12(3), 243–250.
Wallach, W., & Allen, C. (2009). Moral Machines: Teaching Robots Right from Wrong. Oxford
University Press.
Wallach, W., Allen, C., & Smit, I. (2008). Machine morality: bottom-up and top-down approaches
for modelling human moral faculties. AI & SOCIETY, 22(4), 565–582.
Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., & Anandkumar, A. (2024a).
Voyager: An open-ended embodied agent with large language models. Transactions on Ma-
chine Learning Research, 1, 1–44.
Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y.,
Zhao, W. X., Wei, Z., & Wen, J. (2024b). A survey on large language model based autonomous
agents. Frontiers of Computer Science, 18(6).
Watkins, C. J., & Dayan, P. (1992). Q-learning. Machine Learning, 8(3), 279–292.
Weidinger, L., McKee, K. R., Everett, R., Huang, S., Zhu, T. O., Chadwick, M. J., Summerfield, C.,
& Gabriel, I. (2023). Using the veil of ignorance to align AI systems with principles of justice.
Proceedings of the National Academy of Sciences, 120(18), e2213709120.
Winfield, A. F. T., Blum, C., & Liu, W. (2014). Towards an ethical robot: internal models, conse-
quences and ethical action selection. In Mistry, M., Leonardis, A., Witkowski, M., & Melhuish,
C. (Eds.), Advances in Autonomous Robotics Systems, pp. 85–96. Springer International Pub-
lishing.
Wrzesniewski, A., McCauley, C., Rozin, P., & Schwartz, B. (1997).
Jobs, careers, and callings:
people’s relations to their work. Journal of Research in Personality, 31(1), 21–33.
Zhang, Y., Mao, S., Ge, T., Wang, X., de Wynter, A., Xia, Y., Wu, W., Song, T., Lan, M., & Wei, F.
(2024) LLM as a Mastermind: A Survey of Strategic Reasoning with Large Language Models.
arXiv Preprint. arXiv:2404.01230.
Zhuang, S., & Hadfield-Menell, D. (2020). Consequences of misaligned AI. In Proceedings of the 34th
International Conference on Neural Information Processing Systems (NeurIPS’20), Vol. 33,
pp. 15763–15773.
Ziegler, D. M., Stiennon, N., Wu, J., Brown, T. B., Radford, A., Amodei, D., Christiano, P., &
Irving, G. (2019)
Fine-tuning language models from human preferences.
arXiv Preprint
arXiv:1909.08593.
34

```
