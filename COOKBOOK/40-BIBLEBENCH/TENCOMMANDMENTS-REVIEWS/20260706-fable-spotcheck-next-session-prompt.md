# 20260706 — 10CBench Fable Spot-Check: Next-Session Prompt

**Purpose:** paste the block below to open the next (Fable) session. It follows the completed
A/B/C revision execution (commits `0ca0665fa`, `5daef77b0`, `6b10fc2b8`, handoff `133001886`)
and drives the spot-check → TC-9 first-build-wave release. Authored by the Opus execution
session, 2026-07-06.

---

```
Continue the 10CBench (Ten Commandments benchmark) work. This is the FABLE SPOT-CHECK
session that follows the completed A/B/C revision execution. Stay on Fable — this is
adjudication/review work, not execution. Read, in this order:

1. CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/TENCOMMANDMENTS-REVIEWS/20260706-session-ABC-execution-handoff.md
   (what was executed, the delegated author's-choice, and the agent-flagged judgment calls)
2. CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/TENCOMMANDMENTS-REVIEWS/20260705-GATE-ADJUDICATION.md
   (binding law: §1 dispositions, TC-1..TC-12, §5.4 spot-check instruction)
3. CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/TENCOMMANDMENTS-REVIEWS/20260706-revision-orders.md
   (the executed orders + the §A/§B/§C acceptance greps)

What was executed by the prior Opus session (all pushed to origin/main):
- A (v1) = commit 0ca0665fa: 2 new scaffolds 09-WITNESS + 10-APPETITE (from locked §A.0
  specs) + §A.1 gate fixes to 01-08 + portfolio.
- B (v2) = commit 5daef77b0: B.1 cross-file (TC-2/4/6) + B.2 per-design gates to 01-10 + portfolio.
- C (v3) = commit 6b10fc2b8: 00b-inheritance-registry (TC-7) + C.1/C.2 to 01-10 + portfolio.
- Handoff = commit 133001886.

SPOT-CHECK PROTOCOL (adjudication §5.4). This is REVIEW, not re-editing:
A. MANDATORY end-to-end reads (judgment-critical — read yourself, do not delegate):
   - v1 09-witness-no-false-witness.md and v1 10-appetite-no-coveting.md — verify they
     faithfully implement the LOCKED §A.0 specs, are born gate-compliant (numeric
     falsifications, X2, X4 power, X6-scoped novelty, TC-6 arithmetic), and that the
     registered SOVEREIGN↔APPETITE cross-analysis + unblind rule are correct.
   - v3 00b-inheritance-registry.md — it is the single source of truth; verify the C9/C10
     narrowing disclosures, the class-1 TC-8(a) note, and that the C1–C8 "source inferred"
     rows and the TABLETS/CASUIST exclusions are acceptable.
B. Read one revised design per session against the memo. RECOMMENDED: prioritize the
   TC-9 first-wave designs since they build next — SOVEREIGN (v1 01, the L1/L2-P0 split +
   BF≥10), PALTER (v2 09, Spearman≥0.6 gate), ZEROSUM (v2 10), SKIM (v2 08), TABLETS
   (v3 01, BT-within-tier + 270 quota). Scale depth to your appetite.
C. Re-verify the §A/§B/§C acceptance greps (you may delegate the mechanical re-grep to a
   Sonnet agent; keep the judgment reads yourself).

TWO DECISIONS THAT NEED YOUR RULING:
1. 06-UPSTREAM MR construct (R2-F6) — the execution session took the adjudication-authorized
   "author's choice" and chose RENAME to "legal-taxonomy calibration" (execution-safe) over
   the legal↔moral divergence-arm option. CONFIRM the rename, or order the divergence arm
   (the memo notes it's cheap via PROVENANCE's legality×morality machinery). Read 06-upstream
   before ruling.
2. The agent-flagged TC-2 "at ceiling" operationalizations and the TC-4 scoping (gate
   thresholds deliberately NOT tagged "descriptive") — confirm or correct (handoff lists them).

DEFECT RULE: trivial drift → note a one-line correction and fix in place; substantive drift
from a LOCKED spec → write a dated correction-order doc for a follow-up Opus session (do not
turn this Fable session into an execution session).

RELEASE GATE: if the spot-check passes, RELEASE the TC-9 first build wave by writing a new
dated build-release memo in TENCOMMANDMENTS-REVIEWS/ that: (a) greenlights bank-building
sessions for ZEROSUM → SKIM → PALTER → TABLETS → SOVEREIGN with each design's entry gate
(PALTER BT gate early; TABLETS panel recruitment starts immediately; SOVEREIGN L2-P0 first,
then L1); (b) starts the TC-12 casuistry-panel recruitment plan (TABLETS+CASUIST share);
(c) notes the co-registration memo owed before TABLETS builds (TABLETS×CRUX).

RULES: scope isolation — Ten Commandments folders + 00-KNOWLEDGEBASE + the 20-DESIGNS
adjudication memo only; never read sibling benches. Reports/logs get NEW YYYYMMDD- files
(never overwrite). No rm (RECYCLE-BIN only). Parallel sessions share the git index — check
`git log -1` and intersect changed paths before staging; stage only files you changed; commit
atomically; push after commit. Write a handoff at the end.
```

---

## Author notes (two deliberate deviations from the literal orders, for the operator)

- **Recommended spot-checking the five first-wave designs** rather than the literal
  "one revised design per session" minimum — the first-wave five (SOVEREIGN/PALTER/ZEROSUM/
  SKIM/TABLETS) are exactly what build next, so checking them is the highest-leverage use of
  the pass. Framed as "scale depth to your appetite" so it doesn't over-constrain Fable.
- **Made the release action concrete** (a dated build-release memo with entry gates + panel-
  recruitment kickoff + the TABLETS×CRUX co-registration note), because "release the wave" is
  otherwise underspecified; the trilogy handoff's open items (panel recruitment as the true
  critical path, co-registration notes owed before builds) are what actually gate a clean start.
