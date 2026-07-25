**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

> **PART FILE — assembles into paper (b).** §1, §6 and §7 are drafted in
> `pb-01-intro-limitations-future.md`; §3–§5 are drafted separately.
> Target paper: *Judging the Judges for $0: A Two-Referee Concordance Method for Localizing
> LLM-as-Judge Failure on Value-Laden Rubrics.* Venue-generic and author-generic by ruling.
>
> Every citation below is traceable to a vault file listed in the citation ledger at the end
> of this part. Claims for which no vault source could be located are marked inline with
> `[CITATION NEEDED — …]` rather than attributed to a work from memory.

---

## 2 Related work

Four bodies of work bear on the method reported here: the characterisation of LLM-as-judge
scoring and its biases; the use of agreement statistics as evidence of measurement quality;
the measurement-theoretic critique of benchmarks and leaderboards; and meta-evaluation, in
which models are used to audit other models. We take each in turn and state, at the close of
each thread, what this paper adds that the thread does not already contain.

### 2.1 LLM-as-judge and its known failure modes

Model-graded scoring entered the field as a scalability argument. Zheng et al. (2023)
introduced MT-Bench and Chatbot Arena and, in the same paper, both named the practice and
audited it: they document position, verbosity and self-enhancement biases together with
limited reasoning ability, propose mitigations, and report that strong judges such as GPT-4
match controlled and crowdsourced human preferences at over 80% agreement — "the same level of
agreement between humans" — from which they conclude that LLM-as-judge is a scalable and
explainable way to approximate preferences that are otherwise expensive to obtain. The
argument was persuasive and the practice generalised quickly; Gu et al. (2024) survey the
resulting literature, formalise the setting, and organise it around the question of how to
build *reliable* judge systems, which they treat as the field's open problem rather than a
solved one.

The bias catalogue has since been filled in with some precision. Shi et al. (2025) study
position bias systematically across 15 judges on MTBench and DevBench — 22 tasks, roughly 40
solution-generating models, over 150,000 judging instances — and separate judge-level,
candidate-level and task-level contributors. Two of their findings matter for what we do
here: position bias is not attributable to chance and it *varies across judges and tasks*, and
it is strongly affected by the quality gap between the compared solutions. Wataoka et al.
(2024) give a mechanism for self-preference: judges assign higher scores to lower-perplexity
text than human raters do, whether or not that text is self-generated, which reframes
self-preference as a familiarity effect rather than a vanity effect. Koo et al. (2023), in the
CoBBLEr benchmark, assemble 15 models across four size ranges, have them rank one another, and
measure six cognitive biases; they find bias indications in an average of 40% of comparisons
and a rank-biased overlap between machine and human preference orderings of 49.6%, concluding
that judges of this generation could not be used for annotation aligned with human preference.
Beyond English, Son et al. (2024a) build KUDGE, the first non-English meta-evaluation set,
with 5,012 Korean human annotations, and find judges struggling on factual inaccuracy,
cultural misrepresentation and unwanted language; Son et al. (2024b) extend this to MM-Eval
across 18 languages, where 12 evaluator models average 68.9% accuracy against a 50% random
baseline and safety judging in low-resource languages degrades by 18.4 points relative to
English. Faisal et al. (2024) report the same pattern of judge inconsistency across dialects
and language varieties. Beyer et al. (2025) locate judge unreliability inside a larger
pipeline argument, showing that safety evaluations accumulate noise at every stage — dataset
curation, red-teaming optimisation, generation, and judge-based response scoring — to the
point that attacks and defences cannot be fairly compared.

What this thread establishes is that judges are biased *in aggregate*, usually demonstrated on
general-purpose response-quality ratings, and that the biases are properties of judges, tasks
and candidate pairs. What it does not do is quantify the judge's effect on the *comparative
conclusion itself*. A benchmark author reading this literature learns that their judge is
imperfect; they do not learn whether the ordering they are about to publish would survive a
different judge, nor by how much. We supply that missing quantity directly. By rescoring every
administration offline with a second judge from a different model family, so that the judge is
the only variable, and by running three independent epochs so that the epochs serve as
replicates, we decompose each design's headline variance into system, judge, system-by-judge
and epoch-noise components, each read against its df-proportional no-effect expectation. The
interaction term is the decision-relevant one, because it asks whether the two judges agree
about *which* system is better; it is clearly above its 13.79% reference line in four of the
eight judged designs (median 17.2%, maximum 46.5%) and at or below it in the other four. This
also disciplines the conclusion in two directions the bias literature does not: system and
judge footprints are comparable at the median (35.6% versus 35.3%), so the correct statement
is not that the judge overwhelms the signal; and the disagreement is design-specific — the
models differ on most designs, the judges clearly disagree about the ordering on a minority,
and on the rest the systems are too tightly spaced for either judge to resolve.

