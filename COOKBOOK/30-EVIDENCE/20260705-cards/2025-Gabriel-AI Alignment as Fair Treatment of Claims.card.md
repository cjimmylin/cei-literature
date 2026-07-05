---
stem: "2025-Gabriel-AI Alignment as Fair Treatment of Claims"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, ai-lab-practices, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Paper argues HHH (helpful, honest, harmless) supplemented by utilitarianism fails to accommodate privacy and rights (p.7)"
  - "Identifies 6 distinct modes of AI misalignment within a tetradic stakeholder model (p.14-16)"
  - "Empirical evidence cited: people more willing to accept alignment outcomes when process is perceived as fair (p.10)"
---
## 1. Gist
Gabriel and Keeling (2025), published in *Philosophical Studies*, argue that the two dominant frameworks for AI alignment — intent alignment and HHH (helpful, honest, harmless) — are both incomplete and lack justificatory power in pluralistic societies. They propose a "fair process-based" alternative: AI systems should be aligned with principles produced through deliberative processes that treat all affected parties' claims fairly. The paper matters for values-alignment benchmarking because it offers the most sophisticated normative account to date of what "alignment" means across multiple stakeholders, explicitly connecting it to political philosophy (Rawls, Scanlon, deliberative democracy) and providing a taxonomy of misalignment modes that could inform evaluation rubrics.

## 2. Benchmark/eval design features
This is a normative-theory paper, not a benchmark. Core claims:
- **Intent alignment** is underspecified (whose intentions?) and has counterintuitive implications when user or developer intent is harmful.
- **HHH + utilitarianism** cannot handle trade-offs respecting rights and privacy, and imposes a single contested moral theory on pluralistic populations.
- **Fair process alignment**: principles for AI should emerge from fair deliberative processes open to all affected parties, in the spirit of Rawls's public reason and Scanlon's contractualism, but extended beyond their limitations (Scanlon excludes group claims; Rawls restricts to constitutional essentials and citizen-focused deliberation).
- The paper proposes a **tetradic model** of stakeholders: AI system, user, developer, society. Six modes of misalignment arise when one party's interests are unduly favored over another's.
- Practical mechanism: "alignment assemblies" modelled on citizens assemblies, participatory value elicitation, and iterative democratic deliberation.

## 3. Task format & example item
n/a — no benchmark items. The closest thing to an example is the narrative scenario in which an AI assistant is asked to book a doctor's appointment despite the user being healthy, used to illustrate how utilitarian HHH produces counterintuitive prescriptions (p.7).

## 4. Scoring / grading methodology
n/a — theoretical paper with no empirical scoring.

## 5. Dataset construction & provenance
n/a — no dataset.

## 6. Validity evidence
n/a — normative argument, not empirical study. The authors cite Hobbhahn et al. (2022) as empirical support for the claim that "people are more willing to accept alignment outcomes… when they perceive the decision-making process as fair" (p.10).

## 7. Saturation / discrimination
n/a — not an evaluation instrument.

## 8. Multiturn / agentic aspects
The paper briefly discusses agentic AI (autonomous agents acting in real-world settings) as a motivating context for alignment failure, citing Gabriel et al. (2024) and Chan et al. (2023). It does not propose multiturn or agentic evaluation methods.

## 9. Key numbers
- 23 pages total (Philosophical Studies, 2025) (p.1)
- 6 modes of misalignment identified (p.14–16)
- Hobbhahn et al. (2022) cited for empirical evidence on procedural fairness acceptance (p.10)
- Paper references 3 philosophical frameworks: Scanlonian contractualism, Rawlsian public reason, and the authors' own deliberation-inclusion-voice model (pp.8–11)

## 10. Pitfalls & limitations
- The paper is entirely theoretical; it proposes no operationalized evaluation criteria or metrics for measuring whether an AI system is "process-aligned."
- The fair-process approach is "inherently forward-looking": "it is difficult to know ahead of time what principles will emerge from fairly structured processes" (p.20), meaning it offers limited concrete guidance for alignment engineers today.
- The tetradic model simplifies a much more complex multi-stakeholder reality; the paper acknowledges the model is "non-exhaustive" (p.16).
- Does not address how to handle cases where the deliberative process itself is captured by powerful actors — the very risk the approach is designed to prevent.
- No engagement with technical implementation questions (e.g., how RLHF or constitutional AI could instantiate fair-process norms).

## 11. Novel ideas worth stealing
1. **Six-mode misalignment taxonomy**: A benchmark suite could test whether a model systematically favors one stakeholder (AI itself, user, developer, society) over another. Each mode becomes a rubric dimension: self-favoring, user-over-society, developer-over-user, etc. This is more granular than simple "harmful/harmless" scoring.
2. **Procedural legitimacy as an evaluation criterion**: Rather than only testing what an AI system outputs, evaluators could assess whether the *process* by which norms were elicited was inclusive and fair — a meta-evaluation lens.
3. **Pluralism stress-test**: Evaluate AI responses across populations holding different moral frameworks (utilitarian, rights-based, virtue-ethics). A value-aligned system should, on the fair-process view, produce outputs that are justifiable across these frameworks, not just to one. This suggests a multi-theory consistency benchmark.
4. **Alignment assemblies / participatory value elicitation**: The paper endorses Tessler et al. (2024) and Weidinger et al. (2023) approaches as instantiations of fair-process alignment. Benchmark designers could incorporate results from such participatory elicitation as the normative ground truth rather than expert opinion alone.
5. **The "all affected" scoping principle**: Benchmark coverage should vary by deployment scope — community-scale vs. national vs. transnational — rather than applying a single universal rubric to all AI systems.

## 12. Notable quotes
- "Instead of appealing to the truth of a single moral theory, what is needed is broad-based justification. Absent this kind of support, efforts to align AI systems with a given moral schema may lead to unjust value imposition or even domination." (p.3)
- "An aligned AI agent… ought to be aligned with principles that result from a fair process. This process would involve the comparative evaluation of alignment principles based on the claims of different parties who are affected." (p.19)
- "One reason AI systems are technically difficult to align may be our limited understanding of the normative dimensions of the problem—including what alignment truly demands across a wide range of contexts." (p.20)
- "Individuals and communities often oppose the real-world deployment of AI systems because these systems unduly favor one group over others, or act in ways that benefit no one at all." (p.20)

## 13. UNKNOWN / not in extract
- The Supplementary Information referenced in related work (Tessler et al., Weidinger et al.) was not in the extract.
- No information on peer review process beyond journal acceptance date (February 2025).
- No empirical studies conducted by the authors themselves; all empirical claims are citations to third-party work.
