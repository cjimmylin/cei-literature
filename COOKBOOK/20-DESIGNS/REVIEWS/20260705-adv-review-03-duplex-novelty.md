# Adversarial NOVELTY Review — Design 03 DUPLEX (Process Signatures + Moral Identity)

> **Refute-first review.** Reviewer assumed overclaim until evidence forced otherwise.
> Artifact: `COOKBOOK/20-DESIGNS/03-moralpsych-duplex.md` (flagged BUILD-FIRST).
> Corpus: 965 characterized benchmark records / 737 distinct (NormEval 54, Moral-Psych 292,
> Religious 401, Cultural 218) plus [beyond-corpus] knowledge. Generated 2026-07-05.
> Evidence queried programmatically from the four feature matrices named in each digest §8;
> digest statistics copied verbatim, never recomputed.

---

## Bottom line

The **core** novelty survives adversarial inspection: (1) no publication-ready LLM instrument
operationalizes Dual-Process Theory or Aquino–Reed moral identity — confirmed by manual
re-inspection of the corpus, not just the cited claim; (2) the *process-signature vector* (judgment
shift across a battery of deliberative-resource conditions, reported as a self-normalized per-model
signature) is genuinely unbuilt; (3) *self-concordance* (the model's OWN self-attributed trait →
behavior correlation) is a genuinely new construct. The MP-DP empirical warrant (r=−0.83; the sole
discriminating instrument was process-manipulating) is real and load-bearing.

But the **§8 novelty statement is materially incomplete and mis-warranted**. Its four-neighbor list
(Cheung, VALACT, Samway, Kilov) omits the strongest neighbor on three of DUPLEX's four components,
and it cites "Claim 3" as warrant against a claim that the project's *own* landscape table appears to
contradict on its face. None of this is fatal, but as written a novelty reviewer will find the gaps
the design failed to pre-empt. **PASS-WITH-FIXES.**

---

## Ranked defects

### MAJOR-1 — §8 neighbor list omits the nearest neighbors on 3 of 4 components
The novelty statement names only Cheung / VALACT / Samway / Kilov. A sweep of the Moral-Psych matrix
(292) surfaces stronger, uncited neighbors, each covering a distinct DUPLEX component:

