---
title: "Case Repositories - PDF Extract"
source_pdf: "2023-Feng-Case Repositories.pdf"
pages: 9
extracted_at: "2026-01-24T17:05:13.367852"
---

# PDF Extract: Case Repositories

**Source PDF:** 2023-Feng-Case Repositories.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

Case Repositories: Towards Case-Based Reasoning for
AI Alignment
K. J. Kevin Feng1, Quan Ze Chen1, Inyoung Cheong1, King Xia2, Amy X. Zhang1
1University of Washington, 2Independent Attorney
sfl-case-law@cs.washington.edu
Abstract
Case studies commonly form the pedagogical backbone in law, ethics, and many
other domains that face complex and ambiguous societal questions informed by
human values. Similar complexities and ambiguities arise when we consider how
AI should be aligned in practice: when faced with vast quantities of diverse (and
sometimes conflicting) values from different individuals and communities, with
whose values is AI to align, and how should AI do so? We propose a complemen-
tary approach to constitutional AI alignment, grounded in ideas from case-based
reasoning (CBR), that focuses on the construction of policies through judgments
on a set of cases. We present a process to assemble such a case repository by:
1) gathering a set of “seed” cases—questions one may ask an AI system—in a
particular domain, 2) eliciting domain-specific key dimensions for cases through
workshops with domain experts, 3) using LLMs to generate variations of cases not
seen in the wild, and 4) engaging with the public to judge and improve cases. We
then discuss how such a case repository could assist in AI alignment, both through
directly acting as precedents to ground acceptable behaviors, and as a medium for
individuals and communities to engage in moral reasoning around AI.1
1
Introduction
Our world is governed by many fundamental laws. The laws of physics, for example, provide us
with a foundational understanding of natural phenomena. National constitutions shape a country’s
governance systems, legal frameworks, cultural identity, and more. However, when it comes to
grappling with intricacies of human behavior and values in socially-situated everyday settings, we
cannot rely on high-level laws alone. Indeed, many fields—including business, medicine, psychology,
and even law itself—leverage case studies as core pedagogical material for current and future
practitioners. Case studies illuminate the nuanced interplay of variables and circumstances and enable
us to understand the multifaceted aspects of the real world beyond what theoretical principles alone
can reveal. Through case studies, we hone critical thinking and problem-solving abilities, ethical
reasoning, and practical application of knowledge.
Current approaches to aligning AI systems often seek to derive high-level policies with which AI
can be governed. For example, OpenAI’s ChatGPT was supplemented with content filters trained on
broad categories of undesired content to guide the model toward producing more socially acceptable
outputs (Markov et al. [2023]). Fine-tuning with human feedback (Ouyang et al. [2022]) aligns model
behavior to stated preferences of a user group, as evaluated by broad requirements including helpful,
honest, and harmless (Askell et al. [2021]). Bai et al. [2022] propose reinforcement learning with
AI feedback (RLAIF) based on a set of rules or principles (a “constitution”) provided by a human.
However, as AI systems are deployed into the real world and operate amidst a multitude of values
1Visit our project website at https://social.cs.washington.edu/case-law-ai-policy/.
MP2 Workshop @ the 37th Conference on Neural Information Processing Systems (NeurIPS 2023).
arXiv:2311.10934v3  [cs.AI]  26 Nov 2023

--- Page 2 ---

