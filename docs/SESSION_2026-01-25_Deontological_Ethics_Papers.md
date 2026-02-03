# Session Summary: Deontological Ethics Papers for AI/LLM Values Alignment

**Date:** 2026-01-25
**Focus:** Finding and importing papers on deontological ethics, Kantian ethics, and rule-based approaches for AI/LLM values alignment

---

## Overview

This session searched for and imported papers on **deontological ethics for AI values alignment**, including:
- Kantian ethics and categorical imperative approaches
- Rule-based and duty-based moral reasoning in LLMs
- Deontic logic for AI ethics
- Cross-cultural value alignment
- Legal alignment as a deontological framework

---

## Papers Added (14 Total)

### Core Kantian/Deontological Papers

| Paper | Year | Key Contribution |
|-------|------|------------------|
| McDonald - AI, alignment, and the categorical imperative | 2023 | Critiques feasibility of programming Kantian ethics into AI |
| Lu et al. - Aligning LLM Agents with Rational and Kantian Preferences | 2025 | SFT pipeline for homo moralis (Kantian universalizability); GPT-4o κ=0.05 |
| Atf & Lewis - Kantian-Utilitarian XAI | 2025 | Gamified XAI with separate Kantian and utilitarian modules |
| Kolt et al. - Legal Alignment for Safe and Ethical AI | 2026 | 17-author paper defining legal alignment as rule-based AI governance |

### Moral Reasoning & Evaluation

| Paper | Year | Key Contribution |
|-------|------|------------------|
| Mahajan - Mapping Moral Reasoning in LLMs | 2025 | Identifies 3 LLM reasoning patterns: rule-based, balanced, pragmatic |
| Mohammadi et al. - EvalMORAAL | 2025 | 21-point Western vs non-Western alignment gap in moral surveys |
| Zgliczyński-Cuber - AI Ethical Resonance Hypothesis | 2025 | Uses deontic logic in neuro-symbolic architecture |
| Liu et al. - Cross-cultural value alignment | 2025 | Larger LLMs favor deontological reasoning |

### Theoretical Frameworks

| Paper | Year | Key Contribution |
|-------|------|------------------|
| Wang et al. - Moral growth of LLMs | 2024 | Dewey framework; LLMs can't reach "character stage" |
| Terziyan et al. - Towards ethical evolution | 2025 | Immutable ethical principles for recursive AI |
| Baum & Slavkovik - Aggregation Problems | 2025 | Challenges of combining deontological constraints |
| Sorensen - Operationalizing Pluralistic Values | 2025 | Trade-offs between universalist and pluralist alignment |
| Shen et al. - Alignment and Safety Survey | 2025 | Comprehensive survey of ethical constraint adherence |
| Sameer & Fatima - Insights into Moral Reasoning | 2025 | MCT/MFQ comparison (PDF paywalled) |

---

## Key Findings

### 1. Deontological Approaches in Current Research

- **Kantian universalizability** is being empirically tested (Lu et al. found GPT-4o has weak but significant Kantian moral concern)
- **Larger LLMs tend to favor deontological reasoning** over consequentialist (Liu et al. cross-cultural study)
- **Three behavioral patterns** in LLM moral reasoning: rule-based, balanced, and pragmatic integration (Mahajan)

### 2. Implementation Challenges

- **Kantian ethics requires capacities current AI lacks** (McDonald)
- **Aggregation of multiple deontological constraints** shifts rather than resolves ethical challenges (Baum & Slavkovik)
- **Single alignment objective cannot represent everyone** - tension between universalist and pluralist approaches (Sorensen)

### 3. Emerging Frameworks

- **Legal alignment** as principled rule-following from legitimate institutions (Kolt et al. - 17 major authors)
- **Deontic logic** for encoding obligations/permissions in neuro-symbolic architectures (Zgliczyński-Cuber)
- **Hybrid Kantian-utilitarian systems** with meta-explainers for trade-offs (Atf & Lewis)

### 4. Cross-Cultural Considerations

- **Western vs non-Western alignment gap**: 0.21 absolute difference (r=0.82 vs r=0.61) in EvalMORAAL
- **LLMs overemphasize harm/care and fairness**, underweight loyalty, authority, purity (Sameer & Fatima)

---

## Papers Already in Vault (Pre-existing)

These related papers were already present:
- D'Alessandro (2024) - Deontology and safe AI
- Sanwoolu (2025) - Kantian deontology for AI alignment without moral agency
- Park (2025) - Deontological Keyword Bias
- Mougan (2024) - Kantian Deontology Meets AI Alignment
- Samway (2025) - Are Language Models Consequentialist or Deontological
- Priya (2025) - Deontic Temporal Logic for Formal Verification
- Hou (2023) - Foundational Moral Values for AI Alignment
- Neuman (2025) - PRIME Framework Convergent Ethics
- Brophy (2025) - Black Box Deployed (Functional Criteria for AMAs)
- Jiao (2025) - LLM Ethics Benchmark
- Chakraborty (2025) - Structured Moral Reasoning

---

## Search Strategies Used

Effective search queries for finding deontological ethics papers:
1. `"deontological ethics" LLM AI moral reasoning benchmark evaluation arxiv`
2. `"Kantian" OR "categorical imperative" AI LLM "value alignment" arxiv`
3. `deontic logic AI ethics moral reasoning LLM machine ethics`
4. `"rule-based" ethics AI alignment normative framework deontology`
5. `"normative constraints" LLM alignment moral behavior evaluation`

---

## Future Research Directions

Based on gaps identified:
1. More empirical work on Kantian moral concern parameters across different LLMs
2. Better benchmarks for rule-following vs outcome-based reasoning
3. Cross-cultural deontological frameworks beyond Western/non-Western binary
4. Integration of legal interpretation methods into AI alignment
5. Hybrid systems balancing deontological constraints with consequentialist considerations

---

## Technical Notes

- All papers saved to `papers/` with full YAML frontmatter
- PDFs downloaded to `PDFs/` (13/14 successful, 1 paywalled)
- PDF extracts created in `PDF Extracts/`
- Papers tagged with `deontological_ethics: "Yes"` in frontmatter
- `newtags` field includes "Deontology" for easy filtering
