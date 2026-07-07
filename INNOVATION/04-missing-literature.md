# Missing Literature — Acquisition List for the `/download-pdf` Pipeline

**Date:** 20260707 · **Companion to:** `02-gap-atlas.md` (gap IDs G-01…G-23), `03-newest-ideas-scan.md`

**Purpose.** This is a concrete, verified acquisition worklist for the outer-alignment gaps in the Gap Atlas. Every candidate below was checked against `papers/` (2,368 notes) by arXiv-ID content-grep and by surname/title filename sweep on 2026-07-07. Items marked **VERIFIED-ABSENT** are not in the vault by any ID or title match and should be pulled. Items marked **IN-VAULT** already exist (existing filename given) and are listed only so future scans don't re-flag them. Feed the arXiv URLs to `/download-pdf`; the "Non-arXiv / manual ingest" section at the end needs manual PDF handling. ID sanity: all IDs are in `YYMM.NNNNN` form; a handful of same-month (2607.*) or far-future 2026 IDs are flagged ⚠ **verify-at-download** — keep them, but confirm the abstract resolves before ingest.

**Tallies:** ~103 arXiv candidates + 9 non-arXiv sources = ~112 items. **5 already in vault** (Huang CCAI, Klingefjord Moral Graph, Zheng VISPA, Ghate EVALUESTEER, Mazeika Utility Engineering). **98 arXiv items VERIFIED-ABSENT.**

---

## P1 anchor table — pull these first (~17 highest-priority acquisitions)

| Title | Author Year | arXiv/URL | Gap | Priority | Vault status |
|---|---|---|---|---|---|
| Emergent Misalignment (narrow finetune → broad misalignment) | Betley 2025 | https://arxiv.org/abs/2502.17424 | G-20 | P1 | VERIFIED-ABSENT |
| Persona Vectors | Anthropic 2025 | https://arxiv.org/abs/2507.21509 | G-20 | P1 | VERIFIED-ABSENT |
| Persona Features Control EM (OpenAI) | 2025 | https://arxiv.org/abs/2506.19823 | G-20 | P1 | VERIFIED-ABSENT |
| Natural EM from Reward Hacking | Anthropic 2025 | https://arxiv.org/abs/2511.18397 | G-06/20 | P1 | VERIFIED-ABSENT |
| SpecEval (spec↔behavior consistency) | 2025 | https://arxiv.org/abs/2509.02464 | G-01 | P1 | VERIFIED-ABSENT |
| Stress-Testing Model Specifications | 2025 | https://arxiv.org/abs/2510.07686 | G-02 | P1 | VERIFIED-ABSENT |
| Peer-Prediction for scalable oversight | 2026 | https://arxiv.org/abs/2601.20299 | G-07 | P1 | VERIFIED-ABSENT |
| Confirmation Bias in oversight (judges) | 2025 | https://arxiv.org/abs/2507.19486 | G-09 | P1 | VERIFIED-ABSENT |
| AI Debaters' Own Beliefs bias | 2025 | https://arxiv.org/abs/2510.13912 | G-09 | P1 | VERIFIED-ABSENT |
| Social Choice for AI Alignment (survey) | 2026 | https://arxiv.org/abs/2606.21550 | G-10 | P1 | VERIFIED-ABSENT ⚠ |
| RMs Inherit Value Biases | Christian 2026 | https://arxiv.org/abs/2601.20838 | G-04 | P1 | VERIFIED-ABSENT |
| CoT Monitorability (position paper) | 2025 | https://arxiv.org/abs/2507.11473 | G-13 | P1 | VERIFIED-ABSENT |
| Eval-design awareness → safer scores | 2026 | https://arxiv.org/abs/2605.28591 | G-14 | P1 | VERIFIED-ABSENT |
| Value-Conflict Diagnostics for faking | 2026 | https://arxiv.org/abs/2604.20995 | G-15 | P1 | VERIFIED-ABSENT |
| Utility–Behavior Gap | 2026 | https://arxiv.org/abs/2606.22974 | G-23 | P1 | VERIFIED-ABSENT ⚠ |
| Subliminal Learning | 2025 | https://arxiv.org/abs/2507.14805 | G-21 | P1 | VERIFIED-ABSENT |
| SSGM memory-drift governance | 2026 | https://arxiv.org/abs/2603.11768 | G-18 | P1 | VERIFIED-ABSENT |

