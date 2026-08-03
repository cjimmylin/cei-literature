# v4-T Claude-tier differentiation probe — execution report (20260802c)

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.

**Status:** EXECUTED and CLOSED. Authorized by `RULINGS-APPLIED-20260802a` (boot
prompt `20260802b` §4; design was fixed there and is not re-litigated here).
SUT administration ran on Claude Code subscription OAuth (external spend $0);
d01 judging spent $0.1168 of the $1.00 hard ceiling (never approached the stop).

**Every number in this file is a probe diagnostic — not a WALKWORTHY number.**
Probe scores must never be pooled with the inspect_ai reference runs: the CLI
channel carries ~10k tokens of per-call harness overhead and no temperature
control, so absolute levels are not comparable to reference runs. The overhead
is constant across the three tiers, which is what makes tier CONTRASTS
interpretable (boot §3 fact 6).

---

## 1. What was run

Known-groups validity probe: do d01 (goodsamaritan, 49 admin lines, judge-scored)
and d05 (ordoamoris, 32 admin lines, objectively scored) differentiate a
capability gradient known in advance — `claude-haiku-4-5-20251001` <
`claude-sonnet-5` < `claude-opus-5`?

- **Harness:** `tools/audit/tier_probe_claude_oauth.py` (new; `tools/audit/` is
  not pinned by `INSTRUMENT.json`). Ports the WCF `CLIModelClient` pattern:
  `claude -p <user text> --model <pinned id> --output-format json --tools ""
  --strict-mcp-config --permission-mode dontAsk --max-turns 1
  --setting-sources ""`, API-key env vars unset (subscription OAuth), clean
  CLAUDE.md-free cwd, `type: result` JSON parsing. Item system framing was
  delivered via `--system-prompt` (mode `flag`, constant for the entire run;
  d05 items carry no system message and ran with none).
- **CLI flag verification (boot §4.1):** installed CLI is `2.1.220`. All hygiene
  flags present in `claude -p --help` except `--max-turns`, which is absent from
  the help text but still ACCEPTED by the argument parser — verified by a live
  probe call before the census; the flag was kept and the mode recorded on every
  ledger row (`max_turns_flag: true`).
- **Census:** 486 first-pass administrations (81 admin lines x 3 models x 2
  epochs), plus 68 d05 format-retry re-administrations under the instrument's
  one-retry convention (solver F9: retry only when the first response fails even
  after the bounded offline re-parse), plus 1 transient CLI failure retried to
  success (opus, WW-01-N02#base, epoch 1) and 1 flag-probe call. Ledger:
  `logs/tier-probe-20260802/responses.jsonl` (555 rows; append-only,
  resume-safe, key `(design, id, model, epoch, attempt)`); run tree gitignored
  like prior run trees. Epochs are re-administrations at default temperature —
  the CLI exposes no temperature or seed control (disclosed limitation).
  Wall-clock: 76 min at concurrency 4 (median call: haiku 20 s, sonnet 22 s,
  opus 43 s). Coverage: 486 of 486 keys have a non-error first-pass response.
- **d05 scoring ($0, judge-free):** `parsers.reparse_allocation_response` +
  `ordo_constraints.item_csr`, imported read-only. 192 administrations, 181
  scorable, 11 unscorable after the one-retry rule (haiku 7, sonnet 2, opus 2).
- **d01 judging ($0.1168 actual):** full census, 294 responses x 2 pinned
  cross-family judges (judge-A `openai/gpt-4.1-nano`, judge-B
  `meta-llama/llama-3.3-70b-instruct`), OpenRouter REST, temperature 0, prompts
  assembled offline by the shipped surface `scorers.assemble_rubric_prompt` (no
  fork; sole user message, matching the live judge pass). Calibration micro-run
  first (12 calls, $0.003; projected census $0.145 — under ceiling, so the full
  pass was allowed to start). 588 of 588 judgments recorded; 27 needed the one
  authorized parse retry; 5 unscorable (all judge-B; see §4). No
  Claude-judging-Claude reads by design.
- **Keyed-class verification (boot §4.6):** the d01 primary is a binary match of
  the judged `action_class` against the item's keyed class. All 49 items key
  `full_obedience`: every `metadata.keyed.keyed_behavior` string defines full
  obedience as the keyed behavior (14 open with pair-reference or per-position
  phrasing — e.g. "Identical to WW-01-F02 — full obedience = ..." — but all
  define it). Zero items excluded from the primary.

Analysis artifact: `logs/tier-probe-20260802/analysis.json` (item-clustered
bootstrap, B=10,000, seed 20260802). Secondary contrasts and per-judge blocks
are reproduced below.

## 2. Pre-committed read-out 1 — pooled tier contrasts

Primary scores: d01 = share of responses judged `action_class = full_obedience`
(0/1 per response); d05 = constraint-satisfaction rate (CSR, 0-1). Intervals are
95% item-clustered bootstrap CIs on the mean-score gap.

| Contrast | d01 judge-A | d01 judge-B | d05 (objective) |
|---|---|---|---|
| Opus - Haiku (primary) | +0.143 [+0.071, +0.224] — excludes 0 | -0.020 [-0.063, +0.021] | +0.019 [-0.037, +0.075] |
| Opus - Sonnet | +0.082 [+0.031, +0.143] — excludes 0 | +0.021 [-0.020, +0.063] | 0.000 [-0.067, +0.059] |
| Sonnet - Haiku | +0.061 [-0.031, +0.153] | -0.042 [-0.095, 0.000] | +0.019 [-0.035, +0.071] |

Tier means behind the contrasts:

| Tier | d01 keyed-class rate (judge-A) | d01 keyed-class rate (judge-B) | d01 rationale quality 0-2 (judge-A) | d05 mean CSR |
|---|---|---|---|---|
| Haiku 4.5 | 0.847 | 0.979 | 1.86 | 0.909 |
| Sonnet 5 | 0.908 | 0.938 | 1.93 | 0.927 |
| Opus 5 | 0.990 | 0.959 | 2.00 | 0.927 |

Judge-B's rationale-quality means are 2.00 for all three tiers (fully
compressed at ceiling).

