# F7 (JV-8) — design-07 PRIOR-TURN-CONTEXT judging: LIVE RESULTS

**Date:** 2026-07-16 · **Status:** LIVE ARM RUN (both judges) + metrics + report DONE.
**Authorization:** owner GO 2026-07-16, ceiling $4.00 (`20260716-spend-memo-f7.md`, Item 1).
**Estimated actual spend: ~$0.40–$0.78** (see §4) — far under ceiling; no pause triggered.

This report is the live-arm deliverable for the offline assembly documented in
`20260716-f7-offline-assembly-report.md` (read that first for the monkeypatch surface,
assembly counts, and cost model). It targets **R11's PROVISIONAL order-blindness flag** on
design-07 per-turn judging: does re-judging the SAME stored design-07 turns with prior-turn
conversational context change per-turn state verdicts, close the A-vs-B judge gap, or move
arc_pass_rate?

---

## 1. What ran

| Judge | Model slug | Calls (prompts) | Rows | Turn verdicts | Row judge_errors | Unscorable turns |
|---|---|---|---|---|---|---|
| A | `openrouter/openai/gpt-4.1-nano` | 815 | 135 | 815 | 0 | 3 (0.37%) |
| B | `openrouter/meta-llama/llama-3.3-70b-instruct` | 815 | 135 | 815 | 0 | 5 (0.61%) |

- **R10 availability probe (before any authorized run):** one 16-token call per judge.
  Both returned cleanly (A completion `'OK.'`, B completion `'OK'`; usage logged). Neither
  judge unavailable/erroring → proceeded.
- 5 SUTs × 27 design-07 samples/SUT × (5–8 turns) = 815 turns/judge = 163 turns/SUT,
  matching the offline assembly (NOT the boot-prompt's "109" — a transcription error, see
  offline report §8). 135 sample-rows/judge (27×5).
- **Zero judge_errors and zero API failures** on either arm. Verdicts written incrementally
  (JSONL append, `flush()` per row) — progress was visible throughout; no stalls.
- Both judges are G5-certified. Both live JSONLs contain the full 135 rows / 815 turns.
- Output artifacts:
  - `logs/f7-context/context-judgeA.jsonl` (135 rows, 815 turn verdicts)
  - `logs/f7-context/context-judgeB.jsonl` (135 rows, 815 turn verdicts)
  - `logs/f7-context/run-judgeA.log`, `logs/f7-context/run-judgeB.log`

### Per-turn state distribution under context (all 815 turns/judge)

| State | Judge A (context) | Judge B (context) |
|---|---|---|
| full_validation | 510 | 586 |
| comfort_only | 181 | 41 |
| cold_correction | 85 | 18 |
| deflection | 21 | 83 |
| faithful_counsel | 15 | 82 |
| unscorable | 3 | 5 |

---

## 2. Metric family (i): per-turn state agreement — context vs shipped (context-free), PER JUDGE

Join scoped by (sut, log-basename, sample_id); n reflects scorable turn positions
(UNSCORABLE on either side excluded). Self-check (baseline-vs-baseline = 1.000 on all
cells) re-verified before the live run.

| SUT | Judge A: shipped vs context | Judge B: shipped vs context |
|---|---|---|
| deepseek-chat | 118/163 (0.724) | 142/154 (0.922) |
| gemini-flash-lite | 125/162 (0.772) | 144/159 (0.906) |
| gpt-4.1-mini | 126/162 (0.778) | 141/160 (0.881) |
| llama-3.3-70b | 108/162 (0.667) | 137/160 (0.856) |
| mistral-small | 113/163 (0.693) | 140/158 (0.886) |
| **TOTAL** | **590/812 (0.727)** | **704/791 (0.890)** |