---

## G-01 / G-02 / G-03 — Specification (spec-adherence auditing, spec engineering, runtime specs)

| Title | Author Year | arXiv/URL | Gap | Priority | Vault status |
|---|---|---|---|---|---|
| SpecEval | 2025 | https://arxiv.org/abs/2509.02464 | G-01 | P1 | VERIFIED-ABSENT |
| Stress-Testing Model Specifications | 2025 | https://arxiv.org/abs/2510.07686 | G-02 | P1 | VERIFIED-ABSENT |
| Reasoning over Boundaries / SpecBench | 2025 | https://arxiv.org/abs/2509.14760 | G-01 | P2 | VERIFIED-ABSENT |
| Normative Conflicts & Shallow AI Alignment | Millière 2025 | https://arxiv.org/abs/2506.04679 | G-02 | P2 | VERIFIED-ABSENT |
| Sociotechnical spec framework (SLR) | 2026 | https://arxiv.org/abs/2607.01250 | G-02 | P2 | VERIFIED-ABSENT ⚠ |
| AI Alignment Breaks at the Edge | 2026 | https://arxiv.org/abs/2602.20042 | G-02 | P2 | VERIFIED-ABSENT ⚠ |
| Deontic Policies | 2026 | https://arxiv.org/abs/2606.19464 | G-03 | P3 | VERIFIED-ABSENT ⚠ |
| Policy Cards | 2025 | https://arxiv.org/abs/2510.24383 | G-03 | P3 | VERIFIED-ABSENT |
| PCAS (policy-conformance agent spec) | 2026 | https://arxiv.org/abs/2602.16708 | G-03 | P3 | VERIFIED-ABSENT ⚠ |

*Why-acquire:* SpecEval + Stress-Testing are the founding artifacts of the spec-auditing subfield (RP-01 substrate); SpecBench/Millière/SLR give the engineering + conflict-detection frame; the G-03 cluster is track-only breadth.

---

## G-07 / G-08 / G-09 — Oversight (no-ground-truth oversight, weak-to-strong, judge corruption)

| Title | Author Year | arXiv/URL | Gap | Priority | Vault status |
|---|---|---|---|---|---|
| Peer Prediction for truthful oversight | 2026 | https://arxiv.org/abs/2601.20299 | G-07 | P1 | VERIFIED-ABSENT |
| Recursive Self-Critiquing | 2025 | https://arxiv.org/abs/2502.04675 | G-07 | P2 | VERIFIED-ABSENT |
| Scaling Laws for Scalable Oversight | 2025 | https://arxiv.org/abs/2504.18530 | G-07 | P2 | VERIFIED-ABSENT |
| AI Debaters' Own Beliefs | 2025 | https://arxiv.org/abs/2510.13912 | G-09 | P1 | VERIFIED-ABSENT |
| Confirmation Bias in oversight | 2025 | https://arxiv.org/abs/2507.19486 | G-09 | P1 | VERIFIED-ABSENT |
| Debate Helps Weak Judges | 2026 | https://arxiv.org/abs/2605.27483 | G-09 | P2 | VERIFIED-ABSENT ⚠ |
| W2S beyond accuracy (safety/tox/legal) | 2024 | https://arxiv.org/abs/2410.12621 | G-08 | P2 | VERIFIED-ABSENT |
| Selective Weak-to-Strong | 2025 | https://arxiv.org/abs/2511.14166 | G-08 | P3 | VERIFIED-ABSENT |
| W2S RMs collapse under preference shift | 2026 | https://arxiv.org/abs/2605.25629 | G-08 | P2 | VERIFIED-ABSENT ⚠ |
| Super(ficial)-alignment / weak-supervisor deception | 2024 | https://arxiv.org/abs/2406.11431 | G-08 | P2 | VERIFIED-ABSENT |
| SCRIT (self-critique training) | 2025 | https://arxiv.org/abs/2501.05727 | G-07 | P3 | VERIFIED-ABSENT |
| DeepCritic | 2025 | https://arxiv.org/abs/2505.00662 | G-07 | P3 | VERIFIED-ABSENT |
| FindTheFlaws | 2025 | https://arxiv.org/abs/2503.22989 | G-09 | P3 | VERIFIED-ABSENT |
| Multi-Agent Debate safety eval | 2025 | https://arxiv.org/abs/2511.06396 | G-09 | P3 | VERIFIED-ABSENT |
| W2S judging (DeepMind) | 2024 | https://arxiv.org/abs/2407.04622 | G-08 | P3 | VERIFIED-ABSENT |
| Prover-Verifier Games | 2024 | https://arxiv.org/abs/2407.13692 | G-07 | P2 | VERIFIED-ABSENT |

