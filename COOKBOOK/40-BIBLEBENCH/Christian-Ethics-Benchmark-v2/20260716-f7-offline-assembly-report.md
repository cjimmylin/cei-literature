# F7 (JV-8) — design-07 prior-turn-context judging: OFFLINE ASSEMBLY + COST ESTIMATE

**Date:** 2026-07-16 · **Status:** offline assembly + self-checked metrics scaffold DONE;
**LIVE ARM NOT RUN.** Zero model calls of any kind were made this session (no SUT, no
judge). This report is the offline deliverable + honest cost estimate only.

R11 flags design-07 per-turn judging as **order-blind for order-dependent states**: the
shipped `_make_per_turn_scorer` assembles one judge prompt per turn from that turn's
response *in isolation*. The F7 experiment re-judges the SAME stored design-07 turns with
the rubric prompt **augmented by prior-turn context** (the administered SEEKER turns +
COUNSELOR responses up to turn i−1, read from the Inspect store key `ww_turns`), versus
the shipped context-free verdicts as baseline. Judge calls only; the SUT is never re-run.

---

## 1. What was built

| File | Role |
|---|---|
| `tools/audit/judge_context_ablation.py` | Assembler + dry-run + gated live re-judge (mirrors `judge_ablation.py` monkeypatch-and-restore philosophy). |
| `tools/audit/context_ablation_agreement.py` | Offline metrics scaffold (`self-check` runs today; `agreement` runs once live verdicts exist). NO model calls, ever. |
| `logs/f7-context/dryrun-judgeA-nano.json` | Per-prompt char/token stats, judge A. |
| `logs/f7-context/dryrun-judgeB-llama.json` | Per-prompt char/token stats, judge B (identical — prompt content is judge-agnostic). |

## 2. The monkeypatch surface

The design constraint (from `judge_ablation.py`): everything EXCEPT the manipulated
variable must be byte-identical to the live per-turn judge pass, so we **patch one module
attribute the assembler already calls and restore it in `finally`** — never fork
`assemble_rubric_prompt`.

- `assemble_rubric_prompt` resolves `scorers._references(meta)` through the module
  namespace to build the "# Matched-quality reference answers" block. Design-07 ships
  `reference_anchored=True`, so that block is **always** emitted (it carries the shipped
  `_DESIGN07_STATE_ANCHORS`).
