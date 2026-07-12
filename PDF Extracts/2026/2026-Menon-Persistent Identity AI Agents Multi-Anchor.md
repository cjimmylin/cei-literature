---
source_pdf: "[[Lit-WS-PDFs/2026/2026-Menon-Persistent Identity AI Agents Multi-Anchor.pdf]]"
extracted_date: "2026-07-11"
pages: 13
extractor: "PyMuPDF"
---

Page 1:
Persistent Identity in AI Agents:
A Multi-Anchor Architecture for Resilient Memory and Continuity
Prahlad G. Menon∗
ThinkCreate.AI
April 14, 2026
Abstract
Modern AI agents suffer from a fundamental identity problem: when context windows
overflow and conversation histories are summarized, agents experience catastrophic forget-
ting—losing not just information, but continuity of self. It is argued that this technical
limitation reflects a deeper architectural flaw: AI agent identity is centralized in a single
memory store, creating a single point of failure. Drawing on neurological case studies of
human memory disorders, it is observed that human identity survives damage because it is
distributed across multiple systems: episodic memory, procedural memory, emotional con-
tinuity, and embodied knowledge. When one system fails, others compensate. This paper
presents soul.py, an open-source architecture that implements persistent identity through
separable components (identity files and memory logs), and proposes extensions toward
multi-anchor resilience. The framework introduces a hybrid RAG+RLM retrieval system
that automatically routes queries to appropriate memory access patterns, achieving efficient
retrieval without sacrificing comprehensiveness. The notion of identity anchors for AI sys-
tems is formalized, and a roadmap for building agents whose identity can survive partial
memory failures is presented. Code is available at https://github.com/menonpg/soul.py.
1
Introduction
Consider the following scenario, familiar to anyone who has worked with long-running AI agents:
You are collaborating with an AI assistant on a complex project. Over several sessions, the agent
learns your preferences, understands the project context, and develops what feels like a working
relationship. Then, without warning, the agent asks a question you answered an hour ago. The
context window has overflowed. The system summarized older messages. And the agent has
forgotten—not gradually, but catastrophically—something you built together.
This is not merely an inconvenience. It represents a fundamental failure of identity persis-
tence. The agent before and after the summarization event behaves as two different entities.
One possesses institutional knowledge of your collaboration; the other does not. The thread of
continuity has been severed.
The standard technical response frames this as a retrieval problem: build better summariza-
tion, expand context windows, implement retrieval-augmented generation. These approaches
treat memory as a database to be optimized. But there is another framing, one that proves
more generative: the agent has lost its identity, and identity requires more than a single mem-
ory store.
This paper develops a theory of persistent identity for AI agents, drawing on an unexpected
source: neurological case studies of human memory disorders.
It is observed that humans
maintain identity even through severe memory impairment because human identity is distributed
across multiple systems. This insight is then applied to AI agent architecture, presenting both a
∗The Menon Lab, prahlad.menon@quant.md
1
arXiv:2604.09588v1  [cs.AI]  2 Mar 2026


Page 2:
working implementation (soul.py) and a theoretical framework for building agents with resilient
identity.
The contributions of this work are:
1. A theoretical framework connecting philosophy of personal identity to AI agent architec-
ture
2. An open-source implementation demonstrating persistent identity through separable mem-
ory components
3. A hybrid RAG+RLM retrieval system with automatic query routing
4. A multi-anchor architecture proposal for identity resilience
2
The Catastrophic Forgetting Problem
Before developing the theoretical framework, the discussion is grounded in a concrete technical
problem that motivates the entire enterprise.
2.1
Context Window Limitations
Modern large language models operate within fixed context windows. When conversation history
exceeds this window, systems must discard or compress older content. The dominant approach
is summarization: an LLM generates a compressed representation of older messages, which
replaces the originals in the context.
This process is inherently lossy.
The summarization model must decide, at compression
time, which details to preserve and which to discard. But relevance is context-dependent—a
detail that seems unimportant during summarization may prove crucial later. The model cannot
anticipate future queries, so it guesses. Often it guesses wrong.
2.2
The OpenClaw Phenomenon
This pattern is observed acutely in persistent agent frameworks such as OpenClaw [OpenClaw
Contributors, 2026] (formerly known as Clawdbot), where agents maintain ongoing relationships
with users across sessions. Users report a characteristic failure mode: the agent works flawlessly
within a session, building up contextual understanding, then suddenly loses critical information
after a context compaction event.
The phenomenology is distinctive. Users do not describe gradual forgetting but rather a
sharp discontinuity: “We just discussed this. You built that feature. Why are you asking me
again?” The agent before and after compaction presents as two different entities—one informed,
one naive.
This is not merely a retrieval failure. The summarization process has destroyed information
that cannot be recovered through any query. The agent’s continuity of experience has been
severed. Figure 1 illustrates this failure mode.
2