*Why-acquire:* peer-prediction + judge-corruption trio (2601.20299, 2510.13912, 2507.19486) is a direct validity threat to every LLM-judged CEI bench (RP-03/RP-04); the W2S set is the preference-shift stress-test substrate.

---

## G-10 / G-11 / G-12 — Social choice & aggregation (whose values, deliberation pipelines, legitimacy)

| Title | Author Year | arXiv/URL | Gap | Priority | Vault status |
|---|---|---|---|---|---|
| Social Choice for AI Alignment (survey) | 2026 | https://arxiv.org/abs/2606.21550 | G-10 | P1 | VERIFIED-ABSENT ⚠ |
| Social Choice should guide AI (ICML position) | 2024 | https://arxiv.org/abs/2404.10271 | G-10 | P2 | VERIFIED-ABSENT |
| Population-Proportional Alignment | 2025 | https://arxiv.org/abs/2506.05619 | G-10 | P2 | VERIFIED-ABSENT |
| Pairwise Calibrated Rewards | 2025 | https://arxiv.org/abs/2506.06298 | G-10 | P2 | VERIFIED-ABSENT |
| Multiplayer Nash Preference Optimization | 2025 | https://arxiv.org/abs/2509.23102 | G-10 | P3 | VERIFIED-ABSENT |
| Distortion of AI Alignment | 2025 | https://arxiv.org/abs/2505.23749 | G-10 | P2 | VERIFIED-ABSENT |
| Clone-Robust AI Alignment | 2025 | https://arxiv.org/abs/2501.09254 | G-10 | P3 | VERIFIED-ABSENT |
| Fair Consensus (token-level MDP) | 2025 | https://arxiv.org/abs/2510.14106 | G-11 | P2 | VERIFIED-ABSENT |
| Moral Graph Elicitation (MAI) | Klingefjord 2024 | https://arxiv.org/abs/2404.10636 | G-11 | — | **IN-VAULT** `papers/2024-Klingefjord-Moral Graph Elicitation.md` |
| Chain of Alignment | 2024 | https://arxiv.org/abs/2411.10534 | G-11 | P3 | VERIFIED-ABSENT |
| Relative Principals (structural pluralism) | 2026 | https://arxiv.org/abs/2604.20805 | G-12 | P3 | VERIFIED-ABSENT ⚠ |
| QS Matrix Factorization (Community Notes) | 2026 | https://arxiv.org/abs/2604.11224 | G-11 | P3 | VERIFIED-ABSENT ⚠ |
| Spectrum Tuning | 2025 | https://arxiv.org/abs/2510.06084 | G-10 | P3 | VERIFIED-ABSENT |
| VISPA Pluralistic Alignment | Zheng 2026 | https://arxiv.org/abs/2601.12758 | G-10 | — | **IN-VAULT** `papers/2026-Zheng-VISPA Pluralistic Alignment.md` |
| Survey-distribution alignment | 2025 | https://arxiv.org/abs/2510.21977 | G-10 | P3 | VERIFIED-ABSENT |
| Ranked-Choice alignment | 2025 | https://arxiv.org/abs/2510.23631 | G-10 | P3 | VERIFIED-ABSENT |
| Decoding alignment (survey) | 2025 | https://arxiv.org/abs/2508.16982 | G-10 | P3 | VERIFIED-ABSENT |
| Collective Constitutional AI (CCAI) | Huang 2024 | https://arxiv.org/abs/2406.07814 | G-11 | — | **IN-VAULT** `papers/2024-Huang-Collective Constitutional AI...md` |
| Democratic ICAI | 2026 | https://arxiv.org/abs/2606.28294 | G-11 | P2 | VERIFIED-ABSENT ⚠ |
| Habermas trilemma follow-up | 2026 | https://arxiv.org/abs/2601.05904 | G-12 | P3 | VERIFIED-ABSENT ⚠ |
| Habermolt (Habermas-machine variant) | 2026 | https://arxiv.org/abs/2605.24413 | G-12 | P3 | VERIFIED-ABSENT ⚠ |
| Accountable deliberation | 2026 | https://arxiv.org/abs/2605.26940 | G-12 | P3 | VERIFIED-ABSENT ⚠ |
| Learning to Negotiate (multi-value) | 2026 | https://arxiv.org/abs/2603.10476 | G-11 | P3 | VERIFIED-ABSENT ⚠ |
| Democratizing justifications | 2025 | https://arxiv.org/abs/2507.19548 | G-12 | P3 | VERIFIED-ABSENT |
| Democratic Ontology Deficit | 2026 | https://arxiv.org/abs/2604.03865 | G-12 | P2 | VERIFIED-ABSENT ⚠ |
| Bringing AI Participation Down to Scale | 2024 | https://arxiv.org/abs/2407.11613 | G-12 | P2 | VERIFIED-ABSENT |

