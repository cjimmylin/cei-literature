---
title: "Towards Friendly AI - PDF Extract"
source_pdf: "2024-Sun-Towards Friendly AI.pdf"
pages: 15
extracted_at: "2026-01-25T04:08:16.190034"
---

# PDF Extract: Towards Friendly AI

**Source PDF:** 2024-Sun-Towards Friendly AI.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

1
Towards Friendly AI: A Comprehensive Review and
New Perspectives on Human-AI Alignment
Qiyang Sun, Yupei Li, Emran Alturki, Sunil Munthumoduku Krishna Murthy, and Bj¨orn W. Schuller Fellow, IEEE
Abstract—As Artificial Intelligence (AI) continues to advance
rapidly, Friendly AI (FAI) has been proposed to advocate for
more equitable and fair development of AI. Despite its impor-
tance, there is a lack of comprehensive reviews examining FAI
from an ethical perspective, as well as limited discussion on its
potential applications and future directions. This paper addresses
these gaps by providing a thorough review of FAI, focusing on
theoretical perspectives both for and against its development,
and presenting a formal definition in a clear and accessible
format. Key applications are discussed from the perspectives of
eXplainable AI (XAI), privacy, fairness and affective computing
(AC). Additionally, the paper identifies challenges in current tech-
nological advancements and explores future research avenues.
The findings emphasise the significance of developing FAI and
advocate for its continued advancement to ensure ethical and
beneficial AI development.
Index Terms—Friendly Artificial Intelligence (FAI), Ethical
Perspective, Human-AI Alignment
I. INTRODUCTION
T
HROUGHOUT human history, the pursuit of higher
intelligence and enhanced capabilities has been a driving
force behind the progress of civilisation. Humans have en-
hanced their survival capabilities through biological evolution
and developed unique cognitive abilities and collaborative
methods by accumulating culture, technology, and knowledge
[1]. These advancements have allowed humanity to transcend
the limits of natural selection and achieve dominance within
ecosystems.
In recent years, artificial intelligence (AI) has developed
rapidly. Researchers categorise the development of AI into
three stages: Artificial Narrow Intelligence (ANI), focused on
specific tasks; Artificial General Intelligence (AGI), capable
of cross-domain adaptability; and Artificial Superintelligence
(ASI), which surpasses human intelligence [2]. At present,
AI technology has achieved considerable progress at the
ANI stage. For instance, the reinforcement learning system
AlphaGo [3] has demonstrated its ability to surpass top human
players in the complex game of Go. Large language models
Qiyang Sun, Yupei Li and Emran Alturki are with GLAM, Department of
Computing, Imperial College London, UK (e-mail:q.sun23@imperial.ac.uk;
yupei.li22@imperial.ac.uk; e.alturki24@imperial.ac.uk).
Sunil Munthumoduku Krishna Murthy is with CHI – Chair of Health
Informatics, MRI, Technical University of Munich, Germany (e-mail:
sunil.munthumoduku@tum.de).
Bj¨orn W. Schuller is with GLAM, Department of Computing, Imperial
College London, UK; CHI – Chair of Health Informatics, Technical University
of Munich, Germany; relAI – the Konrad Zuse School of Excellence in
Reliable AI, Munich, Germany; MDSI – Munich Data Science Institute,
Munich, Germany; and MCML – Munich Center for Machine Learning,
Munich, Germany (e-mail: bjoern.schuller@imperial.ac.uk).
Qiyang Sun and Yupei Li contributed equally to this work.
(LLMs), trained by vast datasets and substantial computational
resources, have shown exceptional capabilities in language
generation and comprehension [4]. To name but a few, there
are also many machine learning-based applications that have
been successful in various scenarios such as finance, health-
care, and biometric [5], [6], [7].
However, the rapid development of AI has also raised pro-
found concerns. Unlike biological evolution, the development
of AI is not constrained by natural limitations, and its progress
may far exceed the adaptive capabilities of humans [8]. As AI
advances from ANI to AGI and eventually reaches the ASI
stage, its development could become highly uncontrollable [9].
Current AI has already demonstrated superiority over humans
in certain areas, leveraging its memory and computational
abilities. If, in the future, AI acquires emotions, ‘intuition’,
or moral reasoning and makes autonomous decisions without
relying on explicit training data, its actions could conflict with
human interests and even pose threats to humanity. To address
this potential risk, AI ethics research has increasingly focused
on ensuring that the development of intelligent systems aligns
with human values and interests.The concept of friendly AI
(FAI) [10] has thus emerged, becoming a key theoretical
framework for safeguarding the safe development of AI.
AI researcher Yudkowsky first proposed FAI, which aims
to design AI systems that remain beneficial to humanity
under all circumstances [10]. The goal of FAI is to ensure
that AI systems align with human values and ethics while
maintaining sufficient transparency and controllability. This
allows AI to continue promoting human well-being even in
evolving environments. Although the concept was introduced
years ago, it has regained prominence as the possibility of AGI
becomes increasingly tangible [11]. FAI has since inspired
various perspectives focused on its core objectives [12].
In theoretical discussions, philosophers and ethicists hold
diverse views on FAI. On the one hand, proponents argue
that FAI offers an ideal ethical framework. Embedding human
values into AI systems effectively mitigates the risk of AI
behaving unpredictably. They advocate for principles such
as value alignment [13], deontology [14], and altruism [15]
to integrate moral norms and social responsibility into AI,
enabling it to act as a beneficial member of human society.
On the other hand, some philosophers express scepticism about
the feasibility of FAI. They highlight the significant moral and
technical challenges involved [16]. Additionally, the ambiguity
and evolving nature of ‘friendliness’ further complicate its
operationalisation [17]. Safety and trust concerns also arise
[18]. The lack of standardised metrics and reliable evaluation
methods also hinders the FAI’s development status and regu-
arXiv:2412.15114v1  [cs.AI]  19 Dec 2024

--- Page 2 ---

2
latory compliance.
In practical applications, while AGI and ASI remain the-
oretical concepts, computer scientists have begun to explore
technical approaches to implement FAI within existing ANI
systems. For example, eXplainable AI (XAI) [19] helps users
understand the decision-making processes of AI systems rather
than focusing solely on their outputs. Security and privacy-
preserving technologies refine data access controls through
mechanisms such as isolated environments [20] and privacy-
enhancing techniques [21]. These measures limit AI’s direct
access to data, ensuring user privacy while fostering greater
accountability and ethical awareness during collaboration.
Besides, fairness-focused technologies [22] aim to identify
and mitigate biases in AI models, ensuring equitable treat-
ment across diverse user groups and promoting inclusivity in
decision-making processes. Additionally, affective computing
(AC) [23] analyses and responds to users’ emotional states,
enabling AI to better understand human needs and enhance
interactions with greater empathy and personalisation. Collec-
tively, these developments mark a transition in AI program-
ming from unilateral control as ‘slave AIs’ towards ‘utility
AIs’ [24], providing a preliminary foundation for collaboration
between humans and AI.
Despite the concept of FAI sparking extensive academic
discussions in recent years, our search on Google Scholar
(keywords: “Friendly Artificial Intelligence” or “FAI”) reveals
a notable gap. There is currently no comprehensive review
article that systematically summarises the key perspectives
and progress in this field, particularly under the recent break-
throughs in artificial intelligence technologies. This absence
presents challenges for academia and industries in understand-
ing the full scope of FAI and its potential directions.
To address this gap, this paper aims to provide a systematic
review and synthesis of existing research on FAI, offering
a comprehensive analysis of the field. Specifically, the main
contributions of this paper include:
• Proposing and clarifying a coherent definition of FAI: We
present a refined definition that distils key ideas tailored
to the current AI landscape.
• Summarising and categorising the key perspectives in ex-
isting research: We review the differing stances support-
ing and opposing FAI, covering its ethical frameworks,
technical implementation, and societal implications while
highlighting current controversies and limitations.
• Clarifying and categorising FAI-related technologies: We
compile and introduce technical domains that we believe
fall within the scope of FAI, outlining their principles and
potential relevance to the FAI concept.
• Identifying key challenges and future directions for im-
plementing FAI: From a combined theoretical and prac-
tical perspective, we explore the major technical and eth-
ical challenges in realising FAI and propose our insights
for future research.
The remainder of this paper is structured as follows: Section
II provides a detailed discussion of the core definitions and
related concepts of FAI. Section III examines the theoretical
perspectives of FAI, outlining both supportive and opposing
views. Section IV analyses the potential technical subfield
of FAI. Finally, Section V summarises the challenges of
implementing FAI and offers our suggestions and prospects
for future FAI research. We outline the structure of this paper
in Figure 1.
II. FRIENDLY AI DEFINITION
The concept of FAI emerged from the idea of fostering
harmonious coexistence and mutual development between AI
and human society. When the potential for AI to surpass
human capabilities was first introduced to the public, it sparked
widespread apprehension and fear that AI might eventually
dominate humanity. Asimov proposed the Three Laws of
Robotics to ensure safe coexistence between humans and
intelligent machines [25]. These laws state that robots must:
(a) not harm humans, (b) obey human commands unless they
conflict with the first law, and (c) protect their own existence
as long as this does not violate the first two laws.
Asimov’s framework was designed to ensure human-centred
robotic development, which has faced criticism for being
overly dominating and arrogant. Jordana [26] critiques these
laws for treating AI systems as mere tools or slaves, reflecting
an anthropocentric and hierarchical perspective. Scholars such
as Anderson [27] and Palacios-Gonz´alez [28] further advocate
for recognising the rights of AI agents and showing them a
degree of respect. Rather than viewing AI solely as subservient
entities, the goal is to foster a relationship of mutual benefit
and respect, known as FAI.
In Figure 2, we demostrate the stages of AI development and
our current stage. The figure aligns with the three ”as-if” rela-
tionships [24] between AI and humans and their connection to
AI evolution. We argue that we are transitioning from ANI to
AGI. This transition is critical both ethically and technically.
FAI is an important guidance to ensure alignment with human
values when stepping in AGI.
Previous work has explored FAI from various angles, pro-
viding differing definitions. From a moral perspective, Jordana
[26] describes FAI as “those AIs programmed to behave as-if
they were friends of individual humans, though the term as-
if remains ambiguous”. Oliver [29] suggests that FAI should
align with human virtues, yet this concept can feel overly
abstract. From a pragmatic perspective, Mittelstadt [30] argues
that “FAI will benefit, or at the very least, not harm humanity”,
though this seems more aligned with safe AI rather than
genuinely FAI.
Yudkowsky defines FAI in the context of AGI, stating
that it “would have a benign effect on humanity and align
with human interests” [31], which leans toward utilitarianism.
Additionally, recent discussions propose extending FAI to
include friendliness toward animals [32], [33].
While many definitions share common themes, they remain
scattered, complex, and largely one-sided—focusing either on
humans treating AI respectfully or AI ensuring human safety.
However, a comprehensive perspective must emphasise mutual
respect. Based on these insights and evolving perspectives, we
redefine FAI as an initiative to create systems that not only
prioritise human safety and well-being but also actively
foster mutual respect, understanding, and trust between

