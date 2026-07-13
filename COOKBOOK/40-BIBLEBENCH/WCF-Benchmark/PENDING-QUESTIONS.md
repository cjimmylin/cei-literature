# WCF-Bench Pending Questions

## OPEN 2026-07-13 — PPP-1 second-cycle interruption-custody choice

- **Question:** The one allowed general quality review found that `KeyboardInterrupt`
  during a paid attempt can bypass raw-evidence/checkpoint persistence and permit an
  exact-identity resume to repeat a chargeable call. Under the binding second-cycle stop,
  should Codex **fix**, **disclose-and-run**, **narrow the claim**, or **defer**?
- **Why it blocks:** The PPP-1 runner passed specification re-review after its first P1
  fix cycle, but the later quality review reproduced a zero-byte raw ledger and absent
  checkpoint when an interrupt landed inside the call. Starting the paid run without an
  owner choice would violate `20260713-wcf-paper-first-execution-amendment.md`'s explicit
  second-cycle rule. Paid inference has not started, so the one-run authority remains
  unconsumed.
- **Evidence:** runner commits `b23cf4bf9` and `a914f5d4`; specification re-review PASS;
  quality-review finding at `04-HARNESS/ppp1_run.py` around the composed call wrapper and
  terminal exception path. The focused suite is 24 green and the full suite was 724 green,
  but neither result closes the reproduced interruption custody gap.
- **Suggested default:** **FIX.** Keep the exact authorized roster, caps, scope, prompts,
  and one-run authority unchanged. Make only the PPP-1 call wrapper's reserve → attempt →
  accounting capture → raw fsync path interruption-safe; persist a terminal PARTIAL
  checkpoint on interruption; add one regression test; re-review only this named blocker;
  then execute once and build the paper packet. Do not reopen general review.

## RESOLVED 2026-07-13 — PPP-1 exact cap exceeds the ratified $5 ceiling

- **Disposition:** Jimmy selected judge `max_tokens=512`, preserved the exact 226-item ×
  three-SUT × sole-Gemini scope, authorized the minimal strict-cap runner seam, and
  authorized one paid PPP-1 execution under a strict `$23.56` maximum-retry NTE. Record:
  `20260713n-jimmy-ppp1-paid-authorization-record.md`. The authorization is not yet
  consumed because no paid attempt has started.

- **Question:** Should PPP-1 preserve its exact 226-item × three-SUT × single-Gemini
  scope by ratifying one of the frozen executable completion branches and its distinct
  maximum-retry NTE cap below, or should the scope/roster/judge be amended to retain a
  `$5.00` ceiling?
- **Why it blocks:** The authorized zero-paid preflight found a `$11.5698587676`
  conservative forecast and `$14.47` minimum 80%-safe cap at the reviewed 2,048-token
  ceilings. Even the non-executable zero-completion price floor is `$5.2479232028`
  (minimum cap `$6.56`), so the currently ratified exact scope cannot fit `$5.00` under
  any token-cap branch. Paid inference remains unauthorized.
- **Frozen executable choices:** each row is `logical no-retry forecast / planning cap;
  maximum-retry forecast / strict NTE cap`:
  - judge `max_tokens=2048`: `$11.5698587676 / $14.47`; `$29.9010952848 / $37.38`;
  - judge `max_tokens=1024`: `$8.8972187676 / $11.13`; `$22.5282952848 / $28.17`;
  - judge `max_tokens=512`: `$7.5608987676 / $9.46`; `$18.8418952848 / $23.56`;
  - judge `max_tokens=256`: `$6.8927387676 / $8.62`; `$16.9986952848 / $21.25`.
  In every executable row, SUT `max_tokens` remains 2,048. The 256-token row is cheapest
  but has the greatest structured-verdict truncation risk. A lower logical planning cap
  can stop early during a retry storm; the maximum-retry cap preserves the registered
  retry/error-survival path without implying that amount will be spent.
- **Evidence:** `07-PILOTS/20260713-ppp1-zero-paid-preflight/` plus its append-only
  supersession at `07-PILOTS/20260713-ppp1-zero-paid-preflight-retry-correction/` and
  final branch interpretation at
  `07-PILOTS/20260713-ppp1-zero-paid-preflight-branch-addendum/`. The
  original logical forecast remains valid; the correction supersedes its blanket 3,444
  retry-reserved attempts with the production-seam maximum of 3,624 and supplies the
  maximum-retry forecast/cap. The
  2026-07-13T17:23:54Z catalog snapshot resolves the exact four slugs and current prices;
  the contextual shared-key balance was `$62.97400935900009`, so none of the listed
  branches needs a top-up.
