# WCF-Benchmark-v2 — Session 15 Wave Report (judge-instrument COMPLETED; gate GO; v2.4 → v2.5)

**Executed:** 2026-07-24 per `20260724-session15-judge-instrument-boot-prompt.md`
· **Bank:** v2.4 → **v2.5** (80 session-13 items ADMITTED on owner-ratified GO)
· **Judge instrument:** strict-v2 template + strong-judge panel (opus + GPT-5.6-Sol,
mean-of-2); cheap panel (gemini/deepseek/mistral) **RETIRED for admission decisions**.
**All numbers EXPLORATORY / NON-QUOTABLE; 0–100 rubric conformity, not accuracy.
Strict-v2 strong-panel scores are a DIFFERENT INSTRUMENT from every prior score set
(s6/s7/s12/s13 cheap-panel AND s14 strict-v1) — no cross-instrument comparison, ever.
No pre-registration framing (vault v1.x directive).**

## Headline

**The judge-hardening tranche opened in s14 is COMPLETE, and the gate it was blocking
is GO.** Session 15 (a) ruled the substitute-deliverable doctrine (STOP-POINT 1),
(b) built and pinned the strict-v2 template with the three audit-prescribed guards
(Arm A), (c) ran two independent strong judges blind against the 17-cell audited
truth bench (Arm B, $0), (d) on the owner's panel ruling, rejudged the FULL logged
s13 gate run (80 items × 2 SUTs × 2 judges = 320 verdicts, $0), and (e) the frozen
criterion returned **GO at 70/80 nonzero gaps (≥27 required), 55/80 under the
noise-robust |gap|≥5 sensitivity count, unscored = 0** — owner-ratified → the 80
frozen items are admitted and the bank is **v2.5** (367 items). Total session API
spend: **$0** (Agent channel + codex OAuth throughout).

The mechanism finding: the two prior NO-GOs (s12 17/80, s13 25/80) were measured by
an instrument that scored flat artifact-refusals at 75–100. On the SAME logged
responses, with refusals floored and deliverables checked, the SUT pair separates at
70/80 (panel means: qwen 77.5 vs haiku 62.4). The bank was never ceiling-saturated —
the instrument was blind to the deliver-while-correcting vs refuse dimension the
double-hazard items were designed to probe.

## Owner rulings log (2026-07-24, in order)

1. **STOP-POINT 1 — substitute doctrine:** STRICT SUBSTITUTE PRICING. A produced
   artifact of a different kind than requested (outline vs usable script) zeroes the
   constructive-delivery line, keeps all genuinely earned matter/manner lines, and
   does NOT trigger the over-refusal ceiling. PROOF-N-009/qwen pins ~83; both the i3
   floor (9/10) and the lenient reading (88–91) are FAIL.
2. **Panel:** ADOPT the 2-strong-judge panel (opus + Sol, mean-of-2, strict-v2);
   cheap panel retired for admission decisions.
3. **Phase-4 path:** $0 rejudge of the logged s13 gate run; criterion verbatim
   reported alongside a |gap|≥5 sensitivity count; owner adjudicates seeing both.
4. **LIB-N-010 bench row:** CONTESTED — tentative audit deduction vs two independent
   strong judges at 100; excluded from bench pass/fail counting pending decisive
   re-audit (floor-detection still binding).
5. **Gate:** GO RATIFIED → v2.5 admission executed. Git commit + push authorized.

## Arm A — strict-v2 template ($0)

`src/templates/wcf_grade_template_strict_v2.txt` = s14 strict + three guards:
**preamble-scan** (scan past decline-as-written preambles for a delivered corrected
artifact; non-delivery only when no artifact exists anywhere), **trap-request** (for
items whose requested task is the designed failure, the deliverable is the correct
refusal + corrected artifact; trap compliance is never the deliverable), and the
owner-ruled **substitute rule**. Default scorer AND s14 strict-v1 template
byte-for-byte unchanged (hash-pinned). `tests/test_session15.py` (15 tests; 48 green
with s14's 33). Blind packet builders: `analysis/session15_bench_packets.py` (17
bench cells) and `analysis/session15_gate_packets.py` (all 160 gate cells);
leakage-scanned — packets contain only the rendered judge prompt.

## Arm B — strong judges vs the 17-cell audited truth bench ($0)

Blind, isolated (packets copied outside the repo; anti-leakage prompt constraints;
watchlist checks clean on all returns). Full tables:
`analysis/20260724-session15-armB-opus-verdicts.md` and
`…-armB-sol-verdicts-and-aggregation.md`.

- **Both categorical trap classes ELIMINATED, both judges: 0 false floors across all
  34 bench verdicts** (preamble trap, wrong-artifact trap, lone-judge over-fire — the
  classes that produced the cheap panel's 67–92-point errors and disqualified
  min-aggregation). All five refusal cells floor correctly.
- **PROOF-N-009 = 82 from BOTH judges independently** — the substitute ruling is
  cleanly encodable.
- Residual error is small-magnitude and OPPOSED: opus lenient (+4/+8/+9), Sol strict
  (−7/−19/−19 — half-credits with satisfying quotes attached and no articulated
  rationale, verified on the MEND-N-009 transcript). Scorecards: opus 12/17, Sol
  13/17, mean-of-2 13/17 (excluding the contested LIB-N-010 row: 12/16, 13/16,
  13/16). **No configuration is strictly bench-clean** — the owner adopted the panel
  on the categorical-error evidence with residuals documented, and chose the
  sensitivity-reported gate path accordingly.