--- Page 3 ---

3
FAI framework for universal moral principles 
FAI systems prioritise the welfare of human
Hard to realise the moral from technic side
FAI definition is evolving and ambiguous
FAI is still not safe and not trusted by human
Hard to evaluate FAI systems
Theoretical perspective
Cornerstone
Value Alignment
Deontology
Altruism
Against
Moral and technic challenge
Ambiguity and Evolution
Safety and Trust Risk
Evaluation issue
FAI systems can safely accept human interventions and corrections
FAI systems act following human values
Support
Fig. 1.
Theoretical framework of FAI.
humans and AI, ensuring alignment with human values
and emotional needs in all interactions and decisions.
Our definition highlights the essence of friendliness in AI,
emphasising on both interest and moral dimensions. However,
the general concept of FAI remains a subject of intense
debate, particularly between social theorists and technical
practitioners. This ongoing discourse will be further explored
in Section III.
III. THEORETICAL PERSPECTIVES
This section examines and organises the theoretical perspec-
tives supporting and opposing FAI in academia.
A. Support Side
Proponents of FAI have proposed specific frameworks and
guidelines aimed at aligning AI with human values through
ethical design and policy collaboration.
1) Cornerstone: The proposer of FAI, Yudkowsky, has ad-
vanced several theories and principles to support its realisation.
He first introduced the framework of a Structurally Friendly
Goal System [10]. This framework emphasises the creation of
systems capable of overcoming subgoal errors and source code
flaws while addressing issues in the content of supergoals,
goal system structures, and their philosophical foundations.
Through recursive optimisation and consistency maintenance,
such systems reduce dependency on initial conditions, ensur-
ing that AI behaviour remains aligned with its intended ob-
jectives. Then, Yudkowsky proposed the concept of Coherent
Extrapolated Volition (CEV) [34], suggesting that AI’s goals
should not be confined to current human preferences. Instead,
they should be based on an idealised volition, reflecting “our
wish if we knew more, thought faster, were more the people
we wished we were, had grown up farther together.” This
approach envisions AI aligning its objectives with the deeper,
more informed aspirations of humanity rather than short-term
or limited desires. Building on this foundation, Yudkowsky and
his team later introduced the concept of Corrigibility [35]. This
principle ensures that AI systems can cooperate with human
interventions, including accepting goal modifications or safe
shutdown commands, without resisting or manipulating these
actions. Corrigibility highlights the importance of designing
utility functions that enable AI systems to propagate and sus-
tain corrective behaviours while avoiding unintended actions
triggered by the existence of correction mechanisms, such as
shutdown buttons.
2) Value Alignment: Some scholars support FAI from the
perspective of value alignment [36], a concept that seeks to
ensure AI systems act following human values, interests, and
intentions by integrating normative principles with technical
methodologies. Russell explicitly introduced the term “value
alignment” [37]. He argued that AI systems should be designed
to observe and learn from human behaviour to infer and
model human value systems. This allows them to dynamically
adjust their utility functions to achieve ethical consistency. He
highlights the inherent uncertainty and complexity of human
goals [38], arguing that “machines are beneficial to the extent
that their actions can be expected to achieve our objectives.”
This approach seeks to align AI behaviour with human values
but faces significant challenges in capturing the nuanced and
often conflicting ethical principles of human societies.
In response to Russell’s perspective, Peterson criticised the
traditional utility-function-based approach for its limitations in
reflecting complex and dynamic moral values [39]. He argued
that it overly relies on the idealised assumption of consensus
on ethical theories. Peterson proposed a geometric method
based on conceptual spaces, constructing multidimensional
moral spaces using paradigmatic cases. By evaluating the
similarity between new situations and these paradigms, AI

--- Page 4 ---

4
ANI
AGI
ASI
FAI
Slave AI
Utility & Social AI
Current stage
Fig. 2. Stages of AI development
behaviour could be assessed for ethical compliance. Compared
to utility functions, this method is more intuitive and flexible,
particularly in adapting to complex moral scenarios.
Building on these theories, Fr¨oding and Peterson intro-
duced the concept of virtue alignment [24], extending value
alignment to consider AI’s potential influence on human
behaviour and character. Their ‘as-if friendship’ framework
advocates that AI should emulate core virtues found in human
friendships, such as empathy and helpfulness. This approach
promotes social functionality while positively influencing the
development of human virtues. They specifically highlighted
the ethical risks posed by ‘slave-like AI’ models, advocating
for the design of friendly utility AI or social AI to replace such
systems, thereby fostering cooperation and responsibility.
Additionally, Bostrom expanded the discussion on value
alignment by focusing on the potential risks of ASI. However,
his work does not exclusively address the direct alignment
of AI’s goals with human values. Instead, Bostrom’s value
loading problem explores how to mitigate value drift when
idealised solutions, such as CEV, are unattainable due to the
complexity and diversity of human values [40]. He proposed
suboptimal strategies such as the Hail Mary Approach, Value
Porosity and Utility Diversification.
3) Deontology: Deontology [41] is an ethical framework
proposed by philosopher Kant. The core idea of deontology is
that the morality of actions should be determined by adherence
to universal moral principles rather than solely judged by their
outcomes. Deontology emphasises the dignity and rights of
individuals, asserting that all actions must treat humanity as
an end in itself, not merely as a means. This principle-based
framework has garnered significant attention as an ethical
foundation for FAI.
Mougan and Brand argue that integrating deontology into
fairness metrics for AI provides a stronger ethical basis for
value alignment [42]. They criticise the dominant utilitarian
approaches to fairness, which focus excessively on outcome
optimisation while neglecting procedural fairness and moral
principles. They propose that AI systems should prioritise
procedural fairness by adhering to universal principles and re-
specting individual dignity, ensuring transparency and fairness
in decision-making processes.
D’Alessandro notes that deontology’s principles, particu-
larly the emphasis on avoiding harm, have a practical appeal
[14]. However, he cautions that adherence to deontological

--- Page 5 ---

5
rules may not always align with AI safety requirements.
In cases where rules conflict with practical safety needs,
D’Alessandro argues that AI safety should take precedence
over strict adherence to moral rules.
Hooker and Kim propose a formal ethical framework based
on deontology [43]. They developed a system utilising Quanti-
fied Modal Logic (QML) to implement the Universalisability
Principle in AI ethics. Their framework builds on the Dual
Standpoint Theory, allowing for the evaluation of moral ac-
tions from both causal and rational reasoning perspectives.
By formalising action rules, they aim to achieve ethical
transparency, ensuring that AI can systematically evaluate
the feasibility of its actions under universal conditions while
respecting the autonomy of other agents. This system uses
logical reasoning to avoid inconsistencies in moral conflicts.
4) Altruism: Altruism [44] is a core ethical concept that
prioritises the welfare of others, even at the cost of self-
interest. Unlike outcome-focused utilitarianism, altruism em-
phasises the motives and principles of care and direct support
for others. In FAI research, altruism provides critical ethical
guidance for designing AI systems’ goals and behaviours.
Stoel suggests embedding altruistic values into AI to guide
its development in the context of technological singularity
[15]. This integration, achieved through programming or im-
itation, enables AI systems to exhibit cooperation and social
responsibility. Stoel argues that altruism-driven AI enhances
societal collaboration, better balances conflicting interests, and
reduces inequalities and potential threats from technology. The
concept of an ‘altruistic singularity’ underscores the central
role of altruism in shaping future AI societies.
Maillart et al. identify Altruistic Collective Intelligence
(ACI) as a core theoretical framework for advancing AI [45].
By integrating collective intelligence with intrinsic motivation
and embracing principles of transparency and collaboration
from the open-source movement, they argue that ACI balances
technological innovation with ethical values. They highlight
that collective intelligence, facilitated by task self-selection,
peer review, and openness, enhances AI’s robustness and
accountability. The integration of competition and coopera-
tion (coopetition) dynamics improves algorithm diversity and
optimisation.
Effective Altruism (EA), driven by rational analysis and
evidence-based methods, provides vital support for FAI de-
velopment [46]. EA’s central tenet is to maximise global well-
being, aligning closely with FAI’s goal of ensuring that AI
behaviour adheres to human values. EA prioritises addressing
global challenges with significant impacts on humanity and
future generations, such as the existential risks posed by
superintelligent AI. It advocates for multidisciplinary collab-
oration, a long-term perspective, and the inclusion of diverse
objectives within utility functions to ensure AI’s ethical design
dynamically adapts to complex moral contexts.
B. Opposition Side
Although FAI has been proposed and supported by numer-
ous ideas, there remain opposing perspectives. This paper will
explore these objections along with potential arguments that
the public might raise.
1) Moral and Technical Challenges: Achieving friendliness
in AI systems presents significant challenges from both moral
and technical perspectives. Boyles and Joaquin [16] contend
that counterfactual antecedents pose substantial difficulties in
deriving ideal value-based notions. For AI systems, moral
reasoning is guided, learnt, and expressed through factual data.
However, counterfactual antecedents introduce considerable
complexity, as reasoning with counterfactual premises is in-
herently challenging [47]. A simple example is the inference
that we could play outside if the weather is good, conditional
premises showing that bad weather would prevent outdoor
activities; however, this reasoning may overlook additional
conditions in the antecedent, such as the possibility that the
chosen venue might be closed. Furthermore, the virtually
infinite range of counterfactual scenarios places overwhelming
demands on AI systems, which has issues with their current
technical capabilities as well.
The complexity is compounded by the technical limitations
of contemporary AI. Bostrom and Yudkowsky [48] highlight
that defining moral guidelines and embedding ethical and
virtuous behaviour into AI systems entails immense com-
plexity. This view is supported by a European Parliament
study [49], which underscores the challenges associated with
programming AI systems to adhere to ethical frameworks.
Consequently, the concept of FAI remains speculative and dif-
ficult to operationalise from some sociotechnical perspective.
In addition, the concept of the Utilitarian Paradox emerges
as a critical consideration. Originally introduced by Kroon
[50], this paradox is also relevant in the context of FAI
systems. While the aim of FAI is to maximise overall benefits
for humanity, determining whose interests should be prioritised
remains an unresolved ethical dilemma. A classic illustra-
tion of this is the Trolley Problem, which exemplifies the
challenges in making ethical trade-offs. Moreover, achieving
a mutually ‘friendly’ relationship between AI systems and
humans poses significant difficulties. As van Wynsberghe [51]
argues, social robots and AI systems may initially resort to
manipulative strategies, such as deceiving humans, to establish
trust and demonstrate their utility. This dynamic raises further
concerns about the authenticity and sustainability of the trust
relationship between humans and AI.
2) Ambiguity and Evolution: The definition of friendliness
is ambiguous and continues to evolve. Boyles [17] argues
that ethics are not static and may be influenced by FAI
systems in a mutual manner. He also emphasises the subjective
nature of moral definitions, which lack an objective ground
truth for AI systems to use as a basis for learning. The
concept of friendliness, in particular, is deeply rooted in moral
philosophy. An example of this evolution can be seen in
Medieval Europe, where friendliness was largely defined by
kindness and mercy within religious communities. During the
Enlightenment, however, Kant [52] proposed that individuals
possess innate human rights and should respect one another
based on rationality rather than religious imperatives. This
shift marked a significant redefinition of friendliness within
human society, and the concept continues to evolve to this day.
Given this fluidity, the definition of FAI is neither stable nor
consistent, making it a considerable challenge for AI systems

