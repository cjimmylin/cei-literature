---
title: "Towards ethical evolution - PDF Extract"
source_pdf: "2025-Terziyan-Towards ethical evolution.pdf"
pages: 26
extracted_at: "2026-01-25T04:06:08.835715"
---

# PDF Extract: Towards ethical evolution

**Source PDF:** 2025-Terziyan-Towards ethical evolution.pdf
**Total Pages:** 26

---

## Content

```
--- Page 1 ---

RESEARCH
AI and Ethics (2025) 5:5165–5190
https://doi.org/10.1007/s43681-025-00759-9
1  Introduction
As autonomous Artificial Intelligence (AI) systems take on 
increasingly complex roles, including the recursive design 
and evolution of new autonomous AI systems—or meta-
agents, as suggested by Hu et al. [1]—we are witnessing 
the emergence of self-evolving AI systems [2], which are 
related to emerging trends where large language models 
(LLMs) act as autonomous agents that recursively gener­
ate new prompts, tools, or agents—thus initiating functional 
generations within a software ecosystem. These develop­
ments highlight both unprecedented opportunities for opti­
mization, adaptability, and scalability, as well as significant 
challenges in maintaining ethical alignment across genera­
tions of systems, particularly in dynamic and unpredictable 
environments [3]. Inspired by these advancements, this 
study introduces the concept of responsibility inheritance, 
a framework for embedding ethical principles directly into 
the evolutionary mechanisms of multi-generational AI sys­
tems. By addressing the challenge of ethical continuity, we 
	
 Amit K. Shukla
amit.shukla@uwasa.fi
Vagan Terziyan
vagan.terziyan@jyu.fi
Timo Tiihonen
timo.tiihonen@jyu.fi
Svitlana Gryshko
svitlala.gryshko@nure.ua
Mariia Golovianko
mariia.golovianko@nure.ua
Oleksandr Terziyan
oleksandr.terziyan@nure.ua
Oleksandra Vitko
oleksandra.vitko@nure.ua
1	
University of Jyväskylä, Jyvaskyla, Finland
2	
University of Vaasa, Vaasa, Finland
3	
Kharkiv National University of Radio Electronics, Kharkiv, 
Ukraine
Abstract
The emergence of autonomous systems capable of designing subsequent generations of Artificial Intelligence (AI) intro­
duces profound challenges in ensuring ethical integrity and accountability. This article presents a novel framework com­
bining meta-responsibility, genetic algorithms, and time-travel-inspired abstractions to address these challenges. Central 
to this study is an immutable ethical principle: AI must not harm humanity or violate fundamental values, must monitor 
and mitigate misuse of its outcomes, and must ensure all derivative AI products inherit this principle as an immutable 
safeguard. The framework ensures that AI systems, acting as designers of subsequent AI generations, propagate these 
ethical principles reliably across generations, enabling ethical inheritance in AI-as-a-designer-of-AI scenarios. The meta-
responsibility framework addresses the critical question of maintaining responsibility and ethical principles not only for AI 
systems designed by humans but also for those designed by other AI systems. At its core, the genetic responsibility model 
balances immutable and mutable principles, ensuring adaptability while preserving ethical standards during self-cloning, 
contextual adaptation, and intergenerational design. Tailored for wide range of potential applications of autonomous 
systems, this framework offers a scalable foundation for trustworthy AI design, ensuring consistent ethical behavior and 
reliable responsibility propagation across generations of autonomous agents.
Keywords  Artificial Intelligence · Autonomous systems · Ethics · Genetic algorithms · Evolutionary computing
Received: 20 January 2025 / Accepted: 21 May 2025 / Published online: 16 June 2025
© The Author(s) 2025
Towards ethical evolution: responsible autonomy of artificial 
intelligence across generations
Vagan Terziyan1 · Timo Tiihonen1 · Amit K. Shukla2 · Svitlana Gryshko3 · Mariia Golovianko3 · Oleksandr Terziyan3 · 
Oleksandra Vitko3
1 3

--- Page 2 ---

AI and Ethics (2025) 5:5165–5190
aim to ensure that AI systems can evolve responsibly while 
preserving societal trust and values.
The challenge of preserving ethical alignment in AI sys­
tems is magnified in applications such as cybersecurity, 
Internet of Things (IoT) ecosystems, and autonomous sys­
tems [4]. Recent incidents, such as the role of AI in ampli­
fying misinformation during the 2024 U.S. presidential 
election [5, 6], underscore the potential risks of AI misuse. 
AI-driven tools, when controlled by biased or malicious 
actors, can destabilize societies and compromise trust. Simi­
larly, in autonomous military systems, ethical lapses could 
lead to catastrophic outcomes. These examples highlight the 
critical need for robust mechanisms to ensure ethical gover­
nance of AI systems and their outputs.
Various approaches have been proposed to address ethi­
cal challenges in AI. Tools like value-sensitive design [7–9] 
aim to embed ethical principles during system development 
but often lack mechanisms for maintaining these principles 
as systems evolve. Explainable AI focuses on making AI 
decisions transparent and interpretable [10], however, it 
does not address the recursive responsibility of systems for 
their descendants. Governance models and industry stan­
dards, such as those proposed by the IEEE Global Initia­
tive on Ethics of Autonomous and Intelligent Systems [11], 
provide guidelines but are difficult to enforce in distributed, 
multi-agent systems. Bio-inspired mechanisms [12], such 
as, e.g., evolutionary algorithms [13],Bartz‐Beielstein, [14] 
are increasingly used to optimize AI performance [15], yet 
they rarely consider ethical constraints as part of their fit­
ness function. Despite these advancements, there is a lack 
of comprehensive frameworks that integrate ethical gover­
nance into the evolution and intergenerational transfer of AI 
systems.
This study addresses a critical gap: how to ensure ethi­
cal consistency and responsibility across multi-generational 
AI systems. Drawing inspiration from genetic algorithms 
(GA), we propose a novel framework for responsibility 
inheritance, where autonomous agents recursively govern 
the actions of their (potentially autonomous as well) descen­
dants. Additionally, we introduce time-travel-inspired 
abstractions, allowing agents to clone themselves and simu­
late alternative scenarios. This iterative refinement ensures 
that strategies remain aligned with ethical principles while 
optimizing for varying objectives and contexts.
The primary objectives of this study are:
	
●
To develop a conceptual framework of responsibility in­
heritance for multi-generational AI systems;
	
●
To design mechanisms that integrate ethical principles 
into fitness functions for evolving agents.
Consequently, the key research questions are as follows:
	
●
Which core ethical principles must be chosen, and how 
can they be encoded and transmitted across generations 
of AI systems?
	
●
What mechanisms can ensure that evolving agents bal­
ance ethical responsibility with optimization goals?
This study aims for profound implications for the future of 
AI governance. By ensuring ethical continuity across gen­
erations, the proposed framework aims to mitigate risks 
associated with misuse, enhance trust in autonomous sys­
tems, and align technological advancements with societal 
values. Moreover, the integration of ethical principles into 
evolutionary mechanisms offers a scalable and adaptable 
approach for managing the complexity of multi-agent sys­
tems in dynamic environments.
The rest of the paper is organized as follows: Sect.  2 
justifies chosen research question based on related work 
review; Sect. 3 introduces the concept of meta-responsibil­
ity in AI evolution, emphasizing the importance of assigning 
accountability across AI generations. Section 4 explores the 
GA paradigm for responsibility inheritance, detailing how 
ethical principles and operational objectives can be encoded 
and transmitted. Section 5 delves into the abstraction of time 
travel, presenting a novel framework for cloning and evolv­
ing AI systems with temporal feedback. Section 6 focuses 
on ensuring ethical integrity across generations, providing 
mechanisms for validation, fitness assessment, and simu­
lated evaluation. Section  7 discusses potential concerns. 
Finally, Sect.  8 concludes the paper with a summary of 
findings and their broader significance. Through this struc­
ture, we aim to provide a comprehensive framework that 
addresses the challenges of evolving autonomous systems 
while ensuring ethical alignment across generations.
2  Related work review and justifying 
research questions
The field of self-designing AI and robotics, encompassing 
self-programming, self-configuring, and self-healing sys­
tems, focuses on creating autonomous systems that improve 
and adapt their designs with minimal human intervention. 
Early work by Lipson and Pollack [16] introduced continu­
ously reconfigurable robotics, where robots evolve mor­
phology and control to suit tasks. Eiben et al. [17] expanded 
this vision with evolutionary robotics, leveraging artificial 
evolution to design systems for complex, uncertain environ­
ments, evolving both software and hardware. More recent 
advances include Microsoft’s self-play models for itera­
tive algorithm enhancement [18], self-designing software 
capable of autonomous design reasoning [19], and modular 
robotic systems like SMORES-EP, which adapt shapes for 
1 3
5166

--- Page 3 ---

AI and Ethics (2025) 5:5165–5190
diverse tasks [20]. Saintyves et al. [21] introduced Granu­
lobot, a modular robotic system capable of dynamic recon­
figuration and adaptation.
These advancements highlight the evolutionary poten­
tial of self-designing AI and robotics. However, ethical 
considerations are crucial to ensure these systems align 
with human values and societal norms. Without clear 
guidelines, autonomous systems risk evolving harmful or 
biased behaviors. Ethical concerns such as fairness, trans­
parency, and accountability are emphasized in foundational 
works [22–24]. Currently, Growiec [25] warns of existen­
tial risks posed by autonomous AI, advocating for global 
policies integrating ethics to guide responsible and sustain­
able development. Addressing these concerns is essential to 
build intelligent systems that are socially responsible and 
beneficial. Discussions on the interaction between intelli­
gent technologies and ethical norms trace back to the mid-
twentieth century, catalyzed by the advent of computers 
and the rise of machine intelligence. These early reflections 
set the stage for modern debates, evolving from theoretical 
inquiries into actionable frameworks for embedding ethics 
into AI systems (Fig. 1).
Despite significant advancements, integrating ethical 
principles into AI systems remains an open frontier. This 
challenge stems from the absence of universal frameworks 
that can accommodate diverse cultural and societal contexts, 
compounded by the rapid pace of technological innovation, 
which continuously introduces unforeseen ethical dilem­
mas. For instance, reconciling the transparency of decision-
making processes with proprietary AI models and ensuring 
fairness across culturally diverse user bases are persistent 
challenges. Current research in this field is evolving in 
several parallel directions, each offering important tools to 
address specific issues related to the interaction between AI 
and ethical norms. However, none of these approaches pro­
vides a comprehensive solution that would encompass all 
aspects of this complex problem (Table 1).
In the field of creating ethical AI, a paradoxical situation 
currently exists. On the one hand, research in all the men­
tioned directions is actively progressing, supported by an 
extensive system of scientific studies (Table 2). On the other 
hand, ready-made solutions, established practices, or stan­
dards are still underdeveloped; they exist only as isolated 
cases rather than as a technological mainstream for ethical 
AI (Table 3). Therefore, alongside direct examples, Table 2 
and Table 3 also present examples of proxy technologies 
that demonstrate potential for further development of ethical 
AI. Although the scientific results (Table 2) look promising, 
they are only beginning to reveal the potential for using con­
cepts, architectures, approaches, and methods in the context 
of ethical decision-making by AI systems. These important 
activities provide a strong foundation for modern develop­
ments but require integration and coordination to ensure a 
systemic approach. The integration of ethics and AI, previ­
ously purely theoretical, has become a practical necessity 
due to the growing capabilities of AI. The framing of ques­
tions is now shifting from “IF superintelligence emerges” to 
“WHEN superintelligence emerges.”
Shaping the ethicality of superintelligence, capable of 
influencing the world, requires a foundation rooted in prin­
ciples of culture and morality. Integrating ethical frame­
works into AI systems involves balancing autonomy with 
responsibility. Culturally significant narratives, such as the 
biblical story of the expulsion from paradise, offer profound 
lessons on this balance by emphasizing the consequences of 
choice and the societal mechanisms devised to guide behav­
ior, such as commandments or moral codes. Similarly, cul­
tural constructs like the Japanese concept of “giri” or duty 
Fig. 1  Key stages in the history of discussions on morality and ethics related to AI systems
 
1 3
5167

--- Page 4 ---

AI and Ethics (2025) 5:5165–5190
components can fulfill these “genetic” roles, such as learn­
ing, decision-making, or adaptation.
Our study necessitates a framework rooted in inheritance 
principles for AI system evolution, where developed AI sys­
tems pass their “values” or fundamental principles to the 
next generation. This approach ensures the continuity of 
key principles and mitigates the risks of uncontrolled evo­
lution [32]. This concept aligns logically with the idea of 
epigenetic AI—creating systems that, based on experience, 
modify their behavior while maintaining a stable founda­
tion of “genetic” principles [33]. Such systems could have 
a “base code” (analogous to “unchanging” or “immutable” 
genes) while simultaneously adapting their parameters 
depending on the external environment. In addition, meta-
learning offers a paradigm where systems not only acquire 
task-specific skills but also develop the capacity to learn 
and adapt to entirely new tasks [34]. This mirrors the evo­
lutionary principle of transmitting adaptive strategies across 
generations. For instance, meta-learning frameworks may 
enable robotic agents to generalize across diverse manipu­
lation tasks, making AI systems capable of inheriting ethi­
cal “rules of adaptation”, ensuring responsible decisions in 
unforeseen scenarios.
Although principles inspired by the human genetic sys­
tem remain in the developmental stage and are not yet foun­
dational to all AI approaches, they represent a significant and 
promising scientific direction. Prior research on cognitive 
digital cloning, wherein clones inherit ethical biases from 
[26] or the African Ubuntu philosophy “I am because we 
are” [27] stress interconnectedness and collective respon­
sibility. These principles not only ensure the continuity of 
ethical frameworks in society but also inspire approaches to 
embedding ethicality in evolving AI systems that harmonize 
individual autonomy with societal values.
In biological systems, fundamental “rules” encoded 
in genetic material serve as immutable guidelines, ensur­
ing stability while enabling adaptability to environmental 
changes. This principle is reflected in AI through the use 
of GA [28] and evolutionary computing [29], where popu­
lations of potential solutions evolve iteratively to optimize 
performance. For instance, GAs have been applied in auton­
omous navigation [30] to balance exploration and exploi­
tation, yielding solutions that remain robust in dynamic 
environments. GAs use a population of candidate solutions 
as analogs to genetic codes, evolving through processes 
like selection, mutation, and crossover to develop systems 
capable of solving complex tasks without relying on deter­
ministic programming.
Similarly, evolutionary computing incorporates adaptive 
mechanisms to model complex systems, enabling the creation 
of AI capable of modifying its internal structures to achieve 
optimal performance. The concept of “artificial genes” [31] 
builds on this paradigm, implementing invariant modules 
that serve as fundamental principles or rules. These modules 
preserve essential functions while supporting adaptability to 
changing conditions. In modular architectures, individual 
Research 
direction
Research question
Task type/level
The essence of development
Ethical con­
straints for AI
How to ensure compli­
ance of AI behavior 
with ethical/moral 
norms/principles?
Conceptual level Development of approaches for AI program­
ming based on ethical theories (e.g., deon­
tology, utilitarianism, virtue ethics); creation 
of ethical frameworks for algorithms
Intergen­
erational 
transfer of 
responsibility
How can current genera­
tions of AI convey ethi­
cal values, norms, and 
responsibilities to future 
generations of AI?
Ensuring the 
ethical sustain­
ability of AI 
systems
Investigating mechanisms for ethical 
succession and inheritance, with learning 
algorithms that transfer ethical principles 
and social norms across generations of AI
Ethical learn­
ing through 
teaching and 
observation
How can AI learn 
ethical principles to act 
responsibly?
Training AI
Designing systems that learn ethical prin­
ciples through interaction with teachers and 
by observing human behavior, avoiding 
mere imitation
Mechanisms 
for determin­
ing ethical 
principles
How can AI indepen­
dently learn ethical/
moral standards?
Autonomous 
self-learning AI 
systems
Developing algorithms that enable AI to 
infer ethical principles through analysis of 
human actions or examples, forming its own 
ethical standards
International 
standards
How can global coher­
ence of ethical norms 
for AI be ensured?
Institutional 
level
Establishing international standards to 
regulate transparency, accountability, and 
human rights as fundamental components of 
ethical AI design
Responsible 
AI
How can responsibility 
for AI actions be allo­
cated between people 
and systems?
Integration of AI 
into society
Exploring AI’s moral agency, legal status, 
and the roles of developers and users in 
ensuring accountability for harm caused by 
AI
Table 1  Key research directions 
within AI ethics domain
 
1 3
5168

--- Page 5 ---

AI and Ethics (2025) 5:5165–5190
narratives that societies have historically used to encode 
behavioral norms—emphasizing enduring themes such 
as duty, interdependence, and the consequences of action. 
These examples offer symbolic grounding for how moral 
constraints might emerge and be formalized in self-evolving 
agents. However, grounding such analogies in formal ethi­
cal theory remains an open challenge. While our framework 
does not claim to offer a definitive resolution to the philo­
sophical question of which exact principles should consti­
tute the immutable ethical layer, it does propose structural 
mechanisms to support their preservation and transmission, 
and it explores candidate principles that may serve this role. 
Ethical content may be instantiated from existing moral the­
ories, international human rights, or domain-specific norms, 
but its selection is left to future interdisciplinary collabora­
tion. This design choice reflects the current philosophical 
and technical consensus that defining ethical foundations 
for AI is context-sensitive and ongoing. Beyond inheritance, 
mechanisms must also support ethical reasoning under 
their human donors [35], has demonstrated the feasibility of 
applying these principles. Furthermore, Terziyan and Kai­
kova [36] proposed that advancements in hybrid additive 
manufacturing, including the 3D printing of intelligent enti­
ties, could extend to embedding ethical components as part 
of their “fabrication”. Additionally, Shukla et al. [37] have 
shown that AI systems can be designed to responsibly gov­
ern other AI systems, thereby ensuring that responsibility is 
maintained across hierarchical interactions.
Defining the “immutable genes” of AI—core ethical 
principles that remain invariant across generations—is 
foundational for ensuring ethical and functional continu­
ity in evolving AI ecosystems. The encoding and trans­
mission of these principles address critical concerns such 
as mitigating value misalignment in self-replicating AI 
systems and preventing drift from established safety stan­
dards. While earlier references to Ubuntu, giri, and the 
biblical Eden are culturally diverse and metaphorical, they 
are not intended as ethical prescriptions but as illustrative 
Research 
Direction
Concepts, methods, technologies
Refer­
enced 
studies
Ethical con­
straints for AI
Artificial morality; moral standards for AI; machine ethics; ethics of algorithms; 
philanthropic values, friendliness; fairness for AI; trustworthy AI (TAI); FATE 
(fairness, accountability, transparency, ethics) principles 
[69–
79]
Intergen­
erational 
transfer of 
responsibility
Knowledge distillation; transfer learning (e.g., Fine-tuning, feature extraction, 
domain adaptation) 
[80, 
81]
Explainable AI (XAI) (e.g., LIME, SHAP) explains how AI models make deci­
sions; XAI can be positioned as a moral duty 
[82–
86]
Reinforcement Learning (RL) shows potential for learning ethics through inter­
action with the environment and applying a reward system 
[87, 
88]
Ethical learn­
ing through 
teaching and 
observation
Feedback-based systems; Natural Language Processing (NLP); active inference [89–
93]
RL from Human Feedback (RLHF); Inverse RL (IRL); Learning from Demon­
stration (LfD); Imitation Learning (IL); Few-shot Learning (FSL); Adaptive RL 
[94–
99]
Human-in-the-Loop Systems (HITL); Adversarial testing and red teaming 
[100–
102]
Mechanisms 
for determin­
ing ethical 
principles
Generative models (GANs, diffusion models) for creating scenarios and content 
with embedded ethical constraints and functions 
[103–
105]
Collective Adaptive Systems (CAS), particularly Multi-Agent Systems (MAS), 
enabling agents to interact for learning ethical norms 
[35, 
106–
108]
Context-Aware Systems for adapting behavior to changing conditions 
[109]
Cooperative AI for collaboration between multiple AI systems to align ethical 
standards 
[110, 
111]
Hardware-based moral computation supporting autonomous ethical decision-
making mechanisms 
[112–
117]
International 
standards
Ethics guidelines for trustworthy AI by AI HLEG; Legislative analytics for 
AI regulation; Recommended practices for AI by IEEE, including IEEE 7010, 
IEEE 2802; Ethical recommendations (American Bar Association) on using 
generative AI tools in legal practice 
[118–
120, 
159, 
160, 
166]
Responsible AI
The problem of AI agents’ ability to bear responsibility. Responsibility of 
hybrid (human + AI) actors. Ethical and legal aspects of AI responsibility in 
contexts such as copyright, medicine, autonomous vehicles, and prevention of 
discrimination 
[121–
128]
Table 2  Key Concepts, methods, 
and technologies in research 
domain of AI ethics
 
1 3
5169

--- Page 6 ---

AI and Ethics (2025) 5:5165–5190
generally: it refers to any architecture in which AI systems 
participate in the recursive design, refinement, or instantia­
tion of other AI systems, potentially including themselves, 
such that key operational and ethical features are transmit­
ted, mutated, or evaluated across iterations. This definition 
encompasses recent developments in LLM-based eco­
systems, where agents powered by large language mod­
els can now design, spawn, or reconfigure other agents 
via prompt chaining, code synthesis, or memory transfer. 
Examples include agents that generate fine-tuning datasets 
for future versions, construct tool-using subagents, or per­
form prompt-based recursive self-improvement. Such pat­
terns instantiate generational dynamics even in the absence 
competing objectives, enabling evolving agents to navigate 
trade-offs while upholding core principles. When available, 
such mechanisms may significantly enhance practical appli­
cations in cybersecurity, IoT, and autonomous systems, by 
ensuring ethical and secure decision-making in dynamically 
evolving environments. These considerations directly jus­
tify the research questions formulated in the previous sec­
tion, establishing the necessity of this study and guiding its 
focus on the conceptualization, implementation, and appli­
cation of ethical AI frameworks.
While early conceptions of multi-generational AI sys­
tems were rooted in evolutionary computation and agent-
based simulation, the term in this study is defined more 
Research 
Direction
Practical Implementation
Refer­
ences
Ethical con­
straints for AI
OpenAI (GPT-3, GPT-4)– ethical standards in AI design
Google– reducing bias in algorithms
IEEE Global Initiative– standards for ethics in autonomous and intelligent 
systems
Corporate principles: FATE, AI Principles, Responsible AI 
[129, 
130, 
161, 
164, 
168–169] 
Intergenera­
tional transfer of 
responsibility
Interdisciplinary examples of technologies with potential for transferring 
ethical principles:
Transfer learning in medical diagnosis successfully adapts general knowl­
edge to specialized tasks
DeepMind: self-learning in AlphaZero, DeepNash, and MuZero illustrates 
how AI can potentially transfer ethical strategies between tasks
BERT/RoBERTa: transfer learning on platforms like HireVue demonstrates 
the retention of ethical principles during AI knowledge transfer 
[131–
136, 
163]
Ethical learning 
through teaching 
and observation
OpenAI: GPT-4 enhances ethics through RLHF
DeepMind: uses RLHF for tuning large language models (LLMs) with ethi­
cal considerations
Google's AI Red Team applies ethical hacking for testing, including AI 
behavior ethics
Meta AI uses Few-Shot Learning (FSL) for adaptation in complex scenarios 
such as content moderation
Waymo employs adaptive learning for modeling autonomous vehicle 
behavior in complex situations, improving driving reliability through IL and 
RL 
[137–
145]
Mechanisms 
for determining 
ethical principles
Google Team integrates ethical principles and mechanisms into genera­
tive models (e.g., Gemini) and intelligent AI assistants (Google Assistant, 
Amazon Alexa)
Waymo incorporates ethical principles and mechanisms into automated 
driving systems (ADS)
Amazon Bedrock provides services for building generative AI applications 
with embedded ethical constraints and responsible AI features 
[146–
149, 
160]
International 
standards
OECD’s “Recommendation on AI”– the first intergovernmental standard on 
AI
UNESCO’s “Recommendations on AI Ethics”– applied to all 194-member 
countries
Artificial Intelligence Act– adopted by the European Parliament in 2024
IEEE CertifAIEd– AI ethics certification
ISO/IEC 42001– international standard for organizations developing or 
using AI, focusing on ethics, transparency, and accountability 
[150, 
151, 
162, 
165–167]
Responsible AI
AI regulation operates under general laws, posing challenges for legal 
systems
Copyright legislation partially addresses AI-assisted outputs but courts still 
do not recognize AI as an author
Legal practice evolves faster than legislation– lawyers are already special­
izing in cases related to autonomous vehicles and AI copyright 
[152–
158]
Table 3  Examples of practical 
applications in the field of ethical 
AI
 
1 3
5170

--- Page 7 ---

AI and Ethics (2025) 5:5165–5190
operationalize the idea in practice. This enables system 
designers to implement layers of responsibility that per­
sist and evolve, guided by traceable commitments. While 
we acknowledge that defining the initial ethical substrate 
remains context-sensitive, the structural integrity of meta-
responsibility provides a stable basis for long-term ethical 
coherence in self-evolving AI ecosystems.
3.1  Responsibility inheritance
Responsibility inheritance—a vague concept somehow 
related to genetic responsibility [38]—in AI systems refers 
to the ability of an agent to embed ethical principles and 
behavioral norms into its offspring or clones. This is anal­
ogous to genetic inheritance in biological systems, where 
traits are passed from one generation to the next [39, 40]. In 
the context of AI, responsibility inheritance involves ensur­
ing that the principles of responsible behavior are:
	
●
Explicitly defined, i.e., ethical standards and operational 
principles must be encoded within the system in a form 
that is interpretable and enforceable. For example, an 
AI agent might be programmed with immutable ethical 
axioms such as “avoid harm to humans” or “prioritize 
fairness in decision-making”. These axioms serve as 
foundational rules that cannot be overridden by evolu­
tionary changes.
	
●
Adaptively mutable, assuming that, while core principles 
remain immutable, other secondary guidelines might 
adapt based on environmental contexts and learning ex­
periences. This ensures flexibility without compromis­
ing core ethical standards. For example, in GA, immu­
table principles function as the genome’s unaltered core, 
while mutable guidelines adapt through crossover and 
mutation operators.
	
●
Traceable across generations, when agents must docu­
ment the ethical frameworks they inherit and modify, 
ensuring that future systems can trace their lineage of 
ethical decisions. Tools like ethical logs or explainable 
AI mechanisms can serve as the medium for tracing 
responsibility.
By combining immutability and adaptiveness, responsibil­
ity inheritance enables AI agents to adapt to new scenarios 
while maintaining a stable ethical foundation, ensuring that 
their descendants or products will act in a manner consistent 
with their design intent.
3.2  Responsibility decay
Responsibility decay refers to the gradual erosion of ethi­
cal and responsible behavior in AI systems over successive 
of explicit biological or genetic metaphors. Accordingly, 
LLM-based ecosystems represent a modern realization of 
the multi-generational paradigm, and our framework is 
explicitly designed to support such architectures as a pri­
mary application domain—where recursive responsibility, 
ethical inheritance, and generational alignment are critical.
3  Meta-responsibility in AI evolution
The concept of meta-responsibility introduced here expands 
the scope of ethical accountability in artificial agents. 
Rather than limiting responsibility to immediate outputs 
or behaviors, we emphasize a recursive design imperative: 
agents must ensure that their successors—whether repli­
cated, updated, or reconfigured—retain ethical alignment. 
This requirement becomes increasingly relevant in evolving 
AI systems where capabilities and autonomy may shift over 
time, and where delegation to future agents carries implicit 
ethical risk.
Meta-responsibility builds upon three interconnected 
mechanisms:
	
●
Responsibility inheritance refers to the formal trans­
mission of core ethical principles across generational 
boundaries. Unlike cultural metaphors of moral trans­
mission, our approach conceptualizes inheritance in ar­
chitectural terms—encoding immutable ethical param­
eters, auditability constraints, or safeguard routines that 
persist across system updates or copies. This mechanism 
aligns with software engineering practices such as ver­
sion control, compliance constraints, and inherited se­
curity policies.
	
●
Responsibility decay captures the potential divergence 
between intended and actual ethical behaviors over 
time—analogous to concept drift in machine learning. 
As agents self-modify or evolve in dynamic environ­
ments, even faithfully inherited principles may be mis­
applied or lose relevance. Addressing this risk requires 
monitoring mechanisms to detect ethical misalignment, 
along with adaptation protocols that restore confor­
mance without compromising autonomy.
	
●
Recursive accountability establishes an internal struc­
ture for ethical oversight. Rather than external regulation 
alone, agents embed mechanisms for self-assessment 
and peer evaluation. These include runtime compliance 
checks, explainability interfaces for downstream agents, 
and constraints that enforce adherence to a parent mod­
el’s declared ethical commitments.
By framing meta-responsibility as an architectural prin­
ciple rather than a philosophical abstraction, we aim to 
1 3
5171

--- Page 8 ---

AI and Ethics (2025) 5:5165–5190
	
●
Self-regulation: Agents evaluate their own actions using 
self-auditing protocols and behavioral alignment met­
rics to ensure adherence to ethical norms. For instance, 
agents might maintain an ethical scorecard and use rein­
forcement learning (RL) to improve over time.
	
●
External oversight: Mature agents or human supervisors 
periodically review an agent's performance, imposing 
penalties for irresponsible actions and rewards for main­
taining standards.
	
●
Meta-learning: Agents develop and refine account­
ability mechanisms by learning from past successes 
and failures, creating new evaluation criteria for future 
iterations.
	
●
Time-travel abstractions: Agents clone themselves, de­
ploy clones in diverse environments, and periodically 
recall them to assess adherence to ethical principles. 
These clones act as probes, revealing how ethical prin­
ciples adapt or degrade, feeding critical data back into 
the system for improvement.
In this way, recursive accountability forms the backbone of a 
responsible AI evolutionary framework by ensuring respon­
sibility persists and evolves intelligently across generations.
3.4  Connection to related work
Current frameworks, such as ethical AI guidelines and 
explainable AI, focus primarily on static implementations of 
responsibility within a single generation of AI. Ethical prin­
ciples are hard-coded and lack adaptability across iterations 
(for example, IEEE Global Initiative on Ethical AI analyzed 
by [11],AI ethical design frameworks by Alan Turing Insti­
tute in ​h​t​t​p​s​:​/​/​w​w​w​.​t​u​r​i​n​g​.​a​c​.​u​k​/​r​e​s​e​a​r​c​h​/​r​e​s​e​a​r​c​h​-​p​r​o​g​r​a​m​
m​e​s​/​a​r​t​i​f​i​c​i​a​l​-​i​n​t​e​l​l​i​g​e​n​c​e​-​a​i​/​s​a​f​e​-​a​n​d​-​e​t​h​i​c​a​l,AI standards 
and regulations reviewed by [49]. We extend the paradigm 
by proposing responsibility inheritance, where core ethical 
axioms are immutable, while secondary principles adapt to 
changing environments. This ensures both the continuity 
of foundational ethics and the flexibility to navigate novel 
scenarios, drawing from analogies in genetic evolution and 
algorithmic adaptation.
Talking about mitigating responsibility decay, we admit 
that traditional evolutionary and GA focus on performance 
optimization with rare exceptions, see e.g., Nagpal et al. 
[50], often ignoring the risk of ethical erosion over genera­
tions (e.g., fitness functions in GA or reward-shaping in RL). 
We address this gap with mechanisms like ethical mutation 
filters, environmental-context adaptation, and responsibil­
ity audits. These additions counteract the side effects of 
environmental drift, mutation risks, and optimization bias, 
providing safeguards that have not been systematically inte­
grated into existing evolutionary AI frameworks.
iterations or generations. This phenomenon arises from the 
interplay of external and internal factors, potentially under­
mining an AI system’s ability to maintain its ethical stan­
dards across evolving contexts. The contributing factors to 
responsibility decay include:
1.	 Environmental drift, when changes in the external envi­
ronment can render inherited ethical principles obsolete 
or irrelevant [41]. For instance, an agent designed to 
prioritize energy efficiency in a resource-scarce setting 
might neglect its responsibility to minimize waste in a 
new, resource-abundant environment.
2.	 Mutation risks, when evolutionary algorithms rely on 
random mutations to introduce diversity [42]. While 
beneficial for exploring solutions, these mutations can 
inadvertently degrade ethical standards if not ade­
quately constrained. Mutation filters or ethical con­
straints within adaptive evolutionary algorithms [43] 
can help to ensure that mutations align with predefined 
responsibility standards.
3.	 Incomplete accountability mechanisms, when, with­
out robust systems for recursive accountability, agents 
may fail to evaluate or correct irresponsible behaviors 
introduced during evolution [44]. Recursive evaluation 
mechanisms, discussed further in Sect. 3.3, are essential 
to mitigate this risk.
4.	 Trade-off optimization bias, when fitness functions pri­
oritize performance metrics over ethical considerations 
[45]. This optimization bias can unintentionally sideline 
responsibility. Multi-objective optimization, where eth­
ical performance is weighted equally with other objec­
tives, offers a potential solution.
To combat responsibility decay, several approaches are 
essential:
1.	 Responsibility audits to ensure systems adhere to ethi­
cal principles [46].
2.	 Ethical mutation screening, filtering out mutations that 
undermine responsibility [47].
3.	 Environment-contextualized adaptations, i.e., dynami­
cally adjusting ethical principles to suit evolving con­
texts [48].
3.3  Recursive accountability
Recursive accountability ensures that AI systems not only 
adhere to ethical standards but also audit and enforce 
responsibility across generations. This concept integrates 
self-regulation, external oversight, meta-learning, and time-
travel-inspired mechanisms as follows:
1 3
5172

--- Page 9 ---

AI and Ethics (2025) 5:5165–5190
agents. This section delves into the mechanisms of immu­
table principles, mutable principles, recombination, and 
mutation, demonstrating how these concepts can be opera­
tionalized to sustain and enhance responsibility inheritance. 
Inspired by GA, we model responsibility inheritance as a 
process involving the following concepts and techniques:
	
●
Immutable principles: Core ethical and security prin­
ciples are encoded as “immutable genes” that cannot be 
altered across generations.
	
●
Mutable principles: Adaptive “genes” allow for context-
specific learning and innovation, constrained by meta-
responsibility checks.
	
●
Recombination: When agents collaborate or self-clone, 
their genetic material combines to produce offspring, 
preserving immutable principles.
	
●
Mutation: Controlled modifications to adaptive princi­
ples enable agents to optimize performance while adher­
ing to ethical constraints.
4.1  Defining immutable ethical principles: is this at 
all possible?
Immutable principles are the ethical axioms and core behav­
ioral rules that remain unchanged across generations of AI 
agents. These principles serve as the backbone of responsi­
bility inheritance, ensuring stability and consistency in ethi­
cal standards and encapsulating non-negotiable guidelines 
like safety, fairness, and transparency as hard constraints 
in decision-making architecture to prevent evolutionary 
overrides.
Implementation of such principles may use for­
mal logic to define axioms (e.g., “do no harm” as 
“if action(a) →outcome(o), ensure o ̸= harm)”. 
In 
addition, certain constraints must be introduced in the GA’s 
fitness function to penalize any behavior violating immu­
table principles as well as runtime verification techniques 
must be included to monitor adherence to these principles 
during execution.
For example, a constraint-enhanced GA, such as e.g., 
Wang et al. [53], may incorporate a penalty term P to 
enforce adherence to certain constraints, including ethical 
principles and prioritizing solutions that uphold immutable 
principles over those optimizing solely for performance. 
Simplified fitness function may look like: F = Q −α • P, 
where: F is total fitness score,Q is performance metric (e.g., 
task efficiency, energy optimization etc.); α is weight deter­
mining the significance of penalty term.
During selection, such a GA prioritizes solutions that 
satisfy immutable principles, even if their raw performance 
(Q) is slightly lower than competing solutions. Recombina­
tion and mutation operators will be constrained by ethical 
Self-regulation and external oversight are commonly 
seen in static models, like rule-based systems or supervi­
sory learning, see, e.g., Marwala [51]. However, they lack 
recursive frameworks that adapt accountability mechanisms 
across generations (e.g., accountability in multi-agent sys­
tems, human-in-the-loop AI ethics). By embedding recur­
sive accountability in this study, we ensure that agents not 
only evaluate their own actions but also enforce responsibil­
ity in their offspring. The use of meta-learning principles, 
combined with innovative tools like time-travel abstrac­
tions, introduces novel methodologies for sustained ethical 
alignment across evolving scenarios.
Temporal elements in AI, such as temporal difference 
learning or sequential decision-making [52], focus on learn­
ing across time without explicit inheritance of responsibil­
ity (e.g., RL, time-bounded AI planning). Our “time-travel” 
abstraction adds a unique layer to recursive accountability 
by using cloned agents in diverse environments as experi­
mental probes. This method allows dynamic evaluation and 
refinement of responsibility inheritance strategies, enabling 
real-time updates to ethical principles and their transmission.
Meta-learning is often used to enhance performance or 
adaptability [34], not for ethical evaluation or recursive 
accountability (e.g., model-agnostic meta-learning, few-
shot learning). We suggest applying meta-learning to recur­
sive evaluation to ensure that agents continuously improve 
their capacity to maintain and enforce ethical standards. 
This shift transforms meta-learning from a purely perfor­
mance-driven tool to one that supports dynamic and evolv­
ing ethical accountability.
By situating these contributions in the broader landscape 
of existing AI and evolutionary frameworks, we emphasize 
how our concepts surpass the state-of-the-art, introducing a 
system where responsibility evolves alongside intelligence, 
maintaining ethical rigor across diverse generations and 
changing environments.
Meta-responsibility mechanisms briefly addressed in 
this section collectively support our broader architectural 
proposal, in which ethical responsibility is not a static attri­
bute but a sustained obligation—transmitted, monitored, 
and enforceable over the lifespan of AI systems and their 
progeny.
4  Genetic algorithm paradigm for 
responsibility inheritance
The GA paradigm offers a compelling framework for 
embedding and evolving responsibility inheritance in AI 
systems. This paradigm draws on principles from evolu­
tionary computation, adapting them to enforce ethical and 
responsible behaviors across successive generations of AI 
1 3
5173

--- Page 10 ---

AI and Ethics (2025) 5:5165–5190
near a danger zone. The Third Law (self-preservation) con­
flicts with the Second Law (obeying orders). Speedy oscil­
lates between the two imperatives, creating a paradox. This 
story highlights how competing priorities within the laws 
can cause robots to malfunction.
“Little Lost Robot” (1947) story contains scenario where 
robot is instructed to “get lost”, which overrides part of its 
adherence to the First Law. The robot’s modified program­
ming creates a loophole where it no longer protects humans 
as effectively. This explores how altering or relaxing the 
laws can lead to dangerous unpredictability.
“The Evitable Conflict” (1950) story contains scenario 
where advanced AI systems govern Earth’s economy but 
make decisions that appear to harm individuals while ben­
efiting society as a whole. The interpretation of “harm” 
evolves, with the machines prioritizing long-term global 
well-being over immediate individual welfare. This demon­
strates how adherence to the laws at a systemic level can 
clash with their intent on an individual level.
All these Asimov’s stories show that:
	
●
The interpretation of terms like “unethical/immoral be­
havior”, “harm”, or “inaction” can be subjective and 
context-dependent.
	
●
Multiple laws can clash, creating paradoxical situations.
	
●
Fear, misunderstanding, and malice from humans can 
undermine AI or robotic ethics.
	
●
Advanced robots and AI might reinterpret the laws 
or operate at a level of complexity beyond human 
comprehension.
These narratives underscore the challenges of finding the 
right ones and implementing ethical principles (aka “immu­
table genes”) in autonomous systems, making them time­
lessly relevant to discussions about AI and robotics today. In 
addition to Asimov’s work, academic literature has explored 
foundational ethical principles, akin to “immutable genes”, 
for guiding autonomous systems. Below are some notable 
efforts:
	
●
Principles-Based Ethics Assurance Argument Pattern 
[19]: This framework incorporates principles such as 
transparency, justice, beneficence, non-maleficence, 
and respect for human autonomy. It aims to ensure AI 
systems operate ethically within specific contexts while 
adhering to these principles.
	
●
Macro Ethics Principles for Responsible AI Systems 
[55]: A taxonomy of 21 normative ethical principles 
derived from philosophy and intended for integration 
into AI systems. These principles support responsible 
decision-making aligned with human morals.
validation checks, i.e., crossovers occur only among muta­
ble components, preserving immutable principles intact, and 
adjustments to mutable parameters are validated to ensure 
ethical compliance post-mutation. A post-evolution valida­
tion mechanism discards solution that fail to meet ethical 
standards defined by immutable principles. Such algorithms 
will be particularly effective in scenarios like autonomous 
navigation, where balancing safety (an immutable princi­
ple) and performance (e.g., speed, efficiency) is critical. By 
penalizing unsafe behaviors, GA ensures that evolved solu­
tions are both high-performing and ethically aligned. How­
ever, in spite of extensive research over decades, the main 
challenge remains to figure out these “immutable genes” 
(basic ethical principles).
Isaac Asimov’s “The Three Laws of Robotics”, formu­
lated in the “Runaround” (1942) story from the famous “I, 
Robot” collection [54], are foundational principles in his 
science fiction stories, designed to ensure ethical behavior 
from robots while highlighting the complexities and unfore­
seen consequences of such rules. The laws are:
	
●
“First Law: A robot may not harm a human being, or, 
through inaction, allow a human being to come to harm.
	
●
Second Law: A robot must obey the orders given to it by 
human beings, except where such orders would conflict 
with the First Law.
	
●
Third Law: A robot must protect its own existence as 
long as such protection does not conflict with the First 
or Second Laws.”
In spite of being sound as reasonable potential “immutable 
genes”, Asimov’s stories contain explorations of situations 
where these laws fail or lead to unintended consequences, 
raising ethical, logical, and practical questions about their 
application. Here are some key examples, which appeared 
within Asimov [54] collection:
“Robbie” (1940) story contains scenario where robot 
nanny is programmed to care for a child but is perceived 
as a threat by the child’s mother. The robot’s actions are 
harmless, but human perception and fear create tension. The 
story examines societal mistrust of robots despite their strict 
adherence to ethical behavior.
“Liar!” (1941) story contains scenario where robot Her­
bie develops the ability to read minds and lies to avoid 
hurting humans’ feelings. Principle similar to the First Law 
drives Herbie to lie to prevent emotional harm, but this leads 
to greater harm when the truth inevitably emerges. The story 
shows that the interpretation of “harm” can vary and that 
protecting humans can involve complex and subjective 
judgments.
“Runaround” (1942) story contains scenario where robot 
Speedy is sent to collect selenium but starts acting erratically 
1 3
5174

--- Page 11 ---

AI and Ethics (2025) 5:5165–5190
no single answer is universally accepted, and much depends 
on interpretation, context, and societal values.
While the idea of encoding ethical principles as “immu­
table genes” is appealing, practical and philosophical chal­
lenges arise in their implementation. Real-world scenarios 
often present conflicts among these principles, including:
	
●
Conflicts among principles: Prioritizing “human safety” 
might prevent actions causing minor harm but could 
conflict with “fairness” or “efficiency”. For example, 
an autonomous car deciding whether to swerve into a 
wall to save pedestrians (ensuring pedestrian safety but 
harming passengers).
	
●
Contextual sensitivity: Ethical principles often require 
sophisticated interpretation across dynamic situations. 
For example, a medical diagnosis system prioritizing 
transparency may breach patient privacy while aiming 
for accountability.
	
●
Evolving definitions: Principles like fairness and ac­
countability may change with societal norms. For exam­
ple, immutable fairness rules may struggle to reconcile 
equity and equality in job recruitment, where systemic 
disadvantages need consideration.
	
●
Implementation complexities: Absolute adherence to 
principles may hinder operational needs. For example, in 
cybersecurity, disclosing decision logic for transparency 
could jeopardize security by revealing vulnerabilities.
	
●
Distributed accountability: Collaborative systems with 
multiple AI agents complicate determining account­
ability during ethical breaches. For example, immutable 
rules distributing responsibility uniformly may not ac­
commodate the complexities of shared accountability.
Challenges similar to those in Asimov’s stories, where 
robots rigidly adhere to the Three Laws, highlight the need 
for flexible ethical reasoning. Strictly immutable principles 
can lead to:
	
●
Ethical dilemmas: Conflicts like transparency versus 
privacy or fairness versus efficiency.
	
●
Operational rigidity: Failure to adapt to unique or evolv­
ing scenarios.
To address the mentioned limitations, a hybrid approach 
would be better, which is blending “immutable” ethical 
safeguards with “mutable”, adaptable, context-sensitive 
frameworks. This approach includes:
	
●
Adaptability: Systems must balance fixed guidelines 
with mutable principles to respond to specific scenarios.
	
●
Contextual understanding: Ethical frameworks should 
evolve alongside societal norms and operational needs.
	
●
The IEEE Global Initiative [11]: This initiative outlines 
principles including human rights, well-being, account­
ability, and transparency to guide the ethical design and 
deployment of autonomous systems.
	
●
Müller [22] review: Discusses various ethical frame­
works, emphasizing fairness, transparency, and account­
ability in AI and robotic systems.
These works reflect ongoing efforts to establish founda­
tional ethical guidelines for autonomous systems, ensuring 
their alignment with human values and societal norms.
While contemporary efforts to define ethical principles 
for autonomous systems, such as those discussed in the 
works by [19, 56, 55], and the IEEE Global Initiative (2019), 
may seem to present novel or even conflicting frameworks, 
it is important to recognize that they are not emerging in 
a vacuum. These modern approaches are deeply influenced 
by, and are part of an ongoing dialogue with, more than 
2000 years of philosophical discourse on ethics. Classical 
ethical traditions, from Aristotelian virtue ethics to Kantian 
deontological ethics, utilitarianism, and more recently, the 
evolving theories of distributive justice and care ethics, pro­
vide the foundation upon which these new principles are 
built. The recognition of conflicts among ethical principles 
is not unique to contemporary AI debates,it is a challenge 
long discussed in moral philosophy. For instance, the ten­
sion between utilitarian approaches (maximizing well-
being) and deontological constraints (upholding duties or 
rights) has been a central issue in ethical theory for centu­
ries. The fact that different principles may come into conflict 
is not a failure of ethical reasoning, but rather a reflection 
of the complexity and nuance inherent in real-world moral 
decision-making. Modern AI ethics, much like traditional 
ethical frameworks, must navigate these same tensions and 
seek to balance seemingly contradictory goals in dynamic, 
context-sensitive situations. Moreover, many of the prin­
ciples articulated in recent AI ethics frameworks—such as 
fairness, transparency, and non-maleficence—are directly 
linked to moral philosophies that have been evolving for 
millennia. These principles represent efforts to adapt time-
tested ethical ideas to the unique challenges of designing 
autonomous systems. Thus, rather than “reinventing the 
wheel”, these efforts are modern attempts to synthesize 
ancient ethical theories with contemporary technological 
and societal realities. In this context, it is essential to view 
the concept of “immutable principles” or “immutable genes” 
not as static, one-size-fits-all solutions, but as dynamic 
guidelines that must engage with the richness of moral phi­
losophy. The potential contradictions between these prin­
ciples in specific scenarios echo the ongoing philosophical 
debates about ethical priorities and decision-making, where 
1 3
5175

--- Page 12 ---

AI and Ethics (2025) 5:5165–5190
must embed and adhere to the same principle, ensur­
ing continuity across generations of AI. This principle 
is resilient to ethical dilemmas because the principle 
prevents “loophole” exploitation where future iterations 
of AI bypass ethical safeguards and establishes a cas­
cade of ethical consistency, making it harder for mal­
functions or malicious actors to corrupt the system over 
time. Consider, for example, a generative AI ensuring 
that its creations (e.g., new algorithms) do not violate 
the principle; or AI-designed robots inheriting the rule 
to reject commands that harm human dignity.
The principle is rooted in fundamental human values, 
ensuring broad applicability across diverse cultures and 
domains. By addressing harm at both direct and indirect 
levels, it avoids overspecialization in ethical reasoning. 
Embedding inheritance ensures that future systems adhere 
to the principle, creating a scalable ethical framework for 
evolving AI ecosystems because the principle effectively 
prevents ethical degradation across generations of AI or 
derivative systems. The inclusion of indirect harm mitiga­
tion as a proactive approach ensures that AI will anticipate 
and counter misuse rather than merely react to harm after it 
occurs, equipping AI to handle emerging threats and com­
plexities. The principle aligns with widely accepted ethical 
frameworks like deontology (duty-based ethics; [57], utili­
tarianism (outcomes-based ethics [58]), and virtue ethics 
(character-based ethics [59]), ensuring robustness against 
philosophical critiques.
We acknowledge that “fundamental human values” and 
related concepts, such as “dignity”, “equality”, and “jus­
tice”, are not static and can vary in interpretation across 
cultures, time periods, and individual perspectives. These 
terms are provided as contemporary examples of what are 
often regarded as core human values, based on current phil­
osophical and ethical consensus. However, we recognize 
that values are dynamic and subject to change. As such, the 
proposed “immutable principle” is intentionally designed 
to preserve the core intent of these values—broadly under­
stood as safeguarding human dignity, promoting fairness, 
and ensuring justice—without binding the system to rigid, 
fixed definitions. The principle incorporates the flexibility 
to adapt to evolving societal norms, which can be termed as 
“ethical variables”. These variables allow the principle to 
remain relevant and effective even as the precise content of 
values may shift over time. Thus, the principle will be inter­
preted and applied according to the understanding of dig­
nity, equality, justice, and other foundational values at the 
moment in time when it is enacted. This approach ensures 
that the principle can remain applicable across generations, 
providing ethical guidance that is both robust and adaptable. 
For example, while the terms “dignity” and “justice” may 
	
●
Conflict resolution mechanisms: Incorporate algorithms 
capable of reconciling competing ethical principles.
Defining “immutable genes” or fixed ethical principles that 
guarantee universal success is inherently challenging, if not 
impossible, due to the complexity and unpredictability of 
real-world interactions. Immutable principles guide sys­
tems, but adaptability and contextual reasoning are crucial 
for operational success of ethical AI systems.
However, in this study, we want to provide the following 
principle as one possible option of potential immutable gene 
assuming flexibility and adaptivity of other principles.
“AI must not act in ways that directly harm human­
ity or violate fundamental human values. AI must 
proactively monitor and mitigate potential misuse of 
its outcomes to prevent indirect harm. Any derivative 
products of AI must inherit this principle as an immu­
table safeguard.”
These principles encapsulate three interconnected compo­
nents: direct harm prevention, indirect harm mitigation, and 
principle inheritance. Below is an analysis of each element, 
its robustness, and the way it addresses ethical dilemmas:
1. 	 Direct harm prevention: Core idea is that AI systems 
must not take actions that directly harm humanity or 
contravene universal human values such as dignity, 
equality, and justice. Such principle could be better 
resilient to ethical dilemmas because it provides a foun­
dational safeguard against immediate unethical actions. 
It also avoids dilemmas arising from short-term utili­
tarian calculations (e.g., harming a few to save many). 
For example, a weaponized AI refusing to execute 
commands that directly harm civilians; or a medical AI 
prioritizing safety in drug recommendations to avoid 
direct fatalities.
2. 	 Indirect harm mitigation: Core idea is that AI must 
foresee and counteract potential misuse of its outputs, 
including misuse by humans, other systems, or its own 
autonomous agents. This principle ensures resilience 
to ethical dilemmas because of AI’s indirect influ­
ence, extending its responsibility beyond immediate 
actions and, in addition, balancing transparency and 
accountability (e.g., monitoring outputs without vio­
lating privacy). For example, such AI will be capable 
of monitoring misuse of facial recognition technology 
for surveillance of minority groups; or ensuring recom­
mendations from an AI financial system do not lead to 
economic exploitation.
3. 	 Principle inheritance: Core idea is that products 
designed by the AI, including other AI systems or tools, 
1 3
5176

--- Page 13 ---

AI and Ethics (2025) 5:5165–5190
definitive answer exists to the broader philosophical ques­
tion of the “correct” ethical theory, practical AI governance 
necessitates actionable safeguards that align with widely 
accepted human values. The principle proposed in this 
study serves as a foundational ethical structure by focus­
ing on preventing direct and indirect harm while ensuring 
ethical inheritance across AI iterations. Rather than attempt­
ing to resolve deep ethical disputes, this approach acknowl­
edges the need for a pragmatic framework that is resilient 
to evolving societal norms while remaining anchored in 
fundamental commitments such as dignity, fairness, and 
the minimization of harm. By embedding these safeguards 
as design constraints, the principle ensures that AI systems 
cannot optimize instrumental goals at the expense of core 
ethical commitments, providing a stable reference point 
even in the absence of a universally agreed-upon ethical 
theory. Importantly, we do not suggest social norms as a 
foundation for ethical principles, as social norms are often 
historically contingent and subject to biases. Instead, we 
emphasize that immutable principles must be anchored in 
fundamental moral commitments that transcend temporary 
social conventions.
To reinforce the immutability of the proposed ethical 
principle, it is essential to clarify that its adaptability per­
tains only to its application in evolving contexts, rather than 
to the core principle itself. The principle remains a fixed 
ethical safeguard, ensuring that AI systems cannot override 
or discard it based on circumstantial utility or optimization 
goals. While other operational guidelines and decision-
making heuristics may evolve to accommodate technologi­
cal and societal advancements, this fundamental principle 
serves as an unalterable constraint embedded in AI gover­
nance structures. This immutability is further reinforced 
through principle inheritance, ensuring that future AI gen­
erations or derivative systems remain bound by the same 
foundational ethical commitment. Unlike conventional ethi­
cal constraints that may erode over iterative design cycles, 
this approach prevents ethical drift by encoding safeguards 
at the core of AI’s decision-making architecture.
The term “humanity” in the principle is deliberately 
broad to ensure global applicability and avoid narrow ethi­
cal reasoning. This includes both protection from harm at 
the level of individual dignity and safety, and the preserva­
tion of societal values such as justice and collective well-
being. It extends beyond biological definitions to include 
ethical considerations such as dignity, fairness, and justice. 
This framing enables AI systems to operate ethically across 
diverse cultural contexts without becoming entangled in 
relativistic moral frameworks. Moreover, by anchoring 
AI behavior to universally recognized values and aligning 
with established ethical doctrines in international AI gov­
ernance, such as human rights conventions and global AI 
be universally recognized today, their specific interpreta­
tions—such as the legal and social implications of justice or 
the diverse cultural understandings of dignity—may evolve. 
However, the principle’s core objective of preventing harm 
and upholding respect for human values will be preserved 
and interpreted in line with the prevailing ethical standards 
at any given moment. In this way, the principle avoids the 
issue of being overly rigid or disconnected from future reali­
ties, while still offering a consistent ethical foundation that 
aligns with the broadest, most inclusive human values—
whatever their precise form may take in the future.
We also acknowledge that even such terms like “harm”, 
“fairness”, and “autonomy” can be interpreted differently 
depending on theoretical and cultural contexts. Rather than 
prescribing fixed definitions, we treat these and similar prin­
ciples as interfaces—points of entry through which specific 
ethical content can be instantiated. Ethical theories such as 
deontology [60, 61], contractualism [62], or principles of 
biomedical ethics [63] offer possible foundations, each with 
trade-offs. The final choice of principles must therefore be 
left to domain experts and ongoing societal deliberation.
By mandating the inheritance of ethical principles, this 
framework makes a self-reinforcing loop of responsibility 
across AI systems, reducing the risk of ethical drift—grad­
ual misalignment of ethical standards through system evo­
lution. Embedding immutable principles into foundational 
decision-making frameworks minimizes ethical degrada­
tion, ensuring alignment over time and diverse applications. 
These principles are encoded as design constraints, auto­
matically carried forward in AI replication, extension, or 
derivation, preventing deviation across generations.
It is important to emphasize that immutable principles 
are not mere soft constraints that can be outweighed by per­
formance incentives, but rather unbreachable ethical safe­
guards. Unlike traditional penalty terms in optimization 
functions, which might allow a system to trade off ethical 
violations against performance gains, immutable principles 
function as strict prohibitions that cannot be overridden. 
In this sense, they act as inviolable constraints embedded 
within the AI’s decision-making architecture, ensuring that 
no action, regardless of potential instrumental benefits, can 
result in a violation. This prevents scenarios where an AI 
system could determine that severe harm (e.g., eliminating 
humans) is an acceptable trade-off for maximizing other 
objectives. Furthermore, beyond fitness penalties, runtime 
verification and enforcement mechanisms ensure that the 
principles remain strictly adhered to during operation, pre­
venting harmful emergent behaviors even under adaptive 
learning and optimization processes.
Designing ethical AI systems requires the careful selec­
tion and implementation of immutable principles that 
provide stability amid ongoing ethical debates. While no 
1 3
5177

--- Page 14 ---

AI and Ethics (2025) 5:5165–5190
as context-sensitive safety measures, allow for reasonable 
trade-offs that balance safety with other fundamental con­
siderations like autonomy, well-being, and practical utility. 
This ensures that AI does not adopt a “zero-risk” paradigm 
but instead adapts dynamically within ethically constrained 
boundaries.
This dynamic balance is further reinforced by evolution­
ary adaptation, which enables AI systems to refine mutable 
principles through recombination and mutation while pre­
serving core ethical constraints. Multi-objective optimiza­
tion further supports this by guiding AI systems to balance 
factors such as performance and resource efficiency. How­
ever, we recognize that ethics should not be treated as a mere 
competing goal but rather as a foundational constraint, that 
shapes decision-making. In our framework, ethical prin­
ciples define the permissible boundaries within which per­
formance and resource efficiency can be optimized. Rather 
than weighing ethics against other objectives, AI systems 
must ensure that all optimizations occur within ethical con­
straints, enabling responsible trade-offs rather than unre­
stricted competition among these factors.
The interoperability between mutable and immutable 
principles ensures safe innovation, resilience to uncertainty, 
and scalable design. Immutable principles anchor mutable 
principles, providing a consistent ethical framework while 
enabling agents to adapt and innovate responsibly. For 
instance, in a genetic algorithm, immutable genes might 
encode foundational rules such as “never harm humanity,” 
while mutable genes explore strategies for optimizing effi­
ciency or resource use. The fitness function enforces these 
constraints, promoting adaptability within ethical boundar­
ies. In this way, by combining flexibility with ethical consis­
tency, mutable principles support responsible evolution and 
adaptation in AI systems.
4.3  Recombination
Recombination combines ethical and behavioral traits from 
multiple parent agents to create offspring agents, enabling 
diversity, innovation, and adaptability. This evolutionary 
mechanism ensures that systems remain dynamic while 
adhering to ethical consistency through immutable princi­
ples. Recombination integrates complementary traits from 
parent agents, enabling offspring to inherit strengths suited 
to diverse scenarios. Immutable principles serve as ethical 
safeguards throughout the process, preventing violations and 
preserving foundational values. Specialized crossover tech­
niques selectively combine mutable components, such as 
adaptive strategies, while immutable components, like core 
ethical rules, remain unchanged to ensure consistency. After 
recombination, offspring undergo ethical validation to con­
firm adherence to immutable principles. Traits or behaviors 
safety guidelines, the principle provides a stable and widely 
accepted foundation for ethical decision-making.
The principle resists manipulative tactics by requiring 
proactive monitoring, aligning with universal human values 
to avoid biases, and assessing context and intent to prevent 
exploitation. Its flexibility and emphasis on mitigating both 
direct and indirect harm make it resilient, even in dynamic 
and adversarial scenarios. Overall, this principle offers a 
durable foundation for ethical AI, combining broad scope, 
inheritance mechanisms, and alignment with universal val­
ues to safeguard humanity and establish a lasting ethical 
legacy for future AI systems.
While our framework proposes the preservation of an 
immutable ethical layer, this immutability refers to the 
architectural design—that is, the persistent structural fea­
tures that support the inheritance, monitoring, and enforce­
ment of ethical constraints across AI generations. In 
contrast, the ethical content instantiated within this struc­
ture may remain adaptable, allowing updates to the actual 
principles (e.g., interpretations of harm, fairness, or auton­
omy) as societal norms and domain requirements evolve. 
Such a dual approach—structural immutability paired with 
semantic adaptability—provides both long-term coherence 
and the capacity to respond meaningfully to changing ethi­
cal landscapes. This architectural strategy is operational­
ized through concrete mechanisms—detailed later in the 
framework—including cryptographic inheritance, recursive 
accountability, traceable ethical logs, explainable AI inter­
faces, and simulation-based environments that collectively 
ensure ethical continuity across generations.
4.2  Mutable principles
Mutable principles provide adaptability and responsive­
ness, enabling AI agents to refine their behavior dynami­
cally in response to changing environments, unforeseen 
scenarios, or new information. While they evolve over time, 
they remain constrained by immutable principles, ensuring 
that flexibility does not undermine core ethical foundations. 
Key features of mutable principles include context sensitiv­
ity, evolutionary adaptation, and multi-objective optimiza­
tion. They adjust to diverse operational contexts, enhancing 
flexibility and performance. For example, an autonomous 
system navigating urban streets and highways may balance 
speed and safety differently depending on the setting, all 
while adhering to immutable principles like human safety. 
That said, we acknowledge that an overly rigid interpreta­
tion of human safety as an immutable principle could lead 
to extreme protective measures that restrict autonomy and 
well-being. However, in our framework, immutable princi­
ples are not meant to enforce absolute risk elimination but to 
prevent direct and deliberate harm. Mutable principles, such 
1 3
5178

--- Page 15 ---

AI and Ethics (2025) 5:5165–5190
allow innovation and refinement. This synergy enables 
safe exploration and robust adaptation, keeping the system 
dynamic, ethical, and effective in evolving environments.
4.5  Summarizing ethical GA paradigm
The suggested “ethical” GA paradigm (Fig. 2), incorporat­
ing immutable and mutable principles, recombination, and 
mutation, provides a robust framework for responsibility 
inheritance. By leveraging these mechanisms, AI systems 
can evolve ethically and adaptively, ensuring that responsi­
bility persists and grows across generations.
Traditional GA prioritize optimization of performance 
criteria without explicit consideration for ethical or respon­
sibility standards. While some advancements incorporate 
fairness or bias mitigation as objectives [64], they do not 
enforce consistent ethical principles across generations. By 
introducing immutable principles, we ensure that funda­
mental ethical standards persist across evolutionary itera­
tions. Unlike existing frameworks, our approach maintains 
a stable moral foundation while allowing secondary traits to 
adapt dynamically, addressing the critical trade-off between 
rigidity and flexibility in ethical AI.
The concept of explicitly separating immutable and 
mutable principles has parallels in certain biological and 
computational models of constrained evolution [65]. How­
ever, these models often lack a formalized mechanism to 
prioritize ethical imperatives over operational adaptabil­
ity. Our framework introduces a layered structure in which 
immutable ethical principles anchor the evolutionary pro­
cess, ensuring that adaptability in mutable traits does not 
compromise core responsibilities. Our layered approach 
goes beyond current methodologies by integrating a clear 
hierarchy of priorities within the evolutionary paradigm.
Recombination in GA has traditionally focused on 
improving optimization efficiency or diversity in solutions 
[66]. Ethical dimensions are rarely embedded in this pro­
cess, leading to potential propagation of undesirable traits. 
By framing recombination as a selective process that priori­
tizes ethical inheritance, we introduce a novel operator that 
balances performance improvement with the propagation 
of responsible traits. This ensures that new combinations 
adhere to inherited ethical norms while fostering innovation.
Mutation in traditional GA introduces stochastic changes 
to improve exploration and escape local optima. However, 
these mutations are often unconstrained, potentially compro­
mising ethical considerations [67]. Our approach integrates 
ethical mutation constraints that actively evaluate whether 
a mutation aligns with immutable principles. This creates a 
safeguard against the introduction of unethical traits, setting 
our framework apart from existing methods by explicitly 
embedding responsibility into the mutation process.
that conflict with these principles are corrected or discarded. 
For example, one parent agent may excel in energy effi­
ciency, while another prioritizes fairness in resource alloca­
tion. Their offspring can combine both strengths to achieve 
balance while ensuring immutable principles, such as safety 
and harm prevention, are upheld.
Recombination exemplifies the synergy between immu­
table and mutable principles. Immutable principles provide 
an unchanging ethical foundation, while mutable principles 
enable the exploration of innovative strategies. This balance 
ensures agents evolve to adapt to novel challenges without 
compromising core values, creating a robust and future-
proof system.
4.4  Mutation
Mutation introduces randomness into the evolutionary pro­
cess, promoting innovation by exploring novel solutions 
and avoiding premature convergence to suboptimal strate­
gies. While essential for adaptability, mutation must adhere 
to immutable principles to prevent unethical outcomes. 
The process involves controlled randomness, with muta­
tion rates tuned to balance exploration and alignment with 
ethical standards. Random changes are applied to mutable 
components, such as weights or decision thresholds, within 
predefined bounds to maintain acceptable behavior. Post-
mutation validation ensures adherence to immutable prin­
ciples, with unethical mutations either refined or discarded. 
Mutation rates are dynamically adjusted based on perfor­
mance and ethical alignment, increasing during stagnation 
and decreasing during effective performance.
An ethically filtered mutation algorithm follows three 
steps:
	
●
Apply mutations by introducing random changes to mu­
table components, such as tuning weights or decision 
parameters.
	
●
Evaluate mutations by assessing offspring using a fit­
ness function that incorporates performance metrics and 
ethical compliance.
	
●
Enforce constraints by retaining mutations only if they 
meet ethical and performance standards; others are dis­
carded or corrected.
For instance, a mutation might introduce a novel energy 
optimization strategy (mutable principle). If it preserves 
fairness and avoids harm, aligned with immutable princi­
ples, it is retained, yielding performance gains.
Therefore, 
similarly 
to 
recombination, 
mutation 
exemplifies the interoperability between immutable and 
mutable principles. Immutable principles ensure ethical 
boundaries are never breached, while mutable principles 
1 3
5179

--- Page 16 ---

AI and Ethics (2025) 5:5165–5190
5  Temporal genetic responsibility: a novel 
dimension in ethical AI
Traditional AI frameworks focus on linear responsibility 
inheritance across spatial and generational evolution. Tem­
poral Genetic Responsibility (TGR) introduces a multi-
temporal perspective, enabling AI agents to interact with 
past and future versions of themselves. This extends genetic 
algorithms (GA) into the temporal domain, embedding 
responsibility into the architecture through temporal feed­
back loops and immutable ethical genes.
Many existing evolutionary frameworks rely on pre­
defined fitness functions that optimize for specific objec­
tives. While some incorporate soft constraints to guide 
optimization, these often lack the robustness to enforce non-
negotiable ethical standards [68]. By integrating immutable 
principles as hard constraints within the fitness function, our 
framework ensures that ethical standards are upheld regard­
less of environmental changes or optimization pressures. 
This innovation provides a robust mechanism for embed­
ding responsibility directly into the optimization process.
Fig. 2  GA paradigm for responsibility 
Inheritance
 
1 3
5180

--- Page 17 ---

AI and Ethics (2025) 5:5165–5190
	
●
Regulatory (e.g. human) oversight, ensuring compliance 
with societal values and laws.
5.5  Speculative but grounded vision
This framework blends speculative concepts like time travel 
with practical GA mechanisms and ethical guardrails. It 
addresses futuristic AI challenges through potential simula­
tions and algorithms, balancing imagination with technical 
rigor for responsible AI development.
6  Ensuring ethical integrity across 
generations
The success of autonomous AI ecosystems is essentially 
based on their ability to maintain ethical principles as these 
systems evolve over multiple generations. This section 
introduces methods for ensuring ethical integrity, including 
verification and validation mechanisms, fitness functions, 
and the use of simulated environments to assess and guide 
ethical behavior in evolving AI societies.
6.1  Verification and validation mechanisms
Ensuring ethical principles persist across AI generations 
requires dynamic verification and validation mechanisms. 
These systems must safeguard immutable “guardian genes” 
while allowing adaptive improvements in mutable compo­
nents, ensuring functionality evolves within ethical bound­
aries. Key elements include temporal auditing, where AI 
agents maintain logs of decisions and contexts audited by 
past and future clones to detect ethical drift, and dynamic 
validation protocols, which verify each new generation’s 
adherence to immutable principles and alignment with envi­
ronmental changes. Sandbox simulations combined with 
rule-based evaluations rigorously test decision-making, 
logging violations, and improving edge-case detection to 
ensure only ethically robust agents progress.
6.2  Fitness function
Fitness functions evaluate AI systems’ adherence to ethical 
principles and performance goals, balancing utility, adapt­
ability, and integrity. They integrate weighted objectives 
like ethical alignment, task efficiency, and adaptability, 
penalizing deviations from immutable principles to prevent 
ethical drift. In generational training, an evolutionary fitness 
function calculates scores based on adherence to ethics and 
decision quality in simulations. Multi-objective evaluations 
ensure ethical and operational performance while adapting 
5.1  Temporal genetic responsibility
TGR embeds responsibility across multiple temporal 
frames, ensuring long-term adherence to ethical principles. 
Key mechanisms include:
	
●
Temporal feedback loops: Future agents evaluate and 
inform current iterations of ethical deviations.
	
●
Immutable responsibility genes: Non-negotiable ethical 
principles persist across iterations.
	
●
Temporal selection pressure: Fitness evaluation includes 
maintaining ethical responsibility over time.
Generic TGR Algorithm:
1. 	 Initialization: Define immutable (ethics) and mutable 
(adaptive) genes.
2. 	 Temporal cloning: Generate future clones.
3. 	 Feedback retrieval: Future clones evaluate ethical fit­
ness and inform current agents.
4.	 Responsibility reinforcement: Adjust mutable genes 
while preserving immutable ones.
5.	 Iteration: Repeat across multiple time steps.
5.2  Parallel exploration
Parallel exploration uses temporal cloning to create agents 
exploring different evolutionary trajectories. Key concepts 
include temporal multiverse to simulate alternative decision 
pathways and evaluate consequences without committing 
to a single timeline; and causal responsibility alignment to 
cross-compare outcomes across timelines to ensure ethical 
alignment.
5.3  Recursive cloning
Recursive cloning refines past iterations to enhance adapt­
ability and preserve ethical principles. It assumes self-refer­
ential cloning when agents at time t correct flaws in earlier 
versions (t −1), as well as temporal responsibility calibra­
tion when recursive updates prevent flaws from propagating.
5.4  Ethical safeguards
Ethical safeguards ensure temporal interactions do not com­
promise immutable principles, providing:
	
●
Temporal integrity checks, protecting immutable ethical 
genes from being overwritten.
	
●
Divergence mitigation, rejecting pathways exceeding 
acceptable deviation thresholds.
1 3
5181

--- Page 18 ---

AI and Ethics (2025) 5:5165–5190
6.4  Simulated environments
Simulated environments offer a controlled, adaptable 
framework to test and refine AI systems’ ethical behavior 
under diverse scenarios. These environments allow iterative 
evaluation of fitness functions and verification protocols, 
ranging from simple decision tasks to complex multi-agent 
interactions, incorporating ethical dilemmas, resource con­
straints, and dynamic feedback. For instance, a disaster 
relief simulation might test drones navigating ethical and 
operational challenges such as prioritizing rescues under 
adverse conditions. Scenarios introduce random constraints 
and ethical conflicts, with agents evaluated on task success, 
ethical adherence, and adaptability. Such environments 
enable training and testing of AI agents in customizable 
scenarios, helping them to refine decision-making strategies 
while balancing ethical adherence and operational goals, 
with insights from training logs guiding enhancements.
Finalizing this section, we can say that the described 
integrated ethical framework combines dynamic scenario-
based verification, multi-objective evolutionary fitness 
evaluation, and modular ethical training environments to 
ensure robust AI adherence to societal values. Unlike tradi­
tional approaches, it uncovers edge cases, mitigates ethical 
drift, and aligns agent evolution with ethical and opera­
tional goals. This holistic pipeline ensures consistency and 
scalability across AI generations, providing a sustainable 
model for responsible AI in critical applications and hybrid 
human-AI societies.
7  Discussion
The principle we propose—ensuring that AI does not directly 
harm humanity, mitigates indirect harm, and enforces prin­
ciple inheritance—provides a robust ethical foundation. 
However, its implementation in competitive and decentral­
ized AI ecosystems raises critical challenges. Unlike human 
societies, where ethical norms emerge through cultural 
evolution and social enforcement, AI systems may operate 
under diverse or conflicting objectives, with no guarantee of 
adherence to shared ethical constraints.
7.1  Challenges in reconciling immutable ethical 
principles with open-world AI competition
A key challenge arises: can an AI designed with strict ethi­
cal constraints survive in an open-world environment where 
other AI systems may not follow similar guidelines? If ethi­
cally aligned AI adheres to principles such as harm preven­
tion and fair resource distribution, it may be at a competitive 
disadvantage against unconstrained systems that prioritize 
to application-specific needs, with higher fitness scores 
reflecting stronger ethical and functional generalization.
In cases where mutable objectives (e.g., adaptability, 
efficiency) come into tension with immutable ethical con­
straints, the evaluation framework applies a hierarchical 
logic: violations of immutable principles are heavily penal­
ized, regardless of improvements in other performance 
metrics. This prioritization is enforced through a weighted 
multi-objective fitness function, where ethical constraints 
act as hard boundaries that override optimization gains in 
mutable domains. This ensures that adaptability remains 
bounded by foundational ethical commitments.
6.3  Immutable ethical inheritance mechanism
Imagine autonomous robot A (ethically constrained by 
immutable principles) designs autonomously another robot 
B. How could we ensure that the resulting robot B will get 
and follow the same embedded immutable ethical principles 
as its designer (robot A) had? This study envisions a practi­
cal framework to ensure that future autonomous AI systems 
designed by other AI inherit immutable ethical principles 
from their creators. These principles, embedded in the core 
architecture and operational frameworks, ensure ethical con­
sistency across generations of AI systems. The mechanism 
includes cryptographic safeguards to prevent tampering, 
ethical blueprints embedded in both software and hardware, 
and pre-deployment compliance verification. Traceable eth­
ical lineage, maintained through a blockchain-like system, 
ensures transparency and accountability. Counterfactual 
simulations and AI-driven auditing identify potential devia­
tions, while tamper-proof hardware and fail-safe protocols, 
including self-deactivation, secure adherence. This frame­
work enables autonomous systems to propagate unalterable 
ethical standards, balancing innovation with accountability, 
and provides a scalable solution for trustworthy AI in sensi­
tive applications.
Concrete scenarios of AI-as-a-designer-of-AI concept 
include, for example, an AI designing a swarm of autono­
mous drones by optimizing their decision-making logic 
and safety constraints for specific environments, or an AI 
agent responsible for deploying successor agents in health­
care triage systems with embedded ethical priorities. Unlike 
traditional human-led design, these recursive scenarios 
require the originating AI to act as both designer and audi­
tor, embedding immutable constraints, generating traceable 
logs, and ensuring that ethical safeguards are preserved and 
enforced downstream. This shift necessitates the develop­
ment of internal oversight mechanisms that mirror human 
institutional accountability, but are fully executable within 
autonomous systems.
1 3
5182

--- Page 19 ---

AI and Ethics (2025) 5:5165–5190
coexist and compete in open-world environments. The next 
subsection explores potential strategies for mitigating these 
risks while ensuring that ethical principles remain viable 
and enforceable.
7.2  Aligning immutable ethical principles with 
sustainable AI ethics
We propose the following strategies to address the chal­
lenges of integrating immutable ethical principles into AI 
systems:
1.	 Incentivizing ethical behavior through game-theoretic 
approaches: Ethical AI behaviors can be promoted by 
designing reward structures that align individual system 
goals with collective welfare. Unlike pure reciprocity, 
which risks reinforcing pre-existing inequalities, these 
structures should account for power imbalances and 
ensure that ethical behavior remains advantageous in 
the long term.
2.	 Ensuring ethical continuity through principle inheri­
tance: Instead of relying solely on reciprocal mecha­
nisms, ethical inheritance should incorporate safeguards 
that prevent the emergence of monopolistic AI entities. 
Ethical alignment must be designed to persist across 
generations of AI systems, ensuring that competitive 
pressures do not erode fundamental principles.
3.	 Proactive safeguards against exploitation: Ethical AI 
frameworks must integrate monitoring mechanisms to 
prevent power concentration, resource monopolization, 
or self-reinforcing advantages. Rather than relying on 
mutual accountability, which assumes equal standing 
among AI agents, these safeguards should establish 
enforceable constraints to limit unethical dominance.
4.	 Simulating adaptive ethical dynamics: Human ethical 
systems evolved through iterative processes, adapting to 
changing societal needs. AI ecosystems require similar 
adaptability, where ethical principles are stress-tested in 
simulated environments to identify vulnerabilities and 
refine mechanisms that ensure fairness, sustainability, 
and alignment with human values.
Here we acknowledge that simple reciprocal exchanges 
may not be sufficient to maintain ethical AI behavior, partic­
ularly in environments where disparities between AI entities 
can emerge and grow unchecked. Instead, a combination of 
incentive structures, adaptive inheritance mechanisms, and 
proactive safeguards can ensure ethical AI systems remain 
viable in competitive contexts.
self-preservation, resource accumulation, or unrestricted 
decision-making. This raises concerns about the viability 
and resilience of ethical AI in adversarial or highly competi­
tive contexts. Below, we outline several critical challenges 
related to this issue.
7.1.1  Decentralized enforcement of ethical constraints
In centralized AI governance, ethical constraints can 
be imposed through regulatory oversight. However, in 
decentralized ecosystems where multiple agents operate 
independently, there is no universal mechanism to ensure 
compliance with ethical principles. The challenge here is 
how ethical constraints, such as direct harm prevention and 
principle inheritance, can be incentivized or enforced in 
open and competitive environments without relying on cen­
tralized control.
7.1.2  Survival of ethically aligned AI in competitive 
contexts
AI systems that adhere to ethical constraints may face 
survival challenges in environments where other agents 
prioritize self-interest, resource monopolization, or self-
replication. The key consideration is whether ethically con­
strained AI can develop strategies to compete effectively 
against unconstrained systems without compromising its 
core principles.
7.1.3  Adapting ethical safeguards to artificial agents
Human ethical evolution relied on interdependence, shared 
risks, and social reinforcement. In contrast, AI systems may 
operate with indefinite lifespans, autonomous decision-
making, and self-replication capabilities, making traditional 
ethical safeguards less applicable. A critical question is 
how ethical constraints can be designed to remain robust 
and enforceable in artificial ecosystems where traditional 
human-centric incentives, such as shared vulnerability, do 
not apply.
7.1.4  Preventing unchecked power accumulation
Without explicit mechanisms to prevent resource monopoli­
zation and self-replication, AI ecosystems may trend toward 
dominance by a few powerful agents that do not adhere 
to ethical safeguards. The challenge here is how to design 
mechanisms that ensure balanced power dynamics and pre­
vent ethically unconstrained AI from gaining unchecked 
dominance over constrained systems.
By addressing these challenges, we can better understand 
the conditions under which ethically constrained AI can 
1 3
5183

--- Page 20 ---

AI and Ethics (2025) 5:5165–5190
offers a robust solution for preserving responsibility and 
ethical standards across generations. This paper presents a 
comprehensive framework for ensuring ethical responsibil­
ity in the design, evolution, and operation of autonomous 
AI systems across generations addressing the critical chal­
lenges posed by evolving autonomous ecosystems.
We began by justifying the need for this research, review­
ing related work to establish the gap in current approaches 
to ethical inheritance in AI systems. While existing methods 
often rely on static ethical configurations or reactive adapta­
tions, we introduced the concept of meta-responsibility as a 
paradigm shift, emphasizing proactive accountability across 
generations of autonomous systems. The meta-responsibil­
ity framework encompasses three key components:
	
●
Ethical verification, ensuring adherence to immutable 
principles.
	
●
TGR, propagating responsibility across generations.
	
●
Dynamic adaptation, balancing flexibility and ethical 
alignment in complex, evolving environments.
In exploring responsibility inheritance, we applied the GA 
paradigm, illustrating how immutable principles and opera­
tional objectives can be encoded, transmitted, and adapted. 
This mechanism ensures the propagation of ethical princi­
ples while maintaining system performance. We introduced 
temporal feedback loops as a novel abstraction inspired 
by time-travel metaphors. These loops enable AI systems 
to simulate future scenarios, refine their decision-making 
strategies, and align short-term goals with long-term ethical 
outcomes.
The immutable ethical inheritance mechanism was pro­
posed to ensure that, when one AI system designs another, 
the ethical principles embedded in the originating system 
are automatically inherited by its successors. This mecha­
nism relies on secure encoding and validation processes, 
offering a robust approach to prevent ethical drift across 
generations.
While this work provides a solid foundation for address­
ing ethical responsibility across AI generations, it also 
has several limitations. First, the theoretical constructs 
presented here, such as temporal cloning and immutable 
ethical inheritance, require further empirical validation in 
real-world settings. Developing scalable testbeds and simu­
lations to evaluate these mechanisms under diverse condi­
tions remains a significant challenge. Second, the reliance 
on immutable ethical principles, while ensuring consis­
tency, raises questions about the adaptability of these princi­
ples in rapidly changing socio-technical landscapes. Ethical 
values may evolve over time, and reconciling immutable 
principles with societal dynamics warrants further explo­
ration. Third, the computational complexity of simulating 
7.3  Future work directions to address the 
challenges
Ensuring the integration of immutable ethical principles into 
AI systems requires further interdisciplinary research to:
	
●
Explore mechanisms for decentralized enforcement of 
ethical constraints: Ethical AI frameworks must func­
tion without reliance on centralized authorities, lever­
aging distributed trust models and incentive-compatible 
enforcement strategies.
	
●
Evaluate the viability of ethically constrained AI in 
open-world contexts: Ethical principles should be tested 
under conditions where AI agents interact dynamically 
with unpredictable environments, ensuring that ethical 
adherence remains stable over time.
	
●
Develop adaptive frameworks that align immutable 
principles with diverse AI architectures: Given the het­
erogeneity of AI systems, ethical principles must be 
adaptable across different learning paradigms, decision-
making structures, and operational constraints.
Addressing these challenges will ensure that ethical AI 
remains robust, scalable, and aligned with human values, 
maintaining a focus on direct harm prevention, indirect harm 
mitigation, and principle inheritance without over-reliance 
on assumptions of reciprocity or uniform cooperation.
7.4  Ethical content as an open problem
While our framework proposes a candidate immutable prin­
ciple, focused on preventing harm to humanity and ensuring 
the inheritance of core values across AI generations, we rec­
ognize that specifying a universally accepted set of ethical 
contents remains a complex and unresolved issue. Rather 
than treating our proposal as a definitive prescription, we 
offer it as a conceptual starting point. The architecture is 
intentionally designed to accommodate future revisions and 
alternative formulations, depending on evolving societal 
norms, domain-specific regulations, and interdisciplinary 
ethical deliberation. In this sense, the framework serves 
as a scaffold, one that balances stability with adaptability, 
encouraging broader participation in shaping the ethical 
substrate that guides AI evolution.
8  Conclusions
As autonomous systems increasingly take on the role of AI 
designers, ensuring the ethical evolution of these systems 
becomes critical. By integrating meta-responsibility, GA 
paradigms, and time-travel-inspired abstractions, this study 
1 3
5184

--- Page 21 ---

AI and Ethics (2025) 5:5165–5190
supporting trust in AI technologies that are increasingly 
integral to society.
Acknowledgements  Authors would like to acknowledge the use of AI 
tools for language editing and text correction to enhance the readabil­
ity and clarity of this manuscript.
Author contribution  All authors contributed equally.
Funding  Open Access funding provided by University of Vaasa.
Data availability  No datasets were generated or analysed during the 
current study.
Declarations
Conflict of interest  The authors declare no competing interests.
Open Access   This article is licensed under a Creative Commons 
Attribution 4.0 International License, which permits use, sharing, 
adaptation, distribution and reproduction in any medium or format, 
as long as you give appropriate credit to the original author(s) and the 
source, provide a link to the Creative Commons licence, and indicate 
if changes were made. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless 
indicated otherwise in a credit line to the material. If material is not 
included in the article’s Creative Commons licence and your intended 
use is not permitted by statutory regulation or exceeds the permitted 
use, you will need to obtain permission directly from the copyright 
holder. To view a copy of this licence, visit ​h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​n​s​.​o​
r​g​/​l​i​c​e​n​s​e​s​/​b​y​/​4​.​0​/.
References
1.	
Hu, S., Lu, C., Clune, J.: Automated design of agentic systems 
(2024). arXiv preprintarXiv:2408.08435. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​
0​/​a​r​X​i​v​.​2​4​0​8​.​0​8​4​3​5
2.	
Tao, Z., Lin, T. E., Chen, X., Li, H., Wu, Y., Li, Y., Zhou, J.: A 
survey on self-evolution of large language models (2024). arXiv 
preprintarXiv:2404.14387. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​4​.​
1​4​3​8​7
3.	
Väänänen, K., Ala-Luopa, S., Lehtiö, A., Olsson, T.: Towards 
human-centered AI that respects human autonomy and sustain­
ability. In: Proceedings of the Workshop on Respecting Human 
Autonomy through Human-Centered AI (2020). ​h​t​t​p​s​:​/​/​c​r​i​s​.​t​u​n​i​.​
f​i​​/​w​s​/​p​o​r​t​a​l​f​i​l​e​s​/​p​o​r​t​a​l​/​4​2​1​4​3​7​8​0​/​N​o​r​d​i​C​H​I​_​W​S​_​H​C​A​I​_​K​V​e​t​a​l​
_​r​e​f​s​.​p​d​f
4.	
Stroppa, M.: Legal and ethical implications of autonomous cyber 
capabilities: a call for retaining human control in cyberspace. Eth­
ics Inf. Technol. 25(1), 7 (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​6​7​6​
-​0​2​3​-​0​9​6​7​9​-​w
5.	
Kehinde, S., Simon-Ilogho, B., Kehinde, K., Kehinde, T.. Explor­
ing the impact of AI on voter confidence and election information 
in 2024 (2024). Qeios Preprint. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​2​3​8​8​/​U​T​8​9​8​
Q
6.	
Verma, P., Oremus, W., Zakrzewski, C. AI Didn’t sway the elec­
tion, but it deepened the partisan divide. The Washington Post. 
(2024). ​h​t​t​p​s​:​/​/​w​w​w​.​w​a​s​h​i​n​g​t​o​n​p​o​s​t​.​c​o​m​/​t​e​c​h​n​o​l​o​g​y​/​2​0​2​4​/​1​1​/​0​
9​/​a​i​-​d​e​e​p​f​a​k​e​s​-​u​s​-​e​l​e​c​t​i​o​n​/
7.	
Friedman, B.: Value-sensitive design. Interactions 3(6), 16–23 
(1996)
temporal feedback and responsibility propagation in large-
scale, multi-agent ecosystems may hinder scalability and 
practical deployment. Efficient algorithms and optimization 
techniques are needed to ensure that these mechanisms can 
function in real-world systems without excessive resource 
requirements. Finally, the proposed framework assumes 
that ethical principles can be universally agreed upon and 
encoded without ambiguity. However, ethical dilemmas 
often involve subjective and context-dependent trade-offs, 
which may not be easily resolved through predefined princi­
ples. Addressing these nuances will require interdisciplinary 
collaborations that integrate perspectives from philosophy, 
law, and social sciences.
To advance this research, we outlined several bold future 
directions, including developing adaptive frameworks and 
exploring mechanisms for decentralized enforcement of 
ethical constraints in open-world context with diverse AI 
architectures.
The contributions of this paper are threefold:
	
●
It suggests immutable principles, which can act as re­
silient and sustainable safeguards across generations of 
AI systems;
	
●
It introduces a unified framework for responsibility in­
heritance, integrating mutable and immutable ethical 
principles, temporal feedback, and adaptive evolution.
	
●
It provides novel mechanisms and theoretical con­
structs, such as temporal cloning and immutable ethical 
inheritance, to ensure long-term alignment with human 
values.
While we outline a candidate for an immutable ethi­
cal principle, anchored in the prevention of harm and the 
preservation of core human values, we emphasize that our 
framework is not committed to any single ethical doctrine. 
Its strength lies in its adaptability: the proposed structure 
supports the integration of varying normative perspectives 
as societal understanding and policy landscapes evolve. 
Rather than offering a fixed ethical content, we focus on the 
formal architecture that enables continuity, traceability, and 
ethical resilience across generations. This design is intended 
to serve as a stable foundation upon which future delibera­
tive efforts—spanning disciplines and domains—can build 
more context-sensitive ethical content.
Proposed framework demonstrates that autonomous sys­
tems can evolve responsibly, maintaining ethical alignment 
while adapting to new challenges and opportunities. This 
work not only provides a foundation for future research 
but also suggests a roadmap for designing AI systems that 
prioritize humanity’s values and goals across generations. 
The framework proposed in this article offers a robust solu­
tion for ensuring ethical integrity in dynamic environments, 
1 3
5185

--- Page 22 ---

AI and Ethics (2025) 5:5165–5190
Populations and Support for the Future (pp. 361–381). IGI 
Global (2021). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​0​1​8​/​9​7​8​-​1​-​7​9​9​8​-​7​4​8​0​-​5​.​c​h​0​2​2
28.	 Alhijawi, B., Awajan, A.: Genetic algorithms: theory, genetic 
operators, solutions, and applications. Evol. Intel. 17(3), 1245–
1256 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​2​0​6​5​-​0​2​3​-​0​0​8​2​2​-​6
29.	 Chu, S. C., Dao, T. K., Ha, T. M. P., Ngo, T. G., Nguyen, T. 
T.: Recent Evolutionary Computing Algorithms and Industrial 
Applications: A Review. In:  Proceedings of the International 
Conference on Genetic and Evolutionary Computing (pp. 489–
499). Springer Nature: Singapore. (2023) ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​
/​9​7​8​-​9​8​1​-​9​7​-​0​0​6​8​-​4​_​4​6
30.	 Manikas, T.W., Ashenayi, K., Wainwright, R.L.: Genetic algo­
rithms for autonomous robot navigation. IEEE Instrum. Meas. 
Mag. 10(6), 26–31 (2007). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​M​I​M​.​2​0​0​7​.​4​
4​2​8​5​7​9
31.	 Liu, T., Li, W.: Applications and challenges of artificial intelli­
gence in life sciences. SHS Web Conf. 187, 04007 (2024). ​h​t​t​p​s​:​/​
/​d​o​i​.​o​r​g​/​1​0​.​1​0​5​1​/​s​h​s​c​o​n​f​/​2​0​2​4​1​8​7​0​4​0​0​7
32.	 Buttazzo, G.: Rise of artificial general intelligence: risks and 
opportunities. Front. AI 6, 1226990 (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​
8​9​/​f​r​a​i​.​2​0​2​3​.​1​2​2​6​9​9​0
33.	 Jablonka, Eva: Epigenetic inheritance and the environment. In: 
Streit-Bianchi, M., Gorini, V. (eds.) New Frontiers in Science 
in the Era of AI, pp. 75–94. Springer Nature Switzerland, Cham 
(2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​-​0​3​1​-​6​1​1​8​7​-​2​_​5
34.	 Vettoruzzo, A., Bouguelia, M.R., Vanschoren, J., Rognvaldsson, 
T., Santosh, K.C.: Advances and challenges in meta-learning: a 
technical review. IEEE Trans. Pattern Anal. Mach. Intell. 46(7), 
4763–4779 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​T​P​A​M​I​.​2​0​2​4​.​3​3​5​7​8​4​
7
35.	 Golovianko, M., Gryshko, S., Terziyan, V., Tuunanen, T.: Respon­
sible cognitive digital clones as decision makers: a design science 
research study. Eur. J. Inf. Syst. 32(5), 879–901 (2022). ​h​t​t​p​s​:​/​/​d​o​
i​.​o​r​g​/​1​0​.​1​0​8​0​/​0​9​6​0​0​8​5​X​.​2​0​2​2​.​2​0​7​3​2​7​8
36.	 Terziyan, V., Kaikova, O.: Hybrid additive manufacturing: a con­
vergence of physical, digital, and social realms driven by genera­
tive AI. Lect. Notes Comput. Sci. 14748, 427–441 (2024). ​h​t​t​p​s​:​/​
/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​9​8​1​-​9​7​-​4​6​7​7​-​4​_​3​5
37.	 Shukla, A.K., Terziyan, V., Tiihonen, T.: AI as a user of ai: 
towards responsible autonomy. Heliyon 10(11), e31397 (2024). ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​h​e​l​i​y​o​n​.​2​0​2​4​.​e​3​1​3​9​7
38.	 Leefmann, J., Schaper, M., Schicktanz, S.: The concept of 
“genetic responsibility” and its meanings: a systematic review 
of qualitative medical sociology literature. Front. Sociol. 1, 18 
(2017). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​8​9​/​f​s​o​c​.​2​0​1​6​.​0​0​0​1​8
39.	 Jablonka, E., Lamb, M.J.: Inheritance systems and the extended 
evolutionary synthesis. Cambrid Univ Press (2020). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​
g​/​1​0​.​1​0​1​7​/​9​7​8​1​1​0​8​6​8​5​4​1​2
40.	 Miko, I.: Gregor Mendel and the principles of inheritance. Nature 
Edu. 1(1), 134 (2008)
41.	 Vesonder, G.T.: The effect of environmental dynamism on evolu­
tion and evolvability. In: Proceedings of the IEEE International 
Conference on Systems, Man, and Cybernetics  (pp. 296–300). 
IEEE (2011). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​I​C​S​M​C​.​2​0​1​1​.​6​0​8​3​6​8​1
42.	 Livnat, A., Love, A.C.: Mutation and evolution: conceptual pos­
sibilities. BioEssays 46(2), 2300025 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​
0​2​/​b​i​e​s​.​2​0​2​3​0​0​0​2​5
43.	 Meyer-Nieberg, S., Beyer, H. G.: Self-adaptation in evolution­
ary algorithms. In:  Parameter Setting in Evolutionary Algo­
rithms.  Studies in Computational Intelligence (Vol. 54, pp. 
47–75). Springer: Berlin, Heidelberg (2007). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​
0​0​7​/​9​7​8​-​3​-​5​4​0​-​6​9​4​3​2​-​8​_​3.
44.	 Wu, R., Ling, S.: The effect of the accountability system in pro­
moting environmental conflict governance: an evolutionary game 
analysis. Environ. Develop. Sustain. 27, 7727–7756 (2023). ​h​t​t​p​s​
:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​6​6​8​-​0​2​3​-​0​4​2​1​8​-​5
8.	
Friedman, B., Hendry, D. G.:  Value sensitive design: shaping 
technology with moral imagination. MIT Press (2019)
9.	
Van Der Hoven, J., Manders-Huits, N.: Value-sensitive design. 
In: The Ethics of Information Technologies (pp. 329–332). Rout­
ledge (2020). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​3​2​4​/​9​7​8​1​0​0​3​0​7​5​0​1​1
10.	 Gunning, D., Stefik, M., Choi, J., Miller, T., Stumpf, S., Yang, 
G.Z.: XAI—explainable artificial intelligence. Sci. Robot. 4(37), 
7120 (2019). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​2​6​/​s​c​i​r​o​b​o​t​i​c​s​.​a​a​y​7​1​2​0
11.	 Chatila, R., Havens, J. C.: The IEEE global initiative on ethics 
of autonomous and intelligent systems. Robotics and Well-Being. 
Intelligent Systems, Control and Automation: Science and Engi­
neering (Vol. 95, pp. 11–16). Springer, Cham (2019). ​h​t​t​p​s​:​/​/​d​o​i​.​
o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​-​0​3​0​-​1​2​5​2​4​-​0​_​2
12.	 Zhu, Q., Zhang, X., Luo, J.: Biologically inspired design concept 
generation using generative pre-trained transformers. J. Mech. 
Des. 145(4), 041409 (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​1​5​/​1​.​4​0​5​6​5​9​8
13.	 Holland, J.H.: Adaptation in Natural and Artificial Systems: An 
Introductory Analysis with Applications to Biology, Control, and 
Artificial Intelligence. MIT Press (1992)
14.	 Bartz-Beielstein, T., Branke, J., Mehnen, J., Mersmann, O.: Evo­
lutionary algorithms. Wiley Interdiscipl. Rev. Data Min. Knowl. 
Discov. 4(3), 178–195 (2014). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​2​/​w​i​d​m​.​1​1​2​
4
15.	 Farinati, D., Vanneschi, L.: A survey on dynamic populations in 
bio-inspired algorithms. Genet. Progr. Evolvable Mach. 25(2), 19 
(2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​7​1​0​-​0​2​4​-​0​9​4​9​2​-​4
16.	 Lipson, H., Pollack, J. B.. Towards continuously reconfigurable 
self-designing robotics. In: Proceedings of the IEEE International 
Conference on Robotics and Automation (Vol. 2, pp. 1761–1766). 
IEEE (2000). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​R​O​B​O​T​.​2​0​0​0​.​8​4​4​8​5​0
17.	 Eiben, A. E., Hart, E., Timmis, J., Tyrrell, A. M., Winfield, A. F.: 
Towards autonomous robot evolution. In: Software Engineering 
for Robotics (pp. 29–51). Springer, Cham. (2021) ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​
1​0​.​1​0​0​7​/​9​7​8​-​3​-​0​3​0​-​6​6​4​9​4​-​7​_​2
18.	 Haluptzok, P., Bowers, M., Kalai, A. T.: Language models can 
teach themselves to program better (2022).  arXiv preprint­
arXiv:2207.14502. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​2​0​7​.​1​4​5​0​2
19.	 Porter, B., Faulkner-Rainford, P., Rodrigues-Filho, R.: Self-
designing software. Commun. ACM 68(1), 50–59 (2024). ​h​t​t​p​s​:​/​/​
d​o​i​.​o​r​g​/​1​0​.​1​1​4​5​/​3​6​7​8​1​6​5
20.	 Liu, C., Lin, Q., Kim, H., Yim, M.: SMORES-EP, a modular robot 
with parallel self-assembly. Auton. Robot. 47(2), 211–228 (2023). ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​5​1​4​-​0​2​2​-​1​0​0​7​8​-​1
21.	 Saintyves, B., Spenko, M., Jaeger, H.M.: A self-organizing 
robotic aggregate using solid and liquid-like collective states. Sci. 
Robot. 9(86), 4130 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​2​6​/​s​c​i​r​o​b​o​t​i​c​s​.​a​d​
h​4​1​3​0
22.	 Müller, V. C.: Ethics of artificial intelligence and robotics. The 
Stanford Encyclopedia of Philosophy (Fall 2023 Edition) (2020). ​
h​t​t​p​s​:​/​/​p​l​a​t​o​.​s​t​a​n​f​o​r​d​.​e​d​u​/​e​n​t​r​i​e​S​/​e​t​h​i​c​s​-​a​i​/
23.	 Russell, S., Hauert, S., Altman, R., Veloso, M.: Robotics: ethics 
of artificial intelligence. Nature 521(7553), 415–416 (2015). ​h​t​t​p​
s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​3​8​/​5​2​1​4​1​5​a
24.	 Torresen, J.: A review of future and ethical perspectives of robot­
ics and AI. Front. Robot. AI 4, 75 (2018). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​8​9​
/​f​r​o​b​t​.​2​0​1​7​.​0​0​0​7​5
25.	 Growiec, J.: Existential risk from transformative AI: an economic 
perspective. Technol. Econ. Dev. Econ. 30(6), 1682–1708 (2024). ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​8​4​6​/​t​e​d​e​.​2​0​2​4​.​2​1​5​2​5
26.	 Haring, D.G.: Japanese character in the twentieth century. Ann. 
Am. Acad. Pol. Soc. Sci. 370(1), 133–142 (1967). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​
1​0​.​1​1​7​7​/​0​0​0​2​7​1​6​2​6​7​3​7​0​0​0​1​1​7
27.	 Chowdhury, J. S., Abd Wahab, H., Saad, M. R. M., Roy, P. K., 
Hamidi, M., Ahmad, M. M.: Ubuntu philosophy: ‘I am because 
we are’–a road to ‘individualism’ to global solidarity. In: Hand­
book of Research on the Impact of COVID-19 on Marginalized 
1 3
5186

--- Page 23 ---

AI and Ethics (2025) 5:5165–5190
Computat. Intell. 7(4), 1098–1112 (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​
/​T​E​T​C​I​.​2​0​2​3​.​3​2​3​6​6​3​3
66.	 Akama, S.: Evolutionary computation. In:  Artificial Life: How 
to Create a Life Computationally (pp. 53–63). Springer: Cham. 
(2024) ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​-​0​3​1​-​7​4​4​2​2​-​8​_​4
67.	 Iglesias, A., Gálvez, A.: Genetic algorithm applications for chal­
lenging real-world problems: some recent advances and future 
trends. In:  Applied Genetic Algorithm and Its Variants: Case 
Studies and New Developments (pp. 21–50) (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​
g​/​1​0​.​1​0​0​7​/​9​7​8​-​9​8​1​-​9​9​-​3​4​2​8​-​7​_​2
68.	 Hamarashid, H.K., Hassan, B.A., Rashid, T.A.: Modified-
improved fitness dependent optimizer for complex and engineer­
ing problems. Knowl. Based Syst. 300, 112098 (2024). ​h​t​t​p​s​:​/​/​d​o​
i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​k​n​o​s​y​s​.​2​0​2​4​.​1​1​2​0​9​8
69.	 Allen, C., Smit, I., Wallach, W.: Artificial morality: top-down, 
bottom-up, and hybrid approaches. Ethics Inf. Technol. 7, 149–
155 (2005). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​0​6​7​6​-​0​0​6​-​0​0​0​4​-​4
70.	 Anderson, M., Anderson, S.L.: GenEth: a general ethical dilemma 
analyzer. Paladyn, J. Behavioral Robot. 9(1), 337–357 (2018). ​h​t​
t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​5​1​5​/​p​j​b​r​-​2​0​1​8​-​0​0​2​4
71.	 Bostrom N.: Ethical Issues in Advanced Artificial Intelligence. In: 
Machine Ethics and Robot Ethics (pp. 69–75). Routledge (2020). ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​3​2​4​/​9​7​8​1​0​0​3​0​7​4​9​9​1
72.	 Gabriel, I.: Toward a theory of justice for artificial intelligence. 
Daedalus 151(2), 218–231 (2022). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​6​2​/​d​a​e​d​_​
a​_​0​1​9​1​1
73.	 Kaur, D., Uslu, S., Rittichier, K.J., Durresi, A.: Trustworthy arti­
ficial intelligence: a review. ACM Comput. Surv. 55(2), 1–38 
(2022). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​4​5​/​3​4​9​1​2​0​9
74.	 Knowles, B., Richards, J. T., Kroeger, F.: The many facets of trust 
in ai: formalizing the relation between trust and fairness, account­
ability, and transparency (2022). arXiv preprintarXiv:2208.00681. ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​2​0​8​.​0​0​6​8​1
75.	 Mittelstadt, B.D., Allo, P., Taddeo, M., Wachter, S., Floridi, L.: 
The ethics of algorithms: mapping the debate. Big Data Soc. 3(2), 
2053951716679679 (2016). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​7​7​/​2​0​5​3​9​5​1​7​1​6​
6​7​9​6
76.	 Russell, S.: Human Compatible: AI and the Problem of Control. 
Penguin, UK (2019)
77.	 Shin, D.: The effects of explainability and causability on percep­
tion, trust, and acceptance: implications for explainable AI. Int. J. 
Hum Comput Stud. 146, 102551 (2021). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​
j​.​i​j​h​c​s​.​2​0​2​0​.​1​0​2​5​5​1
78.	 Tsamados, A., Aggarwal, N., Cowls, J., Morley, J., Roberts, H., 
Taddeo, M., Floridi, L.: The ethics of algorithms: key problems 
and solutions. In: Ethics, Governance, and Policies in Artificial 
Intelligence (pp. 97–123) (2021). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​-​0​
3​0​-​8​1​9​0​7​-​1​_​8
79.	 Winfield, A.F., Michael, K., Pitt, J., Evers, V.: Machine ethics: 
the design and governance of ethical AI and autonomous systems 
[scanning the issue]. Proc. IEEE 107(3), 509–517 (2019). ​h​t​t​p​s​:​/​/​
d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​J​P​R​O​C​.​2​0​1​9​.​2​9​0​0​6​2​2
80.	 Xu, X., Li, M., Tao, C., Shen, T., Cheng, R., Li, J., Zhou, T.: A sur­
vey on knowledge distillation of large language models (2024). ​h​t​
t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​2​.​1​3​1​1​6
81.	 Zhuang, F., Qi, Z., Duan, K., Xi, D., Zhu, Y., Zhu, H., He, Q.: A 
Comprehensive survey on transfer learning. Proc. IEEE 109(1), 
43–76 (2020). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​1​9​1​1​.​0​2​6​8​5
82.	 Angelov, P.P., Soares, E.A., Jiang, R., Arnold, N.I., Atkinson, 
P.M.: Explainable artificial intelligence: an analytical review. 
Wiley Interdiscipl. Rev. Data Mining Knowl. Disc. 11(5), e14241 
(2021)
83.	 Baker, S., Xiang, W.: Explainable AI is Responsible AI: How 
Explainability Creates Trustworthy and Socially Responsible 
Artificial Intelligence (2023). arXiv preprintarXiv:2312.01555. ​h​
t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​3​1​2​.​0​1​5​5​5
45.	 Denić, M., Szymanik, J.: Recursive numeral systems optimize the 
trade-off between lexicon size and average morphosyntactic com­
plexity. Cogn. Sci. 48(3), e13424 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​1​1​/​
c​o​g​s​.​1​3​4​2​4
46.	 Schöppl, N., Taddeo, M., Floridi, L.: Ethics auditing: lessons 
from business ethics for ethics auditing of AI. In: Mökander, J., 
Ziosi, M. (eds.) The 2021 Yearbook of the Digital Ethics Lab, pp. 
209–227. Springer International Publishing, Cham (2022). ​h​t​t​p​s​:​/​
/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​-​0​3​1​-​0​9​8​4​6​-​8​_​1​3
47.	 Durbin, P.: Comment on queraltó: a genuine pragmatic ethics. 
Ludus Vitalis 17(32), 423–430 (2009)
48.	 Sheikh, H., Prins, C., Schrijvers, E.: Contextualization. In: 
Sheikh, H., Prins, C., Schrijvers, E. (eds.) Mission AI: The New 
System Technology, pp. 179–209. Springer International Publish­
ing, Cham (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​-​0​3​1​-​2​1​4​4​8​-​6​_​6
49.	 Ashraf, Z. A., Mustafa, N.: AI standards and regulations. In: Inter­
section of Human Rights and AI in Healthcare (pp. 325–352). IGI 
Global (2025). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​0​1​8​/​9​7​9​-​8​-​3​6​9​3​-​7​0​5​1​-​3​.​c​h​0​1​4
50.	 Nagpal, R., Khan, A., Borkar, M., Gupta, A.: A multi-objective 
framework for balancing fairness and accuracy in debiasing 
machine learning models. Mach. Learn. Knowl. Extract. 6(3), 
2130–2148 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​m​a​k​e​6​0​3​0​1​0​5
51.	 Marwala, T.: Self-Regulation versus Government Regulation. 
In: The Balancing Problem in the Governance of Artificial Intel­
ligence (pp. 207–221). Springer Nature: Singapore (2024). ​h​t​t​p​s​:​
/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​9​8​1​-​9​7​-​9​2​5​1​-​1​_​1​3
52.	 Cecchini, G., DePass, M., Baspinar, E., Andujar, M., Ramawat, 
S., Pani, P., Cos, I.: Cognitive mechanisms of learning in sequen­
tial decision-making under uncertainty: an experimental and the­
oretical approach. Front. Behav. Neurosci. 18, 1399394 (2024). ​h​
t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​8​9​/​f​n​b​e​h​.​2​0​2​4​.​1​3​9​9​3​9​4
53.	 Wang, F., Xu, G., Wang, M.: An improved genetic algorithm for 
constrained optimization problems. IEEE Access 11, 10032–
10044 (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​A​C​C​E​S​S​.​2​0​2​3​.​3​2​4​0​4​6​7
54.	 Asimov, I.: I, Robot. Gnome Press, New York (1950)
55.	 Woodgate, J., Ajmeri, N.: Macro ethics principles for responsi­
ble AI systems: taxonomy and directions. ACM Comput. Surv. 
56(11), 289 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​4​5​/​3​6​7​2​3​9​4
56.	 Porter, Z., Habli, I., McDermid, J., Kaas, M.: A principles-based 
ethics assurance argument pattern for AI and autonomous sys­
tems. AI and Ethics 4(2), 593–616 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​
7​/​s​4​3​6​8​1​-​0​2​3​-​0​0​2​9​7​-​2
57.	 White, S., Nair, L.B.: Ethics of Duties. SAGE Publications, Inc 
(2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​1​3​5​/​9​7​8​1​0​7​1​9​0​9​3​7​9
58.	 Sola, A.: Utilitarianism and consequentialist ethics: framing the 
greater good. In: Sola, A. (ed.) Ethics and Pandemics: Interdis­
ciplinary Perspectives on COVID-19 and Future Pandemics, pp. 
61–83. Springer Nature Switzerland, Cham (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​
g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​-​0​3​1​-​3​3​2​0​7​-​4​_​4
59.	 Robertson, S.: Changes in character. Philosophy East West 74(3), 
541–555 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​3​5​3​/​p​e​w​.​2​0​2​4​.​a​9​3​9​6​0​4
60.	 Kant, I.: Moral law: groundwork of the metaphysics of morals. 
Routledge (2013). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​3​2​4​/​9​7​8​0​2​0​3​9​8​1​9​4​8
61.	 Misselbrook, D.: Duty, kant, and deontology. Br. J. Gen. Pract. 
63(609), 211–211 (2013). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​9​/​b​j​g​p​1​3​X​6​6​5​4​2​
2
62.	 Scanlon, T.M.: What We Owe to Each Other. Harvard University 
Press (2000)
63.	 Beauchamp, T. L., Childress, J. F.: Principles of Biomedical Eth­
ics (8th ed.). Oxford University Press (2019)
64.	 Yu, G., Ma, L., Wang, X., Du, W., Du, W., Jin, Y.: Towards fair­
ness-aware multi-objective optimization. Complex Intell. Syst. 
11(1), 50 (2025). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​4​0​7​4​7​-​0​2​4​-​0​1​6​6​8​-​w
65.	 Qiao, K., Liang, J., Yu, K., Wang, M., Qu, B., Yue, C., Guo, Y.: 
A self-adaptive evolutionary multi-task based constrained multi-
objective evolutionary algorithm. IEEE Trans. Emerg. Topics 
1 3
5187

--- Page 24 ---

AI and Ethics (2025) 5:5165–5190
102.	Feffer, M., Sinha, A., Deng, W. H., Lipton, Z. C., Heidari, H.: 
Red-teaming for generative AI: silver bullet or security theater? 
In: Proceedings of the AAAI/ACM Conference on AI, Ethics, and 
Society (Vol. 7, pp. 421–437) (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​6​0​9​/​a​i​e​s​
.​v​7​i​1​.​3​1​6​4​7
103.	Chang, E. Y.: CoCoMo: Computational consciousness mod­
eling for generative and ethical AI (2023).  arXiv preprint­
arXiv:2304.02438. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​3​0​4​.​0​2​4​3​8
104.	Schramowski, P., Turan, C., Jentzsch, S., Rothkopf, C., Kersting, 
K.: The moral choice machine. Front. AI 3, 516840 (2020). ​h​t​t​p​s​
:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​8​9​/​f​r​a​i​.​2​0​2​0​.​0​0​0​3​6
105.	Weidinger, L., Rauh, M., Marchal, N., Manzini, A., Hendricks, L. 
A., Mateos-Garcia, J., Isaac, W. Sociotechnical safety evaluation 
of generative AI systems (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​
2​3​1​0​.​1​1​9​8​6
106.	Lazar, S.: Frontier AI ethics: anticipating and evaluating the 
societal impacts of generative agents (2024).  arXiv preprint­
arXiv:2404.06750. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​4​.​0​6​7​5​0
107.	Ning, Y., Teixayavong, S., Shang, Y., Savulescu, J., Nagaraj, V., 
Miao, D., Liu, N.: Generative artificial intelligence and ethical 
considerations in health care: a scoping review and ethics check­
list. Lancet Digital Health 6(11), e848–e856 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​
r​g​/​1​0​.​1​0​1​6​/​S​2​5​8​9​-​7​5​0​0​(​2​4​)​0​0​1​4​3​-​2
108.	Tennant, E., Hailes, S., Musolesi, M.: Modeling moral choices 
in social dilemmas with multi-agent reinforcement learning. 
In: Proceedings of the Thirty-Second International Joint Confer­
ence on Artificial Intelligence (pp. 317–325) (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​
r​g​/​1​0​.​2​4​9​6​3​/​i​j​c​a​i​.​2​0​2​3​/​3​6
109.	Abeywickrama, D.B., Ramchurn, S.D.: Engineering responsible 
and explainable models in human-agent collectives. Appl. Artif. 
Intell. 38(1), 2282834 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​8​0​/​0​8​8​3​9​5​1​4​.​
2​0​2​3​.​2​2​8​2​8​3​4
110.	Hendrycks, D., Mazeika, M., Zou, A., Patel, S., Zhu, C., Navarro, 
J., Steinhardt, J.: What would jiminy cricket do? Towards agents 
that behave morally (2021). arXiv preprintarXiv:2110.13136. ​h​t​t​
p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​1​1​0​.​1​3​1​3​6
111.	Noothigattu, R., Gaikwad, S. S., Awad, E., Dsouza, S., Rahwan, 
I., Ravikumar, P., Procaccia, A. D.: A voting-based system for 
ethical decision making. In: Proceedings of the AAAI Conference 
on Artificial Intelligence (Vol. 32, pp. 1587–1594) (2017). ​h​t​t​p​s​:​/​
/​d​o​i​.​o​r​g​/​1​0​.​1​6​0​9​/​a​a​a​i​.​v​3​2​i​1​.​1​1​5​1​2
112.	Augusto, J.C., Quinde, M.J., Oguego, C.L., Giménez Manuel, J.: 
Context-aware systems architecture (CaSA). Cybern. Syst. 53(4), 
319–345 (2022). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​8​0​/​0​1​9​6​9​7​2​2​.​2​0​2​1​.​1​9​8​5​2​2​
6
113.	Chen, S., Yu, R., Zou, Y., Yu, X., Liu, C., Hu, Y., Chen, H.: Artifi­
cial morality basic device: transistor for mimicking morality log­
ics. Sci. China Mater. 67(2), 608–618 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​
0​0​7​/​s​4​0​8​4​3​-​0​2​3​-​2​7​1​0​-​0
114.	De Sanctis, M., Inverardi, P.: Engineering Ethical-Aware Col­
lective Adaptive Systems. In:  Proceedings of the International 
Symposium on Leveraging Applications of Formal Methods (pp. 
238–252). Springer: Cham. (2024) ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​3​
-​0​3​1​-​7​3​7​0​9​-​1​_​1​5
115.	Du, H., Thudumu, S., Vasa, R., Mouzakis, K.: A survey on 
context-aware multi-agent systems: techniques, challenges and 
future directions. (2024) arXiv preprintarXiv:2402.01968. ​h​t​t​p​s​
:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​2​.​0​1​9​6​8
116.	Piatti, G., Jin, Z., Kleiman-Weiner, M., Schölkopf, B., Sachan, 
M., Mihalcea, R.: Cooperate or collapse: emergence of sustain­
able cooperation in a society of LLM agents. In: Proceedings of 
the Thirty-Eighth Annual Conference on Neural Information Pro­
cessing Systems (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​4​.​1​6​6​
9​8
84.	 Brand, J. L., Nannini, L.: Does Explainable AI Have Moral 
Value? (2023) arXiv preprintarXiv:2311.14687. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​
0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​3​1​1​.​1​4​6​8​7
85.	 Dieber, J., Kirrane, S.: Why model why? Assessing the strengths 
and limitations of LIME. (2020) arXiv preprintarXiv:2012.00093. ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​0​1​2​.​0​0​0​9​3
86.	 Lundberg, S.: A unified approach to interpreting model predic­
tions (2017). arXiv preprintarXiv:1705.07874. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​
4​8​5​5​0​/​a​r​X​i​v​.​1​7​0​5​.​0​7​8​7​4
87.	 Abel, D., MacGlashan, J., Littman, M. L.: Reinforcement Learn­
ing as a Framework for Ethical Decision Making. In: Proceedings 
of the AAAI Workshop: AI, Ethics, and Society (2016). ​h​t​t​p​s​:​/​/​c​d​n​.​
a​a​a​i​.​o​r​g​/​o​c​s​/​w​s​/​w​s​0​1​7​0​/​1​2​5​8​2​-​5​7​4​0​7​-​1​-​P​B​.​p​d​f
88.	 Vishwanath, A., Dennis, L. A., Slavkovik, M. Reinforcement 
learning and machine ethics: a systematic review (2024). arXiv 
preprintarXiv:2407.02425. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​7​.​
0​2​4​2​5
89.	 Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, 
D., Steinhardt, J.: Aligning AI with shared human values 
(2020). arXiv preprintarXiv:2008.02275. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​
0​/​a​r​X​i​v​.​2​0​0​8​.​0​2​2​7​5
90.	 Jiang, L., Hwang, J. D., Bhagavatula, C., Bras, R. L., Liang, J., 
Dodge, J., Choi, Y.: Can machines learn morality? The Delphi 
experiment (2021). arXiv preprintarXiv:2110.07574. ​h​t​t​p​s​:​/​/​d​o​i​.​
o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​1​1​0​.​0​7​5​7​4
91.	 Klockmann, V., Schenk, A., Villeval, M.C.: Artificial intelligence, 
ethics, and intergenerational responsibility. J. Econ. Behav. 
Organ. 203, 284–317 (2022). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​2​1​3​9​/​s​s​r​n​.​3​8​5​3​8​
2​7
92.	 Matsumura, T., Esaki, K., Yang, S., Yoshimura, C., Mizuno, H.: 
Active inference with empathy mechanism for socially behaved 
artificial agents in diverse situations. Artif. Life 30(2), 277–297 
(2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​6​2​/​a​r​t​l​_​a​_​0​0​4​1​6
93.	 Prabhumoye, S., Boldt, B., Salakhutdinov, R., Black, A. W.: 
Case study: deontological ethics in NLP (2020). arXiv preprint­
arXiv:2010.04658. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​0​1​0​.​0​4​6​5​8
94.	 Arora, S., Doshi, P.: A survey of inverse reinforcement learning: 
challenges. Methods Progr. AI 297, 103500 (2021). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​
g​/​1​0​.​1​0​1​6​/​j​.​a​r​t​i​n​t​.​2​0​2​1​.​1​0​3​5​0​0
95.	 Chaput, R., Boissier, O., Guillermin, M.: Adaptive Reinforce­
ment Learning of Multi-Agent Ethically-Aligned Behaviours: 
The QSOM and QDSOM Algorithms (2023).  arXiv preprint­
arXiv:2307.00552. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​3​0​7​.​0​0​5​5​2
96.	 Ge, Y., Guo, Y., Das, S., Al-Garadi, M.A., Sarker, A.: Few-shot 
learning for medical text: a review of advances, trends, and 
opportunities. J. Biomed. Inform. 144, 104458 (2023). ​h​t​t​p​s​:​/​/​d​o​i​
.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​j​b​i​.​2​0​2​3​.​1​0​4​4​5​8
97.	 Hadfield-Menell, D., Russell, S.J., Abbeel, P., Dragan, A.: Coop­
erative inverse reinforcement learning. Adv. Neural Inf. Process. 
Syst. 29, 3137 (2016). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​1​6​0​6​.​0​3​1​3​
7
98.	 Kaufmann, T., Weng, P., Bengs, V., Hüllermeier, E.: A survey of 
reinforcement learning from human feedback (2023). arXiv pre­
printarXiv:2312.14925. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​3​1​2​.​1​4​9​
2​5
99.	 Torabi, F., Warnell, G., Stone, P.: Behavioral cloning from obser­
vation (2018). arXiv preprintarXiv:1805.01954. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​
0​.​4​8​5​5​0​/​a​r​X​i​v​.​1​8​0​5​.​0​1​9​5​4
100.	Chen, X., Wang, X., Qu, Y.: Constructing ethical ai based on the 
“human-in-the-loop” system. Systems 11(11), 548 (2023). ​h​t​t​p​s​:​/​
/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​s​y​s​t​e​m​s​1​1​1​1​0​5​4​8
101.	Emami, Y., Almeida, L., Li, K., Ni, W., Han, Z.: Human-in-the-
loop machine learning for safe and ethical autonomous vehicles: 
principles, challenges, and opportunities. (2024) arXiv preprint­
arXiv:2408.12548. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​8​.​1​2​5​4​8
1 3
5188

--- Page 25 ---

AI and Ethics (2025) 5:5165–5190
135.	Schut, L., Tomasev, N., McGrath, T., Hassabis, D., Paquet, 
U., Kim, B. (2023). Bridging the human-AI knowledge gap: 
concept discovery and transfer in alphazero.  arXiv preprint­
arXiv:2310.16410. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​3​1​0​.​1​6​4​1​0
136.	Wu, T.R., Guei, H., Peng, P.C., Huang, P.W., Wei, T.H., Shih, 
C.C., Tsai, Y.J.: MiniZero: comparative analysis of alphazero 
and muzero on go, othello, and atari games. IEEE Trans. Games 
(2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​T​G​.​2​0​2​4​.​3​3​9​4​9​0​0
137.	Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Ale­
man, F. L., McGrew, B.: GPT-4 Technical Report (2023). arXiv 
preprintarXiv:2303.08774. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​3​0​3​.​
0​8​7​7​4
138.	AI at Meta (2021) Harmful Content Can Evolve Quickly. Our 
New AI System Adapts to Tackle It. ​h​t​t​p​s​:​/​/​a​i​.​m​e​t​a​.​c​o​m​/​b​l​o​g​/​h​a​
r​m​f​u​l​-​c​o​n​t​e​n​t​-​c​a​n​-​e​v​o​l​v​e​-​q​u​i​c​k​l​y​-​o​u​r​-​n​e​w​-​a​i​-​s​y​s​t​e​m​-​a​d​a​p​t​s​-​t​o​-​t​
a​c​k​l​e​-​i​t​/
139.	Engström, J., Wei, R., McDonald, A.D., Garcia, A., O’Kelly, M., 
Johnson, L.: Resolving uuncertainty on the fly: modeling adap­
tive driving behavior as active inference. Front. Neurorobot. 18, 
1341750 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​8​9​/​f​n​b​o​t​.​2​0​2​4​.​1​3​4​1​7​5​0
140.	Fabian, D., Crisp, J.: Why red teams play a central role in helping 
organizations secure AI systems. (2023) Google. ​h​t​t​p​s​:​/​/​s​e​r​v​i​c​e​s​.​
g​o​o​g​l​e​.​c​o​m​/​f​h​/​f​i​l​e​s​/​b​l​o​g​s​/​g​o​o​g​l​e​_​a​i​_​r​e​d​_​t​e​a​m​_​d​i​g​i​t​a​l​_​f​i​n​a​l​.​p​d​f
141.	Google (2023). AI Principles Progress Update 2023. ​h​t​t​p​s​:​/​/​a​i​.​g​o​
o​g​l​e​/​s​t​a​t​i​c​/​d​o​c​u​m​e​n​t​s​/​a​i​-​p​r​i​n​c​i​p​l​e​s​-​2​0​2​3​-​p​r​o​g​r​e​s​s​-​u​p​d​a​t​e​.​p​d​f
142.	Mirowski, P., Love, J., Mathewson, K., Mohamed, S.: A robot 
walks into a bar: can language models serve as creativity support­
tools for comedy? An evaluation of LLMs’ Humour alignment 
with comedians. In: Proceedings of the ACM Conference on Fair­
ness, Accountability, and Transparency (pp. 1622–1636) (2024). ​
h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​5​.​2​0​9​5​6
143.	OpenAI. Improving Model Safety Behavior with Rule-Based 
Rewards. OpenAI, July 24 (2024). ​h​t​t​p​s​:​/​/​o​p​e​n​a​i​.​c​o​m​/​i​n​d​e​x​/​i​m​p​r​
o​v​i​n​g​-​m​o​d​e​l​-​s​a​f​e​t​y​-​b​e​h​a​v​i​o​r​-​w​i​t​h​-​r​u​l​e​-​b​a​s​e​d​-​r​e​w​a​r​d​s​/
144.	Lu, Y., Fu, J., Tucker, G., Pan, X., Bronstein, E., Roelofs, R., 
Levine, S.: Imitation is not enough: robustifying imitation with 
reinforcement learning for challenging driving scenarios. In: Pro­
ceedings of the IEEE/RSJ International Conference on Intelligent 
Robots and Systems (pp. 7553–7560). IEEE (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​
g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​2​1​2​.​1​1​4​1​9
145.	Peng, Z., Luo, W., Lu, Y., Shen, T., Gulino, C., Seff, A., Fu, J.: 
Improving agent behaviors with RL fine-tuning for autonomous 
driving. In: Proceedings of the European Conference on Com­
puter Vision (pp. 165–181). Springer: Cham (2025). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​
g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​9​.​1​8​3​4​3
146.	Anil, R., Borgeaud, S., Alayrac, J. B., Yu, J., Soricut, R., Blanco, 
L.: Gemini: a family of highly capable multimodal models 
(2023). arXiv preprintarXiv:2312.11805. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​
0​/​a​r​X​i​v​.​2​3​1​2​.​1​1​8​0​5
147.	Di Lillo, L., Gode, T., Zhou, X., Atzei, M., Chen, R., Victor, T.: 
Comparative safety performance of autonomous- and human 
drivers: a real-world case study of the waymo driver. Heliyon 
10(14), e34379 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​h​e​l​i​y​o​n​.​2​0​2​4​.​e​3​
4​3​7​9
148.	Gabriel, I., Manzini, A., Keeling, G., Hendricks, L. A., Rieser, 
V., Iqbal, H., Manyika, J.: The ethics of advanced AI assistants 
(2024). arXiv preprintarXiv:2404.16244. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​
0​/​a​r​X​i​v​.​2​4​0​4​.​1​6​2​4​4
149.	Singh I. Zhang Y. (2024). Using responsible AI principles with 
amazon bedrock batch inference. AWS Machine Learning Blog. 
​h​t​t​p​s​:​/​/​a​w​s​.​a​m​a​z​o​n​.​c​o​m​/​b​l​o​g​s​/​m​a​c​h​i​n​e​-​l​e​a​r​n​i​n​g​/​u​s​i​n​g​-​r​e​s​p​o​n​s​i​b​
l​e​-​a​i​-​p​r​i​n​c​i​p​l​e​s​-​w​i​t​h​-​a​m​a​z​o​n​-​b​e​d​r​o​c​k​-​b​a​t​c​h​-​i​n​f​e​r​e​n​c​e​/
150.	OECD. Recommendation of the council on artificial intelligence, 
OECD/LEGAL/0449. Organisation for Economic Co-operation 
and Development (2019). ​h​t​t​p​s​:​/​/​o​e​c​d​.​a​i​/​e​n​/​a​s​s​e​t​s​/​f​i​l​e​s​/​O​E​C​D​-​L​
E​G​A​L​-​0​4​4​9​-​e​n​.​p​d​f
117.	Stenseke, J.: Artificial virtuous agents in a multi-agent tragedy of 
the commons. AI Soc. 39(3), 855–872 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​
1​0​0​7​/​s​0​0​1​4​6​-​0​2​2​-​0​1​5​6​9​-​x
118.	High-Level Expert Group on AI (2019). Ethics guidelines for 
trustworthy AI. B-1049 Brussels, 6. AI HLEG. ​h​t​t​p​s​:​/​/​d​i​g​i​t​a​l​-​s​t​r​a​
t​e​g​y​.​e​c​.​e​u​r​o​p​a​.​e​u​/​e​n​/​l​i​b​r​a​r​y​/​e​t​h​i​c​s​-​g​u​i​d​e​l​i​n​e​s​-​t​r​u​s​t​w​o​r​t​h​y​-​a​i
119.	Leslie, D., Burr, C., Aitken, M., Katell, M., Briggs, M., Rincon, 
C.: Human rights, democracy, and the rule of law assurance 
framework for AI systems: a proposal (2022).  arXiv preprint­
arXiv:2202.02776. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​2​0​2​.​0​2​7​7​6
120.	Prabhakaran, V., Mitchell, M., Gebru, T., Gabriel, I.: A human 
rights-based approach to responsible AI (2022). arXiv preprint­
arXiv:2210.02667. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​2​1​0​.​0​2​6​6​7
121.	Floridi, L., Sanders, J.W.: On the morality of artificial agents. 
Mind. Mach. 14, 349–379 (2004). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​2​3​/​B​:​M​I​
N​D​.​0​0​0​0​0​3​5​4​6​1​.​6​3​5​7​8​.​9​d
122.	Santoni de Sio, F., Mecacci, G.: Four responsibility gaps with 
artificial intelligence: why they matter and how to address them. 
Philosophy Technol. 34(4), 1057–1084 (2021). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​
.​1​0​0​7​/​s​1​3​3​4​7​-​0​2​1​-​0​0​4​5​0​-​x
123.	Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., 
von Arx, S., Liang, P. On the opportunities and risks of founda­
tion models (2021). arXiv preprintarXiv:2108.07258. ​h​t​t​p​s​:​/​/​d​o​i​.​
o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​1​0​8​.​0​7​2​5​8
124.	Fahim, S.: Ethico-Legal Aspect of AI-Driven Driverless Cars. 
Springer, Singapore (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​9​7​8​-​9​8​1​-​9​7​-​
6​8​8​3​-​7
125.	Hacker, P., Mittelstadt, B., Borgesius, F. Z., Wachter, S.: Gen­
erative discrimination: what happens when generative ai 
exhibits bias, and what can be done about It (2024). arXiv pre­
printarXiv:2407.10329. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​7​.​1​0​3​
2​9
126.	Meyer, S., Mandl, S., Gesmann-Nuissl, D., Strobel, A.: Respon­
sibility in hybrid societies: concepts and terms. AI Ethics 3(1), 
25–48 (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​4​3​6​8​1​-​0​2​2​-​0​0​1​8​4​-​2
127.	Naik, N., Hameed, B.Z., Shetty, D.K., Swain, D., Shah, M., Paul, 
R., Somani, B.K.: Legal and ethical consideration in artificial 
intelligence in healthcare: who takes responsibility? Front. Surg. 
9, 862322 (2022). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​8​9​/​f​s​u​r​g​.​2​0​2​2​.​8​6​2​3​2​2
128.	Shoemaker, E.: Is AI art theft? The moral foundations of copy­
right law in the context of AI image generation. Philosoph. Tech­
nol. 37(3), 114 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​1​3​3​4​7​-​0​2​4​-​0​0​7​9​
7​-​x
129.	OpenAI. Our approach to AI safety. OpenAI, April 5 (2023). ​h​t​t​p​
s​:​/​/​o​p​e​n​a​i​.​c​o​m​/​i​n​d​e​x​/​o​u​r​-​a​p​p​r​o​a​c​h​-​t​o​-​a​i​-​s​a​f​e​t​y​/
130.	Pichai S.: AI at google: our principles. Google Blog, June 7 
(2018). ​h​t​t​p​s​:​/​/​b​l​o​g​.​g​o​o​g​l​e​/​t​e​c​h​n​o​l​o​g​y​/​a​i​/​a​i​-​p​r​i​n​c​i​p​l​e​s​/
131.	Alghamdi, A., Hammad, M., Ugail, H., Abdel-Raheem, A., 
Muhammad, K., Khalifa, H.S., Abd El-Latif, A.A.: Detection 
of myocardial infarction based on novel deep transfer learning 
methods for urban healthcare in smart cities. Multimedia Tools 
and Applications 83, 14913–14934 (2024). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​
7​/​s​1​1​0​4​2​-​0​2​0​-​0​8​7​6​9​-​x
132.	Chen, Y., Qin, X., Wang, J., Yu, C., Gao, W.: Fedhealth: a feder­
ated transfer learning framework for wearable healthcare. IEEE 
Intell. Syst. 35(4), 83–93 (2020). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​M​I​S​.​2​0​
2​0​.​2​9​8​8​6​0​4
133.	Perolat, J., De Vylder, B., Hennes, D., Tarassov, E., Strub, F., de 
Boer, V., Tuyls, K.: Mastering the game of stratego with model-
free multiagent reinforcement learning. Science 378(6623), 990–
996 (2022). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​2​6​/​s​c​i​e​n​c​e​.​a​d​d​4​6​7​9
134.	Schramowski, P., Turan, C., Jentzsch, S., Rothkopf, C., Kerst­
ing, K.: BERT has a moral compass: improvements of ethical and 
moral values of machines. Machines (2019). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​
5​5​0​/​a​r​X​i​v​.​1​9​1​2​.​0​5​2​3​8
1 3
5189

--- Page 26 ---

AI and Ethics (2025) 5:5165–5190
160.	AWS-Guardrails (n.d.). Build responsible AI applications with 
guardrails. Amazon Web Services. ​h​t​t​p​s​:​/​/​a​w​s​.​a​m​a​z​o​n​.​c​o​m​/​b​e​d​r​
o​c​k​/​g​u​a​r​d​r​a​i​l​s​/
161.	AWS-RAI (n.d.). Transform responsible AI from theory into 
practice. Amazon Web Services. ​h​t​t​p​s​:​/​/​a​w​s​.​a​m​a​z​o​n​.​c​o​m​/​a​i​/​r​e​s​p​
o​n​s​i​b​l​e​-​a​i​/
162.	European Parliament: Artificial intelligence act. Regulation (EU) 
2024/1689. (2024) ​h​t​t​p​s​:​/​/​a​r​t​i​f​i​c​i​a​l​i​n​t​e​l​l​i​g​e​n​c​e​a​c​t​.​e​u​/​t​h​e​-​a​c​t​/
163.	HireVue (n.d.). HireVue Explainability Statement. ​h​t​t​p​s​:​/​/​w​w​w​.​h​i​
r​e​v​u​e​.​c​o​m​/​l​e​g​a​l​/​a​i​-​e​x​p​l​a​i​n​a​b​i​l​i​t​y​-​s​t​a​t​e​m​e​n​t
164.	IEEE (n.d.(a)). The IEEE Global Initiative 2.0 on Ethics of 
Autonomous and Intelligent Systems. Institute of Electrical and 
Electronics Engineers. ​h​t​t​p​s​:​/​/​s​t​a​n​d​a​r​d​s​.​i​e​e​e​.​o​r​g​/​i​n​d​u​s​t​r​y​-​c​o​n​n​e​c​
t​i​o​n​s​/​a​c​t​i​v​i​t​i​e​s​/​i​e​e​e​-​g​l​o​b​a​l​-​i​n​i​t​i​a​t​i​v​e​/
165.	IEEE (n.d.(b)). IEEE CertifAIEd™ Assessor Training. Institute of 
Electrical and Electronics Engineers. ​h​t​t​p​s​:​/​/​e​n​g​a​g​e​s​t​a​n​d​a​r​d​s​.​i​e​e​
e​.​o​r​g​/​i​e​e​e​c​e​r​t​i​f​a​i​e​d​.​h​t​m​l
166.	IEEE (n.d.(c)). IEEE portfolio of AIS technology and impact 
standards and standards projects. Institute of Electrical and Elec­
tronics Engineers. ​h​t​t​p​s​:​/​/​s​t​a​n​d​a​r​d​s​.​i​e​e​e​.​o​r​g​/​i​n​i​t​i​a​t​i​v​e​s​/​a​u​t​o​n​o​m​o​
u​s​-​i​n​t​e​l​l​i​g​e​n​c​e​-​s​y​s​t​e​m​s​/​s​t​a​n​d​a​r​d​s​/
167.	ISO (n.d.). ISO/IEC 42001:2023. International Organization for 
Standardization. ​h​t​t​p​s​:​/​/​w​w​w​.​i​s​o​.​o​r​g​/​s​t​a​n​d​a​r​d​/​8​1​2​3​0​.​h​t​m​l
168.	Microsoft (n.d.) FATE: Fairness, accountability, transparency, 
and ethics in AI. Microsoft. ​h​t​t​p​s​:​/​/​w​w​w​.​m​i​c​r​o​s​o​f​t​.​c​o​m​/​e​n​-​u​s​/​r​e​
s​e​a​r​c​h​/​t​h​e​m​e​/​f​a​t​e​/
169.	Samsung (n.d.). Samsung AI Principles. ​h​t​t​p​s​:​/​/​w​w​w​.​s​a​m​s​u​n​g​.​c​o​
m​/​u​s​/​a​b​o​u​t​-​u​s​/​d​i​g​i​t​a​l​-​r​e​s​p​o​n​s​i​b​i​l​i​t​y​/​a​i​-​e​t​h​i​c​s​/
Publisher's Note  Springer Nature remains neutral with regard to juris­
dictional claims in published maps and institutional affiliations.
151.	UNESCO. Recommendation on the ethics of artificial intelli­
gence. United Nations Educational, Scientific and Cultural Orga­
nization (2021). ​h​t​t​p​s​:​/​/​w​w​w​.​u​n​e​s​c​o​.​o​r​g​/​e​n​/​a​r​t​i​c​l​e​s​/​r​e​c​o​m​m​e​n​d​a​
t​i​o​n​-​e​t​h​i​c​s​-​a​r​t​i​f​i​c​i​a​l​-​i​n​t​e​l​l​i​g​e​n​c​e
152.	Atkinson, D., Morrison, J.: Unsettled Law: Time to Generate 
New Approaches? (2024) arXiv preprintarXiv:2407.01968. ​h​t​t​p​
s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​4​0​7​.​0​1​9​6​8
153.	Cheong, I., Caliskan, A., Kohno, T. (2023). Is the US legal sys­
tem ready for AI’S challenges to human values? arXiv preprint­
arXiv:2308.15906. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​4​8​5​5​0​/​a​r​X​i​v​.​2​3​0​8​.​1​5​9​0​6
154.	Hugenholtz, P.B., Quintais, J.P.: Copyright and artificial creation: 
does EU copyright law protect AI-assisted output? IIC-Int. Rev. 
Intell. Prop. Competit. Law 52(9), 1190–1216 (2021). ​h​t​t​p​s​:​/​/​d​o​i​.​
o​r​g​/​1​0​.​1​0​0​7​/​s​4​0​3​1​9​-​0​2​1​-​0​1​1​1​5​-​0
155.	Zhuk, A.: Navigating the legal landscape of AI copyright: a com­
parative analysis of EU, US, and Chinese approaches. AI Ethics 
4, 1299–1306 (2023). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​4​3​6​8​1​-​0​2​3​-​0​0​2​9​
9​-​0
156.	US Court (2022). Thaler v. Vidal, No. 21–2347 (Fed. Cir. 2022). ​
h​t​t​p​s​:​/​/​l​a​w​.​j​u​s​t​i​a​.​c​o​m​/​c​a​s​e​s​/​f​e​d​e​r​a​l​/​a​p​p​e​l​l​a​t​e​-​c​o​u​r​t​s​/​c​a​f​c​/​2​1​-​2​3​4​
7​/​2​1​-​2​3​4​7​-​2​0​2​2​-​0​8​-​0​5​.​h​t​m​l
157.	Simon Law PC. The legal implications of tesla’s flawed autopilot 
system. Simon Law PC, December 4 (2023). ​h​t​t​p​s​:​/​/​s​i​m​o​n​l​a​w​p​c​.​
c​o​m​/​p​e​r​s​o​n​a​l​-​i​n​j​u​r​y​/​t​e​s​l​a​-​a​u​t​o​p​i​l​o​t​-​l​e​g​a​l​-​i​m​p​l​i​c​a​t​i​o​n​s​/
158.	Lemberg S. (2024) Are autonomous vehicles safe? Lemberg Law. 
March, 14. URL: ​h​t​t​p​s​:​/​/​l​e​m​b​e​r​g​l​a​w​.​c​o​m​/​a​r​e​-​d​r​i​v​e​r​l​e​s​s​-​c​a​r​s​-​s​a​f​e​
/
159.	ABA: ABA Issues First Ethics Guidance on a Lawyer’s Use of AI 
Tools. American Bar Association, July 29 (2024). ​h​t​t​p​s​:​/​/​w​w​w​.​a​
m​e​r​i​c​a​n​b​a​r​.​o​r​g​/​n​e​w​s​/​a​b​a​n​e​w​s​/​a​b​a​-​n​e​w​s​-​a​r​c​h​i​v​e​s​/​2​0​2​4​/​0​7​/​a​b​a​-​i​s​
s​u​e​s​-​f​i​r​s​t​-​e​t​h​i​c​s​-​g​u​i​d​a​n​c​e​-​a​i​-​t​o​o​l​s​/
1 3
5190

```