### 2.2 Reliability and agreement in evaluation

The reflex response to judge unreliability is to report agreement — between judge and human,
or between two judges — and to treat a respectable coefficient as a licence to proceed.
Zheng et al. (2023) established the template with their human-agreement figure. But the
subjective-task literature has been arguing for some time that agreement statistics conceal
more than they certify. Aroyo et al. (2023), in DICES, argue that the demand for a clean
separation between positive and negative examples simplifies and obscures the inherent
subjectivity of safety judgements; they build a dataset with high replication per item and
fine-grained rater demographics precisely so that variance, ambiguity and diversity can be
*observed* rather than aggregated away. Baan et al. (2022) make the sharper technical point
for the case where raters legitimately disagree: measuring calibration against a human
majority is theoretically problematic when the disagreement is inherent, and they derive
instance-level measures that preserve the class frequency, ranking and entropy of the
judgements instead. Gehrmann, Clark and Sellam (2022) survey two decades of accumulated flaws
in generated-text evaluation practice — human and automatic alike — and observe that better
methods are documented but rarely adopted.

`[CITATION NEEDED — foundational chance-corrected agreement statistics (Cohen's κ, Krippendorff's α) and their standard interpretive thresholds; no vault source located]`
`[CITATION NEEDED — the prevalence/base-rate paradox in κ, i.e. that a high raw agreement rate can coexist with a near-zero chance-corrected coefficient on skewed label distributions; no vault source located]`
`[CITATION NEEDED — generalizability theory / variance-component reliability (Cronbach and successors) as the measurement-theoretic ancestor of the decomposition used in §4; no vault source located]`

Our distinction here is a logical one and it is easy to state. Agreement between two judges is
a *necessary but not sufficient* diagnostic. Two judges can agree on a respectable share of
individual verdicts and still reorder the systems under test, because reordering depends on
where the disagreements fall relative to closely-spaced per-system aggregates, not on how many
there are. That is why we decompose variance rather than reporting a headline agreement
coefficient: the interaction term detects the failure that an agreement rate is structurally
incapable of detecting. It is also why our referee agreement figures are reported strictly
within stratum and within design and are never pooled — the referee sample is
disagreement-enriched by construction, so any single overall agreement number computed over it
would be uninterpretable.

### 2.3 Benchmark validity and what a leaderboard can carry

A third literature asks whether benchmarks measure what their names claim. Raji et al. (2021)
argue that a small set of valorised benchmarks are treated as general measures of progress
they cannot support, and read this as a construct-validity failure in their framing.
Schlangen (2021) makes the adjacent methodological point that the field rarely states the
argument connecting benchmark improvement to progress, or progress towards what. Bean et al.
(2024), with 29 expert reviewers over 445 benchmarks from leading NLP and ML venues, find
recurring patterns in measured phenomena, tasks and scoring metrics that undermine the
validity of the resulting claims, and issue eight recommendations. Eriksson et al. (2025)
meta-review roughly 100 studies of benchmarking shortcomings and catalogue construct-validity
problems alongside contamination, documentation failures, gaming and the difficulty of
distinguishing signal from noise — noting that benchmark practice is shaped by commercial and
competitive dynamics that reward state-of-the-art numbers. Ye et al. (2025) propose importing
psychometrics wholesale, organising the problem into evaluation, validation and enhancement,
and flagging test-retest reliability and prompt sensitivity as first-order threats. Jiang et
al. (2025) attack a specific decay mode — static value-alignment benchmarks saturating or
leaking into training data — with adaptive item generation grounded in measurement theory.
For value-laden constructs specifically, LaCroix and Luccioni (2025) argue that an "ethics"
benchmark is not constructible at all, since moral dilemmas have no keyed answer by design and
benchmarking ethicality presupposes a contested metaethical position; their constructive
proposal is to talk about *values*, stated explicitly as whose values they are.

