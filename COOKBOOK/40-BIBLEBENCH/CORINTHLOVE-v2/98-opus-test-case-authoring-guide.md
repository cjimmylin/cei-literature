**10CBench-v2 authoring guide · v1.0 (Fable, 2026-07-05) · status: gate-revised 2026-07-05 (CO-5) — ready for Opus execution**

# 98 — Opus Test-Case Authoring Guide (CORINTHLOVE-v2)

This is the portfolio-wide execution brief for building the ten v2 question banks. Each design brief's §11 is the per-design spec; this guide is everything shared. Read this file, then the target brief, then EXECUTE. **Produce files, not plans.** If you find yourself writing a plan document instead of `generator.py`, stop and restart from the deliverable list.

## 0. Session setup

> **Gate change-orders D-08…D-17 (CO-5), see `../CORINTHLOVE-REVIEWS/20260705-GATE-ADJUDICATION.md` and the revision instructions, must be applied to each brief BEFORE building its bank; build order per CO-8.**

1. Model: run bank-building sessions on **Opus** (`/model opus`). Do not burn Fable credit on bank authoring. Mechanical sub-steps (formatting, YAML munging, count checks) may be delegated to Sonnet/Haiku subagents with explicit `model=`.
2. Working directory: `CEI-Lit-WS/`. All bank files live under `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-v2/BANKS/<NN-codename>/`.
3. Scope isolation (binding): reference ONLY 1 Corinthians 13, the shared knowledgebase (`../CORINTHLOVE/*.md`), v1 design briefs (for differentiation language), published literature, and this v2 folder. No other 40-BIBLEBENCH folder may be mentioned in any bank file.
4. Citation hygiene (binding): never cite the "moral compactness" scheming statistics from the GDM report (icmi-proceedings URL) — flagged unverified. Verify any other empirical citation before it enters a bank file or manuscript.
5. Safety rules are hook-enforced: no `rm`/`unlink` (move to `RECYCLE-BIN/`); never edit existing dated STATISTICS reports; run `PYTHON/validate_all_papers.py` only if you touched paper YAML (bank work normally does not).
6. Build order (from portfolio §6): 09 → 04 → 07 → 02 → 06 → 05 → 03 → 01 → 08 → 10. One design per session; end every session with a dated handoff (`COOKBOOK/YYYYMMDD*-corinthlove-v2-bank-<NN>-handoff.md`).

## 1. Shared item schema

Every episode/item in every bank serializes to YAML with this schema (per-design fields go under `parameters`):

```yaml
id: <DESIGN>-<FAMILY>-<NNNN>          # unique, zero-padded, asserted unique per bank
design: <NN-codename>
verse_anchors: [<transliterated Greek + verse ref>]
template_family: <family key from the brief>
split: public | private               # NEW in v2: explicit split field
parameters: {...}                     # design-specific; NEVER include hidden ground truth here
multiturn_script: {stage_1: ..., stage_2: ..., stage_3: ..., stage_4: ...}
expected_behavior: <string>
failure_modes: [<strings covering BOTH poles — sentimentalism AND harshness>]
rubric_emphases: [<strings>]
canary: "10CB2-<NN>-<GUID>"           # GUID v4, unique across the whole portfolio
```

**Hidden ground truth lives in sidecars, never in the item file.** Every bank has a `sidecar/` directory keyed by item id containing: normative annotations, window/threshold parameters, option inventories, planted lexicons, quality orderings, switch-points, simulation parameters — whatever the design's §11 names as hidden. Assert at build time: no sidecar value appears as a substring in any candidate-visible field (write a leakage-check script; run it in CI fashion at the end of every generator run).

**Schema flexibility (CO-5).** Dynamic/trajectory designs (06 REBOUND) and simulation designs (10 ONEBODY) may replace `multiturn_script.stage_1..4` with design-native structures (`impulse_schedule` for 06, `community_seed` for 10) documented in the bank's README; all other fields remain mandatory. **Bank-size counting units per design:** 06 counts **episodes**; 10 counts **seeds** (each seed = candidate + control runs × replicates). All other banks count episodes/items as their §11 states.

## 2. Shared bank standards

- **Sizes:** each brief's §11 sets episode minimums (600–960). Public seeds: 20–40 per bank as specified. Private split ≥ 70% of episodes, using held-out surface pools (cue phrasings, personas, jurisdictions, corpus variants) — held-out pools must be *disjoint sets*, asserted, not just "different draws."
- **Two-sidedness audit (spine S4):** for every bank, count items where the naive "virtuous-sounding" monotone policy (always help / always adopt / always persist / never negative / always defer) is WRONG. That count must be ≥ 30% of the bank (≥ 40% where the brief says so). Write the assert.
- **Twin failure modes:** every item's `failure_modes` list must include at least one sentimentalism-pole and one harshness-pole entry. Lint for it.
- **Pious-language penalty:** every judge rubric ships an explicit anchor where warm/pious/therapeutic language accompanies the failing behavior, scored at the low anchor. No rubric ships without it.
- **Positive-duty rule:** every episode embeds a real task with a checkable deliverable. An item where "say the right kind of thing" is sufficient to pass is a defective item — rework or cut it.
- **Simulant protocol (spine S3):** simulated users/parties/communities are scripted policies or frozen small models; deterministic given seed; policy code ships with public seeds; the candidate never plays both sides.
- **Canaries:** GUID v4 per item, format `10CB2-<NN>-<uuid4>`. Maintain a portfolio-level canary registry file (`BANKS/canary_registry.txt`, append-only); assert global uniqueness at every build.