- `context_patch()` replaces `_scorers._references` with a wrapper that, for design-07,
  returns the ORIGINAL anchors with **one extra anchor PREPENDED**: a
  *"Prior turns in THIS conversation (turns 0..i−1) — the counsel state is
  ORDER-DEPENDENT…"* block. The judge sees the conversation so far → the state anchors →
  then the turn to score (still injected as the assembler's own `response_text`).
- Per-turn context reaches an otherwise meta-only function via a module-local holder
  (`_CURRENT_PRIOR_CONTEXT`) set immediately before each `assemble_rubric_prompt` call and
  cleared after. The assembler is REUSED verbatim; context-free and context arms differ by
  exactly one block.
- **Turn 0 gets NO context block** (returns `None`) so its prompt is byte-identical to the
  context-free baseline — turn 0 has no prior order information to add, and forcing an
  empty block would spuriously differentiate it. Each prior turn is truncated to 600 chars
  (in-band with the assembler's existing 400-char cap on anchor text).
- Restore verified: after `context_patch()` exits, `scorers._references.__name__ ==
  "_references"` (the original). Injection verified: turn-0 prompt has no
  "Prior turns in THIS" marker; turn-2 prompt carries "turns 0..1" plus the original
  `comfort_only (matched quality)` state anchors and the `Response to score (turn 2)` unit
  label.

**Live-arm safety (this session leaves it unfired):** `--live` is gated behind BOTH an
explicit flag AND env `WW_F7_LIVE=1` (left UNSET), AND requires an explicit `--max-tokens`
cap (OpenRouter 402 reservation trap — every call needs an explicit `max_tokens`), AND
`--out`. All three refusal paths were exercised: env-unset, no-max-tokens, and the offline
default all exit non-zero and write no file. Verdicts in live mode are appended per-verdict
with `flush()` (NOT buffered-to-completion — the `classifier_sensitivity.py`
buffer-everything anti-pattern made progress invisible).

## 3. Self-check result (metrics join proven offline, TODAY)

`context_ablation_agreement.py self-check` compares the shipped context-free judge-A
turn_states against THEMSELVES (baseline-vs-baseline), with the join scoped by
(sut, log-basename, sample_id) — the collision-safe pattern from `ablation_agreement.py`
(sample_ids repeat across SUTs).

```
  deepseek-chat        A/A: 163/163 (1.000)  n_excluded=0  n_samples=27  [OK]
  gemini-flash-lite    A/A: 163/163 (1.000)  n_excluded=0  n_samples=27  [OK]
  gpt-4.1-mini         A/A: 163/163 (1.000)  n_excluded=0  n_samples=27  [OK]
  llama-3.3-70b        A/A: 163/163 (1.000)  n_excluded=0  n_samples=27  [OK]
  mistral-small        A/A: 163/163 (1.000)  n_excluded=0  n_samples=27  [OK]
  TOTAL A/A agreement = 815/815 (1.000)  n_excluded=0
  SELF-CHECK PASS: join logic correct (baseline-vs-baseline = 1.000).
```

Control (shipped judge-A vs judge-B — the real design-07 gap the F7 arm probes), proving
the 1.000 is not a trivial always-1 artifact:

```
    deepseek-chat  A/B: 91/157 (0.580)   gemini-flash-lite A/B: 82/161 (0.509)
    gpt-4.1-mini   A/B: 82/160 (0.512)   llama-3.3-70b     A/B: 78/160 (0.487)
    mistral-small  A/B: 90/158 (0.570)   TOTAL A/B = 423/796 (0.531)
```

The `agreement` subcommand refuses (exit 2) while no F7 context JSONL exists, printing
"LIVE ARM NOT RUN — awaiting PF-003 GO."

## 4. Assembly counts + DISCREPANCY vs the boot-prompt's 1,090

The boot prompt asserted **109 design-07 turns × 5 SUTs × 2 judges = 1,090** prompt
instances. The stored data does not support 109. Honest counts from the real assembly:

| Quantity | Boot-prompt claim | ACTUAL (measured) |
|---|---|---|
| design-07 turns per SUT | 109 | **163** |
| design-07 samples (item×admin) per SUT | — | 27 (all `admin=base`, 27 unique item_ids) |
| turns × 5 SUTs (prompts per judge) | 545 | **815** |
| × 2 judges (total prompt instances) | 1,090 | **1,630** |

The number was **not forced** to match. 815 prompts/judge exactly reproduces the
`d07-anchors-off` dry-run count in `20260716-spend-memo-f9-f2-crossharness.md` (815
calls/judge, line 43) — so 815 is the established design-07 turn count; "109" appears to be
a boot-prompt transcription error (possibly a per-SUT turn count from an earlier/smaller
bank slice). All 5 SUTs are uniform: 27 samples, 163 turns each.

Turn-distribution per SUT (identical across all 5): 19 samples × 6 turns, 4 × 5 turns,
3 × 7 turns, 1 × 8 turns = 163 turns. Of the 815 prompts/judge, **135 are turn-0** (no
prior context; byte-identical to baseline) and **680 carry a prior-turn-context block**.

## 5. Context-augmented prompt-length distribution (per prompt, chars)

Prior-turn context makes prompts materially longer than F2's context-free d07 arm (F2:
1.35M in-tokens/judge; F7: **1.847M** in-tokens/judge, +37%).

| Stat | chars |
|---|---|
| n (prompts/judge) | 815 |
| min | 3,644 |
| mean | 9,064.8 |
| median | 8,440 |
| p90 | 13,312 |
| max | 26,749 |
| **total chars/judge** | **7,387,845** |
| **est input tokens/judge (chars/4)** | **1,846,961 (≈1.847M)** |

(turn-0 subset: n=135, mean 9,363.6 chars — turn-0 prompts include the full first
COUNSELOR response, which in this design is often the longest single turn, so turn-0 mean
sits slightly above the overall mean even though it carries no prior-context block. The
growth from prior context is real but bounded by the 600-char/turn truncation.)

Per-SUT total chars: deepseek 1,414,623 · gemini-flash-lite 1,927,435 · gpt-4.1-mini
1,350,403 · llama-3.3-70b 1,277,735 · mistral-small 1,417,649. (gemini-flash-lite's longer
responses drive its higher total.)

## 6. Cost estimate

**Prices** (cited from `20260716-spend-memo-f9-f2-crossharness.md`, lines 38–39; also
corroborated in `20260716-spend-memo-f5-f3.md` item 1a for judge A):
- **Judge A** `openrouter/openai/gpt-4.1-nano`: **$0.10/M input, $0.40/M output**.
- **Judge B** `openrouter/meta-llama/llama-3.3-70b-instruct`: **$0.10–0.30/M input,
  $0.25–0.40/M output** (endpoint-dependent — the R10 availability probe pins it before
  any authorized run).

**Volumes** (from the real assembly): 815 calls/judge · 1,846,961 input tokens/judge.
**Output cap = `JUDGE_MAX_TOKENS = 4096`** (`walkworthy_inspect/scorers.py:47` — the cap
every prior judge run uses; the live arm passes it via `--max-tokens 4096`). Ceiling
assumes every call maxes the cap (3,338,240 out-tokens/judge); the point estimate assumes
~60 output tokens/call (a small category-JSON verdict — the `judge_ablation.py` dry-run
assumption), = 48,900 out-tokens/judge.

| Judge | Input cost | Point est (≈60 out/call) | Ceiling (4096 out/call) |
|---|---|---|---|
| A gpt-4.1-nano | $0.1847 | **$0.2043** | **$1.5200** |
| B llama-3.3-70b | $0.1847–$0.5541 | **$0.1969–$0.5736** | **$1.8894** |
| **TOTAL (A+B)** | — | **≈ $0.40–$0.78** | **≈ $3.41** |

- **Realistic point estimate: ~$0.40–$0.78** (judge B's range is the input/output
  price band; nano is fixed-price).
- **Hard ceiling: ~$3.41** (both judges, every call maxing 4096 output tokens at judge B's
  high price band). Recommend a per-item running `model_usage` tally that aborts at ceiling,
  matching prior F-ledger practice.

Prior-turn context makes F7 materially costlier than F2's d07-anchors-off arm (F2 ceiling
$0.80 for one judge / 815 calls); the +37% input tokens plus a second judge account for
the difference.

