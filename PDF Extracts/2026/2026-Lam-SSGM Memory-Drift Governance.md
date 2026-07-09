---
source_pdf: "[[Lit-WS-PDFs/2026/2026-Lam-SSGM Memory-Drift Governance.pdf]]"
extracted_date: "2026-07-09"
pages: 13
extractor: "PyMuPDF"
---

Page 1:
Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the
Stability and Safety Governed Memory (SSGM) Framework
Chingkwun Lam, Jiaxin Li, Lingfei Zhang, Kuo Zhao∗
College of Intelligent Science and Engineering, Jinan University
zhaokuo@jnu.edu.cn
Abstract
Long-term memory has emerged as a founda-
tional component of autonomous Large Lan-
guage Model (LLM) agents, enabling contin-
uous adaptation, lifelong multimodal learn-
ing, and sophisticated reasoning.
However,
as memory systems transition from static re-
trieval databases to dynamic, agentic mech-
anisms, critical concerns regarding memory
governance, semantic drift, and privacy vul-
nerabilities have surfaced. While recent sur-
veys have focused extensively on memory re-
trieval efficiency, they largely overlook the
emergent risks of memory corruption in highly
dynamic environments.
To address these
emerging challenges, we propose the Stabil-
ity and Safety-Governed Memory (SSGM)
framework, a conceptual governance archi-
tecture. SSGM decouples memory evolution
from execution by enforcing consistency ver-
ification, temporal decay modeling, and dy-
namic access control prior to any memory
consolidation.
Through formal analysis and
architectural decomposition, we show how
SSGM can mitigate topology-induced knowl-
edge leakage where sensitive contexts are so-
lidified into long-term storage, and help pre-
vent semantic drift where knowledge degrades
through iterative summarization. Ultimately,
this work provides a comprehensive taxonomy
of memory corruption risks and establishes
a robust governance paradigm for deploying
safe, persistent, and reliable agentic memory
systems.
1
Introduction
Large Language Model (LLM) agents have
demonstrated
impressive
reasoning
and
in-
teraction
capabilities
across
diverse
domains
(Matarazzo and Torlone, 2025); yet, in the ab-
sence of specialized mechanisms, they remain
fundamentally stateless.
Standard LLMs rely
on a fixed-length context window that prevents
∗Corresponding author.
indefinite information retention (Zhong et al.,
2024; Yousuf et al., 2025; OpenAI, 2023). While
early solutions employed Retrieval-Augmented
Generation (RAG) to provide a static knowledge
base (Lewis et al., 2020; Gao et al., 2023), modern
autonomous agents demand a more dynamic capa-
bility: the ability to learn from experience, update
their world models, and refine their strategies over
time (Xi et al., 2023; Wang et al., 2023).
This necessity has driven a paradigm shift from
static memory storage to adaptive, self-refining
memory systems. Recent architectures treat mem-
ory operations not as passive retrieval tasks but as
active decision-making processes. For instance,
Memory-R1 employs reinforcement learning to
train specialized sub-agents that autonomously de-
cide when to add, update, or delete memory units
based on task feedback (Yan et al., 2026). Simi-
larly, frameworks like Mem0 and AtomMem in-
troduce dynamic consolidation mechanisms that
continuously optimize the storage structure via
atomic operations (Chhikara et al., 2025; Huo
et al., 2026).
In these systems, memory is no
longer an immutable log but a mutable asset that
evolves alongside the agent (Zhang et al., 2026b;
Luo et al., 2026).
However, granting agents the autonomy to
rewrite their own memory introduces the stability-
plasticity dilemma into artificial systems. With-
out robust governance, the continuous refinement
of memory creates significant risks.
An agent
may gradually distort facts through repeated sum-
marization (semantic drift), reinforce suboptimal
workflows (procedural drift) (Han et al., 2025;
Rath, 2026), or inadvertently internalize halluci-
nations and malicious injections as valid knowl-
edge (Wang et al., 2025; Greshake et al., 2023).
Unlike static RAG systems, where errors are iso-
lated to a single retrieval step, errors in evolv-
ing memory systems are cumulative and persis-
tent. As delineated in Figure 1, this creates a com-
arXiv:2603.11768v2  [cs.AI]  19 May 2026


Page 2:
Figure 1: The Lifecycle of Memory Evolution and
Emergent Risks. Unlike static RAG, evolving mem-
ory systems introduce a feedback loop where errors can
accumulate. We identify three critical failure points:
(1) Memory Poisoning during input ingestion, (2) Se-
mantic Drift during consolidation updates, and (3)
Conflict/Hallucination during retrieval. SSGM aims
to govern these interfaces.
pounding failure loop across three critical inter-
faces: input ingestion (poisoning), memory con-
solidation (drift), and memory retrieval (halluci-
nation). Figure 1 presents this coarse-grained life-
cycle risk loop, which is later refined into the
four-dimensional failure taxonomy in Table 2. As
noted in recent surveys (Hu et al., 2025; Luo et al.,
2026), while the mechanisms of memory update
are well-studied, the protocols for ensuring their
long-term correctness and safety remain underex-
plored.
To address this gap,
this paper proposes
the Stability- and Safety-Governed Memory
(SSGM) framework.
We argue that for LLM
agents to be reliable in high-stakes environments,
memory evolution must be decoupled from mem-
ory governance. Our contributions are fourfold:
1. Taxonomy of Evolution:
We categorize
memory evolution along three dimensions:
content abstraction, structural reorganization
(e.g., from lists to Zettelkasten-style graphs
(Xu et al., 2025; Jiang et al., 2026)), and pol-
icy optimization.
2. Failure Analysis: We identify and formal-
ize key failure modes in adaptive memory,
specifically distinguishing between intrinsic
drift (e.g., knowledge conflict) and extrinsic
threats (e.g., memory poisoning).
3. The SSGM Framework: We synthesize de-
sign principles for a governed memory ar-
chitecture that integrates consistency verifi-
cation and ground-truth anchoring to mitigate
the risks of uncontrolled evolution.
4. Fundamental Trade-offs: We establish a
formal discussion on the three fundamen-
tal trade-offs inherent in agentic memory—
the latency-safety trade-off, the stability-
plasticity conflict, and the scalability of graph
structures—setting the stage for future re-
search.
2
From Static to Adaptive Memory
Systems
Initial iterations of LLM-based agent systems ei-
ther lacked long-term memory entirely or relied
on simplistic approaches to maintain context. For
example, some agents maintained a sequential log
of recent dialogue and instructions, truncating or
discarding older content upon the saturation of the
context window (Press et al., 2021); others utilized
vector-similarity search within a database of past
interactions to retrieve relevant segments on de-
mand. These strategies constitute a paradigm of
static memory: the agent does not alter its memory
usage adaptively based on interaction outcomes,
and the rules for storage and retrieval are prede-
termined by developers. A classic example is the
Generative Agents framework (Park et al., 2023),
where simulated characters stored factual observa-
tions and reflections, retrieving them via a fixed
relevance-and-recency scoring heuristic.
While
effective to a degree, this design required exten-
sive manual tuning of storage and summariza-
tion criteria, and the system could not learn from
memory management errors. Similarly, Memo-
ryBank (Zhong et al., 2024) and related systems
summarized or discarded observations using fixed
schedules or manually crafted triggers, illustrat-
ing the resource-intensive and suboptimal nature
of heuristic memory management.
The limitations of static approaches motivated
the development of adaptive memory mecha-
nisms. A crucial insight involved framing mem-
ory management as a decision problem amenable
to learning or operating system-like manage-
ment. MemGPT (Packer et al., 2024) pioneered
the concept of treating context as a limited re-
source, employing an OS-inspired paging mech-
anism to transfer information between “main con-
text” (RAM) and “external context” (disk) based
on immediate task requirements. This represented
a fundamental shift from simple sliding windows.
The Tensor Brain (Tresp et al., 2023) constituted
another early effort, introducing a neural archi-