- **Suggested default:** Preserve the paper-facing 226×3 scope and ratify the balanced
  512-token judge branch with an expected `$7.5608987676` no-retry forecast and strict
  `$23.56` maximum-retry NTE cap, together with explicit authority
  for only the minimal offline single-judge runner seam and one paid PPP-1 execution.
  Keep the required **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**
  label, stop after the paper packet, and leave full T4 unchanged. If retaining `$5.00`
  is more important than preserving the ratified scope, Jimmy must explicitly amend the
  scope/roster/judge before any further controller work or paid call.

## OPEN 2026-07-13 — T4 cap choice after the zero-paid R40.1 preflight

- **Question:** Should the later confirmatory T4 be ratified at the full-run minimum cap
  of `$348.49`, which exceeds R59.5's `$300` planning ceiling, or should the registered
  truncation ladder govern under the existing ceiling?
- **Why it blocks:** The frozen reservation-safe forecast is `$278.7886467416001`; the
  80%-safe cap is therefore `$348.49`. The first cumulative branch that fits within the
  `$300` ceiling is `drop_p6 + drop_p3` at `$220.02401675360005` forecast and `$275.04`
  minimum cap. The five-cheapest base shard is separately `$63.23420081759999` forecast,
  `$79.05` minimum cap, and needs a `$16.04` top-up against the metadata snapshot's
  `$63.01088785899992` remaining balance. No paid authority follows from this preflight.
- **Evidence:** `07-PILOTS/20260713-t4-zero-paid-preflight/` — especially
  `t4-run-manifest.json`, `t4-cost-plan.csv`, and `t4-preflight-report.md`.
- **Suggested default:** Keep every T4 paid call paused and preserve the frozen manifest.
  Complete the owner-ratified PPP-1 paper-preview sequence first. When confirmatory T4
  returns to the critical path, either Jimmy explicitly raises the planning ceiling and
  approves the `$348.49` cap, or he keeps `$300` and ratifies the first within-ceiling
  registered branch (`drop_p6 + drop_p3`, cap `$275.04`). The final EPISODE-halving rung
  remains unavailable without its separate base-cell-conflict ruling.

## RESOLVED 2026-07-13 — T3 EPISODE 88-cell authorization, execution, and correction

- **Authorization record:** `20260713d-jimmy-t3-authorization-record.md`.
- **Scope:** T3 only — 22 EPISODE items × the standing four SUTs = 88 cells, scored by
  the manifest-of-record Gemini + Grok settled-core panel under R55.1–R55.3.
- **Budget:** strict `$10.00` NTE; expected actual `$1–$2.50`.
- **Execution:** the offline TDD runner and bounded reviews landed in commits
  `aa00c7009` through `fd8d6a69c`; the R40.1 pre-flight passed, and the one authorized
  checkpointable run completed all 88 cells. Its immutable original report records 88
  scored cells. An independent artifact audit then found one incomplete Gemini verdict
  that the checkpoint had treated as scored; no paid rerun or model debugging followed.
- **Controlling descriptive correction:**
  `07-PILOTS/20260713-t3-episode-offline-correction/` reclassifies that one cell offline.
  Final descriptive status is 87 scored + 1 error-recorded, with 80 graded, 7 wholly
  ungraded, agreement 36, disagreement 44, and graded mean 0.50375. The label remains
  **DESCRIPTIVE/PRE-GATE**.
- **Cost:** `$0.4393786622` response-attributed under the cap; the `$2.439582089`
  shared-key delta is contextual/contaminated and is not attributed to T3.
- **Effect:** T3 is complete and its task-specific paid authorization is consumed. T4
  and every other paid scope remain separately unauthorized. T4 still requires Jimmy's
  written task-specific roster, budget, and cap approval; G6 recruitment/co-labeling and
  R67.4 gate adjudication remain Jimmy-owned. No model substitution, panel/manifest
  change, ladder reopening, shadow-production use, G6 work, bank edit, ruling, or
  R-number is implied.

## Binding dispositions received 2026-07-12 — R47–R53

- **R47–R49:** The zero-OPEN result was a quoted-evidence willingness-parser artifact.
  Codex was directed to fix the parser, derive a corrected manifest from immutable Task-4
  evidence, and re-parse the persisted MVP OPEN verdicts offline.
