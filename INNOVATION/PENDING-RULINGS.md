# PENDING-RULINGS — INNOVATION

**LIVING FILE — created 2026-07-09 (first use), per governance protocol.** Queue for decisions above the executing session's tier. Format follows the succession-protocol pattern: PR-NN, what's blocked, options, recommendation, who decides. Executing sessions may NOT self-approve items here.

---

*(no open rulings)*

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
