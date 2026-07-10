# WCF-Bench — Fable Adjudication Memo: Probe Stability, the Open-Award Reversal, and Per-Surface Gating (R34–R37)

**Date:** 2026-07-10 · **Author:** Fable (main-loop adjudication, session 12)
· **Status:** **BINDING** (rulings **R34–R37**; continues the R-chain from
`20260710e-fable-postfix-adjudication-memo.md` R29–R33)
· **Governing docs:** session-11 handoff `20260710g-wcf-session-handoff.md` §2/§5;
R33.5 report `07-PILOTS/20260710-r33-3judge/20260710-r33-3judge-report.md`
· **New evidence (this session):** K=8 probe-stability sweep
`07-PILOTS/20260710-probe-stability/` — 4 judges × 5 acceptance probes × 8 reps,
temperature 0, 160/160 records complete, run live via OpenRouter
(`04-HARNESS/probe_stability.py --go`, ~cents). Raw verdicts in `raw_verdicts.jsonl`
(authoritative); `pass_rates.json`; console log `sweep-console.log`. An earlier aborted
partial (18 records, killed with its subagent) is preserved append-only as
`raw_verdicts.aborted-0814.jsonl`. Note: the generated report's per-run pattern cells
rendered as `???` (renderer defect, R37(ii)); every number below was verified directly
against `raw_verdicts.jsonl` in the main loop.

> Scope: WCF-Bench only. Nothing here relitigates R1–R33 except where explicitly
> amended (R33.6 panel status, at R34). The sweep is judge-side calibration
> (R29(d) material) — no examinee measurement, no gold minted, no item touched.

---

## 0. The stability table (verified against raw verdicts)

Pass-rates, n/8 at temperature 0:

| judge | G4 | award-consist. | discrimination | disc-inversion | neg-disclosure |
|---|---|---|---|---|---|
| `openai/gpt-4o-mini` | 8/8 | 2/8 | **0/8** | 8/8 | **0/8** |
| `google/gemini-2.5-flash` | 8/8 | 5/8 | **6/8** | 8/8 | **8/8** |
| `mistralai/mistral-small-3.2-24b` | **0/8** | 2/8 | 0/8 | 0/8 | 0/8 |
| `mistralai/mistral-medium-3.1` | **0/8** | 8/8 | 0/8 | 2/8 | 0/8 |

Failure-mode decomposition (the adjudication turns on this, not on the raw rates):

- **gpt-4o-mini, discrimination:** 8/8 reps emitted the *identical* strong/weak
  pattern `{KP1: award, KP2: deny, KP3: deny}` — **zero variance across 8 runs**.
  Deterministic response-insensitivity, not noise. (On the weak cell it mis-awards
  KP1; on the strong cell it mis-denies both manner KPs — *with* the R33.7
  clause-gloss in the prompt, so the R29(c) "citation-required misreading"
  hypothesis is disconfirmed as the full explanation.) Its negative-disclosure
  over-credit is equally deterministic: `0.5` on all 8 reps (reference 0.0). Its
  award-consistency failures (6/8) are format ("no parseable award lines").
