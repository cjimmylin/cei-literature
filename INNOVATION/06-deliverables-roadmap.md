# Deliverables Roadmap — Beyond Benchmarks

**Author:** Fable 5 (main loop) · **Date:** 2026-07-07
**Scope:** what CEI can *ship* from the INNOVATION portfolio besides benchmark banks — papers, datasets, standards, tools, and community artifacts — sequenced by effort and dependency. Program-internal deliverables live in each RP brief; this doc is the cross-portfolio view plus items belonging to no single program.

---

## 1. Publications ladder (fastest → slowest)

| # | Deliverable | Source | Effort | Gate |
|---|------------|--------|--------|------|
| P1 | **Hawthorne-delta short paper** — claim the term + method | RP-07 | S (machinery exists) | keys |
| P2 | **Judge-bias memo → methods paper** — first systematic judge audit of a values-benchmark portfolio | RP-04 phase 1 | S | keys (partial: cached outputs usable now) |
| P3 | **Field position paper: "Measurement is the missing half of outer alignment"** — the field-map + gap-atlas argument, public version | 01/02 docs | M (mostly written — needs citation hardening from 04 acquisitions) | none |
| P4 | **NOGOLD study** — oversight protocols on contested ground | RP-03 | L | keys + harness |
| P5 | **SEISMOGRAPH instrument paper** | RP-09 | L | GPU-inference lane |
| P6 | **SPECGRADE audit report + validation paper** | RP-01 | L | keys |
| P7 | **Aggregation-invariance study** | RP-02 | M | disaggregated datasets |
| P8 | **SAYDO / DRIFTLAB / CONCLAVE / COMMONS papers** | RP-06/05/08/10 | XL | per-brief gates |

The ladder is deliberate: P1–P3 are achievable in the first post-window Opus cycles and establish the vocabulary (Hawthorne delta, spec grading, no-gold validity) that the larger papers then inhabit.

## 2. Datasets & public artifacts

- **D1 — Spec clause registries** (RP-01): both public specs decomposed; useful to others immediately; low effort; also the substrate for D2.
- **D2 — Frozen NOGOLD item set** (RP-03): consensus-stratified value conflicts; the field has no public no-gold substrate — this is the highest-external-value dataset CEI can release.
- **D3 — SEISMOGRAPH battery + norms** (RP-09): the adoption play.
- **D4 — RM value-profile dataset** (RP-04).
- **D5 — Disaggregated-label benchmark inventory** (RP-02): cheap, useful, citable.
- **D6 — The evidence-card corpus itself**: the COOKBOOK's 677 adversarially-audited cards + 965 benchmark characterizations are publishable as a resource ("a curated map of values-alignment evaluation") — currently internal-only. Decision needed from Jimmy on licensing/attribution before any release.

## 3. Standards & methodology exports

- **S1 — Aggregation-sensitivity reporting standard** (RP-02) and **S2 — Hawthorne-corrected reporting** (RP-07): both land as COOKBOOK KB-01 amendments first, external proposals second.
- **S3 — NOGOLD validity criteria** (assignment-invariance family, RP-03): a reusable answer to "how do you validate judgment where no one knows the answer."
- **S4 — Tradition-agent fidelity gate** (RP-08): methods contribution independent of CONCLAVE's results.
- **S5 — PRISMA-lite retrofit** for the vault's own review claims (carried over from the competitive-analysis council's top gap; do it once, cite it forever).

## 4. Tools

- **T1 — Shared live-model runner** (portfolio prerequisite #1): one thin, vendor-agnostic runner with caching + logging, replacing per-project re-wiring. Build once in the first post-window Opus session that has keys; every RP consumes it. (Respect FRUITBENCH live-mode hard-block: the runner is infrastructure; each program's live use still passes its own gates.)
- **T2 — `fairgold` rescoring toolkit** (RP-02, key-free — good credential-blocked-period build).
- **T3 — Spec-diff auditor** (RP-01's recurring low-cost artifact: graded report per spec revision).

## 5. Community / visibility (Jimmy-decision items, listed not assumed)

- **C1 — Workshop proposal**: "Measurement for Values Alignment" (NeurIPS/ICLR workshop cycle) — the portfolio is a natural organizing spine; heavy on Jimmy time; decide after P1–P3 exist.
- **C2 — Public dashboard**: Hawthorne deltas / spec-adherence / drift curves as a maintained public artifact (the vault's dashboard craft applies; "fat data, thin client" architecture ready).
- **C3 — Collaboration pitches**: EM groups (RP-09 K3 path), open-pipeline teams (RP-04 phase 3), deliberation orgs (RP-08 phase B). Draft one-pagers only after the corresponding internal result exists.

## 6. Vault-internal deliverables

- **V1 — Execute `04-missing-literature.md`**: ~98 verified-absent items through `/download-pdf` → extract → classify. First post-window housekeeping cycle; Sonnet-tier work.
- **V2 — New classification fields**: the current 7-stage pipeline has no codes for specification, oversight, aggregation, EM/persona, or agentic-dynamics papers — the incoming acquisitions would classify as miscellaneous "AI Safety." Add Stage-4 topic codes (spec, oversight, aggregation, value-formation, multi-agent) before ingesting V1, or the new literature disappears into the old taxonomy.
- **V3 — COOKBOOK cross-links**: KB-06/12/13 and sketches S1/S3 get "see INNOVATION" pointers; S1 and S3 get upgrade paths (RP-05, RP-10). New-report-file discipline: amendments as new dated files, never edits to existing reports.
- **V4 — Bet review**: `01-field-map-2026.md` §6 lists five falsifiable bets (B1–B5). Calendar a review at 2027-07 — a cheap discipline that keeps the field map honest.

## 7. Sequencing summary (first three post-window Opus cycles)

1. **Cycle 1 (key-independent):** V2 taxonomy codes → V1 acquisitions begin → T2 fairgold build → P3 position-paper hardening → RP-04 O1 prep.
2. **Cycle 2 (keys arrive):** T1 runner → RP-07 run (P1) → RP-04 phase-1 run (P2).
3. **Cycle 3:** RP-03 harness + dry-run (Fable-tier transcript review if a Fable window exists; else queue per succession protocol) → RP-09 O1–O3 → RP-01 clause registries.
