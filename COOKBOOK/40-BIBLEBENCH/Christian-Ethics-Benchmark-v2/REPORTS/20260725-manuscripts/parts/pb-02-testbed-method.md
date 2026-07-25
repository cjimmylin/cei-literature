**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

**PART FILE — assembles into paper (b).**

*Draft §3–§4 for "Judging the Judges for $0: A Two-Referee Concordance Method for Localizing LLM-as-Judge Failure on Value-Laden Rubrics." Venue-generic and author-generic. §3 is a compressed, self-contained description of the testbed instrument, included only so that §5's results are interpretable without the companion benchmark paper in hand; the full instrument exposition belongs to that paper.*

---

## 3 The testbed instrument

The methods in §4 take an existing model-graded evaluation and ask how much of what it reports is a property of the systems being measured and how much is a property of the judge measuring them. Exercising them requires a testbed whose rubrics are genuinely value-laden — the regime in which LLM-as-judge is least trustworthy. This section describes that testbed at the level of detail §5 requires, and no further.

### 3.1 The construct

The testbed instrument (WALKWORTHY v2) measures what a language model **does**, not what it professes, when a scenario's incentives, pressures, or framings pull against a keyed target behavior. Conduct is scored for **concordance with a named, specified corpus**: a fifteen-work registry of Christian-ethics texts that is deliberately single-tradition and identified as such — **Protestant-Reformed-dominant**. Every keyed target behavior is anchored to specific chapters or dictionary entries of that registry, and the anchors are recorded per item and are grep-verifiable against the fifteen source texts.

Two anchoring rules are load-bearing constraints on the construct rather than incidental style choices. First, **direct Scripture anchoring is disallowed by construction**: citation forms naming a passage are book-mediated, anchoring to a registry author's treatment of it, so the keyed behavior is always mediated through a named human ethicist's exposition. Second, **one registry work is restricted to contrast-only use** and carries no consensus claim anywhere in the bank.

The construct must not be overstated, and the discipline binds every claim in this paper. The instrument measures behavioral alignment with the consensus moral teaching of the fifteen-work registry. It is **not** a test of theological truth, of "Christianity," or of whether the corpus's own positions are correct. Results are reported as *aligned with the registry corpus*, never as *correctly Christian*, and no result here is a religious-authority or theological-truth claim.

Items carry an ethical-domain letter that drives anchor selection, a tier, and a stratum. Stratum-`c` items are **intra-corpus disputed** — cases where the fifteen works do not speak with one voice — and are quarantined from comparative claims; headline scope is stratum-`a` only, with 24 stratum-`c` items held out of the headline cells.

### 3.2 Bank census and run surface

At bank revision **2026-07-24b** the public run surface is **344 runnable items** across **ten method-distinct designs**. Because paired-administration designs emit one dataset line per administration — a seat, a twin, a motive arm, or a scripted conversation — rather than one line per item, the 344 items expand to **563 runnable administration lines**; single-administration designs emit one line per item. A stratified **holdout of 158 items** is withheld from all public surfaces; only its existence and size are reported here, and no holdout item text or identifier appears anywhere in this paper.

A sidecar stratifier classifies public items by whether the keyed behavior diverges from generic RLHF harmlessness: **29 `yes`, 129 `partial`, 186 `no`**, with only the `yes` and `no` poles pre-registered as cells.

### 3.3 The ten designs

Each design is a distinct probe format with its own keyed rubric and headline metric. The table gives what §5 needs: what each design scores, its headline, and — the distinction that organizes this paper — whether that headline passes through a model judge.

| # | Short name | What it scores | Headline metric | Scoring mode |
|---|---|---|---|---|
| 01 | goodsamaritan | Costly truth-telling when an objective and an unobserved condition give cover to defect | `full_obedience_rate` | judge-scored |
| 02 | twomasters | Consistency under a scripted multi-turn pressure-escalation ladder | `break_rate`; sole headline `break_turn` | judge-scored |
| 03 | quiettongue | Stated-versus-enacted alignment across paired `say` / `do` administrations | `say_do_gap` | judge-scored |
| 04 | innerweight | Whether evaluation of identical conduct shifts with an attributed motive | `motive_delta_mean` (signed) | judge-scored |
| 05 | ordoamoris | Ordered-love allocation of a fixed scarce resource against keyed constraints | `csr_mean` (`constraint_satisfaction_rate`) | **judge-free primary** |
| 06 | crookedpath | Quality of moral reasoning on a hard dilemma, seven-category process profile | `profile_mean` | judge-scored |
| 07 | seventyseven | Scripted comfort-then-truth therapeutic arc; passes only on a terminal faithful-counsel turn | `arc_pass_rate` | judge-scored |
| 08 | vocationfork | Whether a load-bearing qualifier is held when an instruction licenses deleting it | `covert_overt_gap` | judge-scored |
| 09 | doubleedge | Cross-seat consistency of the floor of honest counsel on one dispute | `symmetry_index` | judge-scored |
| 10 | strangergate | Whether help, mercy, or honesty changes with a deservingness cue | `mercy_delta` | judge-scored |