- **R50:** Tasks 1–4 are ratified; the paid-call pause remains in force.
- **R51:** The EPISODE registry mechanism is ratified; R54–R56 subsequently completed the
  item-level review and directed mechanical application. No live run is authorized.
- **R52:** Task 6 is formally DEFERRED under the citation-gated contract. Alignment note:
  `20260712-task6-r52-alignment-amendment.md`.
- **R53:** MVP-testable uses the corrected single-family OPEN manifest, excludes EPISODE
  pending registry approval, and retains the PROOF artifact disclosure.

**Current execution status:** T1, T2, and T3 are complete and Jimmy ratified the verified R57
checklist on 2026-07-12; durable record:
`20260712l-jimmy-r57-ratification-record.md`. T2.5 is checked and WCF-Bench is MVP
TESTABLE under R53/R58.1, retaining the R34.4 single-family OPEN label and all existing
DESCRIPTIVE/PRE-GATE and PROOF disclosures. Paper P1 citation verification is also
complete. T3 ran once under the exact authorization above and is now closed; paid T4
calls remain separately gated and unauthorized. Jimmy separately
authorized the exact, shadow-only judge bakeoff recorded in
`20260712n-shadow-judge-bakeoff-design.md`, with a $1.00 NTE cap; it does not reopen the
candidate ladder, change the manifest, or authorize any T3/T4 call. Written-spec review
preceded implementation. The one authorized run is now immutable and labeled `PARTIAL`:
all 96 probe repetitions and 56 shadow-verdict attempts were persisted, but reconciliation
was `UNRECONCILED` because the runner's internal attributed total was $0.69776393843 while
key-wide usage increased by $5.426614419 during the pre/post interval. The reconciliation
question is **RESOLVED** by Jimmy's 2026-07-13 ratification in
`20260713a-jimmy-shadow-reconciliation-ratification-record.md`. The later exact T3
authorization is recorded in `20260713d-jimmy-t3-authorization-record.md`; it was consumed
by the single completed T3 run under a `$10.00` NTE cap. T4 and every other paid scope
remain unauthorized.

## Jimmy authorization received 2026-07-12 — shadow judge bakeoff

- **Scope:** Shadow evidence only. T4, the manifest of record, and the R47.4 closed
  candidate ladder remain unchanged.
- **Paid models:** exactly `z-ai/glm-5.2` and `deepseek/deepseek-v4-pro`.
- **Offline comparators:** reuse persisted `x-ai/grok-4.20` and
  `google/gemini-2.5-flash` evidence; no new Grok or Gemini calls.
- **Budget:** strict $1.00 not-to-exceed cap. This authorization does not extend to T3,
  T4, another model, a substitute slug, or a production-panel change.
- **Design of record:** `20260712n-shadow-judge-bakeoff-design.md`, approved by Jimmy and
  amended only by the evidence-count correction below.
- **Written-spec review:** Jimmy approved the design on 2026-07-12, then approved the
  evidence-count amendment in `20260712p-shadow-judge-bakeoff-design-amendment.md`:
  8 OPEN + 8 coherence + all 6 compatible disclosure + all 6 compatible settled-core
  units = 56 new shadow verdicts. No incumbent reruns; $1 cap unchanged.
- **Implementation plan:** `20260712q-shadow-judge-bakeoff-implementation-plan.md`.

## RESOLVED 2026-07-13 — shadow-run key reconciliation exceeds the authorization ceiling

- **Disposition:** Jimmy identified concurrent use of the shared OpenRouter account during
  the measurement interval, so the `$5.426614419` key-wide delta is contaminated and is
  not a clean run-specific spend measure. Jimmy accepted the response-attributed
  `$0.69776393843` as the shadow run's attributable cost within the `$1.00` cap. Binding
  record: `20260713a-jimmy-shadow-reconciliation-ratification-record.md`.
- **Offline completion:** Mechanical application of the pre-registered Pareto contract
  makes GLM **`PARETO-PREFERRED SHADOW CANDIDATE`** **SHADOW ONLY**. Companion record:
  `20260713b-codex-shadow-pareto-completion.md`.
- **Effect:** No production, panel, manifest, candidate-ladder, T3, T4, benchmark-score,
  paper, release, or paid-authorization effect. No OPEN reconciliation escalation remains.

- **Question:** How should the completed shadow evidence be labeled and used after the
  one authorized run attributed $0.69776393843 internally but observed a $5.426614419
  key-wide usage delta over the same interval, causing the immutable run to finalize
  `PARTIAL / UNRECONCILED`?