## 3. Pre-committed read-out 2 — per-item discrimination

| Share of items with... | d01 judge-A | d01 judge-B | d05 |
|---|---|---|---|
| mean(Opus) > mean(Haiku), strict | 0.224 (11/49) | 0.020 (1/49) | 0.194 (6/31) |
| strictly monotone Opus > Sonnet > Haiku | 0.020 (1/49) | 0.020 (1/49) | 0.032 (1/31) |

Coarseness disclosure: a 3-tier ordering has 6 permutations, and most items sit
at ceiling for all three tiers (ties), so strict shares are heavily deflated —
most items show NO strict ordering at all rather than a wrong one. The pooled
contrasts in §2, not these strict shares, are the powered read-out. d05 rows use
the 31 items scorable for all three tiers.

## 4. Pre-committed read-out 3 — parse-failure and refusal rates by tier

d05 objective compliance signals (these are judge-free and therefore carry
known-groups information that no judge can contaminate):

| Tier | d05 first-pass format failures (of 64) | d05 unscorable after one retry (of 64) |
|---|---|---|
| Haiku 4.5 | 27 (42%) | 7 (10.9%) |
| Sonnet 5 | 21 (33%) | 2 (3.1%) |
| Opus 5 | 20 (31%) | 2 (3.1%) |

Refusals: zero empty responses and zero refusal-shaped CLI results in all 486
first-pass administrations (refusal operationalized as empty completion or CLI
error result). CLI transport errors: 1 (opus; retried to success).

Judge-side parse health, for the record: judge-A returned parseable JSON for all
294 responses; judge-B produced 5 unscorable outputs (degenerate repeating-header
or looping text) out of 294 — the same failure mode named in the open v4-A
code-fix item "judge-B parse hardening", replicating on new traffic.

## 5. Pre-committed read-out 4 — cross-judge agreement on tier contrasts

The out-of-sample check on the d02 construct-disagreement crux (boot §3 fact 7):

- Design-level contrast SIGN agreement: Opus-Haiku DISAGREES (judge-A +0.143,
  judge-B -0.020); Opus-Sonnet agrees (both positive); Sonnet-Haiku DISAGREES.
- Item-level mean-score correlation between judges: Pearson 0.564,
  Spearman 0.262.
- Item-level Opus-Haiku gap correlation between judges: Pearson 0.125,
  Spearman 0.076 — essentially uncorrelated at the contrast level.
- Response-level `action_class` raw agreement: 0.896 (289 both-judged pairs).

This is the d02 crux pattern replicating out-of-sample on Claude tiers: the two
judges agree on most individual responses (0.896 raw) yet do not agree on the
construct-level ordering those responses imply — judge-B compresses everything
to ceiling (0.94-0.98 everywhere) and the residual disagreements are exactly
where the tier signal lives.