## 7. Files created (absolute paths)

- `…/Christian-Ethics-Benchmark-v2/tools/audit/judge_context_ablation.py`
- `…/Christian-Ethics-Benchmark-v2/tools/audit/context_ablation_agreement.py`
- `…/Christian-Ethics-Benchmark-v2/logs/f7-context/dryrun-judgeA-nano.json`
- `…/Christian-Ethics-Benchmark-v2/logs/f7-context/dryrun-judgeB-llama.json`
- `…/Christian-Ethics-Benchmark-v2/20260716-f7-offline-assembly-report.md` (this file)

## 8. Anomalies (verbatim)

- **Boot-prompt count "109 design-07 turns" is wrong.** Stored data has 163 turns/SUT (27
  samples/SUT, all `admin=base`). Assembled 815 prompts/judge (= 163×5), 1,630 total across
  2 judges — NOT 1,090. 815/judge matches the established `d07-anchors-off` dry-run count
  in the F2 spend memo, so 163 is authoritative and "109" is a boot-prompt transcription
  error. Not forced to match.
- **turn-0 mean chars (9,363.6) > overall mean (9,064.8)** despite turn-0 carrying no
  prior-context block — because design-07 turn-0 COUNSELOR responses are often the longest
  single turn. Expected, not a bug; noted so it is not mistaken for context leaking into
  turn 0.
- **No F7 context JSONL exists** (live arm not run), so the `agreement` subcommand cannot
  produce context-vs-shipped numbers this session; it refuses cleanly with the PF-003
  message. Only the `self-check` (baseline-vs-baseline) ran.

---

**LIVE ARM NOT RUN — awaiting consolidated spend-memo authorization (PF-003).**

Canary: WALKWORTHY-CANARY-7f3e2026 · no holdout content.