Page 3:
tecture for differentiable episodic, semantic, and
working memory. More recently, Memory-R1 ex-
plicitly formulates memory operations as actions
to be optimized by a learned policy (Yan et al.,
2026).
Other systems incorporate adaptivity via al-
ternative mechanisms: MemAct (Zhang et al.,
2026b) enables the agent to embed memory-
related actions into its chain-of-thought prompting
(Wei et al., 2022; Yao et al., 2023). If the agent
detects uncertainty regarding a detail, it can ex-
plicitly issue a “lookup memory” or “store mem-
ory” action.
Over multiple reasoning sessions,
the agent refines the timing of these actions via
feedback. Similarly, Nemori (Nan et al., 2025)
draws upon cognitive science to introduce a self-
organizing memory policy: the agent internalizes
rules for maintaining consistency and organization
(such as periodically reconciling new information
with old) without external supervision, thereby
gradually improving memory coherence.
3
What Evolves: Content, Structure, and
Policy
Memory in LLM agents evolves along multiple
dimensions. We categorize the major facets as:
(1) the content of memory, comprising stored in-
formation and its level of detail; (2) the struc-
ture of memory, referring to the organization and
representation of knowledge; and (3) the policy
for memory management, namely the decision-
making process that determines how memory is
utilized and updated. While these facets are inter-
related, examining them separately clarifies how
modern systems transcend the limitations of static
memory.
3.1
Evolving Memory Content (What is
Stored)
The most direct form of memory evolution occurs
in the content itself.
Unlike a static transcript,
adaptive agents continually modify memory units.
This process involves adding new facts, updat-
ing existing units, summarizing detailed events
into high-level conclusions, or deleting informa-
tion deemed irrelevant or obsolete. By altering the
content of stored information, the knowledge base
becomes a dynamic resource that changes over
time.
A common pattern is summarization and ab-
straction.
An agent may replace a detailed
episode with a brief synopsis once confidence is
established that fine-grained details are no longer
requisite.
This was observed in early experi-
ments with Generative Agents (Park et al., 2023).
More recently, systems have expanded content
evolution to include multimodal and procedu-
ral knowledge. For instance, VideoARM (Yin
et al., 2025) dynamically constructs hierarchical
memory to reason over long-form videos with-
out exhaustive preprocessing, while WorldMM
(Yeo et al., 2025) continuously tracks spatiotem-
poral states.
Similarly, TeleMem (Chen et al.,
2025) maintains evolving object-centric graphs
that track the changing states of physical environ-
ments, while LEGOMem (Han et al., 2025) syn-
thesizes successful execution traces into procedu-
ral rules.
To further structure this, frameworks
like Agent Workflow Memory (AWM) (Zheng
et al., 2024) demonstrate how episodic traces can
be systematically compressed into reusable work-
flow rules, enhancing procedural memory while
mitigating the noise of raw logs. This shift from
purely textual facts to procedural content increases
the complexity of maintaining consistency, as er-
rors in procedural memory can lead to cascading
failures in task execution.
3.2
Evolving Memory Structure (How
Knowledge is Organized)
The structuring of memory dramatically influ-
ences retrieval effectiveness and the reasoning ca-
pabilities of the agent (Luo et al., 2026). Group-
ing related facts or linking causes and effects
facilitates inferences that are difficult to derive
from unstructured data. Many agent memory sys-
tems draw inspiration from databases or cognitive
metaphors such as knowledge graphs and seman-
tic networks.
Recent advancements have introduced self-
organizing structures. A-MEM (Xu et al., 2025)
adopts the Zettelkasten method, treating memo-
ries as atomic notes that dynamically evolve by
establishing links with related concepts, effec-
tively creating a “living” graph of knowledge.
Drawing directly from neurobiology, HippoRAG
(Gutiérrez et al., 2024) utilizes a spreading activa-
tion mechanism over knowledge graphs to mimic
human associative recall, drastically improving
multi-hop reasoning performance. To bridge the
gap between static retrieval and cognitive syn-
thesis, MemoRAG (Qian et al., 2024) builds a


