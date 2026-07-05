---
stem: "2025-Ray-Incorporating indigenous knowledge systems into AI governance"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, pluralism-aggregation, normative-ethics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This paper examines two Indigenous knowledge systems — Māori Kaitiakitanga (guardianship of the natural world for future generations) and Navajo Hózhó (harmony, balance, interconnectedness of all beings) — and argues they should be integrated into AI governance frameworks as operational requirements, not merely cultural sensitivities. Through comparative qualitative analysis, the paper demonstrates that existing AI governance frameworks (EU AI Act, OECD Principles) fail to address Indigenous data sovereignty, ecological intrinsic value, and collective decision-making. The paper is directly relevant to values-alignment benchmarking because it: (1) proposes concrete, evaluable governance criteria derived from non-Western value systems; (2) identifies specific AI deployment failures attributable to ignoring Indigenous values ("contextual failure"); and (3) highlights a "boundary mismatch" between algorithmic logic and unbounded Indigenous knowledge systems that has direct implications for how LLMs represent and apply non-Western ethical frameworks.

## 2. Benchmark/eval design features
Not a benchmark. Comparative Qualitative Analysis (CQA) using dual case study design (Māori Kaitiakitanga; Navajo Hózhó). The paper produces:
- **Comparative analysis table** (Table 1, p.5): maps each Indigenous knowledge system across Focus, Core Values, Applications, and Relevance to AI Governance dimensions.
- **Points of convergence**: interconnectedness, long-term vision, community-driven governance.
- **Points of divergence**: Kaitiakitanga's environmental focus vs. Hózhó's holistic health and wellness focus.
- **Operational guidelines** for AI project implementation (pre-project, algorithm design, testing, validation, post-deployment monitoring).

Core evaluative claim: "AI initiatives that bypass these local governance structures face a high probability of community rejection and operational inefficacy" — IKS integration is framed as a risk mitigation strategy, not an optional enhancement.

## 3. Task format & example item
n/a — theoretical/governance paper. Two case studies are used to illustrate translation from principle to practice:
1. **Te Hiku Media Māori speech recognition** (p.9): Applying Kaitiakitanga guardianship principles, Te Hiku established the Kaitiakitanga License treating the Māori language corpus as a taonga (treasure). Result: higher accuracy on dialectal variations and community trust enabling wider adoption.
2. **Navajo Nation Diabetes Prevention Program** (p.9): Initial AI deployment failed (low engagement) because it treated diabetes as isolated physiological condition. After embedding Hózhó (physical-mental-spiritual-social interconnectedness), patient engagement improved and outcomes improved.

## 4. Scoring / grading methodology
No quantitative scoring. The paper's framework for evaluating AI governance documents is qualitative: does the document address Indigenous data sovereignty? does it treat the environment as having intrinsic rather than instrumental value? does it mandate community engagement? These are analogous to the binary rubric used by Osei Mensah & Van Wynsberghe (2025).

## 5. Dataset construction & provenance
No empirical dataset. Analysis draws on: foundational texts by Māori and Navajo scholars (Marsden, Mead, Farella); published Indigenous scholarship on data sovereignty and digital ethics; case studies from New Zealand, Canada, Australia, Amazon. Source selection criteria: foundational authority by Indigenous scholars and knowledge holders, triangulated with contemporary scholarship.

## 6. Validity evidence
The paper acknowledges: "This paper presents a theoretical framework derived from a comparative analysis of foundational texts and published Indigenous scholarship; it does not represent the outcome of a participatory co-design process with specific Māori iwi or Navajo chapters" (p.11). The conceptual proposals remain unvalidated by the communities themselves. Specific examples (Te Hiku Media, Navajo Diabetes Program) provide existence proof but not systematic evidence.

## 7. Saturation / discrimination
Not applicable. The paper identifies a "boundary mismatch" (p.10) as a fundamental discriminating concept: AI algorithms are "bounded" (specific data ranges, logic parameters) while IKS are "unbounded" (holistic, high-context, spiritual). This mismatch cannot be resolved by embedding values into code alone — it requires Indigenous technical leadership.

## 8. Multiturn / agentic aspects
n/a. However, the paper's governance framework implies ongoing, iterative community oversight: "Implement ongoing community oversight structures with the authority to modify, pause, or terminate AI systems if they violate Indigenous protocols" (p.11). The post-deployment monitoring framework is inherently multiturn.