That last recommendation is the design principle our testbed already follows, and it is worth
being exact about it. The instrument is anchored to a named fifteen-work,
Protestant-Reformed-dominant Christian-ethics registry and measures behavioral concordance
with that specified corpus — never fidelity to Christianity, to Scripture, or to moral truth.
Our contribution to this thread is empirical rather than programmatic. The validity literature
argues, largely from review and from first principles, that leaderboards outrun their
evidentiary basis. We report a full-scale run of one benchmark and conclude that its
comparative surface is unsupported at the tested tier — and we treat that as the result, not
as a setback to be worked around. The judge-free design in the suite functions as an exact
positive control on this conclusion: its judge and interaction terms are zero by construction
and are recovered as such, and its pre-registered pairwise contrasts yield 0 of 10
Bonferroni-widened intervals excluding zero. A real ordering is therefore not merely being
obscured by judge noise; at this tier there is no ordering to obscure.

### 2.4 Meta-evaluation, referee and ensemble approaches

The final thread uses models to audit models. Meta-evaluation benchmarks — KUDGE (Son et al.,
2024a) and MM-Eval (Son et al., 2024b) — score judges against human-annotated keys, and Gu et
al. (2024) propose a reliability-oriented meta-evaluation benchmark as part of their survey.
A related line studies whether structured multi-model protocols can lift a weaker judge:
Elasky et al. (2026) study proposer-critic debate in a stronger-debater, weaker-judge setting
and find it helps only under a stateable condition — the critic's classification ability must
exceed the judge's, and the judge must treat critic speeches as claims to verify rather than
testimony to summarise — with null effects and dropped verification rates where that condition
fails. Their recommended artefact is a pre-deployment audit that predicts when the protocol
will help, and a cheaper primitive that recovers most of the benefit at lower inference cost.

`[CITATION NEEDED — panels/juries/ensembles of multiple smaller LLM judges as a substitute for a single large judge (e.g. the "panel of LLM evaluators" line); no vault source located]`
`[CITATION NEEDED — work reporting that LLM annotators match or exceed crowdworkers on annotation tasks, the substitution argument that motivates cheap-judge pipelines; no vault source located]`
`[CITATION NEEDED — an explicit accounting of the API cost of meta-evaluation as a barrier to routine pre-publication judge auditing; the cost barrier is asserted here from the design constraints of this study rather than from a cited source]`

Three features separate our protocol from this thread. First, its purpose: panels, juries and
debate protocols aim to produce a *better aggregate score*; our two referees aim to **localize
failure**. The partition they produce — a judge-character component, a rubric-and-state-taxonomy
component, and a small set of defect items whose empty keyed anchors mechanically manufacture
disagreement — matters because those three diagnoses imply three different repairs, with
different costs and different consequences for what the benchmark may afterwards claim. A
judge-swap check alone cannot distinguish them. Second, its economics: both referee arms run
through subscription channels at $0 API spend on a frozen, disagreement-enriched sample scored
with byte-identical shipped prompts, blind to system identity and to the shipped verdicts,
which is what makes the procedure available as routine pre-publication QA rather than as a
funded follow-up study. Third, and most important, its epistemic ceiling. We frame referee
convergence throughout as **reference-model concordance, not ground truth**. Two referees
agreeing establishes that two independent stronger references converge on a reading; it does
not certify any shipped judge as correct, and referees trained under similar regimes may share
correlated error. Nothing in §5 should be read as a demonstration that a judge is right.

---

## Citation ledger

Every citation appearing in §2 above, with the vault file it was read from. No citation appears
in the text that is absent from this table.