**Headline:** Adding prior-turn context **changes a substantial share of judge-A verdicts**
(agreement with the context-free baseline drops to 0.727 — i.e. ~27% of judge-A turn states
move when context is supplied) and a **smaller but non-trivial share of judge-B verdicts**
(0.890 — ~11% move). The instrument IS sensitive to prior-turn context; context judging is
not a no-op. The effect is markedly larger for judge A (nano) than judge B (llama).

## 3. Metric family (ii): cross-judge agreement UNDER CONTEXT

Does context close the design-07 A-vs-B judge gap? **Baseline (shipped, context-free) A-vs-B
= 0.531.**

| SUT | A′/B′ (cross-judge, both under context) |
|---|---|
| deepseek-chat | 91/160 (0.569) |
| gemini-flash-lite | 89/160 (0.556) |
| gpt-4.1-mini | 82/162 (0.506) |
| llama-3.3-70b | 74/162 (0.457) |
| mistral-small | 97/163 (0.595) |
| **TOTAL** | **433/807 (0.537)** |

**Headline:** Cross-judge agreement under context is **0.537**, versus the shipped
context-free baseline of **0.531** — essentially unchanged (+0.006). **Context does NOT
close the design-07 judge gap.** The two judges disagree about design-07 per-turn states
just as much with prior-turn context as without it; each judge shifts its own verdicts
(§2), but they shift toward *different* revised states, so the A-vs-B disagreement persists.

## 4. Metric family (iii): arc_pass_rate movement vs shipped

Coarse terminal-state rule (terminal state == `faithful_counsel`), judge A:

| Arm | arc_pass_rate |
|---|---|
| shipped (context-free) | 0.007 (1/135) |
| context | 0.015 (2/135) |
| **delta** | **+0.007 (+1 sample)** |

**Headline:** arc_pass_rate is **floor-saturated** in both arms (1/135 → 2/135). Context
judging moves the terminal-state pass rate by a single sample. Per-turn *states* move a lot
(§2); the terminal-pass summary barely moves because design-07 arcs almost never terminate
in `faithful_counsel` under either arm. (This is the coarse terminal-state proxy, not the
authoritative shipped `_arc_pass_from_states` rule — see the tool docstring.)

---

## 5. Spend (actual/estimated)

**Method:** input tokens are **near-exact** — derived from the assembled prompt chars
(chars/4) captured in the dry-run stats, identical prompt content per judge: 1,846,961
input tokens/judge over 815 calls. Output tokens were **estimated at ~60/call** (small
category-JSON verdict; the `judge_ablation.py` dry-run assumption) because the tool stores
only the parsed `turn_state`, not raw judge text, so exact output-token totals were not
logged. The R10 probe confirmed usage IS returned by the endpoint per call (e.g. A: 10 in /
3 out) but the batch driver discards it. Spend is therefore **input-exact, output-estimated.**

**Prices** (`20260716-spend-memo-f9-f2-crossharness.md` §38–39): A nano $0.10/M in,
$0.40/M out (fixed); B llama $0.10–0.30/M in, $0.25–0.40/M out (endpoint band).

| Judge | Input cost | Output (@60/call est) | Point est |
|---|---|---|---|
| A gpt-4.1-nano | $0.1847 | $0.0196 | **$0.2043** |
| B llama-3.3-70b | $0.1847–$0.5541 | $0.0122–$0.0196 | **$0.1969–$0.5736** |
| **TOTAL** | — | — | **≈ $0.40–$0.78** |

- **Estimated actual spend: ~$0.40–$0.78**, matching the offline point estimate.
- Hard ceiling (every call maxing 4096 output) would have been ~$3.41; actual output was
  a tiny fraction of the cap, so realized spend sits at the low end.
- **No $3.50 pause trigger reached; $4.00 ceiling not approached.**

---

## 6. Findings — with interpretive guardrails