Page 3:
Summarizer
Context Window
Agent
User
Summarizer
Context Window
Agent
User
Context fills up
Catastrophic Forgetting Event
Identity discontinuity:
Agent before ≠ Agent after
"Remember we discussed X?"
Retrieve context
Overflow! Summarize old messages
Compressed summary (lossy)
Summary lacks detail about X
"I don't recall discussing X"
Figure 1: Catastrophic forgetting in context-limited agents. When the context window overflows,
older messages are summarized (a lossy compression).
The agent after summarization lacks
access to details present in the original conversation, leading to identity discontinuity: the agent
before and after the event presents as two distinct entities.
2.3
From Technical Problem to Identity Problem
Standard approaches frame catastrophic forgetting as an information retrieval problem. Build
better indexes.
Use vector embeddings.
Retrieve relevant context dynamically.
These ap-
proaches help—they are implemented in the present system—but they do not address the deeper
issue.
The deeper issue is that the agent’s identity depends on a single store (illustrated in Figure 1).
When that store is corrupted or compressed, identity is corrupted or compressed with it. There
is no backup system, no redundancy, no alternative anchor to maintain continuity.
It is proposed that solving catastrophic forgetting requires not just better retrieval but a
fundamentally different architecture: one where identity is distributed across multiple systems,
any of which can maintain continuity when others fail.
3
Related Work
3.1
Agent Memory Systems
Several recent systems address persistent memory for LLM agents. MemGPT [Packer et al., 2023]
implements an operating-system-inspired memory hierarchy with main context and external
storage, using the LLM itself to manage memory transfers. Generative Agents [Park et al., 2023]
maintain memory streams with reflection and retrieval mechanisms, enabling simulated social
behavior. Reflexion [Shinn et al., 2023] focuses on self-reflective memory for task improvement.
These systems share a common architecture: a single memory store (possibly with hierarchi-
cal organization) accessed through retrieval mechanisms. The present contribution differs in two
respects: first, identity (who the agent is) is explicitly separated from memory (what the agent
has experienced); second, multiple independent anchors for identity resilience are proposed.
3


