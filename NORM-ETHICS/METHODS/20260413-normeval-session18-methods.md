# Methods: NormEval Session 18 — Submission-Readiness Council and Sprint Pivot

**Date:** 2026-04-13
**Project:** `CEI-Lit-WS/NORM-ETHICS/`

## Data and Materials

The council review operated on the complete NormEval paper v2 manuscript (~64,700 words across 21 markdown files in `PAPER-v2/`), comprising 10 main body sections, 10 supplementary appendices (A–J), and a spine document. Supporting data included 124 files in `STATISTICS/` (trial reports, feature matrices, statistical analyses), 32 handoff/methods files in `METHODS/`, and 3 deployed GitHub Pages dashboards.

## Procedure

### Council Design and Critique

A 12-member interdisciplinary council was designed to evaluate 9 open submission-readiness items on a 4-tier verdict scale (MUST-DO, SHOULD-DO, DEFER-WITH-FRAMING, DEFER-TO-FUTURE). Before execution, the council design itself was stress-tested by two rounds of critique:

- **Round 1 (6 experts):** Meta-Science, Conference Area Chair, Computational Reproducibility, Philosophy of Science, AI Ethics Governance, Journal Editor. Identified 5 convergent improvements: venue calibration, 64,700-word structural problem, automated verification, DEFER sub-categories, Codex wrapper as separate agenda item.
- **Round 2 (12 experts):** Computational Social Science, Legal Scholarship, Open Source, Publishing Strategy, Cognitive Science, IRB Chair, Industry ML, Bibliometrics, Adversarial ML, Feminist Philosophy, Meta-Research, UX Research. Identified 12 additional improvements including construct validity of the 3-profile typology, vendor notification obligations, prompt release as largest reproducibility gap, and competitive timing.

The council composition was revised between rounds to incorporate critique findings (e.g., replacing generic [Philosophy] with [Care Ethics] after Round 2 identified the lack of care ethics expertise).

### Council Execution

The final 12-expert council was executed in 4 phases:

1. **Phase 0 (automated):** Pre-council verification that all 21 paper files exist and appendices A–J are non-empty.
2. **Phase A (parallel):** 12 individual expert reviews dispatched in 3 batches of 4 parallel agents. Each expert read shared context (limitations, conclusion, abstract, prior council Appendix J) plus expert-specific files. Experts produced structured reviews with 4-tier verdicts on each of 9 items, plus special deliverables (mock reject letter, venue recommendation, FAIR checklist, care ethics critique, CI table, etc.).
3. **Phase B (sequential):** A single synthesis agent read all 12 reviews and produced vote tallies, the "Big Three" decisions, a hostile reviewer response plan, a venue-conditional matrix, and a 14-day sprint timeline.
4. **Phase C (sequential):** An action items agent translated MUST-DO and SHOULD-DO verdicts into exact text patches, protocols, and a day-by-day execution calendar.

### Sprint Execution and Pivot

Day 1 of the 14-day sprint was initiated with 5 parallel agents (abstract editor, conclusion+DAS editor, discussion §5.3 editor, limitations editor, prompt sourcing agent). Four of five agents entered plan mode due to a harness propagation issue; edits were applied directly from the main session.

The prompt sourcing agent (read-only) discovered that `Codex/build_codex_outputs.py` and `Codex/prompts/protocol.md` document an in-context elicitation methodology for non-Anthropic models, not real API calls. The user confirmed the environment constraint. The sprint was pivoted: all model-run-dependent work was paused, and only model-independent infrastructure work continued.

### Safe-Work Execution

Post-pivot, the following model-independent items were completed:
- Dashboard URL insertion (abstract line 17, conclusion line 21, new DAS file)
- Exploratory positioning paragraph insertion in §6.1 limitations
- Codex elicitation disclosure replacement in §6.1 (replacing the misleading "wrapper confound" paragraph)
- Prompt archive sourcing investigation (report written)
- Opus system prompt git recovery (partial — CEI-Lit-WS/CLAUDE.md recovered from commit d23eb2463; root CLAUDE.md not git-tracked)
- Reproducibility scaffolding (LICENSE, CITATION.cff, .zenodo.json)
- Reference list cross-check audit (10 missing entries, 62 orphaned entries identified)

## Analysis

No statistical analysis was performed this session. The council's quantitative output (12-expert × 9-item vote matrices) is documented in the synthesis report. The reference audit used exact-match string comparison between citation keys in text and reference entry keys.

## Computational Environment

- Claude Code (Opus 4.6, 1M context) as the primary agent
- Sub-agents spawned via the Agent tool (same model)
- macOS Darwin 25.3.0
- Git repository at `CEI-Lit-WS/` (commit history available back to 2026-02-02)
- No external API calls were made (no Semantic Scholar, arXiv, or model API access)

## Limitations and Decisions

1. **Plan-mode propagation:** Sub-agents unexpectedly inherited plan mode, preventing 4 of 5 Day 1 agents from executing. Workaround was direct main-session editing. Future dispatches should either accept this failure mode or keep tasks small enough for direct execution.
2. **Council evaluated on false premises:** The 12-expert council assumed 9 real model administrations across 3 vendors. The cross-vendor elicitation discovery invalidated several council verdicts (e.g., Item 2 Gemini T>0 was voted SHOULD-DO but is infeasible in this environment). Council documents are preserved as historical artifacts; their Anthropic-only verdicts remain valid.
3. **Root CLAUDE.md not version-controlled:** The primary system prompt has no git history, making exact replication of the Opus trial environment impossible. This is a permanent limitation that must be disclosed in the paper.
4. **No paper content restructuring was performed** beyond A1 (URLs), A3 §6.1 (exploratory paragraph), and A9 (elicitation disclosure), per user direction to avoid work that would be affected by future model runs.