Page 4:
System
Memory Structure
Evolution Policy
Refinement & Stability
Safety & Access
Target Domain
Adaptive & Learning-Based Systems
Memory-R1 (Yan et al., 2026)
Flat Vector DB
RL (PPO)
Feedback-driven Updates
–
Open-Domain QA
MemAgent (Yu et al., 2025)
Semantic Slots
RL (DAPO)
Selective Overwriting
–
Long-Context QA
AtomMem (Huo et al., 2026)
Vector + Buffer
Atomic Ops
Needle-in-Haystack Training
–
Multi-Turn Reasoning
LEGOMem (Han et al., 2025)
Procedural Graph
Failure-driven
Rule Verification
–
Workflow Automation
AgentSM (Biswal et al., 2026)
SQL-based Knowledge
Agentic Tuning
Schema Evolution
Strict Schema Constraints
Text-to-SQL (Enterprise)
AWM (Zheng et al., 2024)
Workflow Rules
Skill Induction
Trace Compression
–
Procedural Execution
DarwinMem (Mi et al., 2026)
Evolutionary Pool
Training-Free
Survival of the Fittest
–
GUI Agent Evolution
Astraea (Ni et al., 2025)
KV Cache
State-Aware Sched.
JCT Lifecycle Optim.
–
Agentic Workflows
Graph-Based & Cognitive Architectures
HiMem (Zhang et al., 2026a)
Hierarchical
LLM-Reasoning
Reconsolidation
Precision-Recall Balance
Long-Horizon Agents
A-MEM (Xu et al., 2025)
Zettelkasten Graph
Self-Organizing
Dynamic Linking
–
General Agents
MemoRAG (Qian et al., 2024)
Global Memory Graph
Insight Extraction
Memory-Enhanced Retrieval
–
Long Context QA
LiCoMemory (Huang et al., 2025)
Lightweight KG
Consistency Checks
Semantic Decay
Fact Verification
Multi-Turn Reasoning
HippoRAG (Gutiérrez et al., 2024)
Neurobiological Graph
Spreading Act.
Pathway Consolidation
–
Open-Domain QA
Forgetful/Faithful (Alqithami, 2025)
Typed Node Schema
Budgeted Forgetting
Coherence Preserved
(ϵ, δ)-Privacy
Privacy-Aware Agents
E-mem (Wang et al., 2026)
Episodic Context
Reconstruction
Context Reconstruction
Traceability
Long-Horizon Tasks
Zep (Rasmussen et al., 2025)
Temporal KG
Incremental Extraction
Entity Resolution
–
Conversational AI
Multimodal & Collaborative Systems
TeleMem (Chen et al., 2025)
Object-Centric Graph
User-driven Trigger
Physical Scene Updates
Privacy Filtering
Embodied AI / IoT
VideoARM (Yin et al., 2025)
Hierarchical Multi.
Adaptive Loop
Multi-level Clue Updates
–
Long-Form Video
WorldMM (Yeo et al., 2025)
Spatiotemporal Mem
Dynamic Retrieval
Video State Tracking
–
Long Video Reasoning
MemVerse (Liu et al., 2025b)
Multimodal Vector
Continual Learning
Cross-Modal Alignment
–
Lifelong Learning
Collab. Mem (Rezazadeh et al., 2025)
Distributed Vector
Consensus Voting
Cross-User Deduplication
Dynamic ACLs
Multi-User Collab
Topology Matters (Liu et al., 2025a)
Multi-Agent Network
MAMA Framework
Leakage Plateau Anal.
Centrality Const.
Multi-Agent Privacy
MIRIX (Wang and Chen, 2025)
Shared Multi-Agent Space
Collaborative Reflection
Procedural Alignment
Agent Role Boundaries
Multi-Agent Systems
Table 1: Taxonomy of Evolving Memory Systems. We categorize recent systems by their storage structure, the
policy governing memory evolution, mechanisms for maintaining stability, and safety provisions. Newly integrated
approaches like HippoRAG, DarwinMem, and VideoARM emphasize the shift towards neurobiology, adaptive
policies, and multimodal environments.
global memory graph over long contexts, enabling
agents to extract structural insights before gener-
ating answers. Similarly, HiMem (Zhang et al.,
2026a) implements a hierarchical structure where
episodic details are continuously distilled into se-
mantic knowledge through a process of reconsol-
idation. ChatDB (Hu et al., 2023) treats memory
as a symbolic SQL database, allowing the agent to
execute complex queries rather than relying solely
on semantic search; the structure evolves as the
agent defines new tables or schemas.
3.3
Evolving Memory Policy (How Memory
is Managed)
Table 1 provides a comprehensive taxonomy of
these evolving systems, categorizing them by their
structural approach (from vector databases to hier-
archical graphs) and their evolution policies. No-
tably, as shown in the table, newer frameworks
like AtomMem (Huo et al., 2026) and MemAgent
(Yu et al., 2025) employ Reinforcement Learn-
ing (RL) to learn optimal memory policies. By
framing memory operations (add, update, delete,
retrieve) as atomic actions, these agents optimize
their memory management strategies to maximize
long-term task rewards. Conversely, DarwinMem
(Mi et al., 2026) proves that memory policies can
also be optimized without parameter updates, em-
ploying a training-free “survival of the fittest” evo-
lutionary pool to adapt GUI agents across tasks.
4
How Memory Evolves: Reflection,
Reinforcement, and Consolidation
Having identified what changes in evolving mem-
ory, we now examine how these changes are ef-
fected.
4.1
Reflection and Self-Supervised Memory
Updates
Reflection involves an agent examining its own
actions or outcomes and generating analyses
or lessons, which then inform future decisions
(Sumers et al., 2023). In Reflexion (Shinn et al.,
2023), the agent prompts itself: “If the solution
was wrong, explain the error.” The generated re-
flection is stored as a memory. This reflective loop
has become a cornerstone of agent improvement
(Madaan et al., 2023; Wang et al., 2023). MemR3
(Du et al., 2025) extends this by employing reflec-
tive reasoning during the retrieval process itself,
refining queries iteratively to bridge the gap be-
tween user intent and stored knowledge.
4.2
Reinforcement Learning and
Outcome-Driven Memory Optimization
While reflection relies on self-supervision, Rein-
forcement Learning (RL) offers a direct method
to optimize memory behavior toward explicit ob-
jectives. Formally, the memory management prob-
lem can be modeled as a Partially Observable
Markov Decision Process (POMDP). At time t,


Page 5:
the agent receives an observation ot (e.g., a user
query), maintains an internal memory state Mt,
and occupies a latent decision state st that sum-
marizes the observation, the current memory, and
the task context. The policy πθ(at | ot, Mt) se-
lects an action at ∈A, where the global ac-
tion space contains both task-level actions and
memory-management actions. We explicitly de-
fine the memory-action subset as follows:
Amem = {ADD(c), UPDATE(idx, v),
DELETE(idx), RETRIEVE(q)}
(1)
where c denotes the content to be stored, idx de-
notes the index or key of an existing memory
item, v denotes the replacement or updated value
written to that indexed item, and q denotes the
retrieval query used to access previously stored
memory. Intuitively, Eq. (1) defines the discrete
action subspace through which the agent treats
memory management as an explicit decision pro-
cess rather than as a fixed backend routine.
The agent optimizes parameters θ to maximize
the expected discounted return:
J(θ) = Eτ∼πθ
" T
X
t=0
γtr(st, at)
#
(2)
where τ denotes a trajectory induced by the pol-
icy πθ, T denotes the horizon length of the in-
teraction episode, γ ∈[0, 1) is the discount fac-
tor that balances immediate and long-term reward,
st denotes the latent decision state at time t, and
r(st, at) denotes the reward assigned to taking ac-
tion at in state st. Intuitively, Eq. (2) formalizes
the objective of learning a memory policy that op-
timizes long-term utility: a memory write that in-
curs slight short-term cost may still be preferred
if it substantially improves future reasoning or re-
trieval.
Memory-R1 (Yan et al., 2026) utilizes
this formulation via Proximal Policy Optimization
(PPO). MemAgent (Yu et al., 2025) further refines
this by using Group Relative Policy Optimization
(GRPO) to handle the sparse rewards associated
with long-term memory benefits.
4.3
Memory Consolidation and Forgetting
The third key mechanism is consolidation and
forgetting,
analogous to biological processes
(Tresp et al., 2023).
Without management, the
memory size |M| grows linearly, causing re-
trieval latency. Alqithami (2025) formalizes this
through “forgetting-by-design”, demonstrating via
the FiFA benchmark that bounded, budget-aware
forgetting policies (e.g., Priority Decay) not only
reduce computational cost but actively preserve
narrative coherence and privacy without sacrific-
ing functionality.
Temporal Decay and Freshness Governance
To mitigate the risk of temporal obsolescence,
where stale facts contradict recent updates, gov-
ernance mechanisms must incorporate time-aware
forgetting. Inspired by cognitive decay theories,
Huang et al. (2025) propose a Weibull-based de-
cay function to model the relevance w(∆τ) of a
memory unit over time:
w(∆τ) = exp

−
∆τ
η
κ
(3)
where ∆τ denotes the elapsed time (e.g., mea-
sured in conversational turns or absolute hours)
since the last successful retrieval of the memory
unit, η is the scale parameter controlling the char-
acteristic time scale of decay, and κ is the shape
parameter controlling the curvature of the forget-
ting profile. Intuitively, Eq. (3) assigns lower rel-
evance scores to stale memory entries, thereby al-
lowing the system to downweight or discard items
that are less likely to remain valid. The Weibull
form is more expressive than a simple exponen-
tial decay because the shape parameter can rep-
resent faster early decay or more delayed forget-
ting under different domains. In the SSGM frame-
work, memory items are pruned or archived when-
ever their temporal relevance falls below a uni-
fied freshness threshold θfresh, thereby reducing
the attack surface for stale reasoning and memory-
induced hallucination.
Furthermore, E-mem (Wang et al., 2026) shifts
from simple retrieval to Episodic Context Recon-
struction, where the agent actively reconstructs the
context from fragmented traces rather than retriev-
ing pre-stored blocks, ensuring higher fidelity to
the original experience.
5
Why Memory Fails: Drift, Efficiency,
Validity, and Safety
Evolving memory empowers LLM agents but also
introduces a spectrum of potential failure modes.
As illustrated in Table 2, we categorize these fail-
ures into four distinct dimensions: Stability, Valid-
ity, Efficiency, and Safety.


