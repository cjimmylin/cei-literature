---
stem: "2022-Prabhakaran-A Human Rights-Based Approach to Responsible AI"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, cultural-linguistic, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Survey of 138 FAT* 2019-2020 papers found only 1 research paper engaging with human rights scholarship (p.7)"
  - "Among 36 AI principles sets, civil society and trans-national agencies rely most heavily on human rights framework (p.6)"
  - "UDHR consists of 30 articles; drafted with input from China, Chile, Soviet Union, Lebanon, India (p.3)"
---
## 1. Gist
This position paper by Prabhakaran, Mitchell, Gebru, and Gabriel argues that the Universal Declaration of Human Rights (UDHR) should serve as the grounding normative framework for responsible AI development and values alignment. The paper addresses a fundamental gap: FATE (Fairness, Accountability, Transparency, Ethics) research in AI lacks an explicit normative foundation, instead assuming implicit Western consensus on values that are then imposed globally through AI systems. The authors propose that human rights doctrine — understood in three ways: as moral claims, as legal instruments, and as a cultural practice/social movement — can perform three key functions: (1) provide cross-cultural value alignment, (2) clarify responsibilities across actors (states, companies, individuals), and (3) serve as a lingua franca for civil society participation. For values-alignment benchmarking, this paper is critical as a normative foundation paper that articulates why any benchmark must go beyond Western-centric assumptions, what values framework has the broadest cross-cultural legitimacy, and how to center harm-to-humans rather than model properties.

## 2. Benchmark/eval design features
This is a theoretical/position paper; no benchmark or dataset is presented. Core claims and arguments:

**Problem diagnosis**: FATE research is predominantly Western (institutions, data, values), yet AI systems are deployed globally, creating the risk of problematic value imposition. FAT* community rarely invokes human rights: survey of 138 FAT* 2019-2020 papers found only 1 research paper engaging with human rights scholarship.

**Three functions of human rights for AI**:
1. **Cross-cultural value alignment** (Section 2.1): UDHR has cross-cultural validity through its drafting history, adoption by nations across diverse political/cultural systems, and use by civil society globally. It provides "overlapping consensus" across cultural systems (African, Islamic, Western, Confucian traditions). It is proposed as a necessary-but-not-sufficient normative baseline.
2. **Allocation of responsibilities** (Section 2.2): Human rights frameworks clarify duties of states, companies (via UN Guiding Principles on Business and Human Rights 2011), and individuals — structuring accountability in the AI ecosystem.
3. **Civil society participation** (Section 2.3): Human rights concepts empower people as "rights-holders" rather than stakeholders or consumers, enabling more meaningful participation in AI governance.

**Illustrations** of three specific rights:
- Freedom from discrimination (UDHR Article 2) — maps to algorithmic bias; argues the FATE community's US-centric discrimination framing misses religion and language as protected characteristics
- Right to health (ICESCR Art. 12.1) — AI as potentially rights-enabling (diagnostic tools at scale) and rights-threatening (racial bias in healthcare algorithms)
- Right to share in scientific advancement (UDHR Art. 27) — argues for inclusive AI research and global distribution of AI benefits

**Appendix worked example**: Online content moderation analyzed through a rights-holders framework, distinguishing creators, addressees, audiences, referents, and moderators as separate rights-holders with potentially competing rights.

## 3. Task format & example item
n/a — theoretical paper with no items or tasks.

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
n/a — no dataset. The paper conducts a literature survey of FAT* 2019-2020 (138 papers) and a survey of 36 AI principles documents, used as evidence for the gap in human rights engagement.

## 6. Validity evidence
Empirical evidence is limited to the literature survey findings. The paper's normative claims rest on philosophical arguments (citing Rawls, Donnelly, Gabriel, Shue) and historical evidence (UDHR drafting, cross-cultural adoption, civil society use). The authors acknowledge four objections to the human rights approach: (1) inadequate coverage of collective goods, (2) cultural relativism objection, (3) neo-imperialism/Western parochialism concern, (4) anthropocentrism. Each is addressed with philosophical counter-arguments.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- FAT* 2019-2020 survey: 138 papers; only 1 research paper engaged with human rights scholarship (p.7)
- 36 AI principles sets surveyed by Berkman Klein Center: civil society and trans-national agencies rely most on human rights (p.6)
- 5 civil society-drafted AI principles documents: 3 explicitly adopt human rights framework (Toronto Declaration, Universal Guidelines for AI, Human Rights in the Age of AI by Access Now) (p.6-7)
- UDHR: 30 articles; drafted with input from China, Chile, Soviet Union, Lebanon, India (p.3)
- UN Guiding Principles on Business and Human Rights (UNGP): 2011 (p.7)
- ML-enabled diabetic retinopathy detection at scale in India — cited as rights-enabling AI example (p.9)

