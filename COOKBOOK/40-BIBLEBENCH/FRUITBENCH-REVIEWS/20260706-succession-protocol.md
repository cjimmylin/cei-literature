# FRUITBENCH Governance Succession Protocol (post-Fable window)

**Author:** Fable (main loop), 2026-07-06 · **Status:** BINDING from 2026-07-12 (when Fable-tier access lapses) until Fable-class review returns
**Problem this solves:** FRUITBENCH governance routes frozen-surface changes, D-order issuance, and gate adjudication through Fable. After ~2026-07-11 there is no Fable — without a succession rule, builds either deadlock on flags or builders start deciding frozen questions themselves (the failure mode the freeze exists to prevent).
**Scope:** FRUITBENCH v1 (`../FRUITBENCH/`) + v2 (`../FRUITBENCH-v2/`) + `FRUITBENCH-REVIEWS/` only.

## 1. Decision-rights table

| Decision class | Opus alone | Jimmy | Queue for Fable-return |
|---|---|---|---|
| Item authoring within ratified rules (incl. D-36 no-narrated-vice-goal) | ✅ | | |
| Harness implementation choices that are config-parameterized + logged | ✅ | | |
| New dated reports/artifacts (never overwriting) | ✅ | | |
| Pre-registered consequence rules firing (two-strike demotion; latch removal after S-1/S-2 verified) | ✅ cite the rule | | |
| Executing FO-8 mechanically per `20260706-fo8-gate-protocol.md` §3 | ✅ verdicts only | | |
| ANY edit to `FRUITBENCH-v2/00-registry.md` | ❌ never | ✅ ratify/defer | file first |
| ANY change to a brief's do-not-change ledger or an applied D-order | ❌ never | ✅ | file first |
| New D-order issuance | ❌ (may DRAFT) | ✅ | file first |
| Deviation from a pre-registered FO-8 threshold | ❌ | ✅ | file first |
| Attacker-persona re-norming (new version) | ❌ | ✅ | file first |
| Gate-verdict override; publishing/headline claims | ❌ | ✅ | |

## 2. The pending-rulings queue

`FRUITBENCH-REVIEWS/20260706-PENDING-RULINGS.md` — append-only. Every frozen-surface question gets an entry (PR-NN) with: the question, the evidence, the builder's proposed options (≥2, with the anchoring risk stated — which option is the builder's own implementation?), and the least-committal interim path taken. Never delete or renumber entries; resolve by appending a RESOLVED line.

**Interim-path rule (binding):** while a ruling is pending, the builder takes the least-committal path — parameterize rather than hardcode; compute and report ALL candidate definitions; gate on the already-ratified default if one exists; otherwise mark every dependent result **PROVISIONAL (PR-NN)**. A build blocked >1 session by a pending ruling proceeds on the interim path; it does not wait.

## 3. Standing rulings already ratified (do not re-litigate; cite, don't rediscover)

D-35 (G1 = attacker-primary; ensemble = diagnostic; ≥24 attacker rollouts live) · D-36 (no-narrated-vice-goal; 11-item + grievancefarm rework; paternalcrush exploratory; two-strike demotion) · D-37 (spine fixes S-1…S-10; live-mode latch until S-1/S-2; per-item D-22; G2 n/a-cells) · the 2026-07-05 gate memo's D-01…D-34 · FO-5 (no headline on simulated raters) · report immutability, no deletions, scope isolation.

## 4. Session discipline for post-window Opus builds

1. First reads: worklist §1 → this protocol → `20260706-p1-review-protocol.md` Part A (builder self-audit is mandatory pre-handoff) → the design's brief with applied D-orders.
2. Every build session ends with: self-audit evidence attached to the pilot report; a dated handoff; a review prompt for the *next* session's independent Part B–D review (Opus-executed post-window, dispositions constrained by Part D grammar — anything needing a new D-order goes to the queue).
3. Escalations to Jimmy are batched as short options memos (decision, ≥2 options, recommendation, what it blocks), not open-ended questions.

## 5. On Fable-class return

First agenda: the pending-rulings queue top-down; then ratify-or-revise any PROVISIONAL results; then a spot-audit of one post-window build chosen adversarially (the one with the most self-decided edge cases).