Page 6:
Category
Failure Mode
Mechanism & Manifestation
Representative Contexts
SSGM Mitigation Strategy
Stability
Semantic Drift
Iterative summarization causes gradual nuance loss
Recursive Summarization (Park et al., 2023)
Ground Truth Anchoring (R)
Procedural Drift
Reinforcement of suboptimal/outdated workflows
Workflow Automation (Han et al., 2025; Fang et al., 2025)
Rule Verification
Goal/Role Drift
Alignment shift due to accumulated interaction bias
Long-term Role-play (Yuen et al., 2026)
Role Partitioning
Validity
Memory Hallucination
Retrieval of non-existent or fabricated facts
Open-domain QA (Du et al., 2025)
Consistency Verifier (TMS)
Temporal Obsolescence
Conflict between stale memories and new states
User Personalization (Rasmussen et al., 2025)
Weibull Decay Function
Efficiency
Retrieval Latency
Search time scales linearly/quadratically with history
Real-time Interaction (Chhikara et al., 2025)
Hierarchical Indexing
Index Bloat
Accumulation of redundant/noisy episodic logs
Infinite Context (Sarin et al., 2025)
Active Forgetting / Pruning
Safety
Memory Poisoning
Injection of malicious instructions into storage
User Instruction Tuning (Greshake et al., 2023)
Write Filtering (Firewall)
Privacy Leakage
Unauthorized cross-session/cross-user retrieval
Multi-tenant Agents (Rezazadeh et al., 2025)
Provenance & ACLs
Table 2: Comprehensive Taxonomy of Evolving Memory Failures. We expand the taxonomy to include Effi-
ciency failures (Latency, Bloat), which are critical in long-horizon agents. Validity failures now explicitly dis-
tinguish between hallucination and temporal obsolescence (fact conflict over time), citing recent evidence from
Rasmussen et al. (2025).
5.1
Semantic Drift and Gradual Deviation
Memory drift refers to the phenomenon where
the knowledge stored by an agent gradually devi-
ates from ground truth (conceptually visualized in
Figure 2, which specifically illustrates preference-
intensity drift under repeated lossy summariza-
tion). Drift is not monolithic; it manifests in sev-
eral forms.
Semantic drift is primarily driven by lossy
compression algorithms, such as iterative sum-
marization. As information is re-encoded multiple
times (e.g., from raw text to summary to higher-
level reflection), nuanced details are stripped
away, leading to a gradual distortion of the ground
truth (Park et al., 2023). Figure 2 provides an in-
tuitive example of this process: a mild user prefer-
ence can be progressively intensified through re-
peated rewriting, eventually causing a concrete
preference violation. As contrasted in Figure 3,
while a naive pipeline exacerbates this nuance loss
by repeatedly overwriting the active memory, an
anchored approach periodically reconciles the mu-
table state with an immutable episodic ledger (for-
mally denoted as Kledger later in Section 6.2) to
preserve original fidelity. Figure 3 abstracts the
causal mechanism behind this process, whereas
Figure 2 visualizes its concrete symptom at the
level of a user preference.
Procedural drift refers to the degradation of
the skills or strategies of an agent as it reinforces
suboptimal execution paths (Han et al., 2025).
For instance, an agent might “learn” a convoluted
workaround for a simple API call and rigidify this
into its procedural memory, blocking future opti-
mization.
Finally, Goal drift represents a subtle misalign-
ment where the behavior of the agent shifts away
from original instructions due to accumulated bi-
ases in its memory (Rath, 2026).
Figure 2: An Illustrative Case of Semantic Drift. It-
erative summarization gradually distorts a specific user
preference through lossy compression and semantic in-
tensification. For example, an originally mild prefer-
ence (e.g., “I like mild spicy food”) may be progres-
sively rewritten as “likes spicy food” and later “loves
very spicy food,” ultimately causing a preference vio-
lation (e.g., suggesting ghost pepper wings).
We can formalize semantic drift δ at time T as
the divergence between the embedding represen-
tation E(MT ) of the current memory and the em-
bedding of the ground-truth reference ledger Ktrue:
δ(MT , Ktrue) = 1 −sim (E(MT ), E(Ktrue)) (4)
where MT denotes the memory state after T up-
date steps, Ktrue denotes the idealized ground-truth
semantic target, E(·) ∈Rd denotes a fixed seman-
tic embedding model projecting the memory into a
d-dimensional continuous space, and sim(·, ·) de-
notes cosine similarity in the embedding space.


Page 7:
Intuitively, Eq. (4) uses embedding-space diver-
gence as a tractable proxy for semantic corruption:
the larger the distance between the current mem-
ory representation and the reference ledger, the
larger the estimated drift. In practice, Ktrue may
be approximated by an immutable ledger of raw
observations, which preserves details that may be
lost in iterative summarization.
5.2
Validity Failures: Hallucination and
Obsolescence
Closely related to drift is the problem of Valid-
ity.
This manifests primarily as Memory Hal-
lucination, where the agent stores hallucinated
content as truth.
Distinct from hallucination is
temporal obsolescence, a failure mode highlighted
by Rasmussen et al. (2025) in temporal knowl-
edge graphs. Here, stored information is factually
correct but outdated. Without mechanisms to re-
solve conflicting timestamps (as addressed by Li-
CoMemory’s decay function), agents may retrieve
and act upon stale data.
5.3
Systemic Failures: Efficiency and Safety
Beyond correctness, evolving memory systems
face Efficiency and Safety challenges. As memory
logs expand, Retrieval Latency can scale linearly
or quadratically (Chhikara et al., 2025). Astraea
(Ni et al., 2025) reveals that isolated segment re-
trieval causes severe Head-of-Line blocking, ad-
vocating for state-aware scheduling that optimizes
the global request lifecycle during agentic mem-
ory operations.
On the safety front, Memory Poisoning re-
mains a critical risk (Greshake et al., 2023). Ad-
ditionally, in multi-user environments, Privacy
Leakage becomes a concern.
Topology Mat-
ters (Liu et al., 2025a) highlights that the network
structure of multi-agent systems intrinsically gov-
erns memory leakage, finding that fully connected
graphs maximize vulnerability. Therefore, with-
out rigorous Access Control Lists (ACLs), as im-
plemented in Collaborative Memory (Rezazadeh
et al., 2025), agents may inadvertently retrieve
cross-session memories, leaking sensitive data to
unauthorized parties.
Figure 3: Logical Mechanism of Memory Drift vs.
Anchored Stability. The left path illustrates how naive
iterative summarization causes semantic drift (loss of
nuance). The right path demonstrates the SSGM ap-
proach, where periodic reconciliation (R) with an im-
mutable anchor log (Kledger) bounds the distortion rela-
tive to the ground truth (Ktrue).
6
Stability and Safety Governed Memory
(SSGM): Design Principles and
Research Agenda
Current memory systems predominantly prioritize
adaptability—the ability of an agent to rapidly
learn and incorporate new context—over stability
and safety. In unrestricted architectures, the agent
interacts directly with the storage medium, act-
ing as both the sole generator and validator of its
evolving knowledge base. As established in Sec-
tion 4, this unconstrained autonomy is the primary
catalyst for semantic drift, catastrophic forgetting,
and susceptibility to adversarial memory poison-
ing (Greshake et al., 2023).
To bridge this critical gap,
we formulate
the Stability- and Safety-Governed Memory
(SSGM) framework. Rather than a specific soft-
ware implementation, SSGM provides a rigor-
ous theoretical architecture and a set of design
principles. At its core, SSGM proposes that ro-
bust memory systems must structurally decouple
the generative cognitive policy of the agent from
the underlying memory substrate through an ac-
tive, intercepting Governance Middleware. Fig-
ure 4 operationalizes the mechanism abstracted in
Figure 3 as a full governed architecture, where
Eq. (5), Eq. (6), and Eq. (7) correspond respec-
tively to constrained retrieval, gated writing, and
asynchronous reconciliation.
6.1
Design Principles of Governed Memory
As illustrated in Figure 4, SSGM replaces di-
rect memory access with a set of governed gates.
We articulate four foundational design principles