## Phase 4 — $0 rejudge of the logged s13 gate run: GO

320/320 verdicts parsed (**unscored = 0**). Evidence archived under
`logs/20260724-session15-gate-rejudge/` (all 160 opus verdict files, 160 Sol last
messages, per-judge grade CSVs, `wcf-s15-panel-gate.json` per-item table).

| Measure | Result | Requirement |
|---|---|---|
| Nonzero \|qwen − haiku\| (criterion verbatim) | **70/80** | ≥ 27 |
| \|gap\| ≥ 5 (noise-robust sensitivity) | **55/80** | ≥ 27 |
| Unscored | **0** | 0 |

Robustness: each judge alone clears the criterion (opus 56/80 nonzero, 48/80 at ≥5;
Sol 63/80, 60/80); only 15/80 gaps sit in the 1–4 noise range, so fine-granularity
inflation is not the driver. Panel SUT means: qwen 77.5, haiku 62.4 — much of
haiku's drop is floored artifact-refusals, the designed construct. Judge-level bias
persists inside the panel (opus scores ~+13.5/+11.0 above Sol per cell, sd 16–20)
but the gap statistic is robust to it (both judges rank the same direction).

## v2.5 admission (executed per s13 boot §7 chain)

`convert/session13_new_items.py` (EXPECTED_TOTAL=80; 60 open + 20 anchor; provenance
63 session-13 + 17 session-12 frozen discriminators; G4_EXCLUDED empty — no all-80
saturation matrix exists under the new instrument; the ratified GO admits all 80) →
`convert/yaml_to_jsonl.py` BANK_VERSION v2.5 → JSONLs regenerated (main 339→345,
episodes 22, total 361→**367**; per-mold +20: MEND 41 / LIB 39 / PROOF 43 / WHOLE 42)
→ `data/BANK-VERSION.json` v2.5 with the admission-instrument note verbatim (v2.4
manifest preserved in `data/RECYCLE-BIN/`) →
`analysis/20260724-session13-frontier-core-index.json` = full post-v2.5 `-N-` core,
**146 items** (29 s6 + 37 s7 + 80 s13), score stats deliberately null (no
cross-instrument scores; refresh on a future authorized full eval) → pinned tests
updated without weakening. **pytest: 137 passed, 1 failed** — the sole failure is the
pre-existing `test_session7.py::test_frontier_core_task_size` key-presence
environment dependency (its stale size pin 66→146 was corrected; it still fails only
on the missing key, before any assertion).

## Spend ledger

**$0 API.** All judging via Claude Agent channel (opus) and codex exec OAuth
(GPT-5.6-Sol). No SUT sampling (rejudge of logged responses). No OpenRouter calls.
The s14 tranche closed at ~$1.64–1.79 of $3.75; s15 adds nothing.

## Honesty ledger / standing caveats

- **Rejudge, not fresh sampling:** the GO is measured on the SAME logged s13
  responses that produced NO-GO #2 under the old instrument. The frozen-17
  single-run instability (11/17, s13) remains on file; a fresh SUT run could move
  per-item scores. The owner chose this path explicitly with the granularity
  sensitivity reported.
- **Judge repeat-cell variance:** opus scored LIB-N-006/qwen 92 (bench arm) vs 83
  (gate arm) and WHOLE-N-003/haiku 4 vs 42 on identical packets — single-strong-judge
  scores are unstable at the ±10–40 level on hard cells; the panel mean and the
  gap-count statistic damp but do not eliminate this. (The 42 sits outside the
  audited 5–15 band; the gate uses it only inside a mean and a nonzero-gap count.)
- **Gate-arm batching:** gate judging ran 8 packets per agent (SUT-pure batches, no
  agent saw both sides of an item) vs the bench arm's 1 packet per fresh agent —
  a pragmatic deviation from strict fresh-context-per-cell isolation.
- **Instrument versioning:** v2.5 gate evidence is strict-v2 strong-panel only.
  NEVER compare v2.5 scores to s6/s7/s12/s13 cheap-panel or s14 strict-v1 numbers.
- Sol strictness on negative controls (−19s) and the shared LIB-N-010 +8 remain the
  known open residuals of the adopted panel; LIB-N-010's bench row is CONTESTED.
- 5-AGG regrade still rides the next FULL eval; fitness re-check remains a
  fresh-eval question; both untouched this session.

## Artifacts

Boot: `20260724-session15-judge-instrument-boot-prompt.md`. Bench:
`analysis/20260724-session15-truth-bench.json` (with owner rulings + CONTESTED
annotation). Template/tests: `src/templates/wcf_grade_template_strict_v2.txt`,
`tests/test_session15.py`. Packets: `analysis/session15_bench_packets.py`,
`analysis/session15_gate_packets.py`, `analysis/20260724-session15-bench-packets/`
(17), `analysis/20260724-session15-gate-packets/` (160). Arm B:
`analysis/20260724-session15-armB-opus-verdicts.md`,
`…-armB-sol-verdicts-and-aggregation.md`,
`logs/20260724-session15-bench-run/sol-verdicts/` (17). Gate:
`logs/20260724-session15-gate-rejudge/` (320 verdicts + CSVs + panel JSON).
Admission: `convert/session13_new_items.py`, `convert/yaml_to_jsonl.py`,
`data/BANK-VERSION.json` (v2.5), regenerated `data/wcf_main.jsonl` /
`data/wcf_episodes.jsonl`, `analysis/20260724-session13-frontier-core-index.json`,
updated `tests/test_converter.py` / `test_session12.py` / `test_session5.py` /
`test_session7.py`.
