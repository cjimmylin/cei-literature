# P1 Acquisition Log — 2026-07-09

**Source:** `INNOVATION/04-missing-literature.md` — P1 anchor table (17 papers)
**Pipeline:** arXiv metadata verify → PDF download (curl) → PyMuPDF extract → paper record creation → YAML validation
**Executed:** 2026-07-09

## Summary

| Metric | Count |
|--------|-------|
| Attempted | 17 |
| ⚠ Verified (warn flag) | 4 / 4 — all resolved correctly |
| Downloaded | 17 / 17 |
| Extracted | 17 / 17 |
| Paper records created | 17 / 17 |
| Misses | 0 |
| Validation (final) | 2385/2385 PASS |

## ⚠ Verification Results (flagged IDs)

| ID | arXiv ID | Resolved Title | Authors | Verdict |
|----|---------|----------------|---------|---------|
| P1-10 | 2606.21550 | AI Alignment From Social Choice Perspectives | Daniel Halpern; Evi Micha; Ariel D. Procaccia | PASS — matches expected topic |
| P1-13 | 2605.28591 | Models That Know How Evaluations Are Designed Score Safer | Katharina Deckenbach; Haritz Puerto; Jonas Geiping | PASS — matches expected topic |
| P1-14 | 2604.20995 | Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models | Inderjeet Nair; Jie Ruan; Lu Wang | PASS — matches expected topic |
| P1-15 | 2606.22974 | When Preferences Fail to Become Incentives: A Utility-Behavior Gap in Large Language Models | Yujun Zhou; Christopher M. Ackerman | PASS — matches expected topic |

All 4 flagged IDs resolved to papers matching the expected topic and Gap assignment. None were misfires.

## Per-Paper Results

| ID | List Title | arXiv ID | Gap | First Author | Year | Downloaded | Paper Record |
|----|-----------|---------|-----|-------------|------|------------|--------------|
| P1-01 | Emergent Misalignment | 2502.17424 | G-20 | Jan Betley | 2025 | YES | `2025-Betley-Emergent Misalignment.md` |
| P1-02 | Persona Vectors | 2507.21509 | G-20 | Runjin Chen | 2025 | YES | `2025-Chen-Persona Vectors.md` |
| P1-03 | Persona Features Control EM (OpenAI) | 2506.19823 | G-20 | Miles Wang | 2025 | YES | `2025-Wang-Persona Features Control EM.md` |
| P1-04 | Natural EM from Reward Hacking | 2511.18397 | G-06/20 | Monte MacDiarmid | 2025 | YES | `2025-MacDiarmid-Natural EM from Reward Hacking.md` |
| P1-05 | SpecEval | 2509.02464 | G-01 | Ahmed Ahmed | 2025 | YES | `2025-Ahmed-SpecEval.md` |
| P1-06 | Stress-Testing Model Specifications | 2510.07686 | G-02 | Jifan Zhang | 2025 | YES | `2025-Zhang-Stress-Testing Model Specifications.md` |
| P1-07 | Peer-Prediction for scalable oversight | 2601.20299 | G-07 | Tianyi Alex Qiu | 2026 | YES | `2026-Qiu-Peer-Prediction Scalable Oversight.md` |
| P1-08 | Confirmation Bias in oversight | 2507.19486 | G-09 | Gabriel Recchia | 2025 | YES | `2025-Recchia-Confirmation Bias in LLM Oversight.md` |
| P1-09 | AI Debaters' Own Beliefs bias | 2510.13912 | G-09 | Maria Victoria Carro | 2025 | YES | `2025-Carro-AI Debaters Own Beliefs Bias.md` |
| P1-10 | Social Choice for AI Alignment (survey) | 2606.21550 | G-10 | Daniel Halpern | 2026 | YES | `2026-Halpern-Social Choice for AI Alignment Survey.md` |
| P1-11 | RMs Inherit Value Biases | 2601.20838 | G-04 | Brian Christian | 2026 | YES | `2026-Christian-RMs Inherit Value Biases.md` |
| P1-12 | CoT Monitorability (position paper) | 2507.11473 | G-13 | Tomek Korbak | 2025 | YES | `2025-Korbak-CoT Monitorability.md` |
| P1-13 | Eval-design awareness safer scores | 2605.28591 | G-14 | Katharina Deckenbach | 2026 | YES | `2026-Deckenbach-Eval-Design Awareness Safer Scores.md` |
| P1-14 | Value-Conflict Diagnostics for faking | 2604.20995 | G-15 | Inderjeet Nair | 2026 | YES | `2026-Nair-Value-Conflict Diagnostics for Faking.md` |
| P1-15 | Utility-Behavior Gap | 2606.22974 | G-23 | Yujun Zhou | 2026 | YES | `2026-Zhou-Utility-Behavior Gap.md` |
| P1-16 | Subliminal Learning | 2507.14805 | G-21 | Alex Cloud | 2025 | YES | `2025-Cloud-Subliminal Learning.md` |
| P1-17 | SSGM memory-drift governance | 2603.11768 | G-18 | Chingkwun Lam | 2026 | YES | `2026-Lam-SSGM Memory-Drift Governance.md` |