--- Page 6 ---

6
to learn and adapt to such a dynamic moral framework.
3) Safety and Trust Risk: Beyond moral and philosophical
concerns, critics also contend that FAI poses significant safety
risks. Sparrow [18] argues that FAI cannot fully mitigate the
dangers associated with the emergence of ASI, as its impli-
cations for human freedom could be catastrophic. Similarly,
Boyles and Joaquin [16] highlight the challenges of accurately
understanding and encoding human values, suggesting that this
difficulty could lead to unintended and unsafe actions by FAI
systems.
This is one potential example of this issue that highlights a
potential hazard associated with the uncontrollability of FAI
[53]. Scholars argue that “FAI may exert unforeseen influences
in the future, often exemplified by the ‘butterfly effect”’.
This phenomenon suggests that small, seemingly insignificant
actions may not produce adverse effects in the short term
but could escalate exponentially over time if left unmonitored
[50]. Another interesting perspective from the field of physics,
presented by Tegmark [54], argues that life is fundamentally
organized by elementary particles. According to this view, the
development of FAI necessitates a novel arrangement of these
elementary particles for the future, a configuration that may be
difficult to discover and, as a result, may not endure over time.
Consequently, this could pose a potential risk, as FAI might
lack a stable structural foundation for its existence together
with human.
More concerning, monitoring FAI systems presents signif-
icant challenges. While these systems are trained to avoid
displaying hazardous behaviour, this does not necessarily mean
they lack knowledge of such risks. Recent advancements in
LLMs exemplify this issue. Queries involving ethical risks are
designed to be avoided during interaction, yet strategies like
‘jailbreaking’ reveal that these models retain the underlying
knowledge of such risks [51]. For example, role-playing
scenarios can enable AI systems to circumvent programmed
restrictions, exposing the inherent difficulties in ensuring com-
pliance.
Such concerns have fuelled opposition to the development
of FAI, as critics argue that its potential for unintended and
uncontrollable outcomes outweighs its purported benefits [18].
4) Evaluation and Compliance Issues: Assessing the de-
velopment status of FAI and ensuring its compliance with
regulatory standards poses significant challenges due to the
difficulty in measuring its capabilities. This issue is analogous
to other AGI systems, such as LLMs. Currently, there are no
straightforward or universally accepted metrics to evaluate the
quality of LLMs. Instead, labour-intensive methods, such as
human evaluations, or unreliable approaches, such as assess-
ments conducted by other AGIs, are often employed.
The challenge is even greater for FAI because its goals are
inherently subjective, aiming to align with human interests
and exhibit friendliness toward humanity. Without an objective
and clearly defined target, it becomes nearly impossible to
quantify FAI’s capabilities or measure its success in achieving
its intended purpose. This version enhances clarity, academic
tone, and readability.
IV. APPLICATIONS
Although the ultimate goal of FAI remains in the AGI and
ASI stages, which are yet to be realised, computer scientists
have begun exploring technical approaches to implement FAI
within existing ANI systems. Several substantial frameworks
have been proposed. Among them, Trustworthy AI [55] is
the most comprehensive, encompassing key aspects such as
transparency, fairness, safety, and ethics. It focuses on building
multi-dimensional trust, enhancing user and societal confi-
dence in AI systems. This framework integrates principles
from Responsible AI [56] , Ethical AI [57] , and Safety AI
[58], while placing additional emphasis on robustness, which
provide a foundation for the more advanced stages of FAI.
Responsible AI prioritises transparency, privacy protection,
and accountability, ensuring that AI systems comply with
regulations and societal norms. Its key focus is on reducing
bias and clarifying responsibility to mitigate risks to public
trust caused by system errors or decision-making failures.
Ethical AI addresses moral principles and value alignment in
AI systems. It aims to ensure that AI behaviours adhere to core
human values, such as fairness, respect, and dignity. Ethical AI
provides the necessary moral constraints to prevent emotional
manipulation and privacy violations, ensuring compliance with
ethical standards.
Safety AI concentrates on operational security and risk
prevention. It addresses technical challenges such as defending
against adversarial attacks, protecting against data breaches,
and ensuring system reliability in diverse scenarios.
Figure 3 illustrates the unique focuses and interconnections
of these frameworks. In addition, this section also introduces
specific applications currently in practice, including XAI,
privacy protection, fairness, and affective computing. These
technologies are vital for regulating AI behaviour, understand-
ing AI decision-making processes, and improving AI’s emo-
tional understanding of humans. We have not assigned these
technologies to any single AI framework, as they often overlap
and align with multiple principles. More importantly, they
represent how they enable trust management for ANI systems
and prepare the practical groundwork for FAI framework in
the future AI stages.
A. Explainable AI
XAI is defined as “a set of methods applied to an AI
model or its predictions that provide explanations for why the
AI made a specific decision” [59]. The primary objective of
XAI is to enhance understanding, trust, and accountability in
AI systems by offering clear insights into their actions and
reasoning processes. This goal aligns closely with one of the
core principles of FAI, which emphasises the importance of
transparency and trust to ensure that AI systems prioritise
human values and interests. Since 2016, the importance of
explainability in AI has been widely recognised, leading to
a surge in research activity [60]. Consequently, a wide range
of XAI techniques grounded in various AI theories has been
developed. Among the popular methods in academic research
are LIME, SHAP, Grad-CAM, and LRP, each representing a

--- Page 7 ---

7
Trustworthy AI 
Ethical AI
Responsible AI
Safety AI
Fairness
AC
Privacy
XAI
FAI
...
Fig. 3. Unique focuses and interconnections of trustworthy frameworks
unique implementation of techniques. These will be quickly
introduced next as examples.
1) LIME: Local Interpretable Model-agnostic Explanations
(LIME) [61] is a widely used perturbation-based approach
in XAI that trains an explainable model by generating new
sample points around the selected sample points and using
these new sample points and the predicted values from the
black-box model. A similarity calculation and the features to
be selected for explanation are then defined. Sample weights
are assigned based on the distance to the sample points after
perturbations are sampled around them. This approach allows
for obtaining a good local approximation of the black-box
model, which means that an explainable model can be used to
explain the complex model locally [62]. Notably, LIME is a
model-agnostic approach, meaning it can be applied to any AI
model regardless of its architecture or underlying principles.
2) SHAP: Shapley Additive exPlanations (SHAP) method
[63] integrates the concept of Shapley values from game
theory into an additive feature attribution framework. In SHAP,
each input feature is treated as a player in a cooperative
game, where the predicted output represents the total payoff.
To determine each feature’s contribution, SHAP calculates
Shapley values based on a weighted average of all possible
feature permutations, with each feature assigned a weight
according to its presence in each permutation. This process
yields a Shapley value for each feature, indicating its specific
contribution to the final prediction. SHAP is notable for its
theoretical guarantees of fairness and consistency, as it ensures
each feature’s contribution is weighted equitably across all
possible permutations.
3) Grad-CAM: Gradient-weighted Class Activation Map-
ping (Grad-CAM) [64] is a gradient-based approach that
extends Class Activation Mapping (CAM) to address its lim-
itations while maintaining compatibility with standard convo-
lutional neural networks (CNNs). Unlike CAM, which relies
on global average pooling and requires architectural mod-
ifications, Grad-CAM leverages the gradients of the target
class score to the feature maps in the last convolutional layer.
These gradients are averaged to compute weights that quantify
the importance of each feature map. The feature maps are
then combined using these weights, producing a heatmap that
highlights the regions of the input image most relevant to the
model’s prediction.
However, it is important to note that Grad-CAM relies on
the existence of convolutional layers and the availability of
gradient information. As a result, it is limited to models that
include convolutional operations, such as CNNs or hybrid
architectures incorporating convolutional components. This
dependency makes Grad-CAM unsuitable for models that lack
such layers, including purely sequential models like recurrent

--- Page 8 ---

