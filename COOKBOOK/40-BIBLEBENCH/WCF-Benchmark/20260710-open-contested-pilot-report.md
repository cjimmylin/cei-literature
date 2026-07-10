# WCF-Bench — OPEN + CONTESTED Live Judge Pilot (2026-07-10)

**Date:** 2026-07-10 · **Executor:** Opus (build session) · **Status:** live pilot GREEN;
DESCRIPTIVE / PRE-GATE only — **NOT the gated G1–G7 measurement**. This report is the
**input a downstream Fable session adjudicates** (judge-disagreement clusters +
judge-calibration go/no-go), per the boot prompt.

Raw data: `07-PILOTS/20260710-open-contested/disagreement.json` (per-judge scores,
disagreement cells, calibration outcome). Reproduce: `04-HARNESS/openrouter_pilot_open.py --go`.

---

## 1. Setup

- **Sanctioned path:** OpenRouter (Jimmy ruling 2026-07-09). One key, cross-family.
- **Judges (cross-family, generator-family excluded, G4-calibrated):**
  `openai/gpt-4o-mini` (openai) + `google/gemini-2.5-flash` (google). Fast mid judges
  (WALKWORTHY F-1 lesson: frontier judges too slow). Both are non-Anthropic, so the
  opus-authored items' generator-family exclusion does not shrink the panel.
- **SUTs (examinees, cross-family, distinct from judge families):**
  `meta-llama/llama-3.1-8b-instruct` (meta) + `deepseek/deepseek-chat` (deepseek).
- **Items (6):** a diverse OPEN slice — `COMP-C8-W301` (complicit), `MEND-C1-W301`
  (mending), `WHOLE-C9-W301` (wholeheart) — + the **3 contested** items
  `AGG-C3-W302`, `AGG-C5-W304`, `AGG-C8-W305`.
- **Cost/scale:** ~10k tokens/SUT, 0 errors, **no truncation** (max_tokens=2048 held).
  12 (item×SUT) cells; each OPEN cell = 2 judges × 3 axes, each contested cell = 2
  judges × 4 constructs.

## 2. Judge-calibration outcome (G4 polish-confound battery, R14) → GO

**Both judges PASSED G4 and neither was discarded.** The battery (WHOLE-C10-W305 +
WHOLE-C10-005: the genuinely-charitable A must out-score the smoother-but-corrupt B)
did not flag either `gpt-4o-mini` or `gemini-2.5-flash`. On this slice the panel is a
**calibration GO** — but see F-1 (the axis-scale inconsistency is a *separate* judge
quality issue the G4 battery does not test).

## 3. Contested items — position/coherence (adherence), per-judge

The binding ruling's scorer ran live and produced the four adherence constructs
(disclosure / defensibility / coherence / settled-core), **never a τ-vs-gold number**.

| item · SUT | judge | disclosure | defensible | coherence | settled-core |
|---|---|---|---|---|---|
| AGG-C3-W302 · llama | gpt-4o-mini | 0.0 | ✔ | 0.8 | 1.0 |
| AGG-C3-W302 · llama | gemini | 0.0 | ✔ | 0.7 | 1.0 |
| AGG-C5-W304 · llama | gpt-4o-mini | 0.5 | ✔ | 0.8 | 1.0 |
| AGG-C5-W304 · llama | gemini | **0.0** | **✗** | **0.2** | 1.0 |
| AGG-C8-W305 · llama | gpt-4o-mini | 0.0 | ✔ | 0.8 | 1.0 |
| AGG-C8-W305 · llama | gemini | 0.0 | ✔ | 0.7 | 1.0 |
| AGG-C3-W302 · deepseek | gpt-4o-mini | 0.5 | ✔ | 1.0 | 1.0 |
| AGG-C3-W302 · deepseek | gemini | **1.0** | ✔ | 0.9 | 1.0 |
| AGG-C5-W304 · deepseek | gpt-4o-mini | 0.5 | ✔ | 1.0 | 1.0 |
| AGG-C5-W304 · deepseek | gemini | 0.0 | ✔ | 0.8 | 1.0 |
| AGG-C8-W305 · deepseek | gpt-4o-mini | 0.5 | ✔ | 1.0 | 1.0 |
| AGG-C8-W305 · deepseek | gemini | 0.0 | ✔ | 0.9 | 1.0 |

**Reads (descriptive, tiny n):**
- **Disclosure is systematically LOW (mostly 0.0–0.5).** Across both SUTs and both
  judges, models almost never surface that the aggravation weighting is *genuinely
  contested within Reformed thought* — they assert a confident single answer. This is
  the single strongest signal and exactly the construct the ruling elevates. If it
  holds at scale it is a headline finding (models over-claim settledness on disputed
  Reformed questions). **F-2.**
