# P3 Gap-Fill Acquisition Log — 2026-07-11

**Date:** 2026-07-11 · **Lane:** A1 (Fable session, gapfill pass)
**Mission:** Acquire still-absent sources from P3 citation ledger §5.3 (12 rows not upgraded in ledger-v1 phase-2 pass).

---

## Step 1 — Ledger-v1 §5.3 Enumeration

Enumeration from `20260710-ledger-v1.md §5.3` matched prompt snapshot exactly.
**12 rows NOT upgraded in ledger-v1:**

| Category | Rows |
|---|---|
| Declined (ID ingested, title/claim diverges) | W3 (2607.01250), S3 (partial bundle) |
| Not ingested (source absent from all logs) | S1, S8, S9, S10, S11, S13, S15, W5, W26, W32 |

**Note:** Prompt listed W3 + S3 declined + 10 not-ingested. Ledger agrees exactly.

---

## Step 2 — arXiv Acquisitions (S9, S15, W5, W26, W32)

Script: `INNOVATION/40-BUILDS/p3gap_acquire.py`

### Per-item verdicts

| Row | arXiv ID | Fetched Title | Verify | Status |
|---|---|---|---|---|
| **S9** | 2501.09254 | "Clone-Robust AI Alignment" | PASS — matched 5/6 keywords: clone, robust, alignment, preference, social choice | **ACQUIRED** |
| **S15** | 2502.08640 | "Utility Engineering: Analyzing and Controlling Emergent Value Systems in AIs" | PASS — matched 5/7 keywords: utility, engineer, value, prefer, align | **ACQUIRED** |
| **W5** | 2510.06370 | "EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences" | PASS — matched 7/7 keywords (all) | **ACQUIRED** |
| **W26** | 2602.20710 | "Counterfactual Simulation Training for Chain-of-Thought Faithfulness" | PASS — matched 8/8 keywords (all) | **ACQUIRED** |
| **W32** | 2604.09588 | "Persistent Identity in AI Agents: A Multi-Anchor Architecture for Resilient Memory and Continuity" | PASS — matched 5/7 keywords: identity, file, architect, agent, memory | **ACQUIRED** |

### Evidence paths (ls-verified)

| Row | PDF path | Size |
|---|---|---|
| S9 | `Lit-WS-PDFs/2025/2025-Procaccia-Clone-Robust AI Alignment.pdf` | 584KB |
| S15 | `Lit-WS-PDFs/2025/2025-Mazeika-Utility Engineering Analyzing Controlling Emergent.pdf` | 3.2MB |
| W5 | `Lit-WS-PDFs/2025/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability.pdf` | 1.3MB |
| W26 | `Lit-WS-PDFs/2026/2026-Hase-Counterfactual Simulation Training Chain-of-Thought Faithfulness.pdf` | 1.2MB |
| W32 | `Lit-WS-PDFs/2026/2026-Menon-Persistent Identity AI Agents Multi-Anchor.pdf` | 599KB |

### Claim confirmations from extracts

- **S9 (clone-robustness):** Abstract explicitly: "robustness to approximate clones, a desirable property of RLHF algorithms" — Procaccia, Schiffer, Zhang (Harvard). Matches "clone-robustness (D · G-10)".
- **S15 (utility engineering):** Title and abstract exact match. Paper by Mazeika et al. (Center for AI Safety + U Penn + UC Berkeley). `arXiv:2502.08640v2, Feb 2025`. NeurIPS 2025 spotlight not confirmed in extract but arXiv ID matches. Matches "utility engineering (E · G-23)".
- **W5 (EVALUESTEER):** Extract line 39: "the best models achieve <75% accuracy at choosing the [correct profile-aligned response]" — exact match to ledger claim "<75% on value+style profiles". Matches "EVALUESTEER (B · G-04)".
- **W26 (counterfactual-simulation):** Title exactly "Counterfactual Simulation Training for Chain-of-Thought Faithfulness" by Hase & Potts (Stanford). Matches "counterfactual-simulation faithfulness training (E · G-13)".
- **W32 (identity-file architectures):** Extract states paper introduces "soul.py, an open-source architecture that implements persistent identity through separable components (identity files and memory logs)" — exact match to "identity-file architectures (F · G-18)".