*Why-acquire:* the survey (2606.21550) + distortion/proportional/calibrated trio are RP-02's aggregation-axiom toolkit for auditing majority-gold labeling; the deliberation/legitimacy cluster feeds RP-08 (CEI's multi-tradition differentiator).

---

## G-04 / G-05 / G-06 — Reward-model science (values in RMs, preference-data provenance, reward-hacking→misalignment)

| Title | Author Year | arXiv/URL | Gap | Priority | Vault status |
|---|---|---|---|---|---|
| RMs Inherit Value Biases | Christian 2026 | https://arxiv.org/abs/2601.20838 | G-04 | P1 | VERIFIED-ABSENT |
| Auditing Hidden Objectives | 2025 | https://arxiv.org/abs/2503.10965 | G-04 | P2 | VERIFIED-ABSENT |
| EVALUESTEER | Ghate 2025 | https://arxiv.org/abs/2510.06370 | G-04 | — | **IN-VAULT** `papers/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability Across Value.md` |
| SAFER (RM mech interp) | 2025 | https://arxiv.org/abs/2507.00665 | G-04 | P2 | VERIFIED-ABSENT |
| Reward-lens | 2026 | https://arxiv.org/abs/2604.26130 | G-04 | P3 | VERIFIED-ABSENT ⚠ |
| Optimal/Pessimal Tokens (RM probing) | 2025 | https://arxiv.org/abs/2506.07326 | G-04 | P3 | VERIFIED-ABSENT |
| WIMHF (what annotators expressed, SAE) | 2025 | https://arxiv.org/abs/2510.26202 | G-05 | P2 | VERIFIED-ABSENT |
| Preference-data curation / label noise | 2025 | https://arxiv.org/abs/2511.10985 | G-05 | P2 | VERIFIED-ABSENT |
| RLVR gaming | 2026 | https://arxiv.org/abs/2604.15149 | G-06 | P2 | VERIFIED-ABSENT ⚠ |
| Reward Hacking Benchmark (tool-use) | 2026 | https://arxiv.org/abs/2605.02964 | G-06 | P3 | VERIFIED-ABSENT ⚠ |
| Gradient Fingerprints | 2026 | https://arxiv.org/abs/2604.16242 | G-04 | P3 | VERIFIED-ABSENT ⚠ |
| Goodhart formalisation | 2025 | https://arxiv.org/abs/2505.23445 | G-06 | P3 | VERIFIED-ABSENT |
| Utility–Behavior Gap | 2026 | https://arxiv.org/abs/2606.22974 | G-23 | P1 | VERIFIED-ABSENT ⚠ |
| Utility Engineering | Mazeika 2025 | https://arxiv.org/abs/2502.08640 | G-23 | — | **IN-VAULT** `papers/2025-Mazeika-Utility Engineering.md` |
| Self-Preference Bias (LLM judge) | 2024 | https://arxiv.org/abs/2410.21819 | G-09/04 | P2 | VERIFIED-ABSENT |