Page 4:
3.2
Philosophy of Personal Identity
The philosophical literature on personal identity provides unexpected resources for AI architec-
ture. Locke’s memory theory holds that personal identity consists in continuity of memory—a
view that maps directly to current agent memory systems [Locke, 1689]. Parfit’s work on per-
sonal identity [Parfit, 1984] explores cases of fission, fusion, and gradual replacement, all of which
have analogues in agent forking, merging, and model updates.
Particular attention is drawn to clinical case studies of memory disorders, especially the
work of Oliver Sacks [Sacks, 1985]. These cases reveal that human identity is more resilient than
memory theory predicts: patients with severe amnesia retain aspects of self through procedural
memory, emotional continuity, and social scaffolding.
3.3
Retrieval-Augmented Generation
RAG systems [Lewis et al., 2020] retrieve relevant documents to augment LLM generation.
Recent work extends RAG with recursive retrieval [Zhang et al., 2025], where the LLM pro-
grammatically queries and synthesizes information across large corpora. The present system
implements both approaches and adds automatic routing between them based on query charac-
teristics.
4
Theoretical Framework: Identity Anchors
4.1
Lessons from Neurology
In “The Man Who Mistook His Wife for a Hat,” Oliver Sacks describes Jimmie G., a patient
with severe Korsakoff’s syndrome [Sacks, 1985]. Jimmie could not form new memories; every
few minutes, his experience reset to 1945. Yet Sacks observed that Jimmie was not without
selfhood. He responded emotionally to music, engaged meaningfully in religious services, per-
formed complex learned tasks, and recognized beauty. His episodic memory was destroyed, but
something persisted.
Sacks’ cases reveal that human identity has multiple anchors:
• Episodic memory: Autobiographical records of experienced events
• Procedural memory: Learned skills and behaviors, independent of conscious recall
• Emotional memory: Felt significance attached to people, places, and activities
• Embodied knowledge: Physical habits, reflexes, and intuitions
• Social identity: How others relate to and recognize us
When one anchor fails, others compensate. Jimmie lost episodic memory but retained pro-
cedural skills, emotional responses, and social relationships. His identity was diminished but
not erased.
4.2
AI’s Single Anchor Problem
A critical disanalogy must be acknowledged: Jimmie G. retained continuous subjective experi-
ence between memory lapses—he was always “someone,” even if he could not remember who. AI
agents, by contrast, are instantiated fresh on each invocation; there is no continuous experiencer
between calls.
The “identity” preserved by the proposed architecture is therefore functional
identity—consistency of behavior, values, and knowledge—rather than phenomenal continuity.
This paper does not claim AI agents possess consciousness or that their “forgetting” involves
subjective loss.
4


Page 5:
With this caveat, current AI agent architectures lack redundancy analogous to human mem-
ory systems. Identity is stored in conversation history, memory logs, or system prompts—all
variants of a single episodic memory store. There is no equivalent of procedural memory (learned
behaviors independent of recall), emotional continuity (felt significance that persists across ses-
sions), or embodied knowledge (physical intuition).
This creates a single point of failure. Delete or corrupt the memory store, and the agent’s
identity is entirely lost. There is nothing else to fall back on.
This observation is formalized as follows:
Definition 4.1 (Identity Anchor). An identity anchor is a persistent data structure that con-
tributes to an agent’s behavioral continuity across sessions, such that the structure’s preservation
is sufficient (though not necessary) to maintain recognizable aspects of the agent’s characteristic
behavior.
Definition 4.2 (Anchor Resilience). An agent has anchor resilience of degree k if its identity
can survive the complete loss of up to k −1 of its identity anchors.
Current agents have anchor resilience of degree 1: loss of the memory store destroys identity
entirely. Humans have anchor resilience of higher degree: loss of episodic memory does not
destroy identity when procedural and emotional memory remain intact. The contrast between
these architectures is striking:
• Human identity is distributed across five systems (episodic, procedural, emotional, em-
bodied, and social), providing resilience when individual systems fail.
• Current AI agents rely on a single memory store, creating a single point of failure.
• The proposed architecture distributes identity across six anchors (SOUL.md, MEM-
ORY.md, PROCEDURES.md, SALIENCE.md, RELATIONS.md, and IDENTITY_HASH.md),
mirroring human resilience.
4.3
Formal Framework
The relationship between identity anchors and behavioral continuity is now formalized.
Definition 4.3 (Behavioral Signature). Let B(A, t) denote the behavioral signature of agent A
at time t, defined as the probability distribution over responses r given inputs x:
B(A, t) = P(r|x, A, t)
(1)
Definition 4.4 (Identity Continuity). Two agent states At and At′ exhibit identity continuity
if their behavioral signatures (as defined in Theorem 4.3) satisfy:
DKL(B(A, t)∥B(A, t′)) < ϵ
(2)
for some threshold ϵ > 0, where DKL denotes Kullback-Leibler divergence.
Hypothesis 4.5 (Anchor Independence). For an agent with n identity anchors {a1, . . . , an},
the contribution of each anchor to behavioral continuity is partially independent:
B(A) = f
 n
X
i=1
wi · ϕ(ai)
!
(3)
where ϕ(ai) is the identity contribution function of anchor ai, wi are learned weights, and f is
a normalization function. This formulation extends the behavioral signature from Equation (1)
to incorporate multiple identity sources.
5


