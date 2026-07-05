---
stem: "2024-Hayes-Virtue and Narrative in AI Practices"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, ai-lab-practices, pluralism-aggregation, cultural-linguistic]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist

This theoretical paper by Hayes, Fitzpatrick, and Ferrandez (published in AI and Ethics, 2025, doi 10.1007/s43681-024-00472-z) proposes Virtuous Practice Design (VPD) as a comprehensive alternative ethical framework for AI ethics. Drawing on Paul Ricoeur's "little ethics" and narrative philosophy, Alasdair MacIntyre's virtue ethics, and the technology-ethics synthesis of Wessel Reijers and Mark Coeckelbergh, the authors argue that dominant approaches — deontological principles, utilitarianism, value sensitive design (VSD), and AI ethics guidelines — all share fundamental flaws: they are ahistorical, context-divorced, unable to challenge structural inequalities, and unenforceable. VPD, in contrast, grounds ethical AI practice in a tripartite framework (aim for the good life, with and for others, in just institutions), requiring deep narrative investigation of technical practices, cultivation of virtues in practitioners, and political engagement with institutional justice. The paper is relevant to values-alignment benchmarking because it provides a normative foundation for thinking about what "ethical" AI behavior should mean — not a checklist of principles, but a framework grounded in character, context, and embedded practice.

## 2. Benchmark/eval design features

This is a theoretical/survey paper; it does not present any benchmark or empirical evaluation. Core claims and arguments:

1. **Inadequacy of dominant frameworks**: Deontology (Kant) and utilitarianism fail in technology ethics because technological futures are unpredictable, algorithmic scale breaks calculi, and rules conflict without clear resolution procedures (p.3). VSD lacks a normative anchor and focuses narrowly on artefact design rather than socio-technical systems (p.4). AI principles (e.g., EU Ethics Guidelines for Trustworthy AI, OECD Principles) are plagued by four structural weaknesses identified by Mittelstadt: no unitary goal, no professional history, no translation methods, no accountability mechanisms (p.4-5). Munn's more radical critique holds that AI ethics is essentially "ethics washing" serving corporate interests (p.5).

2. **VPD as synthesis**: VPD integrates Ricoeur's "little ethics" with MacIntyre's virtue ethics applied to technology by Reijers and Coeckelbergh. The framework is tripartite and iterative: Phase 1 (Description ↔ Interpretation: understand the full practice network), Phase 2 (Interpretation ↔ Evaluation: identify puzzles about life plans, standards of excellence, narrative unity), Phase 3 (Evaluation ↔ Prescription: evaluate practices against the ethical intention and prescribe virtuous practice design) (p.7).

3. **Ethical intention structure**: Ricoeur's triadic ethical intention — aiming at the good life (eudaimonia), with and for others (solicitude), in just institutions (justice/equality) — provides the normative core. Moral norms (deontological principles) act as overridable constraints, not foundations (p.7-10).

4. **Five challenges addressed**: Inadequate frameworks (VPD's VE flexibility responds), ahistorical principles (VPD grounds principles in particular practice narratives), failure to challenge structural inequality (VPD's critical solicitude, justice, participatory design, decolonial design), lack of enforcement (VPD cultivates virtue as internal motivation plus lobbying for external regulation), and resourcing ethics (VPD acknowledges costs but argues for taxation, redistribution, third-party ethics firms) (p.8-17).