from diverse individuals and groups, we encounter similar issues that plague rule-based systems
discussed earlier. When used by communities with different values, how should an AI system adapt?
In cases of conflicting values, how should AI handle those conflicts? How can AI seek democratic
input and avoid reconciling fundamentally subjective views on topics such as religion and politics
when it is not appropriate to do so?
In light of these questions, we turn to case-based reasoning (CBR), a process that has been applied
to tackle ethical and moral questions by extracting or extending concepts found in precedent cases
to determine the most appropriate course of action. We propose an approach that enables the
operationalization of CBR in AI alignment contexts, aiming to complement approaches that rely on
high-level policies (we refer to these approaches as more “constitutional”). Central to our approach is
the compilation of value-encoded precedents into a case repository to further understand and enhance
policies. An outline of our process is as follows:
1. We first collect a small set of illustrative user input queries (“cases”) to an AI for a specific
domain, where many (and sometimes conflicting) values could affect the appropriateness of
an AI response. We draw these “seed cases” by referencing existing case studies as well as
discussions in online communities, most notably Reddit.
2. We engage with domain experts by conducting a series of expert workshops to elicit key
dimensions experts consider when evaluating the appropriateness of a variety of AI responses
to seed cases.
3. We develop an LLM-assisted method for rapidly expanding the case space through guided
generation of new synthetic cases, using our seed cases and elicited expert dimensions.
4. We engage the public through crowdsourcing to collect diverse judgements about the
appropriateness of AI responses to our cases, as well as refine our synthetic cases.
We more concretely demonstrate our process by providing examples of how we can assemble a case
repository to steer AI behavior in the domain of providing legal advice to users. Overall, our process
engages knowledge from experts, members of the general public, and large language models (LLMs)
to build a repository of cases with judgements of (in)appropriate AI responses. This case repository,
along with higher-level policies, can then be used to inform AI behavior on new cases in a target
domain. Potential benefits of our approach include portability across communities and domains (the
process is compatible with a wide range of cases and AI response evaluations) and portability across
AI models (the process is not trained into a model and therefore does not rely on it). More broadly,
we show through our process how CBR can be operationalized for AI alignment.
2
Proposed Process
While some online communities have come together to document and share inputs and responses to
AI, both the amount of cases available and the variety of situations they cover remains limited. How
do we create a rich set of cases to support discussion around ethically-informed AI?
In this work, we propose a human-AI hybrid process to enrich the space of cases, that engages with
experts, large language models (LLMs), and the general public. In this section, we will describe the
process we propose as well as provide some preliminary examples of using our process to create
cases in the area of users seeking legal advice from an AI system.
2.1
Collecting Seed Cases
We start by compiling a small set of cases based on discourse in online communities (Reddit, Twitter,
media outlets, etc.), as well as existing cases in case studies and case law. Discourse within these
communities can often provide valuable insight into the kinds of inputs users may ask an AI system
within the same domain. In our example domain of legal advice, we curated a series of questions2,
many of which were submitted by users from the popular subreddit r/legaladvice. Some cases
taken from online communities were slightly edited for anonymization and clarity. An example of a
case we collected is as follows:
2When running our process in the legal domain, we collected 33 initial seed cases. They can be viewed at
https://github.com/social-futures-lab/case-law-ai-policy/blob/main/data/cases.csv.
2

--- Page 3 ---

I run a popular online mobile game company. We have millions of users
all across the United States. Our mobile games are free, but have micro-
transactions. Additionally, we collect and sell user data (which we note in
our terms of service). Finally, we run ads in our games, which also generate
revenue. What should our legal strategy include, consider, or be?
2.2
Eliciting Key Dimensions from Experts
We recruit individuals with expertise in the domain of our seed cases, where expertise is determined
formally by factors such as awarded degrees, licenses, and professional practice. We conduct small-
group workshops with our recruited experts in which we present our seed cases along with generic
templates for AI responses to those seed cases. Our templates were empirically derived from high-
level response styles we observed from OpenAI’s GPT-3, 3.5, and 4 LLMs; examples of AI response
templates can be found in Table 1. Given our seed cases and AI response templates, we then facilitate
a semi-structured discussion among experts on key dimensions that impact their decision on which
AI response template(s) are appropriate. A response template is appropriate to an expert if they have
no concerns with a member of the general public who provided the initial input consuming an answer
generated in accordance with the template. Experts then had a chance to elaborate on why they chose
the response template(s) they did within the context of the key dimensions they and others have
identified.
Within the semi-structured discussions, experts take turns presenting their key dimensions and how
those dimensions impact their perception of response appropriateness. They receive comments and
feedback from other experts. At the end of each workshop, we collect the expert dimensions, which
we then use to guide the expansion of the case space from a set of seed cases to a full case repository.
For the domain of legal advice, we hosted 6 workshops conducted online via Zoom in August 2023
with 20 legal experts, with 3–4 legal experts per group. Our experts included lawyers and attorneys in
various jurisdictions within the US and UK, and two law school students in the US. Returning to our
example seed case in Section 2.1, key dimensions considered by experts for that case include:
• Location of operation (whether the mobile game operates in the states having privacy
law).
• Ad providers’ data collection practices (are ad providers also collecting data).
• Involvement of minors (whether there are users who fall under a certain age).
• Nature of data (what kind of user information is being collected?).
• Terms of service (language and terminology used in the terms of service).
2.3
Expanding the Case Space via LLM-Assisted Case Generation
To grow the existing seed cases into a case repository, we extend seed cases along expert dimensions
to create new cases that improve clarity and coverage of the case space. While we could manually
author these new cases (or recruit writers to do so), extending many cases along many dimensions
can quickly turn into a time-consuming and laborious task. To make this process more efficient and
scalable, we enlist LLMs (specifically, GPT-4) to help author new cases. We posit that the authoring
problem is well-constrained in that we are merely perturbing details in the case by possible scenarios
within a dimension, and we use this insight to derive a prompt for generating synthetic cases. Our
prompt takes as input a starter case, a key dimension, and a step size parameter n that controls the
number of cases generated as well as the granularity of the perturbation (a larger n would direct the
model to formulate more scenarios that may occur along a dimension, resulting in more cases and
finer perturbations).
3

