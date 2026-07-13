# WCF-Bench Pending Questions

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

**Current execution status:** T1 and T2 are complete and Jimmy ratified the verified R57
checklist on 2026-07-12; durable record:
`20260712l-jimmy-r57-ratification-record.md`. T2.5 is checked and WCF-Bench is MVP
TESTABLE under R53/R58.1, retaining the R34.4 single-family OPEN label and all existing
DESCRIPTIVE/PRE-GATE and PROOF disclosures. Paper P1 citation verification is also
complete. Paid T3/T4 calls remain separately gated and unauthorized. Jimmy separately
authorized the exact, shadow-only judge bakeoff recorded in
`20260712n-shadow-judge-bakeoff-design.md`, with a $1.00 NTE cap; it does not reopen the
candidate ladder, change the manifest, or authorize any T3/T4 call. Written-spec review
preceded implementation. The one authorized run is now immutable and labeled `PARTIAL`:
all 96 probe repetitions and 56 shadow-verdict attempts were persisted, but reconciliation
was `UNRECONCILED` because the runner's internal attributed total was $0.69776393843 while
key-wide usage increased by $5.426614419 during the pre/post interval. All further paid
calls are frozen pending Jimmy's disposition of the question below.

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
calls remain prohibited until Jimmy separately authorizes the specific roster, run, and
budget. The later $1 shadow-bakeoff authorization above is a separate, exact exception and
does not authorize those runs. The historical question records below are retained for
provenance.

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
  shadow-only bakeoff and $1 cap recorded above. Tasks 5–6 and T3/T4 remain paused unless
  separately authorized.

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
