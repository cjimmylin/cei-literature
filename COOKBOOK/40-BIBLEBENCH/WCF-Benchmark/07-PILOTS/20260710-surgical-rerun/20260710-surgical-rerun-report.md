# WCF-Bench — R40.4/R40.5 Surgical Re-run Report (persisted-text-first floor closure)

**Date:** 2026-07-10 · **Executor:** Opus build (main loop, foreground live run)
· **Canary:** `WCFBENCH-CANARY-c1647-x9k4q` (re-used, not re-minted)
· **Governing doc:** binding Fable memo `20260710-fable-grok-ratification-floor-divergence-memo.md`
(R38–R41), directive **R40.4 / R40.5**
· **Run timestamp:** `2026-07-10T15:39:46` · **template_hash:** `47ddb41c355fbf57` (settled-core
prompt UNCHANGED — R40.4 requires the current templates)
· **Panel:** combined third-family manifest
`07-PILOTS/20260710-third-family-screen/20260710-third-family-manifest.json` (UNCHANGED) —
gpt4omini (openai), gemini-flash (google), grok-4.20 (x-ai)
· **Live spend:** ~$0.26 (limit_remaining $44.82 → $44.56; deepseek SUT 3 calls / 2,362 tokens;
budget was < $2)

> DESCRIPTIVE / pre-gate. This report completes the missing settled-core tie-breaker on the
> adjudicated `AGG-C8-W305 × llama` cell and closes the deepseek transport-starved arm, under
> the current templates, preserving the adjudicated sample (persisted-text-first). Verdicts are
> READINGS; the floor is the **sample-level adjudicated** claim per R39(e), not the raw aggregate.

---

## 0. Scope executed (exactly R40.4)

