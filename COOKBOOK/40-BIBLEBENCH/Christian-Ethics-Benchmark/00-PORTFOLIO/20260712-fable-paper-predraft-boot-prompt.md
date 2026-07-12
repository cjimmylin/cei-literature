<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — Boot prompt: Fable paper pre-draft session (results-independent sections)

**Staged:** 2026-07-12 by Claude (Fable), at Jimmy's direction. **Purpose:** before the
panel results land, use a Fable session (Jimmy present) to build the full
AI-conference paper scaffold and flesh out every section that does NOT depend on
results — so that when Codex's O5 pipeline finishes, only results/discussion slots
remain. Runs in PARALLEL with the Codex execution lane (dashboard §12 stays the Codex
prompt; this is a separate lane).

---

```text
New Fable session: WALKWORTHY — PAPER PRE-DRAFT (results-independent sections).
Jimmy present. SCOPE LOCK: CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/
only; differentiate against PUBLISHED LITERATURE ONLY — never sibling benches.

STEP 0 — GRILL ME FIRST: invoke the grill-me skill on Jimmy before writing anything.
Pin down at minimum: target venue/format (e.g. NeurIPS D&B, FAccT, ACL) + page budget;
the paper's ONE headline contribution claim; author framing (religious-values
benchmarking positioning, generalizability story); anonymization needs; what results
scope to promise (full 10-design vs wave-release subset per FR-9). Log answers in the
session doc.

ON OPENING: read 00-PORTFOLIO/project-dashboard.html + the NEWEST dated handoff FIRST —
Codex runs in parallel and results may already partially exist (if W3 recompute or
verdicts landed, incorporate; do not wait for them). Then: the normative charter +
master-plan (§5: paper claims = Fable/Jimmy only), 20260710-fable-gate-prereg-pilot-
adjudication.md (§B/§C/§E — the pre-registration story IS the paper's methods spine),
20260711d-fable-o5-decision-framework.md, 20260710-human-label-protocol.md,
20260712-fable-codex-full-handoff.md. HOLDOUT never loaded; no item text quoted from
HOLDOUT ever; be careful quoting public items (contamination — prefer paraphrase +
counts).

TASK — build PAPER/ (new subdir): outline.md (Fable-authored, the claims skeleton) +
one file per section. Fable writes: title/abstract skeleton, intro + contribution
claims (each claim tagged with the gate/status it is conditioned on), threats-to-
validity/limitations, and the results-section SCAFFOLD (placeholder tables keyed to
the §B statistics, release-formula statuses, G9 headlines, §6.1 readouts — exact
column schemas so Codex can fill them mechanically). Delegate to Opus subagents
(explicit model=opus): related work (published benchmarks: values/ethics/religion/
alignment evals), benchmark-construction methods (corpus, 14-area registry, 10
method-major designs, 3 strata, DSP guards, 356-authored/344-runnable, HOLDOUT,
two-agent authoring + adversarial review cycles), measurement methods (frozen judge
pair + tie-breaker + adjudication + human labeling waves + G1–G10 gates +
pre-registration narrative), experimental setup (6-SUT OpenRouter panel, costs),
ethics statement, reproducibility checklist. Fable adversarially reviews every
Opus-drafted section against the frozen docs (no claim beyond what a gate can
license; no result asserted; every number cross-checked).

CONSTRAINTS: paper release/submission claims remain Jimmy-only (master-plan §5);
FIX-MECHANICS-ONLY untouched; report immutability (PAPER/ files are living drafts —
mark them DRAFT, not dated-immutable); shared git index (explicit pathspecs, ff-only);
no live calls. If Codex results exist, cite the NEW dated readings file, never the
superseded ones.

ON CLOSING: NEW dated handoff; dashboard update (add a PAPER lane to §7 who-owes-what
+ Changelog row; do NOT displace the Codex §12 prompt); update Claude memory; commit +
push WALKWORTHY paths. Output = a PAPER/ scaffold where post-results work is purely
mechanical fill-in.
```
