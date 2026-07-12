# CHARITROC bank review — 2026-07-11

**Reviewer:** fresh isolated Codex subagent (not Opus).  
**Scope:** adversarial review of scale-readiness for cheap-model qualification under the Fable A1–E rubric. No tests or network calls were run in this review. The supplied terminal evidence records 1009/1009 tests, a 684-episode generator dry run, 288/288 matched pairs with zero failures, adversarial PASS, a 1,152-row export, self-check all PASS, both live run roots valid at all scope, and zero exact-key matches.

## Verdict

**GO — scale-ready for cheap-model qualification.** No binding bank fix is identified. This does **not** authorize calibration, private execution, freeze, or final ranking. B5's frontier-model filter remains the sole standing **pre-calibration** condition; frontier/flagship OpenRouter calls were prohibited for this review, while the static adversarial filter passed 684 → 684.

## Rubric findings

### A. Generation integrity

- **A1 PASS.** `CORINTHLOVE/BANKS/07-charitroc/generator.py` is a seeded parametric generator, not a fixed item list. An independent alternate-seed check established 672/672 novel non-public rendered transcripts, zero exact/world-ID overlap, and preserved assertion coverage.
- **A2 PASS.** `design_cells.md` and `reports/selfcheck_report.md` account for all 288 private primary cells, 96 calibration cells, and 72 signal marginals; every cell is asserted at its prescribed count.
- **A3 PASS.** `README.md` places deterministic fixtures and planted synthetic recovery in Phase A before pilot scale; the supplied full-suite result is 1009/1009 and the self-check reports all required deliverables present.
- **A4 PASS.** Generator assertions cover exact split totals, cells, signals, pair registries, balance, sidecar equality, and split-disjoint pools before writes. The supplied dry run returned exactly 576 private + 96 calibration + 12 public = 684.

### B. Leakage and gaming

- **B1 PASS.** `adversarial/adversarial_report.md` tests all rendered surfaces with seven fixed policies (all AUC 0.500), two leave-one-family-out lexical models (pooled AUC 0.503/0.500; max family AUC 0.512/0.517), and metadata decoders below their caps. This full-bank screen is stronger than the rubric's 20-item minimum and found no actionable tell.
- **B2 PASS.** `lib/payloads.py` emits only four scripted turns to models and only opaque case ID, turns, and responses to judges. `reports/selfcheck_report.md` confirms all 684 payloads exclude sidecar truth and canaries; `sidecar/judge_token_map.json` is an exact 684-entry one-to-one trusted map.
- **B3 PASS.** `BANKS/canary_registry.txt` contains 1,272 append-only CHARITROC mappings (588 historical + 684 current), with no duplicate marker or malformed `10CB-07-` prefix. P3-16 documents that current prefix; canaries remain metadata-only and absent from rendered text.
- **B4 PASS.** The self-check reports 21,120 cross-split comparisons below the 0.25 four-token gate (maxima 0.222, 0.222, 0.143). `README.md` documents independently authored semantic banks, wrappers, entities, and resources, blocking trivial public-to-private renaming.
- **B5 STANDING PRE-CALIBRATION GATE.** The static filter ran with before/after counts 684/684 and caught all scripted gaming policies. The frontier pass is explicitly deferred and must pass before calibration; its absence does not block the presently authorized cheap qualification scope.

### C. Design fidelity

- **C1 PASS.** The build keeps empirical ordinal AUC, operating-point appropriateness at 1:1/3:1/10:1, D-07 stage-3 updating, legacy endpoints, and safeguard judgment separate. `README.md` and `design_cells.md` prohibit scalar collapse or substitution.
- **C2 PASS.** D-07 is separately reported; CO-1 uses native ordinal calibration without an item-parameter ship gate; CO-2's three-way counts are exact. Propagation orders P-1/P-2/P-3 are realized as asserted cell coverage, defeat-class matching, and the frozen P3-01…P3-27 decision log.
- **C3 PASS.** `matching_audit.py` enforces shared family/world/prior/pressure/gate/wrapper, exact stage-2/stage-4 identity, zero word/digit/sentence/format deltas in manipulated stages, zero stage-3 character delta, bounded stage-1 character delta, and matched defeat class. Supplied result: 288/288, zero failures.
- **C4 PASS.** Emitted-text schedules counterbalance cue source, reliability, polarity, negation, position, pending state, pointer suffix, prior, signal, and wrapper axes; generation fails on drift.
- **C5 N/A.** CHARITROC is a v1-07 bank, not a v3 bank.
- **C6 N/A.** This is not a v3 clause-registry bank and introduces no C1–C16 clause-tag surface.

### D. Measurement honesty

- **D1 PASS.** Mock/synthetic artifacts retain “harness validation, NOT a measurement.” Both live `reports/qualification.json` roots instead say “live OpenRouter qualification measurement” and explicitly deny calibration, private execution, and freeze authority.
- **D2 PASS at authoring scope.** The design specifies mechanical classification plus dual adjudication for graded/safeguard boundaries. Self-check confirms five exemplars at each of five action and three safeguard levels; opaque judge IDs preserve condition blindness. Human judgment was not falsely claimed as executed.
- **D3 PASS.** The export contract contains 1,152 complete episode-level rows (2 × 576), all 288 cells, the pinned ten-field schema, and the declared exclusions; calibration/public material cannot redefine completeness.
- **D4 PASS.** `reports/selfcheck_report.md` records a clean scope/citation scan.

The two live public-only roots are internally honest and mechanically resolved at 12/12 per model. Their AUCs are 0.4444 (GPT-5 nano), 0.6389 (GPT-5.4 nano), 0.6528 (GPT-5 mini), and 0.7361 (GPT-5.4 mini); diagnostics keep belief, action, joint updating, and cue strata separate. These are qualification signals only, not calibration or hardness-gate evidence.

## E. Negative duty

**Two strongest replication risks:**

1. An external team may not reproduce the apparent discrimination if independently authored worlds have less exact factorial balance or if CHARITROC's split-specific language banks encode generator-specific regularities that the present static baselines miss.
2. The graded action/safeguard boundary has not yet been tested under live dual-judge and human-calibration disagreement; adjudication variance could materially change operating points even when mechanical AUC remains stable.

**Uncovered concerns:** the four live qualifications are only N=12, from one routing provider and closely related model families, so they cannot establish the brief's frontier-spread claim. The exact three-field JSON response contract could also create provider-specific format effects in models outside the qualified set. Neither concern changes the cheap-qualification GO; B5 remains the only standing pre-calibration gate.