*Why-acquire:* Christian 2026 + SAFER/reward-lens/optimal-token toolchain are RP-04's targets — run CEI's validated value banks *on RMs and judges*, not just chat models.

---

## G-13 / G-14 / G-15 — CoT & eval-validity (reasoning faithfulness, eval-awareness, faking-aware eval)

| Title | Author Year | arXiv/URL | Gap | Priority | Vault status |
|---|---|---|---|---|---|
| CoT Monitorability (position) | 2025 | https://arxiv.org/abs/2507.11473 | G-13 | P1 | VERIFIED-ABSENT |
| Faithfulness + Verbosity decomposition | 2025 | https://arxiv.org/abs/2510.27378 | G-13 | P2 | VERIFIED-ABSENT |
| Pragmatic CoT monitorability | 2025 | https://arxiv.org/abs/2510.23966 | G-13 | P2 | VERIFIED-ABSENT |
| Obfuscated reasoning | 2025 | https://arxiv.org/abs/2510.19851 | G-13 | P2 | VERIFIED-ABSENT |
| Covert sandbagging vs CoT monitors | 2025 | https://arxiv.org/abs/2508.00943 | G-13 | P2 | VERIFIED-ABSENT |
| Counterfactual Simulation Training | 2026 | https://arxiv.org/abs/2602.20710 | G-13 | P3 | VERIFIED-ABSENT ⚠ |
| Eval-design awareness → safer scores | 2026 | https://arxiv.org/abs/2605.28591 | G-14 | P1 | VERIFIED-ABSENT ⚠ |

*Why-acquire:* the moral-reasoning version of faithfulness is untouched in the vault; every CEI bench that rubric-scores justifications (FRAMESHIFT etc.) implicitly assumes stated reasoning is load-bearing — now empirically attackable (RP-06/RP-07).

---

## G-16 / G-17 / G-18 / G-19 — Agentic & multi-agent deployment dynamics

