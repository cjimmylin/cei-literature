# G-05 — Preference-Data Provenance and Noise

**Stage B** · **Ratings S/T/F: M/M/M** · **Programs: RP-04 (fold-in)** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
Preference datasets carry >20% label noise and largely unexamined value content; tooling to characterize what annotators actually expressed (SAE-based, WIMHF) appeared in 2025 and the vault lacks the thread entirely.

## Why it matters                  [KERNEL — FROZEN]
"Values in = values out" is the naive model; in practice nobody reads the values in. Severity M (real but partially absorbed by G-04's RM-level audit — the RM is where data defects become behaviorally live). Tractability M: CEI can audit; fixing provenance is the ecosystem's job.

## Evidence                        (corpus + field)
**Corpus baseline:** the "values in = values out" question is unexamined in the vault.

**Field:** the first link in the RLHF chain — the labels themselves — is noisier and less legible than assumed (Front B causal story):
- **Preference-data noise** (arXiv:2511.10985): >20% label noise common in public preference datasets; alignment outcomes highly sensitive to data quality.
- **WIMHF** ("What I Missed of Human Feedback"; arXiv:2510.26202): SAE-based descriptions of what annotators actually *expressed*, as opposed to what the pairwise label records — the first tooling to read value content out of preference data.

The naive theory ("values in = values out") assumes the value content of preference data is known; in practice nobody reads it, and >20% of the labels are noise before value content is even considered.

## State of the art
Provenance tooling is new (2025) and thin; there is no dataset-card-for-values standard. This gap is deliberately **not** a standalone program: the RM-level audit (G-04) dominates it for leverage, because the RM is where data defects become behaviorally live — auditing the RM captures the net effect of the data without needing to fully characterize the upstream labels. CEI's contribution is one audit-style study of a public preference set's value content using bank-derived categories, plus a proposed dataset-card-for-values template that rides alongside RP-02's reporting standards.

## What closing looks like         [KERNEL — FROZEN]
M1 — noise/provenance thread acquired. M2 — one CEI audit-style study of a public preference set's value content using bank-derived categories. M3 — a dataset-card-for-values template proposed alongside RP-02's reporting standards.

## CEI response                    [KERNEL — FROZEN]
Folded into RP-04 (data layer of the hidden curriculum); no standalone program by design — the RM-level audit dominates it for leverage.

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read WIMHF (2510.26202) and summarize the SAE-based annotator-intent method into §State of the art; note whether its SAE features could label CEI value categories.
- [ ] Select one public preference dataset (e.g., an open RLHF/Tulu set) as the M2 audit target and record its documented noise rate.
- [ ] Draft the dataset-card-for-values template (M3): fields for value categories present, annotator-pool composition, and noise estimate — coordinate with RP-02 reporting standards.
- [ ] Add a short note distinguishing G-05 (data layer) from G-04 (RM layer) so the fold-in rationale is legible to future sessions.
- [ ] Cross-check the >20% noise figure (2511.10985) against any noise estimate in the chosen audit dataset before using it in prose.

## Sources                         (evidence classes marked)
- Preference-data curation / label noise — arXiv:2511.10985 — **SEARCH-CONFIRMED** — >20% label noise.
- WIMHF (what annotators expressed, SAE) — arXiv:2510.26202 — **SEARCH-CONFIRMED**.
- RMs Inherit Value Biases (Christian et al.) — arXiv:2601.20838 — **SEARCH-CONFIRMED** — cross-ref: RM layer where data defects become live (G-04).