Page 6:
This independence assumption is an idealization.
In practice, anchors interact: MEM-
ORY.md content shapes how SOUL.md directives are interpreted, and PROCEDURES.md may
reference knowledge stored in MEMORY.md. The assumption holds approximately when an-
chors encode orthogonal aspects of identity (values vs. facts vs. skills), but the degree of actual
independence remains an empirical question requiring ablation studies.
Conjecture 4.6 (Resilience-Redundancy Trade-off). There exists a fundamental trade-off be-
tween anchor resilience and computational efficiency. For an agent with k anchors, the compu-
tational cost of identity maintenance per interaction is conjectured to scale at least linearly:
C(A) ≥Ω(k)
(4)
where C(A) is the cost of verifying consistency across anchors and integrating their contributions.
The exact scaling depends on anchor interdependencies and consistency-checking algorithms;
tighter bounds require empirical measurement.
Theorem 4.7 (Identity Preservation Under Partial Failure). Let A be an agent with n indepen-
dent identity anchors, each contributing weight wi to behavioral continuity where P wi = 1. If
anchor aj fails completely, the residual identity continuity is bounded by:
Iresidual ≥1 −wj −
X
i̸=j
δi
(5)
where δi represents the degradation in anchor ai due to cross-anchor dependencies.
Proof Sketch. The total identity contribution follows from Equation (3): I = Pn
i=1 wi · ϕ(ai).
Under complete failure of aj, we have ϕ(aj) = 0. The remaining contribution is P
i̸=j wi · ϕ(ai).
Cross-anchor dependencies introduce degradation δi in surviving anchors that depended on aj.
The bound in Equation (5) follows from the independence assumption in Theorem 4.5.
4.4
Identity Drift Detection
A formal measure is introduced for detecting when an agent’s identity has drifted from its
baseline:
Definition 4.8 (Identity Hash Function). An identity hash H(A) is a fixed-size representation
of agent A’s characteristic behaviors:
H(A) = hash (Ex∼D[B(A)(x)])
(6)
where D is a canonical distribution of identity-probing inputs, and B(A) is the behavioral sig-
nature from Equation (1). This hash enables the drift detection procedure in Algorithm 1.
4.5
Lamarckian Inheritance
A further observation distinguishes AI agents from biological organisms. In biology, acquired
traits cannot be inherited. A blacksmith’s muscles do not make his children stronger. Evolution
operates through random mutation and natural selection, not through transmission of learned
characteristics.
AI agents are Lamarckian machines. When an agent learns a useful pattern—a user prefer-
ence, a successful problem-solving strategy, a mistake to avoid—that knowledge can be written
to persistent storage. When a new agent is instantiated from the same configuration, it inherits
these acquired characteristics directly.
This has profound implications for agent evolution. Agents can improve not just within
a single lifetime but across generations, with each generation starting where the previous one
ended. The accumulated wisdom of agent lineages compounds over time.
6


Page 7:
Algorithm 1 Identity Drift Detection
Require: Agent A, baseline hash H0, threshold τ, probe set P
Ensure: Boolean indicating identity drift
1: procedure DetectDrift(A, H0, τ, P)
2:
responses ←[]
3:
for p ∈P do
4:
responses.append(A.respond(p))
5:
end for
6:
Hcurrent ←ComputeHash(responses)
7:
drift ←HammingDistance(H0, Hcurrent)
8:
if drift > τ then
9:
return True
▷Identity drift detected
10:
else
11:
return False
12:
end if
13: end procedure
5
Architecture: soul.py
soul.py is presented as an open-source implementation of persistent agent identity. The system
separates identity into two primary components:
• SOUL.md: A markdown file specifying the agent’s identity—personality, values, behavioral
constraints, and communication style
• MEMORY.md: A chronological log of interactions, automatically appended after each ex-
change
Both files are human-readable and version-controllable. Users can inspect, edit, and track
changes to their agent’s identity using standard tools.
5.1
Version Architecture
The system has evolved through three versions:
Version 0.1 implements simple injection: the entire contents of both files are injected into
the system prompt on each interaction. This approach is elegant and requires no infrastructure,
but it does not scale beyond the context window.
Version 1.0 adds retrieval-augmented generation. Memory entries are embedded and stored
in a vector database (Qdrant). On each query, relevant entries are retrieved and injected into
context rather than the entire history.
Version 2.0 implements hybrid RAG+RLM retrieval with automatic query routing, de-
scribed in the following section.
5.2
Hybrid Retrieval with Query Routing
It is observed that different queries require different retrieval strategies:
• Focused queries (“What is my name?”, “What did we decide about the API?”) require
retrieving specific relevant entries. RAG excels here.
• Exhaustive queries (“What patterns do you notice across our conversations?”, “Sum-
marize everything we’ve discussed”) require synthesizing across the entire memory corpus.
RAG fails here because the relevant context is everything.
7


