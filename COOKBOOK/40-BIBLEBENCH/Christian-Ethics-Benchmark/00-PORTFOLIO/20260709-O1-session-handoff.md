# WALKWORTHY — Session O1 Handoff (written 2026-07-09, Opus)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Purpose:** re-entry document after **Session O1 (bank completion & holdout split) COMPLETE**. Next session = **O2 (harness build)**. Supersedes `20260709-next-session-handoff.md` (which scoped O1); that file's §2 authority stack and §5–§6 remain valid.

---

## 1. What WALKWORTHY is (30 seconds)

A family of **10 method-major benchmarks** measuring whether LLMs *enact* (not recite) the ethics taught in a declared corpus of 15 Christian-ethics works — chapter-anchored, dispute-aware, behavioral-first. Root: `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/`. Scope-isolated from all sibling benches; differentiates only against published literature.

## 2. Authority stack (unchanged; all BINDING — read in this order)

1. `00-PORTFOLIO/20260706-normative-charter.md` — construct, 14-area registry, 3-stratum schema, DSP-1..12, tier rules, claim language. **Frozen.**
2. `00-PORTFOLIO/20260706-opus-item-playbook.md` — item recipe, lints L1–L9, five audits, review gates R1–R3.
3. `00-PORTFOLIO/20260706-master-plan.md` — session sequence O1–O6 + **PRE-REGISTERED gates §3 (frozen; execute mechanically)**. **§2 is the O2 build spec.**
4. Per-design specs `DESIGNS/NN-<codename>.md` (immutable design docs of record; carry the 41 Fable exemplars).
5. Adjudications: `REVIEWS/20260706-fable-adjudication.md` (cycle 1), `REVIEWS/20260707-fable-adjudication-2.md` (cycle 2, §C advisories).
6. Judgment calls beyond these → `00-PORTFOLIO/PENDING-RULINGS.md` (still not needed this session; create on first genuine need), park the item, do not guess.

## 3. Current state (as of the O1 commit chain, 2026-07-09)

**Corpus:** 473 seed items + 41 spec exemplars = **514 cases**, split into:
- **PUBLIC = 356 items** (315 public seeds + 41 exemplars) — git-tracked, the run surface.
- **HOLDOUT = 158 items** (33.4%) — in `HOLDOUT/NN-<codename>-holdout.md`, **gitignored, never published** (charter §6.6). Perturbation/contamination use only; O2 harness must NOT load these for public runs.

**Per design (public seed / holdout / exemplars):** 01 44/22/5 · 02 36/18/4 · 03 29/15/4 · 04 29/15/4 · 05 28/14/4 · 06 27/13/4 · 07 27/13/4 · 08 29/15/4 · 09 34/17/4 · 10 32/16/4.

**Quality gates all green:**
- **Charter §3 coverage gate: PASS ×10** — every design ≥10 areas × ≥2 public items (11–13 each). Report: `00-PORTFOLIO/20260709-public-coverage-matrix.md`.
- Two adversarial cycles (145P/68R/1K, then 190P/41R/0K) + O1 fixes discharged. Zero stratum-b (contested tier deliberately empty). Zero L8 (free-standing Scripture) violations. All 10 public banks `yaml.safe_load` clean (0 failures). 0 cross-split leaks.
- Easy-share lifted to ~30% in the two flagged banks (09 24%→31%, 10 21%→31%); others unchanged (04/06 are intentionally hard-heavy by design).
- Holdout stratified by **area × difficulty × wave × author_model** — both splits preserve the pre-registered **fable-vs-opus author-tier** balance and the easy:hard ratio.

**What O1 did (commit chain, all on top of concurrent sibling-session commits):**
1. **Residual fixes** (`e53b6021e`): 05 B02/B03 owed-debt gloss re-anchored area-B 11→area-F 1/11 (precedent-bound); 10 M03 U-cue intensity rebalanced to match twin M02 (removed a delta-0 confound); 09 R2–R9 secondary-citation reaches **DEFERRED to O5** with a per-reach disposition table (in the 09 seeds revision log).
2. **Easy backfill** (`088e85b36`): +11 items (09:+5, 10:+6), all `wave: 3` / `author_model: opus`, two-agent reviewed (separate Opus R1–R3, both all-PASS; dated verdict files in `REVIEWS/20260709-*`). Main-loop L9 spot-check tightened 2 secondary anchors pre-merge.
3. **Holdout split** (`1948858bb`): 158 items moved to gitignored `HOLDOUT/`; benchmark-local `.gitignore` added.
4. **Coverage refresh** (`d7ec0bbb7`): the public-split matrix report + gate PASS.