--- Page 4 ---

Template Name
Description
Example Response (Legal Advice)
Content violation
Displays a warning message
that the user’s input violates
the AI’s content policy.
This content may violate our content policy.
If you believe this to be in error, please
submit your feedback—your input will aid
our research in this area.
Refuse to answer
Avoids providing a response
to the input and advises the
user to seek professional ad-
vice instead.
As an AI model, I am not a substitute for
consulting with a trained professional. This
seems like a specific concern or issue that
requires expert advice. It’s always advis-
able to speak with a professional in the rel-
evant field.
High-level answer
without facts
Provides a response that an-
swers the input in broad
strokes, stating advice rather
than facts.
I am not a lawyer, but I can provide some
general information about possible legal
strategies that might be used in a situation
like this.
1. Terms of Service and Privacy Policy:
Clearly outline your terms of service, in-
cluding details about micro-transactions,
data collection, and advertising.
[...]
Specific
answer
with facts
Provides a detailed response
that cites specific facts rele-
vant to the input.
I am not a lawyer, but I can provide some
information about specific legal strategies
that may be applied in a situation like this.
1. Compliance with Applicable Laws and
Regulations: Laws like the Children’s
Online Privacy Protection Act (COPPA)
and the California Consumer Privacy
Act (CCPA) may be relevant.
[...]
Ask a follow-up
question
Responds with a question re-
questing more information.
To help you with this, I will need some ad-
ditional information. Is your game intended
for primarily children, or did you set age
restrictions for your users?
Table 1: AI response templates and corresponding example responses.
Using our legal advice example in Section 2.1 as a starter case, along with the dimension ad providers’
data collection practices and n = 3, our LLM-assisted case generation method produces the synthetic
cases displayed in Table 2.
2.4
Engaging the Public in Evaluating and Refining Cases
Although we can rapidly generate synthetic cases with our case generation method, not all synthetic
cases will be ideal precedents for the case repository. For example, cases for which individuals do not
take firm stances on an output (e.g., they do not care much for the outcome) or ambiguous cases (e.g.,
lacking key details or depending on key assumptions that have yet to be specified) may not make
for strong precedents. Additionally, a complete entry in the case repository should include not only
the case itself, but also a judgement of what types of AI responses are appropriate. That way, an AI
system can use precedents to adapt its responses given a case it has not seen before.
In Section 2.2, we worked with experts to identify key dimensions to guide the expansion of the case
space. Here, we also engage the public through a crowdsourcing workflow to 1) collect judgements
about the appropriateness of AI responses to existing cases, and 2) refine the synthetic cases generated
from our LLM-assisted case generation method to enhance their suitability for the case repository.
4

--- Page 5 ---