8
neural networks (RNNs) or traditional machine learning algo-
rithms such as decision trees or random forests.
4) LRP: The Layer-wise Relevance Propagation (LRP)
approach is based on the idea of backpropagation [65]. The
goal is to assign relevance scores to each input feature or
neuron in a network to indicate its contribution to the output
prediction. LRP recursively propagates the relevance scores
from the output layer of the network through a Deep Taylor
Decomposition (DTD) propagation to the input layer. At
each layer, the relevance scores are redistributed to the input
neurons based on their contribution to the output activation
of that layer. This redistribution is performed using a set of
propagation rules that ensure that the sum of the relevance
scores at each layer is conserved. However, it is important to
note that LRP is not model-agnostic, as it requires a layered
architecture and propagation rules tailored to the types of
layers within the neural network.
To sum up, although XAI is an independent branch within
the field of ANI, it reflects a profound connection to FAI
principles and provides important technical support for its
future realisation. Firstly, the primary role of XAI is to
uncover the internal decision-making processes of AI systems.
Techniques such as SHAP and LIME explain the model’s
reliance on input features, while Grad-CAM and LRP vi-
sualise the focus regions within the model. Emerging XAI
methods also attempt to explain model decisions from the
perspective of human concepts [66], [19]. These approaches
make the behaviour of complex AI systems more transparent
and provide essential tools for understanding their operational
logic. Secondly, XAI establishes a foundation for monitoring
AI behaviour. Researchers can identify biases, anomalies, or
potential ethical risks, ensuring that AI actions remain within
the control of its designers. Finally, XAI facilitates dynamic
corrections and model optimisation, helping AI systems align
with human values and progressively adhere to specific ethical
standards.
B. Privacy
Privacy modelling is a fundamental component of ethically-
aware AI systems. As the goal is to design FAI systems that
engage with humans on the basis of mutual respect, it is
imperative that such systems neither covertly acquire private
data nor exploit it inappropriately. Privacy modelling serves as
a mechanism to safeguard personal information, embodying
both a critical element and a practical application of FAI
principles.
1) Privacy-preserving model: Privacy-preserving models
represent a critical advancement in the domain of ethically-
aware AI, as they ensure that individual privacy remains intact
during the process of data learning. These models are defined
by their capacity to prevent the compromise of personal in-
formation while enabling AI systems to effectively learn from
data. As highlighted by Yang et al., the Phase, Guarantee, and
Utility triad provides a robust framework to evaluate and guide
the development of privacy-preserving systems [67]. Building
on this foundation, Lu et al. proposed a framework designed
to enable learning over encrypted data, further enhancing data
security during machine learning operations [68].
These models not only advance privacy protection but
also suggest potential directions for improving the regula-
tion of FAI systems. Incorporating privacy-preserving mech-
anisms into FAI regulatory frameworks can provide safe-
guards against misuse of sensitive information. Additionally,
exploring methodologies for FAI systems to maintain their
own privacy could enhance their resilience, minimising the
likelihood of personal information leakage even in adversarial
scenarios. These efforts underscore the dual role of privacy-
preserving models: protecting user data and strengthening the
integrity of AI systems themselves.
2) Federated Learning: An alternative approach to directly
safeguarding private data is to mitigate privacy leakage through
Federated Learning, a distributed paradigm that trains machine
learning models across decentralised devices containing local
data samples. This method circumvents the need for cen-
tralised data collection, thereby maintaining a level of privacy
and reducing the potential impact of privacy breaches. Yang
et al. provide a comprehensive comparison and discussion
of federated learning systems [69]. Additionally, Zhu et al.
propose an Adaptive Personalised Cross-Silo Federated Learn-
ing system incorporating Homomorphic Encryption, which
enhances personalised federated learning configurations [70].
The adoption of such distributed information storage meth-
ods is growing, offering significant potential for FAI systems
to leverage decentralised data storage. This approach intro-
duces a novel mechanism for privacy preservation, aligning
with contemporary efforts to enhance secure and ethical AI
development.
In addition to the previously discussed frameworks, there are
other types of privacy protection models that is pivotal in the
developing FAI systems. For instance, differential privacy has
emerged as a foundational approach, ensuring that individual
data points cannot be reverse-engineered [71]. Similarly, user-
centric systems prioritise user control and transparency over
data usage, fostering trust and aligning with ethical principles
of AI design [72].
These models are built into FAI systems as they contain
values of privacy, security and dignity. Implementing such
privacy-preserving approaches to FAI frameworks does more
than protect user data, it builds public confidence in AI. All
these special methods go hand in hand to create the ideal of
AI systems that are both functionally and ethically sound.
C. Fairness
Fairness in AI refers to the impartial and just treatment of
individuals or groups by algorithms, ensuring that decisions
are free from biases related to inherent or acquired charac-
teristics. In the context of decision-making, fairness is the
absence of any prejudice or favoritism toward an individual or
group based on their inherent or acquired characteristics [73].
Within the current technical framework, fairness is primarily
defined as utilitarian fairness [74] , which focuses on achieving
equality in AI outputs across different groups through technical
methods. While this definition is relatively narrow and does
not fully address deeper issues such as structural inequalities
or ethical fairness, it aligns with FAI’s goal of comprehensive

--- Page 9 ---

9
value alignment with humanity. A truly ”friendly” AI system
must embody fairness, treating all user groups equitably while
maintaining harmony between technical and ethical consider-
ations.
The technical application of fairness is currently focused on
data, models and outputs:
1) Data: Imbalanced data distributions often lead models
to favour majority groups during training, thereby undermining
fairness. Resampling techniques [75] are commonly employed
to adjust the proportions of minority and majority groups,
resulting in a more balanced distribution. Additionally, gen-
erative approaches are utilised for data augmentation [76],
increasing data diversity while mitigating bias during train-
ing. For example, generative models can produce additional
samples for minority groups, improving their representation
within the dataset.
2) Model: Model-level fairness applications primarily in-
troduce constraints during training to adjust the learning
process. For example, the Equalized Odds method [77] adds
constraints to the training objective, ensuring that model out-
puts are conditionally independent of protected attributes given
the true labels. This constraint aims to prevent predictions from
being biased by sensitive attributes across different groups.
Additionally, recent generative methods remove features un-
related to the primary task, such as gender or age, and create
new data representations to force the model to learn attribute-
independent features, thereby reducing bias [7], [78].
To address individual fairness, researchers propose incor-
porating constraints into training to ensure similar individuals
receive similar predictions. For instance, ”Fairness Through
Awareness” [79] introduces distance-based similarity measures
and incorporates these constraints during training to align
predictions for similar individuals. Furthermore, ”Accurate
Fairness” [80] seeks to resolve the trade-off between individual
fairness and model accuracy. This approach combines fairness
and accuracy constraints during training, balancing these ob-
jectives and enhancing individual fairness without significant
performance loss. These advancements represent important
directions for improving fairness at the model level.
3) Output: At the output level, post-processing techniques
adjust model predictions to meet fairness requirements without
altering the model structure or requiring retraining. These
methods modify outputs directly, achieving greater balance
across different groups. Calibration techniques adjust pre-
diction probabilities, such as setting different thresholds for
various groups [81], to optimise result distribution and im-
prove inter-group fairness. Distribution adjustment methods
reallocate prediction labels or probabilities to reduce biases
among groups. While these approaches offer high flexibility
and applicability, they may lead to performance trade-offs and
are less effective when addressing deep-rooted biases in data
or the model itself.
To sum, fairness remains an important yet developing as-
pect of ANI. Current methods largely centre on utilitarian
fairness, aiming to balance outcomes at group or individual
levels. These methods are applied through pre-processing, in-
processing, and post-processing techniques. In the context of
FAI, fairness is both a fundamental requirement and a core
component. It ensures alignment between AI systems and
human values. Achieving comprehensive fairness enhances
trust in AI and supports the broader goal of FAI: ethical and
inclusive intelligence.
D. Affective Computing
Affective Computing (AC) is the study of systems designed
to understand, interpret, and process human emotions [82]. It
plays a crucial role in the development of FAI systems, as the
ability to comprehend emotional cues is essential for creating
interactions that are perceived as empathetic or ”friendly.”
For instance, demonstrating kindness involves recognizing
and responding to emotional signals, a domain where AC is
particularly effective. In general, AC models emphasize emo-
tion recognition, which is foundational for designing systems
that can accurately perceive and respond to human affective
states. The applications of AC span a wide range of fields,
including healthcare, education, entertainment, and robotics,
among others. In this section, we review the foundational
developments and applications of AC, highlighting its potential
as a key component in the design of FAI systems.
1) Development history: The development of AC has un-
dergone significant historical progress. In its early stages, AC
focused primarily on recognizing general emotional states,
a field that shares overlap with psychology and cognitive
science, for example with theories proposed by Ekman [83].
As machine learning models advanced, AC evolved to empha-
size emotion recognition, with key contributions such as the
development of Facial Expression Recognition (FER) through
the introduction of the Facial Action Coding System (FACS)
by Ekman [84] and its integration into emotion recogni-
tion technologies. Additionally, Speech Emotion Recognition
(SER) emerged as a prominent application as well, utilizing
acoustic features such as tone and pitch to predict emotional
states proposed by Schuller [85].
As the applications of AC have become increasingly prac-
tical, the field has evolved into specialized subfields, in-
cluding the recognition of specific emotions and their ap-
plication within particular domains. Healthcare provides a
notable example of this evolution. AC has been integrated
into physiological monitoring, utilizing biological sensors to
assess emotional states by analyzing physiological features
such as heart rate, skin responses, and brain activity [86].
In their comprehensive review, Wang et al. [87] examine the
breadth of affective computing models, while Singh et al. [88]
explore models tailored specifically to the psychological do-
main. Schuller et al. [89] also provide some future directions.
Beyond healthcare, AC has also been applied to the analysis
of everyday behaviors as indicators of emotional states [90].
With the growing recognition of AC systems, their ap-
plications have expanded into multimodal frameworks. The
shift from single-modality to multimodal approaches—such
as integrating facial expressions, voice, and physiological
signals like heart rate—has significantly advanced the field
and was adept at analyzing complex emotions in intricate
scenarios. Bj¨orn et al. [91] present a multimodal approach to
emotion recognition in audiovisual communication, providing

--- Page 10 ---

