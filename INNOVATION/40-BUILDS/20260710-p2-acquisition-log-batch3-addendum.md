# P2 Batch-3 Addendum — arXiv 2510.05192 — 2026-07-09 20:57

## Background: Original MISS

**Batch run:** 2026-07-09 20:51 (`p2_acquire_batch3.py`, P2-B3-12)
**arXiv ID:** 2510.05192
**Expected title keywords:** insider, risk, mitigation
**Fetched title:** "From surveillance to signalling: escalation channels as environmental controls for agentic AI"
**MISS reason logged:** topic mismatch — fetched title did not match keywords

## Orchestrator Verification Evidence

The orchestrator verified via https://arxiv.org/abs/2510.05192 and web search that
this IS the correct paper:

- **arXiv ID confirmed:** 2510.05192 maps unambiguously to a single paper
- **Author confirmed:** Francesca Gomez (sole author, consistent with gap G-16 P2 record)
- **Retitle event:** v1 title (Oct 2025): "Adapting Insider Risk mitigations for
  Agentic Misalignment: an empirical study" → v2 title (Apr 2026): "From surveillance
  to signalling: escalation channels as environmental controls for agentic AI"
- **Abstract match:** confirms insider-risk management + Situational Crime Prevention
  (SCP) + escalation channels — all core G-16 content
- **Match verdict:** SETTLED — do not re-adjudicate

## Acquisition Outcome

| Field | Value |
|-------|-------|
| Status | HIT |
| arXiv ID | 2510.05192 |
| Fetched title (v2) | From surveillance to signalling: escalation channels as environmental controls for agentic AI |
| v1 title | Adapting Insider Risk mitigations for Agentic Misalignment: an empirical study |
| Authors | Francesca Gomez |
| Year filed under | 2025 |
| File stem | 2025-Gomez-From surveillance to signalling escalation channels as |
| Gap | G-16 |
| Priority | P2 |
| PDF magic OK | True |
| Page-1 title check | {'checked_words': ['surveillance', 'signalling', 'escalation', 'channels', 'environmental'], 'matched': ['surveillance', 'signalling', 'escalation', 'channels', 'environmental'], 'pass': True} |

## Vault Paths Created

- **PDF:** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Gomez-From surveillance to signalling escalation channels as.pdf`
- **Extract:** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2025/2025-Gomez-From surveillance to signalling escalation channels as.md`
- **Paper record:** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Gomez-From surveillance to signalling escalation channels as.md`

## Notes

- Paper record body includes a '## Former Title (v1)' section so future title-greps
  on the v1 string will hit this file.
- This addendum log is a NEW file per the project rule (no overwrite of existing
  batch-3 log `20260710-p2-acquisition-log-batch3.md`).
- Script: `INNOVATION/40-BUILDS/p2_acquire_batch3_addendum.py`