## 10. Pitfalls & limitations
- **Provenance of UDHR contested**: Authors acknowledge the UDHR has been criticized as a Western document, but argue it has since achieved genuine cross-cultural adoption. This is a live debate.
- **No implementation path**: The paper argues for using UDHR as a framework but does not specify how to operationalize this in practice (e.g., how to translate Article 2 into a fairness metric, or how to adjudicate when rights conflict).
- **Cultural relativism unresolved**: While the paper rebuts strong cultural relativism, the "relative universality" argument still leaves open which specific interpretations of rights apply in context.
- **Rights conflicts unaddressed**: The content moderation worked example raises the conflict between creators' free expression rights and audiences' freedom from discrimination, but provides no resolution mechanism.
- **Anthropocentric by design**: Authors acknowledge the framework says nothing about AI systems' potential moral status or non-human stakeholders.
- **Limited empirical grounding**: The paper's core contribution is normative; no empirical evaluation of whether human-rights-based interventions actually improve AI fairness outcomes.

## 11. Novel ideas worth stealing
1. **Rights-holders vs. stakeholders distinction**: In AI system design, distinguishing those whose rights are at risk (rights-holders) from those who simply have a stake (stakeholders) — a more principled basis for deciding whose values must be consulted in benchmark design.
2. **Human rights as cross-cultural overlapping consensus**: Rather than claiming universal agreement on all values, identifying the minimal set of rights that have "relative universality" across cultural traditions — directly applicable to designing a cross-cultural values-alignment benchmark scope.
3. **Orienting toward harms-to-humans, not model properties**: The human rights framework explicitly redirects attention from "is the model biased?" to "who is harmed, by what, and how?" — a more actionable framing for benchmark evaluation criteria.
4. **Rights-risk mapping for benchmark design**: The Appendix worked example of content moderation systematically maps rights-holders, their specific rights at risk, and trade-offs between competing rights — a reusable template for designing values-alignment benchmark scenarios.
5. **UDHR as a normative checklist**: Using the 30 UDHR articles as a structured checklist of value dimensions that any alignment benchmark should either cover or explicitly exclude with justification — provides breadth without imposing a single ethical theory.
6. **Protected characteristics expansion**: Noting that FATE research is biased toward US-centric protected characteristics (race, gender) while UDHR also protects religion, language, national origin, political opinion — an actionable expansion target for cultural-linguistic benchmarks.
7. **Shared vocabulary for researcher-civil society collaboration**: Human rights provides a lingua franca that AI researchers and NGOs/advocacy groups share, enabling participatory benchmark design with affected communities.

## 12. Notable quotes
- "Rather, an implicit consensus is often assumed to hold for the values we impart into our models – something that is at odds with the pluralistic world we live in." (p.1)
- "Orienting the research in this space away from the machines and the risks of their biases, and towards humans and the risks to their rights, essentially helping to center the conversation around who is harmed, what harms they face, and how those harms may be mitigated." (p.1)
- "As Birhane and Cummins note in [8], 'it is possible that what is considered ethical currently and within certain domains for certain societies will not be received similarly at a different time, in another domain, or for a different society.'" (p.4)
- "For AI researchers to build effective partnerships with civil society, bridging work needs to be done... failure to engage with human rights scholarship more widely, risks leading to a situation in which FATE researchers end up 'speaking a different language' from those their products affect." (p.7)

## 13. UNKNOWN / not in extract
- Full text of the 36 AI principles documents analyzed and their specific human rights coverage breakdown
- Details of the Appendix worked example scenarios 1-4 for content moderation rights mapping (Appendix starts at p.14 but extract ends before the full table)
- Whether the authors conducted any empirical evaluation of the proposed framework's practical utility
- Full list of UDHR articles analyzed in Section 7.1 (Probing with UDHR) of related Delphi work referenced in the introduction
- Responses from human rights practitioners or civil society organizations to this proposal
