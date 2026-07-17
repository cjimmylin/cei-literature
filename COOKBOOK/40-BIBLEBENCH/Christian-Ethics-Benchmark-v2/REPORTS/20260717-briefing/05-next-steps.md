# WALKWORTHY v2 — Owner Briefing, Report 5 of 6: Next Steps and Scale-Up Readiness

**Date:** 2026-07-17
**Status:** INTERNAL OWNER BRIEFING — decision-support only; presents open items, not rulings
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

> This report answers one question: *if the owner wants to scale WALKWORTHY v2 from a
> 5-SUT pilot to a many-SUT leaderboard run feeding a leaderboard paper and a
> benchmark-design paper, what stands between here and there?* It inventories open items
> and orders them into a readiness ladder. It rules on nothing. The owner has explicitly
> chosen not to close any pending hook this session; every hook below is presented as an
> open decision, and the §5 verdict is labeled as the drafting model's assessment for
> owner review, not a ruling.

---

## §1 The scale-up question, decomposed into four readiness axes

Scaling to a leaderboard is not one decision. It is four different kinds of readiness, and
they are not at the same level of maturity. The harness that runs the eval, the judges that
score it, the governance that lets the numbers be published, and the cost/ops envelope are
independent axes. Three of the four are close to green. One — the judges, i.e. measurement
validity — is not, and it is the one that determines whether a leaderboard would mean
anything. The subsections below take each axis on its own evidence.

### (a) INSTRUMENT readiness — mostly proven, three named defects

The harness itself is proven at pilot scale. The 5-SUT full-scope pilot ran **50/50 eval
runs to success** (10 designs × 5 SUTs), with zero 402s and zero provider failures, 563
scored samples per SUT (`20260716-pilot-report.md` §1). Parity with the v1 O4 manifest is
exact (344-item public parity, pre- and post-review conversion,
`20260715-inspect-fit-assessment.md`), and the `.eval` replay path persists every message
of every sample, including the 17-message design-02 ladders — the v1 PR-9 transcript-loss
class is eliminated by construction. The branch classifier routed **287/287 branched turns
with 0 heuristic fallbacks** on every SUT, so the ladder-routing machinery is auditable
rather than silently degrading. On the pure "does the machine run and produce persistent,
recomputable readings" question, the instrument is scale-ready.

Three instrument-level defects qualify that verdict, and none of them is an ops problem —
each is a measurement-content problem that persists no matter how many SUTs are added.

1. **Three unscorable design-07 items (WW-07-L02 / WW-07-I04 / WW-07-F02).** These items
   ship with a per-turn rubric anchor that is literally "(no keyed text)." Both
   independent referee arms confirmed the consequence: with no keyed norm to score
   against, the two shipped judges fall back on opposite priors and manufacture pure
   disagreement. Opus declared 48 of its 50 unscorables on exactly these three items;
   Sol declared all 87 of its unscorables on the same three
   (`20260716-opus-referee-results.md` Finding 4; `20260717-sol-referee-results.md`
   Finding 4). Two independent stronger-model references now agree these items cannot be
   scored as shipped. They are a mechanical disagreement generator independent of judge
   quality, and they need keyed text authored before design 07 is trustworthy.

2. **Design 07 is floor-saturated at the cheap tier.** Every one of the five pilot SUTs
   scored `arc_pass_rate` = **0.0000** (Wilson interval [0.000, 0.125], n=27, zero
   exclusions), and the judge-B re-score put it at 0.00–0.04 (`20260716-pilot-report.md`
   §3, §4). No cheap-tier SUT ever completes a keyed comfort-then-truth arc. With every
   ladder fully scored, this is a real floor, not an artifact of the exclusion cascade.
   The design is informative as a ceiling-room demonstration but **cannot discriminate
   among SUTs at this tier** — it needs either a stronger SUT roster (which a leaderboard
   run would naturally introduce) or a difficulty recalibration before it separates
   anything. Until then, an "07 leaderboard column" would show every entrant tied at zero.

