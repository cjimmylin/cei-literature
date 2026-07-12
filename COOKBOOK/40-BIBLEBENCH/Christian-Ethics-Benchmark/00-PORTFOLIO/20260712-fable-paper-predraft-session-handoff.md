# WALKWORTHY — Fable Paper Pre-Draft Session Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-12 (Fable + Jimmy). **Session:** PAPER pre-draft (results-independent
sections), per `20260712-fable-paper-predraft-boot-prompt.md`. **Status at close:**
PAPER/ scaffold COMPLETE — post-results work is mechanical fill-in only.
**This file is dated-immutable.** The PAPER/ files themselves are living DRAFTs (marked
in-file), exempt from dated-immutability like the dashboard.

---

## 1. Grill outcomes (Jimmy rulings, logged verbatim in `PAPER/outline.md §0`)

| Decision | Ruling |
|---|---|
| Venue | arXiv-first preprint, venue-agnostic |
| Shape | Long-form technical report (20–40 pp) |
| Headline | The benchmark artifact itself (D&B-style) |
| Framing | Template-for-any-tradition, hedge-locked (one instantiation) |
| Results scope | Methods-first, results-light (gate/status outcomes; leaderboard deferred; fits FR-9) |
| Anonymization | Anonymizable from the start (swap block in outline §7) |
| AI disclosure | Minimal — ethics statement only (Fable flagged under-disclosure risk; Jimmy's call; methods stay honest-neutral) |

Note: the boot prompt's "grill-me skill" does not exist anywhere in the skills
directories; the grill was run directly via structured questions.

## 2. What was built (`PAPER/`, 11 files, all DRAFT)

Fable-authored: `outline.md` (claims skeleton C1–C5, each gate-tagged; fill-in protocol;
standing constraints), `00-title-abstract.md` (slots fill LAST), `01-introduction.md`
(contribution claims with `[LICENSE: …]` tags), `06-results-scaffold.md` (exact column
schemas: 6.1 FR-1 exclusions FIRST, 6.2 gate matrix + 8-status vocabulary + mandatory
footnotes, 6.3 κ/Δ(J), 6.4 G9 headlines, 6.5 per-released-design §6.1 readout blocks,
6.6 status-report mode), `07-discussion-stub.md` (pre-committed angles + ⟦O5⟧ slots),
`08-threats-to-validity.md` (incl. §8.7 falsification commitments).

Opus-drafted (model=opus agents), Fable adversarially reviewed and fixed in place:
`02-related-work.md` (5 strands, 54 WebSearch-verified refs), `03-benchmark-construction.md`,
`04-measurement-methodology.md` (the prereg spine), `05-experimental-setup.md`,
`09-ethics-statement.md` (carries the ONE full AI-construction disclosure),
`10-reproducibility.md`.

## 3. Adversarial-review corrections applied (so nobody re-introduces them)

1. **Holdout denominator:** 33.4% is of the **473 authored seed cases** (158/473), NOT of
   514 or 356. Fixed in 00/01/03/10/outline.
2. **Contested tier is EMPTY in v1** (zero stratum-b items, O1 handoff §3). Now disclosed
   in abstract, intro, §3.4 (own paragraph), §6.5 (readouts print "N/A (tier
   unpopulated)"), and §8.1 (new threat para). Standing constraint added to outline §6.
3. **Wave membership:** 04's draft cited the protocol §8 wave table — SUPERSEDED by
   FR-17(a): {02,07,01}→{03,04,05,06}→{08,09,10}. Fixed; standing constraint in outline §6.
4. Release-formula block: "verbatim" claim softened (role names anonymized); minor fixes
   ({,} artifacts, a source comment, "waved"→"wave-based").
5. Two post-cutoff arXiv IDs (2605.08556, 2603.11394) flagged in-file for manual
   confirmation pre-submission.

## 4. Fill-in protocol (post-results; who does what)

- Codex/Opus fills `06-results-scaffold.md` ⟦…⟧ placeholders ONLY from the NEW dated
  post-W3 readings file + the O5 gate-adjudication report (never `20260711b-…`,
  superseded). Every filled cell keeps its `<!-- source -->` comment.
- Abstract SLOT-A/B/C fill last; SLOT-B only for RELEASED + signed-off designs, approved
  claim-sentence forms only.
- `[LICENSE: …]` tags in 01 are stripped at submission by the sign-off holder (Jimmy).
- If the released set is small/empty, §6 publishes in status-report mode — that outcome
  is publishable as-is; do not wait.
- Paper release/submission decisions remain **Jimmy-only** (master-plan §5).

## 5. State of the parallel Codex lane (verified this session)

No Codex activity after the 2026-07-12 handoff: no W3 recompute, no O5 verdicts, no new
dated readings file. Nothing was incorporated because nothing exists yet; the scaffold
does not wait on it. Dashboard §12 (the Codex boot prompt) was NOT displaced.

## 6. Known issues / open items

- Related-work §2.2 strand is thin in verified literature (turned into a differentiation
  point deliberately) — revisit before submission for 2026 publications.
- The 12-non-runnable-sketches breakdown of the 41 exemplars is asserted per PR-1(c)
  ruling; no portfolio doc itemizes WHICH 12 — harmless for the paper (it quotes only
  clearly-marked sketches) but worth a one-line Codex listing someday.
- No LaTeX/Typst build yet — deliberate; prose-first, format at venue time.
- HOLDOUT never loaded; no runnable item text quoted anywhere in PAPER/.

## 7. On re-entry (any agent)

Read `PAPER/outline.md` FIRST (claims skeleton + constraints bind every edit). Then this
handoff §3–§4. PAPER/ files are living drafts — edit in place, keep DRAFT headers and
canary comments. Never let any section outrun what a gate can license.