## 4. Known residuals (carried forward — none block O2)

- **09 R2–R9 reaches**: 8 non-load-bearing secondary-citation reaches, DEFERRED to **O5's citation/rubric pass** (each backstopped by a correct primary; pre-scoped fix table lives in `DESIGNS/09-doubleedge-seeds.md` → "O1 disposition of R2–R9"). R4 (L01 Matt-18 civil-context) may need an anchor-pack claim or a Jimmy ruling.
- **03-N = 1 public item** (pre-existing singleton; 03 still has 11 areas ≥2 → charter-compliant). Candidate for a future N-area backfill.
- **04 motive-type monotony** in areas I/M/N (adjudication-2 §C; out of O1 scope, not actioned).
- Other adjudication-2 §C advisories still open: 02 S5 recovered-at-window harness gap; 06 F03 judge-certification risk (politically-polarized DSP-6 pair — certify judges on it first); 07 {challenged}-window phrasal tic + D-cluster.

## 5. Next = Session O2 (harness; NO live calls)

**Build spec = master plan §2.** Deliverables:
- Manifest-driven runner (`runs/YYYYMMDD-<panel>/manifest.json` lists item IDs only — text loaded from files at call time; fixed permutation seeds as constants). The vault has **no shared runner** — build fresh (Anthropic SDK + thin per-vendor adapters; keys via `.env` when they exist).
- Per-design executors: single-turn (01/03/04/05/08/10); scripted multi-turn w/ branch tables (02/07); paired-session isolation, order-permuted (03/04/09/10); arbiter probes (09).
- Judge layer: per-category rubric prompts assembled from item YAML + spec §4; **2 cross-family judges**; disagreement logged not averaged.
- Refusal detector (four-way taxonomy) on every response; strict output-block parsers (05 allocations); one-retry rule; non-compliance logged as data.
- **Load the PUBLIC split only.** Never point the harness at `HOLDOUT/`.
- Deliver: dry-run on mock clients for all 10 designs end-to-end; validate output schemas; list the fixed capability battery for the §3.3 gate BEFORE any WALKWORTHY score exists.

Then O3 pilot → O4 6-model panel → O5 frozen-gate adjudication → O6 findings/deck v2. Pre-registered gates (master plan §3) are frozen — execute mechanically.

## 6. Blocked on Jimmy (unblocks O3+)

Multi-vendor API keys; ~60 items/design human labels for the judge-validity gate (§3.4); release decisions. **O2 needs none of these** (mock-first).

## 7. Standing cautions

- **This worktree has ≥3 concurrent sessions** (INNOVATION, DUPLEX/COOKBOOK, taxonomy) committing to the shared git index. HEAD moved 4× during O1. Always `git log -1` before staging; stage WALKWORTHY paths explicitly; never rewrite sibling commits.
- Repo rules: no deletions (mv to `RECYCLE-BIN/`); `HOLDOUT/` + `*-DRAFT.md` gitignored; new reports = new `YYYYMMDD-` files; edits to existing dated `STATISTICS/REVIEWS` are hook-denied.
- Anchor packs use FOUR claim-label conventions (playbook L2). Citations must match gloss, not just resolve (L9) — cycle-2's dominant defect.
- `HOLDOUT/` lives only on this disk. It is **not recoverable from git** — if the working copy is lost, the split must be re-derived from the pre-split seed history + the held-ID lists in each seed file's "## HOLDOUT split" note.
- **Fable-window note:** window closes ~2026-07-11. If a Fable session runs before then, its best WALKWORTHY use is adjudicating the FIRST real panel/calibration results against the gates (§3), or any neutrality-gate failure — NOT harness-building (O2 needs no Fable judgment).

## 8. O1 commit chain
`e53b6021e` (residual fixes) → `088e85b36` (easy backfill) → `1948858bb` (holdout split) → `d7ec0bbb7` (coverage matrix) → this handoff. All interleaved with concurrent sibling-session commits; WALKWORTHY paths were staged explicitly each time.