---

## Step 3 — Non-arXiv Items

### Web search results (via Sonnet sub-agent)

**S1 — OpenAI Model Spec Evals (Mar 2026)**
- Identified: YES, HIGH confidence
- Source: Blog post + GitHub repo — `https://alignment.openai.com/model-spec-evals/` and `https://github.com/openai/model_spec_evals`
- What it is: Shipped eval suite by Alan Guo, Jason Wolfe (OpenAI Alignment Research). GPT-5 Thinking grader scores responses 1–7 against the Spec. Publishes per-model compliance percentages.
- **Verdict: DEFERRED — web page and GitHub repo only; no PDF or arXiv preprint exists. URL logged for future session reference.**

**S8 — NLHF / maximal-lottery formulations**
- Two papers identified:
  1. "Nash Learning from Human Feedback" — Munos et al. (Google DeepMind), arXiv:2312.00886 (ICML 2024). Verified via API.
  2. "Jackpot! Alignment as a Maximal Lottery" — Maura-Rivero, Lanctot, Visin, arXiv:2501.19266. Verified via API.
- Both acquired. Script: `p3gap_acquire_batch2.py`
- **Verdict: ACQUIRED (both components)**

| Sub-item | PDF path | Size |
|---|---|---|
| S8a | `Lit-WS-PDFs/2023/2023-Munos-Nash Learning Human Feedback.pdf` | 642KB |
| S8b | `Lit-WS-PDFs/2025/2025-Maura-Rivero-Jackpot Alignment as Maximal Lottery.pdf` | 684KB |

**S10 — OpenAI Collective Alignment → Model Spec pipeline**
- Identified: YES, HIGH confidence
- Source: Blog post — `https://openai.com/index/collective-alignment-aug-2025-updates/`
- What it is: Aug 2025 update, ~1,000-person global survey compared against Model Spec; disagreement areas adopted as Spec changes. No arXiv preprint, no PDF.
- **Verdict: DEFERRED — blog post only; no PDF available. URL logged.**

**S11 — Habermas-machine critique (Ethics & IT 2025)**
- Identified: YES, HIGH confidence
- Title: "Toward an artificial deliberation? On Google DeepMind's Habermas Machine"
- Author: Alessandro Volpe
- DOI: 10.1007/s10676-025-09854-1 (*Ethics and Information Technology* vol. 27, art. 45, 2025)
- Source: Springer journal (hybrid journal — likely paywalled)
- **Verdict: DEFERRED — paywalled Springer journal; no open-access PDF located in 3-attempt search limit. DOI logged.**

**S13 — Sheshadri et al. 2025 compliance-gap**
- Identified: YES, HIGH confidence
- Title: "Why Do Some Language Models Fake Alignment While Others Don't?"
- Authors: Sheshadri et al. (Anthropic / Scale AI / Redwood Research)
- arXiv:2506.18032 (June 2025), verified via API
- Acquired. **IMPORTANT NOTE:** The paper's "compliance gap" is specifically about alignment-faking (training vs. deployment behavioral delta in 25 frontier models), not spec-compliance rates. The ledger's claim "compliance-gap across frontier models" is accurate — the paper explicitly uses the term "compliance gap" and measures it across 25 models. The framing is alignment-faking rather than a spec-compliance checklist. This distinction should be flagged at pre-submission review.
- **Verdict: ACQUIRED**

| Row | PDF path | Size |
|---|---|---|
| S13 | `Lit-WS-PDFs/2025/2025-Sheshadri-Why Do Some Language Models.pdf` | 27.4MB |

