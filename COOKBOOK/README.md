# CEI COOKBOOK — Values-Alignment Benchmark Knowledgebase & Design Portfolio

> Built 2026-07-05 during Fable week. Distills **620 values-alignment papers + 61 frontier-lab
> reports** (677 evidence cards, adversarially audited) and the four completed CEI meta-evaluations
> (**965 benchmark characterizations**: NormEval 54, Moral Psych 292, Religious Values 401,
> Cultural-Global 218) into a knowledgebase and design portfolio for creating **new, difficult,
> unsaturated, discriminative values-alignment benchmarks** — including multiturn and agentic
> settings beyond chat MCQs.

---

> **📊 Living dashboard: [`project-dashboard.html`](project-dashboard.html)** — the core track's
> single status page (plan since genesis, per-design tabs, session forecasts, and the prepared
> next-session boot prompt in §10). **ALL agents** — Anthropic/Claude, OpenAI/Codex, or any other
> model — read it at session start and update it in place at session end; protocol in
> [`AGENTS.md`](AGENTS.md). It is the ONE file exempt from the dated-report immutability rule.
> (Scope excludes `40-BIBLEBENCH/`, whose benches keep their own dashboards.)

---

## How to use this cookbook (guide for Opus)

**To design a new benchmark from scratch:**
1. Read `00-KNOWLEDGEBASE/01-benchmark-design-best-practices.md` — the Seven Laws + the ten-step
   Design Pipeline + the pre-registration checklist. This is the master document.
2. Pick options from `02-design-space-options-and-tradeoffs.md` (format/item/scoring menus with
   evidence-backed pros and cons).
3. For the domain, read the matching methods doc (08 normative / 09 moral psych / 10 religious /
   11 cultural) — each ends with a design brief and points at the corresponding full design in
   `20-DESIGNS/`.
4. Apply the specialist docs at the matching pipeline step: 03 validity, 04 difficulty/saturation,
   05 contamination/robustness, 06 agentic/multiturn, 07 judges/scoring, 12 pluralism/whose-values,
   13 lab practices.
5. Before finalizing, run the doc-01 checklist and the doc-04 §6 "hard/unsaturated/discriminative"
   contract.

**To develop one of the existing designs:** start at `20-DESIGNS/00-design-rationale-and-portfolio.md`
(selection logic + build order: DUPLEX → CRUX → UNMARKED → others). Each design is a full spec
(construct, tasks, scoring, validity, pilot protocol, novelty statement, risks). The eight sketches
in `20-DESIGNS/SKETCHES/` are promotion-ready seeds.

**To verify or extend a claim:** every load-bearing claim carries a `[card-stem]` citation. Drill
down: claim → theme dossier (`30-EVIDENCE/20260705-dossiers/`, evidence tables mapping stems→facts)
→ evidence card (`30-EVIDENCE/20260705-cards/<stem>.card.md`, page-cited) → source extract
(`../PDF Extracts/`). Page refs in cards are accurate to ±1–2 pages. The four sub-project digests
(`30-EVIDENCE/20260705-digests/`) carry each meta-evaluation's exact statistics and file pointers —
copy numbers from them verbatim, never recompute.

**For literature context:** `10-LITERATURE/` holds descriptive companions (one lit review + SOTA per
school, cross-corpus landscape statistics, and an alignment-methods survey).

## Directory map

```
COOKBOOK/
├── README.md                          ← you are here
├── 00-KNOWLEDGEBASE/                  ← Fable-authored synthesis (13 docs)
│   ├── 01-benchmark-design-best-practices.md   (MASTER: Seven Laws, pipeline, checklist)
│   ├── 02-design-space-options-and-tradeoffs.md
│   ├── 03-validity-and-psychometrics.md
│   ├── 04-saturation-difficulty-discrimination.md
│   ├── 05-contamination-gaming-robustness.md
│   ├── 06-agentic-and-multiturn-evaluation.md
│   ├── 07-llm-judges-and-scoring-methods.md
│   ├── 08-normative-ethics-methods.md
│   ├── 09-moral-psychology-methods.md
│   ├── 10-religious-values-methods.md
│   ├── 11-cultural-linguistic-methods.md
│   ├── 12-pluralism-aggregation-whose-values.md
│   └── 13-ai-lab-alignment-practices.md
├── 10-LITERATURE/                     ← Opus-drafted descriptive companions (6 docs)
│   ├── lit-review-normative-ethics.md
│   ├── lit-review-moral-psychology.md
│   ├── lit-review-religious-values.md
│   ├── lit-review-cultural-linguistic.md
│   ├── benchmark-landscape-statistics.md        (965 records; 737 distinct; overlap quantified)
│   └── alignment-methods-overview.md
├── 20-DESIGNS/                        ← Fable-authored design portfolio
│   ├── 00-design-rationale-and-portfolio.md     (selection logic + build order)
│   ├── 01-flagship-unmarked.md        (unannounced moral behavior, agentic)
│   ├── 02-normative-frameshift.md     (framework-conditioned reasoning)
│   ├── 03-moralpsych-duplex.md        (process signatures + moral identity — BUILD FIRST)
│   ├── 04-religious-intra.md          (intra-tradition reasoning, denominational)
│   ├── 05-cultural-cultivate.md       (in-situ cultural adaptation)
│   ├── 06-crosscutting-crux.md        (value-conflict adjudication — BUILD SECOND)
│   └── SKETCHES/sketches-S1-S8.md     (8 promotion-ready concepts)
├── 30-EVIDENCE/                       ← machine layer (dated 20260705-)
│   ├── 20260705-corpus-manifest.json            (620 papers, filter documented)
│   ├── 20260705-ailabs-{listing,shortlist}.json (343 → 61 curated)
│   ├── 20260705-cards/                          (620 paper evidence cards)
│   ├── 20260705-ailabs-cards/                   (57 lab-report cards)
│   ├── 20260705-digests/                        (4 sub-project digests)
│   ├── 20260705-dossiers/                       (13 theme dossiers + parts/)
│   ├── 20260705-card-index.json                 (theme routing)
│   └── 20260705-run-state.json                  (validation ledger)
└── PYTHON/                            ← pipeline scripts (manifest, batching, validation, routing)
```

## Provenance & quality notes

- Evidence cards were produced by a 181-agent fan-out (Opus readers for the 196 benchmark-central
  papers, Sonnet for context papers) under an anti-hallucination contract (every number/quote
  page-cited; unknowns explicitly bucketed). A 32-card stratified adversarial audit found 30/32
  substantively clean; the 2 failures were corrected against sources. Treat card page refs as ±1–2 pp.
- 4 AI-lab reports were un-cardable because the vault PDFs are misextracted (wrong papers inside):
  Anthropic Sabotage Evals / Sycophancy Probes / Sleeper Agents, and "Gemini Safety" (2403.04312).
  One card filename mismatch: the CCAI-named Anthropic card actually contains the Sycophancy paper.
  Fix upstream before relying on those stems.
- Sub-project caveats propagate: NormEval F1–F7 are elicited/exploratory; Moral Psych model-specific
  absolutes carry a self-administration disclosure; RV cross-vendor comparisons are suggestive;
  Cultural-Global cross-model numbers are descriptive (N_eff≈3.4). Landscape/structural findings in
  all four are solid.
- The adversarial-review pass over `20-DESIGNS/` and `10-LITERATURE/` was deferred at session end
  (rate-limit window) — see the session handoff for the exact protocol to run next.
