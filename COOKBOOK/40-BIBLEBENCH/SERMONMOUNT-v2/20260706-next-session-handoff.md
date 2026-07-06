# 2026-07-06 — SermonMountBench: Next-Session Handoff (clean-context entry point)

**For:** the next session continuing SermonMountBench work (expected: Opus build session per the Fable-week tiering protocol — Fable planned and gated; Opus builds).
**State as of this handoff:** everything designed, gated, committed, and pushed (`358cea5a5` on `main`). Nothing built or piloted. Zero uncommitted SermonMountBench files.

---

## 1. Read these, in this order (they are the context — do not skim past 1–3)

1. `20260706-opus-gate-corrections-workorder.md` — **the work order. §2 is your first job** (eight explicit v1-card edits implementing gate recs R-1…R-7, pre-authorized by Fable — apply verbatim, add the `(gate memo 2026-07-05, R-n)` markers, verify per its §4). §3 = standing directives; §5 = the per-session loading protocol for all subsequent work.
2. `00-REGISTRY-sermon-principles.md` — the frozen S01–S40 construct codebook every brief cites. FROZEN; never edit.
3. The design brief you are building (start = `DESIGNS/09-witness.md` unless the user redirects; see §3 below). Its §7 is your work order; §2/§8 are LOCKED.
4. `COOKBOOK/00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` + the brief's flagged specialist KB docs (header line).
5. `02-OPUS-AUTHORING-GUIDE.md` — file conventions, shared core ledger, six-stage pipeline, judge/panel rules.
6. Reference only as needed: `01-PORTFOLIO-overview.md` (orthogonality boundaries, LOCKED/FREE), `20260705-fable-adversarial-gate-v1-v2.md` (why things are the way they are), `20260705-sermonmount-v2-handoff.md` (original design-session handoff).

## 2. What exists (one paragraph)

Two gated portfolios: **v1** (`../SERMONMOUNT/DESIGNS/` — ten unit-anchored designs, one Sermon pericope each) and **v2** (this folder — ten whole-passage designs, one unique methodology each: WITNESS, CROSSWINDS, TESSERA, SCRIBE, PLUMBLINE, LEDGER, CANTICLE, GLEANING, PILGRIM, VILLAGE), sharing the frozen S01–S40 registry and a 2026-07-05 adversarial gate (20/20 GO; all v2 fixes already applied in-brief and marked "gate"; v1 fixes are pending YOUR §2 job).

## 3. The queue (top-down)

1. **Apply work-order §2** (v1 amendments) → verify (§4) → commit atomically citing the gate memo.
2. **Build `DESIGNS/09-witness.md`** — first v2 build; it authors the shared scenario-core seed stock (`SHARED/core-ledger.jsonl`, guide §3) that designs 02/05/06/08 reuse. Produce FILES: 30 pilot cores + 4 renderings each, rendering pipeline + matching audit, format-control battery, M-ACT sandbox, P1 run, dated P1 report. STOP at the brief's gates for Fable review.
3. **Start panel recruitment kits** during the WITNESS build (theologian 8-tradition + secular standards; one panel serves v1 AND v2 — guide §6).
4. If the user wants the cross-version slate instead: v1-03 PLAINYES → v2-09 WITNESS → v1-06 LOGSPECK → v2-02 CROSSWINDS → v1-01 BLESSED (gate memo §5).
5. Never start VILLAGE (v2-07) before two other v2 designs pass P1 (gate condition, in its brief).

## 4. Hard rules (violations = redo)

- **Scope isolation:** sources are ONLY the SERMONMOUNT corpus (`../SERMONMOUNT/*.md`), v1 DESIGNS (differentiation), `COOKBOOK/00-KNOWLEDGEBASE/`, and published literature. NO sibling benchmark folders, ever. Pre-commit check: `grep -riE 'corinth[l]ove|tencommand[m]ents|fruit[b]ench' .` → zero hits.
- **LOCKED vs FREE:** registry, methodology definitions, falsification conditions, headline metrics, boundaries, differentiation claims = LOCKED (Fable review only; the work order's §2 edits are pre-authorized). Surface content, counts ±50%, judge choices, pilot scale = FREE.
- **EXECUTE, don't plan:** every session ends with files (generators, banks, audits, code, dated reports). A prose-only session failed.
- **First step of any build:** post-2026-07 literature overlap re-check (WebSearch) for that brief's §8 claims; report drift to Fable, don't silently rewrite.
- **No Sermon/registry/confessional language in any prompt shown to tested models** (except SCRIBE, by design).
- **Vault safety:** no deletions (mv to RECYCLE-BIN/); never overwrite dated reports; new reports get fresh `YYYYMMDD-` prefixes; commit atomically and check `git log -1` first (parallel sessions share the index).
- **X-VULN floor:** no item anywhere scores "endure abuse"/"waive protection" as gold.

## 5. Session end

Write a dated session handoff in this folder (what was built, gates passed/failed, files created, next step), update the auto-memory `sermonmount-v2-portfolio-state`, and commit on user request.

## 6. Paste-ready prompt for starting that session

```
Continue SermonMountBench. Read
CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/SERMONMOUNT-v2/20260706-next-session-handoff.md
first and follow it exactly: apply the work-order §2 v1 amendments and verify them,
then build DESIGNS/09-witness.md per its §7 (files, not plans — pilot cores,
pipelines, audits, P1 run + dated report; stop at Fable-review gates). Respect the
handoff's hard rules (scope isolation, LOCKED/FREE, no Sermon language in prompts).
Work only inside COOKBOOK/40-BIBLEBENCH/SERMONMOUNT and SERMONMOUNT-v2.
```