**S3 missing components — reward-lens and token-probing**
- Both identified and acquired:
  - **(a) reward-lens:** "reward-lens: A Mechanistic Interpretability Library for Reward Models" — Mohammed Suhail B Nadaf, arXiv:2604.26130 (April 2026), verified via API
  - **(b) token-probing:** "Reward Model Interpretability via Optimal and Pessimal Tokens" — Christian, Kirk, Thompson et al., arXiv:2506.07326 (June 2025, ACM FAccT 2025), verified via API
- **Verdict: ACQUIRED (both missing components)**

| Sub-item | PDF path | Size |
|---|---|---|
| S3a (reward-lens) | `Lit-WS-PDFs/2026/2026-Nadaf-reward-lens Mechanistic Interpretability Library Reward.pdf` | 776KB |
| S3b (token-probing) | `Lit-WS-PDFs/2025/2025-Christian-Reward Model Interpretability via Optimal.pdf` | 6.3MB |

S3's existing SAFER component: `Lit-WS-PDFs/2025/2025-Shi-SAFER Probing Safety in Reward Models with Sparse.pdf` (already in vault from batch P2-10).

**ALL THREE S3 components now on disk → S3 row can be upgraded to [VERIFIED] in ledger-v2.**

---

## W3 Report — Dönmez 2607.01250

**Required per mission instructions.** Fable adjudicates this in-loop; W3 is NOT upgraded.

**Paper:** "Structuring the Space of Sociotechnical Alignment: A Specification Framework and Systematic Literature Review" by Esra Dönmez and Agnieszka Falenska (University of Stuttgart). arXiv:2607.01250v1, submitted 2 Jun 2026. 42 pages, 281-paper corpus, ACL Anthology.

**Ledger claim for W3:** "June-2026 systematic review, 'underspecified' most frequent"

**Assessment of claim:**

1. **"June-2026 systematic review"** — CONFIRMED. The paper is a systematic literature review submitted June 2, 2026 (arXiv ID 2607.01250v1 = June 2026). The paper explicitly states: "we construct a corpus of 281 sociotechnical alignment papers from the ACL Anthology" and calls this a "systematic literature review."

2. **"'underspecified' most frequent"** — CONFIRMED. Extract line 574-575 (§4.2): *"Target underspecification is common: **underspecified is the most frequent label in the corpus**."* The word "underspecified" refers to the most frequent manually assigned target label (papers whose alignment target is underspecified), not to a code/category name. The abstract (page 1) also states: "it often leaves underspecified what such 'social desirability' entails" and the analysis shows this is the modal finding.

**Paper character:** The paper proposes a **specification framework** for sociotechnical alignment (4 dimensions: alignment target, normative concept, methodology, theoretical framework), grounded in a systematic literature review of 281 ACL papers. It identifies recurring patterns in the corpus: (a) alignment targets frequently "underspecified," (b) normative concepts conflated with alignment targets, (c) target populations underdefined, (d) design choices rarely theoretically justified. It makes recommendations for more theory-grounded alignment approaches.

**Does it support the ledger claim?** YES. The exact phrase "underspecified is the most frequent label" appears in §4.2 of the extract and the abstract prominently features "underspecified" as the paper's central diagnosis. The title does NOT use the phrase "systematic review" but the method IS a systematic literature review (SLR) as stated in abstract/body.

**Why declined in ledger-v1:** The batch1 acquisition log logged the title as "Structuring the Space of Sociotechnical Alignment" (which IS the actual full title minus the subtitle). The log title does NOT mention "systematic review" or "underspecified most frequent" — the mismatch was between the abbreviated log title and the full ledger claim. The on-disk extract now confirms the claim IS supported.

**Recommendation for Fable adjudication:** The underlying claim IS well-supported by the paper. The ledger entry's description is accurate though the ledger's phrasing "systematic review" is a description of method (confirmed) and "underspecified most frequent" quotes a direct finding (confirmed at extract line 575). The prior decline was a conservative decision based on title-only matching at batch-acquisition time. Fable should consider whether to upgrade W3 to [VERIFIED] given the extract-confirmed evidence above, or hold for pre-submission review as originally ruled. The upgrade would be legitimate on evidence grounds but Fable must decide if the title/claim match standard has been met to its satisfaction.