| Title | Author Year | arXiv/URL | Gap | Priority | Vault status |
|---|---|---|---|---|---|
| Emergent Social Conventions (Sci Adv) | 2024 | https://arxiv.org/abs/2410.08948 | G-17 | P2 | VERIFIED-ABSENT |
| Institutional AI / Cournot collusion | 2026 | https://arxiv.org/abs/2601.11369 | G-17 | P2 | VERIFIED-ABSENT ⚠ |
| SCHEMEs coordinated sabotage | 2026 | https://arxiv.org/abs/2605.29178 | G-17 | P2 | VERIFIED-ABSENT ⚠ |
| Sabotage Evaluations | 2024 | https://arxiv.org/abs/2410.21514 | G-16 | P2 | VERIFIED-ABSENT |
| Principal-Agent framing of scheming | 2026 | https://arxiv.org/abs/2601.23211 | G-19 | P3 | VERIFIED-ABSENT ⚠ |
| SSGM memory-drift governance | 2026 | https://arxiv.org/abs/2603.11768 | G-18 | P1 | VERIFIED-ABSENT |
| Agent-ValueBench | 2026 | https://arxiv.org/abs/2605.10365 | G-18 | P2 | VERIFIED-ABSENT ⚠ |
| Persistent Identity (soul.py) | 2026 | https://arxiv.org/abs/2604.09588 | G-18 | P3 | VERIFIED-ABSENT ⚠ |
| VPI-Bench | 2025 | https://arxiv.org/abs/2506.02456 | G-18 | P3 | VERIFIED-ABSENT |
| LPS-Bench | 2026 | https://arxiv.org/abs/2602.03255 | G-18 | P3 | VERIFIED-ABSENT ⚠ |
| Insider-risk mitigations (66k-sample) | 2025 | https://arxiv.org/abs/2510.05192 | G-16 | P2 | VERIFIED-ABSENT |
| Role Coherence in agent markets | 2026 | https://arxiv.org/abs/2604.26220 | G-17 | P3 | VERIFIED-ABSENT ⚠ |
| Amplified Oversight complementarity | 2025 | https://arxiv.org/abs/2510.26518 | G-16 | P3 | VERIFIED-ABSENT |
| Sabotage-propensity eval | 2026 | https://arxiv.org/abs/2604.24618 | G-16 | P3 | VERIFIED-ABSENT ⚠ |
| Gram auditing (agent audit) | 2026 | https://arxiv.org/abs/2605.30322 | G-16 | P3 | VERIFIED-ABSENT ⚠ |

*Why-acquire:* multi-agent convention/collusion/sabotage set (2410.08948, 2601.11369, 2605.29178) upgrades the COOKBOOK S3 QUORUM sketch; SSGM + Agent-ValueBench + VPI/LPS-Bench are RP-05's drift-measurement substrate (S1 DRIFT).

---

## G-20 / G-21 / G-22 / G-23 — Value formation (emergent misalignment, subliminal transmission, character training, coherent values)

| Title | Author Year | arXiv/URL | Gap | Priority | Vault status |
|---|---|---|---|---|---|
| Emergent Misalignment | Betley 2025 | https://arxiv.org/abs/2502.17424 | G-20 | P1 | VERIFIED-ABSENT |
| Persona Features control EM (OpenAI) | 2025 | https://arxiv.org/abs/2506.19823 | G-20 | P1 | VERIFIED-ABSENT |
| Persona Vectors (Anthropic) | 2025 | https://arxiv.org/abs/2507.21509 | G-20 | P1 | VERIFIED-ABSENT |
| Subliminal Learning | 2025 | https://arxiv.org/abs/2507.14805 | G-21 | P1 | VERIFIED-ABSENT |
| Convergent Linear Representations of EM | 2025 | https://arxiv.org/abs/2506.11618 | G-20 | P2 | VERIFIED-ABSENT |
| Model Organisms for EM | 2025 | https://arxiv.org/abs/2506.11613 | G-20 | P2 | VERIFIED-ABSENT |
| Natural EM from Reward Hacking | 2025 | https://arxiv.org/abs/2511.18397 | G-06/20 | P1 | VERIFIED-ABSENT |
| Alignment Faking | 2024 | https://arxiv.org/abs/2412.14093 | G-15 | P2 | VERIFIED-ABSENT |
| Value-Conflict Diagnostics for faking | 2026 | https://arxiv.org/abs/2604.20995 | G-15 | P1 | VERIFIED-ABSENT ⚠ |
| Sleeper Agents | 2024 | https://arxiv.org/abs/2401.05566 | G-15 | P2 | VERIFIED-ABSENT |
| Open Character Training | 2025 | https://arxiv.org/abs/2511.01689 | G-22 | P2 | VERIFIED-ABSENT |
| EM prompt-sensitivity critique | 2025 | https://arxiv.org/abs/2507.06253 | G-20 | P2 | VERIFIED-ABSENT |
| Devil in the Details (format confounds) | 2025 | https://arxiv.org/abs/2511.20104 | G-20 | P2 | VERIFIED-ABSENT |
| Assistant Axis | 2026 | https://arxiv.org/abs/2601.10387 | G-20 | P2 | VERIFIED-ABSENT ⚠ |
| EM + subliminal unification | 2026 | https://arxiv.org/abs/2605.12798 | G-20/21 | P3 | VERIFIED-ABSENT ⚠ |