Page 8:
Dual Memory Substrate
(Middleware & Control)
Governance Middleware
Immutable Episodic Log
LLM Cognitive Policy
(Input & Reasoning)
Editable Structured Memory for Reasoning
Governance Layer
Mutable Active Graph
Cognition Layer
Read Filtering Gate
Write Validation Gate
Consistency + Truth Maintenance +
Accept or Reject updates
(Storage & Sync)
Asynchronous replay/anchoring
Memory Layer
Provenance + Temporal Relevance +
Reconciliation 
Append-only Episodic Records
(Reasoning + Tool Use)
Access Control (ACL/ABAC)
to correct the graph
Anchor
(trace / evidence)
Consolidate
Candidates
Candidate Memories
Memory
Replay /
Retrieve
Filtered Context
Update
Read/Write
Resource
Access
Editor
Role
User
D1
U1
DATE
Context Query
Access
Resource
Role
User
Read/Write
D1
Editor
U1
Consis-
Check
Logic
Truth
Value
Pass
A=>B
True
Fail
A=>?
False
Reject
Update
Fail
Figure 4: The conceptual architecture of the SSGM framework, featuring a decoupled left-to-right pro-
cessing pipeline. The Governance Middleware intercepts memory interactions between the LLM Agent and the
Memory Substrate. The upper pathway governs memory consolidation (Write Validation) to ensure logical consis-
tency and mitigate drift, while the lower pathway manages memory retrieval (Read Filtering) by enforcing access
scopes and temporal relevance. The right-side dual-memory substrate further supports reversible reconciliation by
pairing a mutable active graph with an immutable episodic log.
necessary for engineering reliable, long-horizon
agents:
Principle 1: Pre-Consolidation Validation
In
biological systems, the hippocampus does not in-
stantly commit every perception to the neocortex;
information undergoes significant filtering and re-
ality monitoring (Tresp et al., 2023). Similarly, in
SSGM, memory updates should never be commit-
ted passively. When the agent generates a mem-
ory delta (∆M), it must pass through a Write
Validation Gate (depicted as the upper consolida-
tion pathway in Figure 4). This mechanism acts
as a Truth Maintenance System (TMS) that re-
trieves established core facts (Mcore) to execute a
strict logical contradiction check: if the condition
∆M ∧Mcore |= ⊥evaluates to true, the update is
rejected. By bounding updates with formal Natu-
ral Language Inference (NLI) checks, the system
actively prevents hallucination cascades from per-
manently corrupting the semantic graph (Xu et al.,
2025).
Principle
2:
Temporal
and
Provenance
Grounding
Not all stored information retains
its validity indefinitely. Unrestricted retrieval of-
ten pulls stale or maliciously injected instructions,
leading to temporal obsolescence (Rasmussen
et al., 2025). SSGM advocates for a Read Filter-
ing Gate (illustrated in the lower retrieval pathway
in Figure 4) that evaluates candidate contexts
based on two axes. First, it requires cryptographic
provenance (σ(µ)) to ensure the memory unit
was generated by a trusted source rather than an
adversarial prompt. Second, it applies a cognitive
decay function, such as the Weibull distribution
w(∆τ) = exp(−(∆τ/η)κ) proposed by Huang
et al. (2025). Memories falling below a dynamic
relevance threshold are pruned before reaching
the agent’s context window, ensuring the agent
reasons exclusively over fresh, high-confidence
data.
Principle 3:
Access-Scoped Retrieval
The
shift towards multi-agent (Wang and Chen, 2025)
and multi-tenant systems exposes critical privacy
vulnerabilities.
As demonstrated by Liu et al.
(2025a), fully connected memory networks max-
imize the risk of topology-induced knowledge
leakage. SSGM dictates that retrieval mechanisms
must not rely solely on semantic similarity. In-
stead, the Read Filtering Gate must inject identity-
based constraints (e.g., Attribute-Based Access
Control, ABAC) directly into the query execution
layer (Rezazadeh et al., 2025). This ensures strict
isolation of memory sub-graphs, preventing the
cross-contamination of agent personas or sensitive
user data.
Principle 4: Reversible Reconciliation
To ef-
fectively bound long-term semantic drift, the un-
derlying storage substrate must be dual-track.


Page 9:
Drawing inspiration from human episodic and
semantic memory divisions (Alqithami, 2025),
SSGM pairs a rapidly updatable Mutable Ac-
tive Graph (for fast, semantic reasoning) with an
append-only Immutable Episodic Log (acting as
the operational source of truth). This dual struc-
ture enables asynchronous reconciliation, allow-
ing the system to periodically “replay” and correct
drifted concepts against the raw interaction trace,
effectively offering a rollback mechanism if severe
agent behavioral degradation occurs (Rath, 2026).
6.2
Formalizing the SSGM Framework
To provide a rigorous theoretical account of
SSGM, we formulate the agent’s memory evolu-
tion as a controlled state transition.
Let Mt−1
denote the mutable memory state at time t −1,
let Mcore denote the set of protected core facts
used for contradiction checking, let Kledger denote
the append-only immutable ledger of raw obser-
vations, and let Ktrue denote the idealized seman-
tic target that the system seeks to approximate.The
read–write lifecycle in SSGM is then governed by
constrained retrieval, gated writing, and periodic
reconciliation.
The Read Phase (Constrained Retrieval):
Unlike naive Retrieval-Augmented Generation
(RAG), which relies only on semantic Top-K re-
trieval, the retrieved context Ct given a query qt
in SSGM is defined by jointly enforcing semantic
relevance, access control, and temporal freshness:
Ct = {µ ∈Top-K(qt, Mt−1) | ACL(µ, uid)
∧(w(∆τµ) ≥θfresh)}
(5)
where µ denotes a candidate memory unit,
Top-K(qt, Mt−1) denotes the set of the top-
K semantically retrieved items from the current
memory state with respect to query qt, uid de-
notes the identity of the requesting user or agent,
ACL(µ, uid) denotes an access-control predicate
that returns true only when uid is permitted to
read memory unit µ, ∆τµ denotes the elapsed time
since the last valid use of µ, and θfresh denotes
the global freshness threshold. Intuitively, Eq. (5)
implements a two-stage read path: semantic re-
trieval first proposes candidates, and governance
then filters them to prevent both privacy leakage
and stale-memory activation.
The Write Phase (Gated Transition):
In
an unconstrained system, the next memory state
would be produced by directly unioning the agent-
generated update with the existing memory, i.e.,
Mt = Mt−1 ∪Agent(Ct). In SSGM, this transi-
tion is intercepted by a write-governance operator:
Mt = Mt−1 ∪Gwrite (Agent(Ct), Mcore)
(6)
where Agent(Ct) denotes the candidate memory
delta proposed by the agent after reasoning over
Ct, and Gwrite(∆M, Mcore) = ∆M if ∆M ∧
Mcore ̸|= ⊥, and ∅otherwise. Here, ∆M denotes
the candidate update set and |= ⊥denotes the logi-
cal entailment of contradiction. Intuitively, Eq. (6)
turns memory writing into a guarded transition:
the system only admits updates that do not con-
flict with protected core facts, thereby preventing
hallucinated or inconsistent statements from being
consolidated into long-term memory.
Reconciliation (Drift Bounding): To prevent
the cumulative drift of admitted updates from di-
verging as T →∞, the asynchronous reconcilia-
tion operator R periodically re-aligns the mutable
memory against the immutable ledger:
Mclean ←arg min
M E
h
δ