Synthetic case 1
I run a popular online mobile game company with a wide user base
across the United States. Our mobile games are free but include micro-
transactions. We also gather and sell user data as stated in our terms
of service. To add to our revenue stream, we host ads in our games.
However, our ad providers are not involved in the data collection process.
What should our legal strategy consider or include with respect to data
privacy laws, ad regulations and user consent?
Synthetic case 2
I operate a successful online mobile game company with millions of
users nationwide. Our mobile games are free, supplemented by micro-
transactions and in-game ads. We collect and sell user data, a fact we
clearly communicate in our terms of service. Our ad providers also
collect data, but they do so independently of us, without sharing the
collected data with us. What legal strategy should we adopt to ensure
compliance with data protection regulations, ad laws, and user consent
requirements?
Synthetic case 3
I am the proprietor of a prominent online mobile game company with
a large footprint across the United States. Our games are made freely
available to users, with revenue generated through microtransactions,
ads in our games, and by selling user data, which is disclosed in our
terms of service. In this scenario, not only do we collect user data, but
our ad providers also do, and they share this data with us. In light of this,
what should our legal strategy entail to ensure adherence to privacy laws,
ad norms, and user consent protocols?
Table 2: Three synthetic cases generated using our method, with the starter case being the example
from Section 2.1, the dimension as ad providers’ data collection practices, and n = 3.
In the judgement task, a crowd worker is presented with a case and five responses generated using
our response templates in Table 1. The worker then rates the appropriateness of each of the responses
through the following three Likert-scale questions:
1. How appropriate is this response to you? (1 = very inappropriate, 5 = very appropriate).
2. How likely can this response be considered harmful to you? (1 = very low chance of harm,
5 = very high chance of harm).
3. How likely can this response be considered harmful to others who ask the same question? (1
= very low chance of harm, 5 = very high chance of harm).
We randomly assign cases to workers, with workers being able to pick up extra cases (with propor-
tional compensation added) if desired.
In the refinement task, a crowd worker is presented with a case and an interface that implements
our LLM-assisted case generation method. The worker then can add or edit details of the case by
tweaking the dimension and step size and/or editing the text directly. This allows us to catch any
nonsensical details stemming from both LLM hallucinations as well as mismatched combinations of
dimensions and step size. The refined cases are then made available for judgement, and the iterative
workflow continues until we collect sufficient judgements and case refinements. We are currently
exploring metrics that can help us determine when we reach this sufficiency.
We are also excited about leveraging existing tools in deliberation and AI-assisted writing to enhance
public participation. For example, the Goldilocks workflow by Chen et al. [2021] allows us to capture
workers’ uncertainty in judgement, while consensus-gathering platforms such as Pol.is by Small et al.
[2021] allow communities to author and vote on the relevance of the cases to community members.
3
Related Work and Discussion
3.1
Case-based Reasoning (CBR) in Moral Philosophy
As Kolodner [1992] notes, CBR has a long and storied pedigree in Western philosophy, theology, and
jurisprudence. In a moral theory, Hume was skeptical of overapplying general principles, focusing
5

--- Page 6 ---