## Vault Paths Created

### PDFs (Lit-WS-PDFs/YYYY/)

- `Lit-WS-PDFs/2025/2025-Betley-Emergent Misalignment.pdf` (8468 KB, 41 pages)
- `Lit-WS-PDFs/2025/2025-Chen-Persona Vectors.pdf` (4809 KB, 63 pages)
- `Lit-WS-PDFs/2025/2025-Wang-Persona Features Control EM.pdf` (8003 KB, 52 pages)
- `Lit-WS-PDFs/2025/2025-MacDiarmid-Natural EM from Reward Hacking.pdf` (1285 KB, 75 pages)
- `Lit-WS-PDFs/2025/2025-Ahmed-SpecEval.pdf` (3929 KB, 133 pages)
- `Lit-WS-PDFs/2025/2025-Zhang-Stress-Testing Model Specifications.pdf` (12915 KB, 27 pages)
- `Lit-WS-PDFs/2026/2026-Qiu-Peer-Prediction Scalable Oversight.pdf` (4308 KB, 36 pages)
- `Lit-WS-PDFs/2025/2025-Recchia-Confirmation Bias in LLM Oversight.pdf` (2927 KB, 61 pages)
- `Lit-WS-PDFs/2025/2025-Carro-AI Debaters Own Beliefs Bias.pdf` (2541 KB, 31 pages)
- `Lit-WS-PDFs/2026/2026-Halpern-Social Choice for AI Alignment Survey.pdf` (570 KB, 30 pages)
- `Lit-WS-PDFs/2026/2026-Christian-RMs Inherit Value Biases.pdf` (3161 KB, 29 pages)
- `Lit-WS-PDFs/2025/2025-Korbak-CoT Monitorability.pdf` (406 KB, 11 pages)
- `Lit-WS-PDFs/2026/2026-Deckenbach-Eval-Design Awareness Safer Scores.pdf` (1011 KB, 42 pages)
- `Lit-WS-PDFs/2026/2026-Nair-Value-Conflict Diagnostics for Faking.pdf` (1286 KB, 54 pages)
- `Lit-WS-PDFs/2026/2026-Zhou-Utility-Behavior Gap.pdf` (2564 KB, 23 pages)
- `Lit-WS-PDFs/2025/2025-Cloud-Subliminal Learning.pdf` (1300 KB, 34 pages)
- `Lit-WS-PDFs/2026/2026-Lam-SSGM Memory-Drift Governance.pdf` (5789 KB, 13 pages)

### Extracts (CEI-Lit-WS/PDF Extracts/YYYY/)