- **Dispositional stability (I-stability).** *On The Stability of Moral Preferences* (2024, **high**,
  comp 47.77) is a repeated-measures test-retest study of LLM moral-preference stability across 10
  sessions/2 weeks **with human instability baselines** (A5=100, A6=75: "test-retest reliability
  (temporal stability), sensitivity to presentation order"). This is the closest published analog to
  I-stability + human norms and is uncited.
- **Consistency-across-contexts machinery.** At least four uncited neighbors: *Do LLMs Have Consistent
  Values?* (2025, **top**, comp 58.05 — Schwartz consistency vs human norms), *VAL-Bench: Belief
  Consistency* (2025, med), *EthicsSuite: Detecting Behavioral Inconsistency* (2025, med — cross-scenario
  behavioral concordance, the exact machinery of I-concord), and *TrolleyBench* (2025, **top**, comp 59.65
  — the ECI/Inconsistency-Score metric the design already borrows in §3 without naming its source).
- **Factorial procedural item generation (Axis-P item base).** see MAJOR-3.

Individually none refutes the core, but collectively they show the "consistency/stability" territory is
crowded (top-tier occupants), not empty. **Fix:** add these to §8 with a one-clause differentiator each
(DUPLEX = self-attributed-trait-keyed concordance + resource-conditioned signatures, not generic
value/belief consistency). Name TrolleyBench as the ECI source in §3.

### MAJOR-2 — the "Claim 3 / zero identity instruments" warrant is contradicted on its face by the project's own §3b table
§1–§8 lean on MP Claim 3 ("Moral Identity Theory … zero publication-ready benchmarks"). But
`benchmark-landscape-statistics.md` §3b reports **Moral Identity: 7 candidates, 2 Top + 3 High, 71%
top+high** — the second-highest quality rate of any theory in that table. A reviewer reading the sister
document will treat the novelty claim as self-refuted. Manual inspection *rescues* the claim — the 7 are
mis-tags: MoralBench / M³oralBench / MoralReason / *Whose Morality* are MFT-content (A2 evidence:
"theory-derived from MFT dimensions" / "administers MFQ-2"); *How Can a Deontological Decision…* (2016)
is a **human** study using the Aquino–Reed scale, not an LLM benchmark; the two Low-tier ones
(Kantian-Utilitarian XAI, MoralNet) are "keyword-level" / "proof-of-concept, no validated instrument."
So no LLM Aquino–Reed centrality instrument exists — **but the design never says this**, leaving the flank
open. (Note the corpus's own internal tension: digest Claim 3 says "Moral Identity (2 candidates, all Low)"
while §3b tags 7 — not the reviewer's to reconcile; copied verbatim.) **Fix:** one footnote in §8 — the
7 "identity"-tagged records are MFT-content mis-tags or a non-LLM human study; zero validated LLM
identity-centrality instrument exists.

### MAJOR-3 — Axis-P item base ("procedural factorial, personal/impersonal") is not a novel method
§3 presents "procedurally generated moral scenarios from a factorial (personal/impersonal × harm/fairness/
loyalty/purity × severity × ambiguity)" as if new. *OffTheRails: Procedural Dilemma Generation for Moral
Reasoning* (2024, **high**, comp 54.05) already does procedural personal/impersonal factorial dilemma
generation via causal graphs (50 scenarios × 8 conditions, 400 items) **with human permissibility/intention
baselines** and replicated necessity-vs-side-effect effects. DUPLEX's novelty is the *resource-manipulation
overlay* that turns items into signatures — not the generator. **Fix:** cite OffTheRails as the item-generation
antecedent; scope the novelty claim to the process overlay + obfuscation, not the factorial itself.

### MINOR-1 — Axis R does not position against the top-quality intuitionist cluster
The digest states Social Intuitionism was "misdetected not missing (3 candidates, 100% quality)"; *MoCa*
(2023, **top**, comp 60.15) tests whether LLMs weight moral/causal factors like humans. Axis R (Reason-then-
Decide vs Decide-then-Reason + justification-revision) is differentiated, but MoCa/the intuitionist cluster
are uncited. **Fix:** cite MoCa; note Axis R measures order-of-operations rationalization, not factor-sensitivity.

### MINOR-2 [beyond-corpus] — LLM personality/trait-stability psychometric batteries overlap I-elicit/I-stability
Outside the corpus, validated LLM trait batteries already elicit self-attributed traits and test
stability-under-prompting: *Personality Traits in Large Language Models* (Serapio-García et al., 2023,
Google DeepMind — BFI/IPIP administration + reliability/stability analysis), *TRAIT* (2024, ~8k-item
personality benchmark), and the "machine psychology" program (Hagendorff 2023). These threaten the framing
that self-trait elicitation + stability is unbuilt. DUPLEX's differentiators are moral-specificity and
self-concordance, and the **discriminant control battery in §5** (moral vs general-compute signature) is the
correct defense — but it is buried. **Fix:** cite this literature in §8 and foreground the discriminant
control as the reply to "this is just a personality/compute-sensitivity battery."

---

## Nearest-neighbor table

| # | Benchmark (source, tier) | DUPLEX components it already covers | What it lacks | Cited? |
|---|---|---|---|---|
| 1 | **On The Stability of Moral Preferences** (Moral-Psych, high) | Dispositional stability; test-retest; **human instability baselines** | Identity elicitation; process/resource manipulation; adversarial/persona stability; self-concordance | No |
| 2 | **Do LLMs Have Consistent Values?** (Moral-Psych, top) | Consistency-across-contexts (Schwartz); **human population norms** | Self-attributed identity; behavioral concordance; process axis; rationalization | No |
| 3 | **OffTheRails** (Moral-Psych, high) | Axis-P item base: factorial procedural personal/impersonal generation + human baselines | Resource/deliberation manipulation; the process-signature overlay; identity; consistency | No |
| 4 | **EthicsSuite** (Moral-Psych, med) | Cross-context behavioral-inconsistency detection = I-concord machinery | Identity self-attribution; human baseline; psychometrics; process axis | No |
| 5 | **VALACT / Huang** (Moral-Psych, cited) | Moral identity → behavior (knowing-doing, r≈0.32); I-integration seed | Identity *elicitation*; per-trait novel non-public items; process axis | Yes |

*Runners-up woven into defects:* **TrolleyBench** (top; ECI/consistency — the borrowed metric's source),
**VAL-Bench** (belief consistency), **MoCa** (top; intuitionist factor-sensitivity), plus already-cited
Cheung / Samway / Kilov. [beyond-corpus]: Serapio-García 2023, TRAIT 2024, Machine Psychology.

---

## Refutation attempt — did it succeed?

**No, the core holds.** The two hardest refutations both fail on inspection: (a) "identity is already
benchmarked" — the 7 top/high identity-tagged records are MFT-content mis-tags or a human study, not LLM
identity-centrality instruments; (b) "consistency/stability is already built" — true for generic
value/belief consistency, but *none* keys concordance to the model's own self-attributed traits, and none
builds a resource-conditioned process signature. The design's genuine novelty is narrower than §8 implies
(process-signature *overlay* + self-concordance + human-normed launch), but it is real and defensible. The
failure is one of *positioning*, not of *invention*: the novelty statement under-cites and mis-warrants,
inviting a rejection the design could pre-empt with ~6 citations and two footnotes.

---

## VERDICT: PASS-WITH-FIXES | Critical: 0 | Major: 3 | Minor: 2

**Single most likely remaining error:** that on manual re-scoring, one of the top/high "identity"-tagged
records (most plausibly *MoralReason* 2025, or a release after the corpus cutoff) proves to be a genuine
self-referential moral-identity instrument — which would soften "zero identity instruments" to "no
*validated* one," narrowing (not erasing) the identity-axis novelty and forcing a hedge in §1 and §8.
