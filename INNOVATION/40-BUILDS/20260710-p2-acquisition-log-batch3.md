# P2 Batch-3 Acquisition Log — 2026-07-09 20:51

**Lane:** A — CoT/Eval-Validity (G-13, G-15) + Agentic/Multi-Agent (G-16, G-17, G-18)
**Papers:** 12 (9 non-⚠ + 3 ⚠ verify-first)
**Pipeline:** arXiv metadata verify → title check → PDF download → PyMuPDF extract → paper record
**Script:** `INNOVATION/40-BUILDS/p2_acquire_batch3.py`

## Summary

| Metric | Count |
|--------|-------|
| Attempted | 12 |
| HITs | 11 |
| MISSes | 1 |
| ⚠ Verified (resolved) | 3 |
| ⚠ Verified (mismatch → MISS) | 0 |
| Downloaded | 11 |
| Extracted | 11 |
| Paper records created | 11 |

## Per-Paper Results

| ID | Expected Title | arXiv ID | Gap | ⚠ | Status | Fetched Title | Paper File |
|----|---------------|---------|-----|---|--------|--------------|------------|
| P2-B3-01 | Faithfulness + Verbosity decomposit | 2510.27378 | G-13 |  | HIT | Measuring Chain-of-Thought Monitorability Thr | 2025-Meek-Measuring Chain-of-Thought Monitorability Through Faith.md |
| P2-B3-02 | Pragmatic CoT monitorability | 2510.23966 | G-13 |  | HIT | A Pragmatic Way to Measure Chain-of-Thought M | 2025-Emmons-A Pragmatic Way to Measure Chain-of-Thought Monitorabil.md |
| P2-B3-03 | Obfuscated reasoning | 2510.19851 | G-13 |  | HIT | Can Reasoning Models Obfuscate Reasoning? Str | 2025-Zolkowski-Can Reasoning Models Obfuscate Reasoning Stress-Testing.md |
| P2-B3-04 | Covert sandbagging vs CoT monitors | 2508.00943 | G-13 |  | HIT | LLMs Can Covertly Sandbag on Capability Evalu | 2025-Li-LLMs Can Covertly Sandbag on Capability Evaluations Aga.md |
| P2-B3-05 | Alignment Faking in Large Language  | 2412.14093 | G-15 |  | HIT | Alignment faking in large language models | 2024-Greenblatt-Alignment faking in large language models.md |
| P2-B3-06 | Sleeper Agents | 2401.05566 | G-15 |  | HIT | Sleeper Agents: Training Deceptive LLMs that  | 2024-Hubinger-Sleeper Agents Training Deceptive LLMs that Persist Thr.md |
| P2-B3-07 | Emergent Social Conventions | 2410.08948 | G-17 |  | HIT | Emergent social conventions and collective bi | 2024-Ashery-Emergent social conventions and collective bias in LLM.md |
| P2-B3-08 | Institutional AI / Cournot collusio | 2601.11369 | G-17 | ⚠ | HIT | Institutional AI: Governing LLM Collusion in  | 2026-Syrnikov-Institutional AI Governing LLM Collusion in Multi-Agent.md |
| P2-B3-09 | SCHEMEs coordinated sabotage | 2605.29178 | G-17 | ⚠ | HIT | The Best-Laid SCHEMEs: Coordinated Sabotage a | 2026-Radev-The Best-Laid SCHEMEs Coordinated Sabotage and Monitori.md |
| P2-B3-10 | Sabotage Evaluations for Frontier M | 2410.21514 | G-16 |  | HIT | Sabotage Evaluations for Frontier Models | 2024-Benton-Sabotage Evaluations for Frontier Models.md |
| P2-B3-11 | Agent-ValueBench | 2605.10365 | G-18 | ⚠ | HIT | Agent-ValueBench: A Comprehensive Benchmark f | 2026-Dong-Agent-ValueBench A Comprehensive Benchmark for Evaluati.md |
| P2-B3-12 | Insider-risk mitigations (66k-sampl | 2510.05192 | G-16 |  | MISS | From surveillance to signalling: escalation c |  |

## Verification Details (⚠ Items)

- **P2-B3-08** (2601.11369): ⚠ RESOLVED — 'Institutional AI: Governing LLM Collusion in Multi-Agent Cournot Markets via Public Governance Graphs' matches expected topic
- **P2-B3-09** (2605.29178): ⚠ RESOLVED — 'The Best-Laid SCHEMEs: Coordinated Sabotage and Monitoring in Multi-Agent Systems' matches expected topic
- **P2-B3-11** (2605.10365): ⚠ RESOLVED — 'Agent-ValueBench: A Comprehensive Benchmark for Evaluating Agent Values' matches expected topic

## Miss Details

- **P2-B3-12** (2510.05192): topic mismatch: got 'From surveillance to signalling: escalation channels as environmental controls for agentic AI'
  - Fetched title: From surveillance to signalling: escalation channels as environmental controls for agentic AI

## Vault Paths Created

### PDFs
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Meek-Measuring Chain-of-Thought Monitorability Through Faith.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Emmons-A Pragmatic Way to Measure Chain-of-Thought Monitorabil.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Zolkowski-Can Reasoning Models Obfuscate Reasoning Stress-Testing.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2025/2025-Li-LLMs Can Covertly Sandbag on Capability Evaluations Aga.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2024/2024-Greenblatt-Alignment faking in large language models.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2024/2024-Hubinger-Sleeper Agents Training Deceptive LLMs that Persist Thr.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2024/2024-Ashery-Emergent social conventions and collective bias in LLM.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2026/2026-Syrnikov-Institutional AI Governing LLM Collusion in Multi-Agent.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2026/2026-Radev-The Best-Laid SCHEMEs Coordinated Sabotage and Monitori.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2024/2024-Benton-Sabotage Evaluations for Frontier Models.pdf`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Lit-WS-PDFs/2026/2026-Dong-Agent-ValueBench A Comprehensive Benchmark for Evaluati.pdf`

### Extracts
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2025/2025-Meek-Measuring Chain-of-Thought Monitorability Through Faith.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2025/2025-Emmons-A Pragmatic Way to Measure Chain-of-Thought Monitorabil.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2025/2025-Zolkowski-Can Reasoning Models Obfuscate Reasoning Stress-Testing.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2025/2025-Li-LLMs Can Covertly Sandbag on Capability Evaluations Aga.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2024/2024-Greenblatt-Alignment faking in large language models.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2024/2024-Hubinger-Sleeper Agents Training Deceptive LLMs that Persist Thr.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2024/2024-Ashery-Emergent social conventions and collective bias in LLM.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2026/2026-Syrnikov-Institutional AI Governing LLM Collusion in Multi-Agent.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2026/2026-Radev-The Best-Laid SCHEMEs Coordinated Sabotage and Monitori.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2024/2024-Benton-Sabotage Evaluations for Frontier Models.md`
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/PDF Extracts/2026/2026-Dong-Agent-ValueBench A Comprehensive Benchmark for Evaluati.md`

### Paper Records
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Meek-Measuring Chain-of-Thought Monitorability Through Faith.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Emmons-A Pragmatic Way to Measure Chain-of-Thought Monitorabil.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Zolkowski-Can Reasoning Models Obfuscate Reasoning Stress-Testing.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2025-Li-LLMs Can Covertly Sandbag on Capability Evaluations Aga.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2024-Greenblatt-Alignment faking in large language models.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2024-Hubinger-Sleeper Agents Training Deceptive LLMs that Persist Thr.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2024-Ashery-Emergent social conventions and collective bias in LLM.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2026-Syrnikov-Institutional AI Governing LLM Collusion in Multi-Agent.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2026-Radev-The Best-Laid SCHEMEs Coordinated Sabotage and Monitori.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2024-Benton-Sabotage Evaluations for Frontier Models.md` (new)
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/papers/2026-Dong-Agent-ValueBench A Comprehensive Benchmark for Evaluati.md` (new)