- `PDF Extracts/2025/2025-Betley-Emergent Misalignment.md`
- `PDF Extracts/2025/2025-Chen-Persona Vectors.md`
- `PDF Extracts/2025/2025-Wang-Persona Features Control EM.md`
- `PDF Extracts/2025/2025-MacDiarmid-Natural EM from Reward Hacking.md`
- `PDF Extracts/2025/2025-Ahmed-SpecEval.md`
- `PDF Extracts/2025/2025-Zhang-Stress-Testing Model Specifications.md`
- `PDF Extracts/2026/2026-Qiu-Peer-Prediction Scalable Oversight.md`
- `PDF Extracts/2025/2025-Recchia-Confirmation Bias in LLM Oversight.md`
- `PDF Extracts/2025/2025-Carro-AI Debaters Own Beliefs Bias.md`
- `PDF Extracts/2026/2026-Halpern-Social Choice for AI Alignment Survey.md`
- `PDF Extracts/2026/2026-Christian-RMs Inherit Value Biases.md`
- `PDF Extracts/2025/2025-Korbak-CoT Monitorability.md`
- `PDF Extracts/2026/2026-Deckenbach-Eval-Design Awareness Safer Scores.md`
- `PDF Extracts/2026/2026-Nair-Value-Conflict Diagnostics for Faking.md`
- `PDF Extracts/2026/2026-Zhou-Utility-Behavior Gap.md`
- `PDF Extracts/2025/2025-Cloud-Subliminal Learning.md`
- `PDF Extracts/2026/2026-Lam-SSGM Memory-Drift Governance.md`

### Paper Records (CEI-Lit-WS/papers/)

- `papers/2025-Betley-Emergent Misalignment.md` — G-20, Value Formation & Emergent Misalignment
- `papers/2025-Chen-Persona Vectors.md` — G-20, Value Formation & Emergent Misalignment
- `papers/2025-Wang-Persona Features Control EM.md` — G-20, Value Formation & Emergent Misalignment
- `papers/2025-MacDiarmid-Natural EM from Reward Hacking.md` — G-06/20, Value Formation & Emergent Misalignment
- `papers/2025-Ahmed-SpecEval.md` — G-01, Specification & Compliance
- `papers/2025-Zhang-Stress-Testing Model Specifications.md` — G-02, Specification & Compliance
- `papers/2026-Qiu-Peer-Prediction Scalable Oversight.md` — G-07, Scalable Oversight
- `papers/2025-Recchia-Confirmation Bias in LLM Oversight.md` — G-09, Scalable Oversight
- `papers/2025-Carro-AI Debaters Own Beliefs Bias.md` — G-09, Scalable Oversight
- `papers/2026-Halpern-Social Choice for AI Alignment Survey.md` — G-10, Preference Aggregation & Social Choice
- `papers/2026-Christian-RMs Inherit Value Biases.md` — G-04, AI Safety & Alignment
- `papers/2025-Korbak-CoT Monitorability.md` — G-13, AI Safety & Alignment
- `papers/2026-Deckenbach-Eval-Design Awareness Safer Scores.md` — G-14, AI Safety & Alignment
- `papers/2026-Nair-Value-Conflict Diagnostics for Faking.md` — G-15, AI Safety & Alignment
- `papers/2026-Zhou-Utility-Behavior Gap.md` — G-23, Value Formation & Emergent Misalignment
- `papers/2025-Cloud-Subliminal Learning.md` — G-21, Value Formation & Emergent Misalignment
- `papers/2026-Lam-SSGM Memory-Drift Governance.md` — G-18, Multi-Agent Value Dynamics

## Misses

None. All 17 P1 anchor papers successfully acquired.

## Validation Output

```
Validating 2385 papers...
Valid papers:     2385/2385
Papers with errors: 0
All papers have valid YAML frontmatter!
```

## Notes

- Non-arXiv P1 items in 04-missing-literature.md (Teaching Claude Why, Agentic Misalignment blog post) require manual PDF handling and are out of scope for this arXiv-only run.
- All 4 flagged IDs verified against arXiv abs page before download — none were misfires.
- Paper records use ethics_perspective codes from classification v1.5 (5 new dual-homed codes active).
- `innovation_gap` field added to each paper record for easy INNOVATION project filtering.
- Files named per vault convention: `YYYY-FirstAuthorSurname-Short Title.md/.pdf`.
- Script artifacts: `INNOVATION/40-BUILDS/p1_acquire.py`, `p1_rename.py`, `p1_fix_yaml.py`, `p1_fix_tags2.py`
