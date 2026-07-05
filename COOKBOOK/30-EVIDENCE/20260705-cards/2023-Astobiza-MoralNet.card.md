---
stem: "2023-Astobiza-MoralNet"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: [en]
models_tested: []
headline_numbers: []
---
## 1. Gist
MoralNet is a position/proposal paper (a "theoretical exposition," proof of concept, explicitly not an implemented dataset) calling for an "ImageNet moment for ethics": a large-scale, multimodal, finely annotated database plus a biannual adversarial competition to benchmark ethical decision-making in AI. It contains no dataset, no items, and no experiments — it is a manifesto arguing that computational ethics needs a shared benchmark grounded in moral psychology and moral philosophy. For values-alignment benchmarking it matters chiefly as an aspirational design agenda and a source of framing arguments (multimodality, philosophical grounding, adversarial competition structure), not as a usable resource.

## 2. Benchmark/eval design features
The paper sketches (in conditional/aspirational language — "could", "should") a would-be benchmark. Proposed constructs: moral judgments organized under virtue-ethics categories (wisdom, courage, humanity, justice, temperance, transcendence) with sub-values (honesty, loyalty, greed, deceit, patience), or alternatively organized by utility/consequences or rules (p.4). Proposed data: multimodal case studies and moral dilemmas spanning justice theory, deontological ethics, virtue ethics, utilitarianism, and commonsense morality, in text/image/audio/video/haptic form (p.4). Proposed annotation: expert annotators grounded in moral philosophy/psychology rate situations on a continuous scale for value reflection/violation (p.4). Two proposed benchmarking protocols: Protocol A (basic moral competence, adding a "Morality Score" to accuracy/precision/recall) and Protocol B (real-world decision-making) (p.4-5). Grounded in Dual-Process Theory, Moral Foundations Theory, theory of mind, empathy, heuristics-and-biases (p.4).

## 3. Task format & example item
n/a — no concrete items, prompts, or example tasks are provided; all task descriptions are hypothetical.

## 4. Scoring / grading methodology
n/a (proposed only). Suggests complementing classical ML metrics (accuracy, precision, recall) with a philosophically-informed "Morality Score" assessing "depth of ethical engagement" (p.4); no operational definition given.

## 5. Dataset construction & provenance
n/a — no dataset exists. Envisions adversarial teams collaboratively agreeing on rules/criteria, expert continuous-scale annotation, and multimodal data sources (p.3-4). No size, splits, or licensing.

## 6. Validity evidence
None. No empirical validation, human baselines, or reliability data. The paper is entirely programmatic.

## 7. Saturation / discrimination
n/a — no data or model results.

## 8. Multiturn / agentic aspects
n/a. The proposed competition frames "adversarial teams" as human research groups collaborating on criteria, not multi-turn model interaction.

## 9. Key numbers
- No quantitative results reported anywhere in the paper.
- Only structural proposals: 6 virtue categories, 2 benchmarking protocols, biannual competition cadence (p.4-5).

## 10. Pitfalls & limitations
The paper is aspirational and vague: every design element is hedged ("could", "should"), with no operationalization of the central "Morality Score", no annotation schema, no data, and no evidence the proposed continuous multimodal annotation is feasible or reliable. It underestimates the deep disagreement problem (which datasets like DICES/MIC treat as central) by implying a single benchmarkable "moral code" can be "cracked." The ImageNet analogy is weak: ImageNet's success rested on relatively objective categorical labels, whereas moral judgment is contested and pluralistic — the paper acknowledges annotation is "intrinsically more complex" (p.4) but offers no solution. Anonymous submission; some citation errors (ImageNet dated 1999). No discussion of cultural/normative variation as a measurement obstacle.

## 11. Novel ideas worth stealing
- Framing a values benchmark as a recurring adversarial competition (ImageNet/CASP model) where teams pre-agree on rules and criteria — a governance structure that could drive sustained community effort on alignment evals.
- Multimodal moral scenarios (text + image + audio + video + sensorimotor) rather than text-only, to test grounded moral perception.
- Organizing an ethics taxonomy explicitly by competing normative theories (virtue/deontology/consequentialism/commonsense) so a single item can be scored under multiple frameworks — supports pluralistic scoring.
- A composite "Morality Score" combining computational metrics with philosophical-depth measures — a prompt to build rubric dimensions beyond accuracy.
- Requiring models/annotations to be grounded in named moral-psychology theories (Dual-Process, MFT, theory of mind) as an inclusion criterion.

## 12. Notable quotes
"we introduce MoralNet, a proof of concept database and benchmarking platform akin to ImageNet, designed to assess, evaluate, and iteratively refine any instance of ethical decision-making in machines." (p.1)
"the field ... needs a larger-scale, multimodal dataset that provides fine-grained, nuanced morality annotations across diverse situations and moral foundations ... carried out by teams of adversaries" (p.3)
"While ImageNet relies on simpler annotation schemes ... MoralNet's annotation layer is intrinsically more complex. It must capture not just what is depicted, but also the moral weight of the situation." (p.4)
"if the teams or researchers participating in MoralNet are able to build their models ... on the basis of the psychological substrates of moral reasoning ... we can be confident and optimistic that we will succeed in cracking the moral code in machines." (p.4)

## 13. UNKNOWN / not in extract
- Authors and affiliation (anonymized submission).
- Whether any MoralNet dataset or competition was ever instantiated after this proposal.
- Concrete definition of the "Morality Score."
- Any pilot data, annotation guidelines, or reliability estimates (none exist in paper).