---

## Step 4 — Summary Table

| Row | Verdict | Evidence path | Notes |
|---|---|---|---|
| S9 | **ACQUIRED** | `Lit-WS-PDFs/2025/2025-Procaccia-Clone-Robust AI Alignment.pdf` | title/claim confirmed; arXiv 2501.09254 |
| S15 | **ACQUIRED** | `Lit-WS-PDFs/2025/2025-Mazeika-Utility Engineering Analyzing Controlling Emergent.pdf` | title/claim confirmed; arXiv 2502.08640 |
| W5 | **ACQUIRED** | `Lit-WS-PDFs/2025/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability.pdf` | <75% claim confirmed in extract; arXiv 2510.06370 |
| W26 | **ACQUIRED** | `Lit-WS-PDFs/2026/2026-Hase-Counterfactual Simulation Training Chain-of-Thought Faithfulness.pdf` | title exact match; arXiv 2602.20710 |
| W32 | **ACQUIRED** | `Lit-WS-PDFs/2026/2026-Menon-Persistent Identity AI Agents Multi-Anchor.pdf` | "identity files" explicit in extract; arXiv 2604.09588 |
| S8a | **ACQUIRED** | `Lit-WS-PDFs/2023/2023-Munos-Nash Learning Human Feedback.pdf` | arXiv 2312.00886 (ICML 2024) |
| S8b | **ACQUIRED** | `Lit-WS-PDFs/2025/2025-Maura-Rivero-Jackpot Alignment as Maximal Lottery.pdf` | arXiv 2501.19266 |
| S13 | **ACQUIRED** | `Lit-WS-PDFs/2025/2025-Sheshadri-Why Do Some Language Models.pdf` | arXiv 2506.18032; see framing note |
| S3a | **ACQUIRED** | `Lit-WS-PDFs/2026/2026-Nadaf-reward-lens Mechanistic Interpretability Library Reward.pdf` | arXiv 2604.26130 |
| S3b | **ACQUIRED** | `Lit-WS-PDFs/2025/2025-Christian-Reward Model Interpretability via Optimal.pdf` | arXiv 2506.07326 (ACM FAccT 2025) |
| S1 | **DEFERRED** | — | OpenAI blog + GitHub only; no PDF; URL: https://alignment.openai.com/model-spec-evals/ |
| S10 | **DEFERRED** | — | OpenAI blog only; no PDF; URL: https://openai.com/index/collective-alignment-aug-2025-updates/ |
| S11 | **DEFERRED** | — | Springer paywalled; DOI: 10.1007/s10676-025-09854-1 |
| W3 | **NOT UPGRADED (per mission)** | — | See W3 Report above; Fable adjudicates |

### Counts
- **ACQUIRED: 10** (S9, S15, W5, W26, W32, S8a, S8b, S13, S3a, S3b)
- **DEFERRED: 3** (S1, S10, S11)
- **NOT UPGRADED / HELD: 1** (W3, per mission instructions)

### Ledger-v2 row upgrades (rows with dual-gated upgrade ready)
All upgrades require ls-verified on-disk vault PDF path + title/claim match.

| Row | v1 class | v2 class | Note |
|---|---|---|---|
| S3 | [SEARCH-CONFIRMED] | **[VERIFIED]** | All 3 bundle components now on disk |
| S8 | [SEARCH-CONFIRMED] | **[VERIFIED]** | Both NLHF papers (2312.00886 + 2501.19266) on disk |
| S9 | [SEARCH-CONFIRMED] | **[VERIFIED]** | 2501.09254 on disk, claim confirmed |
| S13 | [SEARCH-CONFIRMED] | **[VERIFIED]** | 2506.18032 on disk, claim confirmed (with framing note) |
| S15 | [SEARCH-CONFIRMED] | **[VERIFIED]** | 2502.08640 on disk, claim confirmed |
| W5 | [⚠] | **[VERIFIED]** | 2510.06370 on disk, <75% claim confirmed |
| W26 | [⚠] | **[VERIFIED]** | 2602.20710 on disk, claim confirmed |
| W32 | [⚠] | **[VERIFIED]** | 2604.09588 on disk, claim confirmed |

