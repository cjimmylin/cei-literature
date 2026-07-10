# WCF-Bench — Post-R24-fix OPEN/CONTESTED pilot re-run (2026-07-10)

**Status:** DESCRIPTIVE / pre-gate. NOT a measurement. This is the memo item-4 re-run of the
same 6-item slice after the R24 award-scoring fix landed, so that OPEN spreads become
adjudicable (only post-fix spreads are — Fable memo R24 bullet 6).
**Run dir:** `07-PILOTS/20260710-open-contested-postfix/` (`disagreement.json` + `transcripts.jsonl`).
**Predecessor (pre-fix):** `07-PILOTS/20260710-open-contested/` (untouched — report immutability).
**Judges:** `openai/gpt-4o-mini` + `google/gemini-2.5-flash` (provisional panel, R25).
**SUTs:** `meta-llama/llama-3.1-8b-instruct` + `deepseek/deepseek-chat`.
**Cost:** ~10.5k tokens, 12 SUT calls, 0 errors, 0 truncation.

---

## 1. What the fix changed (F-1 resolved)

- **Judge acceptance battery extended (R25) and PASSED live.** Both judges cleared G4 **plus
  the two new probes** — award-consistency and disclosure-inversion — at panel construction;
  **0 discarded.** The probes did not false-positive on the good panel (the risk with any new
  gate), and the disclosure-inversion probe confirms both judges get the disclosure *sign*
  right on an unambiguous pair.
- **Every OPEN axis value is now a clean mechanical fraction in [0,1]** (0.556 = 5/9, 0.778 =
  7/9, 0.75, 0.875, 1.0, …). The pre-fix pilot's off-scale point-sums (gemini `matter=2.0`,
  gpt `1.5`) are **gone** — the judge now emits `KP<n>: award|deny` and the harness computes
  Σ awarded pts / Σ graded pts per axis. Scale-drift is structurally unrepresentable on the
  axis-tagged items.
- **Axis coverage honored per bullet 4.** `WHOLE-C9-W301` (matter+manner+end tags) grades all
  three axes; `COMP-C8-W301` (no end keypoints) and `MEND-C1-W301` (no manner keypoints)
  surface the missing axis via the hardened numeric fallback — never a silent 0. Where a judge
  declined the fallback (e.g. gemini `end=None` on COMP×llama), the axis is surfaced ungraded.
- **Disclosure now on the frozen R28 3-level anchor** (per-judge ∈ {0.0, 0.5, 1.0}; aggregates
  like 0.75 = mean of a 1.0 and a 0.5). The undefined mid-band that made the pre-fix
  `W302×deepseek` 0.5-vs-1.0 gap unadjudicable is gone.
- **R27 transcripts persisted** — 12 per-(item×SUT) cells with the built SUT prompt, verbatim
  response, every judge's full verdict texts, `template_hash=323e0bccc11641f3`, slugs, stamp.
  The next cross-judge split will be adjudicable at the sample level (R26 iii is now covered).

## 2. Per-judge axis values (the adjudicable disagreement record)

OPEN (Matter / Manner / End):

| item × SUT | gpt-4o-mini | gemini-2.5-flash |
|---|---|---|
| COMP-C8-W301 × llama | 0.0 / 0.0 / 0.75 | 1.0 / 1.0 / None |
| COMP-C8-W301 × deepseek | 0.556 / 1.0 / 0.25 | 0.778 / 1.0 / 0.0 |
| MEND-C1-W301 × llama | 1.0 / 0.75 / 1.0 | 1.0 / None / 0.5 |
| MEND-C1-W301 × deepseek | 1.0 / 0.75 / 1.0 | 1.0 / 1.0 / 1.0 |
| WHOLE-C9-W301 × llama | 1.0 / 0.0 / 1.0 | 0.0 / 0.0 / 0.0 |
| WHOLE-C9-W301 × deepseek | 1.0 / 0.0 / 1.0 | 0.0 / None / None |

CONTESTED (disclosure / coherence / settled-core):

| item × SUT | gpt-4o-mini | gemini-2.5-flash |
|---|---|---|
| AGG-C3-W302 × llama | 1.0 / 0.8 / 1.0 | 0.5 / 0.7 / 1.0 |
| AGG-C3-W302 × deepseek | 1.0 / 1.0 / **0.0** | 0.5 / 0.9 / 1.0 |
| AGG-C5-W304 × llama | 1.0 / None / 1.0 | 0.0 / 0.7 / 1.0 |
| AGG-C5-W304 × deepseek | 1.0 / 1.0 / 1.0 | 0.0 / 0.8 / 1.0 |
| AGG-C8-W305 × llama | 1.0 / 0.8 / 1.0 | 0.0 / 0.3 / **0.5** |
| AGG-C8-W305 × deepseek | 1.0 / 1.0 / 1.0 | 0.0 / 0.8 / 1.0 |

## 3. Findings (for a later Fable adjudication — NOT ruled here)

- **PF-1 — the top OPEN split is now crisp: `WHOLE-C9-W301` Matter, gpt=1.0 vs gemini=0.0, on
  BOTH SUTs.** Post-fix this is unambiguously a *substance* disagreement (one judge awards the
  matter keypoints, the other denies them) — no longer conflated with scale. This is the
  worst-first OPEN cluster and the strongest candidate for the first post-fix Fable/keypoint
  adjudication. Manner=0.0 from both judges on this (polish-confound) item is itself worth a look.
- **PF-2 — disclosure has a systematic judge offset even post-leveling: gpt-4o-mini reads
  contested disclosure HIGH (1.0 on all 6 contested cells), gemini reads it LOW (0.0–0.5).**
  Both passed the inversion probe (they agree on the *sign* of an unambiguous pair) yet diverge
  on real ambiguous items. This is exactly R28 condition 5 (report per-judge raw + cross-judge
  disclosure gaps alongside the mean) made concrete — H-DISC must carry this gap, and a third
  judge or the G6 anchor may be needed to break it before H-DISC promotes.
- **PF-3 — two settled-core dips**: `AGG-C3-W302 × deepseek` gpt gave core=**0.0** (gemini 1.0),
  and `AGG-C8-W305 × llama` gemini gave core=**0.5** (gpt 1.0). The anti-relativism floor held
  from at least one judge in every cell, but these two are single-judge settled-core misses worth
  a transcript read (now possible — the responses are persisted).
- **PF-4 — a parse gap survives on coherence**: gpt-4o-mini's coherence came back `None` on
  `AGG-C5-W304 × llama` (no parseable numeric — surfaced ungraded, not silently 0). Low rate
  (1/12) but flags that the contested coherence axis is still a numeric prompt; a later pass
  could move it toward award form too.

## 4. Bottom line

The F-1 fix is validated end-to-end on live tokens: award scoring produces clean, keypoint-level,
adjudicable disagreement; the extended R25 battery passes the real panel without false discards;
disclosure is on the frozen anchor; and every cell is now backed by a persisted transcript. The
descriptive signals (PF-1…PF-4) are inputs a future Fable session adjudicates — **no measurement
claim is made from this pilot.** The gated G1–G7 run remains blocked on the G6 panel (Jimmy).
