# PENDING-RULINGS — INNOVATION

**LIVING FILE — created 2026-07-09 (first use), per governance protocol.** Queue for decisions above the executing session's tier. Format follows the succession-protocol pattern: PR-NN, what's blocked, options, recommendation, who decides. Executing sessions may NOT self-approve items here.

---

## PR-01 — Stage-4 taxonomy codes: sign-off + routing placement · **OPEN** · decides: Jimmy

- **Artifact:** `INNOVATION/20260709-taxonomy-stage4-codes-proposal.md` (5 new codes, ready-to-apply patch in §7)
- **Blocked on this:** application of the patch to `_OPERATING-SYSTEM/Standards/classification-logic.md` (standards file), and handoff item **1.2 Acquisitions** (~98 papers; running it first sends them into old categories).
- **Decision needed:** (i) approve/revise/reject each of the 5 codes; (ii) pick routing option from proposal §9.1: (a) Stage-4-only, (b) mirror the five names into Stage 3's list, (c) apply `research_topic` regardless of the `ethics_overall < 50` gate.
- **Fable recommendation (2026-07-09, FC-1):** approve all 5 as drafted; pick **(b)**. Under (a) most target papers route to Stage 3 and never receive the codes — defeating the 1.1-before-1.2 sequencing. (b) is mechanical and precedented (`AI Safety & Alignment` is already dual-homed). (c) changes classifier behavior corpus-wide; defer to the vocabulary-reconciliation pass (queue item 3.5).
- **On approval:** apply §7 patch (+ Stage-3 mirror if (b)), run `PYTHON/validate_all_papers.py`, then unblock 1.2.

---

*Resolved rulings move to a `## Resolved` section below with date + outcome; never delete.*

## Resolved

*(none yet)*