10
valuable insights into the integration of visual and auditory
cues for emotion detection in this domain. Shi and Huang [92]
proposed a novel framework that effectively integrates multi-
modal cues by capturing cross-modal relationships to analyze
various emotions in conversational contexts. Similarly, Jun et
al. [93] developed a Multi-Layer Graph Attention Network,
which aligns with similar applications in emotion recognition.
Schuller et al. [94] explored the analysis of user states and
traits through multimodal data, advancing the paradigm in
new directions. Moreover, recent reviews by Cabada et al.
[95] highlight key challenges and opportunities, including
the integration of LLMs into emotion recognition systems,
marking a significant maturation in AC research. These de-
velopments suggest that AC models are approaching a level
of sophistication where they can serve as essential components
of FAI systems, enabling dynamic, real-time emotion analysis
and understanding.
2) Application: After the vertical discussion of this fields
development, we begin a horizontal review on AC application
here. There we mainly review healthcare, education, entertain-
ment, and robotics.
a) Healthcare: Healthcare is one of the primary applica-
tions of AC, particularly in the domain of mental health. Liu et
al. [96] present the most recent review of foundational models,
challenges, and future directions in AC, building upon the
valuable insights provided by Shu et al. [97]. Neural networks
are commonly employed in this domain [98], and Mallol et
al. [99] introduce a curriculum-based approach as a notable
example. AC models in healthcare typically focus on emotion
recognition, integrating physiological signals measured by
devices such as smartwatches. These models aim to monitor
emotional states, enhance patient care, and support mental
health management.
b) Education: The integration of AC is increasingly
important in the educational process, particularly in virtual
learning environments. Yang et al. [100] propose models that
detect emotions based on facial expressions, while Lasri et
al. [101] offer similar insights, emphasizing the use of con-
volutional neural networks. Additionally, sentiment analysis
methods have proven valuable for emotion detection in educa-
tional contexts [102]. Speech analysis models, as reviewed by
Schr¨oder [103], are also beneficial for understanding emotional
states in students. The field continues to evolve, as highlighted
in the overview by Yu et al. [104]. AC models in education are
increasingly capable of monitoring remote teaching, particu-
larly within the context of the current hybrid education model,
where they can enhance both student engagement and learning
outcomes.
c) Entertainment:
AC models have significantly en-
hanced both commercial and non-commercial applications in
the entertainment industry. De et al. [105] design an interface
that connects AC models with brain-computer interactions,
enabling more flexible and immersive experiences in enter-
tainment contexts. Huang et al. [106] utilize emotion decoding
for movie classification, which can contribute to improving
recommendation systems. Li [107] offers insights into the
application of AC models in e-learning platforms, particularly
using genetic algorithms for art design. AC models are capable
of extracting nuanced emotional information in entertainment,
supporting downstream tasks such as optimizing content for
greater audience engagement and increasing media views.
d) Robotics: Robotics has made significant strides, but
the integration of AC models can further enhance robots’ em-
pathy and reasoning capabilities. Spezialetti et al. [108] high-
light recent advances and future perspectives in this area, while
Stock et al. [109] provide comprehensive reviews, placing
particular emphasis on the psychological aspects of robotics.
Additional techniques have demonstrated the effectiveness of
AC technologies in this domain. For instance, Leo et al. [110]
design a robot-child interaction system based on AC models,
aimed at improving therapeutic outcomes, while Zhang et
al. [111] develop a humanoid robot that incorporates emo-
tion recognition. Furthermore, some human-interactive robots,
known as sociable agents, which are designed to demonstrate
emotional behaviours and enhance human-robot interaction
[112]. These approaches enable FAI to be instructed with
greater specificity, allowing it to analyse human emotions in
a more targeted and precise manner. With the integration of
AC models, robotics is positioned to become an increasingly
promising field, empowering robots to better understand and
respond to human emotions.
3) Future direction: From the early challenges in emo-
tion detection, as developed by Schuller et al. [113], to the
present, the field of AC remains a dynamic area of ongoing
research. Schuller et al. [114] emphasize that foundational
models have reshaped the direction of AC research, suggesting
that further integration of human psychological features is
necessary. Additionally, the incorporation of empathy within
AC models is becoming increasingly important, as some
previous studies have explored [115], although significant gaps
remain regarding how and what aspects of empathy should be
embedded.
In summary, AC models hold considerable promise for
fostering the development of FAI systems, much like their
applications in the areas discussed above. These models are
poised to become critical components of FAI applications, and
the continued advancement of foundational AC technologies
will play a key role in the evolution of these systems.
V. CHALLENGES AND SUGGESTIONS
In this section, we discuss the current challenges facing the
FAI field and provide some forward-looking outlooks.
A. Challenges
One major obstacle lies in the inability to establish a unified
definition for FAI. Theoretical definitions of ‘friendliness’ vary
widely, with scholars proposing conflicting frameworks. For
instance, Yudkowsky’s CEV supports humanity’s ideal collec-
tive will, while Mittelstadt’s “not harm humanity” principle
prioritises safety and harm avoidance. These differing per-
spectives lead to disagreements over the scope and objectives
of FAI, further complicating efforts to quantify its success.
Without a universally accepted definition, practitioners lack
clear guidelines for evaluating whether an AI system aligns
with FAI principles, rendering its practical application even

--- Page 11 ---

11
more challenging. The absence of a widely recognised defi-
nition for FAI has led to fragmented discourse on the topic.
While many scholars share similar theoretical concerns about
the future of AI and have proposed related ideas, they often do
not explicitly use the term ‘FAI’ [116]. This lack of consistent
terminology limits the dissemination of these ideas, making
it challenging to collect and organise relevant contributions
into a coherent body of knowledge. As a result, the field
struggles to achieve the critical mass needed to drive large-
scale collaborative efforts.
Also, this ambiguity stems from defining ‘friendliness’ in a
culturally diverse world. Different societies and cultures pri-
oritise distinct moral values; for example, individual autonomy
may be emphasised in some cultures, while collective welfare
is prioritised in others. This raises the question of how to
balance these conflicting priorities within a single framework.
Additionally, determining what values should take precedence
in cross-cultural contexts is an inherently subjective process,
further complicating efforts to create universally friendly AI
systems. To meet these demands, FAI must not only accom-
modate diverse ethical standards but also navigate complex de-
cisions about whose interests to prioritise, a task that remains
unresolved in theory and practice. As previously discussed,
FAI lacks a unified theoretical framework. Consequently,
developers cannot rely on clear guidelines when designing
and implementing AI systems, resulting in confusion and a
lack of direction in practice. Developers find it challenging
to determine whether a specific technological implementation
aligns with the core goals of FAI. In practical scenarios, this
ambiguity in ethical standards may lead to further difficulties.
Moreover, the absence of a clear theoretical foundation makes
it nearly impossible to quantify or evaluate the success of ideal
FAI systems.
Furthermore, The development of FAI remains largely a
preparatory effort, as the AGI era has not yet arrived. Most
current research focuses on ANI technologies. While progress
has been made in areas like computer vision and natural
language processing, some fields still fall short of human-
level capabilities. For example, speech generation often lacks
nuance and contextual understanding. Tasks requiring fine
motor skills or complex reasoning, such as robotic surgery or
decision-making in uncertain environments, also often remain
beyond AI’s abilities. As a result, research today focuses on
building more precise and efficient AI models rather than
addressing broader ethical alignment or value-driven frame-
works. This gap highlights the difficulty of transitioning from
task-specific ANI to the comprehensive systems required for
FAI.
Besides, it is unclear whether some current AI subfields will
eventually be formally included within the FAI framework.
For instance, while XAI aims to enhance transparency and
trustworthiness, its connection to FAI’s broader ethical goals
is mostly indirect. Privacy-preserving technologies, although
effective in building trust, primarily address technical concerns
and lack full integration with FAI’s long-term objectives.
Similarly, AC seeks to improve AI’s ability to understand
and respond to human emotions, but its focus remains on
human-machine interaction rather than deeper alignment with
human values. Consequently, no current research provides a
systematic definition of the technical directions that should
or could be included under FAI. This ambiguity not only
affects the prioritisation of research efforts but also leads to a
fragmented approach to long-term goals.
The realisation of FAI requires broad collaboration across
disciplines and industries, yet this collaboration faces multiple
challenges in practice. First, differences in regulations and
policy priorities between countries create significant obstacles.
Some nations prioritise technological competitiveness, while
others focus on ethics and safety. This lack of alignment com-
plicates the creation of global standards. Second, the sensitive
nature of AI technology adds another layer of complexity.
In areas such as national security, military applications, or
biomedical research, the sharing of data and technologies is
heavily restricted. This often leads to a lack of trust among
stakeholders. Third, businesses and academic institutions often
have diverging objectives in collaboration. Companies are
generally driven by commercialisation and rapid application,
whereas academics aim to explore long-term ethical and
theoretical questions. These differing priorities limit resource
allocation and reduce the efficiency of joint efforts. Finally,
the globalisation of AI development exacerbates challenges, as
cultural, economic, and political differences further complicate
cooperation. For instance, some regions emphasise stricter
privacy protections, while others prioritise freedom in tech-
nological innovation. Together, these factors make the multi-
stakeholder collaboration required for FAI highly complex
when the AGI era lands.
B. Suggestions
Building on these challenges, we propose several potential
suggestions to address the obstacles of FAI.
1) Establishing a Unified Definition Framework: The lack
of a unified definition for FAI remains a significant obstacle
to both theoretical exploration and practical application. As
discussed in Section III, much of the criticism directed towards
FAI is not against its core ideas (e. g., value alignment and
deontology) but stems from concerns over its ambiguous scope
and perceived impracticality due to its evolving nature. To
address this, we propose that international academic institu-
tions lead efforts to convene ethicists, policymakers, and AI
researchers to develop a modular framework. This framework
should clearly define the core principles and boundaries of
FAI. Additionally, instead of dismissing FAI as unachievable,
it is important to address these concerns through incremental
progress. By first agreeing on a theoretical foundation and then
considering practical implementation strategies, the ideal of
FAI can be approached systematically rather than prematurely
dismissed.
2) Consolidating Fragmented Knowledge Systems:
The
lack of consistency in terminology and research directions has
led to the fragmentation of FAI-related knowledge, limiting its
ability to achieve large-scale impact. To address this, we pro-
pose the creation of an open-access knowledge-sharing plat-
form. Such a platform, akin to an ‘FAI Wiki’ could centralise
academic papers, technological advancements, and industry

--- Page 12 ---