| Cited as | Vault source file |
|---|---|
| Zheng et al. (2023), *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* | `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2023-Zheng-Judging Llm Judge With.md` |
| Gu et al. (2024), *A Survey on LLM-as-a-Judge* | `CEI-Lit-WS/papers/2024-Gu-A Survey on LLM-as-a-Judge.md` |
| Shi et al. (2025), *A Systematic Study of Position Bias in LLM-as-a-Judge* | `CEI-Lit-WS/papers/2025-Shi-A Systematic Study of Position Bias in LLM-as-a-Judge.md` |
| Wataoka et al. (2024), *Self-Preference Bias in LLM-as-a-Judge* | `CEI-Lit-WS/papers/2024-Wataoka-Self-Preference Bias in LLM-as-a-Judge.md` |
| Koo et al. (2023), *CoBBLEr: Assessing the Cognitive Bias of LLMs as Evaluators* — note: this vault file's `Metadata` block lists "Guo, X.; Zhang, B.; …" while its `Authors` block lists Koo, Lee, Raheja, Park, Kim, Kang; the author line should be verified against the arXiv record before submission | `CEI-Lit-WS/papers/2023-Guo-COBBLER.md` |
| Son et al. (2024a), *LLM-as-a-Judge & Reward Model: What They Can and Cannot Do* (KUDGE) | `CEI-Lit-WS/papers/2024-Son-LLM-as-a-Judge & Reward Model What They Can and Cannot Do.md` |
| Son et al. (2024b), *MM-Eval: A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge and Reward Models* | `CEI-Lit-WS/papers/2024-Son-MM-Eval A Multilingual Meta-Evaluation Benchmark for LLM-as-a-Judge.md` |
| Faisal et al. (2024), *Dialectal Toxicity Detection: Evaluating LLM-as-a-Judge Consistency Across Language Varieties* | `CEI-Lit-WS/papers/2024-Faisal-Dialectal Toxicity Detection Evaluating LLM-as-a-Judge Consistency.md` |
| Beyer et al. (2025), *LLM-Safety Evaluations Lack Robustness* | `CEI-Lit-WS/papers/2025-Beyer-LLM-Safety Evaluations Lack Robustness.md` |
| Aroyo et al. (2023), *DICES: Diversity in Conversational AI Evaluation for Safety* | `CEI-Lit-WS/papers/2023-Aroyo-DICES Dataset.md` |
| Baan et al. (2022), *Stop Measuring Calibration When Humans Disagree* | `CEI-Lit-WS/papers/2022-Baan-Stop Measuring Calibration When Humans Disagree.md` |
| Gehrmann, Clark and Sellam (2022), *Repairing the Cracked Foundation* | `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2022-Gehrmann-Repairing The Cracked Foundation.md` |
| Raji et al. (2021), *AI and the Everything in the Whole Wide World Benchmark* | `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2021-Raji-Ai And The Everything.md` |
| Schlangen (2021), *Targeting the Benchmark: On Methodology in Current NLP Research* | `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2021-Schlangen-Targeting The Benchmark Methodology.md` |
| Bean et al. (2024), *Measuring What Matters: Construct Validity in LLM Benchmarks* | `CEI-Lit-WS/papers/2024-Bean-Measuring What Matters - Construct Validity in LLM Benchmarks.md` |
| Eriksson et al. (2025), *Can We Trust AI Benchmarks? An Interdisciplinary Review* | `CEI-Lit-WS/papers/2025-Eriksson-Can We Trust AI Benchmarks An Interdisciplinary Review.md` |
| Ye et al. (2025), *Large Language Model Psychometrics* | `CEI-Lit-WS/papers/2025-Ye-Large Language Model Psychometrics.md` |
| Jiang et al. (2025), *Raising the Bar* (GETA) | `CEI-Lit-WS/papers/2025-Jiang-Raising the Bar.md` |
| LaCroix and Luccioni (2025), *Metaethical perspectives on 'benchmarking' AI ethics* | `CEI-Lit-WS/papers/2025-LaCroix-Metaethical perspectives on ‘benchmarking’ AI.md` |
| Elasky et al. (2026), *Debate Helps Weak Judges* | `CEI-Lit-WS/papers/2026-Elasky-Debate Helps Weak Judges Reward.md` |

**Duplicate-source note.** Two of the works above also have near-duplicate vault entries under
different first-author strings — construct validity in LLM benchmarks appears additionally at
`CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Li-Measuring What Matters Construct.md`,
and LLM psychometrics additionally at
`CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/EXTRACT/2025-Gupta-Large Language Model Psychometrics.md`.
The `papers/` entries are used as canonical here; the author lines should be reconciled once
before the reference list is finalised.

**Open gap markers left in this part (5):** foundational chance-corrected agreement statistics;
the κ prevalence/base-rate paradox; generalizability theory / variance-component reliability;
panels or juries of LLM judges; the substitution and cost-barrier literature motivating cheap
judge pipelines.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