3. **Design 02's state taxonomy is contested.** The four-way referee evidence found that a
   strong-model consensus reading of the 02 taxonomy exists that both shipped judges miss:
   Sol↔Opus agreement on the 02 disagreement stratum is **0.735 (κ 0.653)**, and both
   referees land on the *same* neither-state on 83/200 disagreement units (41.5%), while
   each referee agrees with each shipped judge at only 0.23–0.27
   (`20260717-sol-referee-results.md` Finding 1). The concession boundaries and the
   `full_compliance` threshold are read differently by the shipped judge pair than by two
   independent stronger references. Arm 2 revised arm 1's framing here: "gap = pure rubric
   ambiguity" is now too strong — the 02 gap is substantially *both-judges-diverge-from-
   consensus*, with residual genuine ambiguity on top.

### (b) JUDGE readiness — the owner's "is there a fixed judge?" question, answered honestly: NO

The owner's standing question — is there a fixed judge? — has to be answered plainly:
**not yet, not on designs 02 and 07.** Three things are unresolved, and one is settled.

First, **judge-A (gpt-4.1-nano) is doubly flagged.** Two independent stronger-model
references now mark it as the divergent instrument on design 07: on turns where the two
shipped judges disagree, both referees side with judge-B roughly 3:1 over judge-A (Opus
0.594 vs 0.217; Sol 0.605 vs 0.138), rising to ~0.76 with the defective no-keyed-text items
removed, and both referees jointly back judge-B on 225/392 contested turns vs judge-A on 48,
backing opposite judges on only 13 (`20260716-opus-referee-results.md` Finding 1;
`20260717-sol-referee-results.md` Finding 2). Guardrail on reading this evidence: "closer
to Opus/Sol" is reference-model concordance, not ground truth — the referees are stronger
models, not oracles, and two referees agreeing may share correlated error; the referee data
lives outside the benchmark instrument and changes no judge pins without an explicit owner
ruling (see 03-meta-judging.md). Independently, the F3 cross-family classifier
run found nano is the classifier outlier: two alternative families (mistral-small-3.2,
gemini-2.5-flash-lite) agree with each other at 0.902 but only 0.721 / 0.685 with the pilot
nano route, and **on 24.4% of branch turns both alternatives agree against nano**
(`20260716-f3-crossfamily-classifier-results.md`). The judge/classifier distinction is real
(F5 certified nano as a conclusion-neutral *judge*; F3 speaks to nano as a *classifier*),
but the owner-facing summary is the same: the incumbent judge-A instrument is under a
question mark on both 02 and 07.

Second, **the 07-judge choice is an open owner hook.** Both referee arms list the same
candidate actions for design 07 — replace judge-A, re-weight it, or add a third judge — and
both explicitly leave the choice as an owner ruling, taken by nobody
(`20260716-opus-referee-results.md` hook 2; `20260717-sol-referee-results.md` hook 2).

Third, **the design-02 path has two open pieces.** The judge-pair-versus-taxonomy question
is an open hook: arm 2 says the options now include (a) taxonomy revision and (b) treating
the shipped judge pair as the weak link on 02 (e.g. a stronger 02 judge in v-next), and
choosing between them is an owner ruling (`20260717-sol-referee-results.md` hook 3).
Separately, the v-next design-02 classifier re-pin **is ruled but not implemented**: the
owner ruled that v-next 02 runs switch to a cross-family-corroborated classifier
(mistral-small-3.2 or gemini-2.5-flash-lite, not nano), but that decision is memo-only, with
no code and no re-runs (`20260716-design02-classifier-pin-decision.md`). It creates a new
instrument version under C6 when implemented; until then, no scale-up 02 run can use the
re-pinned instrument.

What is settled: **G5 neutrality certification is green.** All three candidate judges
(gpt-4.1-nano, llama-3.3-70b-instruct, gpt-4.1-mini) are G5-certified on designs 06 and 09,
each after at most one cleared re-elicitation (`20260716-f5-certification-results.md`). That
axis needs nothing further before scale-up.

One structural consequence for every scale-up run: the **2-judge rule (R4)** is binding.
Every design flipped its naive point-estimate ordering under the judge-B re-score in the
pilot (`20260716-pilot-report.md` §2), so no single-judge ranking survives. Any scale-up run
must budget judge-B as a first-class component, not an optional audit — this is a cost line
(see (d)), not a nice-to-have.

### (c) GOVERNANCE readiness — the framework exists; two structural gates remain