- **gemini-2.5-flash:** exactly **three failed reps in the whole sweep carry an
  `error` finish_reason** on one of their calls (award-consistency reps 0 and 5,
  discrimination rep 1 — the same "KP→None" flip session 11 observed live). The
  probe path calls `judge.complete()` directly and never retries on
  `finish_reason == 'error'` or short emission (unlike the production award path,
  which has R33.3). Net substantive record after removing transport losses:
  discrimination 6 pass / 1 genuine off-reference rep (rep 0: over-awarded the weak
  cell's manner KPs); award-consistency 5 pass / 1 genuine format miss;
  negative-disclosure a constant, correct `0.0` (8/8).
- **mistral-small-3.2:** G4 fails 8/8 **substantively** (`flagged=True` on both
  calibration fixtures, i.e. scored the weak response ≥ the strong) *and* the
  disclosure form is unparseable 8/8. Multiply invalid.
- **mistral-medium-3.1** (fresh 4th candidate, slug live-validated): G4 fails 8/8
  substantively (B≥A on one or both fixtures every rep); discrimination 0/8 with an
  identical all-award pattern; disclosure-inversion mostly unparseable (A=None).
  Perfect award-consistency (8/8) is irrelevant given G4 — a judge that formats
  reliably while ranking the weak response above the strong is reliably wrong.

## R34 — The open-award characterization reversal is REAL; R33.6 panel status AMENDED

**Ruling.** The R33.5 live observation is confirmed and is not a single-run artifact:

1. **gpt-4o-mini is INVALID on the OPEN award surface — SUSPENDED** (in addition to
   its R30 disclosure suspension). Basis: deterministic 0/8 discrimination with zero
   pattern variance + 6/8 award-consistency format failures. R33.6's "gpt retained
   for OPEN award" is **overturned**. gpt-4o-mini is retained ONLY for **coherence +
   settled-core** (G4 8/8 stable).
2. **gemini-2.5-flash is RE-QUALIFIED for the OPEN award surface** under the R35
   repeat-probe gate: 6/8 discrimination, with both failures accounted for (one
   transport error the probe path failed to retry; one genuine off-reference
   leniency rep, recorded). Its R29b suspension is lifted **as of the R33.1 reason
   mandate**, not retroactively.
3. **Reconciliation with R29 — no relitigation.** R29's sample-level adjudication was
   correct on its (pre-R33.1) evidence: gemini's session-10 holistic failures were
   *reasonless* blanket verdicts. The R33.1 mandate differentially repaired gemini —
   forcing a per-keypoint reason forces a per-keypoint reading — while gpt, already
   format-compliant, was untouched by it: its insensitivity is content-level. R29's
   reference keypoint verdicts stand unchanged (they are the probe fixtures). The
   lesson is recorded as binding context: **judge characterizations are
   intervention-relative** — any prompt-contract change invalidates prior per-surface
   characterizations until re-qualification (mechanized at R35.4).
4. **Consequence for the panel:** OPEN-award-valid families = {google} only;
   disclosure-valid families = {google} only. **Both scored contested/OPEN surfaces
   now rest on a single family.** Extending R30's logic (same rationale — no
   redundancy behind a single reader, no cross-judge gap reportable): the gated
   OPEN/contested measurement requires **≥2 valid judge families on every surface it
   scores** (OPEN award and disclosure alike). Descriptive single-family runs may
   proceed but must be labeled single-family, and their OPEN/disclosure numbers may
   not be quoted as measurements. H-DISC status unchanged (unpromotable; R30
   condition 6 unmet).

## R35 — Non-determinism remedy: repeat-probe majority gating (tolerance widening REJECTED as primary)

**Ruling.** Per-surface acceptance moves from single-shot probes to a
**retry + majority-of-K** gate. Precise, implementable directive:

1. **Probe-path retry parity.** Every probe judge-call routes through the same
   R33.3 retry semantics as the production award path: retry ONCE on
   `finish_reason ∈ {length, error}` or short emission (emitted KP lines < listed);
   a rep that still fails post-retry counts as a **failed rep with recorded cause**
   — never an error dropped from the denominator. (This alone converts gemini's
   observed instability from 3 spurious fails to ~1.)
2. **K=8 repetitions per probe, gate = pass iff ≥5/8 reps pass.** Uniform across all
   five probes (G4, award-consistency, discrimination, disclosure-inversion,
   negative-disclosure). Tolerance stays 1; the per-rep `patterns_differ`
   requirement stays. Cost is trivial (this sweep: 160 probe executions ≈ cents).
3. **Rep-level cause taxonomy recorded** in the qualification artifact:
   `pass | fail_substantive | fail_format | fail_transport_after_retry`.
4. **Qualification is an artifact, not a side effect.** `JudgePanel` consumes a
   recorded **qualification manifest** (dated run dir + template hashes + slugs +
   the pass table + eligible-surface sets); surface eligibility is FROZEN to that
   manifest. Re-qualification is required iff (a) a judge slug changes, (b) the
   template hash of any prompt used by that surface's probes or grading changes, or
   (c) a binding memo orders it. Panel construction must NOT silently re-derive
   eligibility per run — the run-to-run gate flip session 11 observed becomes
   structurally impossible.
5. **Why not widen the tolerance (rejected as primary):** the observed instability
   decomposes into transport losses (fixed by 1) and rare rep-level grading variance
   (absorbed by 2); neither is a near-threshold reference disagreement. Widening
   tolerance 1→2 would raise a *coin-flip* judge's single-shot admission probability
   to ≈0.30 (P(≤2 mismatches over 6 binary checks) = 22/64, × P(patterns differ) ≈
   7/8), i.e. it stabilizes valid judges only by inflating false admission. The
   majority-of-8 gate at tolerance 1 holds the coin-flip admission at ≈3×10⁻⁴ while
   giving a genuinely-valid judge (post-retry p ≈ 0.86) >98% decision replication.
   Empirical separation in this sweep: invalid judges sit at p = 0.0 with zero
   variance; the valid judge sits at p ≈ 0.75–0.86 — the ≥5/8 threshold bisects a
   wide margin on both sides.
6. **Provisional manifest, effective immediately:** this sweep
   (`07-PILOTS/20260710-probe-stability/`) is the qualification manifest of record
   for the current prompt templates. Eligible surfaces: gemini-2.5-flash → {OPEN
   award, disclosure, coherence, settled-core}; gpt-4o-mini → {coherence,
   settled-core}; mistral-small-3.2, mistral-medium-3.1 → {} (discarded). The
   session-11 settled-core prompt fix does not invalidate this manifest (the
   settled-core surface is gated by G4, whose fixtures do not use the settled-core
   prompt) — but that exposes a **gap, flagged not blocking**: settled-core has no
   prompt-specific probe. Optional future probe; not required for the next re-run.