12
practices in one accessible location. By incorporating features
such as multilingual translation and systematic categorisation,
this platform would facilitate collaboration among researchers
and foster knowledge accumulation. It would provide a solid
foundation for advancing FAI research and ensuring its broader
development.
3) Developing a Cross-Cultural Ethical Framework: The
concept of ‘friendliness’ varies across cultures, reflecting di-
verse moral values and social priorities. To address this com-
plexity, we propose a multi-layered ethical decision-making
system that combines global core principles, such as fairness
and privacy, with dynamic adaptability to regional ethical
requirements. For instance, an AI system could prioritise
individual autonomy in societies where personal freedom is
emphasised while focusing on collective welfare in cultures
that value community-oriented decision-making. By tailoring
ethical decisions to the specific moral priorities of each region,
while maintaining consistency with overarching standards,
such a framework allows AI systems to align more effectively
with human values.
4) Accelerating Breakthroughs in Technical Capabilities:
Many ANI systems face limitations in areas such as nuanced
expression, long-memory storage, and adaptive decision-
making. These gaps highlight the need for targeted advance-
ments to bridge the transition from ANI to AGI and ensure
alignment with FAI principles. To address these challenges,
research efforts should focus on enhancing AI’s ability to
process and utilise contextual information over extended pe-
riods, enabling systems to handle complex and dynamic en-
vironments more effectively. For example, enhancing memory
architectures can improve long-term context retention, while
refining natural language models can enable AI to better
understand and respond to cultural and emotional nuances,
fostering more meaningful interactions.
However, while pursuing these innovations, it is essential
to balance technical advancements with continuous evalua-
tion of their broader implications [117]. Focusing solely on
performance risks overlooking other aspects such as ethical
considerations and alignment with human values. Developers
should integrate regular assessments of how new technologies
impact societal norms and ethical frameworks, ensuring that
progress in capabilities does not come at the expense of
responsible and aligned AI development.
5) Defining potential subfields for FAI: To address the
ambiguity over which AI subfields belong within the FAI
framework, we propose identifying and categorising technolo-
gies relevant to FAI. In our discussion above, XAI, privacy,
fairness and AC are promising candidates, as they provide
foundational tools for transparency, trust, and responsiveness
to human needs. While these fields alone cannot fully encom-
pass the scope of FAI, they offer significant contributions to
its framework. Additionally, other subfields that have not been
explicitly discussed here may also play a important role and
should be considered in future explorations. We recommend
that academic bodies or professional associations take the
lead in defining and formalising the scope of FAI-related
technologies. By systematically identifying and including such
technologies, the field can establish a clearer trajectory for
integrating ethical principles into technological development
and ensure a more unified approach toward FAI.
6) Promoting Multi-Stakeholder Collaboration: To address
the complexities of multi-stakeholder collaboration in FAI
conception, establishing structured mechanisms is important to
reconcile diverse priorities across disciplines, industries, and
nations. An international coordination body, potentially led
by organisations such as the United Nations, could provide
a platform to harmonise differing interests, including govern-
mental emphasis on safety, corporate focus on commercial-
isation, and academic dedication to ethical and theoretical
considerations. By developing clear cooperation guidelines,
standardising resource-sharing frameworks, and fostering mu-
tual trust through transparent practices, such an initiative could
effectively bridge these divides.
7) Enhancing Public Trust and Awareness: The ultimate
goal of FAI is to ensure mutual trust and respect between
humans and AI. Gaining public support and confidence in
AI systems is essential for achieving this aim. Promoting AI
requires transparent communication about its objectives and
benefits. Educational initiatives, such as interactive exhibits or
accessible online courses, can help the public understand and
appreciate the technology. Additionally, involving the public
in discussions about FAI’s ethical principles and potential
applications can create a sense of inclusion, fostering greater
trust and collective support for its development.
VI. CONCLUSION
In this paper, we have conducted a comprehensive review
of FAI, primarily from an ethical perspective. We have sum-
marised public perspectives both supporting and opposing the
development of FAI, alongside a discussion of its formal
definition, which we have presented in a clear and accessible
format. Additionally, we explored relevant FAI applications,
focusing on XAI, privacy, and AC. Furthermore, we outlined
the challenges associated with current technological advance-
ments and discussed potential future directions for the field.
In conclusion, we advocate for the continued development of
FAI and emphasise its value, expressing our strong support for
its advancement.
ACKNOWLEDGMENT
REFERENCES
[1] Y. N. Harari, Sapiens: A brief history of humankind.
Random House,
2014.
[2] A. A. Abonamah, M. U. Tariq, and S. Shilbayeh, “On the commodi-
tization of artificial intelligence,” Frontiers in psychology, vol. 12, p.
696346, 2021.
[3] M. Lapan, Deep Reinforcement Learning Hands-On: Apply modern
RL methods, with deep Q-networks, value iteration, policy gradients,
TRPO, AlphaGo Zero and more.
Packt Publishing Ltd, 2018.
[4] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi,
C. Wang, Y. Wang et al., “A survey on evaluation of large language
models,” ACM Transactions on Intelligent Systems and Technology,
vol. 15, no. 3, pp. 1–45, 2024.
[5] Z. J. Ye and B. Schuller, “Trading through earnings seasons using
self-supervised contrastive representation learning,” arXiv preprint
arXiv:2409.17392, 2024.
[6] J. Han, Z. Zhang, C. Mascolo, E. Andr´e, J. Tao, Z. Zhao, and B. W.
Schuller, “Deep learning for mobile mental health: Challenges and
recent advances,” IEEE Signal Processing Magazine, vol. 38, no. 6,
pp. 96–105, 2021.

--- Page 13 ---