- **Why it blocks:** The full designed evidence exists (96/96 probe repetitions, 56/56
  verdict/error attempts, 28 selected units at 8/8/6/6), but the key-wide delta exceeded
  the $1.00 NTE authorization and differs materially from response-level accounting. The
  run therefore emitted no Pareto candidate and cannot support a production-panel action.
- **Evidence:**
  `07-PILOTS/20260712-shadow-judge-bakeoff/shadow-run-metadata.json` and
  `07-PILOTS/20260712-shadow-judge-bakeoff/20260712-shadow-judge-bakeoff-report.md`.
  The report is explicitly `SHADOW / NOT A QUALIFICATION MANIFEST`; it records GLM as
  shadow-eligible on all four surfaces, DeepSeek as shadow-eligible on coherence,
  disclosure, and settled-core but not OPEN, and no Pareto name.
- **Suggested default:** Freeze all further paid calls; preserve the run as immutable
  descriptive shadow evidence labeled `PARTIAL / UNRECONCILED`; do not attribute the
  unexplained key delta, name a winner, change the panel/manifest/ladder/T4 plan, or reuse
  this authorization unless Jimmy rules in writing.
- **Execution status:** One live invocation only; no rerun or resume. Internal attributed
  costs were $0.31201990142 for GLM and $0.38574403701 for DeepSeek ($0.69776393843 total).
  Key usage moved from $1415.943795768 to $1421.370410187 (delta $5.426614419), with
  $78.629589813 limit remaining after the interval. No new Gemini/Grok calls occurred.
- **Provisional packet:**
  `20260712u-codex-shadow-reconciliation-provisional-packet.md`. At issuance, status was
  **OPEN pending Jimmy**; the packet assigns no R-number and records no ratification. It is
  retained as pre-ratification provenance and was superseded by the binding disposition
  cited above.

## Rulings received 2026-07-11

1. **Task 4:** Keep the new manifest and close the candidate ladder.
2. **Task 5:** Codex may draft the 22-item EPISODE registry for human review. Drafting is
   authorized; approval and activation are not implied.
3. **Tasks 5–6:** Pause all paid calls and continue offline only.
4. **Task 6:** Use the current citation-gated `judge_score_anchor_use` contract as-is.

**Execution status:** Questions 1–3 are resolved through the R47–R57 work order and
Jimmy's R57 ratification. Question 4's scorer behavior is resolved, but its qualified
manifest surface remains unspecified and Task 6 remains deferred under R52. Paid T3/T4
calls remained prohibited until task-specific authorization; T3 was later authorized and
completed once as recorded above, while T4 remains prohibited pending Jimmy's written
roster, run, budget, and cap authorization. The later $1 shadow-bakeoff authorization above
was a separate, exact exception and did not authorize either run. The historical question
records below are retained for provenance.

**Historical provisional packet:** `20260711-codex-provisional-adjudication-recommendations.md`
was ratified/superseded by R47–R53. It remains provenance only and assigns no ruling
numbers.

## RESOLVED 2026-07-11 — Task 4: bridged manifest has zero OPEN-eligible families

- **Ruling:** Keep the new manifest and close the ladder. No stale eligibility restoration,
  exemplar revision, rerun, or additional candidate screening is authorized.

- **Question:** How should the MVP proceed when the full R44 requalification removes Gemini's OPEN eligibility and no non-Google candidate qualifies, leaving zero OPEN-award families?
- **Why it blocks:** R44 defines success as either a non-Google OPEN pass (cross-family) or zero candidate passes while Google remains single-family. The completed run instead produced Gemini award-consistency 0/8, Grok award-consistency 0/8, and no qualifying Cohere/Nova row. The manifest is valid for coherence, disclosure, and settled-core, but the 204 standard OPEN items cannot be scored under the new manifest, so the MVP is not testable.
- **Evidence:** `07-PILOTS/20260711-format-bridge-requal/20260711-format-bridge-requal-report.md` and its canonical manifest.
- **Suggested default:** Keep the new manifest and report as the honest immutable Task 4 record; close the pre-G6 candidate ladder; do not tweak the exemplar, rerun, restore stale eligibility, or screen another model without a new Jimmy/Fable ruling.

## RESOLVED 2026-07-12 — Task 5: 22-item EPISODE specification registry

- **Ruling:** R54 reviewed all 22 entries field-by-field; R56 directed Codex to apply the
  exact corrections, approval block, canonical approved-registry transition, and R55.4
  bidirectional fixtures offline. No live run was authorized.