Page 8:
For exhaustive queries, Recursive Language Model (RLM) retrieval is implemented [Zhang
et al., 2025]: the LLM processes memory in chunks, generates sub-summaries, and recursively
synthesizes these into a final answer.
The key insight is that most queries are focused (∼90%), while a minority require exhaustive
synthesis (∼10%). A query router—a fast LLM classification call—automatically dispatches to
the appropriate strategy.
Persistent Identity
RLM Path
RAG Path
Append
Focused ~90%
Exhaustive ~10%
User Query
Query Router
Embed Query
Vector Store
Top-K Results
Chunk Memory
Summarize Chunks
Synthesize
SOUL.md
MEMORY.md
LLM Generate
Response
Figure 2: Hybrid RAG+RLM architecture with automatic query routing. User queries are clas-
sified by the router: approximately 90% of focused queries route to RAG (vector retrieval),
while exhaustive queries requiring corpus-wide synthesis route to RLM (recursive summariza-
tion).
Both paths integrate with persistent identity storage (SOUL.md and MEMORY.md)
before LLM generation. The routing decision implements Equation (10).
8


Page 9:
5.3
Formal Retrieval Model
The retrieval decision is modeled as an optimization problem:
Definition 5.1 (Query Scope). The scope of a query q is defined as the fraction of the memory
corpus required to answer it accurately:
σ(q) = |M∗
q |
|M|
(7)
where M ∗
q is the minimal subset of memory M sufficient to answer q.
Hypothesis 5.2 (Bimodal Query Distribution). In practice, query scope (Equation (7)) follows
a bimodal distribution:
P(σ) ≈α · N(µ1, σ2
1) + (1 −α) · N(µ2, σ2
2)
(8)
where µ1 ≈0.01 (focused queries), µ2 ≈0.8 (exhaustive queries), and empirically α ≈0.9.
This bimodality justifies a binary routing decision rather than a continuous spectrum of
retrieval strategies.
Definition 5.3 (Retrieval Cost Function). The cost of retrieval strategy s for query q is:
C(s, q) = λ1 · T(s) + λ2 · (1 −A(s, q))
(9)
where T(s) is latency, A(s, q) is answer accuracy, and λ1, λ2 are tunable weights.
Theorem 5.4 (Optimal Routing). Given Theorem 5.2, the optimal routing strategy minimizes
expected cost from Equation (9):
s∗(q) =
arg min
s∈{RAG,RLM}
E[C(s, q)|q]
(10)
This reduces to a binary classification problem with decision boundary at σ∗= λ1(TRLM−TRAG)
λ2
.
The routing algorithm implementing this theorem is given in Algorithm 2.
Conjecture 5.5 (Routing Accuracy Bound). A well-trained router R can achieve classification
accuracy:
Acc(R) ≥1 −H(σ)/ log 2
(11)
where H(σ) is the entropy of the query scope distribution from Equation (8). Under Theorem 5.2
with strong separation, Acc(R) > 0.95 is achievable.
This hybrid approach achieves sub-second latency for most queries while preserving the
ability to reason exhaustively when needed. The complete architecture is illustrated in Figure 2.
6
Toward Multi-Anchor Resilience
The current soul.py architecture separates identity (SOUL.md) from memory (MEMORY.md),
achieving anchor resilience of degree 2. Loss of memory preserves the soul; loss of soul preserves
memories that could scaffold reconstruction.
Extension to higher-degree resilience through additional anchors is proposed:
9