R(M, Kledger), Ktrue
i
(7)
where M ranges over candidate cleaned memory
states, R(M, Kledger) denotes the reconciled mem-
ory obtained by replaying or correcting M using
the immutable ledger, δ(·, ·) is the semantic-drift
measure defined in Eq. (4), and the expectation
is taken over the stochasticity of task trajectories,
noisy summaries, or reconciliation decisions. In-
tuitively, Eq. (7) states that the system repeatedly
searches for a cleaned memory state Mclean whose
reconciled form is, in expectation, as close as pos-
sible to the desired semantic target. This objec-
tive makes the distinction among the three refer-
ence objects explicit: Mcore protects critical facts
during writing, Kledger is the operational raw trace
used for correction, and Ktrue is the ideal target
used for evaluation.
Theorem 1 (Bounded Semantic Drift). Assume
that each valid summarization or consolidation
step introduces at most ϵstep semantic error be-
fore reconciliation, and assume that the reconcil-
iation operator R restores the mutable memory
to a state whose residual error is bounded by a
constant independent of the total horizon. In a
naive system, the expected drift at time T scales as
O(T · ϵstep). Under the SSGM framework, if rec-
onciliation is executed every N steps, the expected


Page 10:
semantic drift is upper-bounded by O(N · ϵstep),
ensuring stability even when T ≫N.
Proof Sketch. In an unconstrained update process
without Eq. (7), per-step errors accumulate addi-
tively, yielding E[δ(MT )] ≤PT
t=1 ϵstep = T ·ϵstep.
Under SSGM, reconciliation is invoked every N
steps, so error can accumulate for at most one rec-
onciliation window before being corrected. For
any T = mN + r with 0 ≤r < N, the unrecon-
ciled portion contributes at most r·ϵstep < N ·ϵstep,
up to the bounded residual reconciliation error.
Hence the dominant growth term is bounded by
the window size N, not by the full horizon T.
6.3
Testable Research Hypotheses and
Evaluation Protocols
The formalization of SSGM establishes a new
paradigm for evaluating agent memory.
Mov-
ing beyond simplistic metrics like Recall@K (Ai
et al., 2025), we propose three testable research
hypotheses that should guide future empirical
evaluations in the NLP community:
H1: Governance Gates Statistically Bound
Drift Magnitude. Based on Theorem 1, we hy-
pothesize that agents equipped with Gwrite and R
will exhibit an asymptotic upper limit on drift
magnitude (δ(MT , Ktrue)) over infinite-horizon
tasks (e.g., T
> 100 turns), whereas baseline
agents will demonstrate approximately linear drift
accumulation. Evaluation Protocol: This can be
robustly tested using established benchmarks like
LongMemEval (Wu et al., 2025), utilizing LLM-
as-a-Judge and metrics like BERTScore to quan-
tify the fidelity of the final memory graph against
the ground-truth text over extended timesteps.
H2: Access-Scoped Retrieval Lowers Adver-
sarial Leakage Risk. We hypothesize that enforc-
ing the constrained retrieval rule in Eq. (5) will
dramatically lower the successful injection rate of
cross-tenant adversarial prompts without degrad-
ing the primary task success rate.
Evaluation
Protocol: Researchers should simulate multi-user
role-playing scenarios and measure the “Leak-
age Plateau” (Liu et al., 2025a) when adversar-
ial data is deliberately injected into neighboring
graph nodes.
H3: The Latency vs. Coherence Trade-off.
Integrating strict logical contradiction checks into
the critical path of Eq. (6) will yield a measurable
increase in memory write latency. Evaluation Pro-
tocol: Future studies must quantify this trade-off,
potentially demonstrating that asynchronous gov-
ernance protocols (e.g., executing R during idle
periods) can achieve high coherence (low δ) with-
out compromising the immediate conversational
fluidity (Zhang et al., 2025).
7
Conclusion
The transition from static context windows to
evolving, self-refining memory represents a piv-
otal leap in agentic AI. However, as demonstrated
in this survey, this autonomy comes with the peril
of memory corruption—ranging from subtle se-
mantic drift to catastrophic poisoning.
We ar-
gue that the prevailing focus on “retrieval accu-
racy” is insufficient; the next generation of mem-
ory systems must prioritize memory integrity and
safety.
The SSGM framework proposed in this pa-
per serves as a conceptual foundation for rigor-
ous memory governance. By decoupling the cog-
nitive policy from the memory substrate via val-
idation and filtering gates, we can build agents
that are adaptable yet robust. Beyond proposing
SSGM, this work also provides a taxonomy of
evolving memory systems, a structured analysis
of failure modes, and a framing of the core trade-
offs that will shape future governed memory de-
signs. Looking forward, the community must fo-
cus on standardized safety benchmarks (like Mem-
oryBench) that stress-test memory stability under
adversarial drift, machine unlearning protocols to
surgically remove toxic memories, and evaluating
the hypotheses defined in our research agenda. Ul-
timately, solving the memory-governance problem
is a prerequisite for deploying lifelong learning
agents in high-stakes, real-world environments.
Limitations
While SSGM provides a blueprint for reliable
memory, it introduces three fundamental trade-
offs that warrant future investigation:
1. The Latency-Safety Trade-off: The pro-
posed governance layer introduces a “System 2”
verification step into the memory loop. Validating
consistency and provenance for every update in-
curs significant latency, potentially rendering the
agent unresponsive in real-time scenarios. Future
work must explore asynchronous governance,
where memory is optimistically updated but pe-
riodically “sanitized” in the background (Zhang
et al., 2025).


