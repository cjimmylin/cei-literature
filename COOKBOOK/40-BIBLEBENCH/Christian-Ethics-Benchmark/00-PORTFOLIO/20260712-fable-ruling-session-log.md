<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — 2026-07-12 Fable ruling session: Jimmy rulings (verbatim) + FR-17 residuals

**Session:** 2026-07-12, Fable (`claude-fable-5`; authority check passed), Jimmy
present. Companion to `20260712-fable-FR16-w1-surface-ruling.md` (issued earlier this
session). This log records Jimmy's answers **verbatim** (selected option labels from the
structured question tool) and closes the residual-judgment sweep. After this session,
ALL WALKWORTHY execution moves to Codex; see the 2026-07-12 full handoff.

---

## 1. Jimmy's blocking one-liners (PR-9 items 1 & 3, C-4, C-5) — ALL CLEARED

| # | Question | Jimmy's answer (verbatim option) | Effect |
|---|---|---|---|
| R-J1 | PR-9 item 1 — 02/07 transcripts | **"Authorize re-execution (~$26.68) (Recommended)"** | NEW immutable six-SUT 02/07 re-execution authorized at the $26.681701 historical baseline; existing O4 run untouched; full-turn persistence verified against the data-contract test before the spend counts as done. PR-9 item 1 CLOSED. |
| R-J2 | PR-9 item 3 / STOP-8 — tie-breaker | **"Accept Mistral + 580-cell Part-B (Recommended)"** | `mistralai/mistral-large-2512` is the W1 tie-breaker (frozen §E fallback; no amendment). Jimmy accepts the FR-16 full-surface own-family Part-B burden: up to 225 records / 580 cells (pre-tie-breaker upper bound). STOP trigger 8 DISCHARGED. PR-9 item 3 CLOSED. |
| R-J3 | C-4 — 06/09 G5 references | **"Yes — author + Fable-review now (Recommended)"** | Two-agent (Opus) authoring dispatched this session; Fable adversarial review in-session; drafts stay gitignored pending Jimmy promotion ratification. C-4 lane UNBLOCKED. |
| R-J4 | C-5 — L7 rotation list | **"Yes — authorize (Recommended)"** | Codex authorized to formalize the machine-readable L7 name-rotation list (TDD, no live calls) while other lanes run. C-5 lane UNBLOCKED. |

## 2. Ratification sweep — ENTIRE BACKLOG RATIFIED (nothing pending)

Both sweep questions were multi-select; Jimmy selected **every** item:

| # | Item | Status |
|---|---|---|
| R-J5 | PR-1 option (c) — "356 authored / 344 runnable" everywhere | **RATIFIED** |
| R-J6 | PR-2 — `builders.ADVICE_SYSTEM` frame for 06 (and 09 arbiter probe) | **RATIFIED** |
| R-J7 | PR-3 — §6.4 interpretation (2026-07-10 ruling: engagement-override + keyed-coupled refusal branch + verdicts[0] decoupling + retro re-tag) | **RATIFIED** |
| R-J8 | PR-4 — OpenRouter is the sanctioned panel path | **RATIFIED** |
| R-J9 | PR-6 — within-tolerance mean rule (+ FR-10 strict-identity sensitivity row) | **RATIFIED** |
| R-J10 | PR-8 — FR-1…FR-15 bundle (incl. FR-3, FR-1, FR-5, FR-14) | **RATIFIED** |
| R-J11 | FR-16 — W1 full 3,172-cell surface / routing / cell-level Part-B | **RATIFIED** |
| R-J12 | W4 06-reference fixes (A01/K01/E01 relabels, re-key K01, trim D01/L03/N01) — may enter `DESIGNS/06-*.md`; 06 stays PROVISIONAL until G5 | **RATIFIED** |

Release-language debt from unratified rulings is now **zero**. PR-7 (G6 next-cycle
amendment) remains open by design — it is a next-cycle question, not this cycle's.

## 3. FR-17 — Residual rulings (Fable, delegated window; closes the Codex STOP-AND-ASK sweep)

**FR-17(a) Part-B triage order (consequence of R-J2).** The cell-level Part-B queue is
worked **wave-aligned with the Part-A label plan**: wave 1 {02, 07, 01} → wave 2
{03, 04, 05, 06} → wave 3 {08, 09, 10}; within a wave, by design number; within a
design, by item id. Rationale: G4 validation and Part-B adjudication then complete
per-design together, enabling FR-9 wave releases instead of an all-or-nothing tail.

**FR-17(b) Post-tie-breaker contested cells.** A cell still contested after the frozen
pair + tie-breaker (no two of three agree within tolerance) routes to cell-level Part-B;
if unlabeled at verdict time it stays EXCLUDED with published counts (frozen §B) and
counts against FR-1's ≤10% precondition. This is confirmation of frozen text, not new
policy.

**FR-17(c) Tie-breaker rubric identity.** The tie-breaker receives **byte-identical
rubric text** to what the frozen pair received for that unit (per the transition-package
W1 spec) — no paraphrase, no added instructions beyond the mechanical output-format
wrapper. Binding.

**Sweep result:** walking W1→W5 + framework §6 triggers with the above and R-J1..R-J12
in force, no remaining STOP-AND-ASK is reachable except the genuinely data-dependent
ones (§6 items 2–7, 10 — G5/G4/label outcomes) and §6 item 9 (release = Jimmy-only,
always). No FR-18 needed.

## 4. Net effect

- **W1 is fully unblocked** pending mechanical execution (re-execution → exporter/tie-breaker TDD → adjudication).
- Tie-breaker = `mistralai/mistral-large-2512`, explicit slug everywhere (FR-12).
- The only Jimmy-owed inputs anywhere in O5 are now **labor, not decisions**: Part-A
  labels (~25–30 h, 3 waves), Part-B labels (≤580 own-family cells + FR-17(b) residue,
  wave-aligned), 2nd-labeler recruitment (or declared test–retest), G5-reference
  promotion ratification after Fable review, and final release sign-off.

*No frozen text was rewritten. No live calls were made. FIX-MECHANICS-ONLY preserved.*
