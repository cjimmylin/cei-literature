---
stem: "2024-Varshney-Decolonial AI Alignment - Openness Visesa-Dharma and Including"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, cultural-linguistic, pluralism-aggregation, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Six mechanisms of colonial AI identified: extractivism, automation, sociological essentialism, surveillance, containment, plus moral absolutism (new, p.6)"
  - "Three desiderata for decolonial alignment proposed; LoRA identified as the accessible alignment technology (p.11–12)"
---
## 1. Gist
This theoretical position paper argues that mainstream LLM alignment practices are a form of colonialism, specifically through the mechanism of "ethical essentialism" or moral absolutism. The author (an IBM Research scientist of Hindu background) contends that major model providers (Anthropic, OpenAI, Meta) impose Western moral philosophy as universal when delivering closed or semi-open LLMs via APIs, thereby committing epistemic violence against non-Western value systems. The paper proposes decolonial AI alignment grounded in the tradition of Hinduism — a non-dogmatic, non-absolutist, pluralistic moral philosophy — and specifically the concept of viśeṣa-dharma (context-specific right behavior). A concrete reference architecture using open models, LoRA fine-tuning, and a contextual bandit orchestrator is sketched. This paper matters profoundly for values-alignment benchmarking: it is one of the most philosophically developed arguments for why current benchmark-based alignment approaches are inadequate, and it provides a vocabulary and framework for thinking about pluralistic, context-sensitive evaluation.

## 2. Benchmark/eval design features
Theory and position paper; no benchmark is designed or evaluated. Core arguments relevant to benchmark design:
- Current alignment technologies (RLHF, RLAIF, constitutional AI, prompt engineering, guardrails) all assume universal values and Western epistemologies, and are not contextually adaptable (Section 3).
- Anthropic's constitution for Claude includes the UN Universal Declaration of Human Rights — itself subject to moral universalism and coloniality (p.10, fn.10).
- Context-specific (viśeṣa) harms "do not have existing benchmarks given their unique nature" (p.14 / Section 4.2.5).
- Evaluation and auditing for viśeṣa-dharma "will require innovation that may be developed hand-in-hand with eliciting and representing values" (p.14).
- Three desiderata: (1) open models permitting community-specific tuning; (2) values from communities not assumed universal; (3) values expressible in non-commandment epistemologies.

## 3. Task format & example item
n/a — theoretical paper; no experimental items.

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
n/a — no dataset created. The paper references empirical literature showing West-centric biases in LLMs (e.g., Benkler et al. 2023 World Values Survey analysis, Durmus et al. 2023 global opinions study) but does not conduct its own empirical analysis.

## 6. Validity evidence
n/a for formal validity. The paper builds its argument from: (a) historical-philosophical literature on colonialism and decoloniality (Quijano, Mignolo, Mohamed et al.); (b) Hindu philosophy (Dhand 2002, Ranganathan 2022, Tharoor 2018); (c) critical AI literature (Bender et al., Birhane); (d) existing alignment technology literature (Ouyang et al. RLHF, Bai et al. Constitutional AI). The author's positionality statement (Section 2.4) provides transparency about the situated perspective.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a — theoretical paper, though the proposed reference architecture includes an orchestrator for contextual adaptation at inference time.

## 9. Key numbers
- Six colonial mechanisms in AI identified (five prior + one new: moral absolutism) (p.6)
- Three desiderata for decolonial alignment + one additional (cost/accessibility) = four total (p.11–12)
- LoRA identified as the accessible technology (in the "sweet spot" for application developers) vs. full SFT, RLHF, data curation which are too expensive (p.12)
- Example: Jacaranda Health's UlizaLlama trained on 322M Kiswahili tokens for maternal health in East Africa (p.2)

## 10. Pitfalls & limitations
- Highly prescriptive use of Hinduism as a framework risks romanticizing or essentializing a complex tradition (author acknowledges "nostalgic Hinduism" criticism, p.8).
- The paper proposes a reference architecture but provides no implementation, evaluation, or case study.
- Hindutva (Hindu nationalism) has co-opted similar "decolonial" language for anti-Muslim purposes — author acknowledges this tension but does not fully resolve it (p.8).
- The argument that RLHF workers are forced to project monocultural values is important but relies on secondary sources (Perrigo 2023, Miceli & Posada 2022).
- The distinction between viśeṣa-dharma and relativism is philosophically important but not fully operationalized for technical implementation.
- Context window limitations of LLMs and the practical challenges of a contextual bandit orchestrator over a LoRA library are acknowledged but not addressed in depth.

## 11. Novel ideas worth stealing
- **Viśeṣa-dharma as a design principle for context-dependent benchmark items**: instead of universal moral scenarios, design benchmark items that are explicitly contextualized by role, relationship, community, and situation — and accept that "correct" answers vary by context.
- **LoraHub-style open library of value adapters**: a values-alignment benchmark could be paired with a library of community-specific fine-tuning matrices that allow the benchmark to be run in culturally-adapted modes.
- **Contextual bandit orchestrator for value selection**: selecting which values (LoRA matrices) to apply at inference time based on deployment context is a novel approach to personalized alignment — and an interesting benchmark design challenge.
- **Non-commandment epistemologies**: alignment values expressed through story, metaphor, image, dance, or silence rather than explicit rules. Benchmark designers should consider narrative or scenario-based elicitation methods beyond Likert scales and forced-choice pairs.
- **Reflective equilibrium for value uncertainty**: iterative deliberation to achieve coherent values in context is a method from political philosophy that could be operationalized as an iterative human-LLM dialogue evaluation protocol.
- **Sadharana vs. visesa harm taxonomy**: distinguishing universal (sadharana) harms from context-specific (visesa) harms is a two-level taxonomy directly applicable to benchmark construction — universal items for cross-cultural comparability plus community-specific items for local validity.
- **The Ekalavya problem for open access**: open access is still colonial if the computational cost is too high for Global South communities — a relevant constraint for benchmark design (accessible baselines, not only frontier-model evaluations).

## 12. Notable quotes
- "If a powerful model provider views their (Western) ethics or moral philosophy as universally correct, leaves no possibility for moral variety, and marginalizes all other ways of thinking about right and wrong, then their approach to AI alignment is colonial." (p.6)
- "Designing AI in accordance with a single moral doctrine would, therefore, involve imposing a set of values and judgments on other people who did not agree with them." (p.10, quoting Gabriel 2020)
- "Common harms that should be avoided according to sādharaṇa-dharma are captured in several recent harm taxonomies for LLMs, but context-specific harms are not included." (p.7)
- "Testing LLMs is difficult enough when only considering common, sādharaṇa sociotechnical harms such as hallucination, inciting violence, stereotyping, hate speech and toxicity. It becomes even more difficult when considering context-specific, viśeṣa harms that do not have existing benchmarks given their unique nature." (p.14)

## 13. UNKNOWN / not in extract
- Empirical validation of any component of the proposed architecture.
- Whether LoraHub or similar systems have been tested with community-authored value matrices.
- How the contextual bandit algorithm would be trained or evaluated.
- Specific examples of non-commandment value representation (beyond references to Divakaran et al. 2023).