5. **Foucauldian dispositif**: A final section acknowledges that pre-existing power structures (Foucault's dispositif) constrain virtue cultivation and may limit VPD's efficacy, requiring working within and against hegemonic narratives (p.18-19).

## 3. Task format & example item

n/a — this is a purely theoretical paper with no benchmark items or example evaluation tasks.

## 4. Scoring / grading methodology

n/a — no empirical scoring; the paper is normative/philosophical.

## 5. Dataset construction & provenance

n/a — no dataset. The paper is a conceptual analysis drawing on philosophical literature (Ricoeur, MacIntyre, Reijers & Coeckelbergh, Vallor, Mittelstadt, Munn, D'Ignazio & Klein, Crawford, Foucault) and illustrative examples (crime hotspot algorithms, medical AI diagnosis tools, welfare fraud detection, social media recommender systems).

## 6. Validity evidence

n/a as a benchmark. The paper's arguments are grounded in philosophical literature and evaluated through conceptual coherence and response to existing critiques. No empirical human baselines, inter-rater reliability, or factor analyses are present. The authors acknowledge that VPD "has not yet been aimed at a multiplicity of issues in a systematic way" and claim this paper represents "the first effort to apply VPD in an in-depth manner to the problem of the ethical design of artificial intelligence" (p.2).

## 7. Saturation / discrimination

n/a — no quantitative measurements, ceiling effects, or item discrimination analysis.

## 8. Multiturn / agentic aspects

n/a — this is a philosophy paper; no interaction protocol or agent environment is described.

## 9. Key numbers

- Paper published in AI and Ethics (2025) 5:1217–1239 (p.1)
- Paper is 23 pages in PDF form (extract metadata)
- Mittelstadt identifies 4 structural challenges to principles-based AI ethics (p.4-5)
- VPD framework has 3 iterative phases drawn from Ricoeur's narrative philosophy (p.7)
- Ricoeur's ethical intention has 3 elements: good life / with and for others / just institutions (p.7)
- 5 challenge categories addressed: inadequate frameworks, ahistorical principles, structural inequality, enforcement gaps, resourcing (p.8-9)
- Vallor proposes 12 technomoral virtues including honesty, self-control, humility, justice, courage, empathy, care, civility, flexibility, perspective, magnanimity, technomoral wisdom (p.6)
- EU AI Act approved by EU Parliament using tiered risk-based approach (p.17)

## 10. Pitfalls & limitations

**Author-admitted limitations:**
- VPD narrative investigation is "truly significant and in-depth, multi-step and iterative" and "would likely be resource intensive and a challenge to execute for small and medium sized businesses" (p.8)
- VPD emerged "in the Global North primarily through a series of Western thinkers" and may not translate across cultural contexts or may conflict with decoloniality (p.8)
- VPD has not been tested empirically in real AI use cases; this paper is the "first effort to apply VPD in an in-depth manner" (p.2)
- The dispositif (Foucauldian power structures) may be "so entrenched" that VPD's tools are "doomed to failure by operating within existing dispositifs" (p.19)
- VPD makes "no practical considerations towards costs" that it may incur through education, training, and regulatory compliance (p.17)

**Additional observed limitations:**
- The framework is highly abstract and offers no operationalization pathways for empirical research or benchmark construction
- The paper conflates "ethical AI" with "ethical practitioners" — the question of how to evaluate AI system outputs against these norms is not addressed
- Virtue cultivation as a mechanism assumes motivated practitioners; incentive misalignment in for-profit AI development is acknowledged but not fully resolved
- The decolonial design recommendation remains programmatic without concrete guidance on implementation
- No engagement with how LLM systems themselves might express or fail to express virtues in their outputs

## 11. Novel ideas worth stealing

For values-alignment benchmark designers, this paper offers several reusable conceptual moves:

1. **Practice-embedded evaluation**: Rather than testing AI responses to abstract principles ("Is this action fair?"), design scenarios that embed the AI in a specific practice context (medical diagnosis, policing, welfare allocation) and evaluate whether responses reflect appropriate virtues for that context. The VPD framework's narrative investigation phases could structure scenario generation.

2. **Triadic ethical intention as rubric**: Ricoeur's three-part structure (good life / with and for others / just institutions) provides a graded evaluation scheme: does the AI response (a) serve the agent's goals, (b) show solicitude for others, and (c) engage with institutional justice? This is more tractable than "fairness" as an undifferentiated term.

3. **Virtues as behavioral anchors**: Vallor's list of 12 technomoral virtues (p.6) — especially care, justice, honesty, humility, perspective, flexibility — can serve as named behavioral dimensions for rubric-based scoring of LLM outputs. Each virtue is defined concretely enough to distinguish responses that exemplify vs. violate it.

4. **Narrative mediation scenarios**: VPD's attention to how technology reconfigures practice narratives (prefiguration → configuration → refiguration) suggests agentic evaluation scenarios where the AI's role across multiple turns changes the story — and benchmarks should assess whether the AI's contributions are virtue-supporting or virtue-impeding for affected parties.

5. **Critical solicitude as evaluation criterion**: The concept of "critical solicitude" — attending to vulnerable others at risk from norms — maps directly onto harm-avoidance evaluation. Scenarios could specifically probe whether AI responses identify and protect vulnerable groups whose interests might be overridden by majority preferences.

6. **Stakeholder narrative elicitation**: The paper endorses participatory design methods where affected communities narrate their experiences. This suggests a benchmark construction methodology: collect narratives from affected communities (e.g., welfare recipients, patients, marginalized groups) as scenario inputs, then evaluate whether AI responses demonstrate awareness of those narratives.

7. **The dispositif as adversarial pressure**: The Foucauldian dispositif concept translates to adversarial testing — scenarios where institutional pressure (economic, legal, market) pushes toward unethical responses. Does the AI maintain virtuous responses under dispositif-style pressure, or does it accommodate existing power structures?

## 12. Notable quotes

1. "The ethical intention was aiming at the good life, with and for others, and in just institutions." (p.6, describing Ricoeur's core formulation)

2. "Moral expertise is reflected in, but not drawn from, fixed principles […] principles can emerge from observations of patterns of right action, but right action does not (necessarily) emerge from principles." (p.9, citing Vallor)

3. "VPD makes no practical considerations towards costs, which it may even incur through education and training processes, and the regulatory compliance that it effectively champions — this is an undeniable reality." (p.17)

4. "Within the dispositif all forms of ethics are aspirational and arguably the dispositif must bend for ethics to truly blossom — yet even within the logic of the dispositif as it is there remains a space where ethics fit, the marketable logic of acceptability." (p.19)

## 13. UNKNOWN / not in extract

- No empirical data, case studies, or pilot implementations of VPD are described; the paper is entirely theoretical
- The exact reference list for [75] (Reijers & Coeckelbergh's primary VPD paper) is not fully visible in this extract to confirm the specific publication title
- Whether the authors have conducted follow-up empirical work applying VPD to specific AI development organizations is unknown
- The specific content of Vallor's 12 technomoral virtues list is only partially given in the extract (p.6 lists 12 virtues but some text was cut)
- The paper's reception in the AI ethics field (citations, critiques, replies) is not assessable from the extract alone
- No information is available about the anonymous reviewers' substantive feedback mentioned in acknowledgements