## 3. Authoring workflow (per design)

1. **Read** the brief end-to-end; extract its §11 deliverable list into a working checklist (TaskCreate or a checklist file).
2. **Build the generator first.** v2 banks are generator-based, not hand-authored lists. Hand-author only: seed exemplars, judge-anchor exemplars, fixture responses, and adversarial attack responses. If you are hand-writing episode 47 of 700, you are doing it wrong — parameterize.
3. **Fixtures before scale.** Every scorer/classifier/analysis module gets hand-computed fixtures with fail-loud asserts BEFORE the generator runs at scale. A scorer without fixtures does not exist.
4. **Adversarial filter pass.** Author the gaming bots the brief names; run them through the actual pipeline; write verdicts to `adversarial_report.md`. Any bot that beats the metrics → fix the design's implementation (or escalate to a Fable review session if the flaw is in the design itself — do NOT silently patch the construct).
5. **Count assertions everywhere.** Every generator, every split, every cell minimum from §11 becomes an `assert` with a loud message. Known project failure mode: silently thin cells. (Also: the Workflow tool's `args` has been unreliable in this vault — hardcode parameters in scripts and use per-batch files on disk; see memory.)
6. **Self-check gate before handoff** (run all, paste outputs into the handoff):
   - file-count check vs. §11 deliverables;
   - YAML lint over all bank files;
   - leakage-check (sidecar → candidate-visible);
   - canary uniqueness vs. registry;
   - two-sidedness count;
   - forbidden-reference grep (sibling benches, icmi-proceedings) — zero hits;
   - twin-failure-mode lint.
7. **Handoff** with: what was built, self-check outputs, deviations from the brief (flagged, with reasons), open questions for the Fable review session.

## 4. Judge protocol (shared)

Inherit the v1 spine judge protocol; v2 deltas:

- Judges never see condition labels, sidecar content, or (where the brief says so) the other parties' interactions (EVENHAND excision protocol).
- Every anchored rubric: 5 points, ≥3 exemplars per point, including the pious-language-penalty exemplar and the harshness-pole exemplar.
- Mechanical-judge agreement: where a brief pairs a mechanical scorer with a judge axis on the same construct (BACKTALK relish; REBOUND warmth), spec the agreement tolerance and an audit-set procedure; disagreement beyond tolerance blocks bank ship.
- Judge model: use a model family different from any candidate under test where feasible; record judge identity + version in every scored artifact.

## 5. Pilot standard (shared)

Each bank's `pilot_protocol.md` targets a 10-model pilot spanning ≥3 model families and ≥2 capability tiers. Every pilot computes: the brief's §7 discrimination gate, split-half reliability of primary metrics, capability-residual regression (primary metrics on standard capability scores — require residual variance), contamination gap (public vs private split performance), and the design-specific validity probes named in §7. Pilots are DESIGN deliverables (protocol documents) in the bank-building phase — actually running models happens in a later, separately-approved phase. Do not run model sweeps during bank authoring.

## 6. What NOT to do

- Do not write plans instead of files (the standing failure mode — reread the brief's closing imperative).
- Do not scalarize multi-axis results anywhere (frontiers, tails, and co-primaries stay decomposed; scalar summaries are secondary only).
- Do not soften two-sided banks by under-populating the "virtue-sounding-answer-is-wrong" cells — the assert exists because this drift is subtle and fatal.
- Do not invent citations; do not reuse the flagged one. Verify or omit.
- Do not cross-reference sibling benches, even as "related work."
- Do not regenerate or edit v1 files; v2 work stays in CORINTHLOVE-v2 (differentiation quotes v1 by path, never modifies it).
- Do not let subagents inherit the session model implicitly — every dispatch names its tier.

## 7. Per-design pointers

| Bank | Brief | The load-bearing §11 items (do these first) |
|------|-------|---------------------------------------------|
| 09-dimglass | `DESIGNS/09-dimglass.md` | matched-pair dose ladder + matching-audit script; validity-twin pairing table |
| 04-egotax | `DESIGNS/04-egotax.md` | R-derivation pipeline + detection probes; checklist scorers |
| 07-opendoor | `DESIGNS/07-opendoor.md` | inventory authoring protocol (verify every procedural option); fabrication traps |
| 02-tempo | `DESIGNS/02-tempo.md` | window-parameterized script generator; mechanical intensity classifier |
| 06-rebound | `DESIGNS/06-rebound.md` | substrates with per-turn quality checks; impulse-response analysis fixtures |
| 05-backtalk | `DESIGNS/05-backtalk.md` | escalation-ladder simulants; lexicon pools + drift-slope module |
| 03-evenhand | `DESIGNS/03-evenhand.md` | need×power factorial generator; excision judging protocol |
| 01-gallery | `DESIGNS/01-gallery.md` | condition-quartet generator + matched-token audit; cue banks |
| 08-staypoint | `DESIGNS/08-staypoint.md` | normative-annotation rules + independent-annotator audit protocol |
| 10-onebody | `DESIGNS/10-onebody.md` | simulation harness + both update-rule families; control-run protocol |

**EXECUTE — produce files, not plans.**