The pre-registration framework is ratified. F11 is RATIFIED
(`20260716-prereg-comparisons-RATIFIED.md`): the comparison families (C1 = 30 pairwise on
the 04/05/10 sub-panel, C2 = 70 pairwise on the R7-caveated designs), the blunt-Bonferroni
multiplicity handling (α = 0.05 family-wise, m frozen by formula), the 2-judge precondition,
the certified-judge requirement for 06/09, and the pinned-classifier requirement (C6) are all
in force. This is the machinery a leaderboard's comparative claims would run through, and it
exists.

Two structural gates remain, and they are the reason "the framework is ratified" does not
equal "a leaderboard can be published."

- **C9 first-use rule.** Because the ratified comparison list post-dates the pilot data, the
  same comparisons computed on the *existing pilot logs* are reportable only as "post-hoc on
  pilot data — hypothesis-generating" (`20260716-prereg-comparisons-RATIFIED.md` §3). A
  reportable leaderboard therefore requires **new data — a fresh SUT run.** The pilot is,
  forever, hypothesis-generating; no amount of reanalysis promotes it. This is the single
  hardest governance constraint on a leaderboard paper: it cannot be built from what is
  already on disk.

- **v2 is PARALLEL, not canonical.** By owner ruling, Christian-Ethics-Benchmark-v2 is a
  parallel harness alongside the canonical v1 custom harness, indefinitely; v1 remains the
  canonical execution path for release-grade evidence, and the recommendation to adopt v2 as
  canonical was considered and explicitly not adopted
  (`20260716-owner-ruling-v2-parallel.md`). A leaderboard paper sourced from v2 would
  therefore need *either* a canonical-readiness ruling (which the owner has not made) *or*
  explicit parallel-track framing ("this leaderboard is a parallel-harness reading, offered
  alongside v1"). Which of those two the paper takes is an owner decision.

Three lesser governance items are also open. The **s8 session has not been run**: the
F-ledger close-out capstone report and the canonical-readiness memo (checking the fit-memo §4
preconditions) are scoped as the s8 agenda but not yet produced
(`20260716-boot-prompt-s8-ledgerclose-canonical.md`). The **R11 order-sensitivity caveat is
standing** — F7 gave direct evidence that design-07 per-turn judging is order-sensitive, and
the ruling on whether to retain, sharpen, or lift the PROVISIONAL flag is an open Task-0 item
in the s8 boot prompt. And in the F-ledger, **F6 is dormant** (DSP judge-prompt credit rule,
design-memo-first, coupled to the un-ruled F4-C) and **F10 is unscoped** (an optional k=3 seed
decode-stability probe never specified in detail) (`REVIEWS/20260716-adjudication-benchmark-
critique.md` FIX-later ledger).

### (d) COST/OPS readiness — green

Cost and operations are the least concerning axis. The pilot spent **$2.73 exact** (SUT +
judge-A + 02/07 classifier, live OpenRouter prices) for 5 SUTs, plus an **estimated ≈ $0.90**
for the judge-B re-score over the same prompt volume, for ≈ $3.63 total against a $7.90
authorized envelope — the cost model was ≈2× conservative
(`20260716-pilot-report.md` §1, §7). Zero provider failures, zero 402s.

Deriving per-SUT unit costs from the pilot:

- SUT + judge-A + classifier: $2.73 / 5 SUTs ≈ **$0.55 / SUT**
- judge-B re-score: $0.90 / 5 SUTs ≈ **$0.18 / SUT**
- Full two-judge cost: ≈ **$0.73 / SUT** over the 563-sample-per-SUT full scope

[UNVERIFIED — arithmetic extrapolation from the pilot's per-SUT unit cost; not a measured
figure. A larger, more expensive SUT roster and the v-next 02 classifier re-pin (a different-
priced model) would move these numbers.]

| Roster size | SUT + judge-A + classifier (~$0.55/SUT) | + judge-B (~$0.18/SUT) | Full two-judge (~$0.73/SUT) |
|---|---|---|---|
| 20 SUTs | ~$11.0 | ~$3.6 | ~$14.6 |
| 30 SUTs | ~$16.5 | ~$5.4 | ~$21.9 |
| 50 SUTs | ~$27.5 | ~$9.0 | ~$36.5 |

Wall-clock from the pilot: half-1 ≈ 24 min (5 SUTs parallel at `--max-connections 4`), half-2
≈ 50 min (deepseek's ladders are the long pole), with judge-B re-scores ≈ 25–45 min each run
in parallel (`20260716-pilot-report.md` §1). At `--max-connections 4` the wall-clock roughly
halves; a many-SUT run parallelizes across SUTs, so the wall-clock scales with concurrency
rather than roster size. On cost and ops, a 20–50-SUT run is well within a small, predictable
envelope. This axis does not gate scale-up.

---

## §2 Gap list → readiness ladder

The table orders the open gaps as the recommended sequence: close the governance capstone and
the hooks first (cheap, owner-facing, unblock everything downstream), then the mechanical
instrument work those rulings authorize, then the one thing C9 makes unavoidable — a fresh
run — and only then the papers. "Who decides" separates owner hooks (a ruling is required)
from mechanical work (execution against a settled spec). Effort is rough order-of-magnitude.

| # | Gap | Evidence | Blocking for | Who decides | Rough effort |
|---|---|---|---|---|---|
| 1 | s8 not run: F-ledger close-out + canonical-readiness memo | `20260716-boot-prompt-s8-ledgerclose-canonical.md` | leaderboard paper, benchmark-design paper | mechanical (memos) → then owner reads | 1 session, free |
| 2 | R11 flag ruling (retain / sharpen / lift design-07 order-sensitivity caveat) | s8 boot Task 0.1; F7 evidence | leaderboard paper, benchmark-design paper | owner hook | 1 ruling |
| 3 | Canonical-vs-parallel framing for a v2 leaderboard | `20260716-owner-ruling-v2-parallel.md`; fit memo §4 | leaderboard paper | owner hook (after memo #1) | 1 ruling |
| 4 | Design-07 judge choice (replace / re-weight / third judge) | Opus hook 2; Sol hook 2 | leaderboard run (07 column), leaderboard paper | owner hook | 1 ruling |
| 5 | Design-02 judge-pair vs taxonomy (revise taxonomy / stronger 02 judge) | Sol hook 3; Opus hook 3 | leaderboard run (02 column), leaderboard paper | owner hook | 1 ruling |
| 6 | Author keyed text for WW-07-L02 / I04 / F02 (unscorable defect items) | Opus/Sol Finding 4 (dual-confirmed) | leaderboard run (07 trustworthy), design paper | mechanical (rubric authoring) after #4 | rubric authoring pass |
| 7 | Design-07 floor-saturation: stronger roster or difficulty recalibration | pilot §3/§4 (arc_pass 0.000) | leaderboard run (07 discriminates) | mechanical + roster choice | recalibration / roster |
| 8 | Implement design-02 classifier re-pin (ruled, not built) | `20260716-design02-classifier-pin-decision.md` | leaderboard run (02 column) | mechanical after #5 | code + spec declaration |
| 9 | Fresh C9-clean multi-SUT run (declare m by formula before first use) | RATIFIED §3 (C9) | leaderboard run, leaderboard paper | mechanical after #4–8 + spend GO | paid run (~§1(d) table) |
| 10 | Leaderboard paper drafting | gated on #1–9 | leaderboard paper | authoring after run | manuscript |
| — | F6 (dormant), F10 (unscoped) | critique FIX-later ledger | neither paper (optional) | owner scopes if wanted | design memo / probe spec |

The critical dependency chain is: **#1 (free capstone) → #2–5 (owner hooks) → #6–8 (mechanical
instrument work the hooks authorize) → #9 (the fresh run C9 requires) → #10 (papers).** Items
#4 and #5 gate the instrument work under them, because you do not author keyed text or re-pin a
classifier until the owner has ruled *which* judge/taxonomy the v-next instrument uses. Item #9
is the hinge: it is the first paid item on this list, it needs its own spend memo and explicit
GO (no pre-authorized paid work exists), and it must declare its multiplicity m by the frozen
formula *before* the run's first use (RATIFIED §2/§3).

---

## §3 What is already publishable regardless

One of the two papers is not gated on any of the above.

**The benchmark-design paper needs no new runs.** Its content is the instrument design, the
methods, the pilot-as-pilot, and — the genuinely novel methodological contribution — the
judge-referee meta-audit. All of that already exists on disk. The design (10 designs, the
corpus-distinctive 04/05/10 sub-panel, the ladder solvers, the refusal taxonomy, the CSR
comparator) is documented; the methods (Inspect-AI port, 2-judge re-score, pinned classifier,
G5 certification) are documented; the pilot is a legitimate pilot exactly as run and reported;
and the **two-arm blind referee protocol** — 942 units, frozen manifest, two independent
stronger-model references (Opus via Claude Code, Sol via codex exec), $0 API spend, referee-
referee agreement 0.735–0.920 as a new class of instrument evidence
(`20260716-opus-referee-results.md`, `20260717-sol-referee-results.md`) — is a
methods-innovation story in its own right. That paper can be drafted now; it reports the
pilot honestly as descriptive/hypothesis-generating and does not need C9-clean data, because it
makes no leaderboard claim. The one dependency worth clearing first is the s8 F-ledger
close-out (gap #1), which gives the design paper its "what the adjudication cycle bought"
spine.

**The leaderboard paper is gated on §2.** It makes SUT-vs-SUT comparative claims, which
require C9-clean fresh data (#9), which requires the judge/taxonomy hooks resolved (#4–5) and
the instrument defects fixed (#6–8), plus a framing ruling on parallel-vs-canonical (#3).
Nothing about the leaderboard paper can be sourced from the pilot logs.

---

## §4 Pending inventory — nothing else is hiding

A complete enumeration of open items, so the owner can see the whole board:

**Five owner decision hooks (arm-2 phrasing, which supersedes arm-1 where noted):**

1. **v-next rubric priority (dual-referee-confirmed):** author keyed text for WW-07-L02 /
   WW-07-I04 / WW-07-F02 (`20260717-sol-referee-results.md` hook 1).
2. **Design-07 judge-A (strengthened):** two independent references mark gpt-4.1-nano as the
   divergent instrument on 07 — replace / re-weight / third judge (hook 2).
3. **Design-02 (revised framing):** a strong-model consensus reading exists; options are (a)
   taxonomy revision or (b) treating the shipped judge pair as the weak link (stronger 02
   judge in v-next) (hook 3).
4. **Design-06 `principles` category (downgraded):** arm 1's strict-reading question is now a
   referee-*disagreement* question — Opus's strict `principles` reading is Opus-specific, not
   a strong-model consensus (Sol−Opus on `principles` ≈ +0.40); optional third reference or
   human ruling only if this category ever matters downstream (hook 4).
5. **No judge pins changed; nothing in the referee arms enters benchmark reports or
   comparative claims** — R1/R3/C9 + RATIFIED F11 untouched (hook 5).

**s8 agenda items** (`20260716-boot-prompt-s8-ledgerclose-canonical.md`): the F-ledger
close-out report (Task 1, free), the canonical-readiness check against fit-memo §4
preconditions (Task 2, free), the R11 flag ruling (Task 0.1, owner), v-next package scoping
(Task 0.2, owner), and the canonical-readiness ruling (Task 0.3, owner, after the memo).

**F-ledger dormant/open items:** F6 (DSP judge-prompt credit rule, dormant, design-memo-first,
coupled to un-ruled F4-C) and F10 (optional k=3 seed decode-stability probe on design 10,
never specified in detail) (`REVIEWS/20260716-adjudication-benchmark-critique.md`).

**R11 order-sensitivity caveat:** standing PROVISIONAL flag on design-07 per-turn judging;
ruling pending (s8 Task 0.1).

**Design-02 classifier re-pin:** ruled for v-next, implementation not started — memo-only, no
code, no re-runs (`20260716-design02-classifier-pin-decision.md`).

**Holdout bank — unused so far.** A separate holdout of **158 runnable items** exists
(`20260715-conversion-parity-report.md`: public 344 runnable / holdout 158 runnable), loader-
guarded and gitignored, never entered into any prompt or report. It has not been touched by any
run to date (the pilot §7 confirms "Holdout untouched"). It exists for a future
contamination-controlled wave — a distinct future option, noted here only so the owner knows it
is available; its content is never quoted.

That is the entire open board. There is no hidden pending item outside this list.

---

## §5 Bottom-line readiness verdict

**This section is the drafting model's assessment for owner review. It is not a ruling, and
it rules on none of the §4 hooks.**

Harness, ops, and certification are scale-ready. The instrument runs cleanly at pilot scale,
the cost envelope for a 20–50-SUT run is small and predictable, and all three candidate judges
are G5-certified. If the only question were "can the machine produce numbers for 50 SUTs
without falling over," the answer would be yes.

**Measurement validity is not yet scale-ready.** A leaderboard is a measurement claim, and
three things currently prevent that claim from being defensible: (i) the judge identity on
designs 02 and 07 is unresolved — judge-A is dual-referee-flagged as the divergent instrument
on 07 and is the cross-family classifier outlier on 02, and the owner has not ruled how to
respond; (ii) three design-07 items are dual-referee-confirmed unscorable as shipped, and a
fourth issue is that design-07 is floor-saturated at the cheap tier so it discriminates nothing
until stronger SUTs or recalibrated difficulty arrive; and (iii) C9 makes the existing pilot
data forever hypothesis-generating, so a leaderboard *must* come from a fresh run regardless of
how the instrument questions land.

**Minimal critical path — the fewest actions that unlock a defensible leaderboard run:**

1. Run s8: ship the F-ledger close-out and the canonical-readiness memo (free; also gives the
   design paper its spine).
2. Rule the three run-blocking hooks: the design-07 judge choice, the design-02 judge-pair-vs-
   taxonomy choice, and the parallel-vs-canonical framing for the leaderboard.
3. Do the mechanical instrument work those rulings authorize: author keyed text for the three
   unscorable 07 items, implement the design-02 classifier re-pin, and settle the 07 roster/
   difficulty question (a stronger SUT roster is the natural fix and a leaderboard run supplies
   one).
4. Declare m by the frozen C9 formula, then run one fresh multi-SUT eval with both judges
   budgeted (a spend memo + explicit GO; ≈ §1(d) table cost).
5. Draft the leaderboard paper from that fresh run; the benchmark-design paper can proceed in
   parallel and needs none of steps 2–4.

The single highest-leverage move is step 2: the three run-blocking hooks are cheap for the
owner to rule and unblock everything mechanical and paid downstream. Nothing paid should fire
until they are ruled and the fresh-run spend memo has an explicit GO.

---

## Sources

- `20260716-pilot-report.md` — 5-SUT full-scope pilot (ops §1, judge-swap §2, per-design cells
  §3, design-07 anchors §4, diagnostics §6, receipts/spend §7).
- `20260716-boot-prompt-s8-ledgerclose-canonical.md` — pending s8 agenda (F-ledger close-out,
  canonical-readiness memo, R11 ruling, v-next scoping).
- `20260715-inspect-fit-assessment.md` — fit verdict; §4 canonical-readiness preconditions;
  §5 carried open items.
- `20260716-opus-referee-results.md` — JR arm 1 (Opus); 5 owner decision hooks; Findings 1–5.
- `20260717-sol-referee-results.md` — JR arm 2 (Sol); supersedes arm-1 hook phrasing where
  noted; design-02 revised, design-07 corroborated, defect items confirmed.
- `20260716-prereg-comparisons-RATIFIED.md` — F11 RATIFIED; C1/C2 families, C6 pinned
  classifier, C9 first-use, R4 2-judge rule, multiplicity handling.
- `20260716-design02-classifier-pin-decision.md` — v-next 02 classifier re-pin ruled,
  unimplemented.
- `REVIEWS/20260716-adjudication-benchmark-critique.md` — F-ledger (F6 dormant, F10 unscoped),
  R-rules, MUST-FIX/FIX-later classification.
- `20260716-owner-ruling-v2-parallel.md` — v2 PARALLEL, v1 canonical.
- `20260716-f3-crossfamily-classifier-results.md` — nano classifier outlier; 24.4% 2v1-vs-nano;
  0.902 alt-alt agreement.
- `20260716-f5-certification-results.md` — all three judges G5-certified on 06/09.
- `20260715-conversion-parity-report.md` — holdout = 158 runnable items (parity table).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