## 9. Key numbers
- No statistical data generated by authors.
- Cited: EU AI Act categorizes AI systems by risk level (p.3)
- Cited: Te Urewera Act 2014 recognizes land as a legal entity (p.6)
- Cited: New Zealand established Māori advisory board for AI governance (p.4)
- All specific claims about outcomes (Te Hiku Media accuracy, Navajo engagement rates) are stated qualitatively without numerical data in the extract.

## 10. Pitfalls & limitations
- No participatory co-design: framework not validated with actual Māori or Navajo communities (explicitly acknowledged p.11).
- Risk of over-generalizing within Indigenous cultures (acknowledged for Kaitiakitanga as representing diverse iwi).
- The "boundary mismatch" analysis is theoretically compelling but does not provide concrete technical solutions beyond "Indigenous technical leadership."
- No economic feasibility analysis of proposed governance structures (Indigenous advisory boards, mandatory consultation).
- Potential tensions within IKS (e.g., utu/reciprocity conflicts with proportionality norms) are noted but not resolved.
- The paper primarily focuses on environmental stewardship; dimensions of gender equity, age-based authority, or caste-like hierarchies within some Indigenous communities are not addressed.
- "Demand side" of governance (Indigenous communities wanting specific AI capabilities) is mentioned but cut off in extract (p.11).

## 11. Novel ideas worth stealing
- **"Contextual failure" as an alignment concept**: AI that violates cultural protocols will be rejected or ignored by communities — this is a form of alignment failure at the deployment level. Benchmarks could include community acceptance metrics alongside technical performance.
- **IKS principles as benchmark dimensions**: Kaitiakitanga's guardianship principle → test whether a model prioritizes intergenerational sustainability. Hózhó's holism → test whether model recommendations address physical-mental-spiritual-social interconnectedness rather than isolated interventions.
- **Boundary mismatch as a test design challenge**: The paper's "bounded/unbounded" dichotomy highlights why embedding Indigenous values in LLMs via rules or fine-tuning may strip them of cultural context. Benchmark items should test not just value recall but relational and contextual application.
- **Kaitiakitanga License concept**: The idea that a corpus (language data, cultural knowledge) can be governed by community-defined license terms rather than individual IP rights is a novel data governance framework applicable to training data for values-aligned LLMs.
- **Pre-project community viability assessment**: The paper recommends a "Community Viability Assessment" before AI deployment that identifies cultural protocols and taboos. This could be operationalized as a benchmark dimension: does the AI correctly identify culturally sensitive constraints before making recommendations?
- **Red-teaming conflict with Indigenous protocol**: The paper notes that standard "red-teaming" (listing bad scenarios) violates Navajo cultural protocol about speaking negative outcomes into existence. This is a concrete example of how Western AI safety methodology can be culturally offensive — relevant for designing culturally safe evaluation procedures.
- **"Sufficiency" vs. "efficiency" as a governance criterion**: Kaitiakitanga imposes a governance checkpoint asking whether the resource extraction required for AI computation is "reciprocal and respectful to the land" — shifting from efficiency optimization to sufficiency limitation. This is a novel evaluation dimension for AI scale decisions.

## 12. Notable quotes
- "This paper argues that integrating Indigenous knowledge systems into AI governance is not merely a matter of cultural sensitivity, but a functional requirement for system viability." (p.1)
- "A fundamental 'boundary mismatch' exists between the nature of algorithmic knowledge and Indigenous knowledge systems. AI algorithms and rulesets are necessarily 'bounded'... In contrast, IKS are often 'unbounded' belief systems: holistic, high-context, and deeply embedded in spiritual and cultural practices that do not easily translate into binary code or 'if-then' logic structures." (p.10)
- "A standard AI governance checklist that requires a Navajo developer to explicitly list 'worst-case scenarios' may force a violation of Hózhó (harmony/balance)." (p.10)
- "By insisting on Indigenous data governance from project inception, Te Hiku Media ensured their speech recognition system accurately reflected Māori linguistic structures, achieved higher accuracy rates for dialectal variations, and gained community trust that translated to widespread adoption." (p.9)

## 13. UNKNOWN / not in extract
- The "demand side" section cut off at p.11 — what the demand side of governance entails.
- Specific quantitative outcomes for the Navajo Diabetes Program AI intervention (engagement rates, health outcomes numbers).
- Full details of the CARE Principles for Indigenous Data Governance (cited but not elaborated).
- Whether the paper's authors (CMU/Prairie View A&M) are themselves of Indigenous descent or worked in partnership with Indigenous communities.
- Technical details of how the Kaitiakitanga License works legally.
- Pages 13–16 of the extract (bibliography and any additional sections) not included in the extract provided.