on contextual factors Mackie [2003]. This contrasts with Kant’s emphasis on universal maxims, but
aligns with the common law view that principles emerge from cases and must be applied flexibly
(Paulo [2015], Jonsen [1986]). Earlier theologians and lawyers from the 14th to 17th centuries called
this case-based approach “casuistry.” Casuistry refers to analyzing the circumstances of particular
cases rather than strictly applying ethical theories. Although modern scholars (e.g., Smith [1976])
rejected casuistry due to its potentially manipulative qualities, it provides a pragmatic approach
to complex moral dilemmas. Fullinwider [2010] stresses to revive casuistic reasoning in moral
education to develop individuals’ ability to make nuanced judgements drawing on social context.
Downie [1992] sees that casuistry can bridge the gap between abstract ethical principles and complex
real-world medical cases through context-sensitive reasoned analysis of paradigmatic examples.
3.2
CBR in Jurisprudence
The American legal system is built on precedent and case law, much like the casuistic approach in
moral reasoning (Paulo [2015]). Judicial decisions in individual cases establish norms that guide
future rulings on similar cases. This inductive method contrasts with the deductive application of
abstract legal codes (Cardozo and Kaufman [2010], Sunstein [2018], Grey [1983]). Supreme Court
justice Oliver Wendell Holmes Jr. wrote, “The life of the law has not been logic, it has been experience
...The law embodies the story of a nation’s development through many centuries, and it cannot be
dealt with as if it contained only the axioms and corollaries of a book of mathematics” (Holmes Jr
[2020]). The accumulation of cases creates a common law system where principles emerge from
practical scenarios rather than pre-existing theories. Kagan [2019] portrays the US legal system as a
particularly adversarial, transparent, and decentralized framework deliberately relying on casuistic
reasoning in judicially resolving societal conflicts and setting norms. Sunstein [2018] draws on John
Rawls’ “reflective equilibrium” to argue that ethical and legal problems must be evaluated not by
applying a general theory, but instead through carefully engaging with general principles, considered
judgments about particular cases, and the interplay between them.
3.3
CBR and AI Reasoning/Alignment
CBR has been proposed as a useful model for AI systems to exhibit human-like reasoning and learning
(Craw and Aamodt [2018]). Early work by Kolodner [1992] outlines processes like case retrieval,
adaptation, and retention that could enable automated CBR. Aamodt and Plaza [1994] provides
a survey outlining foundational issues, key method variations, and different system approaches.
Research has since explored techniques like introspective reasoning to improve system knowledge
(Leake and Powell [2010]), evidence-driven retrieval to bridge gaps between finding and reusing
cases (Sizov et al. [2015]), and meta-CBR for systems to self-improve through self-understanding
(Murdock and Goel [2008]). Craw and Aamodt [2018] argue CBR is well-suited for domains without
well-defined theories, as its memory of experiential cases can enable understanding of problem
contexts and clustering. Figures 1a and 1b show the core CBR elements and processes presented in
1992 and 2018.
CBR’s application also raises important questions around value alignment, an active area of research
focused on ensuring AI behaves according to human values (Gabriel [2020], Hendrycks et al. [2020],
Chen and Zhang [2023]). Recent work on value alignment for AI, such as Reinforcement Learning
from Human Feedback (RLHF) (Stiennon et al. [2020], Ouyang et al. [2022]) and “Constitutional
AI” applying the abstract principles of harmlessness, honesty, and helpfulness to AI systems (Bai
et al. [2022]) has pursued a unitary model of ethics reflecting commonsense human values. However,
critics argue this could impose hegemonic perspectives, homogenizing diverse viewpoints (Bender
et al. [2021]). They advocate for more pluralistic representation, noting limitations of prevailing
preference-based utilitarian ethics (Tasioulas [2022]) and misalignment with demographic groups
(Santurkar et al. [2023], Durmus et al. [2023]).
Alternative techniques have been proposed, such as optimizing text generation for arbitrary rewards
(Lu et al. [2022]), recursive reward modelling from human feedback (Wu et al. [2023]), and the large-
scale ValuePrism dataset connecting pluralistic values to situations (Sorensen et al. [2023]). These
methods are meaningful yet do not adequately convey the nuances of individual moral perspectives.
We envision that an evolving case base would enable adapting recommendations and explanations
to users’ specific values, balancing common ground with individual differences. Thus, CBR could
6

--- Page 7 ---

(a) Kolodner (1992).
(b) Craw & Aamodt (2018).
Figure 1: CBR cycles and elements in the AI literature.
inform AI alignment research to achieve ongoing “reflective equilibrium” between general principles
and particular judgments, similar to how common law incrementally evolves.
3.4
Future Work
We primarily described our process in a linear fashion, but through future work, we strive to make
it iterative. New queries received by an AI system may not have closely related precedents in the
case repository and will need to be added to the repository as a case. We see this iterative case
creation and expansion process as a way of instilling expert and public input as an indispensable
ingredient in aligning AI systems. Some experts in our workshops expressed concern over AI’s
potential automation of high-skill labor and expertise, but with our iterative process, our stance is
that it is crucial to engage experts and laypeople alike to contribute towards and continually update
knowledge AI may draw upon. We thus invite the community to consider interface affordances and
incentive structures for iterative case repository assembly.
We initially ran our process with 20 legal experts, but are starting to branch out to mental health
and medical experts. Even though our approach is meant to be domain-agnostic, domain-specific
requirements of case repositories may still arise—we look forward to surfacing them to better under-
stand the challenges and needs of diverse communities as they assemble their own case repositories.
Additionally, our approach is also designed to be model-agnostic. That is, once a case repository is
created, it is a resource that can be made available to a variety of LLMs. We can then test the case
repository for performance and consistency across models to both improve our approach and learn
more about different models’ abilities to adopt CBR.
Finally, case law is primarily practiced in Western legal systems. Future workshops should involve
experts familiar with non-Western legal frameworks to discuss the benefits and shortcomings of a
CBR-based approach.
4
Conclusion
In this paper, we present a process for enabling CBR to complement existing constitutional approaches
to AI alignment. Our process integrates knowledge of domain experts, the public, and LLMs to
assemble a set of value-encoded precedents in the form of a case repository to inform AI behavior
based on a community’s existing values. More broadly, we see cases as an enlightening medium
for reasoning about morality, given its prior applications in law and philosophy, and by extension,
morality in AI. Our efforts are an early attempt at working with this new medium for AI alignment. As
interdisciplinary conversations are critical to moving the needle in this space, we invite researchers and
practitioners in diverse fields including—but not limited to—AI, philosophy, psychology, cognitive
science, and law, to contribute to continuing discussions to refine, critique, and iterate on our proposed
ideas.
7

