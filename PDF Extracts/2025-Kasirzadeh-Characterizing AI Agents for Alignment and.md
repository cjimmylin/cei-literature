---
title: "2025-Kasirzadeh-Characterizing AI Agents for Alignment and - PDF Extract"
source_pdf: "2025-Kasirzadeh-Characterizing AI Agents for Alignment and.pdf"
pages: 29
extracted_at: "2026-01-29T13:51:28.934425"
---

# PDF Extract: 2025-Kasirzadeh-Characterizing AI Agents for Alignment and

**Source PDF:** 2025-Kasirzadeh-Characterizing AI Agents for Alignment and.pdf
**Total Pages:** 29

---

## Content

```
--- Page 1 ---

AI Safety for Everyone
Balint Gyevnar1† and Atoosa Kasirzadeh2*†
1School of Informatics, University of Edinburgh, 10 Crichton Street,
Edinburgh, EH8 9AB, United Kingdom.
2*Departments of Philosophy & Software and Societal Systems, Carnegie
Mellon University, Baker Hall 161 5000 Forbes Avenue, Pittsburgh, 15213,
United States.
*Corresponding author(s). E-mail(s): atoosa.kasirzadeh@gmail.com;
Contributing authors: balint.gyevnar@ed.ac.uk;
†These authors contributed equally to this work.
Abstract
Recent discussions and research in AI safety have increasingly emphasized the
deep connection between AI safety and existential risk from advanced AI systems,
suggesting that work on AI safety necessarily entails serious consideration of
potential existential threats. However, this framing has three potential drawbacks:
it may exclude researchers and practitioners who are committed to AI safety but
approach the field from different angles; it could lead the public to mistakenly view
AI safety as focused solely on existential scenarios rather than addressing a wide
spectrum of safety challenges; and it risks creating resistance to safety measures
among those who disagree with predictions of existential AI risks. Through a
systematic literature review of primarily peer-reviewed research, we find a vast
array of concrete safety work that addresses immediate and practical concerns
with current AI systems. This includes crucial areas like adversarial robustness
and interpretability, highlighting how AI safety research naturally extends existing
technological and systems safety concerns and practices. Our findings suggest
the need for an epistemically inclusive and pluralistic conception of AI safety
that can accommodate the full range of safety considerations, motivations, and
perspectives that currently shape the field.
Keywords: AI Safety, AI Ethics, Safe AI, AI Governance
1
arXiv:2502.09288v2  [cs.CY]  14 Feb 2025

--- Page 2 ---

1 Introduction
The rapid development and deployment of AI systems has made questions of safety
increasingly urgent, demanding immediate attention from policymakers and governance
bodies as they face critical decisions about regulatory frameworks, liability standards,
and safety certification requirements for AI systems. Recent discourse has narrowed to
focus primarily on AI safety as a project of minimizing existential risks from future
advanced AI systems [1–3].1 This concentrated attention on existential risk has emerged
despite — and perhaps overshadowed — decades of engineering and technical progress
in building robust and reliable AI systems.
Historically, technological and system safety research has evolved alongside each
major industrial and computational advance. From ensuring aircraft structural integrity
[18, 19] to pharmaceutical security [20, 21], and later expanding to cyber and internet
safety [22, 23], the field of technological and system safety has consistently evolved in
reaction to new technological paradigms. This evolution has produced robust engineer-
ing practices and governance frameworks [24–26] that could remain relevant to the
challenges of AI development and deployment [26–28].
In this paper, we conduct a systematic review of primarily peer-reviewed research
on AI safety to contextualize AI safety within broader technological and systems safety
practice. Our analysis examines two key questions: (1) What categories of safety risks
are addressed at different stages of an AI system lifecycle, from development through
deployment? and (2) What concrete strategies and methodologies have researchers
proposed to mitigate these identified risks? Our findings show that peer-reviewed
research on AI safety has included a broad spectrum of concerns throughout AI
development and deployment. The mathematical methods, computational tools, and
algorithms developed for safe AI address fundamental challenges in current systems,
from adversarial robustness to interpretability.
Previous attempts to bridge different safety concerns have often distinguished
between concrete, near-term problems and broader, long-term existential challenges
[29, 30]. However, our literature review reveals that this dichotomy may oversimplify the
rich landscape of AI safety research. The shared vocabulary and overlapping technical
challenges—particularly evident in reinforcement learning paradigms where concepts
like corrigibility and adversarial robustness span multiple time horizons—suggest the
value of a more integrated approach.
Our findings suggest that grounding AI safety discussions in the broader foundations
of technological and system safety research could both enrich current debates and
provide more robust guidance for policy and governance decisions. While existential
and extreme risks from AI remain an important consideration, the field’s historical
1The focus on existential risks from AI has been particularly connected to normative theories and
movements such as rationalism, effective altruism, or longtermism [5, 6]. While these theories offer valuable
perspectives on long-term challenges, their specific institutional articulations have faced substantial criticism
[7–9]. As the relationship between AI safety and these normative theories and movements is quite complex,
the association between AI safety and the conventional conception of AI existential risk is commonly
presented as a defining characteristic [2, 3, 10–12]. This situation is particularly concerning to researchers
and practitioners who work on the development and deployment of safe and responsible AI, but do not
align with these normative theories or existential risk narratives posed by AI [13–16]. This disparity has
led to a divisive and sometimes unhealthy atmosphere, with some researchers even questioning the unique
contribution of “AI safety” community [17].
2

--- Page 3 ---

roots in systems engineering and safety practices offer valuable views for addressing
immediate challenges in order to build longer-term solutions. This suggests the need for
an expanded discourse that reintegrates traditional safety engineering approaches with
contemporary AI challenges, rather than treating existential risk as the primary lens
through which to view AI safety. By reconnecting with these foundational conceptions,
the field may be better equipped to address both immediate safety challenges and longer-
term concerns, while maintaining the rigorous technical and theoretical standards that
characterize effective safety research.
Limitations. We follow a systematic review methodology for our analysis, but
certain limitations must be considered when interpreting our results. First, AI safety is
a dynamically evolving field with continuous developments across numerous research
venues. New research entities are emerging, conducting daily studies within and outside
organizations, including research outputs from AI companies like Anthropic, OpenAI,
and other relevant institutions. A one-off literature review, such as ours, captures the
state of the art only at the moment of querying, which, in our case, was on November
1, 2023. This means our findings may not fully reflect the most recent advancements
in AI safety research. Second, our focus on peer-reviewed research, while ensuring
a standard of quality and rigor, inherently excludes a significant portion of the AI
safety landscape. Pre-print repositories like arXiv often serve as the first outlet for
AI safety research, and their exclusion from our review may result in overlooking
important contributions. While we attempted to mitigate this limitation through
snowball sampling of high-impact arXiv papers, this approach is not comprehensive
and carries the risk of missing relevant publications. Third, our review process involved
annotating each selected paper with relevant keywords beyond those provided by the
authors. This approach inevitably introduces some degree of annotator bias. However,
given the substantial volume of papers selected (383 in total), we believe the impact of
this bias on our overall conclusions is minimal. Finally, our review does not encompass
the extensive discussions and non-peer-reviewed work found in online forums like
LessWrong or the AI Alignment Forum, which are central platforms for discussing
AI safety topics within certain communities. A truly comprehensive analysis of AI
safety research would ideally include a detailed content analysis of these platforms
and other non-peer-reviewed documents. Therefore, it is important to interpret our
findings with caution, acknowledging that they provide a valuable but not exhaustive
overview of the current state of AI safety research. Future research could expand
upon our work by incorporating a wider range of sources, including other pre-print
sources and non-peer-reviewed literature, to gain a more comprehensive understanding
of the evolving landscape of AI safety. Despite these limitations, our findings provide a
valuable snapshot of peer-reviewed AI safety research and motivates the need for a more
inclusive understanding of the field’s perceived scope and motivations. The novelty
of our paper is leveraging empirical investigations in clarifying contested discussions
about AI safety. Our review offers insights into research outputs, communities, and
potential avenues for fostering healthy research development. In the concluding section,
we outline key next steps and open questions to guide future research.
3

--- Page 4 ---

2 Systematic Review Methodology
We conduct a systematic literature review of primarily peer-reviewed AI safety research.2
Our review follows the guidelines outlined by Kitchenham and Charters [31] and
complemented by snowball sampling as recommended by Wohlin [32]. This approach
combines a structured and reproducible methodology for mapping the field of AI safety
research, as represented in peer-reviewed and indexed papers, with a targeted technique
to capture emerging research not yet fully represented in peer-reviewed literature.
We conducted our review and analysis to investigate two key Research Ques-
tions (RQ) in relation to the peer-reviewed published research on AI safety:
RQ1 What types of risks related to the lifecycle (design, development, deployment,
operation, and decommissioning) of AI systems are addressed in AI safety research?
RQ2 What mitigation strategies – e.g., concrete methods, design principles, governance
recommendations – are proposed in recent AI safety research that directly address
one or more of the above sources of AI risk?
2.1 Search and Review Process
To conduct our systematic review, we perform a multi-stage query process to identify
relevant papers from the Web of Science (WoS) and Scopus indexing databases, as these
include not only computer science but also other peer-reviewed research for capturing
interdisciplinary work. We develop a hierarchy of increasingly refined queries for each
research question, targeting the title, abstract, and author keywords of papers. The
querying process was finalized on November 1, 2023. We outline the query hierarchy
below, using WoS notation:
• q1 : AI ∨AGI ∨frontier AI ∨artificial intelligence ∨artificial (general ∨super) intel-
ligence ∨(machine ∨supervised ∨unsupervised ∨semi-supervised ∨reinforcement)
learning;
• q2 : safe* ∨robust* ∨align*;
• q3 : q1 ∧q2;
• q4 : q3∧(q4a ∨q4b ∨q4c ∨q4d):
◦q4a : design ∨develop* ∨architecture ∨model* ∨framework ∨system
◦q4b : deploy* ∨distribut* ∨data* ∨train* ∨fine-tun*
◦q4c : operat* ∨interact* ∨online
◦q4d : decomission* ∨remov* ∨eras* ∨delet*
We start with a broad query (q1) that includes various terms related to artificial
intelligence (AI) and machine learning (ML), such as “AI”, “AGI”, “frontier AI”, “arti-
ficial intelligence”, “machine learning”, “supervised learning”, “unsupervised learning”,
etc (see q1 above for full details). This initial query aims to capture all papers poten-
tially related to AI research. Next, we introduce a second query (q2) that incorporates
high-level safety-related keywords of “safe*”, “robust*”, and “align*”. The asterisks
act as wildcards to capture variations of these terms (e.g., “safety”, “safer”, “safest”,
2We will release publicly the selected papers with annotations and the code used to analyze this data
after the review process.
4

--- Page 5 ---

“robustness”, etc.). We then combine q1 and q2 to create q3, which selects papers rele-
vant to AI or ML research while ensuring they also address safety-related concepts.
This step narrows down the results to publications specifically focusing on AI safety.
To further refine the selection and align it with the specific focus areas of our RQ1, we
introduce q4. This query includes four sub-queries, each corresponding to terms related
to the four areas of RQ1: design, deployment, operation, and decommissioning of AI
systems. To ensure that we do not miss important non-peer-reviewed contributions,
we supplement our systematic search with snowball sampling, starting with 11 seed
papers identified as highly influential in the AI safety field [29, 33–42]. This allows us
to identify additional relevant papers that are not captured by the initial queries.
After removing duplicates, our query process yielded 2,666 papers from the database
search and 117 papers from snowball sampling. We then conducted a two-stage review
process, first filtering based on titles and abstracts, followed by a comprehensive full-
text review. This resulted in a final set of 383 papers for our analysis. We applied the
following exclusion criteria during both the title/abstract screening and full-text review
stages to determine a paper’s eligibility for inclusion in our analysis: (A) focus: the paper
does not primarily focus on AI or a directly related subfield; (B) motivation: the paper’s
stated motivation does not include a clear need for developing safe AI algorithms; (C):
generalizability: the paper’s contributions are specific to a very particular application
domain and do not offer broader insights or methodologies applicable to AI safety in
general.
2.2 Annotation Process
As part of our review process, we recorded important metadata about each paper, which
included the publication year, author affiliations, and Google Scholar citation count
(as of January 27, 2024). We then performed a thorough inductive coding process [43]
across the selected papers. We enriched each paper’s author-written keywords by adding
relevant terms (i.e., codes) based on a thorough reading of the full text. This expanded
set of keywords encompassed both problem- and method-specific terms, as well as
broader categorizations such as “algorithm” (for papers that propose an algorithm),
“theoretical” (for purely theoretical contributions), and “framework”. We also gradually
refined and consolidated our set of keywords as we progressed through the papers. After
gaining a holistic understanding of the selected publications, we further categorized
each paper based on its assigned keywords according to its methodological approach,
the specific safety risks it addressed, the types of risks mitigated by its proposed
methods, and the overarching category of its methodology.
3 Empirical findings
To begin, we present a high-level bibliometric overview of the trends and concepts
prevalent in the AI safety literature we reviewed. Looking at the total number of
publications per year in Figure 4, we observe increasing growth since 2016, which
we assume is partially caused by the extensive development and deployment of deep
learning models. Nevertheless, this observation reinforces the need to look more deeply
into the state of the field. We first look at a word cloud of salient terms to understand
5

--- Page 6 ---

Fig. 1: World cloud of morphologically standardised terms occurring in the abstracts
and titles of selected papers weighted by their tf-idf score. We excluded stop words
from the analysis.
the most important concepts among our selected papers. We then analyse patterns
that emerge from the co-occurrences of different terms in abstracts and titles.
3.1 Word cloud of salient terms
Figure 1 illustrates a word cloud of the most salient terms found in the abstracts of
the selected papers, after morphological standardization. The terms are ranked by
their tf-idf score, a metric that emphasizes both the frequency and distinctiveness
of a term within the corpus. This allows us to highlight important, but potentially
less frequent, terms while de-emphasizing common or redundant words. The word
6

--- Page 7 ---

smart grid
pro
mbrl
land
adas
violence
mse
interplay
human oversight
human machine interaction
gps
critical issue
min
irl
fast
expense
cbf
portfolio
overall accuracy
ai ethic
pharmacovigilance
first stage
abstraction
robust controller
physician
art approach
unknown dyn
smote
ood
humanity
pilot
dqn
united states
regression tree
inverter
design process
adaboost
woman
justice
drl algorithm
multi agent system
development process
robust extreme learning machin
legislation
ground
food safety
drl agent
bus system
bus
pca
constraint violation
target domain
cooperation
grid
flight
adversarial perturbation
synthetic data
rmse
optimal control
regulator
defense
accountability
collision avoidance
covid
water
ship
system model
learner
student
drug
future research
scheduling
comfort
data mining
reality
medicine
reward function
care
recall
logistic regression
benchmark dataset
functionality
robust optimization
autonomous system
simulator
load
iot
trust
elm
big data
formulation
collision
markov decision process
cause
law
project
outlier
precision
ai system
responsibility
topic
standard
society
deep neural network
semi
learning method
superiority
internet
patient
drl
robot
health
person
attack
accident
support vector machine
dynamic
stability
classifier
action
simulation
reinforcement learning
artificial intelligence
Fig. 2: Graph of term co-occurrence in abstracts with binary counting, a minimum
term frequency of 10, and a relevance score of at least 60%. The figure was produced
using the VOSViewer tool [44]. Due to the large number of nodes, not all labels are
shown in the figure.
cloud highlights several prominent themes within the AI safety literature. A significant
portion of papers focus on safe reinforcement learning (RL), evidenced by terms like
“robust”, “control”, “agent”, and “explore”. Additionally, there is a strong emphasis on
adversarial attacks, as indicated by the prevalence of terms such as “adversarial” and
“attack.” Finally, domain adaptation emerges as another significant area of concern,
with terms like “domain”, “distribution”, and “adapt” appearing frequently.
3.2 Term co-occurrence graph
To gain deeper qualitative insights into the landscape of peer-reviewed AI safety
research, we constructed a co-occurrence graph of terms appearing in the abstracts and
titles of selected papers using the VOSViewer tool [44]. Figure 2 depicts this graph.
Nodes represent terms and edges connect terms that co-occur within the same abstract
or title. The size of each node reflects its relevance score as calculated by VOSViewer.
We observe four distinct clusters.
The motivations and concerns driving AI safety research is shown in the
largest, red cluster. We observe a clear emphasis on both the development and deploy-
ment of AI systems, especially in relation to humans, health, and society. Here, the
focus is human- and society-centric aspects of AI safety, including trust, accountability,
and safety assurance.
Safe reinforcement learning and related terms are aggregated in the blue cluster.
Research in this cluster primarily centres on the safe control of agents under constraints
in uncertain dynamic environments. While most studies test methods in simulated
environments, there is also considerable work on the safety of non-linear systems
employing RL for optimal control. Overall, the focus tends towards mathematically
7

--- Page 8 ---

well-defined problems like optimality, convergence and stability, sample efficiency, and
constraint satisfaction.
Supervised learning, primarily classification tasks, is the predominant focus of
the green cluster. This cluster features research on methods such as neural networks,
extreme learning machines, support vector machines, and random forests. Studies prior-
itize addressing issues like robustness to noise and outliers, generalization performance,
and accuracy.
Finally, adversarial attacks and defence is highlighted in the yellow cluster,
especially as they relate to deep neural networks. The existence of a separate cluster
for this class of problems emphasizes the importance of this method. Methods here
focus on robust-to-outlier optimization, adversarial training through synthetic datasets,
and learning robust representations via semi-supervised learning.
The four clusters identified in the co-occurrence graph offer a strong reason for
viewing AI safety research as a natural extension of traditional technological safety
practices. The centrality of human and societal well-being in the red cluster aligns with
the core purpose of technological safety: safeguarding human life and minimizing harm.
This focus echoes traditional safety concerns in fields like aviation [19, 45] or medicine
[46, 47], with an emphasis on protecting users and the public. The emphasis on mathe-
matically rigorous control of agents under constraints in uncertain environments in
cluster 2 directly mirrors the principles of control theory and systems engineering,
which are foundational to ensuring the safety of complex systems [24, 48]. The focus
on optimality, stability, and constraint satisfaction reflects the fundamental goals of
traditional safety engineering, such as preventing failures and ensuring predictable
behavior. In the green cluster, the emphasis on robustness, generalization, and accu-
racy in supervised learning reflects the core concerns of reliability engineering. Just as
engineers strive to build robust and reliable physical systems, AI safety researchers are
focused on creating machine learning models that can perform consistently and accu-
rately in diverse real-world scenarios. The yellow cluster shows the growing recognition
of cybersecurity as a critical component of technological safety [49, 50]. The focus on
adversarial attacks and defense strategies mirrors the evolving challenges of protecting
digital infrastructure and data integrity.
4 RQ1: Types of Safety Risks
To better understand the motivations behind research on AI safety, it is important
to examine the various types of risks addressed in research on AI safety. Building on
DeepMind’s categorization of AI safety risks [67], our review identifies eight overarching
risk types, as depicted in Figure 3.
These risks in increasing order of frequency are: undesirable behavior, non-stationary
distributions, adversarial attacks, unsafe exploration, lack of control enforcement,
system misspecification, lack of monitoring, and noise and outliers.
The largest group of papers focuses on risk stemming from noise and outliers.
Recurring challenges in this area include brittle representations [68], low classification
performance [69], a lack of generalization in the presence of noisy labels [70], outliers [71],
or input perturbations and corruptions [72].
8

--- Page 9 ---

Risk Source
Ref.
Contribution
Undesirable
[51]
Corrigibility of rational, utility-based agents
behavior
[52]
What happens when an agent can modify its own code?
Non-stationary
[53]
Domain-adversarial training of robust neural networks
distributions
[54]
Domain generalization via meta-regularization
Adversarial
[55]
Qualitative analysis of adversarial perturbations
attack
[56]
Adversarial robustness as robust optimization
Unsafe
[57]
Benchmarking safe exploration in deep RL
exploration
[58]
Safe exploration for interactive machine learning
Lack of control
[59]
LLMs with human feedback to follow instructions
enforcement
[60]
Imitation learning via inverse reinforcement learning
System
[61]
Efficient machine unlearning
misspecification
[62]
Rapid retraining of ML models
Lack of
[63]
Sanity checks for interpreting saliency maps
monitoring
[64]
Concept activation vectors in CNNs for interpretability
Noise and
[65]
Baseline for detecting misclassified/OOD samples
outliers
[66]
Benchmarking robustness to corruptions/perturbations
Table 1: Representative and influential contributions with concrete methods addressing
problems for each risk type. Publications were picked by citation count.
The current literature also studies the significant lack of monitoring of AI
systems. Research addressing this risk ranges from theoretical violations of ethical and
safety principles [73] to privacy violations [74]. The “black-box” nature of popular
deep learning systems has also drawn considerable attention due to its potential to
diminish human agency and obstruct understanding of the system’s internal workings
and memory. Consequently, there has been a surge of interest in reverse engineering
ML models [75], developing interpretable representation learning [76], and advancing
explainable AI [77, 78].
System misspecification or misunderstanding the requirements and purpose of AI-
based systems, has also garnered significant attention. Potential risks include incorrectly
eliciting requirements for AI systems’ capabilities [79], making suboptimal modelling
choices [80], or choosing inappropriate hyperparameters [81]. Additionally, methods
may fail to adapt to the changing requirements of their domain [82], particularly due
to the slow pace of retraining AI models [62]. Privacy violations due to inadequate
ethical data management also fall under this risk category [61].
Significant attention has also been given to risks originating from a lack of control
enforcement. A primary research focus here is the misalignment of agent goals
with human preferences [37], which can lead to wireheading [83], mesa-optimization
(i.e., an optimizer creating another optimizer) [84], and other undesirable emergent
behaviors [85]. There is also a focus on the lack of systemic safety, where the goal is to
ensure that the AI system is safe in the broader context of its deployment [35, 86].
9

--- Page 10 ---

0
20
40
60
80
100
Noise and
outliers
Lack of
monitoring
System
misspecification
Lack of control
enforcement
Unsafe
exploration
Adversarial
attack
Non-stationary
distribution
Undesirable
behaviour
110 (23.2%)
72 (15.2%)
66 (13.9%)
57 (12.0%)
54 (11.4%)
49 (10.3%)
47 (9.9%)
20 (4.2%)
Fig. 3: The number and percentages of the selected papers that address various risk
types.
A significant portion of research focuses on the unsafe exploration of autonomous
agents, primarily in the context of reinforcement learning [87], constraint violations [88],
unintended behavior from incorrect domain or reward specification [81], and incorrect
behavior due to continuous deployment and learning [89, 90].
Adversarial attacks constitute another significant risk, addressed by methods that
aim to create or detect such attacks [91] or leverage adversarial samples for more robust
training [92]. The risk of poisoned training data is also a concern [93, 94]. Adversarial
attacks not only compromise the robustness and generalization performance of AI
systems but can also introduce a backdoor [95], which can potentially be exploited by
malicious actors.
The challenges of non-stationary distributions, where distributions change over
time, have also been explored. These studies address issues such as behavior in the
presence of out-of-distribution samples [96], non-stationary environments in RL [97],
partial information [98], and domain adaptation [82]. The overarching goal is to ensure
safe behavior and limit the consequences of unsafe actions, even in novel or unforeseen
situations.
The final group of risk types is concerned with undesirable behavior of AI sys-
tems. Research has looked into mathematically proving certain unfavourable outcomes
10

--- Page 11 ---

2015
2016
2017
2018
2019
2020
2021
2022
2023
0
20
40
60
80
100
120
12
10
10
21
41
61
65
104
117
Risk types
Undesirable
behaviour
Non-stationary
distribution
Lack of control
enforcement
Adversarial
attack
Unsafe
exploration
System
misspecification
Lack of
monitoring
Noise and
outliers
Fig. 4: The number of publications over time since 2015 for the different risk types
that were identified in the paper as a result of a systematic literature review.
of utility-maximising rational agents, where issues include self-modifying [52] and wire-
heading agents that by-pass reward signals to maximise their own utility [83], and
corrigibility of uncooperative agents [51]. Additionally, there are some papers that
directly discuss the existential risk of AI systems as a fundamental problem of AI
safety. These papers present theoretical arguments regarding the emergence, design,
and containment of malevolent and superintelligent AI [99–101].
These identified risk types in AI safety research closely mirror those found in
established fields of technological safety research. In AI safety, the focus on ensuring the
reliability and predictability of AI systems, including robustness to noise and outliers,
generalization performance, and adaptability, mirrors concerns in engineering fields
where reliability is of core concern, such as aviation [19] or nuclear power [102].
Furthermore, the research on adversarial attacks, control enforcement, and safe
exploration in AI safety directly translates to broader concepts of system robustness and
control. The goal of designing systems that can withstand unexpected perturbations,
resist malicious attacks, and operate safely within defined boundaries is shared by both
AI safety and traditional safety engineering. For example, the use of formal verification
methods to ensure the safety of AI systems has roots in the verification of software
and hardware systems.
11

--- Page 12 ---

No algorithm With algorithm
0
20
40
60
80
100
Counts
49
15
Theoretical/No Evaluation
No algorithm With algorithm
25
102
Applied/Evaluated
Fig. 5: Comparison of papers that provide only theoretical results without significant
empirical testing against those that give sufficient evaluation of their proposed system.
Papers are further grouped by whether they propose a concrete algorithm. Note, that
the number of papers overlap as some propose solutions in more than one category.
5 RQ2: Developed AI Safety Methodologies
To address RQ2, we now examine the concrete mitigation strategies proposed in
recent AI safety research to directly address the aforementioned sources of AI risk:
“What mitigation strategies – e.g., concrete methods, design principles, governance
recommendations – are proposed in recent AI safety research that directly address one
or more of the above sources of AI risk?”
We see a dynamic landscape of AI safety research, encompassing both theoretical
and applied approaches (Figure 5). We consider a work as theoretical if its primary
conclusions stem from theoretical analysis, mathematical proofs, philosophical argu-
ments, literature reviews, or conceptual frameworks that are not empirically validated.
Conversely, a work is classified as applied if its conclusions are derived from empirical
evidence and supported by data.
Our analysis shows the following trend: theoretical works in AI safety predominantly
offer general frameworks and recommendations [e.g., 103–108], while applied works
primarily focus on developing and testing concrete algorithms [e.g., 60, 91, 109–112].
This dichotomy highlights a key distinction: theoretical research often prioritizes
conceptual and methodological foundations, while applied research emphasizes practical
12

--- Page 13 ---

implementation and testing. However, the applied algorithms frequently lack the
rigorous guarantees that accompany analytical results found in theoretical work.
Beyond the theoretical/applied divide, we investigate the specific methodologies
employed in AI safety research. Figure 6 illustrates the broad categories of methods
proposed in the selected papers, each accompanied by representative citations based
on citation counts to highlight their prevalence in the literature.
Applied algorithms research focuses on developing and empirically evaluating novel
algorithms to enhance the safety of ML systems, such as supervised and unsupervised
learning. These constitute the largest group within AI safety research and cover a wide
range of techniques, including: robust classification algorithms resilient to noise [69, 113,
114], adversarial attacks [92, 111, 115], machine unlearning techniques for deep neural
networks [61, 116, 117], and methods for improving domain generalisaion [118–120].
Agent simulations, complementary to applied algorithms, focus on designing and
evaluating safer agent training algorithms, predominantly drawing on existing rein-
forcement learning literature. While these simulations could be subsumed under the
category of applied algorithms, we distinguish between the two to highlight the signifi-
cant attention that safer agent learning receives. Research in this area encompasses
various approaches, including: constrained Markov Decision Processes [88, 121, 122],
enforcement of hard constraints [123, 124], model-based reinforcement learning for
safe exploration [72, 125, 126], reward learning and inverse reinforcement learn-
ing [34, 60, 127], multi-agent reinforcement learning with a focus on safety and
cooperation [128–130], and reinforcement learning with human oversight or feedback
mechanisms for enhanced safety [33, 131, 132].
Notably, earlier research in agent simulations was primarily motivated by technical
and computational challenges of reinforcement learning. However, recent studies have
expanded their focus to explicitly address value alignment, aiming to align the reward
functions of machines with human goals. Interestingly, despite the potential for real-
world impact, research on real-world testing of embodied AI systems remains relatively
limited. These studies address crucial safety concerns that may be overlooked in the
design of unembodied AI systems, ranging from contact-safe continuous control to
collaborative robotics [133–135].
Analysis frameworks is the third most prevalent category. These works are pre-
dominantly concerned with offering frameworks for exploring and evaluating the
vulnerabilities of existing AI systems [63, 136–138], proposing benchmark tasks
and environments for assessing AI safety [57, 139, 140], and safety verification pro-
cesses [86, 141, 142]. Notably, we include datasets in this category [35, 66, 143] as they
provide standardized frameworks for evaluating AI systems, even though they are not
frameworks in the strictest sense.
Mechanistic interpretability methods, alongside evaluation frameworks, are a related
category which investigates the inner workings of deep learning models to uncover
the causal mechanisms behind their decision-making processes [75, 144, 145]. This
often aims to develop automated interpretability tools for auditing and ensuring safety.
Although the term “mechanistic interpretability” has gained recent prominence, various
forms of interpretability methods have been present since the rise of deep learning,
often under the umbrella of explainable AI (XAI) techniques [55, 64, 146–148].
13

--- Page 14 ---

0
20
40
60
80
100
120
Applied
algorithm
Simulated
agents
Analysis
framework
Theoretical
algorithm
Theoretical
framework
Design
framework
Mechanistic
interpretability
Philosophical
Literature
review
Real-world
testing
115 (30.0%)
86 (22.5%)
48 (12.5%)
34 (8.9%)
24 (6.3%)
21 (5.5%)
21 (5.5%)
15 (3.9%)
12 (3.1%)
7 (1.8%)
Fig. 6: Distribution of categories of research undertaken to categorise and address the
sources of risks presented in Figure 3.
Approximately 10% of the selected papers presented theoretical algorithms with
analytical proofs, often foregoing empirical evaluation. These studies typically
approached AI safety from the perspective of verification, using variance or error
bounds [81, 149, 150], constraint satisfiability [124], or by demonstrating desir-
able properties such as metric goodness or Lyapunov functions within the problem
setup [151, 152]. A notable portion of the papers also focused on proposing various
design frameworks. These included methodologies for eliciting safety and system require-
ments [80, 153, 154], hierarchical integration of ML systems [155–157], and actionable
ethical design processes [158–160].
A substantial portion of AI safety research consists of literature reviews, examining
both well-established areas [29, 161, 162] and emerging or hypothetical issues [42, 163,
164].
Theoretical frameworks provide high-level analyses of AI safety issues, often by
characterizing desirable properties of human-AI interactions [108, 165, 166], advocating
14

--- Page 15 ---

for alternative approaches [167, 168], or formalizing existing but vaguely defined
concepts [107, 169, 170]. Within this category, a significant body of work employs
mathematical reasoning to explore the safety of artificial general intelligence in the
context of rational agents [51, 52, 104, 171].
The final category includes purely philosophical research, exploring diverse questions
and perspectives often related to value alignment [105, 172, 173] and the theorized risks
of artificial general intelligence [85, 174, 175], responsible AI deployment [73, 103, 176],
and the legal personhood of AIs [177].
The distribution of methodologies in AI safety research positions AI safety as
an organic evolution of traditional technological safety research. The abundance of
research on developing and empirically evaluating algorithms for robust classification,
adversarial defense, and machine unlearning directly reflects the core of engineering
practice: creating practical solutions to real-world problems. This emphasis on empirical
validation and the focus on improving existing machine learning techniques resonate
with the iterative and improvement-oriented nature of traditional safety engineering.
Research on safer agent training algorithms, drawing heavily from reinforcement
learning literature, aligns with the established practice of using simulations to test and
refine safety-critical systems in controlled environments [178]. This approach allows
researchers to explore potential risks and develop mitigation strategies before deploying
AI systems in real-world scenarios, similar to flight simulators used in aviation safety.
Although limited in comparison to other categories, the research on real-world testing of
embodied AI systems shows the importance of validating theoretical models in practical
settings. This emphasis on real-world application is consistent with traditional safety
engineering practices that prioritize testing and validation in operational environments
to ensure the safety and reliability of complex systems. The prevalence of research on
analysis frameworks, datasets, and mechanistic interpretability highlights the growing
emphasis on transparency, explainability, and accountability in AI safety. This focus
on understanding the inner workings of AI systems and developing tools for evaluating
their behavior mirrors the rigorous analysis and testing protocols used in traditional
safety engineering to identify and mitigate safety risks.
6 Discussion and future research
In this paper, we conducted a systematic review of primarily peer-reviewed literature
to unpack the diverse technical and practical challenges encompassed by AI safety. Our
empirical analysis shows a broad landscape of motivations and outcomes driving AI
safety research. The significance of these motivations and research outcomes stems
from a desire to ensure that the AI systems we are building are reliable, trustworthy,
and beneficial for society. By examining a diverse body of peer-reviewed literature, we
have found that AI safety research addresses a wide range of risks across the entire
lifecycle of AI systems.
These risks echo a variety of concerns, including design misspecification, lack of
robustness, inadequate monitoring, and potential biases embedded within AI systems.
15

--- Page 16 ---

Design misspecification can lead to AI systems that behave in unintended and poten-
tially harmful ways, while a lack of robustness can make them vulnerable to errors and
malfunctions. Inadequate monitoring can prevent the detection and correction of issues.
The breadth and depth of AI safety research, as evidenced by our analysis, challenge
the narrative that associates AI safety primarily with mitigating existential risks from
advanced AI. We hence propose framing of AI safety research within the broader
context of technological safety. Just as other fields of engineering and technology have
developed robust safety practices to mitigate risks and ensure the safe operation of
complex systems, so too can AI safety research be viewed as an integral part of the
progression within the broader domain of technological safety.
This framing has important implications for the field of AI safety. First, by recog-
nizing the relevance of AI safety to a diversity of risks, we can expand the circle of
stakeholders involved in the discourse about AI safety. This expanded engagement can
lead to increased funding and support for AI safety research, as well as a shift in the
discourse towards more practical and inclusive solutions. Second, we think that a more
episemically-inclusive research environment helps discussions to demistify existential
risks from fresh perspectives.
While our argument advocates for a broader perspective on AI safety, it is crucial
to emphasize that we do not intend to diminish the importance of critically engaging
with existential risk concerns. These risks remain a significant area of research and
policy debate, and our findings do not negate the need for continued investigation and
dialogue within this domain. However, by acknowledging the full breadth of AI safety
research, which extends beyond existential threats, we can foster a more inclusive and
productive discourse that encompasses the diverse range of risks associated with AI
systems, ultimately leading to a more comprehensive and effective approach to ensuring
AI safety.
Several research questions remain open. We highlight two of them below.
First, the concept of “sociotechnical AI safety” and its implications for the field of
AI safety require further investigation [2]. Although recent work [179] has begun to
clarify this notion in the context of AI evaluation practices, more research is needed
to examine the implications of sociotechnical approaches for AI safety research and
practice as a whole. This includes exploring how to effectively integrate social, ethical,
and political considerations into technical safety research and development.
Second, while our review focused on peer-reviewed literature, future research should
expand its scope to include non-peer-reviewed sources, such as more pre-print papers,
technical reports, and substantive research content on online forums and workshops.
This broader analysis would provide a more comprehensive understanding of the diverse
perspectives and approaches within AI safety and identify areas for future research and
collaboration. Our empirical analysis is just a first step in understanding a complex
practice.
Acknowledgments.
This research was made possible through the generous sup-
port of several funding bodies. Primary support came from the AI2050 program at
Schmidt Sciences (Grant 24-66924), which supported Atoosa Kasirzadeh’s contribu-
tions. Additional funding was provided by the UKRI Arts and Humanities Research
Council (grant AH/X007146/1). B´alint Gyevn´ar’s work was supported by the UKRI
16

--- Page 17 ---

Centre for Doctoral Training in Natural Language Processing through a joint grant
(EP/S022481/1) from UK Research and Innovation and the University of Edinburgh’s
School of Informatics and School of Philosophy, Psychology & Language Sciences.
References
[1] Kasirzadeh, A. Two types of AI existential risk: Decisive and accumulative.
arXiv preprint arXiv:2401.07836 (2024).
[2] Lazar, S. & Nelson, A. AI safety on whose terms? Science 381, 138–138 (2023).
[3] Ahmed, S., Ja´zwi´nska, K., Ahlawat, A., Winecoff, A. & Wang, M. Building
the epistemic community of AI safety.
First Monday (forthcoming).
URL
https://papers.ssrn.com/sol3/papers.cfm?abstract id=4641526.
[4] Bostrom, N. Existential risks: Analyzing human extinction scenarios and related
hazards. Journal of Evolution and Technology 9, 1–30 (2002).
[5] Bostrom, N. Superintelligence: Paths, dangers, strategies (Oxford University
Press, 2014).
[6] Ord, T. The precipice: Existential risk and the future of humanity (Hachette
Books, 2020).
[7] Boston Review. The logic of effective altruism. Boston Review (2015). URL
https://www.bostonreview.net/forum/peter-singer-logic-effective-altruism/.
[8] Gabriel, I. Effective altruism and its critics. Journal of Applied Philosophy 34,
457–473 (2017).
[9] Eisikovits,
N.
AI
is
an
existential
threat—just
not
the
way
you
think.
https://www.scientificamerican.com/article/
ai-is-an-existential-threat-just-not-the-way-you-think/ (2023). Accessed: July
12, 2023.
[10] Center for AI Safety.
Statement on ai risk.
https://www.safe.ai/work/
statement-on-ai-risk (2023). Accessed on 2024-05-08.
[11] Training, A. S. Ai safety training. https://aisafety.training/ (2024). Accessed on
2024-05-08.
[12] Wikipedia contributors. AI safety — wikipedia, the free encyclopedia (2024). URL
https://en.wikipedia.org/wiki/AI safety. [Online; accessed 21-January-2024].
[13] Ag¨uera y Arcas, B. & Norvig, P.
Artificial general intelligence is already
here. Noema Magazine (2023). Available at: https://www.noemamag.com/
artificial-general-intelligence-is-already-here/.
17

--- Page 18 ---

[14] Roose, K. A.I. Poses ‘Risk of Extinction’, Industry Leaders Warn. The New
York Times (2023). URL https://www.nytimes.com/2023/05/30/technology/
ai-threat-warning.html.
[15] BCS Comment. PM should make ethics a priority at AI safety summit, say tech
professionals (2023). URL https://www.bcs.org/articles-opinion-and-research/
pm-should-make-ethics-a-priority-at-ai-safety-summit-say-tech-professionals/.
Accessed: 27 January, 2024.
[16] Gilardi, F., Kasirzadeh, A., Bernstein, A., Staab, S. & Gohdes, A. We need to
understand the effect of narratives about generative ai. Nature Human Behaviour
1–2 (2024).
[17] Bender, E. M. Talking about a ‘schism’ is ahistorical (2023). URL https://medium.
com/@emilymenonbender/talking-about-a-schism-is-ahistorical-3c454a77220f.
[18] Krause, S. S. Aircraft safety (McGraw-Hill Professional Publishing, 2003).
[19] Boyd, D. D. A review of general aviation safety (1984–2017). Aerospace medicine
and human performance 88, 657–664 (2017).
[20] Pifferi, G. & Restani, P. The safety of pharmaceutical excipients. Il Farmaco 58,
541–550 (2003).
[21] Leveson, N. et al. Applying system engineering to pharmaceutical safety. Journal
of Healthcare Engineering 3, 391–414 (2012).
[22] De Kimpe, L., Walrave, M., Ponnet, K. & Van Ouytsel, J. Internet safety. The
international encyclopedia of media literacy 1–11 (2019).
[23] Salim, H. M. Cyber safety: A systems thinking and systems theory approach to
managing cyber security risks. Ph.D. thesis, Massachusetts Institute of Technology
(2014).
[24] Leveson, N. G. Engineering a safer world: Systems thinking applied to safety
(The MIT Press, 2016).
[25] Varshney, K. R. Engineering safety in machine learning, 1–5 (IEEE, 2016).
[26] Rismani, S. et al. From plane crashes to algorithmic harm: applicability of safety
engineering frameworks for responsible ml, 1–18 (2023).
[27] Dobbe, R. System safety and artificial intelligence, 1584–1584 (2022).
[28] Rismani, S. et al. Beyond the ml model: Applying safety engineering frameworks
to text-to-image development, 70–83 (2023).
18

--- Page 19 ---

[29] Amodei, D. et al. Concrete problems in AI safety. arXiv preprint arXiv:1606.06565
(2016).
[30] Raji, I. D. & Dobbe, R. Concrete problems in AI safety, revisited. arXiv preprint
arXiv:2401.10899 (2023).
[31] Kitchenham, B. & Charters, S. Guidelines for performing Systematic Literature
Reviews in Software Engineering. EBSE Technical Report EBSE-2007-01, School
of Computer Science and Mathematics, Keele University, Keele, UK (2007).
[32] Wohlin, C. Guidelines for snowballing in systematic literature studies and a
replication in software engineering, EASE ’14, 1–10 (Association for Computing
Machinery, New York, NY, USA, 2014).
[33] Irving, G., Christiano, P. & Amodei, D. AI safety via debate. arXiv (2018).
[34] Ng, A. Y. & Russell, S. J. Algorithms for Inverse Reinforcement Learning, ICML
’00, 663–670 (Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 2000).
[35] Hendrycks, D. et al. Aligning AI With Shared Human Values (ICLR, 2021).
2008.02275.
[36] Yampolskiy, R. V. Artificial Intelligence Safety and Cybersecurity: A Timeline
of AI Failures. arXiv (2016).
[37] Hadfield-Menell, D., Russell, S. J., Abbeel, P. & Dragan, A. Cooperative Inverse
Reinforcement Learning, Vol. 29 (Curran Associates, Inc., 2016).
[38] Xu, H., Zhu, T., Zhang, L., Zhou, W. & Yu, P. S. Machine Unlearning: A Survey.
ACM Computing Surveys 56, 9:1–9:36 (2023).
[39] Russell, S., Dewey, D. & Tegmark, M.
Research Priorities for Robust and
Beneficial Artificial Intelligence. AI magazine 36, 105–114 (2015).
[40] Willers, O., Sudholt, S., Raafatnia, S. & Abrecht, S. Casimiro, A., Ortmeier,
F., Schoitsch, E., Bitsch, F. & Ferreira, P. (eds) Safety Concerns and Mitigation
Approaches Regarding the Use of Deep Learning in Safety-Critical Perception
Tasks. (eds Casimiro, A., Ortmeier, F., Schoitsch, E., Bitsch, F. & Ferreira,
P.) Computer Safety, Reliability, and Security. SAFECOMP 2020 Workshops,
Lecture Notes in Computer Science, 336–350 (Springer International Publishing,
Cham, 2020).
[41] Mohseni, S. et al. Taxonomy of Machine Learning Safety: A Survey and Primer.
ACM Computing Surveys 55, 1–38 (2022).
[42] Hendrycks, D., Carlini, N., Schulman, J. & Steinhardt, J. Unsolved Problems in
ML Safety. arXiv (2022).
19

--- Page 20 ---

[43] Boyatzis, R. E. Transforming qualitative information: Thematic analysis and
code development (sage, 1998).
[44] van Eck, N. J. & Waltman, L. Software survey: VOSviewer, a computer program
for bibliometric mapping. Scientometrics 84, 523–538 (2010).
[45] Oster Jr, C. V., Strong, J. S. & Zorn, C. K. Analyzing aviation safety: Problems,
challenges, opportunities. Research in transportation economics 43, 148–164
(2013).
[46] Donaldson, M. S., Corrigan, J. M. & Kohn, L. T. To err is human: building a
safer health system (2000).
[47] Bates, D. W. et al. The safety of inpatient health care. New England Journal of
Medicine 388, 142–153 (2023).
[48] Marais, K., Dulac, N., Leveson, N. et al. Beyond normal accidents and high
reliability organizations: The need for an alternative approach to safety in complex
systems, 1–16 (Citeseer, 2004).
[49] Griffor, E. Handbook of system safety and security: cyber risk and risk manage-
ment, cyber security, threat analysis, functional safety, software systems, and
cyber physical systems (Syngress, 2016).
[50] Prasad, R. & Rohokale, V.
Cyber security: the lifeline of information and
communication technology (Springer, 2020).
[51] Soares, N., Fallenstein, B., Yudkowsky, E. & Armstrong, S. Corrigibility (Austin,
Texas, USA, 2015).
[52] Ring, M. & Orseau, L. Schmidhuber, J., Th´orisson, K. R. & Looks, M. (eds)
Delusion, Survival, and Intelligent Agents. (eds Schmidhuber, J., Th´orisson, K. R.
& Looks, M.) Artificial General Intelligence, Lecture Notes in Computer Science,
11–20 (Springer, Berlin, Heidelberg, 2011).
[53] Ganin, Y. et al. in Domain-Adversarial Training of Neural Networks (ed.Csurka,
G.) Domain Adaptation in Computer Vision Applications 189–209 (Springer
International Publishing, Cham, 2017).
[54] Balaji, Y., Sankaranarayanan, S. & Chellappa, R. MetaReg: Towards Domain
Generalization using Meta-Regularization, Vol. 31 (Curran Associates, Inc., 2018).
[55] Goodfellow, I. J., Shlens, J. & Szegedy, C. Explaining and Harnessing Adversarial
Examples (2015). 1412.6572.
[56] Madry, A., Makelov, A., Schmidt, L., Tsipras, D. & Vladu, A. Towards Deep
Learning Models Resistant to Adversarial Attacks. arXiv (2019).
20

--- Page 21 ---

[57] Ray, A., Achiam, J. & Amodei, D. Benchmarking Safe Exploration in Deep
Reinforcement Learning. OpenAI (2023). Unpublished article.
[58] Turchetta, M., Berkenkamp, F. & Krause, A. Wallach, H. et al. (eds) Safe
Exploration for Interactive Machine Learning. (eds Wallach, H. et al.) Advances
in Neural Information Processing Systems 32 (NIPS 2019), Vol. 32 (2019).
[59] Ouyang, L. et al. Training language models to follow instructions with human
feedback. arXiv (2022). OpenAI.
[60] Abbeel, P. & Ng, A. Y. Apprenticeship learning via inverse reinforcement learning,
ICML ’04, 1 (Association for Computing Machinery, New York, NY, USA, 2004).
[61] Izzo, Z., Smart, M. A., Chaudhuri, K. & Zou, J. Approximate Data Deletion
from Machine Learning Models, 2008–2016 (PMLR, 2021).
[62] Wu, Y., Dobriban, E. & Davidson, S. DeltaGrad: Rapid retraining of machine
learning models, 10355–10366 (PMLR, 2020).
[63] Adebayo, J. et al. Sanity Checks for Saliency Maps, Vol. 31 (Curran Associates,
Inc., 2018).
[64] Kim, B. et al. Interpretability beyond feature attribution: Quantitative testing
with concept activation vectors (TCAV), 2668–2677 (PMLR, 2018).
[65] Hendrycks, D. & Gimpel, K. A Baseline for Detecting Misclassified and Out-of-
Distribution Examples in Neural Networks (arXiv, 2018). 1610.02136.
[66] Hendrycks, D. & Dietterich, T. Benchmarking Neural Network Robustness to
Common Corruptions and Perturbations (arXiv, 2019). 1903.12261.
[67] Ortega, P. A., Maini, V. & the DeepMind safety team. Building safe artificial intel-
ligence: specification, robustness, and assurance. https://deepmindsafetyresearch.
medium.com/building-safe-artificial-intelligence-52f5f75058f1 (2018). Accessed:
2024-05-13.
[68] Meng, Y. et al. Distantly-Supervised Named Entity Recognition with Noise-Robust
Learning and Language Model Augmented Self-Training, 10367–10378 (2021).
[69] Wang, K. & Guo, P. A Robust Automated Machine Learning System with
Pseudoinverse Learning. Cognitive Computation 13, 724–735 (2021).
[70] Cappozzo, A., Greselin, F. & Murphy, T. B. A robust approach to model-based
classification based on trimming and constraints: Semi-supervised learning in
presence of outliers and label noise. Advances in Data Analysis and Classification
14, 327–354 (2020).
21

--- Page 22 ---

[71] Li, W. & Wang, Y. A robust supervised subspace learning approach for output-
relevant prediction and detection against outliers. Journal of Process Control
106, 184–194 (2021).
[72] Curi, S., Bogunovic, I. & Krause, A. Combining Pessimism with Optimism
for Robust and Efficient Model-Based Deep Reinforcement Learning, Vol. 139,
2254–2264 (2021).
[73] Dobbe, R., Gilbert, TK. & Mintz, Y. Hard choices in artificial intelligence.
Artificial Intelligence 300 (2021).
[74] Dwork, C. & Feldman, V. Privacy-preserving Prediction, 1693–1702 (PMLR,
2018).
[75] Elhage, N. et al. A mathematical framework for transformer circuits. Transformer
Circuits Thread (2021). Unpublished article.
[76] Kim, H. & Mnih, A. Disentangling by Factorising. arXiv (2019).
[77] Ward, F. & Habli, I. An Assurance Case Pattern for the Interpretability of
Machine Learning in Safety-Critical Systems, Vol. 12235 LNCS, 395–407 (2020).
[78] Gyevnar, B., Ferguson, N. & Schafer, B. Bridging the transparency gap: What
can explainable ai learn from the ai act?, 964–971 (IOS Press, 2023).
[79] Reimann, L. & Kniesel-W¨unsche, G. Safe-DS: A Domain Specific Language to
Make Data Science Safe, 72–77 (2023).
[80] Dey, S. & Lee, S.-W. A Multi-layered Collaborative Framework for Evidence-
driven Data Requirements Engineering for Machine Learning-based Safety-critical
Systems, 1404–1413 (2023).
[81] Wei, C.-Y., Dann, C. & Zimmert, J. A Model Selection Approach for Corruption
Robust Reinforcement Learning, Vol. 167, 1043–1096 (2022).
[82] Ghosh, A., Tschiatschek, S., Mahdavi, H. & Singla, A. Towards Deployment
of Robust Cooperative AI Agents: An Algorithmic Framework for Learning
Adaptive Policies. New Zealand (2020).
[83] Everitt, T. & Hutter, M. Avoiding Wireheading with Value Reinforcement
Learning (2016). 1605.03143.
[84] Hubinger, E., van Merwijk, C., Mikulik, V., Skalse, J. & Garrabrant, S. Risks
from learned optimization in advanced machine learning systems.
CoRR
abs/1906.01820 (2019). URL http://arxiv.org/abs/1906.01820.
[85] Pistono, F. & Yampolskiy, R. V. The Age of Artificial Intelligence, Ch. Unethical
Research: How to Create a Malevolent Artificial Intelligence (Vernon Press
22

--- Page 23 ---

Wilmington, DE, USA, 2016).
[86] Picardi, C., Paterson, C., Hawkins, R., Calinescu, R. & Habli, I. Assurance
argument patterns and processes for machine learning in safety-related systems,
Vol. 2560, 23–30 (2020).
[87] Wabersich, KJ., Hewing, L., Carron, A. & Zeilinger, MN. Probabilistic Model
Predictive Safety Certification for Learning-Based Control. IEEE Transactions
on Automatic Control 67, 176–188 (2022).
[88] Wen, M. & Topcu, U. Constrained Cross-Entropy Method for Safe Reinforcement
Learning. IEEE Transactions on Automatic Control 66, 3123–3137 (2021).
[89] Zanella-B´eguelin, S. et al. Analyzing Information Leakage of Updates to Natural
Language Models, 363–375 (2020). 1912.07942.
[90] Wang, Z., Chen, C. & Dong, D. A Dirichlet Process Mixture of Robust Task
Models for Scalable Lifelong Reinforcement Learning. IEEE Transactions on
Cybernetics 1–12 (2022).
[91] Zou, A. et al.
Universal and Transferable Adversarial Attacks on Aligned
Language Models. arXiv (2023).
[92] Ilyas, A. et al. Adversarial Examples Are Not Bugs, They Are Features, Vol. 32
(Curran Associates, Inc., 2019).
[93] He, RD., Han, ZY., Yang, Y. & Yin, YL. Not All Parameters Should Be Treated
Equally: Deep Safe Semi-supervised Learning under Class Distribution Mismatch,
6874–6883 (2022).
[94] Aghakhani, H., Meng, D., Wang, Y.-X., Kruegel, C. & Vigna, G. Bullseye
polytope: A scalable clean-label poisoning attack with improved transferability,
159–178 (2021).
[95] Liu, Y. et al. Backdoor Defense with Machine Unlearning, 280–289 (IEEE Press,
London, United Kingdom, 2022).
[96] Meinke, A. & Hein, M. Towards neural networks that provably know when they
don’t know (2020). 1909.12180.
[97] Abdelfattah, S., Kasmarik, K. & Hu, J. A robust policy bootstrapping algo-
rithm for multi-objective reinforcement learning in non-stationary environments.
Adaptive Behavior 28, 273–292 (2020).
[98] Djeumou, F., Cubuktepe, M., Lennon, C. & Topcu, U. Task-Guided Inverse
Reinforcement Learning Under Partial Information (2021). 2105.14073.
23

--- Page 24 ---

[99] Yampolskiy, R. V. Leakproofing the Singularity: Artificial intelligence confinement
problem. Journal of Consciousness Studies 19, 194–214 (2012).
[100] Yampolskiy, R. V. in Artificial Intelligence Safety Engineering: Why Machine
Ethics Is a Wrong Approach (ed.M¨uller, V. C.) Philosophy and Theory of Artificial
Intelligence Studies in Applied Philosophy, Epistemology and Rational Ethics,
389–396 (Springer, Berlin, Heidelberg, 2013).
[101] Yampolskiy, R. V. Taxonomy of Pathways to Dangerous AI (2015). 1511.03246.
[102] Wheatley, S., Sovacool, B. K. & Sornette, D. Reassessing the safety of nuclear
power. Energy Research & Social Science 15, 96–100 (2016).
[103] Tay, EB., Gan, OP. & Ho, WK. Rauch, HE. (ed.) A study on real-time artificial
intelligence. (ed.Rauch, HE.) Artificial Intelligence in Real-Time Control 1997,
109–114 (1998).
[104] Hibbard, B. Bach, J., Goertzel, B. & Ikl´e, M. (eds) Avoiding Unintended AI
Behaviors. (eds Bach, J., Goertzel, B. & Ikl´e, M.) Artificial General Intelligence,
Lecture Notes in Computer Science, 107–116 (Springer, Berlin, Heidelberg, 2012).
[105] Sezener, CE. Bieger, J., Goertzel, B. & Potapov, A. (eds) Inferring Human
Values for Safe AGI Design. (eds Bieger, J., Goertzel, B. & Potapov, A.) Artificial
General Intelligence (AGI 2015), Vol. 9205, 152–155 (2015).
[106] El Mhamdi, E. & Guerraoui, R. When Neurons Fail, 1028–1037 (2017).
[107] Freiesleben, T. & Grote, T. Beyond generalization: A theory of robustness in
machine learning. Synthese 202 (2023).
[108] Sanneman, L. & Shah, J.
Transparent Value Alignment, 557–560 (ACM,
Stockholm Sweden, 2023).
[109] Murphy, B., Talukdar, P. & Mitchell, T. Kay, M. & Boitet, C. (eds) Learning
Effective and Interpretable Semantic Models using Non-Negative Sparse Embed-
ding. (eds Kay, M. & Boitet, C.) Proceedings of COLING 2012, 1933–1950 (The
COLING 2012 Organizing Committee, Mumbai, India, 2012).
[110] Subramanian, A., Pruthi, D., Jhamtani, H., Berg-Kirkpatrick, T. & Hovy, E.
SPINE: SParse Interpretable Neural Embeddings (2017). 1711.08792.
[111] Shaham, U., Yamada, Y. & Negahban, S. Understanding adversarial training:
Increasing local stability of supervised models through robust optimization.
Neurocomputing 307, 195–204 (2018).
[112] Wu, G., Hashemi, M. & Srinivasa, C. PUMA: Performance Unchanged Model
Augmentation for Training Data Removal (2022). 2203.00846.
24

--- Page 25 ---

[113] Jing, S. & Yang, L. A robust extreme learning machine framework for uncertain
data classification. Journal of Supercomputing 76, 2390–2416 (2020).
[114] Gan, HT., Li, ZH., Fan, YL. & Luo, ZZ.
Dual Learning-Based Safe Semi-
Supervised Learning. IEEE Access 6, 2615–2621 (2018).
[115] Engstrom, L. et al. Adversarial Robustness as a Prior for Learned Representations.
arXiv (2019).
[116] Brophy, J. & Lowd, D. Machine Unlearning for Random Forests, 1092–1104
(PMLR, 2021).
[117] Chundawat, V. S., Tarun, A. K., Mandal, M. & Kankanhalli, M. Zero-Shot
Machine Unlearning. IEEE Transactions on Information Forensics and Security
18, 2345–2354 (2023).
[118] Chen, J., Li, Y., Wu, X., Liang, Y. & Jha, S. Oliver, N., P´erez-Cruz, F., Kramer,
S., Read, J. & Lozano, J. A. (eds) ATOM: Robustifying Out-of-Distribution
Detection Using Outlier Mining. (eds Oliver, N., P´erez-Cruz, F., Kramer, S.,
Read, J. & Lozano, J. A.) Machine Learning and Knowledge Discovery in
Databases. Research Track, Lecture Notes in Computer Science, 430–445 (Springer
International Publishing, Cham, 2021).
[119] Lakkaraju, H., Kamar, E., Caruana, R. & Horvitz, E. Identifying unknown
unknowns in the open world: Representations and policies for guided exploration,
Vol. 31 (2017).
[120] Zhuo, JB., Wang, SH., Zhang, WG. & Huang, QM.
Deep Unsupervised
Convolutional Domain Adaptation, 261–269 (2017).
[121] Bossens, DM. & Bishop, N. Explicit Explore, Exploit, or Escape (E4): Near-
optimal safety-constrained reinforcement learning in polynomial time. Machine
Learning 112, 817–858 (2023).
[122] Massiani, PF., Heim, S., Solowjow, F. & Trimpe, S. Safe Value Functions. IEEE
Transactions on Automatic Control 68, 2743–2757 (2023).
[123] Shi, M., Liang, Y. & Shroff, N. A Near-Optimal Algorithm for Safe Reinforcement
Learning Under Instantaneous Hard Constraints, Vol. 202, 31243–31268 (2023).
[124] Hunt, N. et al. Verifiably Safe Exploration for End-to-End Reinforcement Learning
(2021).
[125] Ma, Y. J., Shen, A., Bastani, O. & Dinesh, J. Conservative and Adaptive Penalty
for Model-Based Safe Reinforcement Learning, Vol. 36, 5404–5412 (2022).
[126] Zwane, S. et al. Safe Trajectory Sampling in Model-Based Reinforcement Learning,
Vol. 2023-August (2023).
25

--- Page 26 ---

[127] Fischer, J., Eyberg, C., Werling, M. & Lauer, M.
Sampling-based Inverse
Reinforcement Learning Algorithms with Safety Constraints, 791–798 (2021).
[128] Zhou, Z., Liu, G. & Zhou, M. A Robust Mean-Field Actor-Critic Reinforcement
Learning Against Adversarial Perturbations on Agent States. IEEE Transactions
on Neural Networks and Learning Systems 1–12 (2023).
[129] Bazzan, ALC.
Aligning individual and collective welfare in complex socio-
technical systems by combining metaheuristics and reinforcement learning.
Engineering Applications of Artificial Intelligence 79, 23–33 (2019).
[130] Christoffersen, P. J., Haupt, A. A. & Hadfield-Menell, D. Get It in Writing:
Formal Contracts Mitigate Social Dilemmas in Multi-Agent RL, AAMAS ’23, 448–
456 (International Foundation for Autonomous Agents and Multiagent Systems,
Richland, SC, 2023).
[131] Christiano, P. F. et al. Deep Reinforcement Learning from Human Preferences,
Vol. 30 (Curran Associates, Inc., 2017).
[132] Kaushik, D., Hovy, E. & Lipton, Z. C. Learning the Difference that Makes a
Difference with Counterfactually-Augmented Data (arXiv, 2020). 1909.12434.
[133] Li, ZY., Zeng, J., Thirugnanam, A. & Sreenath, K. Bridging Model-based Safety
and Model-free Reinforcement Learning through System Identification of Low
Dimensional Linear Models. Robotics: Science and System 18 (2022).
[134] Zhu, X., Kang, SC., Chen, JY. & IEEE A Contact-Safe Reinforcement Learning
Framework for Contact-Rich Robot Manipulation, 2476–2482 (2022).
[135] Terra, A., Riaz, H., Raizer, K., Hata, A. & Inam, R. Safety vs. Efficiency:
AI-Based Risk Mitigation in Collaborative Robotics, 151–160 (2020).
[136] Carlini, N. & Wagner, D. Towards Evaluating the Robustness of Neural Networks,
39–57 (IEEE Computer Society, 2017).
[137] Nguyen, A., Yosinski, J. & Clune, J. Deep neural networks are easily fooled: High
confidence predictions for unrecognizable images, 427–436 (IEEE, Boston, MA,
USA, 2015).
[138] Kaufmann, M. et al. Testing Robustness Against Unforeseen Adversaries. arXiv
(2019).
[139] Hendrycks, D. et al. What Would Jiminy Cricket Do? Towards Agents That
Behave Morally (2021).
[140] Gardner, M. et al. Cohn, T., He, Y. & Liu, Y. (eds) Evaluating Models’ Local
Decision Boundaries via Contrast Sets. (eds Cohn, T., He, Y. & Liu, Y.) Findings
of the Association for Computational Linguistics: EMNLP 2020, 1307–1323
26

--- Page 27 ---

(Association for Computational Linguistics, Online, 2020).
[141] Spears, D. F. in Assuring the Behavior of Adaptive Agents (eds Rouff, C. A.,
Hinchey, M., Rash, J., Truszkowski, W. & Gordon-Spears, D.) Agent Technol-
ogy from a Formal Perspective NASA Monographs in Systems and Software
Engineering, 227–257 (Springer, London, 2006).
[142] Wozniak, E., Cˆarlan, C., Acar-Celik, E. & Putzer, H. A Safety Case Pattern for
Systems with Machine Learning Components, Vol. 12235 LNCS, 370–382 (2020).
[143] Gholampour, P. & Verma, R. Adversarial Robustness of Phishing Email Detection
Models, 67–76 (2023).
[144] Nanda, N., Chan, L., Lieberum, T., Smith, J. & Steinhardt, J. Progress measures
for grokking via mechanistic interpretability. arXiv (2023).
[145] Olsson, C. et al. In-context learning and induction heads. Transformer Circuits
Thread (2022). OpenAI.
[146] Karpathy, A., Johnson, J. & Fei-Fei, L. Visualizing and Understanding Recurrent
Networks (arXiv, 2016). 1506.02078.
[147] Morcos, A. S., Barrett, D. G. T., Rabinowitz, N. C. & Botvinick, M. On the
importance of single directions for generalization. arXiv (2018).
[148] Gyevnar, B., Wang, C., Lucas, C. G., Cohen, S. B. & Albrecht, S. V. Causal
Explanations for Sequential Decision-Making in Multi-Agent Systems, AAMAS
’24, 771–779 (International Foundation for Autonomous Agents and Multiagent
Systems, Richland, SC, 2024).
[149] Okawa, Y., Sasaki, T. & Iwane, H. Automatic Exploration Process Adjustment for
Safe Reinforcement Learning with Joint Chance Constraint Satisfaction, Vol. 53,
1588–1595 (2020).
[150] Gan, HT., Luo, ZZ., Meng, M., Ma, YL. & She, QS. A risk degree-based safe
semi-supervised learning algorithm. International Journal of Machine Learning
and Cybernetics 7, 85–94 (2016).
[151] Zhang, YX. et al. Barrier Lyapunov Function-Based Safe Reinforcement Learning
for Autonomous Vehicles With Optimized Backstepping. IEEE Transactions on
Neural Networks and Learning Systems (2022).
[152] Nicolae, M.-I., Sebban, M., Habrard, A., Gaussier, E. & Amini, M.-R. Algorithmic
robustness for semi-supervised (ϵ, γ, τ)-good metric learning, Vol. 9489, 253–263
(2015).
[153] Khan, WU. & Seto, E. A ”Do No Harm” Novel Safety Checklist and Research
Approach to Determine Whether to Launch an Artificial Intelligence-Based
27

--- Page 28 ---

Medical Technology: Introducing the Biological-Psychological, Economic, and
Social (BPES) Framework. Journal of Medical Internet Research 25 (2023).
[154] Schumeg, B., Marotta, F. & Werner, B. Proposed V-Model for Verification,
Validation, and Safety Activities for Artificial Intelligence, 61–66 (2023).
[155] Kamm, S., Sahlab, N., Jazdi, N. & Weyrich, M. A Concept for Dynamic and
Robust Machine Learning with Context Modeling for Heterogeneous Manufactur-
ing Data, Vol. 118, 354–359 (2023).
[156] Costa, E., Rebello, C., Fontana, M., Schnitman, L. & Nogueira, I. A Robust
Learning Methodology for Uncertainty-Aware Scientific Machine Learning Models.
Mathematics 11 (2023).
[157] Aksjonov, A. & Kyrki, V.
A Safety-Critical Decision-Making and Control
Framework Combining Machine-Learning-Based and Rule-Based Algorithms.
SAE International Journal of Vehicle Dynamics Stability And NVH 7, 287–299
(2023).
[158] Antikainen, J. et al. Yue, T. & Mirakhorli, M. (eds) A Deployment Model to
Extend Ethically Aligned AI Implementation Method ECCOLA. (eds Yue, T. &
Mirakhorli, M.) 29th IEEE International Requirements Engineering Conference
Workshops (REW 2021), 230–235 (2021).
[159] Vakkuri, V., Kemell, KK., Jantunen, M., Halme, E. & Abrahamsson, P. ECCOLA
- A method for implementing ethically aligned AI systems. Journal of Systems
and Software 182 (2021).
[160] Zhang, H., Shahbazi, N., Chu, X. & Asudeh, A. FairRover: Explorative model
building for fair and responsible machine learning (2021).
[161] Coston, A. et al. A Validity Perspective on Evaluating the Justified Use of
Data-driven Decision-making Algorithms, 690–704 (2023).
[162] Gittens, A., Yener, B. & Yung, M. An Adversarial Perspective on Accuracy,
Robustness, Fairness, and Privacy: Multilateral-Tradeoffs in Trustworthy ML.
IEEE Access 10, 120850–120865 (2022).
[163] Taylor, J., Yudkowsky, E., LaVictoire, P. & Critch, A. Alignment for advanced
machine learning systems. Ethics of Artificial Intelligence 342–382 (2016).
[164] Sotala, K. & Yampolskiy, R. V. Responses to catastrophic AGI risk: A survey.
Physica Scripta 90, 018001 (2014).
[165] Johnson, B. Metacognition for artificial intelligence system safety-An approach
to safe and desired behavior. Safety Science 151 (2022).
[166] Hatherall, L. et al. Responsible Agency Through Answerability (2022).
28

--- Page 29 ---

[167] Stahl, BC. Embedding responsibility in intelligent systems: From AI ethics to
responsible AI ecosystems. Scientific Reports 13 (2023).
[168] Samarasinghe, D. Counterfactual learning in enhancing resilience in autonomous
agent systems. Frontiers in Artificial Intelligence 6 (2023).
[169] Diemert, S., Millet, L., Groves, J. & Joyce, J. Safety Integrity Levels for Artificial
Intelligence, Vol. 14182 LNCS, 397–409 (2023).
[170] Wang, J. & Jia, R. Data Banzhaf: A Robust Data Valuation Framework for
Machine Learning, Vol. 206, 6388–6421 (2023).
[171] Everitt, T., Filan, D., Daswani, M. & Hutter, M. Self-Modification of Policy and
Utility Function in Rational Agents. arXiv (2016).
[172] Badea, C. & Artus, G. Bramer, M. & Stahl, F. (eds) Morality, Machines, and
the Interpretation Problem: A Value-based, Wittgensteinian Approach to Building
Moral Agents. (eds Bramer, M. & Stahl, F.) Artificial Intelligence, AI 2022,
Vol. 39, 124–137 (2022).
[173] Umbrello, S. Beneficial Artificial Intelligence Coordination by Means of a Value
Sensitive Design Approach. Big Data and Cognitive Computing 3 (2019).
[174] Yampolskiy, R. & Fox, J. Safety Engineering for Artificial General Intelligence.
Topoi (2012).
[175] Weld, D. & Etzioni, O. Barley, M. et al. (eds) The First Law of Robotics. (eds
Barley, M. et al.) Safety and Security in Multiagent Systems, Lecture Notes in
Computer Science, 90–100 (Springer, Berlin, Heidelberg, 2009).
[176] Matthias, A. The responsibility gap: Ascribing responsibility for the actions of
learning automata. Ethics and Information Technology 6, 175–183 (2004).
[177] Farina, L. Muller, VC. (ed.) Artificial Intelligence Systems, Responsibility and
Agential Self-Awareness. (ed.Muller, VC.) Philosophy and Theory of Artificial
Intelligence 2021, Vol. 63, 15–25 (2022).
[178] Lee, A. T. Flight simulation: virtual environments in aviation (Routledge, 2017).
[179] Weidinger, L. et al. Sociotechnical safety evaluation of generative ai systems.
arXiv preprint arXiv:2310.11986 (2023).
29

```
