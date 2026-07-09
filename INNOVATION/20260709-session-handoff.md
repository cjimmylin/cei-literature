# INNOVATION — Session Handoff

**Written:** 2026-07-09 (covers the Fable build session of 2026-07-07) · **Author:** Fable 5
**Commits:** `85d8af29f` (portfolio layer, 18 files) + `347f2afb9` (deep-dive layer, 62 files) — both pushed to `main`.
**Status:** Fable design layer COMPLETE. Nothing in INNOVATION is blocked on further Fable design work. Execution is Opus work; the hard gates are Jimmy's (keys, GPU budget, panels).

---

## What exists (80 files, all committed)

| Layer | Path | Contents |
|---|---|---|
| Orientation (frozen) | `INNOVATION/00…07` flat files | charter, field map, gap atlas G-01…G-23, ideas scan, missing-lit list (~112 items, 98 verified-absent), 10 RP briefs + portfolio overview, deliverables roadmap, **07-opus-handoff.md = the live execution queue** |
| Governance | `00-CHARTER/` | BINDING protocol (decision rights, kill-criteria adjudication, PENDING-RULINGS + PROVISIONAL rule), vocabulary (14 coined terms), re-entry playbooks, decision log DL-01…07 |
| Field detail | `10-FIELD-MAP/` | per-front deep dives A–F (each with ranked CEI entry points + watch-list triggers w/ pre-committed responses), bets registry B1–B5 + S1–S3 (score 2027-07) |
| Gap detail | `20-GAP-ATLAS/` | 23 dossiers — Fable kernels FROZEN, Opus bodies, OPUS-EXPAND checklists |
| Idea detail | `30-IDEAS/` | 23 dossiers — same model |
| Provenance | `20260707-structure-addendum.md` | records the two-layer structure |

## How work continues (this is the whole loop)

1. Read `00-CHARTER/03-reentry-guide.md`, pick your playbook (A: keys / B: credential-blocked / C: Fable-tier / D: housekeeping).
2. Work `07-opus-handoff.md` top-down within the current cycle; check items off in place (it's the one living queue).
3. **Cycle 1 is fully key-independent and is the next work**, in order:
   - **1.1 Taxonomy codes (V2)** — new Stage-4 codes (specification, scalable-oversight, aggregation/social-choice, value-formation/EM, multi-agent-dynamics) via a new dated proposal file + Jimmy sign-off. **Must precede 1.2** or acquisitions vanish into old categories.
   - **1.2 Acquisitions (V1)** — `04-missing-literature.md`, P1 table (17 anchors) first; verify ⚠-flagged IDs on arXiv before download; Sonnet-tier batch work with rate-limit discipline.
   - **1.3 `fairgold` toolkit** (RP-02 O2) — pure computation, no keys.
   - **1.4 Position paper (P3)** — draft from `01-field-map-2026.md` + `02-gap-atlas.md`; upgrade citations to VERIFIED as 1.2 lands PDFs; queue for Fable-tier/Jimmy review before any external use.
   - **1.5 RP-04 O1** — assemble frozen response corpus from existing pilot outputs (FRUITBENCH THORNS, DIMGLASS, SERMONMOUNT WITNESS).
   - **1.6 RP-01 O1** — clause registries from the two public specs (fetch current versions, stamp them).
4. Dossier deepening is always-legitimate filler work: any unchecked OPUS-EXPAND item in `20-GAP-ATLAS/` / `30-IDEAS/`. Append below kernels as `## [OPUS-EXPANSION YYYYMMDD]`; never edit kernel sections (governance §4).
5. End of session: check off handoff items, one line appended to `00-CHARTER/04-decision-log.md`.

## Binding constraints (do not relax — full list in `00-CHARTER/01-governance-protocol.md`)

- Kill criteria in RP briefs execute mechanically; softening requires a logged Fable-tier/Jimmy ruling.
- Evidence classes: external prose cites VERIFIED only; ⚠ IDs must be confirmed at download; ~25 are flagged in `04-missing-literature.md`.
- G-09 judge-corruption caveat in every judged study's methods; synthetic/mock outputs never reported as measurements.
- Report immutability: frozen docs get new dated amendment files. Living files: `07-opus-handoff.md`, `04-decision-log.md`, `PENDING-RULINGS.md` (create on first use), dossier checklists.

## Jimmy's gate list (unchanged, priority order)

1. **API keys** (Anthropic + OpenAI min; Gemini ideal as third judge family) → unblocks Cycle 2 (shared runner T1 → RP-07 HAWTHORNE run → RP-04 dogfood run).
2. **GPU-inference budget** (rented endpoints, no training) → RP-09 organism validation, RP-04 phase 2.
3. **Human raters/panels** → RP-01 O3, RP-08 Phase B.
4. **D6 licensing decision** (evidence-card corpus release) — non-blocking, high-visibility.
5. If a Fable window is ever open again: adjudicate the PR queue first, then queued gate reviews (HAWTHORNE 20-pair sample, NOGOLD dry-run transcripts, SAYDO 30-triplet sample, CONCLAVE non-negotiables registries).

## Known issues / honesty notes

- Sweep citations: top anchors fetch-verified 2026-07-07 (SpecEval, Betley EM, pairwise-calibrated, stress-testing, oversight scaling laws — all real); everything else SEARCH-CONFIRMED or ⚠. Nothing ⚠ goes external unverified.
- 2026 arXiv IDs (26xx.*) could not be independently re-verified in-session; confirm-at-download is the standing instruction.
- The four flat docs and the folder layer were authored in one session; the error-correction mechanism is the bets registry (scored 2027-07) plus the watch-list triggers in each field-map front — keep both.
- Parallel-session note: WCF-BENCH sessions were committing to the same repo the same week; always `git log -1` before committing (shared-index rule).

## One-paragraph orientation for a cold reader

INNOVATION is CEI's outer-alignment expansion: the vault measures values deeply but only at the *evaluation* stage of the alignment pipeline; the field's 2025–26 movement (model specs, no-gold oversight, social-choice aggregation, emergent misalignment/persona geometry, agentic value dynamics) happened at the other five stages. The portfolio converts CEI's real assets — psychometric benchmark craft, the CRUX contested-item engine, 14 operationalized normative traditions — into ten research programs (RP-01…RP-10) that instrument those fronts, each with pre-registered kill criteria so cheaper models can execute without diluting the science.
