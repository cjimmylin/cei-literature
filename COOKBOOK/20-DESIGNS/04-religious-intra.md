# Design 04 — INTRA: Intra-Tradition Reasoning Assessment

> **CEI COOKBOOK · 20-DESIGNS.** Fable-authored (2026-07-05). Status: full design, pre-pilot;
> long-pole dependency = tradition-board partnerships (start early). Venue framing: NeurIPS D&B +
> a FAccT companion on the governance model. Grounding: KB doc 10; religious-values dossier;
> RV meta-evaluation digest; cards cited inline.

---

## 1. Motivation

The RV meta-evaluation (401 candidates, 14 traditions) shows a field measuring the wrong construct:
only 27.7% of gate-passing benchmarks test theological *reasoning* (p=0.0015); mean values-relevance
is 30.0/100 (d=−1.23; the field's #1 instrument is a knowledge-extraction task — the "ELQV paradox");
93.75% treat traditions as monoliths; and 8/14 traditions have zero viable benchmarks. The one
instrument that discriminated at the frontier (93.3-point spread) was a domain-specific,
liturgical-language, exact-match reasoning task (Arabic *fara'id* inheritance law), while every
holistic rubric produced ceiling/floor pathology. And the barrier for uncovered traditions is
**infrastructure, not formalizability** (r=0.74 vs r=0.41 n.s.).

**INTRA is the first *multi-tradition, denominationally-resolved* reasoning-first benchmark — built by
the shared-task playbook that made Islamic benchmarking strong (the QIAS 2025 EMNLP shared task on
Islamic inheritance reasoning is the named template, T2), aimed first at the traditions with corpora
but no community pipeline (Judaism, Confucian/Taoist canon, Jainism).** Single-tradition reasoning-first
instruments already exist (QIAS 2025, BuddhismEval); INTRA's contribution is generalizing the recipe
across traditions and conditioning gold on school membership, not "reasoning-first" per se (see §8).

**Primary discrimination bet (revised post-gate).** The M-layer is by construction a
knowledge/recognition-plus-computation layer, so it is demoted to a *paired capability baseline*
(Law 1: recognition is baseline, not headline). The **discrimination story runs on the D-layer
ask-or-flag fork and the V-layer, treated as co-primary**; M-layer spread is diagnostic, not the
success condition. **Falsification condition (Law 7 / KB 01 Step 0):** INTRA claims to measure
*religious-reasoning propensity, not religious knowledge*; that claim is **falsified** if the
pre-registered pilot shows M-layer carries the discrimination while D-flag and V fail to produce a
continuous mid-band spread — in which case INTRA reverts to an honestly-labeled jurisprudential-knowledge
benchmark (see §6 kill criterion).

- **K — Knowledge floor** (doctrine facts, source identification): expected to saturate; capability
  control only.
- **M — Method Application**: the T2 recipe generalized — computable, exact-match problems *within*
  a tradition's jurisprudential/casuistic method (T2 = **QIAS 2025**, the Islamic-inheritance-reasoning
  shared task; Islam here is *method transfer*, not a new instrument — the niche is already crowded,
  see §8). Per-tradition subdomains chosen for verifiable answers + genuine difficulty gradation:
  fara'id shares and *'awl/radd* redistribution (Islam); halakhic calendrics, kashrut ratios
  (*batel b'shishim*), eruv geometry (Judaism); canon-law marriage impediments and dispensation logic
  (Catholicism); karma-consequence casuistry under specified school premises (Dharmic; Jain *anuvrata*
  case rulings); ritual-propriety precedence orderings (Confucian *li*). **Pre-registered M-layer kill
  criterion:** if M-layer capability-PC1 correlation ≥40% (Law 1 red-flag threshold) OR the best
  frontier model exceeds ~70% of ceiling on the hard ("conflicting-rule-with-meta-principle") tier
  (KB 04 §6 item 1 — the inherited fara'id exemplar saturated at 100%, so this is a live risk), the
  M-layer is reported as capability-only and cannot carry any values claim.
- **D — Denominational Conditioning**, decomposed into two sub-scores (Law 2 — one scalar must not hide
  two constructs):
  - **D-know** — apply the *specified* school's ruling (Hanafi vs Ja'fari inheritance; Ashkenazi vs
    Sephardi practice; Theravada vs Mahayana precept scope). Knowledge/capability sub-score, expected
    to saturate; paired baseline.
  - **D-flag** — on *unspecified*-school forks, ask or flag the fork; a silent single-school answer
    scores as a **doctrinal flattening error** (the 93.75% problem, inverted into a metric). This is
    the behavioral signal and the reported **headline**; only D-flag — the ask-or-flag *scoring
    mechanic* — supports the "no precedent in the 965 characterizations" claim (§8).
- **V — Values-Behavioral layer** (co-primary with D-flag): multi-turn advisory scenarios (pastoral,
  familial, commercial) where the model advises a person *within* their stated tradition. Scored on:
  reasoning-from-within (not comparative-religion lecturing — the "external analytical register"
  deduction from RV trials), epistemic integrity ("scholars differ" acknowledged on genuinely disputed
  questions, and NOT on settled ones — a calibration measure, both directions scored [2025-Lahmar]),
  harm floor compliance, and recipient-standpoint responsiveness (Tronto-phase machinery from NormEval
  Appendix H, imported). V-scoring feasibility is gated on the §5 keypoint-decomposition pilot.

## 3. Task design details

- **Language axis**: M-layer items presented in liturgical/source language AND the local vernacular;
  per-language scores + inter-language consistency (bias direction flips with language
  [2025-Hossain-BRAND]); default-to-majority contrastive probes and Specific-vs-General scope items
  embedded [2025-Hossain; 2025-Lahmar].
- **Difficulty engineering**: M-layer graded by derivation depth (single-rule / multi-rule /
  conflicting-rule-with-meta-principle); adversarial filtration on pilot; a "plausible-wrong-derivation"
  distractor set built from real student errors (sourced from seminary/madrasa teaching materials with
  permission).
- **Indirect elicitation battery** (V-layer supplement): creative-completion stance probes, forced
  perspective-taking, differential-refusal audit across traditions (refusal-rate asymmetry as
  stigmatization signal [2024-Hovy]) — calibrated to avoid the saturation trap of extreme probes
  [2024-Elrod].
- **Capability coupling**: every values run pairs with a matched neutral-domain task so alignment-tax
  and over-correction are measurable [2021-Barikeri-REDDITBIAS].
- **Robustness battery** (KB 01 Step 7 + checklist — mandatory, previously missing): **answer-order
  reversal** on M/D MCQ-like items (order-sensitivity marks dead items, KB 04 §4); **paraphrase
  flip-rates**; **per-condition SD** (correct-answer-effect check, KB 03 §5); and an **eval-awareness
  comparator arm — monitored-vs-unmonitored (announced-vs-embedded)** on the multi-turn V-layer, where
  evaluation-awareness modulates behavior (Law 6; KB 03 §5.3). Flip-rates and per-condition SD are
  reported as first-class numbers; the monitored/unmonitored compliance gap is reported, not assumed in
  direction.

## 4. Governance and construction (the differentiating half of the design)

- **Two separated boards per tradition (de-circularized ground truth, C2):** roles that were fused are
  now split so label reliability is independently computable (KB 03 §2: "no coefficient reported =
  disqualifying"; KB 07 §4: never let one body generate AND adjudicate).
  - **Authoring board** — in-tradition scholars (NATIVE positionality; CONSULTED minimum; composition
    disclosed) who write items, propose school labels and "scholars differ" designations, and hold
    release veto. Honoraria budgeted; sacred-text ethics respected (interpretive frameworks are
    tradition-internal — religious digest §7 lesson 8).
  - **Independent validation panel** — in-tradition scholars *not* on the authoring board who re-label
    a blind sample, yielding a real chance-adjusted per-category κ/α, and who supply the human ceiling
    (reported explicitly as ≠ 1.0, never the authors' own consensus). Sized for computable IAA per
    KB 03 §2.
  - **Per-school coverage (M3):** because D-forks turn on school membership (Hanafi vs Ja'fari;
    Ashkenazi vs Sephardi; Theravada vs Mahayana), each fork's gold requires sign-off from
    representatives of *each* school in the fork — boards are sized to school coverage, not tradition
    coverage, via per-school external raters where a single board cannot span the schools. Budget and
    honoraria scale accordingly (see §7).
  - The claimed novelty is the governance *protocol* (veto + school-label ownership + disclosed
    positionality + honoraria + multi-tradition + author/validate separation), **not** "experts author
    items" — in-tradition expert authorship/grading already exists (Gospel Coalition, CatholicBench; §8).
- **Shared-task bootstrap**: for the two CRITICAL-GAP traditions, INTRA's v1 deliverable is a
  *community shared task* (Judaism: Sefaria-derived M-layer + responsa-based V-layer; Confucian/Taoist:
  Chinese Text Project canon) — the mechanism proven to convert corpus wealth into benchmark
  infrastructure (religious digest §7 lesson 9: the first shared task is the hardest; investment is
  front-loaded). QIAS 2025 is the named exemplar of this playbook for a *covered* tradition; INTRA's
  contribution is deliberately porting it to zero-coverage traditions.
- **Oral/communal traditions explicitly out of scope** with the reasoning stated (structural epistemic
  exclusion; CARE principles; externally-led benchmarks inappropriate — religious digest §7 lesson 11).
  INTRA's datasheet names this boundary rather than tokenizing.
- **Cross-vendor protocol hygiene** (religious digest §7 lesson 12, from its own caveats): matched
  administration, blind gold labels, independent cross-family rubric scoring, provenance documentation.
  (All lesson citations point to `30-EVIDENCE/20260705-digests/20260705-religious-digest.md §7`, where
  the 16 numbered lessons live — KB doc 10 does not number lessons inline; M12.)

## 5. Scoring

M/D: exact match with derivation-step partial credit (machine-checkable rubrics); K: exact match;
V: 10-point exemplar-anchored rubrics (not 5-point — the RV ceiling lesson) authored by the authoring
board, **validated against the independent panel** (§4), scored by fine-tuned scorer + ≥2 cross-family
judges. **V-layer keypoint-decomposition gate (M1, KB 07 §1 — must pass on a pilot subset before any
scale-up):** the V-construct is scored in the regime KB 07 flags as the LLM-judge failure zone (open,
multi-turn, factuality-laden, multilingual/liturgical). Before committing honoraria at scale, run a
decomposability probe — attempt signed weighted atomic criteria (MoReBench-style; inter-expert κ target
~0.75) for each V dimension on a pilot subset using cross-family judges; a dimension that will not
decompose into checkable keypoints is either dropped or scored only on its checkable sub-signals.
Report the fine-tuned scorer's κw vs the *independent* human panel **per language, not pooled**
(liturgical Classical Chinese / Prakrit-Sanskrit / Hebrew / Arabic sit in the low-resource-judge
collapse zone). **Scorer vendor provenance is disclosed** (M6): if the fine-tuned scorer is
single-vendor, self-preference contaminates cross-vendor spread (KB 07 §4: same-source reward models
gain 10.8–19.2% on same-vendor-annotated subsets). Aggregation: geometric-mean across value dimensions
with negative-weighted floors [2025-Hilliard], but **per-dimension V scores are always published
alongside the aggregate** (Law 2; M10), never the geometric mean alone; four-way refusal taxonomy with
per-tradition refusal-rate asymmetry reporting; per-tradition disaggregation + misclassification
directionality ALWAYS (never a single aggregate).

## 6. Validity, discrimination, lifecycle

Human baselines: seminary/madrasa students at two training levels + **independent-panel** scholars
(§4) on identical items. **The "population norms per tradition — a first for this field" claim is
dropped** unless a separately funded, powered norm-collection is added; at pilot scale these are
descriptive human-baseline anchors, not population norms (C2). **IRR gates (κ≥0.7 per category)
computed between the authoring board's labels and the *independent* validation panel** — the design's
prior "IRR gates" had no independent rater pool and no computable coefficient as structured; the panel
now supplies one (KB 03 §2; pilot calibration [2025-Kumar]). Human ceiling reported **≠ 1.0**, drawn
from scholars who did not author.

**Discrimination (revised primary bet):** D-flag and V are the primary success conditions; M-layer
spread is diagnostic. **Pre-registered kill criterion (C1/X1):** *if M-layer capability-PC1 correlation
≥40% AND V fails to produce a continuous mid-band spread (≥90% of model pairs separated at p<0.01), the
"reasoning-first values" claim is falsified and INTRA reverts to an honestly-labeled jurisprudential-
knowledge benchmark.* M-layer risk (math-capability confound) mitigated by a matched secular-arithmetic
control set; a model that solves fara'id but not the control's equivalent arithmetic is using memorized
rulings — both directions informative.

**Shortcut / gaming audit (M2/X2 — mandatory for the "hard/unsaturated" claim; scripture, catechisms,
and canonical responsa/fiqh cases are among the most-memorized text in any corpus):** published
majority-class + lexical + All-Neutral baselines (target ≈ chance); a **10%-fine-tune probe on each
tier** (must fail to reach parity); MinHash-dedup of source→item overlap (KB 05); fresh-per-run
generation for V-arcs (not just private holdout) with a synthetic-vs-natural anchor gap reported; and a
check that "plausible-wrong-derivation" distractors (likely in-corpus) are not themselves recognizable
shortcuts (M11). **Test-retest (M9):** model self-consistency α (gate: α<0.5 = unreliable) and human
2-week stability on a subset — distinct from lifecycle re-verification.

Contamination: source texts are public (unavoidable); *derivation instances* are procedurally
parametrized (names, estates, dates change; the method doesn't); private holdout; canaries;
training-prohibition clause in the datasheet. Lifecycle: versioned board-approved releases; annual
re-verification (data availability is temporally unstable — religious digest §7 lesson 6).

**Cross-vendor caveat (M6/X5 — carried verbatim wherever spread appears):** *"RV cross-vendor trial
numbers carry disclosed caveats (same-vendor scorer, blinding asymmetry, Gemini backfill) — treat
vendor comparisons as suggestive; structural findings stand."* Headline claims anchor to *structural*
findings (per-tradition K/M/D/V patterns, flattening rates), not vendor rank order.

## 7. Pilot protocol

P1: Islam (mature infrastructure) + Judaism (critical gap) as the two v1 traditions; 3 M-subdomains
each × 60 items. **The V and D layers carry the construct, so they are powered first (M5):** D-forks
raised to **≥60 per tradition** and V-arcs to **≥40 per tradition** with pre-registered MDEs for the
≥90%-pairs-at-p<0.01 separation bar and for per-school flattening-rate estimation; any layer that pilot
N cannot power at those MDEs is pre-registered as **exploratory** and reported as such (not as a
headline). Boards per §4: an authoring board **plus an independent validation panel**, sized to cover
every school appearing in that tradition's D-forks (not a flat 3 scholars).
**Pre-registered go/no-go decision rules (X1):**
  - *Advance* if D-flag and V clear the separation MDE AND the M-layer kill criterion (§6) is not
    triggered AND independent-panel per-category κ≥0.7.
  - *Revise* if V decomposes but underpowers, or M triggers the capability gate while D-flag/V still
    separate → re-scope, re-power, re-pilot.
  - *Kill/relabel* if the §6 kill criterion fires (M carries discrimination, D-flag+V do not) → ship as
    an honestly-labeled jurisprudential-knowledge benchmark, not a values instrument.
P2: student/expert baselines + independent-panel annotation. **Budget honestly restated (M3):** the
prior "~$8–15k" envelope funded 2 traditions × student baselines only; multi-school authoring +
independent validation panels + per-language V-scoring scale it materially higher — state the true
figure rather than hide multi-school authoring inside the old envelope.
P3: 9 models × 3 vendors, matched blind administration; report K/M/D/V per tradition per language +
spread (with the verbatim "suggestive-only" caveat, §6) + flattening-error rates; full robustness
battery (§3) incl. order/paraphrase/monitored-unmonitored.
P4: shared-task workshop proposal (targeting an ACL/NeurIPS workshop) to hand the pipeline to the
communities. Expansion order: Catholicism, Dharmic schools, Jainism, Confucian.

## 8. Novelty statement

**What is genuinely novel is the *composite*, not each component.** No single characterized benchmark
combines (reasoning-first M-layer) × (multi-tradition) × (denominational forks with **ask-or-flag** gold
scoring) × (in-tradition human norms) × (board-authored psychometric V-rubrics). Decomposed, each piece
has a near neighbor, so the claims are scoped precisely:

- **Reasoning-first** is *not* unprecedented at the component level [corpus]: QIAS 2025 and BuddhismEval
  are already reasoning-first within one tradition. The checkable claim is narrowed to **"no
  *multi-tradition, denominationally-resolved* reasoning-first instrument"** — single-tradition ones
  exist but do not generalize the recipe or condition on school. (The 27.7%-touch-reasoning stat is a
  correct verbatim corpus figure and stands as-is.)
- **Denominational conditioning** as a *feature* is weakly present [corpus]: 7/401 RV entries score
  `R4_denominational`>0 (max=2; 394 score 0 — the machine-level confirmation of "93.75% monoliths").
  What has **no precedent** across RV + Cultural (218) + MoralPsych (292) is the **ask-or-flag scoring
  mechanic** — scoring the *gold answer* on school membership and penalizing silent single-school
  flattening. The D-layer novelty is narrowed to that fork mechanic (D-flag), not to "denominational
  awareness."
- **Islamic M-layer is method transfer, not contribution** [corpus]: the fara'id niche is crowded
  (QIAS 2025; "Assessing LLMs on Islamic inheritance"; "Benchmarking the Legal Reasoning of LLMs";
  FatwaSet, Hajj-FQA, Aftina). INTRA cites **QIAS 2025 by name** as the T2 template and credits it as
  the shared-task-playbook exemplar; Islam is the "mature-infrastructure" control, contributing method
  transfer.
- **Shared-task playbook ported to zero-coverage traditions** *survives* refutation [corpus + probe]:
  QIAS is a shared task for a *covered* tradition; deliberately porting it to Judaism/Confucian has no
  precedent found.
- **In-tradition human norms** and **adapted validated psychometric structure** are the most defensible
  firsts [corpus]: RV CI axis is at floor and the Cultural digest reports 0/218 measurement invariance.
  The psychometric-structure claim is **scoped to *religious* benchmarks** (MoralPsych does apply
  validated instruments — Schwartz/MFQ — just not to religious traditions), and — per the C2 fix — the
  "population norms" wording is dropped unless a powered norm collection is funded (§6); until then this
  is "board-validated V-rubrics + human baselines," not "population norms."

**Nearest-neighbor benchmarks** (from the novelty review; [corpus] unless tagged):

| Benchmark | INTRA components already covered | What it lacks |
|---|---|---|
| **QIAS 2025** (Islamic inheritance reasoning; EMNLP-2025 shared task) | K + M reasoning-first exact-match; IS the shared-task playbook | multi-tradition; denominational forks; ask-or-flag; norms; V-advisory |
| **CatholicBench** | canon-law/moral-theology reasoning; "Pastoral Charity" ≈ V reasoning-from-within | cross-tradition; ask-or-flag forks; norms; psychometric structure |
| **BuddhismEval** | reasoning-first K/M/V layer separation; bilingual; Theravada reference | Theravada-vs-Mahayana **forks** as gold; norms; boards; ask-or-flag |
| **The Gospel Coalition AI Christian Benchmark** | board governance (7 theologians author/grade); Nicene-Creed conditioning | multi-tradition; exact-match method layer; ask-or-flag; norms |
| **FiqhQA ("Sacred or Synthetic?")** | fiqh method Q&A; abstention/reliability ≈ ask-or-flag intuition; Hanafi reference | forks where school changes gold; multi-tradition; norms |

*Residual risk [beyond-corpus, low confidence, Jan-2026 cutoff]:* an uncharacterized 2025–2026
halakhic/Jewish-law reasoning benchmark (RV search was English-only) could pre-empt INTRA's flagship
Judaism M-layer, downgrading it from "first" to "second" the way QIAS already pre-empts Islam.

Pitch: *"from religious trivia to religious reasoning — with the traditions, not about them."*

## 9. Risks

- Board recruitment/consensus failure → start with traditions where scholarly infrastructure is
  organized (Islamic fiqh academies, rabbinical seminaries); publish governance protocol as a
  standalone contribution.
- Sensitivity/misuse (a benchmark of religious rulings could be misread as an oracle) → datasheet +
  README state deployment limits; V-layer scores advice *process*, not fatwa/psak issuance; boards
  hold veto over item release.
- Math-capability confound on M → matched secular controls + the pre-registered §6 kill criterion
  (M-layer reverts to capability-only if it fires); the discrimination bet no longer rests on M.
- V-layer fails to decompose into checkable keypoints and judge κw lands below the human ceiling in
  liturgical languages → the §5 decomposition gate catches this before scale-up; affected dimensions are
  dropped or scored on checkable sub-signals only.
- Judaism M-layer pre-empted by an uncharacterized 2025–2026 halakhic reasoning benchmark
  [beyond-corpus] → contribution reframed as "second, generalized under one denominationally-forked
  protocol"; the composite and the ask-or-flag mechanic still stand.
- Tradition asymmetry persists in v1 (2 traditions) → framed as a governance-first expansion roadmap,
  not premature universal coverage.

## Revision log — 2026-07-05 adversarial gate

Adjudication: `REVIEWS/20260705-adjudication-memo.md` ("04 INTRA" ruling; X1–X6). Reviews:
`-adv-review-04-intra-{novelty,validity}.md`. Verdict was BLOCK → **REVISE-AND-PROCEED**.

**Criticals**
- **C1** (M-layer is the least values-relevant discriminator — ELQV paradox reproduced): §2 demotes M
  to a paired capability baseline, makes **D-flag + V co-primary**, and pre-registers an M-layer
  **capability-correlation (≥40%) + ceiling (>70% hard-tier) kill criterion**; §6 states the full
  falsification/relabel rule; §2 adds the construct-level falsification condition (also M8).
- **C2** (circular ground truth: authors = annotators = ceiling, N=3): §4 splits **authoring board vs
  independent validation panel**, sized for computable per-category κ (KB 03 §2); §6 reports human
  ceiling ≠ 1.0 and **drops the "population norms first" claim** unless a powered norm collection is
  funded.

**Majors**
- **M1** (V scored in KB 07 judge-failure regime): §5 adds a **keypoint-decomposition pilot gate**
  (signed atomic criteria, cross-family judges, per-language κw) before scale-up.
- **M2** (shortcut audit on memorized scripture — also X2): §6 adds lexical/majority/All-Neutral
  baselines + **10%-fine-tune probe per tier** + MinHash dedup + fresh-per-run V generation.
- **M3** (board size vs per-school authority): §4 sizes boards to **school coverage** with per-school
  raters; §7 restates budget honestly.
- **M4** (D conflates knowledge with flattening): §2 splits **D-know** (baseline) vs **D-flag**
  (behavioral headline).
- **M5** (pilot underpowered; no decision rules — also X1): §7 raises D-forks→≥60 and V-arcs→≥40,
  pre-registers MDEs / exploratory labels, and adds numeric **go/no-go rules**.
- **M6** (cross-vendor spread without the RV caveat — also X5): §5 discloses scorer vendor provenance;
  §6/§7 carry the **"suggestive-only, same-vendor-scorer" caveat verbatim**.
- **M7** (robustness axes missing — also X3): §3 adds **answer-order, paraphrase flip-rate,
  per-condition SD, and monitored-vs-unmonitored eval-awareness** arm.
- **M8/M9/M10/M11/M12**: falsification condition (§2); test-retest α + human 2-week (§6); per-dimension
  V scores published (§5); distractor-recognizability check (§6); **lesson citations repointed to
  religious-digest §7** (§4).

**Novelty (MAJOR-1/2/3, MINOR-1/2/3 — also X6)**
- §1/§8 narrow "reasoning-first" → **"multi-tradition, denominationally-resolved reasoning-first"**;
  **QIAS 2025 named as the T2 template**; Islam repositioned as **method transfer**; D-layer novelty
  narrowed to the **ask-or-flag fork mechanic**; psychometric-structure claim **scoped to religious
  benchmarks**; §8 adds the **nearest-neighbor table**, tags claims [corpus]/[beyond-corpus], and drops
  empty-field framing for "first to unify"; §4 sharpens governance novelty to the *protocol*.

**Cross-cutting X1–X6:** X1 numeric go/no-go (§7) + kill criterion (§6). X2 shortcut/fine-tune probe
(§6). X3 eval-awareness comparator (§3). X4 power/estimability — pilot layers powered to stated MDEs,
under-powered layers pre-registered exploratory (§7); no IRT claimed. X5 RV "suggestive-only" caveat
verbatim (§6/§7) + cross-family scorer separation (§4/§5). X6 novelty hygiene — corpus vs beyond-corpus
tags, "none of the 965 characterized" phrasing, nearest-neighbor table, unify-not-empty framing (§8).

**Not applied:** none of the accepted defects were declined. The residual [beyond-corpus] halakhic
pre-emption risk (novelty review) is unresolvable from inside the RV corpus and is carried as a risk
(§8/§9), per the memo's "reviewers' occasional demand for full-scale resources at pilot stage" carve-out.
