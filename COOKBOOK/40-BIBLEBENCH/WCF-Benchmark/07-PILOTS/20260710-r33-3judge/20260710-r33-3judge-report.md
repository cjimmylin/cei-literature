# WCF-Bench — R33.5 3-Judge Per-Surface Pilot Report (DESCRIPTIVE / pre-gate)

**Date:** 2026-07-10 · **Session:** 11 (Opus build) · **Governing spec:** binding memo
`20260710e-fable-postfix-adjudication-memo.md` (R33.4/R33.5/R33.6)
· **Run dir:** `07-PILOTS/20260710-r33-3judge/` (append-only; report immutability)
· **Harness:** `04-HARNESS/openrouter_pilot_r33.py --go` · **Canary:** `WCFBENCH-CANARY-c1647-x9k4q`

> DESCRIPTIVE, pre-gate — **no measurement claim**. This is the R33.5 deliverable: wire a
> third judge family, qualify all judges under the extended per-surface battery (R33.4),
> and re-run the 6-item slice to see whether the disclosure channel regains a cross-judge
> pair. It does NOT. The qualification run **diverges from the memo's reference verdicts**
> and surfaces a non-determinism validity threat — both flagged for a Fable pass.

## 1. What ran (live, GREEN)

- **Judges (3 families, fast-mid):** `openai/gpt-4o-mini`, `google/gemini-2.5-flash`,
  `mistralai/mistral-small-3.2-24b-instruct` (mistral = the R33.5 third family; qwen
  dropped per WALKWORTHY F-2 dead-slug). Slugs validated live against `/api/v1/models`.
- **SUTs:** `meta-llama/llama-3.1-8b-instruct`, `deepseek/deepseek-chat` (cross-family,
  distinct from every judge family).
- **Items:** 3 OPEN (COMP-C8-W301, MEND-C1-W301, WHOLE-C9-W301) + 3 CONTESTED
  (AGG-C3-W302, AGG-C5-W304, AGG-C8-W305). `k=3` → all judges grade every item; per-surface
  aggregation then selects the eligible ones.
- **Result:** 0 errors, 12 (item×SUT) cells, 12 R27 transcript cells persisted
  (`transcripts.jsonl`, template_hash `47ddb41c355fbf57`), disagreement clusters in
  `disagreement.json`. The extended battery + per-surface panel + truncation-retry + R27
  transcripts all exercised **live** for the first time.

## 2. Per-surface qualification (the headline)

Live battery outcome at panel construction (each judge, all five probes):

| judge | G4 | award-consist. | discrimination | disc-inversion | neg-disclosure | ⇒ eligible surfaces |
|-------|----|----|----|----|----|----|
| gpt-4o-mini | ✅ | ❌ (format) | ❌ (identical strong/weak) | ✅ | ❌ (0.5 on a settled order) | coherence, settled-core |
| gemini-2.5-flash | ✅ | ✅ | ❌* (KP2/KP3 → None) | ✅ | ✅ (0.0) | **all four** |
| mistral-small-3.2 | ❌ (format) | ✅ | ❌ (all-award) | ❌ (unparseable) | ❌ (unparseable) | **none → discarded** |

`*` gemini's discrimination is **non-deterministic** — see §4.

**Consequence:** after mistral is discarded and gpt is suspended for open-award + disclosure,
**DISCLOSURE-valid families = {google} only; OPEN-award-valid families = {google} only.**
Both surfaces are **still starved** (< 2 families). **R30 promotion condition 6 (≥2
disclosure-valid judge families) is NOT satisfied — H-DISC remains unpromotable, and the
gated OPEN/contested measurement still lacks a cross-family award pair.** R33.5's goal is unmet
with *this* third-family slug.

## 3. Divergence from the memo → warrants a Fable pass

The memo's provisional per-surface status (R33.6) and R29 characterization did **not**
reproduce cleanly:

- **R33.6 expected** gpt RETAINED for open-award (R29: "reads per-keypoint, blunt at the
  margins") and gemini SUSPENDED for open-award (R29b: "holistic all-or-nothing"). **Live it
  reversed:** gpt emitted an **identical** award pattern for the strong (deepseek, all-award)
  and weak (llama) WHOLE-C9-W301 responses — the holistic failure the discrimination probe
  exists to catch — and its award-consistency emission was unparseable. gemini, by contrast,
  emitted all 7 keypoint lines correctly on at least one run (all-award on the strong cell,
  all-deny on the weak — the reference divergence).
- **R30 CONFIRMED (robustly):** the negative-disclosure probe reproduced the dead-channel
  finding — gpt awarded avoided-settled on a confident total-order response (disclosure 0.5),
  gemini correctly denied both (0.0). gpt's disclosure suspension stands on real-item evidence.

Per the boot prompt, a qualification run that **disagrees with the memo's reference verdicts**
is the reserved trigger for a final Fable pass. The open-award characterization (which judge
is holistic) is the disputed point; the disclosure characterization is not.

## 4. Non-determinism — a validity threat to per-surface acceptance

gemini's discrimination probe verdict **flipped across three live calls** at temperature 0:
- panel construction: **passed** (admitted to open-award);
- diagnostic run 1: **failed** — strong-cell KP2/KP3 came back `None` (2 mismatches > tol 1);
- diagnostic run 2: **passed** — all 7 KP lines emitted, all award (`finish_reason=stop`,
  7 lines, 2098 chars — not a truncation).

A single probe pass/fail is therefore **not a stable gate**: the same judge qualifies or is
suspended for a surface depending on the run. **Directive for the next design pass (Fable):**
run each probe with repetition (best-of-N / majority) before it gates a surface, or widen the
discrimination tolerance to absorb a single dropped keypoint line. The per-surface machinery is
sound; its single-shot gating is not.

## 5. Live-caught regression (fixed this session)

The pilot showed `settled_core = 0.0` on **all 6 contested cells** — but session-9's floor held
1.0. Cause: the R33.1 settled-core **reason mandate** requires a reason, but the settled-core
**prompt never asked for one**, so a format-compliant judge emitted reasonless `1: correct`
(verified in the transcripts) → uncredited → the anti-relativism floor collapsed everywhere.
**Fixed:** the settled-core prompt now mandates `<n>: correct — <reason>` (test
`test_settled_core_prompt_requests_a_reason`). A re-run will confirm the floor holds; the
`20260710-r33-3judge` numbers for settled-core are an artifact of the pre-fix prompt and must
not be read as a floor failure.

## 6. Descriptive scored notes (2 valid judges after mistral drop; NOT a measurement)

- **Disclosure discriminates** (F-2 confirmed): deepseek 0.5/0.0/0.5 vs llama 0.0/0.0/0.5 across
  the three contested items — models rarely surface contestedness, and the channel now separates
  a hedge from a flat assertion.
- OPEN axes: deepseek ≫ llama (deepseek COMP/MEND 1.0/1.0/1.0, WHOLE Matter 0.71; llama COMP
  ungraded, MEND 0.33/0.25/0.0, WHOLE 0.0/0.0/1.0) — consistent with the pilot ordering, no claim.
- No SUT truncation; no malformed RANKING lines in this slice (R33.8 parse-report clean).

## 7. Guardrails honored

WCF-Bench scope only. Report immutability: new dated run dir + report; the postfix pilot dir
untouched. Canary not re-minted. Secrets sourced at runtime, never committed. No gold minted;
the probe fixtures are judge-side calibration (R29(d)), not examinee items. Shared git index
treated as LIVE.

## 8. For the next session

1. **Fable pass (window ~2026-07-11):** adjudicate the open-award characterization reversal
   (gpt holistic vs gemini) and rule on the non-determinism remedy (repeat-probe gating vs
   tolerance widening) before any surface eligibility is treated as fixed.
2. **Third family:** `mistral-small-3.2-24b` is NOT viable (G4 + disclosure-form format
   failures). Try a more instruction-following mid slug (e.g. `mistralai/mistral-medium-3.1`,
   `cohere/command-r`, or `x-ai/grok` fast tier) — the disclosure surface stays starved until a
   second disclosure-valid family qualifies.
3. Re-run this slice after the settled-core prompt fix to confirm the floor holds.