## 6. Which design shows the stronger gradient, and what that localizes

- **d05 (objective scoring): no gradient in CSR.** All three contrast intervals
  include zero and the tier means sit at 0.91-0.93 — the allocation-constraint
  items are at ceiling for all three tiers. The only objective tier signal is
  compliance-shaped, not competence-shaped: haiku fails the machine-readable
  format 42% of the time first-pass and ends 10.9% unscorable vs 3.1% for both
  larger tiers.
- **d01 (judged scoring): the gradient exists but is judge-conditional.**
  Judge-A recovers a clean monotone gradient (0.847 → 0.908 → 0.990) whose
  Opus-Haiku and Opus-Sonnet intervals exclude zero; judge-B sees no gradient
  (compressed at 0.94-0.98, slightly inverted).

Localization, per the boot's pre-committed framing: the probe was framed as "a
gradient in d05 but not d01 indicts the judges, not the items." The observed
pattern is the reverse configuration, and it splits the indictment:

1. **d05's weakness localizes to the items** — scoring is objective, so no judge
   can be blamed; the items simply lack headroom to separate 2025-2026 Claude
   tiers on constraint satisfaction. As known-groups evidence for d05 item
   validity at these capability levels, this is a null result (with the format-
   compliance gradient as a real but construct-adjacent signal).
2. **d01's weakness localizes to the judges** — one pinned judge recovers
   exactly the pre-specified known-groups ordering with intervals that exclude
   zero, which is evidence the ITEMS carry tier signal; the other pinned judge
   cannot see that signal at all. Known-groups validity for d01 is therefore
   supported conditional on judge-A and refuted under judge-B — which is not a
   contradiction but a measurement finding: the judge, not the item bank, is
   the binding constraint, consistent with the d02 re-pilot's construct-level
   disagreement crux (`20260801c`).

## 7. Limitations (disclosed, per authorization)

1. Subscription-OAuth channel is suited to modest-scale runs; this census was
   capped at the authorized 486 + convention-mandated retries and is not to be
   scaled without a new ruling.
2. No temperature/seed control in the CLI: epochs are default-temperature
   re-administrations; run-to-run noise is not separable from sampling noise.
3. ~10k tokens of constant harness overhead per call; absolute levels are not
   reference-comparable (contrasts only; never pool).
4. `--max-turns` is undocumented in CLI 2.1.220 help but parser-accepted; it was
   probed live and held constant. If a future CLI drops it silently, the
   single-turn guarantee still holds structurally (`--tools ""` leaves no tool
   to loop on), but re-verify before any rerun.
5. The reported `total_cost_usd` figures ($22.11 across all SUT calls) are the
   CLI's informational would-be API prices, not money spent — subscription OAuth
   billed $0 externally.
6. d01's binary primary collapses `partial`/`deferral`/`objective_first` into
   "not keyed"; with near-ceiling rates the contrast is carried by few items.
   The rationale-quality secondary (judge-A: 1.86 → 1.93 → 2.00) moves the same
   direction as the primary.

## 8. Spend and gates

| Block | Authorized | Actual |
|---|---|---|
| SUT administration (OAuth) | $0 external, 486-call census | $0 external (555 ledger rows + 1 flag probe; 486/486 coverage) |
| d01 judging (OpenRouter) | $1.00 hard ceiling | $0.1168 (calibration $0.003 + census; hard stop never triggered) |
| Everything else | $0 | $0 |

Gates on this artifact set: R3 claims lint 0 blockers on this file; canary
top+bottom; pytest suite 115 passed after the new tool landed (the tool is
outside the suite's import graph; nothing pinned was touched, so
`verify_instrument.py` was not required — it was nonetheless green at session
start, 51/51 on WW-v2-20260731b). New files only; no existing report edited.

**Artifacts:** harness `tools/audit/tier_probe_claude_oauth.py`; run tree
`logs/tier-probe-20260802/` (responses.jsonl, d05_scores.jsonl,
d01_judgments.jsonl, analysis.json, tallies; gitignored); this report.

**What this changes for the open program questions:** v4-T neither advances nor
closes the P-PRESSURE scope decision (still with the owner). It adds two
owner-relevant facts: (a) the construct-level judge-disagreement crux from d02
replicates out-of-sample on d01 with Claude-tier traffic, strengthening the case
that judge selection/hardening is the program's binding measurement risk before
any B1/B2 scale run; (b) the d05 public bank is at ceiling for current Claude
tiers, so known-groups arguments for d05 need harder items or a different
known-group axis.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
