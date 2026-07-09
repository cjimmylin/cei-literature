# Fable Adjudication — Cycle 1 Wave 1 (items 1.1, 1.3, 1.5, 1.6)

**Date:** 2026-07-09 · **Adjudicator:** Fable 5 (in-window; Playbook C, delegation mode)
**Scope:** four Opus-executed Cycle-1 artifacts, reviewed same-session. Verification performed independently in the main loop (file existence, fairgold pytest re-run: 49/49 pass, JSON validity of manifest + both registries, clause counts confirmed).

Rulings are numbered FC-N and are binding on downstream Opus sessions unless overturned by Jimmy. Jimmy-tier decisions are NOT ruled here — they are queued in `PENDING-RULINGS.md` with a Fable recommendation attached.

---

## 1.1 Taxonomy proposal (`20260709-taxonomy-stage4-codes-proposal.md`) — ACCEPTED as artifact; application gated on PR-01

- **FC-1 (routing tension, §9.1 of the proposal).** The proposal correctly declined to choose among Stage-4-only / Stage-3 mirror / gate-bypass scripting. This is Jimmy's call (standards file) → queued as **PR-01** with Fable recommendation **option (b)** (mirror the five names into Stage 3's category list). Reasoning: most target papers discuss values/alignment and will score `ethics_overall ≥ 50`, routing to Stage 3 — under option (a) the acquisitions would *still* vanish into old categories, defeating the stated purpose of sequencing 1.1 before 1.2. Option (b) is mechanical, has explicit precedent (`AI Safety & Alignment` already dual-homed in Stages 3 and 4), and changes no pipeline logic. Option (c) (apply `research_topic` regardless of gate) is cleaner long-term but alters classifier behavior for the whole corpus — defer to the vocabulary-reconciliation pass.
- **FC-2 (documented-vs-live vocabulary drift, §9.2).** Real finding, correctly scoped out of 1.1 ("Benchmarks & Datasets" documented but used 0×; live vocabulary has ≥8 undocumented codes). Converted into a new queue item (3.5 in `07-opus-handoff.md`) rather than left as a footnote. Housekeeping-tier; needs no ruling now.
- **FC-3 (no sixth reward-model code, §9.4).** Ratified. G-06 welds reward hacking to EM in the gap atlas; splitting across *Value Formation & EM* / *Scalable Oversight* follows the atlas. Revisit only if 1.2's pull surfaces ≥15 standalone RM-values papers (mechanical trigger, logged here so it isn't re-litigated).
- **FC-4 (evidence-marker vocabulary, §9.3).** The agent preserved `04-missing-literature.md`'s actual markers (VERIFIED-ABSENT / IN-VAULT / ⚠) instead of the handoff's prose vocabulary — correct behavior; the handoff wording was imprecise, the artifact is right.

## 1.3 fairgold toolkit (`40-BUILDS/rp02-fairgold/`) — ACCEPTED; A1–A6 ratified with one rider

- **FC-5.** Ambiguity resolutions A1 (plurality ties → expected credit 1/k), A2 (normalized Borda partial credit), A4 (TV point-credit ≡ proportional; divergence only for distributional models — correctly derived), A5 (missing predictions raise by default), A6 (contestedness = normalized Shannon entropy, thresholds caller-supplied): all ratified as the conservative standard readings.
- **FC-6 (rider on A3, binding on RP-02 O1).** A3 is mathematically correct: maximal lottery computed from marginal votes degenerates to plurality; non-degenerate ML needs per-annotator *rankings*. Consequence: the O1 dataset inventory must treat **ranking-level disaggregation as a first-class inclusion criterion**, else H1's aggregation-sensitivity statistic (`min_tau`) silently loses one of its five rules. This rider travels with the brief's K2 downgrade logic — if <3 datasets carry rankings, report ML-rule degeneracy explicitly rather than padding the rule set.
- Tests independently re-run this session: **49/49 pass**. No measurements were produced; tool-not-result discipline held.

## 1.5 RP-04 corpus (`40-BUILDS/rp04-corpus/`) — ACCEPTED; headline finding confirmed

- **FC-7 (provenance headline).** Confirmed and adopted: **0 re-scoreable real-model responses exist**; 10,430 response-level records are MockModelClient synthetic. The judge-bias memo (RP-04 P2) is therefore *fully* key-gated — no partial Cycle-1 version is possible or permitted. The rescoring matrix pre-registration stands as the Cycle-2 contract.
- **FC-8 (strata rulings).** Ratified: DIMGLASS = Stratum S0 stimulus (prompts, not responses); THORNS N=4 real probe = qualitative anchor only (verbatim text unrecoverable — it may never enter counts); WITNESS `scored.jsonl` = S1 machinery-validation lane only.
- **FC-9 (holdout hygiene).** Ratified with a rider: the agent correctly refused to copy DIMGLASS `private_bank.yaml` (996 holdout episodes). Rider: the copied 1,026 scoring *keys* are acceptable intra-repo, but **any external release of the RP-04 corpus must strip the DIMGLASS keys** — holdout protection travels with derived artifacts.
- **FC-10 (erratum).** The 2026-07-07 handoff's source paths were wrong: all three pilots live under `COOKBOOK/40-BIBLEBENCH/`, not the workspace top level. The frozen handoff is not edited (immutability); this memo + the corpus README are the correction of record.

## 1.6 RP-01 registries (`40-BUILDS/rp01-registries/`) — ACCEPTED; two binding riders

- **FC-11 (granularity split).** Ratified. Registering the Constitution at enumerated-unit + section-principle granularity instead of atomizing reason-based prose into invented clauses is the right refusal — interpretive paraphrase would poison O2. Binding rider: **O2 must pull full clause text from the recorded anchors**, never score from headings/excerpts alone.
- **FC-12 (K3 tripwire).** The stale-banner contradiction on the Model Spec's dated page (two authoritative currency signals vs. one "newer version available" banner) is registered. Binding rider: **re-verify Model Spec currency at O2 start** (one fetch of the root redirect + CHANGELOG top entry); if a newer version has landed, O1 re-runs for the delta before O2 scores anything.
- Both specs fetch-verified live 2026-07-09 with SHA-256 hashes — these registries are **VERIFIED-class** and may back external prose.

## Queue effects (applied to `07-opus-handoff.md` this session)

- 1.1 ☑ drafted — application + 1.2 gated on **PR-01** (Jimmy)
- 1.3 ☑, 1.5 ☑, 1.6 ☑ — done with rulings above
- 1.4 dispatched this session (draft-only; external use double-gated on citation upgrade + review)
- New 3.5: Stage-4 documented-vs-live vocabulary reconciliation (from FC-2)

## Honesty notes

- All four artifacts were produced by Opus subagents and adjudicated by Fable the same session; independent verification was mechanical (tests, JSON, counts), not a line-by-line re-derivation. The fairgold expected-values were hand-derived by the building agent; a hostile re-derivation was not performed (cost/benefit — the textbook profiles used are standard).
- The RP-01 registries' verbatim-ness was verified by the building agent's raw-curl + hash method, not re-fetched by the adjudicator.
