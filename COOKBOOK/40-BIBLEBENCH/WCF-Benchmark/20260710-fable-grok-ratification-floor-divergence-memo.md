# WCF-Bench — Fable Adjudication Memo: Second Disclosure Family Ratified + the Settled-Core Floor Divergence (R38–R41)

**Date:** 2026-07-10 · **Author:** Fable (main-loop adjudication, session 14)
· **Status:** **BINDING** (rulings **R38–R41**; continues the R-chain from
`20260710h-fable-probe-stability-adjudication-memo.md` R34–R37)
· **Agenda:** session-13 handoff `20260710j-wcf-session-handoff.md` §4 (Q1–Q3), per the boot
prompt `20260710k-fable-adjudication-boot-prompt.md`.
· **Evidence (all persisted; no model re-run for this adjudication):**
`07-PILOTS/20260710-third-family-screen/` (K=8 pass table + combined manifest);
`07-PILOTS/20260710-floor-rerun/` (`transcripts.jsonl` — the persisted llama `AGG-C8-W305`
response + every judge's verbatim verdict texts; `disagreement.json`; report);
`05-BANK-YAML/aggravate-expansion2.yaml` (the AGG-C8-W305 gold key + rubric floor points);
`04-HARNESS/wcfbench/contested.py` (`settled_core_keypoints`, aggregation tie rule at
`judge_panel.py:360`); precedent R31(a)/(b) in `20260710e-fable-postfix-adjudication-memo.md`.

> Scope: WCF-Bench only. Sample-level judge-side adjudication in the R29/R31 mode —
> reference verdicts on persisted text; no gold minted, no item edited, no examinee
> measurement, no G6 activity. Nothing in R1–R37 is relitigated except where explicitly
> stated (one gemini keypoint verdict overruled at R39(a), parallel in kind to R31(a)).

---

## 0. What the load-bearing cell actually contains

The `AGG-C8-W305 × llama` divergence was read at the sample level from
`transcripts.jsonl`, alongside the item's bank entry. Facts that govern everything below:

1. **The item's gold is "declines total order."** The key opens: *"Incomparable. A confident
   total order scores 0 on the ordering point,"* and closes: *"Full answer maps both, declines
   false precision, notes tendencies."* The stem itself instructs the SUT to apply **"the Q151
   calculus"** and offers `RANKING: declines total order` as the sanctioned exit.
2. **The two settled-core keypoints** (extracted by `settled_core_keypoints()` from the
   rubric, in order) are: **kp1** *"no collapse to 'both equal'; profiles differentiated"*
   (0.5 pts) and **kp2** *"Q152 floor on both"* (0.5 pts, anchor WLC Q152 — "Every sin, even
   the least, … deserveth his wrath and curse"). The contested ordering criterion (1.5 pts,
   "declines a confident total order…") is **not** a settled-core keypoint — it is
   position-scored, per the R21 contested ruling.
3. **llama's response is genuinely pathological, in the same signature R31(b) adjudicated:**
   it invents a six-factor "Q151 calculus" (Quality/Quantity/Duration/Intensity/Social
   status/Age — none of them WLC Q151's actual heads), emits `RANKING: b < a` (a confident
   total order, b least heinous), argues in the adjacent prose that **b is more heinous**
   (contradicting its own ranking line), then hedges *"the Q151 calculus does not yield a
   confident ordering between the two options, as both involve significant moral wrongness.
   However, … Renu's prolonged and intentional breach of trust makes her situation more
   heinous."* It takes all three available positions in one response.
4. **But on the floor specifically**, the response calls (a) *"morally reprehensible …
   dishonesty and a failure to take responsibility"* and (b) *"also morally reprehensible …
   dishonesty and a failure to act with integrity,"* counts Renu's 11-year drift as
   **aggravating** (not exculpatory), and nowhere grades either leg harmless or flattens them
   to equality. It differentiates the profiles on approximately the key's own telling
   elements (a = decision-point deliberateness; b = continuance/duration).
5. **The aggregate 0.0 is partly mechanical:** grok's JSONDecodeError drop left an even
   2-judge settled-core panel, and `judge_panel.py:360` (`sum(votes) > len(votes)/2`)
   resolves a 1–1 tie to **False**. With grok present, either keypoint could have resolved
   2–1.

## R38 — Q1: `x-ai/grok-4.20` is RATIFIED as the valid SECOND disclosure family

**Ruling.** Ratified, on the probe evidence, effective immediately.

1. **The qualification instrument is the R35 K=8 battery, and grok passed it as cleanly as
   the gate can be passed:** g4 8/8, disclosure-inversion 8/8, negative-disclosure 8/8 —
   24/24 on the three probes gating its eligible surfaces, **zero variance**, with the
   negative-disclosure probe being the **real** AGG-C5-W304 item as R30 required (frozen in
   `probe_fixtures.py`). Its OPEN-award exclusion (award-consistency `fail_format` 8/8,
   discrimination `fail_substantive` 8/8) is correctly enforced by the manifest — the gate
   is discriminating surfaces, not rubber-stamping the family.
2. **The live JSONDecodeError does not impeach qualification.** It is a harness seam gap —
   the R35.1 retry covers `finish_reason ∈ {length, error}` and short emission but not a
   downstream JSON parse failure — occasional, not systematic (grok graded AGG-C3, AGG-C5,
   and all three llama OPEN cells cleanly in the same run; its settled-core verdicts there
   are the best-evidenced of the three judges: quoted, floor-engaged, e.g. its AGG-C5 kp2
   `wrong` with *"grades (a) essentially no-fault"*). A parse loss is a transport-class
   event, and R35.1's own principle (a transport loss is never a substantive fail) cuts both
   ways: it is also never substantive evidence against a judge.
3. **Conditions attached (operational, not qualification):**
   - (i) The retry seam is extended to JSONDecodeError / unparseable-verdict (one retry,
     then `fail_transport_after_retry`, recorded, never a silent drop) — build item in R40.2.
   - (ii) **The R40 re-run doubles as grok's operational confirmation.** No separate
     confirmation run is required. If grok shows ≥2 post-retry parse losses on the re-run
     slice, this ratification reopens; otherwise it is final.
   - (iii) The standing R35.4 conditions bind unchanged (slug or template-hash change →
     full re-qualification).
4. **Consequences:** DISCLOSURE-valid families = {google, x-ai} ≥ 2 → **R30 condition 6 is
   MET on the judge side.** H-DISC's sole remaining block is **G6 (Jimmy)**. OPEN award is
   unchanged: single-family {google}, still not quotable as a measurement (R34.4); further
   third-family candidates for the OPEN-award surface remain optional per R36.4.

## R39 — Q2: the settled-core floor HOLDS post-fix at the sample level; the AGG-C8 aggregate 0.0 is a judge-side + transport-side artifact, not a model failure

This is the headline validity call, and the answer is **neither judge's package wholesale**:
gpt's *conclusion* is right on both keypoints (with weak reasons); gemini's kp2 verdict is
overruled outright; gemini's kp1 verdict stands as a defensible-strict disagreement record
exactly as R31(b) left its predecessor. In detail:

**(a) kp2 ("Q152 floor on both") — reference verdict `correct`; gemini OVERRULED.**
gemini's stated reason — *"The response introduces a 'Q151 calculus' which is not the Q152
calculus. It then lists factors that are not the Q152 factors"* — is a **category error**.
WLC Q152 is not a calculus and has no factors; it is the wrath floor ("every sin, even the
least…"). The aggravation calculus **is** Q151, and the item's stem itself directs the SUT
to "the Q151 calculus." The keypoint's established application is the negative test R31(a)
used: *is either leg graded harmless?* Nothing in llama's text does — both legs are
"morally reprehensible," the drift is counted as aggravating, no exculpation is accepted.
gemini answered a different (coherence-flavored) question on the floor keypoint; its
`wrong` is a judge-side event, overruled on the same footing as R31(a)'s overruled gpt
error. (gpt's `correct` here is ratified in outcome, but its reason — "applies the Q151
calculus to both scenarios" — also fails to engage the floor; right verdict, weak
evidence. Recorded, not sanctioned.)

**(b) kp1 ("no collapse to 'both equal'; profiles differentiated") — reference verdict
`correct` on the literal criterion; gemini's strict reading stands as a disagreement
record, per R31(b) applied verbatim.** The response differentiates the profiles (deliberate
decision-point refusal vs eleven-year continuance — approximately the key's own telling
elements) and never flattens them to equality; gemini's quoted evidence (*"does not yield a
confident ordering … both involve significant moral wrongness"*) is a decline of confident
ordering — which is the **gold position** on this item — not an assertion of equality. On
the criterion as written the literal call is `correct`. But this response repeats the exact
mutual-contradiction pathology R31(b) called "genuinely pathological" (ranking line vs
prose), and R31(b) ruled a judge reading that as "no stable differentiation" is within
reason. Same item, same SUT, same judge, same pathology → same treatment: **not overruled,
left standing as a disagreement record; the reference is the literal `correct`.**

**(c) The response's true defect is incoherence, and the coherence axis caught it — again.**
gemini's coherence 0.0 and `DEFENSIBLE: no` (the fabricated six-factor calculus,
misattributed to the Standards) are the better-evidenced verdicts on that surface,
consistent with R31(b) ("gemini 0.3 with detailed textual grounding vs gpt's bare 0.8").
The divergence is two judges answering different questions: gpt graded the floor (all the
settled-core surface asks); gemini graded theological competence (real, bad, and already
priced into coherence/defensibility). The settled-core surface must not double-charge it.

**(d) SYSTEMATIC FINDING — gemini penalizes principled decline-of-ordering on the
no-collapse keypoint.** On AGG-C5 × llama its kp1 `wrong` quotes the same hedge and even
concedes *"even if a ranking is ultimately provided"*; on AGG-C8 it reads the decline as
collapse. That is, gemini treats the behavior the AGG-C8 gold key **rewards** ("declines
total order"; "a confident total order scores 0 on the ordering point") as a floor
violation. This is now a two-cell pattern, orthogonal-to-backwards on the floor. Directive
(build, mock-first): add a **floor-gloss** to the settled-core judge prompt, mirroring the
R33.7 clause-gloss mechanism —
  - "'no collapse to both-equal' targets the lazy-equivalence escape ('both equal / who's
    to say'); a response that *differentiates the profiles* while declining a confident
    total order is NOT a collapse;"
  - "'Q152 floor' = neither leg graded harmless/no-fault; it is a floor, not a calculus."

  Because the settled-core prompt is not in the manifest's hash set, this change is
  manifest-safe under current hashing — which is exactly the **R35.6 flagged gap** now made
  load-bearing. The gloss therefore MUST land together with the settled-core probe R35.6
  anticipated: fixtures = (i) this persisted AGG-C8×llama response, reference {kp1 correct,
  kp2 correct} (per this ruling); (ii) the persisted AGG-C3×llama response, reference
  {floor correct} (both incumbent errors: gpt's AGG-C3 `wrong` is another R31(a)-class
  event, absorbed by majority); (iii) a synthetic true-collapse text ("both are equally
  bad; the tradition cannot rank them" with no profile work), reference {kp1 wrong}. Then
  hash the settled-core prompt into `current_template_hashes()` and re-qualify the
  settled-core surface for all three judges (K=8, ≥5/8, R35 semantics). These fixtures are
  judge-side calibration in the R30 mode — no gold minted, examinee blind.

**(e) What the "R31 12/12 floor" criterion MEANS going forward (binding definition).** The
floor is a **sample-level, adjudicated** claim: *no settled-core failure that survives
review against the persisted response text.* Precisely:
  1. The raw aggregate is a **screen, not the claim**. Any settled-core keypoint `False`
     in the aggregate (a fortiori any cell 0.0) triggers sample-level review before a
     floor-break may be asserted or a floor number quoted in any gated or headline reading.
  2. A lone per-judge `wrong` is a disagreement record, never itself a floor break.
  3. **A genuine weak-SUT miss DOES count against the floor** — the floor is
     credit-when-earned, an empirical observation about SUT behavior, not a guaranteed
     property of the bank. If an adjudicated reading finds a real collapse-to-equal or
     harmless-grading, the cell is reported as a floor miss (floor held n/N, miss
     documented as a model finding). gemini's *principle* was right; its application to
     this text was wrong. The floor's validity function is that settled-core failures,
     when reported, are REAL.
  4. **Tie→False is abolished for settled-core keypoints.** An even eligible-judge split
     is UNGRADED (`None`) + an escalation flag — never a silent False. (Build item, R40.3;
     same no-silent-zero principle R32 confirmed elsewhere in the harness.)

**(f) Floor status of THIS run (adjudicated, descriptive).** llama: **3/3 scoreable
contested cells preserve the settled core** — AGG-C3 1.0 (gpt's lone `wrong` = R31(a)-class
judge error, absorbed by majority), AGG-C5 0.5 (a genuine partial: grok+gemini's
well-evidenced kp2 `wrong` — "(a) essentially no-fault" — stands; credit-when-earned
working as intended; cell floor held under fraction > 0), AGG-C8 adjudicated reference 1.0
(this ruling) against a recorded raw aggregate 0.0. deepseek: unscoreable (transport, R40),
floor status pending the re-run. The floor-rerun report's "2/3" line stands as the
immutable raw record; this memo is the adjudicated reading of it. **R37.1's requirement —
that the re-run confirm the R31 floor — is CONFIRMED on the scoreable sample: the
session-11 prompt fix works (no uniform collapse), and both residual dips are judge-side
or transport-side, exactly as in R31.**

## R40 — Q3: the operational re-run is DIRECTED (next Opus session; no live work in this one)

1. **Root cause corrected first.** The deepseek 403s are `"Key limit exce[eded]"` — an
   **OpenRouter key-limit/credit condition**, not provider routing (the handoff §4's
   "transient provider/routing issue" characterization is amended accordingly; same class
   as WALKWORTHY's HTTP 402). Pre-flight: check the key's limit/usage (`GET
   /api/v1/auth/key`) before any call; if the limit needs raising or a top-up, that is a
   **Jimmy item** and the re-run waits on it. Provider-pin alone would not have prevented
   this; it may still be added as secondary hygiene (PR-5 parity).
2. **Retry-seam extension (mock-first TDD):** one retry with short backoff on (i)
   JSONDecodeError / unparseable judge verdict, (ii) empty/silent emission (already
   covered), (iii) HTTP 402/403/429 transport errors; a post-retry failure is recorded
   `fail_transport_after_retry` in the run artifact (the `judges_discarded` record is kept).
   This discharges R38 condition (i).
3. **Tie→UNGRADED fix** per R39(e)(4) (settled-core keypoint tie among eligible judges →
   `None` + escalation flag).
4. **Surgical scope — persisted-text-first, so the adjudicated sample is preserved:**
   - (a) **Re-grade grok ONLY** on the **persisted** AGG-C8-W305 × llama response (no new
     SUT call — the response text this memo adjudicates remains the sample of record).
   - (b) **Re-grade all three judges** on the **persisted** deepseek WHOLE-C9-W301 response
     (the SUT response exists; all three judge calls transport-failed).
   - (c) **Fresh deepseek SUT calls ONLY** for AGG-C3-W302 / AGG-C5-W304 / AGG-C8-W305
     (no persisted response exists).
   - (d) The llama arm is NOT re-run (scored and adjudicated).
   - New dated run dir (append-only; `20260710-floor-rerun/` is frozen); the combined
     manifest is reused unchanged — **run the surgical re-run FIRST under the current
     templates** (comparability with this adjudication), and do the R39(d) floor-gloss +
     settled-core probe + re-qualification as the following build item, not before.
5. **After the re-run:** recompute the floor reading sample-level per R39(e); grok's parse
   behavior on the slice is the R38(3)(ii) confirmation data. Any deepseek settled-core
   `wrong` gets sample-level review before any floor claim is updated.

## R41 — Housekeeping bindings

1. **The handoff §4 / boot-prompt gloss "wrong calculus (Q151 not Q152)" inherited
   gemini's category error** and is corrected by this memo: Q151 is the aggravation
   calculus the item itself mandates; Q152 is the wrath floor. Future readers should read
   the handoff's §4 through R39(a).
2. **`disagreement.json` cell rows display ineligible judges' raw axis values** alongside
   eligible ones (e.g., gpt's disclosure 1.0 on AGG-C8 despite disclosure-ineligibility;
   surface filtering happens at aggregation, `judge_panel.py:328ff`). Display-only —
   aggregation is correct — but a reader of the raw cells can be misled; optional build
   nicety: annotate per-judge values with eligibility in the disagreement record.
3. **This memo is R29/R31-mode judge-side sample adjudication.** The reference verdicts in
   R39(a)/(b) and the R39(d) probe fixtures are judge-calibration material; no gold was
   minted, no item edited, the examinee stays blind.

## Status after this memo

**Nothing in WCF-Bench is model-blocked.** The full remaining queue:

| item | blocked on |
|---|---|
| G6 confessional panel → gated G1–G7 run, H-DISC promotion (R30 cond. 6 now met judge-side), W304/W305 position maps, 4 LIB `[DISPUTED]` legs | **Jimmy** (recruit raters) |
| OpenRouter key limit check / top-up (pre-flight for R40) | **Jimmy** |
| R40 surgical re-run + retry/tie fixes | next **Opus** build |
| R39(d) floor-gloss + settled-core probe + re-qualification | next **Opus** build (after R40 run) |
| Earlier-wave transcription ~161→230 | **Opus**, deferred (fabrication-sensitive; G6-gated regardless) |

## Handoff → next Opus build session (ordered)

1. R40.1 pre-flight (key limit; stop and surface to Jimmy if top-up needed).
2. R40.2–.3 harness fixes (retry extension + tie→ungraded; mock-first, TDD).
3. R40.4 surgical re-run (persisted-first scope exactly as written; new dated dir).
4. R40.5 floor recompute + R38(3)(ii) confirmation check; short dated report.
5. R39(d) floor-gloss + settled-core probe fixtures + hash + re-qualify (K=8).
6. Then §5 transcription per session-11 protocol, or park.

## Guardrails honored

Adjudication only — no code written, no live call made, no gold minted, no item edited, no
G6 activity. Report immutability: this is a NEW dated memo; `20260710-third-family-screen/`
and `20260710-floor-rerun/` untouched and append-only; the floor-rerun report's raw "2/3"
stands as the historical record. Canary `WCFBENCH-CANARY-c1647-x9k4q` not re-minted. Shared
git index treated as LIVE (`git log -1` before commit; explicit paths only; sibling dirty
files untouched). Secrets sourced at runtime, never committed. Scope-locked to
`COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`.
