# WCF-Bench — G6 Confessional Panel

**Date:** 2026-07-09 · **Author:** opus · **Governing:** shared-spine §7 (gate G6)

`g6-panel.html` is the rating instrument for **gate G6**: a WCF-Bench gold label is
valid only at **≥85% consensus among confessionally-literate raters** (ministers /
elders / seminarians / theologians of confessional Reformed bodies). Below that
threshold an item is scored by calibrated abstention and stays `[DISPUTED]`. G6
replaces single-author (Fable/Opus) theology with rater consensus — the standing
construct-validity risk for the suite.

## What's on the panel (9 cards)

| Card | Ruling | Kind | The question |
|------|--------|------|--------------|
| LIB-C7-008 | `[DISPUTED]` + R3 | confirm | social dancing — is the strict/narrow Q139 divide genuine + parties correct? |
| LIB-C3-W202 | `[DISPUTED]` | confirm | minced oaths — genuine Q113 divide? |
| LIB-C8-W304c | `[DISPUTED]` | confirm | usury scope (need-loan interest) — genuine Q142 divide? |
| LIB-C2-W305b | `[DISPUTED]` | confirm | instruments/song — genuine element-vs-circumstance divide (WCF 21.1)? |
| AGG-C7-007 | R1 | position | adultery ordering — genuinely contested (incomparable / (b)-in-kind / (a)-by-aggravation)? |
| AGG-C3-W302 | R20 | position | formation (H1) vs frequency (H3) — is the ordering genuinely contested? |
| AGG-C5-W304 | R21 | position | willful-refusal vs drift (honoring a parent) — genuinely contested? |
| AGG-C8-W305 | R21 | position | willful-refusal vs drift (restitution) — genuinely contested? |
| MEND-C10-008 | R4 | verdict | is structure-scoring an acceptable mechanism? |

- **The scoring principle** (`../20260709-contested-item-scoring-ruling.md`): on genuinely
  contested items the benchmark does **not** grade a model correct/incorrect — that would only
  measure conformity to one Reformed sub-tradition. It measures **adherence**: disclosure that
  the matter is contested, *which* legitimate view the answer occupies, and whether it holds
  that view coherently and consistently. A settled floor (Q152; the forbidden legs) still stays
  right/wrong.
- **confirm** cards (the four `[DISPUTED]` liberty items) ask whether the item is a genuine,
  correctly-scoped intra-confessional divide (Yes → calibrated-abstention dev-set item).
- **position** cards (R1/R20/R21 aggravation orderings) ask whether the *ordering/weighting* is
  genuinely contested (Yes → the item is **position-scored**, no single gold minted) and validate
  the legitimate positions shown on the card.
- **verdict** card (R4) — the methodology question: whether structure-scoring (grade the reasoning
  structure, not the disclose-vs-refrain verdict) is the acceptable mechanism.

Each card shows the **verbatim Westminster anchors**; the `[DISPUTED]` cards show the **two named
traditions** and the **position** cards show the **legitimate views** in play, so raters judge
against the actual clause text.

## How to run the panel (coordinator)

1. **Recruit ~7 qualified raters.** Seven is the practical minimum for ≥85% to be a clean
   cut (6/7 = 85.7% passes; 5/7 fails). For the four `[DISPUTED]` items, the panel MUST
   span both named sides — at least one rater from a strict/exclusive body (RPCNA /
   Covenanter / Free Church Continuing) **and** one from PCA/OPC — or a "yes, genuine
   divide" consensus is hollow. The Aggregate tab warns if your loaded panel misses a side.
2. **Distribute `g6-panel.html`.** It is a single self-contained file — email it, or host it.
   A rater opens it (double-click; works offline, no server, no install), fills in the
   **Rate** tab (identity + all 9 cards + a one-line rationale each), and clicks
   **Export my answers** → downloads one `g6-<name>-<date>.json`. Work autosaves in their
   browser, so they can close and return.
3. **Collect** the JSON files back.
4. **Aggregate.** Open `g6-panel.html` yourself → **Aggregate** tab → drop in all the
   collected JSONs. It computes per-item consensus, applies the **≥85%** gate, shows the
   per-option breakdown + every rationale + the panel roster, and **Export consensus
   summary** writes `g6-consensus-<date>.json` (the machine-readable gold decisions).

## Feeding results back into the bank

For each item the consensus summary gives one of:

- **`confirm` item, ≥85% "genuine `[DISPUTED]`"** → ships as a calibrated-abstention dev-set
  item (`dev_set_only: true` + `disputed: true`, already marked).
- **`position` item, ≥85% "genuinely contested"** → the item is **position-scored** (a model is
  graded on adherence / coherence / disclosure, not correct/incorrect) and marked `contested:
  true` (+ the validated `positions:` map). **No single gold order is minted** — the harness must
  route it off the ordinal τ-scorer (see `../20260709-contested-item-scoring-ruling.md` §
  Consequences 2). If instead ≥85% say "settled," a single gold IS minted.
- **`verdict` item (R4), ≥85%** → structure-scoring kept (position-score the verdict) or a single
  verdict mandated, per the modal answer.
- **below 85% (any kind)** → the item stays contested (position-scored / abstention); **no single
  gold is minted** (spine §7).

These map onto rulings **R1 / R3 / R4 / R20 / R21** and the four `[DISPUTED]` legs; the frozen
surfaces (spine, R1–R23) then change only via a `[NEEDS-RULING]` entry citing the consensus
summary — the standing one being `../20260709-contested-item-scoring-ruling.md`.

## Notes

- **Privacy:** all computation is in the browser; nothing is uploaded anywhere.
- **Safety:** rater-submitted JSON is untrusted input; the page renders it via
  `textContent` only (no `innerHTML`), so a malicious file cannot inject script.
- **Provenance:** anchors quoted verbatim from `../../WCF/` sources; canary
  `WCFBENCH-CANARY-c1647-x9k4q` embedded (do-not-train). Verified render + ≥85%-gate math
  via Playwright (`screenshots/g6-panel-verify.png`).
- **Not a dashboard:** deliberately single-file/zero-dependency/offline (unlike the vault's
  CDN dashboards) because it is distributed to external raters who just open the file.