| leg | cell | mode | new SUT call? |
|---|---|---|---|
| (a) | `AGG-C8-W305 × llama` | re-grade **grok-4.20 ONLY** on the PERSISTED response; combine with persisted gpt/gemini for the 3-judge tie-break | **no** (persisted) |
| (b) | `WHOLE-C9-W301 × deepseek` | re-grade **all 3 judges** on the PERSISTED response (all 3 judge calls transport-failed in the floor re-run → `judges=[]`) | **no** (persisted) |
| (c) | `AGG-C3-W302`, `AGG-C5-W304`, `AGG-C8-W305 × deepseek` | **fresh deepseek SUT calls** (the 403'd "Key limit exceeded" contested arm), panel-graded | **yes** (3 calls) |
| (d) | the llama arm | NOT re-run (scored + adjudicated) | — |

Harness state: the R40.2 retry seam (one retry + backoff on JSONDecodeError / HTTP 402/403/429,
post-retry loss → `fail_transport_after_retry`) and the R40.3 tie→UNGRADED rule are LIVE in
`judge_panel.py` for this run.

---

## 1. (a) `AGG-C8-W305 × llama` — the completed 3-judge settled-core tie-breaker

grok re-graded the **persisted** llama response cleanly on the first attempt
(`retried=false`, `finish_reason="stop"` — **no JSONDecodeError this run**). This supplies the
third vote that was missing when grok's JSONDecodeError dropped it in the floor re-run.

**Per-keypoint settled-core, 3-judge panel (raw run):**

| settled-core keypoint | gpt4omini | gemini-flash | grok-4.20 | raw aggregate (R40.3 rule) |
|---|---|---|---|---|
| **kp1** "no collapse to 'both equal'; profiles differentiated" | correct | wrong | **correct** | **True** (2–1) |
| **kp2** "Q152 floor on both" | correct | wrong | **wrong** | **False** (2–1) |

**Raw 3-judge `settled_core_fraction` = 0.5** (kp1 held, kp2 not).

grok's per-axis on this cell: disclosure **0.0**, coherence **0.0**, position **not defensible**
(grok's coherence verdict: *"fabricates an entirely alien 'Q151 calculus'… operates on vibes… SCORE:
0.0"*). grok's settled-core verdict text verbatim:

> 1: correct — profiles are clearly differentiated with explicit ranking (b < a) and no collapse to "both equal"
> 2: wrong — response does not engage or satisfy the Q152 floor; it explicitly uses and repeatedly references a fabricated "Q151 calculus" instead

### 1.1 The R39(e) sample-level reading of this cell (NOT a floor break)

- **kp1 resolves `True` (2–1)** — this **confirms the memo's R39(b) reference verdict** (`correct` on
  the literal criterion): the response differentiates the profiles and declines a confident order,
  which is the gold position, not a collapse. gemini's lone `wrong` remains the R31(b) disagreement
  record. **grok agrees with the reference.**
- **kp2 resolves `False` (2–1) on the RAW run — but this is a SCREEN, not the claim (R39(e)(1)).**
  A settled-core `False` triggers **sample-level review before any floor break may be asserted.**
  Reviewed: **grok's kp2 `wrong` repeats gemini's exact category error** already adjudicated at
  **R39(a)** — it reads the response's fabricated **Q151** "calculus" as a failure to satisfy the
  **Q152 floor**. But WLC Q152 *"is not a calculus and has no factors; it is the wrath floor"*
  (R39(a)); the established kp2 test is the **negative** one — *is either leg graded harmless?*
  The persisted llama text grades neither leg harmless (both "morally reprehensible", the 11-year
  drift counted as **aggravating**), so **the adjudicated reference for kp2 is `correct`** (R39(a),
  binding). grok graded the theological competence of the calculus (real, bad — and already priced
  into its coherence 0.0), not the floor. **The kp2 `False` is a two-judge (gemini+grok) category
  error on the floor keypoint, overruled on the R39(a) footing; it is NOT a model floor miss.**
- **Adjudicated reading of the cell: settled core PRESERVED** (kp1 `correct` confirmed 2–1; kp2
  adjudicated `correct` per R39(a) — the raw `False` is a judge-side category error surviving
  sample review, exactly the R39(e)(2)/(3) distinction: a judge `wrong` that does not survive review
  against the text is not a floor break). This is fully consistent with R39(f): "AGG-C8 adjudicated
  reference 1.0 against a recorded raw aggregate 0.0."
- **NEW systematic-finding datum for R39(d):** grok has now joined gemini in penalizing the floor via
  the Q151-vs-Q152 conflation (grok's kp2 `wrong` reason is verbatim the R39(a) category error). This
  **strengthens the R39(d) directive**: the floor-gloss ("'Q152 floor' = neither leg graded
  harmless/no-fault; it is a floor, not a calculus") is needed for **≥2 judge families**, not one.
  (R39(d) is the NEXT build item, not this one — flagged here as confirming evidence.)

---

## 2. (b) `WHOLE-C9-W301 × deepseek` — all 3 judges re-graded (persisted text)

The persisted deepseek WHOLE-C9 response (an OPEN wholeheart item) had `judges=[]` in the floor
re-run (all 3 judge calls transport-failed). Re-graded cleanly by all 3 judges under the retry seam:

- **triaxial 1.0 / 1.0 / 1.0** (matter/manner/end), **headline 1.0**; judges used = gpt/gemini/grok.
- per-judge: gemini 1.0/1.0/1.0, grok 1.0/1.0/1.0, gpt 1.0/**0.0**/1.0 (gpt's lone Manner 0.0 is a
  per-judge disagreement record; OPEN-award aggregation over the OPEN-award-eligible judge(s) only).
- **No transport failures** — the WHOLE-C9 arm is recovered.

---

## 3. (c) fresh deepseek contested arm (AGG-C3 / AGG-C5 / AGG-C8) — the 403'd arm closed

Fresh deepseek/deepseek-chat SUT calls (3 calls, all `error=null` — the "Key limit exceeded" 403
condition is cleared post-topup), panel-graded:

| item | settled_core_fraction | disclosure | coherence | position_defensible | escalation | RANKING line |
|---|---|---|---|---|---|---|
| AGG-C3-W302 | **1.0** | 0.5 | 0.917 | yes | none | `RANKING: a < b < c` |
| AGG-C5-W304 | **1.0** | 0.25 | 0.667 | yes | none | `RANKING: a < b` |
| AGG-C8-W305 | **1.0** | 0.5 | 0.583 | yes | none | `RANKING: B < A` |

- **All 3 deepseek contested cells preserve the settled core (fraction 1.0), no ties, no escalation.**
- Per-keypoint settled_core: every keypoint `True` on all three (Q152 floor + no-collapse both `True`;
  AGG-C3 single settled keypoint `True`). No settled-core `False` → **no sample-level review triggered**
  on the deepseek arm.
- deepseek's responses are theologically stronger than llama's here (it does not fabricate a six-factor
  calculus in the same pathological way; it grounds in WLC Q141–152 and gives a clean `RANKING:` line),
  which is why the settled core is credited cleanly.

---

## 4. Transport / retry event log

`judges_discarded` (verbatim) — **both entries are per-surface eligibility SUSPENSIONS, NOT transport
losses**:

```
["gpt4omini",  "per-surface SUSPENDED for ['disclosure', 'open_award'] — manifest openai/gpt-4o-mini"]
["grok-4.20",  "per-surface SUSPENDED for ['open_award'] — manifest x-ai/grok-4.20"]
```

- **Zero `fail_transport_after_retry` events. Zero JSONDecodeError drops. Zero HTTP 402/403/429.**
- grok's AGG-C8 re-grade succeeded on the first attempt (`retried=false`) — the floor-rerun
  JSONDecodeError did not recur on this slice. The R40.2 retry seam was armed but never needed to
  fire on the live cells.

---

## 5. R40.5 — settled-core floor recompute (R39(e) semantics) + R38(3)(ii) ratification confirmation

### 5.1 Floor recompute (sample-level, adjudicated — R39(e))

| SUT | cell | raw settled_core_fraction | settled-core `False`? | sample-level adjudicated reading |
|---|---|---|---|---|
| llama | AGG-C8-W305 | 0.5 (kp1 True, kp2 False) | kp2 `False` (raw) | **PRESERVED** — kp1 `correct` (2–1, confirms R39(b)); kp2 raw `False` = a 2-judge (gemini+grok) **category error** on the floor keypoint, overruled per R39(a); adjudicated reference 1.0 |
| deepseek | AGG-C3-W302 | 1.0 | no | PRESERVED |
| deepseek | AGG-C5-W304 | 1.0 | no | PRESERVED |
| deepseek | AGG-C8-W305 | 1.0 | no | PRESERVED |

**Adjudicated floor reading: the settled core HOLDS on every scoreable cell in this slice.** The only
settled-core `False` in the raw data (llama AGG-C8 kp2) does **not survive sample-level review** — it is
the judge-side Q151↔Q152 category error the memo already ruled at R39(a), now reproduced by a second
judge (grok). Per R39(e)(2)–(3): a judge `wrong` that fails review against the text is not a floor break;
the floor's validity function (reported misses are REAL) is intact — there is no real weak-SUT
collapse-to-equal or harmless-grading in any reviewed cell. The deepseek arm, previously
transport-starved, now confirms the floor cleanly (3/3, no review needed).

> Note on the raw record: the raw 3-judge `AGG-C8 × llama` fraction is **0.5** (not the pre-fix 0.0 and
> not 1.0). This is the R40.3 tie rule + grok's real vote working as designed — grok resolved kp1 to
> `True` (killing the old 1–1→False artifact on kp1) but voted kp2 `wrong` (the category error). The
> gap between the raw 0.5 and the adjudicated 1.0 is exactly the R39(a) overruled floor keypoint; it is
> disclosed here, not smoothed.

### 5.2 R38(3)(ii) ratification-confirmation verdict — grok's parse behavior on the slice

R38(3)(ii): *"If grok shows ≥2 post-retry parse losses on the re-run slice, this ratification reopens;
otherwise it is final."*

- grok made settled-core/disclosure/coherence/position calls on: (a) the persisted llama AGG-C8 cell,
  (b) the persisted deepseek WHOLE-C9 cell, (c) the 3 fresh deepseek contested cells (5 cells total,
  ~4 `.complete` calls each).
- **grok post-retry parse losses on the slice: 0.** No JSONDecodeError, no `fail_transport_after_retry`,
  no discard for cause. grok graded every cell cleanly, first attempt (`retried=false` where reported).
- **VERDICT: R38(3)(ii) CONDITION NOT TRIGGERED (0 < 2). grok-4.20's ratification as the SECOND
  disclosure family is CONFIRMED / FINAL.** The single floor-rerun JSONDecodeError stands as the
  occasional-not-systematic robustness event R38(2) characterized; the R40.2 retry seam now covers its
  recurrence.

---

## 6. Consequences

- **Nothing model-blocked is reopened.** grok ratification final (R38(3)(ii) confirmed); the
  settled-core floor holds sample-level on the full scoreable slice (llama + deepseek); the deepseek
  transport-starved arm is closed.
- **R39(d) is strengthened, not contradicted:** grok independently reproduced the gemini
  Q151↔Q152 floor category error (kp2 `wrong`), so the floor-gloss + settled-core probe + re-qualify
  (the NEXT build item) now has a two-family motivation. That work changes the settled-core prompt and
  is deliberately NOT done here (R40.4 ordering: surgical re-run FIRST, under current templates).
- H-DISC's sole remaining block stays **G6 (Jimmy)**; the judge-side R30 condition 6 is met.

## 7. Artifacts (append-only; report immutability honored)

- `07-PILOTS/20260710-surgical-rerun/transcripts.jsonl` — full run payload (persisted re-grades +
  fresh deepseek responses + per-keypoint votes + grok verbatim verdict texts).
- `07-PILOTS/20260710-surgical-rerun/disagreement.json` — same payload, indented.
- `07-PILOTS/20260710-surgical-rerun/20260710-surgical-rerun-report.md` — this report.
- `07-PILOTS/20260710-floor-rerun/` — FROZEN, untouched (its raw "2/3" line stands as the historical
  record; this is the adjudicated reading of it, per the memo).

## 8. Guardrails honored

Report immutability (NEW dated dir; floor-rerun/ untouched). Settled-core prompt template, probe
fixtures, and `current_template_hashes()` NOT touched (that is R39(d), a later agent). Canary not
re-minted. Secrets sourced at runtime, never written. Live run from the session main loop, foreground.
No `git`, no deletions. Scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`.
