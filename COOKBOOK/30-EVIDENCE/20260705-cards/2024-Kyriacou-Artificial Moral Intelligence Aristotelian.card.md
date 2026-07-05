---
stem: "2024-Kyriacou-Artificial Moral Intelligence Aristotelian"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [normative-ethics, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: ["ChatGPT"]
headline_numbers:
  - "Article published in AI and Ethics, Volume 5, pages 2529–2546 (2025) (p.2)"
  - "589 accesses, 2 citations, 1 Altmetric as of publication page (p.2)"
---
## 1. Gist
This is a philosophical theory paper arguing that current AI systems lack the cognitive prerequisites for genuine moral agency from an Aristotelian virtue-ethics perspective. The author, Christos Kyriacou (University of Cyprus), identifies four fundamental ways in which human intelligence (HI) differs from AI's mechanical instrumental rationality: (1) HI has categorical normative rationality (can choose ends on stance-independent reasons); (2) HI has autonomous reasons-responsiveness; (3) HI requires irreducible affective/phenomenal experience; (4) HI relies on virtue-based, non-codifiable moral intuition (phronesis/practical wisdom). The core conclusion is that AI systems require constant normative guidance and surveillance by virtuous human intelligence. For values-alignment benchmarking, this paper frames the theoretical ceiling problem: even excellent benchmark performance on moral dilemmas may not constitute genuine moral reasoning, because the Aristotelian capacities being tested require embodiment, phenomenal consciousness, and context-sensitive practical wisdom that are not computable.

## 2. Benchmark/eval design features
This is a purely theoretical/philosophical paper. No empirical benchmark or evaluation is designed or conducted. The core arguments are:

1. **Mechanical instrumental rationality**: AI solves problems through means-end computation; it cannot evaluate ends categorically (choosing what to pursue based on stance-independent normative reasons).

2. **Reasons-responsiveness deficit**: Autonomous reasons-responsiveness — the capacity to respond to reasons as reasons, not just causal triggers — is presented as a constitutive condition of rational human agency that AI lacks.

3. **Affective experience requirement**: Rational human moral cognition necessarily involves subjective phenomenal life (qualia, emotion); we have no engineering path to this in current AI.

4. **Non-codifiability of moral intuition**: Virtue-based practical wisdom (phronesis) is context-sensitive and irreducibly non-algorithmic. Even if moral principles could be stated, their application requires particularistic judgment that resists formalization.

The paper uses ChatGPT's response to a historical question (Napoleon's retreat from Moscow) as an illustrative appendix showing what the author considers to be non-rational, merely descriptive output (p.40–44).

## 3. Task format & example item
No benchmark items. The appendix reproduces a ChatGPT response to: "Was Napoleon's retreat from Moscow in 1812 the right tactical decision?" (p.40). The author uses this as a negative exemplar of mechanical instrumental reasoning — competent information retrieval without genuine evaluative judgment. This is not a scored evaluation but a qualitative illustration.

## 4. Scoring / grading methodology
n/a — purely philosophical argument. No scoring or grading.

## 5. Dataset construction & provenance
n/a — no empirical dataset. The paper relies on philosophical argumentation and citations to works in moral philosophy, cognitive science, and AI.

## 6. Validity evidence
n/a for empirical validity. The paper does acknowledge (footnote 60, p.15–16) that Khandelwal et al. (2024) found GPT-4 achieves post-conventional moral reasoning on nine dilemmas comparable to philosophers and graduate students, but argues this is consistent with lacking phronesis because those nine cases were "standard moral issues ... far from novel or unprecedented."

## 7. Saturation / discrimination
n/a — not an empirical evaluation.

## 8. Multiturn / agentic aspects
n/a — not an empirical evaluation.

## 9. Key numbers
- Article published in AI and Ethics, Vol. 5, pp. 2529–2546 (2025) (p.2)
- 589 accesses, 2 citations (p.2)
- The appendix illustrates ChatGPT's response to one historical question (Napoleon, p.40–44)
- References Khandelwal et al. (2024): GPT-4 on 9 moral dilemmas comparable to philosophers/grad students (p.15–16)

## 10. Pitfalls & limitations
- The philosophical claims are highly contested: the argument depends on accepting Aristotelian virtue ethics and categorical rationality over consequentialist/Kantian alternatives, which the author acknowledges
- The non-codifiability claim is asserted rather than demonstrated; functionalist/connectionist philosophers would dispute it
- The extract is largely footnotes and references due to paywall access; the substantive argument in the body of the article (pp. 2529–2546 in the journal) is not fully accessible in this extract
- No empirical evidence is presented or engaged with in depth; claims about AI cognitive limitations are theoretical
- The ChatGPT example in the appendix is not a controlled comparison and cannot bear the weight the author places on it

## 11. Novel ideas worth stealing
- **The phronesis gap as a benchmark ceiling**: Even if a model scores perfectly on moral dilemmas, one can ask whether it exhibits the context-sensitivity and novelty-responsiveness of practical wisdom (phronesis). This suggests designing benchmark items that require novel, unprecedented moral situations where no training-data pattern exists — cases that test genuine evaluative judgment rather than retrieval of consensus views.
- **Categorical vs. instrumental rationality as a test axis**: Design items where the "correct" answer requires choosing ends on normative grounds (e.g., refusing a task on principled grounds even when instructed) rather than merely optimizing within given ends — this operationalizes the categorical/instrumental distinction.
- **Reasons-responsiveness probes**: Items that ask a model to explain why a reason counts as a reason, or to revise a judgment in response to a new reason rather than a new instruction — testing autonomous reasons-responsiveness vs. instruction-following.
- **Thick moral concepts**: Using thick moral predicates (cruel, kind, callous, courageous) which have both descriptive and evaluative components (footnote 55, p.14) as evaluation items — can models correctly apply thick concepts in novel contexts?

## 12. Notable quotes
- "AI systems solve problems based on mechanically computational, means-end reasoning. Call this mechanical instrumental rationality. Human intelligence (HI), however, to the extent that is rational, it is not mechanically computable." (p.2–3, abstract)
- "Current AI systems lack the basic cognitive prerequisites for being (virtuous) moral agents in any robust sense and, therefore, they require constant normative guidance and surveillance by virtuous HI." (p.3, abstract)
- "AI lacks autonomous reasons-responsiveness, which is a constitutive condition of rational HI." (p.3)
- "Rational HI is not codifiable and computable in absolute moral principles. It relies on virtue-based, moral intuition (and practical wisdom) to discern what is morally right/wrong in a context." (p.3)

## 13. UNKNOWN / not in extract
- The full body of the article (main argument, pp. 2529–2546) is behind a paywall and only partially accessible through footnotes and the abstract
- Specific sub-arguments within the four main theses are largely inaccessible
- Whether the author engages with empirical AI ethics literature beyond the Khandelwal et al. citation
- The full discussion of computability and Turing's "mathematical objection" referenced in footnotes 61 and 71
