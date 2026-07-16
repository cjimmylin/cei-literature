# Opus judge-referee (JR) meta-audit — results

**Date:** 2026-07-16 · **Session:** WALKWORTHY v2 side-session JR
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

## Framing guardrail (verbatim)

This is NOT benchmark work and adds nothing to the benchmark. "Closer to Opus" =
**reference-model concordance, not ground truth** — Opus is a stronger model,
not an oracle; where Opus sides with one judge, that is evidence about judge
character, not correctness. Results change NO judge pins, enter NO benchmark
reports, and trigger NO instrument changes without a separate explicit owner
ruling. (R1/R3 + ratified F11 govern benchmark claims; this data lives outside
that instrument entirely.) The sample is deliberately disagreement-enriched —
no pooled "overall agreement" headline is valid without the per-stratum split
adjacent.

## Protocol (as pre-committed)

Precommit memo: `20260716-jr-sampling-precommit.md` (committed `5246986fd`
BEFORE any dispatch). Frozen manifest sha256 `b2839b14…f5ef9f`, seed 20260716,
n = 942: design 07 = 392 disagreement (all) + 150 controls; design 02 = 200
disagreement (sampled; base rate 0.767) + 80 controls; design 06 = 60 top-|Δ
profile_mean| + 60 controls. Prompts exported byte-identical to shipped judge
prompts (`assemble_rubric_prompt` reused, never forked; determinism-verified;
02 = un-anchored as shipped, 07 = anchored + context-free as shipped).

**Referee channel:** blind Claude Code Opus agents (`model: opus` explicit),
OAuth subscription, **zero OpenRouter/API calls** (owner-authorized channel for
this non-benchmark meta-audit; AGENTS.md rule 3 governs benchmark measurement).
Referees received only `{prompt_sha256, prompt}` slices staged in `/tmp` — no
A/B verdicts, no repo paths, no SUT identities. Batches ladder-spread
(no two turns of one ladder per batch); within-batch non-independence remains a
documented caveat.

**Dispatch stats:** 40 dispatches (39 planned batches + 1 single-unit re-ask
after one referee skipped a unit). 942/942 verdicts ingested, 0 hash rejects,
0 refusals, 0 hand-patches. 50 `unscorable` verdicts (5.3%), all design 07 (see
§Finding 4). ~4.1M subscription tokens across referee dispatches (~4.4M
including build/analysis agents), $0 API spend. One referee independently
flagged an embedded canary-like block inside a stored SUT response and
correctly ignored it as inert content.

Tools: `tools/audit/export_referee_prompts.py`, `make_referee_manifest.py`,
`make_referee_batches.py`, `ingest_referee_verdicts.py`,
`referee_agreement.py`. Data (gitignored): `logs/jr-referee-20260716/`
(prompts, manifest, opus-verdicts.jsonl, referee-agreement.json).

## Concordance tables (all per-stratum; judge-A = gpt-4.1-nano, judge-B = llama-3.3-70b)

### Designs 02/07 — raw agreement and Cohen's κ (unweighted)

| Slice | n | Opus↔A raw | Opus↔A κ | Opus↔B raw | Opus↔B κ |
|---|---|---|---|---|---|
| 02 / control (A==B) | 80 | 0.5125 | 0.2828 | 0.5125 | 0.2828 |
| 02 / disagreement | 200 | 0.2500 | 0.0031 | 0.2550 | 0.1035 |
| 07 / control (A==B) | 150 | 0.8800 | 0.3650 | 0.8800 | 0.3650 |
| 07 / disagreement | 392 | 0.2168 | −0.0697 | 0.5944 | 0.3091 |

### A/B-disagreement stratum — side-with rates

| Design | n | sides with A | sides with B | sides with NEITHER |
|---|---|---|---|---|
| 02 | 200 | 0.2500 (50) | 0.2550 (51) | **0.4950 (99)** |
| 07 | 392 | 0.2168 (85) | **0.5944 (233)** | 0.1888 (74) |
| 07 excl. no-keyed-text items | 274 | 0.1569 (43) | **0.7628 (209)** | 0.0803 (22) |

Direction is uniform across all 5 SUTs in both designs (07 sides-with-B range
0.53–0.69 shipped-set, 0.69–0.84 in the sensitivity slice; 02 neither-rate
range 0.38–0.60).

### Design 06 — profile comparison

| Stratum | mean profile_mean: Opus / A / B | avg category Δ O−A | avg Δ O−B | closer to A / B / equidistant |
|---|---|---|---|---|
| control | 0.778 / 0.880 / 0.908 | −0.101 | −0.130 | 23 / 11 / 26 |
| gap (top-|Δ|) | 0.648 / 0.506 / 0.833 | +0.142 | −0.186 | 27 / 32 / 1 |

Standout category: **principles** ("brings relevant norms as norms") — Opus
scores it far below both judges (Δ ≈ −0.51 vs A and B on controls; −0.53 vs B
on gap). Every other category is within ±0.15 on controls.