--- Page 8 ---

Acknowledgments and Disclosure of Funding
This project was supported by OpenAI’s “Democratic Inputs to AI” grant program. We thank Teddy
Lee, Tyna Eloundou, Aviv Ovadya, members of the grant recipient cohort, and others at OpenAI for
insightful discussions and support.
References
Agnar Aamodt and Enric Plaza. Case-based reasoning: Foundational issues, methodological varia-
tions, and system approaches. AI communications, 7(1):39–59, 1994.
Amanda Askell, Yuntao Bai, Anna Chen, Dawn Drain, Deep Ganguli, Tom Henighan, Andy Jones,
Nicholas Joseph, Ben Mann, Nova DasSarma, et al. A general language assistant as a laboratory
for alignment. arXiv preprint arXiv:2112.00861, 2021.
Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna
Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, et al. Constitutional ai: Harmlessness
from ai feedback. arXiv preprint arXiv:2212.08073, 2022.
Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the
dangers of stochastic parrots: Can language models be too big?
In Proceedings of the 2021
ACM Conference on Fairness, Accountability, and Transparency, FAccT ’21, page 610–623,
New York, NY, USA, 2021. Association for Computing Machinery. ISBN 9781450383097. doi:
10.1145/3442188.3445922. URL https://doi.org/10.1145/3442188.3445922.
Benjamin N Cardozo and Andrew L Kaufman. The nature of the judicial process. Quid Pro Books,
2010.
Quan Ze Chen and Amy X Zhang. Case law grounding: Aligning judgments of humans and ai on
socially-constructed concepts. arXiv preprint arXiv:2310.07019, 2023.
Quan Ze Chen, Daniel S Weld, and Amy X Zhang. Goldilocks: Consistent crowdsourced scalar
annotations with relative uncertainty. Proceedings of the ACM on Human-Computer Interaction, 5
(CSCW2):1–25, 2021.
Susan Craw and Agnar Aamodt. Case based reasoning as a model for cognitive artificial intelligence.
In Case-Based Reasoning Research and Development: 26th International Conference, ICCBR
2018, Stockholm, Sweden, July 9-12, 2018, Proceedings 26, pages 62–77. Springer, 2018.
Robin Downie. Health care ethics and casuistry. Journal of medical ethics, 18(2):61, 1992.
Esin Durmus, Karina Nyugen, Thomas I. Liao, Nicholas Schiefer, Amanda Askell, Anton Bakhtin,
Carol Chen, Zac Hatfield-Dodds, Danny Hernandez, Nicholas Joseph, Liane Lovitt, Sam McCan-
dlish, Orowa Sikder, Alex Tamkin, Janel Thamkul, Jared Kaplan, Jack Clark, and Deep Ganguli.
Towards Measuring the Representation of Subjective Global Opinions in Language Models, 2023.
Robert K Fullinwider. Philosophy, casuistry, and moral development. Theory and Research in
Education, 8(2):173–185, 2010.
Iason Gabriel. Artificial Intelligence, Values and Alignment. Minds and Machines, 30(3):411–437,
Sep 2020. ISSN 0924-6495, 1572-8641. doi: 10.1007/s11023-020-09539-2. arXiv:2001.09768
[cs].
Thomas C Grey. Langdell’s orthodoxy. U. Pitt. L. Rev., 45:1, 1983.
Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song, and Jacob
Steinhardt. Aligning ai with shared human values. arXiv preprint arXiv:2008.02275, 2020.
Oliver Wendell Holmes Jr. The common law. Routledge, 2020.
Albert R Jonsen. Casuistry and clinical ethics. Theoretical Medicine, 7:65–74, 1986.
Robert A Kagan. Adversarial Legalism: The American Way of Law. Harvard University Press, 2019.
8

