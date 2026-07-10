# PENDING-RULINGS — INNOVATION

**LIVING FILE — created 2026-07-09 (first use), per governance protocol.** Queue for decisions above the executing session's tier. Format follows the succession-protocol pattern: PR-NN, what's blocked, options, recommendation, who decides. Executing sessions may NOT self-approve items here.

---

### PR-02 — CLI-OAuth posture: ToS comfort + internal-citation boundary · **OPEN 2026-07-09** · decides: Jimmy

- **Context:** `INNOVATION/20260709d-cli-oauth-provisional-ruling.md` (Fable, provisional) opened a GREEN/YELLOW/RED lane structure for the three OAuth-authenticated vendor CLIs. Two questions inside it exceed session tier:
  1. **ToS posture:** consumer CLIs are not marketed for bulk benchmark use. The ruling caps volumes at pilot scale (≤500 calls/family/session). Is Jimmy comfortable with this posture at all, and with the caps as set?
  2. **Internal-citation boundary:** may *internal* frozen verdicts cite `cli-oauth-provisional` judge-pilot results before API replication, or is provisional data quarantined from frozen surfaces entirely? (External claims are already NEVER — that part is not open.)
- **Blocked without ruling:** nothing immediate (GREEN/YELLOW work proceeds under the provisional ruling); a NO on (1) retroactively halts the lane.
- **Options (2):** (a) full quarantine — provisional data never cited by frozen verdicts; (b) cite-with-flag — allowed if marked provisional + replication obligation attached.
- **Fable recommendation:** (a) full quarantine. The vault's core failure mode (SERMONMOUNT lesson) is provisional numbers hardening into load-bearing facts; cite-with-flag invites exactly that.

---

### PR-03 — Stage-4 vocabulary reconciliation: A+C hybrid standards patch (v1.6) · **OPEN 2026-07-10** · decides: Jimmy

- **Context:** `INNOVATION/20260710-stage4-vocab-reconciliation-proposal.md` (Lane D2, handoff item 3.5), grounded in fresh inventory `INNOVATION/20260710-stage4-vocab-inventory.md` (Lane D1). Decisive finding, Fable-verified against source: the live classifier `PYTHON/classify_non_ethics_topics.py` hard-codes the "undocumented" Stage-4 codes in its `TOPIC_CATEGORIES` dict (+ `Other` fallback, + priority-boost for Truthfulness/Bias/Safety) — **the standard is the stale artifact, not the corpus.** The standard's 12 documented codes and the classifier's 12 emitted codes are two different sets of twelve.
- **Blocked without ruling:** application of the 3-patch edit to `_OPERATING-SYSTEM/Standards/classification-logic.md` (§6 of the proposal: document the 6 code-emitted codes + `Other`; rename "Computer Vision" → "Computer Vision & Multimodal"; drop dead "Benchmarks & Datasets"; retain the 5 v1.5 codes as annotated forward vocabulary; fold in deferred Patch D header bump 1.0 → 1.6 + history row). Standards file = Jimmy sign-off; the executing session did NOT apply it.
- **Options (3):** (a) apply the A+C hybrid as drafted — standards-only, **0 paper files touched, no migration script**; (b) additionally elect Option B re-routes (≤16 legacy-tagged files, each a content judgment call; guarded script in proposal §7); (c) defer.
- **Fable recommendation:** (a). Screened 2026-07-10: classifier claims verified against source; all three patch Find-anchors match the standard verbatim (lines 3, 314–327, 863); zero YAML-batch risk; does not re-open PR-01. One annotation for the record: the patch's "0 live usage" note on the 5 v1.5 codes refers to Stage-4 `research_topic` fields only — those codes ARE in live use in Stage-3 `ethics_perspective`/`newtags` on the ~60 INNOVATION acquisition records (ethics_overall ≥ 50 papers route to Stage 3 by design). Do not read "not yet emitted" as "inert."

---

*Resolved rulings move to a `## Resolved` section below with date + outcome; never delete.*

## Resolved

### PR-01 — Stage-4 taxonomy codes: sign-off + routing placement · **RESOLVED 2026-07-09** · decided: Jimmy

- **Ruling (Jimmy, verbatim intent):** all 5 codes approved as drafted; routing option **(b)** (mirror into Stage 3, dual-homed) selected; apply and unblock 1.2.
- **Applied 2026-07-09 (same session, Fable-supervised):** §7 Patches A/B/C applied to `classification-logic.md` (version-history row 1.5) + Stage-3 mirror (list items 11–15, dual-homing note, matching example-keyword blocks in both stages' detection sections). `validate_all_papers.py`: 0 errors. Patch D (header `Version: 1.0` bump — pre-existing staleness) was gated separately in the proposal and remains unapplied; fold into queue item 3.5.
- **Effect:** handoff item 1.2 (Acquisitions V1) UNBLOCKED; P1 batch dispatched same session.

- **Original request (for the record):**
  - Artifact: `INNOVATION/20260709-taxonomy-stage4-codes-proposal.md` (5 new codes, ready-to-apply patch in §7)
  - Blocked: patch application (standards file) + handoff item 1.2 (~98 papers)
  - Options: (a) Stage-4-only / (b) Stage-3 mirror / (c) bypass `ethics_overall < 50` gate
  - Fable recommendation (FC-1): approve all 5; pick (b) — (a) lets papers route past Stage 4; (b) mechanical + precedented; (c) corpus-wide behavior change, deferred to item 3.5.