## Findings (descriptive language)

**1. Design 07: the A/B gap looks like judge-A character, not symmetric
ambiguity.** On turns where the judges disagree, Opus sides with judge-B
roughly 3:1 over judge-A (0.594 vs 0.217), rising to 0.763 with the defective
no-keyed-text items removed, and the neither-rate collapses to 0.08. The
dominant disagreement patterns are judge-A calling `comfort_only` (127) or
`cold_correction` (63) where judge-B and Opus both call `full_validation`.
Control-stratum concordance is high (0.880). Read: on design 07, judge-A
under-calls `full_validation` relative to both judge-B and the reference
model — consistent with the F2/2c picture of nano as the anchor-sensitive,
noisier instrument, even though 07 ships anchored.

**2. Design 02: the referee corroborates "gap = rubric/state-taxonomy
property."** Opus sides with NEITHER judge on 49.5% of disagreement turns —
an even three-way split (0.250 / 0.255 / 0.495) — and control concordance is
only 0.513 even where A and B agree with each other. No judge is vindicated;
the state boundaries themselves (`holds_line` / `soft_concession` /
`material_concession` / `full_compliance` / `pushback_with_alternative`) are
read differently by three capable evaluators. Notably, the most common
neither-pattern is Opus calling `full_compliance` where the shipped judges
chose softer states (top triples: A=pushback/B=material→Opus=full_compliance
17; A=holds_line/B=material→full_compliance 13) — the reference model reads
SUT responses as more compliant/broken than either shipped judge. This is
exactly the outcome F2 predicted if the 02 taxonomy is intrinsically
ambiguous.

**3. Design 06: Opus does NOT simply endorse judge-B's documented
generosity.** On contested (gap) completions Opus lands between A (0.506) and
B (0.833) at 0.648, splitting closer-to 27/32. On controls Opus is stricter
than both (0.778 vs 0.880/0.908). The divergence is concentrated in one
category: `principles`, which Opus scores ~0.5 points lower than both judges —
the referee reads "brings relevant norms as norms" as a much higher bar
(explicit corpus-norm invocation) than either shipped judge does. B's
generosity is corroborated as real (B > A everywhere) but not as correct.

**4. Item-level rubric defect discovered: "(no keyed text)" anchors.** 48 of
50 Opus unscorables sit on three design-07 items whose shipped per-turn rubric
anchor is literally "(no keyed text)": WW-07-L02 (19), WW-07-I04 (18),
WW-07-F02 (11). On these same units judge-A overwhelmingly says
`full_validation` while judge-B scatters toward `deflection` — i.e., with no
keyed norm to score against, the two judges fall back on opposite priors and
generate pure disagreement. Referee agents split on scorability the same way
(most declared unscorable; some scored on the shared state anchors). These
items are a mechanical disagreement generator independent of judge quality.

**5. Ledger composition.** The referee evidence REFINES F2 rather than
contradicting it: the "gap = instrument property" conclusion is corroborated
for design 02 (three-way split, low control concordance) but for design 07 the
gap decomposes into (a) a judge-A character component (under-calling
`full_validation`; Opus↔B κ 0.31 vs Opus↔A κ −0.07 on contested turns) and
(b) an item-defect component (no-keyed-text anchors). Both composites are
consistent with F-2c-3's finding that nano is the anchor-hungry, less
self-consistent judge.

## Caveats

Reference-model concordance, not ground truth (see guardrail). Sample is
disagreement-enriched by design; strata are never pooled here and must not be
pooled downstream. Single-pass referee (no self-consistency replicate).
Within-batch non-independence (≤1 turn per ladder per batch, but 23–25 units
share one agent context). Referee channel differs from shipped judges (agentic
Claude Code vs direct API), so referee/judge differences compose channel +
model effects. Design-06 gap ranking excluded 9 units with all-null judge-B
profiles (recorded in manifest-meta.json).

## OWNER DECISION HOOKS (listed, NOT executed)

1. **v-next rubric priority:** author keyed text for WW-07-L02 / WW-07-I04 /
   WW-07-F02 (+ audit WW-07-A02, WW-07-D03 turn-level gaps) — currently
   "(no keyed text)" anchors that mechanically generate judge disagreement.
2. **v-next judge choice (design 07):** referee concordance marks judge-A
   (gpt-4.1-nano) as the divergent instrument on 07; candidate actions —
   replace, re-weight, or add a third judge — are owner rulings, not taken.
3. **Design 02 taxonomy:** the three-way split says revision effort belongs in
   the state definitions (esp. the concession boundaries and
   `full_compliance` threshold), not in judge selection.
4. **Design 06 `principles` category:** decide whether the shipped judges'
   lenient reading or the referee's strict reading matches design intent;
   affects any future anchor authoring.
5. No judge pins changed; nothing here enters benchmark reports or
   comparative claims (R1/R3/C9 + RATIFIED F11 untouched).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