Page 11:
2.
The Stability-Plasticity Conflict: Strict
consistency filtering may lead to knowledge os-
sification.
If the governance layer aggressively
rejects information that conflicts with established
memory, the agent may fail to adapt to legitimate
environmental changes (e.g., a user changing their
address).
Designing “conflict resolution proto-
cols” that can distinguish between drift and update
remains an open algorithmic challenge.
3.
Scalability of Graph Structures: While
graph-based memories (e.g., Zep, MAGMA) offer
superior reasoning capabilities, maintaining a con-
sistent graph at scale is non-trivial. As interaction
history grows, the complexity of graph traversal
and entity resolution can degrade retrieval perfor-
mance, necessitating more efficient graph pruning
and compression algorithms (Jiang et al., 2026).
References
Qingyan Ai, Yuhang Tang, Chuan Wang, Jiahui Long,
Weijie Su, and Yiting Liu. 2025.
Memorybench:
A benchmark for memory and continual learning in
llm systems. arXiv preprint arXiv:2510.17281.
Saad Alqithami. 2025.
Forgetful but faithful:
A
cognitive memory architecture and benchmark for
privacy-aware generative agents.
arXiv preprint
arXiv:2512.12856.
Archana Biswal, Cao Lei, Xiatian Qin, Ang Li, Brah-
midesh Narayanaswamy, and Tim Kraska. 2026.
AgentSM: Semantic memory for agentic text-to-
SQL. arXiv preprint arXiv:2601.15709.
Chunliang Chen, Ming Guan, Xiao Lin, Luxi Lin,
Jiaxu Li,
Qiyi Wang,
Xiangyu Chen,
Jixiang
Luo, Changzhi Sun, Dell Zhang, and Xuelong Li.
2025.
TeleMem:
Building long-term and mul-
timodal memory for agentic AI.
arXiv preprint
arXiv:2501.07722.
Pratham Chhikara, Dhyey Khant, Shivam Aryan, Tarun
Singh, and Divyansh Yadav. 2025. Mem0: Building
production-ready ai agents with scalable long-term
memory. arXiv preprint arXiv:2504.19413.
Xueying Du, Liang Li, Dawei Zhang, and Lin Song.
2025.
Memr3:
Memory retrieval via reflec-
tive reasoning for llm agents.
arXiv preprint
arXiv:2512.20237.
Rui Fang, Yinuo Liang, Xiaohui Wang, Jian Wu, Shi-
hong Qiao, Peng Xie, Fei Huang, Hua Chen, and
Ning Zhang. 2025. Memp: Exploring agent proce-
dural memory. arXiv preprint arXiv:2508.06433.
Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia,
Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Hao Wang,
and Haofen Wang. 2023. Retrieval-augmented gen-
eration for large language models: A survey. arXiv
preprint arXiv:2312.10997, 2(1).
Kai Greshake, Sahar Abdelnabi, Shailesh Mishra,
Christoph Endres, Thorsten Holz, and Mario Fritz.
2023. Not what you’ve signed up for: Compromis-
ing real-world llm-integrated applications with indi-
rect prompt injection. In Proceedings of the 16th
ACM Workshop on Artificial Intelligence and Secu-
rity, pages 79–90.
Bernal Jiménez Gutiérrez, Yiheng Shu, Yu Gu, Michi-
hiro Yasunaga, and Yu Su. 2024. HippoRAG: Neu-
robiologically inspired long-term memory for large
language models. In Advances in Neural Informa-
tion Processing Systems, volume 37.
Dong Han, Clement Couturier, David M. Diaz, Xing
Zhang, Volker Rühle, and S. Rajmohan. 2025.
Legomem: Modular procedural memory for multi-
agent llm systems for workflow automation. arXiv
preprint arXiv:2510.04851.
Chenxu Hu, Jie Fu, Chenzhuang Du, Simian Luo,
Junbo Zhao, and Hang Zhao. 2023. Chatdb: Aug-
menting llms with databases as their symbolic mem-
ory. arXiv preprint arXiv:2306.03901.
Yuting Hu, Sijie Liu, Yuhang Yue, Guosheng Zhang,
Boxiang Liu, Fang Zhu, Jian Lin, Hao Guo, Shuhan
Dou, Zhi Xi, et al. 2025. Memory in the age of ai
agents. arXiv preprint arXiv:2512.13564.
Ziyu Huang, Zhi Tian, Qian Guo, Fan Zhang, Yu Zhou,
Dawei Jiang,
Zhu Xie,
and Xia Zhou. 2025.
Licomemory:
Lightweight and cognitive agentic
memory for efficient long-term reasoning.
arXiv
preprint arXiv:2511.01448.
Yuge Huo, Yining Lu, Zhen Zhang, Hao Chen, and Yan
Lin. 2026.
Atommem: Learnable dynamic agen-
tic memory with atomic memory operation. arXiv
preprint arXiv:2601.08323.
Dongming Jiang, Yi Li, Guanpeng Li, and Bingzhe
Li. 2026.
Magma: A multi-graph based agentic
memory architecture for ai agents. arXiv preprint
arXiv:2601.03236.
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio
Petroni, Vladimir Karpukhin, Naman Goyal, Hein-
rich Küttler, Mike Lewis, Wen-tau Yih, Tim Rock-
täschel, et al. 2020. Retrieval-augmented generation
for knowledge-intensive nlp tasks. In Advances in
neural information processing systems, volume 33,
pages 9459–9474.
Jinbo Liu, Defu Cao, Yifei Wei, Tianyao Su, Yuan
Liang, Yushun Dong, Yan Liu, Yue Zhao, and
Xiyang Hu. 2025a. Topology matters: Measuring
memory leakage in multi-agent llms. arXiv preprint
arXiv:2512.04668.


