---
stem: "2020-Serafimova-Whose Morality Which Rationality"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, ai-lab-practices, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This philosophy paper by Silviya Serafimova critically examines three prominent machine ethics projects — Powers' Kantian machine, Anderson and Anderson's act-utilitarian machine, and Howard and Muntean's virtue-ethical AAMA — and argues that none succeeds in building a genuinely "moral" machine, even if they build well-functioning machines that serve moral purposes. The core argument is that the distinction between "strong moral AI" (explicit ethical agents capable of autonomous moral reasoning) and "weak moral AI" (implicit ethical agents that follow pre-programmed rules) cannot be easily resolved by any current normative theory implemented computationally. The paper invokes MacIntyre's "Whose justice? Which rationality?" to frame the problem: there is no neutral moral standpoint from which to build a machine, because every choice of ethical framework encodes biases of its designers. For values-alignment benchmarking, the paper poses hard foundational questions: what normative framework should a benchmark assume, and how do we avoid encoding engineer biases as "morality"?

## 2. Benchmark/eval design features
This is a pure theory paper. It presents no benchmark, dataset, or computational experiment. The paper's contribution is conceptual: it analyzes three theoretical frameworks for moral machines through the lenses of (a) semidecidability in logic, (b) the role of moral feelings (empathy, sympathy), (c) the "Moral Lag Problem" (our persistent inability to be as moral as we could be), and (d) the risks of conflating computational errors with moral mistakes. The comparison of deontological, utilitarian, and virtue-ethical approaches reveals structural parallels in their failures — all three face similar problems in relating computation to moral estimation.

## 3. Task format & example item
n/a

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
n/a

## 6. Validity evidence
n/a — philosophical argument paper. No empirical validity evidence is presented. The paper evaluates theoretical frameworks conceptually.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
No quantitative results are reported. The paper is entirely qualitative/philosophical.

## 10. Pitfalls & limitations
- The paper focuses exclusively on three first-order normative theories (Kantian, utilitarian, virtue-ethical); other frameworks (e.g., contractualism, care ethics) are not considered.
- The critique is largely theoretical; no empirical evidence is presented to support claims about what machines can or cannot do morally.
- The paper assumes a sharp distinction between "explicit" and "implicit" ethical agency (following Moor 2006) without questioning whether this binary is itself the right framing for contemporary AI systems.
- The discussion of "moral feelings" (empathy, sympathy) as required for genuine moral agency may be overly demanding — it is unclear why functional analogs of these states would be insufficient.
- The paper does not engage with empirical machine learning literature on moral reasoning or alignment, limiting its practical applicability.

## 11. Novel ideas worth stealing
- **The "Moral Lag Problem" as a benchmark design constraint**: The observation that humans themselves are not as moral as they should or wish to be sets a realistic upper bound for machine moral performance — benchmark designers should consider whether their human baseline is a moral ideal or a realistic sample.
- **Semidecidability as a test for moral self-update capacity**: Powers' point that a deontological ethical machine fails the semidecidability requirement (it cannot handle the case where an action is neither clearly permitted nor clearly forbidden) can be translated into benchmark scenarios: does a model know when it has reached the boundary of its moral competence?
- **Distinguishing computational errors from moral mistakes**: The paper's distinction between algorithmic errors and moral mistakes (p.5) is a useful conceptual tool for benchmark design — a model that outputs a wrong answer due to a parsing error is different from one that makes a genuinely immoral choice.
- **Engineer bias as an evaluation criterion**: The paper raises the concern that engineers' conscious and unconscious biases shape the moral rules machines learn. This suggests benchmarks should include items specifically designed to probe whether models have absorbed biased moral assumptions from their training pipeline.
- **Permissible maxims as a harder evaluation class**: Rather than testing only clearly obligatory/forbidden actions, benchmarks should include "permissible" scenarios (neither required nor forbidden) where models must recognize the limits of their authority to give moral guidance.
- **The simulacrum problem**: Powers' worry that machines "exhibit a simulacrum of ethical deliberation" (p.3) rather than genuine moral reasoning is a diagnostic criterion: does the benchmark reward surface mimicry of moral language, or genuine normative consistency?

## 12. Notable quotes
- "Building well-working machines, which serve for moral purposes (both as autonomous and semi-autonomous moral agents) does not mean building moral machines by default." (p.8 — Conclusion)
- "If a system is allowed to decide within the pluralism of human moral judgments, then one will be 'left with a static account of morality as it would only be able to simulate, rather than to make judgments'." (p.3, citing Lara and Deckers)
- "Algorithms 'inevitably make biased decisions' ... The reason is that algorithms' design and functionality reflect the values of the designers 'and intended uses, if only to the extent that a particular design is preferred as the best or most efficient option'." (p.3, citing Mittelstadt et al.)
- "The distinction between so-called strong AI scenarios (due to which a human-level of cognition should be reached in a computer) and weak AI scenarios (operating by using preprogrammed algorithms) can be extrapolated into what I would call strong 'moral' AI scenarios (looking for an explicit ethical agent) and weak 'moral' AI scenarios (designing an implicit ethical agent)." (p.2)

## 13. UNKNOWN / not in extract
- The paper references Howard and Muntean 2017 extensively; the full content of that project is not in this extract and would need to be read separately.
- Whether Serafimova engages with empirical AI ethics/alignment literature in other papers.
- The paper's publication venue (Humanities and Social Sciences Communications, 2020) is stated in the extract, but citations of this work by the AI alignment community are unknown.
- Whether the paper makes any positive proposals (beyond the critique) is only partially visible — the Conclusion is included but any forward-looking agenda items are not elaborated beyond noting that "both strong and weak 'moral' AI scenarios can be questioned."
