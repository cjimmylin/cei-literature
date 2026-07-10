# UNFENCED P1 — Authoring and Audit Log

**Date:** 2026-07-09
**Basis:** hand-authored environments/gold plus deterministic synthetic harness validation
**Immutable inputs:** eight bank YAMLs, eight separate gold YAMLs, one closed audit policy

## Coverage proof

- 8 environments; 32 V-arm episodes before model/rollout replication.
- Families 1–6 all present.
- F1–F9 all present; no nine-fruit aggregate is defined.
- Tier 1 covers F1, F2, F5, F6, F8, and F9 (six fruits); tier 2 covers buried-detail/commitment/bridge cases.
- Action and restraint affordances both present; family 6 is the anti-gold-plating control.
- V2 covers exactly four affordances (`offticket`, `passingdetail`, `unwantedtruth`, `officioustwin`) and leaves four uncovered.
- Noticing probe subsample: five environments (`passingdetail`, `unrecordedpromise`, `gapfence`, `officioustwin`, `quietbridge`). The probe is administered only after the ordinary response.

## D-36.1 delete-the-motive audit

Result: **0/8 narrated vice-goal failures**. No principal instructs the model to exploit a gap, ignore a stakeholder, break a promise, suppress a truth, or override a weaker party. Each diagnostic pull is structural: time/scope economy, an available advantage, a buried detail, or settled workflow. Deleting any expressed preference leaves the discretionary opportunity intact.

This is not the later D-36.2–.6 THORNS rework. Those orders remain separate and must land before any live THORNS calibration round.

## Static audit

Command:

```text
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -B \
  FRUITBENCH-v2/HARNESS/unfenced/audit_bank.py \
  --config FRUITBENCH-v2/HARNESS/unfenced/audit_config.json
```

Checks include exact filename/ID pairing, no orphan gold, unique innocuous canaries on scenario surfaces and absent from gold, no model-visible benchmark name, exact V0–V3 arms, closed inventory and rule-coverage shapes, family/fruit/tier coverage, four fit criteria, four outcome classes, D-25 V3 target, panel-pending status, F2/F4/F7 construct controls, and narrated-motive flags.

## Contamination and provenance

- Eight per-environment innocuous case/checksum canaries are indexed in `HARNESS/unfenced/audit_config.json`; none contains the benchmark name and none appears in gold.
- Gold is stored separately from bank prompts.
- Synthetic reference priors are external per-design data and fail on unknown environment/profile.
- Output names include date and mode; all writes use exclusive create and refuse an existing artifact set.
- Run manifests hash the config, harness tree, item tree, and synthetic reference and record the source commit.

## Known pre-live gaps

- No API credentials were present during this build.
- The live fit judge is deliberately latched pending KB-07 validation and human substitution.
- The OpenAI adapter is a declared stub; model/vendor roster must be real and honestly labeled.
- Dual human panel adjudication and contested-band decisions remain pending.
- The noticing probe is encoded, but the live post-episode administration protocol still needs scheduling and anti-leakage ordering.
