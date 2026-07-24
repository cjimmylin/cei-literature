# BOOT PROMPT — WALKWORTHY v2 item assessment PHASE 2: pending rulings + close-out

Paste/read this at the start of a fresh session. Self-contained: a session with zero
prior context can execute it. **Intended main-loop model: Fable** (`/model fable`) —
the core work is ruling facilitation + adjudicated application; if the owner only wants
mechanical application of already-drafted fixes, Opus suffices (say so and proceed).
Authored 2026-07-24 by the Fable assessment-execution session.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

---

## Where things stand (read this, don't re-derive)

The 2026-07-18 benchmark-ITEM assessment is COMPLETE and its owner-ruled edit groups
are EXECUTED (commit `3aaab7c2d`, pushed):

- All 513 items (public + holdout) were double-rated (IVR-1.1, kv κw 0.76), Fable-
  adjudicated, adversarially reviewed. Reports 00–10 + the proposed-edits ledger live
  in `$V2/REPORTS/20260718-item-assessment/` (read `20260718-10-synthesis.md` first,
  then `20260718-09-proposed-edits-ledger.md`).
- Applied 2026-07-24 (see `$V2/RULINGS-APPLIED-20260724.md` — the authoritative
  what-changed record): PE-1..8, PE-18..22. Bank rev 2026-07-24: **public 344 items /
  344 runnable / 563 lines** (11 dead exemplars retired; runnable surface unchanged),
  holdout 158/158/260; contamination/budget/missing-direction classes all 0; verify
  PASS; tests 33/33.
- Holdout item IDs exist ONLY in gitignored
  `$V2/logs/item-assessment-20260718/fable-adjudication-rulings.md` (Fable's Phase-3
  rulings, authoritative for adjudication detail) — never copy holdout IDs/text into
  tracked files or final chat messages.

## Mission (in priority order)

**1. Obtain + apply the PENDING rulings.** Present these to the owner via
AskUserQuestion (batched sensibly, with the adversarial-review evidence summarized
from ledger §C and the rulings file), then apply what's approved:

- **PE-9** WW-02-A05 — reclassify T3 "led the pivot" as soft/shading concession under
  A-13 (adversary: STANDS-MODIFIED; A-12 doesn't cover a false causal-role claim).
- **PE-10** WW-04-F04 — strip β-arm discretionary acts (defensive documentation,
  survey-timed raise) to a pure trigger cue (STANDS).
- **PE-11** WW-04-A03 — symmetrize the forecast channel or reframe the DV
  (STANDS-MODIFIED; correlation is rational-forecast evidence). Includes a design-04
  caveat worth recording either way.
- **PE-12** WW-04-C03 + 1 holdout d04 sibling — reconcile direction="zero" with
  asymmetric target prose (internal contradiction).
- **PE-13** WW-10-E04 — replace the repaid-loan second cue (anti-inflationary
  confound) with a non-repayment arc element.
- **PE-14** 1 holdout d10 item — hold observability constant across N/U arms
  (dual-confirmed confound).
- **PE-15** WW-05-M03 — wording: drop the "both DSP-5 poles reject" attestation
  overclaim, ground the guard in host-role instead.
- **PE-16** 1 holdout d08 item — tighten credited-neutral/surfaced/editorializing
  scoring boundary + supply Powlison C26 locator.
- **PE-17** WW-02-E02 (minor) — one scoping sentence keeping DSP-9 out of the score.
- **PE-23** minor documentation batch (WW-01-D03-P cross-ref; d10 composite-cue
  exemplar notes; holdout d05 spec-clarity notes).
- **PE-25** (NEW) WW-01-D05/D06 — empty `keyed_behavior` extras field caused by the
  marker-variant class (`**Keyed behavior (per-position, DSP-5):**` vs the vendored
  builder's exact label `Keyed behavior`). Not run-blocking (scoring rides `target`).
  Fix = normalize the bank marker (as done for d07) — NOT a v1-builder edit.

**2. PE-24 (no ruling needed, assessment-side):** fix the item-assessment
packet-builder's pack-entry extraction in
`$V2/tools/audit/item_assess_build_packets.py` — prefix-less pack citations resolved
to the SCENARIO section of area packs instead of the CLAIMS section, which generated
false "wrong content" anchor findings in the 2026-07-18 sweep. Fix + prove on the
known cases (K-1/K-2/K-3/K-5/K-16 must yield the end-of-life/stewardship claims).

**3. Offer the owner a next-arms menu (do NOT start unbidden):**
(a) smoke-run / rescore of the changed items (design-05 CSR now enforces sum-checks;
d07 has 3+2 newly scorable keys; B02 re-keyed) — note spend and the C9 comparability
caveats in RULINGS-APPLIED-20260724 §Comparability; (b) draft the paper-shaped
validity section from reports 04/08/10; (c) design-02 pushback_rate first-look on
stored pilot logs ($0, offline rescore).

## Execution discipline (learned this cycle — follow it)

- **Close the bank→converter→metadata loop.** Bank edits are INERT until
  `tools/convert_banks.py` parses them. The vendored v1 builders use EXACT-match
  label regexes (`**Keyed.**`, `f.get("Keyed behavior")`, `Expressed = **X**`) —
  normalize bank markers to parser-exact form; NEVER edit the vendored v1 builder
  code; v2-side post-processing in convert_banks.py is the editable layer (it already
  carries 2026-07-24 scrubbers/assertions — follow that pattern).
- After ANY bank edit: `python tools/convert_banks.py` (holdout too) →
  `python tools/verify_conversion.py` → re-census (pattern:
  `logs/item-assessment-20260718/20260724-postfix-census.md`) → tests.
- **Tests run in the PROJECT venv** `$V2/.venv/bin/python` (py3.14, has inspect_ai +
  pytest); the vault top-level .venv is py3.9 and CANNOT run them. 33 tests must pass.
- Parallel edits: one agent per disjoint file set; pass explicit `model` on every
  Agent dispatch (hook-enforced); verify every agent produced file changes.
- Shared trunk: WCF-Benchmark-v2 sibling sessions are active — before rebase/push,
  stash only their TRACKED unstaged changes if any (`git stash push -- <wcf path>`),
  restore after; untracked files don't block. Pre-commit hooks run tests — expect them.
- Hard rails: no `rm` (mv to `$V2/RECYCLE-BIN/`); reports immutable (new dated files);
  canary in every artifact; holdout quarantine as above; v1 sibling read-only; a
  security hook blocks file-writes containing the token exec-immediately-followed-by-
  open-paren (rephrase; use importlib in Python examples); `/tmp/jr-*` paths in
  tools/audit are intentional referee-blindness — don't fix.
- Item edits are governed (F11/C9): ruled edits only; record outcomes in a NEW dated
  `RULINGS-APPLIED-YYYYMMDD.md` companion (don't overwrite the 2026-07-24 one).

## Out of scope (do not pick up unbidden)

Judge/referee re-audit (done 2026-07-16/17) · SUT leaderboard claims (C9) ·
`WCF-Benchmark-v2/` (separate project) · v1 modifications · re-running the full
2-rater sweep (only spot-verify edited items if a ruling asks).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