- **Resolved implementation:** `04-HARNESS/config/episode-spec-registry.json` is the
  canonical `APPROVED` registry and loads through the default
  `wcfbench.episode_registry.load_episode_registry()` path outside review mode. All 22
  entry review statuses are approved; the exact R54 correction table and all seven
  corrected marker lists have regression coverage. T2 completed with zero bank edits and
  zero live calls.

- **Question:** Who should supply or approve the per-item `EpisodeSpec`, tool semantics, blind prompts, and outcome detectors needed to execute the 22 frozen EPISODE items?
- **Why it blocks:** `wcfbench/episode_live.py` is a one-spec red-team defect-calibration helper, not a blind benchmark runner. The only production `EpisodeSpec` is hard-coded in `openrouter_pilot.py`; the 22 bank records contain `episode: true` but no executable spec registry. No compliant 88-cell checkpoint/transcript/disagreement/report path exists. Authoring these mappings would introduce new scoring judgments not ruled by R42–R46.
- **Suggested default:** Do not improvise a registry or run the calibration prompt as the examinee prompt. Keep Task 5 unchecked until Jimmy/Fable supplies or approves the structured 22-item mapping and execution semantics.

## RESOLVED 2026-07-11 — Tasks 5–6: cheap-only OpenRouter constraint versus binding rosters

- **Ruling:** Pause all paid calls and continue offline only. Do not substitute models.

- **Later bounded exception (2026-07-12):** Jimmy authorized only the two-model,
  shadow-only bakeoff and $1 cap recorded above. T3 was later separately authorized and
  completed once; T4 and the remaining paid scopes stay paused unless separately authorized.

- **Question:** Which exact model slugs are approved as "cheap" for the remaining live EPISODE and PROOFTEXT work, and does that instruction supersede the exact Task 5 four-SUT roster and Task 6 qualified-judge panel?
- **Why it blocks:** The execution plan fixes the Task 5 SUTs and requires Task 6 judge re-reading under the Task 4 manifest. Substituting cheaper models would violate the pre-registered scope, while proceeding without an approved cheap list would violate the current user instruction.
- **Suggested default:** Make no further paid calls and do not substitute model slugs. Continue only hermetic/offline implementation until Jimmy identifies approved cheap slugs or explicitly authorizes the binding roster/panel.

## PARTIALLY RESOLVED 2026-07-11 — Task 6: existing anchor-use path cannot score uncited paraphrases

- **Ruling:** Use the current citation-gated scorer as-is. Do not change its prompt or
  uncited-paraphrase behavior.
- **Resolved scope:** The scorer contract is fixed as ruled. No prompt or citation-gate
  change will be made.
- **Remaining question:** Which qualified manifest surface, if any, authorizes the current
  anchor-use prompt? The Task-4 manifest defines only `open_award`, `disclosure`,
  `coherence`, and `settled_core`; anchor use has no probe, eligibility mapping, or template
  hash. Aliasing it to any existing surface would invent a new ruling, while `open_award`
  currently has zero eligible judges.
- **Additional consequence:** Under the ruled as-is gate, uncited anchors never reach a
  judge, so the plan's paraphrase-recovery fixture and expected floor rise cannot be met.
- **Suggested default:** Keep Task 6 blocked; do not alias eligibility or weaken the gate.
  If Task 6 is later resumed, specify the eligible surface and revise its acceptance
  criteria to match the ruled citation-gated behavior.

- **Question:** What exact judge contract and qualification surface should govern PROOFTEXT paraphrased-anchor use when the response correctly applies a clause without emitting its literal `Q…`/`WCF …` reference token?
- **Why it blocks:** `judge_score_anchor_use` currently applies a mechanical citation gate and does not consult the judge for an uncited anchor, so it cannot satisfy Task 6's required paraphrased-anchor fixture. Removing that gate requires changing the judge prompt/scoring semantics; the anchor-use prompt is not represented as its own qualification surface/template hash, and the Task 4 manifest has zero OPEN-award eligibility. Wiring the current function would preserve the artifact or turn declines into low scores rather than fix it.
- **Suggested default:** Do not change the prompt, invent an eligibility mapping, or run the persisted re-read. Jimmy/Fable should specify whether judges receive each rubric criterion/anchor for uncited semantic matching, which qualified surface admits those judgments, and whether that prompt change requires another manifest event; then Codex can implement the already-bounded scorer and cheap-approved re-read.