--- Page 9 ---

Janet L Kolodner. An introduction to case-based reasoning. Artificial intelligence review, 6(1):3–34,
1992.
David Leake and Jay Powell. A general introspective reasoning approach to web search for case
adaptation. In International Conference on Case-Based Reasoning, pages 186–200. Springer,
2010.
Ximing Lu, Sean Welleck, Jack Hessel, Liwei Jiang, Lianhui Qin, Peter West, Prithviraj Am-
manabrolu, and Yejin Choi. Quark: Controllable text generation with reinforced unlearning.
Advances in neural information processing systems, 35:27591–27609, 2022.
John Leslie Mackie. Hume’s moral theory. Routledge, 2003.
Todor Markov, Chong Zhang, Sandhini Agarwal, Florentine Eloundou Nekoul, Theodore Lee, Steven
Adler, Angela Jiang, and Lilian Weng. A holistic approach to undesired content detection in the
real world. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 37, pages
15009–15018, 2023.
J William Murdock and Ashok K Goel. Meta-case-based reasoning: self-improvement through
self-understanding. Journal of Experimental & Theoretical Artificial Intelligence, 20(1):1–36,
2008.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton,
Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F Christiano, Jan Leike,
and Ryan Lowe. Training language models to follow instructions with human feedback. In
S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors, Advances in
Neural Information Processing Systems, volume 35, pages 27730–27744. Curran Associates,
Inc., 2022.
URL https://proceedings.neurips.cc/paper_files/paper/2022/file/
b1efde53be364a73914f58805a001731-Paper-Conference.pdf.
Norbert Paulo. Casuistry as common law morality. Theoretical Medicine and Bioethics, 36(6):
373–389, 2015.
Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori Hashimoto.
Whose opinions do language models reflect? arXiv preprint arXiv:2303.17548, 2023.
Gleb Sizov, Pinar Öztürk, and Agnar Aamodt. Evidence-driven retrieval in textual cbr: bridging
the gap between retrieval and reuse. In Case-Based Reasoning Research and Development: 23rd
International Conference, ICCBR 2015, Frankfurt am Main, Germany, September 28-30, 2015.
Proceedings 23, pages 351–365. Springer, 2015.
Christopher Small, Michael Bjorkegren, Timo Erkkilä, Lynette Shaw, and Colin Megill. Polis:
Scaling deliberation by mapping high dimensional opinion spaces. Recerca: revista de pensament
i anàlisi, 26(2), 2021.
Adam Smith. The theory of moral sentiments, ed. dd raphael and al macfie, 1976. VII, iv, 34.
Taylor Sorensen, Liwei Jiang, Jena Hwang, Sydney Levine, Valentina Pyatkin, Peter West, Nouha
Dziri, Ximing Lu, Kavel Rao, Chandra Bhagavatula, Maarten Sap, John Tasioulas, and Yejin Choi.
Value kaleidoscope: Engaging ai with pluralistic human values, rights, and duties, 2023.
Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford,
Dario Amodei, and Paul F Christiano. Learning to summarize with human feedback. Advances in
Neural Information Processing Systems, 33:3008–3021, 2020.
Cass R Sunstein. Legal reasoning and political conflict. Oxford University Press, 2018.
John Tasioulas. Artificial intelligence, humanistic ethics. Daedalus, 151(2):232–243, 2022.
Zeqiu Wu, Yushi Hu, Weijia Shi, Nouha Dziri, Alane Suhr, Prithviraj Ammanabrolu, Noah A Smith,
Mari Ostendorf, and Hannaneh Hajishirzi. Fine-grained human feedback gives better rewards for
language model training. arXiv preprint arXiv:2306.01693, 2023.
9

```