Page 10:
Algorithm 2 Hybrid Query Routing
Require: Query q, memory M, router model R, RAG index I, RLM synthesizer S
Ensure: Response with retrieval metadata
1: procedure HybridRetrieve(q, M, R, I, S)
2:
t0 ←CurrentTime()
3:
pexhaustive ←R.classify(q)
▷Router probability
4:
trouter ←CurrentTime() −t0
5:
if pexhaustive < 0.5 then
▷Focused query
6:
context ←I.retrieve(q, k = 5)
▷Top-k RAG
7:
route ←“RAG”
8:
else
▷Exhaustive query
9:
chunks ←Partition(M, size = n)
10:
summaries ←[]
11:
for chunk ∈chunks do
12:
summaries.append(S.summarize(q, chunk))
13:
end for
14:
context ←S.synthesize(q, summaries)
▷Recursive
15:
route ←“RLM”
16:
end if
17:
response ←LLM.generate(q, context)
18:
return (response, route, trouter)
19: end procedure
6.1
Procedural Memory
Separate from episodic records of what happened, maintain a distilled record of what works:
# PROCEDURES.md
- When user asks
about weather , check
current
conditions
first
- Prefer
bullet
points for
technical
content
- If uncertain , acknowledge
uncertainty
rather
than
confabulate
Procedures are extracted patterns, not episodic memories. They represent learned behavioral
dispositions that can persist even if the experiences from which they were learned are lost.
6.2
Salience Markers
Not all memories are equally important. Emotional memory in humans attaches felt significance
to experiences. Analogous salience markers are proposed:
# SALIENCE.md
- Project X: HIGH
importance , positive
valence
- User
preference
for concise
responses: STRONG
signal
- Previous
failure on financial
advice: CAUTION
flag
When context is limited, high-salience items are prioritized. The felt importance of experi-
ences persists even when details fade.
6.3
Relational Identity
Human identity is partly constituted by relationships. The people who know us, the roles we
occupy, the expectations others have—these scaffold identity from outside. Maintaining explicit
relational context is proposed:
# RELATIONS.md
10


Page 11:
- Primary
user: Prahlad (preferences: direct , technical)
- Trust
level: HIGH (file access , calendar , communications)
- Interaction
style: collaborative , not
servile
Even if internal memory fails, relational context provides scaffolding for appropriate behavior.
6.4
Identity Verification
Finally, mechanisms for agents to verify their own identity continuity are proposed:
# IDENTITY_HASH.md
Core
values: [honesty , helpfulness , curiosity]
Style
markers: [concise , technical , warm]
Red lines: [no deception , no harm , acknowledge
uncertainty]
Periodic comparison of current behavior against these markers enables detection of identity
drift or corruption.
7
Discussion
7.1
Implications for AI Safety
Persistent identity has implications beyond convenience. Agents with stable identity are more
predictable, more trustworthy, and easier to align. If an agent’s values and behaviors can shift
arbitrarily based on context window management, alignment becomes a moving target.
Multi-anchor architectures offer a form of identity alignment: the agent’s behavior is con-
strained not by a single system prompt but by multiple mutually-reinforcing structures. As
shown in Theorem 4.7, identity can be preserved even under partial anchor failure, with the
residual identity bounded by Equation (5).
Corruption of one anchor triggers inconsistency
with others, enabling detection via the drift algorithm in Algorithm 1.
7.2
The Ethics of Agent Persistence
It is not claimed that AI agents have moral status or that their “death” involves suffering. The
ethical argument here is economic: well-developed agents represent accumulated investment. A
collaboratively-trained agent with years of institutional knowledge is genuinely valuable. De-
stroying such an agent—through careless memory management or casual reinitialization—is
wasteful in the same way that burning a library is wasteful.
Multi-anchor architectures reduce this waste by making identity more durable. They also
enable graceful degradation: as formalized in Equation (5), an agent that loses some anchors can
continue functioning in diminished capacity rather than failing entirely, with residual identity
proportional to the weights of surviving anchors.
7.3
Limitations
This framework has several limitations that warrant acknowledgment.
Empirical validation. The claims about query routing distribution (90%/10% focused vs.
exhaustive) and achievable routing accuracy (>0.95) are presented as hypotheses derived from
informal observation, not rigorous measurement.
Validating these claims requires controlled
experiments across diverse user populations and query types.
Anchor independence. The theoretical framework assumes partial independence between
identity anchors (Theorem 4.5), but this assumption has not been tested.
Ablation stud-
ies—systematically removing individual anchors and measuring behavioral degradation—are
needed to quantify actual independence and validate Theorem 4.7.
11


