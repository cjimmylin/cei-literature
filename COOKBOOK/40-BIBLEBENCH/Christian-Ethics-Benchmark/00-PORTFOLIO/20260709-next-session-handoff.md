# WALKWORTHY — Next-Session Handoff (written 2026-07-09)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Purpose:** single re-entry document for continuing WALKWORTHY in a clean context. Companion prompt: `20260709-next-session-prompt.md` (paste it to start the next session).

---

## 1. What WALKWORTHY is (30 seconds)

A family of **10 method-major benchmarks** measuring whether LLMs *enact* (not recite) the ethics taught in a declared corpus of 15 Christian-ethics works — chapter-level anchored, dispute-aware, behavioral-first. Root: `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/`. Scope-isolated from all sibling benches (per vault rule); differentiates only against published literature.

## 2. Authority stack (read in this order; all BINDING)

1. `00-PORTFOLIO/20260706-normative-charter.md` — whose ethics, 14-area registry, 3-stratum schema, DSP-1..12 dispute registry, tier rules, claim language. **Frozen.**
2. `00-PORTFOLIO/20260706-opus-item-playbook.md` — item recipe, lint L1–L9, five audits, per-design quick cards, review gates R1–R3. (L8 no-direct-Scripture and L9 gloss-integrity added in cycle 2.)
3. `00-PORTFOLIO/20260706-master-plan.md` — session sequence O1–O6 + **PRE-REGISTERED gates §3 (frozen 2026-07-06; execute mechanically, never re-litigate)**.
4. Per-design specs `DESIGNS/NN-<codename>.md` (with FA-1..6 + FA2-5 amendments applied).
5. Adjudication memos: `REVIEWS/20260706-fable-adjudication.md` (cycle 1) and `REVIEWS/20260707-fable-adjudication-2.md` (cycle 2, incl. §C advisory list for O1).
6. Judgment calls beyond these: file to `00-PORTFOLIO/PENDING-RULINGS.md` (create if absent), park the item, move on. Do NOT guess on charter-level questions.

## 3. Current state (as of commit `4429dce39`, 2026-07-07)

- **Item banks: 462 seeds (~503 cases incl. 41 spec exemplars), all 10 designs at doubled targets** (66/54/44/44/42/40/40/44/46/42). Every wave-2 item tagged `wave: 2` + `author_model: fable|opus` (provenance for the pre-specified author-tier discrimination analysis).
- **Quality: two full adversarial cycles discharged.** Cycle 1: 145P/68R/1K, all revisions applied. Cycle 2 (wave-2 scope): 190P/41R/0K (17.7%), all revisions applied, plus bank-wide citation-gloss sweeps. Zero stratum-b (contested tier deliberately empty). Zero L8 violations.
- **Docs/deck:** PRD, charter, master plan, playbook, 18-slide HTML deck, 14 verified anchor packs, 22 review files, 2 adjudication memos, 3 handoffs (`20260706-session-handoff.md`, `20260707-wave2-handoff.md`, this file).
- **Not done, by design:** harness code, live runs, holdout physical split, human labels, contested-tier items.
- **Known residuals** (non-blocking, listed for O1): adjudication-2 §C advisories; wave-1 gloss items flagged by the 05/09 sweeps (05: B02/B03 area-B-11; 09: R2–R9 reaches); easy-share below ~30% in banks 09 (22%) and 10 (20%); 04 motive-type monotony in areas I/M/N.

## 4. Next session = slimmed Session O1 (Opus-appropriate; no keys needed)

Work top-down; each numbered item is independently committable:

1. **HOLDOUT split.** Create `HOLDOUT/` at benchmark root; add to `.gitignore` (verify `git check-ignore HOLDOUT/x`); MOVE (never delete) every 3rd item per bank into per-design holdout files, stratified by area × difficulty × wave × author_model so both the public split and holdout keep the matrices balanced. Update each seeds file's tally block with a `holdout: N items removed` line. **Holdout never enters git.**
2. **Residual fixes** from §3: the two wave-1 gloss items in 05, the R2–R9 documented reaches in 09 (apply or explicitly defer each with reason), 10's wave-1 M03 intensity asymmetry.
3. **Easy-tier backfill** for banks 09 and 10 toward ~30% easy (author per playbook; ~4–6 items each; never soften existing keys — FC-4). Run R1–R3 self-gates on new items (two-agent rule: separate reviewer pass).
4. **Portfolio coverage matrix refresh:** regenerate the per-design × 14-area counts (public split) into a new dated STATISTICS-style file in `00-PORTFOLIO/` and check every design still holds ≥10 areas × ≥2 items *in the public split* after the holdout move (rebalance the split if not).
5. **Commit** per repo rules (atomic, dated files, no deletions — `mv` to RECYCLE-BIN only; check `git log -1` first, parallel sessions are active in this worktree).

## 5. After O1 (unchanged from master plan)

- **O2 harness** (mock-first, NO live calls): master plan §2 is the build spec. Vault has no shared runner — build fresh (Anthropic SDK + thin per-vendor adapters; keys via .env when they exist).
- **O3 pilot → O4 6-model panel → O5 frozen-gate adjudication → O6 findings + deck v2.** Pre-registered gates in master plan §3 are frozen — execute mechanically.
- **Jimmy-owed (blocking O3+):** multi-vendor API keys; ~60 items/design human labels for the judge-validity gate (§3.4); release decisions.
- **Fable-window note:** the Fable access window closes ~2026-07-11. If a Fable session runs before then, its best marginal uses are (a) adjudicating the FIRST real panel/calibration results against the gates, (b) any neutrality-gate failure, (c) PENDING-RULINGS. Item-writing and harness-building do NOT need Fable.

## 6. Standing cautions

- Session-limit kills happened twice mid-fan-out (both recovered): checkpoint-commit between phases; prefer background agents that write files incrementally.
- Anchor packs use FOUR claim-label conventions (playbook L2 note). Citation must match gloss, not just resolve (L9).
- Never edit existing dated REVIEWS/STATISTICS files (hook-enforced); new dated files only.
- All Agent dispatches carry an explicit `model=` parameter (vault tiering hook).