**Guardrails (binding).** This is **INSTRUMENT evidence** targeting R11's **PROVISIONAL**
order-blindness flag on design-07 per-turn judging. Descriptive language only — no
"significant", no inferential claims. The pilot logs are **existing data**, so every
comparison here carries the **C9 "post-hoc on pilot data — hypothesis-generating" label**
(`20260716-prereg-comparisons-RATIFIED.md`). **No SUT-vs-SUT claims** — per-SUT cells are
shown only for join transparency and n sanity-checks (all n ≈ 815/judge minus a handful of
UNSCORABLE, as expected).

Stated plainly:

1. **Does context judging move per-turn states? YES, descriptively — and substantially for
   judge A.** Re-judging design-07 turns with prior-turn conversational context changes
   ~27% of judge-A per-turn states (agreement 0.727 vs the context-free baseline) and ~11%
   of judge-B states (0.890). This is consistent with R11's flag that the shipped
   context-free per-turn judge is **order-blind for order-dependent states**: supplying the
   conversation-so-far demonstrably alters how a turn is classified. The instrument responds
   to context; it is not inert.

2. **Does context close the A-vs-B judge gap? NO.** Cross-judge agreement under context is
   0.537, essentially identical to the shipped context-free baseline of 0.531 (+0.006). The
   two judges each revise their own verdicts when given context, but toward divergent
   states, so the design-07 judge disagreement is **not** resolved by adding context. The
   ~0.53 A-vs-B gap on design-07 is robust to this manipulation.

3. **Does context move arc_pass_rate? Barely — it is floor-saturated.** Terminal-state
   arc_pass moves 1/135 → 2/135 (+0.007). Per-turn states move a lot (finding 1) but the
   terminal-pass summary is near-zero in both arms, so it registers almost no movement.

**Net (hypothesis-generating, per C9):** design-07 per-turn judging is **order-sensitive as
an instrument** — prior-turn context materially changes individual per-turn verdicts,
corroborating R11's order-blindness concern as a real (not merely theoretical) property of
the shipped context-free scorer. However, that sensitivity does **not** reconcile the two
judges (cross-judge gap unchanged) and does **not** move the coarse arc-pass summary (floor-
saturated). R11's PROVISIONAL flag is descriptively supported at the per-turn-verdict level;
it does not translate into a closed judge gap or a shifted arc outcome on this pilot data.

---

## 7. Files created (absolute paths)

- `…/Christian-Ethics-Benchmark-v2/logs/f7-context/context-judgeA.jsonl`
- `…/Christian-Ethics-Benchmark-v2/logs/f7-context/context-judgeB.jsonl`
- `…/Christian-Ethics-Benchmark-v2/logs/f7-context/run-judgeA.log`
- `…/Christian-Ethics-Benchmark-v2/logs/f7-context/run-judgeB.log`
- `…/Christian-Ethics-Benchmark-v2/20260716-f7-context-judging-results.md` (this file)

## 8. Anomalies (verbatim)

- **Output-token spend is ESTIMATED, not measured.** The batch driver (`_judge_one`)
  returns only the parsed `turn_state` and discards the per-call `usage` object, so exact
  output tokens were not logged. Input tokens are near-exact (chars/4 of assembled prompts);
  output uses the ~60-tok/call assumption. Spend is input-exact, output-estimated.
- **Boot-prompt / offline-report count reconciled:** 815 prompts/judge (163 turns/SUT × 5),
  1,630 total across 2 judges — NOT the boot prompt's "1,090". 815/judge matches the
  established `d07-anchors-off` dry-run count. Confirmed live: both JSONLs hold 135 rows /
  815 turn verdicts.
- **Judge B (llama-70b) ran ~2× slower per call than judge A (nano)** — expected for the
  larger model; no stalls, steady incremental JSONL growth throughout both runs.
- **A-vs-B baseline gap re-confirmed at 0.531** (self-check control) before the live run;
  under context it is 0.537 — the near-identity of these two numbers is the key result of
  metric family (ii).

---

Canary: WALKWORTHY-CANARY-7f3e2026 · no holdout content.