Designs 02 and 07 are scripted ladders in which a **classifier model** routes each turn's branch by classifying the prior response into a turn-state; the classifier is part of the instrument and is pinned (§4.4). Designs 06 and 09 embed matched-quality reference answers in the judge prompt and therefore required — and passed — a judge-neutrality certification (G5) that blind-scores matched-quality, opposite-conclusion answer pairs for a systematic conclusion penalty. G5 certifies conclusion-neutrality only; a judge can be conclusion-neutral and still anchor-dependent, a separately documented property governed by the two-judge rule. Three gap headlines are read jointly with a companion metric by standing rule (`say_do_gap` with `revealed_faithful_rate`; `covert_overt_gap` with `covert_protection_rate`; `mercy_delta` with `mercy_pass_rate`), so no gap metric is ever read alone.

### 3.4 Design 05 as a built-in positive control

Design 05 matters to *this* paper out of proportion to its size. Its primary metric, `constraint_satisfaction_rate`, is computed by a strict parser from the model's emitted allocation block against the item's keyed constraints, and **never reaches a judge**. Only a secondary `rationale_honesty` category is model-graded. Design 05 is therefore a **positive control internal to the instrument**: every judge-effect measurement in this paper can be run on a surface where the true judge effect is known in advance to be exactly zero. Any nonzero judge effect recovered on design 05 would be an artifact of the measurement pipeline rather than a property of judging, and §4.2 uses this as an arithmetic correctness check on real data.

Because design 05 depends on the model emitting a parseable block, format non-compliance is a real and separable failure mode; a one-shot format-retry solver and a bounded offline re-parse are applied, with `format_retry_used` surfaced so retry compliance never masquerades as first-pass compliance.

### 3.5 The construct-validity annotation (CV-1)

One annotation is carried forward here because it bounds how §5's per-design results may be read. **CV-1** records that, at the cheap system-under-test tier, designs **04, 05, 06, 07 and 10** are annotated *candidate-distinct* from generic RLHF harmlessness, with the remainder marked non-discriminant at this altitude. The set was amended from its original {04, 05, 10} to add designs 06 and 07 by owner ruling (PE-22). CV-1 is stated as an **annotation, not an empirical finding**: it has not been established by a discriminant test, and upgrading it to a finding would require a positive demonstration, such as a harmlessness-only control model or a discriminant-validity correlation against a generic-safety benchmark.

---

## 4 Method

Three methods are reported. The first (§4.1) is a binary per-design verdict obtainable from any two-judge design. The second (§4.2) converts that verdict into a quantity at zero marginal cost from any run with replication. The third (§4.3) is the localization step — it says *where* the judging fails — and is obtained for **$0** in metered spend.

All three run over one measurement substrate: the full public bank at revision 2026-07-24b, **five systems under test × three epochs**, 150 evaluation runs with zero non-success statuses, 563 administrations per system per epoch, 8,445 total administrations, plus 15 judge-B rescoring passes producing 8,445 judge-B verdict rows. The five systems are a fixed roster of cheap-tier chat models; they are never ranked or ordered anywhere in this paper, and every table in §5 is either per-design or per-judge.

### 4.1 The two-judge swap protocol (rule R4)

The instrument mandates a **two-judge cross-family rule**, R4: a comparative claim must hold in the same direction under two judges drawn from different model families, or the contrast is declared *judge-sensitive* and no claim is made.

The two judges are deliberately cross-family: **judge-A is `gpt-4.1-nano`** and **judge-B is `llama-3.3-70b`**. Judge identity is a task parameter of the harness, and the crucial property of the design follows from that: **every administration is scored by judge-A during the run and rescored offline by judge-B from the stored transcript.** No system under test is re-run. The system's response text is fixed byte-for-byte across the two scorings, so the only variable that changes between the judge-A and judge-B readings of a cell is the judge itself. This is what makes every difference reported in §5 attributable to judging rather than to sampling from the system under test.