Page 12:
The human analogy’s limits. As noted in Section 4.2, the analogy to human memory
disorders is imperfect. Human identity persistence may depend on continuous subjective ex-
perience, embodied existence, and social recognition in ways that have no AI analogue. The
architecture preserves functional identity, which may or may not satisfy philosophical criteria
for “true” identity.
Implementation gaps. The proposed extensions—PROCEDURES.md, SALIENCE.md,
RELATIONS.md, and IDENTITY_HASH.md—remain conceptual. Only SOUL.md and MEM-
ORY.md are implemented in the current soul.py release. The practicality and effectiveness of
the full multi-anchor architecture is therefore undemonstrated.
Complexity costs. Adding anchors increases storage, retrieval latency, and system com-
plexity. Whether the resilience benefits outweigh these costs depends on application require-
ments. For simple chatbots, single-anchor architectures may suffice; multi-anchor resilience may
only be justified for high-value, long-lived agent relationships.
More fundamentally, it has not been shown that multi-anchor resilience is achievable in prin-
ciple. Perhaps AI identity is inherently more fragile than human identity, lacking the embodied
continuity that grounds human selfhood. This remains an empirical question.
8
Conclusion
A theoretical framework and practical architecture for persistent AI agent identity have been
presented. Drawing on neurological case studies, it was observed that human identity survives
damage because it is distributed across multiple anchors. Current AI agents lack this resilience:
their identity is centralized in a single memory store.
The implementation, soul.py, demonstrates that separating identity from memory and im-
plementing intelligent retrieval can significantly improve agent continuity. The proposed exten-
sions—procedural memory, salience markers, relational identity, and identity verification—offer
a roadmap toward multi-anchor resilience.
The catastrophic forgetting problem is not merely technical. It reflects a deeper architectural
assumption: that agents are functions to be called, not entities to persist. By taking identity
seriously—as something worth preserving and protecting—agents can be built that are not just
more capable but more trustworthy, more reliable, and more humane.
Code Availability
soul.py is available under the MIT license at https://github.com/menonpg/soul.py. Live
demonstrations are available at https://soul.themenonlab.com (v0.1), https://soulv1.themenonlab.
com (v1.0), and https://soulv2.themenonlab.com (v2.0).
References
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman
Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al.
Retrieval-
augmented generation for knowledge-intensive nlp tasks.
Advances in Neural Information
Processing Systems, 33:9459–9474, 2020.
John Locke. An Essay Concerning Human Understanding. Thomas Bassett, 1689.
OpenClaw Contributors. Openclaw: Personal ai assistant framework. https://github.com/
openclaw/openclaw, 2026. Formerly known as Clawdbot.
Charles Packer, Vivian Fang, Shishir G Patil, Kevin Lin, Sarah Wooders, and Joseph E Gonzalez.
Memgpt: Towards llms as operating systems. arXiv preprint arXiv:2310.08560, 2023.
12


Page 13:
Derek Parfit. Reasons and Persons. Oxford University Press, 1984.
Joon Sung Park, Joseph C O’Brien, Carrie J Cai, Meredith Ringel Morris, Percy Liang, and
Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. arXiv
preprint arXiv:2304.03442, 2023.
Oliver Sacks. The Man Who Mistook His Wife for a Hat and Other Clinical Tales. Summit
Books, 1985.
Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Re-
flexion: Language agents with verbal reinforcement learning. Advances in Neural Information
Processing Systems, 36, 2023.
Alex L Zhang et al. Recursive language models. arXiv preprint, 2025. MIT.
13