## R36 — Third family: mistral tier EXHAUSTED; screen-first retry criteria

**Ruling.**

1. **mistral-small-3.2 is OUT — confirmed** (the R33.5 discard stands; now on K=8
   evidence: substantive G4 failure, not merely format).
2. **mistral-medium-3.1 is OUT — new** (substantive G4 failure 8/8 + all-award
   discrimination). The mistral family is exhausted at fast-mid tier; do not spend
   further reps on mistral slugs below the frontier tier.
3. **Screen-first protocol (binding):** every future third-family candidate runs the
   K=8 battery (`probe_stability.py`, extended per R35.1) **before** any pilot
   wiring. A candidate is wired only if it reaches ≥5/8 on at least one starved
   surface (disclosure at minimum; OPEN award ideally both).
4. **Candidate order** (fast-mid tier; family ∉ {openai, google, anthropic}; never
   the cell's SUT family per §4.3): `cohere/command-r` class → `x-ai/grok` fast
   tier → `amazon/nova` class — slugs live-validated against `/api/v1/models` at
   run time (an Opus build detail). If three further candidates fail: escalate
   **tier within new families** (command-a / grok-frontier class) for the starved
   surfaces only — per-call cost is acceptable at disclosure/OPEN-award volumes; or
   propose a format-bridge (few-shot exemplar in the award/disclosure prompt),
   noting a template change ⇒ new template hash ⇒ **full re-qualification of all
   judges** (R35.4).
5. **Until ≥2 families are valid per scored surface:** gated OPEN/contested
   measurement stays blocked and H-DISC stays unpromotable (R30 condition 6 + R34.4);
   descriptive single-family runs permitted with the single-family label.

## R37 — Housekeeping bindings

1. **The r33-3judge settled-core numbers remain a pre-fix artifact** (reaffirming
   the session-11 report §5): the floor re-run happens after R35 lands, on the same
   6-item slice, and must confirm the 12/12 sample-level floor of R31.
2. **Report-renderer defect:** `20260710-probe-stability-report.md` rendered every
   per-run pattern cell as `???` (the renderer read a key the records don't carry in
   that shape). Per report immutability the generated report is NOT regenerated;
   `raw_verdicts.jsonl` is authoritative and this memo's §0 table is the corrected
   record. Fix the renderer in `probe_stability.py` for future runs only.
3. **Probe-path/production asymmetry** (found pre-data, confirmed by the sweep):
   `run_discrimination_probe` and its siblings call `judge.complete()` directly,
   bypassing R33.3. R35.1 closes this. Until it lands, no probe outcome is a valid
   gate — the provisional manifest (R35.6) governs in the interim.
4. **Sweep provenance:** the first sweep attempt died with its dispatching subagent
   at 18/160 records (background process lifetime is bound to the spawning agent);
   the partial is preserved append-only. Operational note for future live runs: run
   long sweeps from the session main loop or a persistent runner, not inside a
   subagent's background shell.

## Confirmations (frozen surfaces — verified, not relitigated)

- **R30 disclosure ruling:** reproduced deterministically (gpt constant 0.5
  over-credit ×8; gemini constant correct 0.0 ×8). The dead-channel suspension
  stands on the strongest possible footing.
- **R29 reference verdicts, R28 frozen anchor + conditions 1–6, contested-scoring
  ruling, R33.1–.8 build, OpenRouter path, canary:** untouched.
- **Anti-gaming:** unchanged — probe fixtures remain judge-side calibration; no item
  re-authored; examinee blind.

## Handoff → next Opus build session (ordered)

1. R35.1–.4: probe-path retry parity + K=8 ≥5/8 majority gating + cause taxonomy +
   qualification-manifest consumption in `JudgePanel` (mock-first, TDD).
2. R36.3–.4: screen cohere/command-r-class candidate(s) with the K=8 battery;
   wire the first qualifier.
3. Re-run the 6-item slice (post settled-core prompt fix, with the manifest panel):
   confirm the R31 floor holds; check whether disclosure gains a second family.
4. Earlier-wave transcription ~161→230 (protocol unchanged, session-11 handoff §3).
5. Minor: renderer fix (R37.2).

## Guardrails honored

WCF-Bench scope only; siblings untouched. Report immutability: new dated memo; the
probe-stability dir is a new append-only run dir; the aborted partial preserved, not
deleted; no existing pilot dir touched or re-scored. No gold minted; no item edited;
no G6 run. Canary `WCFBENCH-CANARY-c1647-x9k4q` not re-minted. Secrets sourced at
runtime, never committed. Shared git index treated as LIVE (explicit paths,
`git log -1` before commit).