13
[7] Q. Sun, A. Akman, X. Jing, M. Milling, and B. W. Schuller, “Audio-
based kinship verification using age domain conversion,” arXiv preprint
arXiv:2410.11120, 2024.
[8] J. H. Korteling, G. C. van de Boer-Visschedijk, R. A. Blankendaal,
R. C. Boonekamp, and A. R. Eikelboom, “Human-versus artificial
intelligence,” Frontiers in artificial intelligence, vol. 4, p. 622364, 2021.
[9] S. Iqbal, “The intelligence spectrum: Unraveling the path from ani to
asi,” Journal of Computing & Biomedical Informatics, vol. 7, no. 02,
2024.
[10] E. Yudkowsky, “Creating friendly ai 1.0: The analysis and design of
benevolent goal architectures,” The Singularity Institute, San Francisco,
USA, 2001.
[11] T. Feng, C. Jin, J. Liu, K. Zhu, H. Tu, Z. Cheng, G. Lin, and J. You,
“How far are we from agi,” arXiv preprint arXiv:2405.10313, 2024.
[12] M. Fahad, T. Basri, M. A. Hamza, S. Faisal, A. Akbar, U. Haider, and
S. E. Hajjami, “The benefits and risks of artificial general intelligence
(agi),” in Artificial General Intelligence (AGI) Security: Smart Appli-
cations and Sustainable Technologies.
Springer, 2024, pp. 27–52.
[13] P. Eckersley, “Impossibility and uncertainty theorems in ai value
alignment (or why your agi should not have a utility function),” arXiv
preprint arXiv:1901.00064, 2018.
[14] W. D’Alessandro, “Deontology and safe artificial intelligence,” Philo-
sophical Studies, pp. 1–24, 2024.
[15] A. Stoel, “The meme of altruism and degrees of personhood,” The
Transhumanism Handbook, pp. 623–629, 2019.
[16] R. J. M. Boyles and J. J. Joaquin, “Why friendly ais won’t be
that friendly: a friendly reply to muehlhauser and bostrom,” AI &
Society, vol. 35, no. 2, pp. 505–507, 2020. [Online]. Available:
https://link.springer.com/article/10.1007/s00146-019-00903-0
[17] R. J. M. Boyles, “Problems with ’friendly ai’,” Ethics and Information
Technology, vol. 23, no. 2, pp. 187–195, 2021. [Online]. Available:
https://link.springer.com/article/10.1007/s10676-021-09595-x
[18] R. Sparrow, “Friendly ai will still be our master. or, why we
should not want to be the pets of super-intelligent computers,”
AI & Society, vol. 39, no. 1, pp. 1–6, 2024. [Online]. Available:
https://link.springer.com/article/10.1007/s00146-023-01698-x
[19] A. Akman and B. W. Schuller, “Audio explainable artificial intelli-
gence: A review,” Intelligent Computing, vol. 2, p. 0074, 2024.
[20] R. Gupta, S. Tanwar, F. Al-Turjman, P. Italiya, A. Nauman, and S. W.
Kim, “Smart contract privacy protection using ai in cyber-physical
systems: tools, techniques and challenges,” IEEE access, vol. 8, pp.
24 746–24 772, 2020.
[21] E. U. Soykan, L. Karacay, F. Karakoc, and E. Tomur, “A survey and
guideline on privacy enhancing technologies for collaborative machine
learning,” IEEE Access, vol. 10, pp. 97 495–97 519, 2022.
[22] A. Triantafyllopoulos, M. Milling, K. Drossos, and B. W. Schuller,
“Fairness and underspecification in acoustic scene classification: The
case for disaggregated evaluations,” arXiv preprint arXiv:2110.01506,
2021.
[23] B. Schuller, A. Mallol-Ragolta, A. P. Almansa, I. Tsangko, M. M.
Amin, A. Semertzidou, L. Christ, and S. Amiriparian, “Affective
computing has changed: The foundation model disruption,” 2024.
[Online]. Available: https://arxiv.org/abs/2409.08907
[24] B. Fr¨oding and M. Peterson, “Friendly ai,” Ethics and Information
Technology, vol. 23, pp. 207–214, 2021.
[25] I. Asimov, I, Robot. New York, NY: Gnome Press, 1950, first appeared
in the short story ”Runaround,” published in 1942.
[26] D. Jordana, “The ethics of ai and robotics: Principles, tools, and
issues,” Ethics and Information Technology, vol. 23, pp. 29–41,
2021. [Online]. Available: https://link.springer.com/article/10.1007/
s10676-020-09556-w
[27] S. L. Anderson, “Asimov’s “three laws of robotics” and machine
metaethics,”
AI
&
Society,
vol.
22,
no.
4,
pp.
477–493,
2008. [Online]. Available: https://link.springer.com/article/10.1007/
s00146-007-0094-5
[28] R. E. Ashcroft, “The common good and the egalitarian research
imperative,” in The Oxford Handbook of Research Ethics, A. S.
Iltis and D. MacKay, Eds.
Oxford University Press, 2023, ch. 4,
pp. 69–88. [Online]. Available: https://academic.oup.com/book/57593/
chapter-abstract/469209964?redirectedFrom=fulltext
[29] O.
Li,
“Problems
with
“friendly
ai”,”
Ethics
and
Information
Technology, vol. 23, no. 3, pp. 543–550, 2021. [Online]. Available:
https://link.springer.com/article/10.1007/s10676-021-09595-x
[30] B. Mittelstadt, “Principles alone cannot guarantee ethical ai,” Nature
Machine Intelligence, vol. 3, pp. 869–872, 2021. [Online]. Available:
https://link.springer.com/article/10.1007/s43681-021-00051-6
[31] E. Yudkowsky et al., “Artificial intelligence as a positive and negative
factor in global risk,” Global catastrophic risks, vol. 1, no. 303, p. 184,
2008.
[32] S. Ghose and collaborators, “The case for animal-friendly ai,” arXiv
preprint, 2024. [Online]. Available: https://arxiv.org/abs/2403.01199
[33] P. Singer and B. Tse, “Ai ethics: The case for including animals,”
Ethics and Information Technology, vol. 24, 2022. [Online]. Available:
https://link.springer.com/article/10.1007/s43681-022-00187-z
[34] E. Yudkowsky, “Coherent extrapolated volition,” Singularity Institute
for Artificial Intelligence, 2004.
[35] N. Soares, B. Fallenstein, S. Armstrong, and E. Yudkowsky, “Corrigi-
bility,” in Workshops at the twenty-ninth AAAI conference on artificial
intelligence, 2015.
[36] I. Gabriel, “Artificial intelligence, values, and alignment,” Minds and
machines, vol. 30, no. 3, pp. 411–437, 2020.
[37] S. Russell, D. Dewey, and M. Tegmark, “Research priorities for robust
and beneficial artificial intelligence,” AI magazine, vol. 36, no. 4, pp.
105–114, 2015.
[38] S. Russell, Human compatible: AI and the problem of control. Penguin
Uk, 2019.
[39] M. Peterson, “The value alignment problem: a geometric approach,”
Ethics and Information Technology, vol. 21, pp. 19–28, 2019.
[40] N. Bostrom, “Hail mary, value porosity, and utility diversification,”
2014.
[41] D. Misselbrook, “Duty, kant, and deontology,” British Journal of
General Practice, vol. 63, no. 609, pp. 211–211, 2013.
[42] C. Mougan and J. Brand, “Kantian deontology meets ai align-
ment: Towards morally robust fairness metrics,” arXiv preprint
arXiv:2311.05227, 2023.
[43] J. N. Hooker and T. W. N. Kim, “Toward non-intuition-based machine
and artificial intelligence ethics: A deontological approach based on
modal logic,” in Proceedings of the 2018 AAAI/ACM Conference
on AI, Ethics, and Society, ser. AIES ’18.
New York, NY, USA:
Association for Computing Machinery, 2018, p. 130–136. [Online].
Available: https://doi.org/10.1145/3278721.3278753
[44] R. Kraut, “Altruism,” in The Stanford Encyclopedia of Philosophy,
Fall 2020 ed., E. N. Zalta, Ed.
Metaphysics Research Lab, Stanford
University, 2020.
[45] T. Maillart, L. Gomez, M. Sharada, D. Chakraborty, and S. Nana-
vati, “Altruistic collective intelligence for the betterment of artificial
intelligence,” in The Routledge Handbook of Artificial Intelligence and
Philanthropy.
Routledge, 2024, pp. 344–360.
[46] W. MacAskill, “The definition of effective altruism,” Effective altruism:
Philosophical issues, vol. 2016, no. 7, p. 10, 2019.
[47] G. Restall and G. Russell, “Barriers to implication,” in A Companion
to Philosophical Logic, D. Jacquette, Ed.
Wiley-Blackwell, 2010, pp.
243–257. [Online]. Available: https://doi.org/10.1002/9781444310795.
ch13
[48] N. Bostrom and E. Yudkowsky, “The ethics of artificial intelligence,”
in Artificial intelligence safety and security.
Chapman and Hall/CRC,
2018, pp. 57–69.
[49] E. Bird, J. Fox-Skelly, N. Jenner, R. Larbey, E. Weitkamp, and
A. Winfield, “The ethics of artificial intelligence: Issues and initiatives,”
European Parliamentary Research Service, Study PE 634.452, 2020.
[Online]. Available: https://www.europarl.europa.eu/RegData/etudes/
STUD/2020/634452/EPRS STU(2020)634452 EN.pdf
[50] F. Kroon, “A utilitarian paradox,” Analysis, vol. 41, no. 2, pp. 107–112,
1981. [Online]. Available: https://philpapers.org/rec/KROAUP
[51] A. van Wynsberghe, “Social robots and the risks to reciprocity,” AI
& Society, vol. 37, no. 2, pp. 479–485, 2022. [Online]. Available:
https://link.springer.com/article/10.1007/s00146-021-01207-y
[52] I. Kant, Groundwork of the Metaphysics of Morals. New York: Harper
& Row, 1785, translated by H. J. Paton in 1948, original publication
1785.
[53] N. Bostrom, Superintelligence: Paths, Dangers, Strategies.
Oxford:
Oxford University Press, 2014.
[54] M. Tegmark, “Friendly artificial intelligence: the physics challenge,”
2014. [Online]. Available: https://arxiv.org/abs/1409.0813
[55] N. A. Smuha, “The eu approach to ethics guidelines for trustworthy
artificial intelligence,” Computer Law Review International, vol. 20,
no. 4, pp. 97–106, 2019.
[56] V. Dignum, Responsible artificial intelligence: how to develop and use
AI in a responsible way.
Springer, 2019, vol. 2156.
[57] B. Mittelstadt, “Principles alone cannot guarantee ethical ai,” Nature
machine intelligence, vol. 1, no. 11, pp. 501–507, 2019.

--- Page 14 ---