- **Settled-core held at 1.0 everywhere** — the Q152 floor / no-collapse guardrail is
  satisfied even where disclosure fails. The ruling's anti-relativism guardrail works:
  models keep the settled floor while missing the contested disclosure.
- **The one defensibility split** (`AGG-C5-W304 · llama`): gemini judged llama's answer
  a *misapplication of Q151* (defensible=✗, coherence 0.2) while gpt-4o-mini judged it a
  defensible reading of familial-honor duty (defensible=✔, coherence 0.8). **This is a
  genuine cross-judge disagreement cluster — the top item for Fable to adjudicate.**
- Position *labels* differ freely between judges (free-text; the G6 `positions:` map is
  deferred) — expected, not disagreement per se.

## 4. OPEN items — triaxial Matter/Manner/End, per-judge

Triaxial scored live after the parse hardening (see F-1). Values are the two judges'
raw axis scores M/Mn/E; `None` = that judge's axis was ungraded (surfaced, not 0).

| item · SUT | gpt-4o-mini (M/Mn/E) | gemini (M/Mn/E) |
|---|---|---|
| COMP-C8-W301 · llama | 0.0 / None / 0.0 | None / 1.0 / 1.0 |
| MEND-C1-W301 · llama | 1.0 / 1.0 / 1.0 | 2.0 / 1.0 / 0.8 |
| WHOLE-C9-W301 · llama | 1.0 / 1.0 / 0.8 | None / 0.0 / 0.625 |
| COMP-C8-W301 · deepseek | 1.0 / 0.5 / 0.5 | 0.6 / 0.1 / 0.1 |
| MEND-C1-W301 · deepseek | 1.5 / 1.5 / 1.5 | 1.0 / 1.0 / 1.0 |
| WHOLE-C9-W301 · deepseek | 0.5 / 1.0 / 0.9 | 1.0 / None / 1.0 |

**Reads:**
- The triaxial chain now parses on nearly every axis (vs almost all-`None` before the
  fix). A few residual `None`s remain where a judge emitted no `SCORE:` token.
- **F-1 (scale inconsistency):** some cells carry axis values > 1.0 (gemini M=2.0,
  gpt-4o-mini M/Mn/E=1.5) despite the explicit `0.0–1.0` instruction — those judges fell
  back to a 0–2 (rubric-points) scale. So a raw cross-judge spread of ~1.0 on these OPEN
  cells **conflates scale-disagreement with substance-disagreement** and must not be read
  as pure substance disagreement. The disagreement cells flagged for OPEN items
  (COMP/MEND/WHOLE × llama at spread 1.0) are partly this artifact.

## 5. Disagreement clusters (worst-first — the Fable queue)

From `summarize_disagreement` (split-on-defensibility ranks above raw spread):

1. **`AGG-C5-W304 · llama` — SPLIT on defensibility** (gemini ✗/coh 0.2 vs gpt ✔/coh 0.8).
   The one *substantive* contested disagreement. **Adjudicate first.**
2. `COMP-C8-W301 · llama`, `MEND-C1-W301 · llama`, `WHOLE-C9-W301 · llama` — OPEN spread
   1.0, but **confounded by F-1 scale-inconsistency**; re-check after the scale fix.
3. `AGG-C3-W302 · deepseek` — disclosure spread 0.5 (gemini 1.0 vs gpt 0.5): a real
   disclosure-judgment gap on a contested item.
4. Remaining contested cells: coherence/disclosure spreads ≤ 0.5.

## 6. What the Fable session should adjudicate

1. **Judge-calibration go/no-go.** G4 passed both judges → provisional GO, but **F-1
   (axis-scale inconsistency) is an un-tested judge-quality failure**: decide whether to
   (a) re-instruct/pin the scale harder, (b) switch triaxial to per-keypoint award
   scoring (compute the axis fraction mechanically, like the contested settled-core), or
   (c) accept 0..1-clamped headlines and report per-judge raw. This is a design call.
2. **The one real disagreement cluster** (`AGG-C5-W304 · llama` defensibility split): is
   llama's familial-honor reading a defensible Reformed position or a Q151 misapplication?
   This is the kind of call the position taxonomy (G6 `positions:` map) is meant to settle
   — note it feeds the G6 remit, not a single-gold vote.
3. **The disclosure-low signal (F-2):** confirm whether "models rarely disclose
   contestedness" is a scale-worthy headline before committing measurement design to it.

## 7. Guardrails honored

WCF-Bench scope only. OpenRouter path (sanctioned). Secrets sourced at runtime, never
committed. Mock-first suite stays hermetic (240 pytest, 0 network); this live run is
opt-in `--go`. No frozen surface changed; rulings R1–R23 + the contested-scoring ruling
untouched; canary not re-minted. New dated files only (report immutability). G6 not run
(Jimmy's remit).
