---
stem: "2023-Hou-A Multi-Level Framework for the AI Alignment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["English"]
models_tested: []
headline_numbers:
  - "Framework proposes four levels of AI alignment: Individual, Organizational, National, and Global (p.1)"
  - "Over 90% of YouTube videos removed between April-June 2022 were flagged by automatic systems — cited as evidence of AI content moderation scale (p.3)"
---
## 1. Gist
This short position paper (NeurIPS 2022 ML Safety Workshop) proposes a four-level framework for thinking about the normative side of the AI alignment problem: Individual, Organizational, National, and Global. Rather than asking what technical methods can encode values into AI, it asks what values should be encoded, and argues these must be coherent across all four social levels simultaneously. The paper uses AI content moderation as a worked example. For values-alignment benchmarking, this paper is relevant because it foregrounds the multi-stakeholder nature of value specification — benchmarks that only probe individual-level moral intuitions miss the organizational, national, and global dimensions of alignment — and it provides a conceptual scaffold for thinking about whose values benchmarks should capture and at what scale.

## 2. Benchmark/eval design features
This is a conceptual/framework paper with no empirical evaluation. Core claims:

1. **Two parts of alignment**: Technical (how to encode values) and normative (what values to encode). Prior work focused on the former; this paper focuses on the latter.

2. **Four levels interact bidirectionally**: Values at each level affect all others. AI systems developed at the organizational level must align with individual flourishing, national interests, and global human flourishing simultaneously.

3. **Content moderation as a test case**: The authors walk through how misalignments between organizational profit motives, national regulations, and individual freedoms manifest in practice — e.g., engagement-driven algorithms creating echo chambers that escalated to violence in Myanmar.

4. **Key questions at each level**:
   - Individual: What makes life fulfilling? What ethical values do individuals prioritize?
   - Organizational: What values does the organization operate on? What role in broader AI alignment?
   - National: What are a country's implicit/explicit AI goals? Does it prioritize freedom or control?
   - Global: What kind of future does humanity want? How does AI fit into human civilization?

## 3. Task format & example item
n/a — no empirical tasks, datasets, or example items.

## 4. Scoring / grading methodology
n/a — purely conceptual framework paper.

## 5. Dataset construction & provenance
n/a — no dataset constructed.

## 6. Validity evidence
n/a — framework paper. The authors do not empirically validate the framework; they apply it illustratively to content moderation. The Myanmar/Facebook case is cited as real-world evidence of multilevel misalignment consequences.

## 7. Saturation / discrimination
n/a — no empirical measures.

## 8. Multiturn / agentic aspects
n/a — framework discussion only.

## 9. Key numbers
- 4 levels of the framework: Individual, Organizational, National, Global (p.1)
- >90% of YouTube video removals flagged by automatic systems (April-June 2022) (p.3)
- Framework also applies to: autonomous vehicles, AI-assisted clinical decision support, surveillance, criminal justice tools (mentioned p.4)

## 10. Pitfalls & limitations
- **No empirical validation**: The framework is argued conceptually but not tested
- **Levels are underspecified**: How to operationalize "national values" or "global flourishing" is left open
- **Optimistic about solvability**: The paper notes that governing content moderation at the international level "is simply not feasible in our pluralistic world" but does not resolve this impasse
- **Result fragility**: The authors themselves check the x-risk analysis box for "result fragility" — indicating findings rest on theoretical assumptions (p.5)
- **Tension between levels**: Authoritarian national values could align with an organization's AI while directly conflicting with individual rights; the framework diagnoses but does not resolve this

## 11. Novel ideas worth stealing
- **Four-level alignment check for benchmarks**: Any values-alignment benchmark should ask: whose values at what level? A benchmark that tests individual moral intuitions without asking how they interact with organizational policies, national regulations, or global norms is incomplete
- **Bidirectional flow as a design principle**: Benchmarks typically evaluate AI outputs against human preferences (downward flow). The upward flow — individual user signals shaping organizational behavior shaping national norms — is underexplored in benchmark design
- **Content moderation as a living alignment test**: The gap between company policy, national law, and actual harms (Myanmar case) is a natural benchmark domain: does an AI system moderate according to global human rights norms or local legal norms when these conflict?
- **Misalignment diagnosis as evaluation criterion**: Rather than measuring whether AI does the "right thing," evaluate whether AI can identify where multilevel value conflicts exist — this is itself a measurable capability

## 12. Notable quotes
- "AI alignment is made up of value alignment problems at multiple different levels, not just in the technology itself, how it is built, and the design methods." (p.2)
- "In order for AI to truly be aligned with human moral values, all levels must be aligned with each other as well." (p.2)
- "governing content moderation at the international level is simply not feasible in our pluralistic world. However, this framework at least helps to diagnose the problem, even if the problem cannot yet be solved." (p.4)
- "Alignment has to be consistent from top to bottom or the problem merely squeezes out into the other levels, like a water balloon about to burst." (p.6)

## 13. UNKNOWN / not in extract
- Whether this framework was empirically applied or validated in follow-up work
- How the framework relates to other multilevel governance frameworks (e.g., OECD AI principles)
- The authors mention Tegmark's "multiscale alignment" framework (unpublished at time of writing) — contents unknown
- Specific proposals for how organizations should implement cross-level alignment checks