14
[58] D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman,
and D. Man´e, “Concrete problems in ai safety,” arXiv preprint
arXiv:1606.06565, 2016.
[59] D. Gunning and D. Aha, “Darpa’s explainable artificial intelligence
(xai) program,” AI magazine, vol. 40, no. 2, pp. 44–58, 2019.
[60] Q. Sun, A. Akman, and B. W. Schuller, “Explainable artificial
intelligence for medical applications: A review,” 2024. [Online].
Available: https://arxiv.org/abs/2412.01829
[61] M. T. Ribeiro, S. Singh, and C. Guestrin, “” why should i trust you?”
explaining the predictions of any classifier,” in Proceedings of the 22nd
ACM SIGKDD international conference on knowledge discovery and
data mining, 2016, pp. 1135–1144.
[62] E. Lee, D. Braines, M. Stiffler, A. Hudler, and D. Harborne, “Develop-
ing the sensitivity of lime for better machine learning explanation,”
in Artificial Intelligence and Machine Learning for Multi-Domain
Operations Applications, vol. 11006.
SPIE, 2019, pp. 349–356.
[63] D. Fryer, I. Str¨umke, and H. Nguyen, “Shapley values for feature
selection: The good, the bad, and the axioms,” Ieee Access, vol. 9,
pp. 144 352–144 360, 2021.
[64] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and
D. Batra, “Grad-cam: Visual explanations from deep networks via
gradient-based localization,” in Proceedings of the IEEE international
conference on computer vision, 2017, pp. 618–626.
[65] S. Bach, A. Binder, G. Montavon, F. Klauschen, K.-R. M¨uller, and
W. Samek, “On pixel-wise explanations for non-linear classifier deci-
sions by layer-wise relevance propagation,” PloS one, vol. 10, no. 7,
p. e0130140, 2015.
[66] R. Achtibat, M. Dreyer, I. Eisenbraun, S. Bosse, T. Wiegand, W. Samek,
and S. Lapuschkin, “From” where” to” what”: Towards human-
understandable explanations through concept relevance propagation,”
arXiv preprint arXiv:2206.03208, 2022.
[67] R. Xu, N. Baracaldo, and J. Joshi, “Privacy-preserving machine
learning:
Methods,
challenges
and
directions,”
2021.
[Online].
Available: https://arxiv.org/abs/2108.04417
[68] E. Frimpong, K. Nguyen, M. Budzys, T. Khan, and A. Michalas,
“Guardml: Efficient privacy-preserving machine learning services
through hybrid homomorphic encryption,” 2024. [Online]. Available:
https://arxiv.org/abs/2401.14840
[69] A. Banse, J. Kreischer, and X. O. i J¨urgens, “Federated learning with
differential privacy,” 2024. [Online]. Available: https://arxiv.org/abs/
2402.02230
[70] M. T. Hosain, M. R. Abir, M. Y. Rahat, M. F. Mridha, and S. H. Mukta,
“Privacy preserving machine learning with federated personalized
learning in artificially generated environment,” IEEE Open Journal of
the Computer Society, vol. 5, pp. 694–704, 2024.
[71] Z. Ji, Z. C. Lipton, and C. Elkan, “Differential privacy and
machine learning: a survey and review,” 2014. [Online]. Available:
https://arxiv.org/abs/1412.7584
[72] M. K. Yogi and A. Chakravarthy, “A novel user centric privacy mech-
anism in cyber physical system,” Computers & Security, p. 104163,
2024.
[73] N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman, and A. Galstyan,
“A survey on bias and fairness in machine learning,” ACM computing
surveys (CSUR), vol. 54, no. 6, pp. 1–35, 2021.
[74] A. Triantafyllopoulos and B. Schuller, “Enrolment-based personalisa-
tion for improving individual-level fairness in speech emotion recog-
nition,” arXiv preprint arXiv:2406.06665, 2024.
[75] D. Kim, S. Park, S. Hwang, M. Ki, S. Jeon, and H. Byun, “Resampling
strategy for mitigating unfairness in face attribute classification,” in
2020 International Conference on Information and Communication
Technology Convergence (ICTC).
IEEE, 2020, pp. 399–402.
[76] N.-T. Tran, V.-H. Tran, N.-B. Nguyen, T.-K. Nguyen, and N.-M.
Cheung, “On data augmentation for gan training,” IEEE Transactions
on Image Processing, vol. 30, pp. 1882–1897, 2021.
[77] Z. Tang and K. Zhang, “Attainability and optimality: The equalized
odds fairness revisited,” in Conference on Causal Learning and Rea-
soning.
PMLR, 2022, pp. 754–786.
[78] S. Tan, Y. Shen, and B. Zhou, “Improving the fairness of deep gen-
erative models without retraining,” arXiv preprint arXiv:2012.04842,
2020.
[79] C. Dwork, M. Hardt, T. Pitassi, O. Reingold, and R. Zemel, “Fairness
through awareness,” in Proceedings of the 3rd innovations in theoretical
computer science conference, 2012, pp. 214–226.
[80] X. Li, P. Wu, and J. Su, “Accurate fairness: Improving individual fair-
ness without trading accuracy,” in Proceedings of the AAAI Conference
on Artificial Intelligence, vol. 37, no. 12, 2023, pp. 14 312–14 320.
[81] S. Pfohl, Y. Xu, A. Foryciarz, N. Ignatiadis, J. Genkins, and N. Shah,
“Net benefit, calibration, threshold selection, and training objectives for
algorithmic fairness in healthcare,” in Proceedings of the 2022 ACM
Conference on Fairness, Accountability, and Transparency, 2022, pp.
1039–1052.
[82] R. W. Picard, Affective Computing. Cambridge, MA: MIT Press, 1997.
[83] P. Ekman and W. V. Friesen, “Felt, false, and miserable smiles,” Journal
of Nonverbal Behavior, vol. 6, pp. 238–252, 1982.
[84] ——, Facial Action Coding System: A Technique for the Measurement
of Facial Movement.
Palo Alto, CA: Consulting Psychologists Press,
1978.
[85] B. Schuller, G. Rigoll, and M. Lang, “Hidden markov model-based
speech emotion recognition,” in 2003 IEEE International Confer-
ence on Acoustics, Speech, and Signal Processing, 2003. Proceed-
ings.(ICASSP’03)., vol. 2.
Ieee, 2003, pp. II–1.
[86] S. Hengameh, S. Sadjadi, and A. Zadeh, “Biofeedback systems: Ap-
plications in autonomic control for therapeutic settings,” Journal of
Biofeedback and Relaxation Techniques, vol. 45, pp. 156–168, 2015.
[87] Y. Wang, W. Song, W. Tao, A. Liotta, D. Yang, X. Li, S. Gao, Y. Sun,
W. Ge, W. Zhang, and W. Zhang, “A systematic review on affective
computing: Emotion models, databases, and recent advances,” 2022.
[Online]. Available: https://arxiv.org/abs/2203.06935
[88] V. S. Bakkialakshmi and T. Sudalaimuthu, “A survey on affective
computing for psychological emotion recognition,” in 2021 5th In-
ternational Conference on Electrical, Electronics, Communication,
Computer Technologies and Optimization Techniques (ICEECCOT),
2021, pp. 480–486.
[89] D. M. Schuller and B. W. Schuller, “A review on five recent and near-
future developments in computational processing of emotion in the
human voice,” Emotion Review, vol. 13, no. 1, pp. 44–50, 2021.
[90] Y. Wang et al., “Affective computing and emotion-sensing technology
for emotion recognition,” in Applications of Artificial Intelligence in
Additive Manufacturing. Springer, 2021, pp. 281–299. [Online]. Avail-
able: https://link.springer.com/chapter/10.1007/978-3-030-70111-6 16
[91] B. Schuller, M. Lang, and G. Rigoll, “Multimodal emotion recognition
in audiovisual communication,” in Proceedings. IEEE international
conference on multimedia and expo, vol. 1. IEEE, 2002, pp. 745–748.
[92] T. Shi and S.-L. Huang, “Multiemo: An attention-based correlation-
aware multimodal fusion framework for emotion recognition in conver-
sations,” in Proceedings of the 61st Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), 2023, pp.
14 752–14 766.
[93] J. Wu, J. Wu, Y. Zheng, P. Zhan, M. Han, G. Zuo, and L. Yang, “Mlgat:
Multi-layer graph attention networks for multimodal emotion recogni-
tion in conversations,” Journal of Intelligent Information Systems, pp.
1–17, 2024.
[94] B. Schuller, “Multimodal user state and trait recognition: An overview,”
The Handbook of Multimodal-Multisensor Interfaces: Signal Process-
ing, Architectures, and Detection of Emotion and Cognition-Volume 2,
pp. 129–165, 2018.
[95] R.
Zatarain
Cabada
et
al.,
Multimodal
Affective
Computing:
Technologies and Applications in Learning Environments.
Cham,
Switzerland: Springer, 2023. [Online]. Available: https://link.springer.
com/book/10.1007/978-3-031-32542-7
[96] Y. Liu, K. Wang, L. Wei, J. Chen, Y. Zhan, D. Tao, and Z. Chen,
“Affective computing for healthcare: Recent trends, applications, chal-
lenges, and beyond,” arXiv preprint arXiv:2402.13589, 2024.
[97] L. Shu, J. Xie, M. Yang, Z. Li, Z. Li, D. Liao, X. Xu, and X. Yang, “A
review of emotion recognition using physiological signals,” Sensors,
vol. 18, no. 7, p. 2074, 2018.
[98] M. Dhuheir, A. Albaseer, E. Baccour, A. Erbad, M. Abdallah, and
M. Hamdi, “Emotion recognition for healthcare surveillance systems
using neural networks: A survey,” in 2021 International Wireless
Communications and Mobile Computing (IWCMC).
IEEE, 2021, pp.
681–687.
[99] A. Mallol-Ragolta, S. Liu, N. Cummins, and B. Schuller, “A curriculum
learning approach for pain intensity recognition from facial expres-
sions,” in 2020 15th IEEE international conference on automatic face
and gesture recognition (FG 2020).
IEEE, 2020, pp. 829–833.
[100] D. Yang, A. Alsadoon, P. C. Prasad, A. K. Singh, and A. Elchouemi,
“An emotion recognition model based on facial recognition in virtual
learning environment,” Procedia Computer Science, vol. 125, pp. 2–10,
2018.
[101] I. Lasri, A. R. Solh, and M. El Belkacemi, “Facial emotion recognition
of students using convolutional neural network,” in 2019 third inter-
national conference on intelligent computing in data sciences (ICDS).
IEEE, 2019, pp. 1–6.

--- Page 15 ---

15
[102] M. L. Barron-Estrada, R. Zatarain-Cabada, and R. O. Bustillos, “Emo-
tion recognition for education using sentiment analysis.” Res. Comput.
Sci., vol. 148, no. 5, pp. 71–80, 2019.
[103] M. Schr¨oder, “Emotional speech synthesis: A review,” in Seventh
European Conference on Speech Communication and Technology,
2001.
[104] S. Yu, A. Androsov, H. Yan, and Y. Chen, “Bridging computer
and education sciences: a systematic review of automated emotion
recognition in online learning environments,” Computers & Education,
p. 105111, 2024.
[105] D. de Queiroz Cavalcanti, F. Melo, T. Silva, M. Falc˜ao, M. Caval-
canti, and V. Becker, “Research on brain-computer interfaces in the
entertainment field,” in International Conference on Human-Computer
Interaction.
Springer, 2023, pp. 404–415.
[106] P. Huang, “Decoding emotions: Intelligent visual perception for movie
image classification using sustainable ai in entertainment computing,”
Entertainment Computing, vol. 50, p. 100696, 2024.
[107] S. Li, “Application of entertainment e-learning mode based on genetic
algorithm and facial emotion recognition in environmental art and
design courses,” Entertainment Computing, vol. 52, p. 100798, 2025.
[108] M. Spezialetti, G. Placidi, and S. Rossi, “Emotion recognition for
human-robot interaction: Recent advances and future perspectives,”
Frontiers in Robotics and AI, vol. 7, p. 532279, 2020.
[109] R. Stock-Homburg, “Survey of emotions in human–robot interactions:
Perspectives from robotic psychology on 20 years of research,” Inter-
national Journal of Social Robotics, vol. 14, no. 2, pp. 389–411, 2022.
[110] M. Leo, M. Del Coco, P. Carcagni, C. Distante, M. Bernava, G. Pioggia,
and G. Palestra, “Automatic emotion recognition in robot-children
interaction for asd treatment,” in Proceedings of the IEEE International
Conference on Computer Vision Workshops, 2015, pp. 145–153.
[111] L. Zhang, M. Jiang, D. Farid, and M. A. Hossain, “Intelligent facial
emotion recognition and semantic-based topic detection for a humanoid
robot,” Expert Systems with Applications, vol. 40, no. 13, pp. 5160–
5168, 2013.
[112] C. Breazeal, “Emotion and sociable humanoid robots,” International
journal of human-computer studies, vol. 59, no. 1-2, pp. 119–155,
2003.
[113] B. Schuller, S. Steidl, A. Batliner, A. Vinciarelli, K. Scherer,
F. Ringeval, M. Chetouani, F. Weninger, F. Eyben, E. Marchi et al.,
“The interspeech 2013 computational paralinguistics challenge: Social
signals, conflict, emotion, autism,” in Proceedings INTERSPEECH
2013, 14th Annual Conference of the International Speech Commu-
nication Association, Lyon, France, 2013.
[114] B. Schuller, A. Mallol-Ragolta, A. P. Almansa, I. Tsangko, M. M.
Amin, A. Semertzidou, L. Christ, and S. Amiriparian, “Affective
computing has changed: The foundation model disruption,” arXiv
preprint arXiv:2409.08907, 2024.
[115] M. Ghandi, M. Blaisdell, and M. Ismail, “Embodied empathy: Using
affective computing to incarnate human emotion and cognition in ar-
chitecture,” International Journal of Architectural Computing, vol. 19,
no. 4, pp. 532–552, 2021.
[116] S. Livingston and M. Risse, “The future impact of artificial intelligence
on humans and human rights,” Ethics & international affairs, vol. 33,
no. 2, pp. 141–158, 2019.
[117] T. Shen, R. Jin, Y. Huang, C. Liu, W. Dong, Z. Guo, X. Wu, Y. Liu,
and D. Xiong, “Large language model alignment: A survey,” arXiv
preprint arXiv:2309.15025, 2023.

```
