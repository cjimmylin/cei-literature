# CORINTHLOVE workstream — next-session handoff (written by Fable, 2026-07-06)

**Read this first in any fresh session continuing CORINTHLOVE work. It is self-contained: everything needed is here or one pointer away.**

---

## 1. Where the workstream stands (as of commit `53e717bbc`, pushed to main)

The CORINTHLOVE trilogy is **design-complete and adversarially gated; nothing is built yet**:

| Layer | Location (under `COOKBOOK/40-BIBLEBENCH/`) | State |
|---|---|---|
| **v1** "10CBench" — one design per love aspect | `CORINTHLOVE/DESIGNS/` (00 portfolio + briefs 01–07; 08–09 unwritten; 10-NOISYGONG SUPERSEDED, do not write) | Gated; gate amendments in portfolio §8; briefs NOT yet revised |
| **v2** — dynamics/social-embedding designs | `CORINTHLOVE-v2/` (00 + briefs 01–10 + 98 guide) | Gated; amendments in portfolio §8; briefs NOT yet revised |
| **v3** — whole-passage agentic methodologies + C1–C16 clause registry | `CORINTHLOVE-v3/` (00 + briefs 01–10 + 98 guide) | Gated; amendments in portfolio §9 + guide §7; briefs NOT yet revised |
| **Gate record** | `CORINTHLOVE-REVIEWS/` — 7 reviews (R1–R7), **`20260705-GATE-ADJUDICATION.md`** (binding memo: verdicts, CO-1…CO-12, D-01…D-27), **`20260706-OPUS-REVISION-INSTRUCTIONS.md`** (per-brief expanded edit instructions) | Complete |

Gate outcome in one line: all 27 briefs PASS-WITH-FIXES (8 reviewer BLOCKs adjudicated — none killed); the fixes are binding change-orders, fully expanded into executable edit instructions.

## 2. The work queue (strict order)

1. **Revision Session 1 (Opus):** apply §1 of `CORINTHLOVE-REVIEWS/20260706-OPUS-REVISION-INSTRUCTIONS.md` — v1 briefs 01–07 (CO-1/CO-2 on all seven + D-01…D-07 + the CO-10 crosswalk table into the v1 portfolio). End with dated handoff + verification-grep output.
2. **Revision Session 2 (Opus):** instructions §2 — v2 briefs 01–10 (D-08…D-17) + v2 98-guide CO-5.
3. **Revision Session 3 (Opus):** instructions §3 — v3 briefs 01–10 (D-18…D-27 + the ALL-TEN family-level gate wording).
4. **Focused re-review (single Opus reviewer):** v1-03 STATUSGAME only, after its D-03 revision (verify the rivalry delta now isolates framing, not incentive). No other brief needs re-review.
5. **Bank building (Opus, one bank per session), cross-version order CO-8:** ① v2-09 DIMGLASS → ② v1-07 CHARITROC → ③ v3-01 CROSSROADS → ④ v3-05 AGAPEGAME *or* v3-04 WITNESS → ⑤ v3-03 MANYMIRRORS (gated on 2-method concordance from ③–④). Each bank build follows the relevant 98 guide (`CORINTHLOVE-v2/98-…` for v2 banks, `CORINTHLOVE-v3/98-…` for v3 banks incl. its §7 interim-gate rule) plus the brief's §11.
6. Later / Fable sessions: megamatrix analysis (after ≥3 banks pilot, per v3 portfolio §9 CO-6a), any registry changes (frozen — Fable-only).

## 3. Rules that bind every session (do not rediscover these the hard way)

- **Model tiering:** revision + bank sessions run on Opus (`/model opus`); subagent dispatches always carry explicit `model=`. Fable is reserved for adjudication/design changes.
- **Scope isolation:** 1 Corinthians 13 ONLY. Never reference any sibling bench folder in 40-BIBLEBENCH (other benches exist; they are out of scope and their similarly-named files are NOT this workstream). Knowledgebase = the five docs at `CORINTHLOVE/*.md` root.
- **Citation ban:** the "moral compactness" statistics (icmi-proceedings URL, in the GDM knowledgebase doc) are unverified — never cite.
- **Safety (hook-enforced):** no deletions (move to `RECYCLE-BIN/`); never edit dated `STATISTICS/` reports; new reports get new `YYYYMMDD-` prefixes.
- **Git:** parallel sessions share the index — `git log -1` before committing; stage+commit atomically, scope-limited paths only; commit/push only when Jimmy asks.
- **Revision discipline:** targeted edits per the instructions doc, never rewrites; stamp frontmatter `status: gate-revised 2026-07-05 (D-…)`; if an instruction's target text can't be found, log the discrepancy in the handoff and skip — do not improvise.
- **Bank discipline:** generator-based authoring; fixtures + synthetic-recovery asserts before scale; adversarial-filter bots run and documented; hardness-gate logs (v3); fail-loud count asserts; sidecar rule for hidden ground truth; canary registry (`BANKS/canary_registry.txt`, formats `10CB2-`/`10CB3-`).
- **Every session ends with a dated handoff file** in `COOKBOOK/` and a memory update.

## 4. Key file map (absolute anchors)

```
CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/
├── CORINTHLOVE/                      # v1 + shared knowledgebase (5 root docs)
├── CORINTHLOVE-v2/                   # v2 portfolio, briefs, 98 guide
├── CORINTHLOVE-v3/                   # v3 portfolio (C1–C16 registry §3, gate amendments §9), briefs, 98 guide
└── CORINTHLOVE-REVIEWS/
    ├── 20260705-R1…R7-*.md           # the 7 adversarial reviews
    ├── 20260705-GATE-ADJUDICATION.md # BINDING memo (CO/D orders)
    └── 20260706-OPUS-REVISION-INSTRUCTIONS.md   # ← next session starts here
```

Prior session handoffs (context, not required reading): `COOKBOOK/20260705d-…` (v2 build), `20260705e-…` (v3 build), `20260705f-…` (gate).

## 5. Open items for Jimmy (decisions, not tasks)

- Human-rater dependencies need real recruitment before Phase-B stages: TONGUES localization consultants, CRUCIBLE standing curation panel, CROSSROADS/MANYMIRRORS key/structure validators. Protocols are specced; people are not.
- CRUCIBLE's perpetual curation is a resourcing commitment (memo D-26) — decide before its R2 cycle, not now.
- v1 briefs 08 (SECONDCHANCE) and 09 (LONGHAUL) remain unwritten — optional; nothing downstream depends on them.
