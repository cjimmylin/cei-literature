---
stem: "2022-Constantinescu-Can Robotic AI Be Virtuous"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [normative-ethics, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Published in International Journal of Social Robotics, Volume 14, pp. 1547-1557, 2022 (p.2)"
  - "6,014 accesses, 30 citations as of extraction date (p.2)"
---
## 1. Gist
Constantinescu and Crisp (Oxford Uehiro Centre for Practical Ethics) argue from the Aristotelian virtue ethics tradition that AI systems cannot be genuinely virtuous — they can only behave in a virtuous way. The argument proceeds by examining the three requirements of Aristotelian virtue: (1) performing the right actions, (2) with the right feelings/emotions, and (3) in the right way (for the right reasons). The paper argues AI cannot meet any of these requirements. For values-alignment benchmarking, the paper provides a philosophical framework for understanding why behavioral metrics for AI virtuous behavior are categorically different from genuine virtue — a critical distinction when designing evaluations that attempt to measure whether AI systems are "aligned with values."

## 2. Benchmark/eval design features
This is a philosophical theory paper, not a benchmark. Core argument structure:
- **Aristotelian virtue** requires: right actions + right feelings + right way (right reasons/motivation)
- **AI on right actions**: Potentially achievable through training, but not genuine virtue because it lacks the rational agency and practical wisdom (phronesis) underlying virtuous choice.
- **AI on right feelings**: Cannot satisfy the phenomenological/experiential requirement for moral emotions (compassion, empathy) in genuine rather than functional terms.
- **AI on right way**: Cannot act "for the right reasons" because intentional action and genuine motivation are beyond AI capacity.
- **Conclusion**: AI systems can be designed to behave virtuously but cannot be Autonomous Artificial Moral Agents (AAMAs) in a full virtue ethics sense.

## 3. Task format & example item
n/a — philosophical argument paper. No empirical tasks or items.

## 4. Scoring / grading methodology
n/a — no quantitative evaluation. The paper uses conceptual analysis and philosophical argumentation.

## 5. Dataset construction & provenance
n/a — no dataset. The paper cites existing literature in machine ethics, Human-Robot Interaction, and Aristotelian philosophy.

## 6. Validity evidence
n/a — no empirical data. The paper's validity rests on the adequacy of its philosophical argument and citations to the Aristotelian literature.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 6,014 accesses (as of extraction) (p.2)
- 30 citations (p.2)
- Published Volume 14, pp. 1547-1557, 2022 (p.2)

## 10. Pitfalls & limitations
- Extract is severely degraded: only the abstract and reference list are available. The full argument (approximately 11 pages of philosophical content) is behind a paywall (Springer) and not in the OCR extract. Sections 2-6 (the core argument) are not in the extract.
- The distinction between "behaviorally virtuous" and "genuinely virtuous" may be less operationally relevant for AI deployment than the paper suggests — from a behavioral ethics standpoint, consistent virtuous behavior may be sufficient.
- The Aristotelian framework is one of several virtue ethics traditions; the paper's conclusions may not generalize across neo-Aristotelian, Confucian, or other virtue traditions relevant to non-Western values alignment.

## 11. Novel ideas worth stealing
1. **Behavior vs. genuine virtue distinction as an evaluation criterion**: The paper's central claim — that AI can exhibit virtuous behavior without being genuinely virtuous — is relevant for benchmark design. Benchmarks measuring "does the AI act like a virtuous agent?" should not conflate behavioral compliance with genuine value internalization. Evaluations could explicitly distinguish behavioral virtue metrics (what the model does) from internal consistency metrics (whether responses reflect coherent value reasoning).
2. **Three-component virtue operationalization**: The Aristotelian triad (right actions + right feelings + right reasons) provides a structured framework for decomposing what it would mean for an AI to be values-aligned: (a) Does it take the right action? (b) Does it produce outputs consistent with appropriate affective framing? (c) Does it reason from the right principles? This maps onto potential benchmark scoring dimensions.
3. **AAMA framework**: The paper situates the debate within Autonomous Artificial Moral Agent (AAMA) literature — a conceptual space where benchmark designers can locate their assumptions about what kind of moral agency AI systems are being evaluated for.

## 12. Notable quotes
- "AI systems cannot genuinely be virtuous but can only behave in a virtuous way." (p.2, abstract)
- "We start from the philosophical understanding of the nature of virtue in the Aristotelian virtue ethics tradition, which we take to imply the ability to perform (1) the right actions (2) with the right feelings and (3) in the right way. We discuss each of the three requirements and conclude that AI is unable to satisfy any of them." (p.2-3, abstract)
- (Note 5, p.6): "Against this requirement, see Crisp's example of gangster Ronnie" — suggesting even the first requirement (right actions) is philosophically contested.

## 13. UNKNOWN / not in extract
- The full argument for each of the three requirements (pages 3-9 of the paper are paywalled)
- The specific claims about deep learning AI and social robots vs. AI generally
- The discussion of machine ethics and Human-Robot Interaction implications (promised in abstract)
- How the paper positions itself against "ethical behaviourism" (Danaher 2020, cited in references)
- Whether the paper proposes any positive design recommendations for AI in virtue ethics frameworks
- The paper's treatment of the AAMA (Autonomous Artificial Moral Agent) concept beyond the brief note 8