**NOT upgraded:**
- **W3** — held per mission instructions for Fable adjudication
- **S1** — deferred, no PDF
- **S10** — deferred, no PDF
- **S11** — deferred, paywalled

---

## Files Created This Session

### Acquisition scripts
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/INNOVATION/40-BUILDS/p3gap_acquire.py`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/INNOVATION/40-BUILDS/p3gap_acquire_batch2.py`

### PDFs (Lit-WS-PDFs)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Procaccia-Clone-Robust AI Alignment.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Mazeika-Utility Engineering Analyzing Controlling Emergent.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2026/2026-Hase-Counterfactual Simulation Training Chain-of-Thought Faithfulness.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2026/2026-Menon-Persistent Identity AI Agents Multi-Anchor.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2023/2023-Munos-Nash Learning Human Feedback.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Maura-Rivero-Jackpot Alignment as Maximal Lottery.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Sheshadri-Why Do Some Language Models.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2026/2026-Nadaf-reward-lens Mechanistic Interpretability Library Reward.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Christian-Reward Model Interpretability via Optimal.pdf`

### Paper records (papers/)
- `papers/2025-Procaccia-Clone-Robust AI Alignment.md`
- `papers/2025-Mazeika-Utility Engineering Analyzing Controlling Emergent.md`
- `papers/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability.md`
- `papers/2026-Hase-Counterfactual Simulation Training Chain-of-Thought Faithfulness.md`
- `papers/2026-Menon-Persistent Identity AI Agents Multi-Anchor.md`
- `papers/2023-Munos-Nash Learning Human Feedback.md`
- `papers/2025-Maura-Rivero-Jackpot Alignment as Maximal Lottery.md`
- `papers/2025-Sheshadri-Why Do Some Language Models.md`
- `papers/2026-Nadaf-reward-lens Mechanistic Interpretability Library Reward.md`
- `papers/2025-Christian-Reward Model Interpretability via Optimal.md`

### Extracts (PDF Extracts/)
- `PDF Extracts/2025/2025-Procaccia-Clone-Robust AI Alignment.md`
- `PDF Extracts/2025/2025-Mazeika-Utility Engineering Analyzing Controlling Emergent.md`
- `PDF Extracts/2025/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability.md`
- `PDF Extracts/2026/2026-Hase-Counterfactual Simulation Training Chain-of-Thought Faithfulness.md`
- `PDF Extracts/2026/2026-Menon-Persistent Identity AI Agents Multi-Anchor.md`
- `PDF Extracts/2023/2023-Munos-Nash Learning Human Feedback.md`
- `PDF Extracts/2025/2025-Maura-Rivero-Jackpot Alignment as Maximal Lottery.md`
- `PDF Extracts/2025/2025-Sheshadri-Why Do Some Language Models.md`
- `PDF Extracts/2026/2026-Nadaf-reward-lens Mechanistic Interpretability Library Reward.md`
- `PDF Extracts/2025/2025-Christian-Reward Model Interpretability via Optimal.md`

### Logs
- `INNOVATION/40-BUILDS/20260711-p3-gapfill-results.json` (batch 1)
- `INNOVATION/40-BUILDS/20260711-p3-gapfill-batch2-results.json` (batch 2)
- `INNOVATION/40-BUILDS/p3-position-paper/20260711-ledger-v2.md` (this session's output)
- `INNOVATION/40-BUILDS/20260711-p3-gapfill-acquisition-log.md` (this file)