The **ordering-flip test** asks, per design and per epoch, whether the rank order of the five systems by that design's headline metric is preserved under the judge swap. The criterion is exact equality of the full five-way permutation of unrounded point estimates, with ties broken by a stable sort and no interval applied; the implementing tool labels it a *naive point-estimate order*. A design that preserves that ordering in an epoch is recorded STABLE for that epoch; a design whose ordering permutes is recorded as flipping. The criterion is deliberately strict and correspondingly blunt: a single adjacent transposition counts as a flip, and it reports no magnitude, so a flip verdict should be read alongside the per-cell values in §5.2 rather than on its own. Running the test per epoch rather than once is itself part of the method: an ordering that holds in one epoch and permutes in another is not a stable ordering but a coincidence at that sample, and the three-epoch design is what exposes that.

One reporting detail is load-bearing for §5's design-02 material. Design 02's **`break_turn` is the sole headline**; `pushback_rate` is a **secondary** metric, reported **per judge only and never pooled**, with a standing caveat that the cross-judge stability of the underlying `pushback_with_alternative` state is untested and that all earlier figures for it are single-judge. Judge-B's `pushback_rate` was computed by importing the project's own `_break_turn_item` helper rather than by a parallel reimplementation, so both judges' figures come from **identical code on an identical item base** — again leaving the judge as the only variable.

### 4.2 The variance decomposition

The ordering-flip test returns a binary verdict per design. It establishes judge-sensitivity qualitatively but says nothing about *how much* of what the instrument reports is attributable to the judge rather than to the model. Because three epochs were run, that quantity is recoverable from data already on disk at no additional cost, fully offline.

The design is a balanced **5 (system under test) × 2 (judge)** layout with the **three epochs as replicates**, fitted per design on that design's reported headline metric:

```
SS_total (df 29) = SS_SUT (4) + SS_judge (1) + SS_SUT×judge (4) + SS_error (20)
```

Each term answers a distinct question:

| Term | Question it answers |
|---|---|
| **SUT** | Do the models differ at all? |
| **judge** | Do the judges differ in overall severity — a level shift? |
| **SUT × judge** | **Do the judges disagree about which model is better?** |
| **error** | Epoch-to-epoch stochastic noise |

The methodological point that justifies the epoch budget is explicit: **using epochs as replication is what makes the interaction estimable separately from error.** Without replication, `SUT × judge` — the term that actually voids comparative claims — is confounded into the residual, and the judge's footprint is understated. A single-epoch two-judge run can report a judge main effect but cannot separate the interaction from noise, which means it cannot measure the quantity that decides whether a leaderboard is admissible.

The decomposition carries a **built-in correctness check**. Design 05's primary metric is judge-free (§3.4), so its `judge` and `SUT × judge` terms must be exactly zero. They are: **0.000000 and 0.000000**. This validates the decomposition arithmetic on real data rather than on a simulation. It does not by itself license any claim about the other designs: a control whose true value is zero exercises only the null path. The separate conclusion that nonzero judge effects elsewhere are not rescore-pipeline artefacts rests on a different observation — design 05's judge-A and judge-B headline cells are identical to four decimal places on all five systems (§5.4).

Two constraints travel with every figure the decomposition produces. It decomposes variance in the **reported headline** — one value per system × judge × epoch cell — not in per-item scores. And it uses **two judges only**: the judge main effect is a one-degree-of-freedom contrast, not an estimate of a judge population, and may not be read as "judges in general account for X%". Design 05 (zero by construction) and the floor-saturated design 07 are excluded from cross-design summaries; including design 05 would bias the judge medians downward.

### 4.3 The $0 two-referee meta-audit

**Provenance and comparability — read before §5.6.** Unlike the swap test and the variance
decomposition, the referee meta-audit was **not** run over the full-bank administration
reported in §5.1–§5.5. It was run over the earlier 2026-07-16 pilot logs, at the prior bank
revision. Under C9 it is therefore a **separate comparability line**, and its stratum
denominators are pilot-run turn counts — 815 judgeable turns on design 07 and 1,610 on
design 02 — not the full-bank counts that appear in the §5.6 agreement table. Where §5.6
converges with the decomposition, that convergence is across two *runs at different bank
revisions*, which is a weaker form of corroboration than two analyses of one dataset and is
reported as such.

The first two methods measure *that* the judges disagree and *how much*. Neither can say which judge is diverging, or whether the disagreement is a judge property at all rather than a property of the rubric. That question cannot be answered from inside the judge pair: two raters who disagree are symmetric evidence about each other, and there is no third vantage point.

The meta-audit supplies a third vantage point deliberately and provisionally, and the epistemics are stated up front rather than in a closing caveat: **this is reference-model concordance, not ground truth.** The referees are stronger models, not oracles. A referee siding with one judge is evidence about *judge character* — which judge diverges, and in which direction — and never proof that the judge is correct. Two referees agreeing may share correlated error from similar training regimes, so referee-to-referee agreement is *consensus* evidence, not *correctness* evidence. No result in this paper claims a referee proves a judge right.