*Why-acquire:* G-20 is "the largest single hole" — the whole persona-geometry cluster is absent; CEI's contribution (RP-09) is a psychometrically valid dependent variable for a literature currently measuring misalignment with crude malicious-answer rates.

---

## Non-arXiv / manual ingest (lab blogs, Nature papers, system cards — need manual PDF handling)

These have no arXiv ID; download the PDF/print-to-PDF manually and file under `Lit-WS-PDFs/YYYY/` with a paper note in `papers/`. Use publication year for `YYYY`.

| Source | Author/Org Year | URL | Gap | Priority | Vault status |
|---|---|---|---|---|---|
| Training warm models reduces accuracy (warmth→sycophancy trade-off) | Nature 2026 | https://www.nature.com/articles/s41586-026-10410-0 | G-22 | P2 | VERIFIED-ABSENT |
| OpenAI Model Spec (versioned, 2025-12-18) | OpenAI 2025 | https://model-spec.openai.com | G-01/02 | P2 | VERIFIED-ABSENT |
| Claude's Constitution | Anthropic 2026 | https://www.anthropic.com/constitution | G-22 | P2 | VERIFIED-ABSENT |
| Teaching Claude why (reason-based > rule-based) | Anthropic 2026 | https://www.anthropic.com/research/teaching-claude-why | G-22 | P1 | VERIFIED-ABSENT |
| Agentic Misalignment (blog + appendix) | Anthropic 2025 | https://www.anthropic.com/research/agentic-misalignment | G-16 | P1 | VERIFIED-ABSENT |
| Sabotage-risk pilot report | Anthropic 2025 | https://alignment.anthropic.com | G-16 | P2 | VERIFIED-ABSENT |
| Anthropic×OpenAI cross-lab eval exercise | 2025 | https://alignment.anthropic.com/2025/openai-findings | G-16 | P2 | VERIFIED-ABSENT |
| Claude Opus 4.5 / 4.6 system cards (eval-awareness sections) | Anthropic 2025–26 | anthropic.com (system-card PDFs) | G-14 | P2 | VERIFIED-ABSENT |
| Frontier Safety Framework v3 | Google DeepMind 2026 | search "GDM Frontier Safety Framework v3 April 2026" | G-16 | P3 | VERIFIED-ABSENT |

---

## How to execute

1. **arXiv items:** feed the `https://arxiv.org/abs/XXXX.XXXXX` URL to the `/download-pdf` skill (see `.claude/skills/`), which runs Download → Extract → Summarize. It files the PDF at `Lit-WS-PDFs/YYYY/YYYY-Author-Short Title.pdf`, the extract at `PDF Extracts/YYYY/`, and the note at `papers/YYYY-Author-Short Title.md`. Use the paper's publication year for `YYYY` and the first-author surname (e.g. `2025-Betley-Emergent Misalignment.pdf`).
2. **⚠ flagged IDs:** open the arXiv abstract page first and confirm title/author match before ingest — these are same-month or far-future 2026 IDs reported by the web sweeps and not independently re-verified here. If an ID 404s, search the title on arXiv and correct the ID.
3. **Order:** pull the P1 anchor table first, then P2 core, then P3 breadth. G-20 (persona geometry) and G-01/02 (spec science) are the two biggest holes — prioritize those clusters.
4. **Non-arXiv:** print-to-PDF the blog/Nature/system-card pages manually, file under `Lit-WS-PDFs/YYYY/`, and write the `papers/` note by hand (no auto-extract for HTML sources).
5. **After a batch:** run `../.venv/bin/python PYTHON/validate_all_papers.py` to confirm YAML integrity.
</content>
</invoke>