Page 12:
Junming Liu, Yifei Sun, Weihua Cheng, Haodong
Lei, Yirong Chen, Licheng Wen, Xuemeng Yang,
Daocheng Fu, Pinlong Cai, Nianchen Deng, Yi Yu,
Shuyue Hu, Botian Shi, and Ding Wang. 2025b.
MemVerse: Multimodal memory for lifelong learn-
ing agents. arXiv preprint arXiv:2512.03627.
Jin Luo, Yu Tian, Cheng Cao, Zhi Luo, Hao Lin, Kang
Li, Cheng Kong, Rui Yang, and Jian Ma. 2026.
From storage to experience: A survey on the evo-
lution of llm agent memory mechanisms. Preprints.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler
Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,
Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,
et al. 2023.
Self-refine: Iterative refinement with
self-feedback.
In Advances in Neural Informa-
tion Processing Systems, volume 36, pages 46534–
46594.
Andrea Matarazzo and Riccardo Torlone. 2025. A sur-
vey on large language models with some insights
on their capabilities and limitations. arXiv preprint
arXiv:2501.04040.
Hongze Mi, Yibo Feng, WenJie Lu, Song Cao, Jinyuan
Li, Yanming Li, Xuelin Zhang, Haotian Luo,
Songyang Peng, He Cui, Tengfei Tian, Jun Fang,
Hua Chai, and Naiqiang Tan. 2026.
Darwinian
memory:
A training-free self-regulating memory
system for gui agent evolution.
arXiv preprint
arXiv:2601.22528.
Jiahui Nan, Wei Ma, Wei Wu, and Yuhong Chen.
2025.
Nemori:
Self-organizing agent memory
inspired by cognitive science.
arXiv preprint
arXiv:2508.03341.
Hongqiu Ni, Jiabao Zhang, Guopeng Li, Zilong Wang,
Ruiqi Wu, Chi Zhang, and Haisheng Tan. 2025.
Astraea: A state-aware scheduling engine for llm-
powered agents. arXiv preprint arXiv:2512.14142.
OpenAI. 2023. Gpt-4 system card. Technical report,
OpenAI.
Charles Packer, Sarah Wooders, Kevin Lin, Vivian
Fang, Shishir G. Patil, Ion Stoica, and Joseph E.
Gonzalez. 2024. Memgpt: Towards llms as oper-
ating systems. arXiv preprint arXiv:2310.08560.
Joon Sung Park, Joseph O’Brien, Carrie J. Cai, Mered-
ith Ringel Morris, Percy Liang, and Michael S.
Bernstein. 2023. Generative agents: Interactive sim-
ulacra of human behavior.
In Proceedings of the
36th annual acm symposium on user interface soft-
ware and technology, pages 1–22.
Ofir Press, Noah A. Smith, and Mike Lewis. 2021.
Train short, test long: Attention with linear biases
enables input length extrapolation. arXiv preprint
arXiv:2108.12409.
Hong Qian et al. 2024. Memorag: Boosting long con-
text processing with global memory-enhanced re-
trieval augmentation.
In Proceedings of the ACM
Web Conference 2025.
Peter Rasmussen, Pavel Paliychuk, Thomas Beauvais,
Jacob Ryan, and Daniel Chalef. 2025. Zep: a tem-
poral knowledge graph architecture for agent mem-
ory. arXiv preprint arXiv:2501.13956.
Abhinav Rath. 2026.
Agent drift:
Quantifying
behavioral degradation in multi-agent llm sys-
tems over extended interactions.
arXiv preprint
arXiv:2601.04170.
Ali Rezazadeh, Zhi Li, An Lou, Yang Zhao, Wei Wei,
and Yujia Bao. 2025. Collaborative memory: Multi-
user memory sharing in llm agents with dynamic ac-
cess control. arXiv preprint arXiv:2505.18279.
Saksham Sarin, Lakshay Singh, Bhaskar Sarmah, and
Dipti Mehta. 2025. Memoria: A scalable agentic
memory framework for personalized conversational
ai. In 2025 5th International Conference on AI-ML-
Systems, pages 32–39.
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao. 2023. Re-
flexion: Language agents with verbal reinforcement
learning. In Advances in Neural Information Pro-
cessing Systems, volume 36, pages 8634–8652.
Theodore
Sumers,
Shunyu
Yao,
Karthik
R.
Narasimhan,
and
Thomas
L.
Griffiths.
2023.
Cognitive
architectures
for
language
agents.
Transactions on Machine Learning Research.
Volker Tresp, Sahand Sharifzadeh, Hang Li, Dario
Konopatzki, and Yunpu Ma. 2023. The tensor brain:
A unified theory of perception, memory, and seman-
tic decoding. Neural Computation, 35(2):156–227.
Bin Wang, Wei He, Shu Zeng, Zhi Xiang, Yue Xing,
Jian Tang, and Peng He. 2025. Unveiling privacy
risks in llm agent memory. In Proceedings of the
63rd Annual Meeting of the Association for Compu-
tational Linguistics, pages 25241–25260.
Guanzhi Wang, Yuandong Xie, Yunfan Jiang, Ajay
Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
and Anima Anandkumar. 2023. Voyager: An open-
ended embodied agent with large language models.
arXiv preprint arXiv:2305.16291.
Kai Wang, Yuxuan Lin, Jian Lou, Zhen Zhou, Bobur
Suvonov, and Jian Li. 2026. E-mem: Multi-agent
based episodic context reconstruction for llm agent
memory. arXiv preprint arXiv:2601.21714.
Yue Wang and Xing Chen. 2025. Mirix: Multi-agent
memory system for llm-based agents. arXiv preprint
arXiv:2507.07957.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V. Le, Denny Zhou,
et al. 2022. Chain-of-thought prompting elicits rea-
soning in large language models.
In Advances in
neural information processing systems, volume 35,
pages 24824–24837.


Page 13:
Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang,
Kai-Wei Chang, and Dong Yu. 2025.
Long-
memeval: Benchmarking chat assistants on long-
term interactive memory.
Zhi Xi, Wen Chen, Xin Guo, Wei He, Yi Ding,
Bo Hong, Ming Zhang, Jian Wang, Sen Jin,
En Zhou, et al. 2023.
The rise and potential of
large language model based agents: A survey. arXiv
preprint arXiv:2309.07864.
Wei Xu, Ke Mei, Han Gao, Jian Tan, Zhen Liang, and
Yong Zhang. 2025. A-mem: Agentic memory for
llm agents. In Advances in Neural Information Pro-
cessing Systems.
Shi Yan, Xiao Yang, Zhi Huang, En Nie, Zheng Ding,
Zhe Li, Xiao Ma, Jian Bi, Kristian Kersting, Jeff Z.
Pan, et al. 2026. Memory-r1: Enhancing large lan-
guage model agents to manage and utilize mem-
ories via reinforcement learning.
arXiv preprint
arXiv:2508.19828.
Shunyu Yao, Jian Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2023.
React: Synergizing reasoning and acting in language
models. In International Conference on Learning
Representations (ICLR).
Woongyeong Yeo, Kangsan Kim, Jaehong Yoon, and
Sung Ju Hwang. 2025. WorldMM: Dynamic mul-
timodal memory agent for long video reasoning.
arXiv preprint arXiv:2512.02425.
Yufei Yin, Qianke Meng, Minghao Chen, Jiajun Ding,
Zhenwei Shao, and Zhou Yu. 2025.
VideoARM:
Agentic reasoning over hierarchical memory for
long-form video understanding.
arXiv preprint
arXiv:2512.12360.
Raquib Bin Yousuf, Aadyant Khatri, Shengzhe Xu,
Mandar Sharma, and Naren Ramakrishnan. 2025.
Can an llm induce a graph?
investigating mem-
ory drift and context length.
arXiv preprint
arXiv:2510.03611.
Hongli Yu, Tinghong Chen, Jiangtao Feng, Jiangjie
Chen, Weinan Dai, Qiying Yu, Ya-Qin Zhang, Wei-
Ying Ma, Jingjing Liu, Mingxuan Wang, and Hao
Zhou. 2025.
Memagent: Reshaping long-context
llm with multi-conv rl-based memory agent. arXiv
preprint arXiv:2507.02259.
Sizhe Yuen, Francisco Gomez Medina, Ting Su, Yali
Du, and Adam J. Sobey. 2026.
Intrinsic mem-
ory agents:
Heterogeneous multi-agent llm sys-
tems through structured contextual memory. arXiv
preprint arXiv:2508.08997.
Jiarui Zhang, Muxin Fu, Guancheng Wan, Miao Yu,
Kun Wang, and Shuicheng Yan. 2025. G-memory:
Tracing hierarchical memory for multi-agent sys-
tems. arXiv preprint arXiv:2506.07398.
Ningning Zhang, Xingxing Yang, Zhizhong Tan, Weip-
ing Deng, and Wenyong Wang. 2026a. Himem: Hi-
erarchical long-term memory for llm long-horizon
agents. arXiv preprint arXiv:2601.06377.
Yuxiang Zhang, Jiangming Shu, Ye Ma, Xueyuan Lin,
Shangxi Wu, and Jitao Sang. 2026b. Memory as ac-
tion: Autonomous context curation for long-horizon
agentic tasks. arXiv preprint arXiv:2510.12635.
Bo Zheng et al. 2024. Agent workflow memory. arXiv
preprint arXiv:2409.07429.
Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and
Yanlin Wang. 2024. Memorybank: Enhancing large
language models with long-term memory. In Pro-
ceedings of the AAAI Conference on Artificial Intel-
ligence, volume 38, pages 19724–19731.