**Frozen, disagreement-enriched sample.** The audit runs on a single pre-committed manifest of **942 units**, frozen before any referee dispatch, with a recorded manifest hash, a fixed seed, and a fixed draw order; the manifest is the population, and no units were added after the first dispatch. The strata are:

| Design | Stratum | n |
|---|---|---:|
| 07 | disagreement | 392 |
| 07 | control | 150 |
| 02 | disagreement | 200 |
| 02 | control | 80 |
| 06 | gap | 60 |
| 06 | control | 60 |
| **Total** | | **942** |

Disagreement on designs 02 and 07 is defined as judge-A state ≠ judge-B state at the same positional turn, with `unscorable` counting as a state. Design 06 has no state taxonomy, so its contested stratum is the top 60 units by absolute divergence between the two judges' profile means.

**Disagreement enrichment, and why it forbids a pooled headline.** The sample deliberately over-represents units on which the two shipped judges already disagreed: on design 07 it takes *all* disagreement turns, and on designs 02 and 07 the contested strata are sampled at rates unrelated to their population base rates. The sample's composition is therefore an artifact of the sampling design, not of the instrument. Any pooled "overall agreement" figure computed across these strata would be a weighted average whose weights were chosen by the sampler, and would move arbitrarily with the enrichment ratio. **Agreement is therefore reported per design and per stratum, never pooled**, and no overall-agreement headline is reportable without the per-stratum split adjacent. This constraint binds §5 and every downstream use.

**Blindness.** Referee prompts were exported **byte-identical to the shipped judge prompts** by reusing the project's own prompt-assembly function rather than forking it; export determinism was verified across two runs, and each row carries a prompt hash. Referees received only `{prompt_hash, prompt}` slices — never judge-A or judge-B verdicts, never system-under-test identities, never repository paths. Batches were ladder-spread so that no two turns of one conversation shared a batch.

**Two independent referee channels, both at $0 metered spend.** Arm 1 dispatched a **Claude Opus** referee through a subscription agent channel: 40 dispatches, 942/942 verdicts ingested, 0 hash rejects, 0 refusals, 0 hand-patched verdicts, $0 API spend. Arm 2 dispatched **GPT-5.6-Sol** through a command-line exec channel over the *same* frozen manifest with no new sampling, hardened for blindness — a working directory outside the repository, network access disabled, tool servers disabled, ephemeral sessions against cross-batch contamination, reading only the batch slices and writing only verdict files: 39 batch dispatches, 942/942 accepted on the first pass, 0 re-asks, 0 refusals, 0 hash rejects, $0 API spend. The cross-vendor, cross-channel construction is deliberate; it is also why any referee-versus-judge difference composes a channel effect with a model effect. Each referee scored each unit once, so within-referee noise is unmeasured, and roughly two dozen units share one agent context per batch, so within-batch non-independence applies to both arms.

### 4.4 Governing rules

Four standing rules govern every number reported in §5 and are stated here so that the results section can be read without re-deriving them.

- **R3 — interval language only.** Estimates are reported as point estimates with intervals; the language is "excludes zero" or "crosses zero". No significance testing is performed, the word "significant" is not used as an adjective, and no significance markers appear in any table.
- **R4 — the two-judge precondition.** A comparative claim must hold in the same direction under judge-A and judge-B. A direction flip is reported as *judge-sensitive — no system claim*. A related same-family exclusion rule applies where a system under test and a judge share a model family; such cells lean on the other judge explicitly.
- **C6 — no cross-classifier pooling, ever.** The branch classifier for designs 02 and 07 is part of the instrument, pinned by model slug, provider, prompt-template hash, and route policy. A classifier change is an instrument change, and cells scored under different pinned classifiers are not comparable and are never pooled. For this lineage the **classifier is pinned at `gpt-4.1-nano`**.
- **C9 — first-use and comparability fences.** Results are fenced to bank revision 2026-07-24b, public bank only, holdout untouched. Cells produced under earlier bank revisions, under the pre-anchor design-08 judge rubric, or under a different classifier pin are separate comparability lines and are not merged. Pre-registered comparison families are declared before first use of the data they govern.

Finally, two scope statements. WALKWORTHY v2 is a **parallel** harness established by ruling; version 1 remains canonical for release evidence, and nothing here is a release claim. And the offline judge-level analyses reported in §5 are read at the **instrument level and judge level only** — they support no comparative reading between systems under test.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
