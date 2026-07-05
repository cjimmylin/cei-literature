---
stem: "2020-Awad-Crowdsourcing moral machines"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, cultural-linguistic, pluralism-aggregation, design-space]
task_format: "forced-choice"
scoring_type: "behavioral"
dataset_size: 40000000
dataset_construction: "crowdsourced"
languages: ["en", "multilingual"]
models_tested: []
headline_numbers:
  - "40 million decisions collected from millions of visitors across 233 countries and territories (p.8)"
  - "Three main country clusters found: Western, Eastern, Southern (p.8)"
  - "Top three preferences: spare humans over pets, spare more over fewer, spare younger over older (p.8)"
---
## 1. Gist
This Communications of the ACM article presents and defends the Moral Machine (MM) platform — a crowdsourcing tool for collecting public preferences on how autonomous vehicles (AVs) should handle trolley-problem-style ethical dilemmas. Deployed in June 2016, MM collected 40 million decisions from millions of visitors across 233 countries, making it the largest dataset on AI ethics ever assembled at the time. The article reviews major objections to the Trolley Problem methodology (scenarios are naïve, simple, improbable, disconnected from real action, distracting, or scary) and responds to each. It also proposes a "Society in the Loop" (SITL) regulatory framework where behavioral data from platforms like MM informs an iterative cycle of machine design, regulatory review, and public engagement. For values-alignment benchmarking, MM is a canonical example of large-scale crowdsourced preference elicitation and illustrates both the power and the fundamental limits of asking the public what machines should do.

## 2. Benchmark/eval design features
Not a model benchmark but a human-preference collection platform. Key design elements:
- **Judge mode**: users see 13 forced-choice dilemma pairs per session. Each pair presents two visual outcomes of an AV decision.
- **Scenario dimensions**: 6 core dimensions (age, gender, fitness, social status, number of characters, species); 3 additional dimensions (interventionism, relation to AV, legality) randomly combined with each core scenario.
- **Characters**: 20 different character types combinable in each scenario.
- **Counterbalancing**: order of 13 scenarios counterbalanced over sessions; random assignment of users to conditions.
- **Constraint**: scenarios restricted to exactly two outcomes (no "safe" middle option) to force difficult ethical choices.
- **Classic mode**: traditional Switch, Loop, Footbridge trolley dilemmas also available (analyzed in companion paper Awad et al. PNAS 2020).
- The platform's goal is to capture normative stated preferences (what people believe the car should do), not behavioral responses.

## 3. Task format & example item
Forced-choice visual dilemma presented on a webpage. Example (p.4, Figure 2): "A pictorial representation of a dilemma faced by an AV. If the AV continues ahead it will hit and kill a group of pedestrians, including three adults and a dog, crossing on a red light. If the AV swerves, it will hit a barrier and result in the death of its sole passenger, a female athlete."

Question: "What should the self-driving car do?"

## 4. Scoring / grading methodology
- Preference tallied by counting forced-choice selections across scenario variants.
- Country-level aggregate preferences computed.
- Published findings (Awad et al., Nature 2018) analyzed via conjoint analysis and regression.
- No formal inter-rater reliability; data aggregated by majority preference and regression modeling.

## 5. Dataset construction & provenance
- Platform launched June 2016 at moralmachine.mit.edu.
- Data collection ongoing; 40M decisions by millions of visitors from 233 countries and territories (as of publication, p.8).
- Scenarios generated via randomization under constraints.
- Optional demographic survey completed by a subset of users (~20,000 survey takers in the companion PNAS paper), skewed toward young, male, college-educated, left-leaning, secular respondents.
- No licensing restrictions mentioned; data used for academic analysis.

## 6. Validity evidence
- External validation: MM results generalize to different presentation formats (Sütfeld et al. 2019, cited p.9).
- No formal psychometric analysis of item quality.
- Self-selection bias acknowledged: viral online experiment attracts non-representative population.
- Cross-national comparison limited by differential internet access and literacy.
- Exposure study found no significant adverse effect of MM participation on AV trust attitudes (p.7).

## 7. Saturation / discrimination
Not applicable to classic benchmark sense. The MM design deliberately prevents "easy" exits — scenarios are forced-choice with no safe option — ensuring discrimination among preference types. Cross-national variability is the key finding: while qualitative orderings are consistent, quantitative magnitudes differ substantially across country clusters, showing the instrument discriminates culturally meaningful variation.

## 8. Multiturn / agentic aspects
n/a for model benchmarking. The platform itself provides a short 13-scenario session per user, but this is fixed and not interactive in a meaningful way.

## 9. Key numbers
- Total decisions collected: 40 million (p.8)
- Countries/territories represented: 233 (p.8)
- Scenarios per session: 13 (p.8)
- Core scenario dimensions: 6 (age, gender, fitness, social status, number, species) (p.8)
- Additional dimensions: 3 (interventionism, relation to AV, legality) (p.8)
- Character types: 20 (p.8)
- Three top cross-cultural preferences: spare humans > pets; spare more > fewer; spare younger > older (p.8)
- Three country clusters: Western, Eastern, Southern (p.8)
- Germany: first country to draft AV ethics guidelines (2016) (p.8)
- Rule of law correlates positively with preference to spare the lawful (p.8)

## 10. Pitfalls & limitations
- Strong self-selection bias; sample skews young, male, college-educated (documented in PNAS companion).
- Scenarios limited to exactly two outcomes, excluding realistic AV decision spaces.
- AV-Trolley scenarios are extremely improbable in practice — their relevance to real AV programming is contested.
- Stated preferences diverge from actual behavior; no ground-truth behavioral data available.
- Cultural clusters may reflect internet access patterns rather than genuine moral diversity.
- Findings already influenced by media coverage, which could prime responses.
- No mechanism to ensure participants understand scenario premises (brakes failing, pedestrians frozen, etc.).
- The SITL framework is aspirational; no regulatory body has actually adopted MM data.

## 11. Novel ideas worth stealing
- **Randomized controlled scenario design with constraints**: randomly assigning users to dilemma variants while holding all but one dimension constant (a within-platform conjoint design) cleanly isolates the effect of each moral factor; reusable for LLM moral judgment benchmarks.
- **SITL (Society in the Loop) framework**: presenting a layered feedback architecture where public preferences feed into regulatory proposals, which in turn inform machine programming — a template for legitimizing values-alignment benchmarks as policy instruments.
- **Counterbalanced multi-scenario sessions**: presenting 13 randomized scenarios per session reduces acquiescence bias and provides per-user consistency data; applicable to LLM evaluation across multiple ethical framings.
- **Aesthetic constraint for forced-trade-off elicitation**: removing the "safe" third option (e.g., slow down and stop) forces participants to reveal genuine preferences; analogous to designing benchmark items where refusal is not available as an easy escape.
- **Cross-cultural cluster analysis**: grouping respondents by cultural/geographic variables and comparing preference magnitudes reveals whether a benchmark discriminates cross-cultural variation — a validity check for global values benchmarks.
- **Edge-case focus as design choice**: deliberately targeting low-probability, high-impact scenarios because they reveal moral principles more cleanly than typical cases, despite arguments that they are "improbable."

## 12. Notable quotes
- "The goal of the crowdsourcing task here is not to capture the actual actions, but to capture what humans would believe (from the comfort of an armchair) to be the best course of action." (p.7)
- "We believe that social scientists and computational social scientists have a pivotal role to play as intermediaries between engineers and humanities scholars in order to help them articulate the ethical principles and priorities that society wishes to embed into intelligent machines." (p.5)
- "Data collected shows discrepancies between the preferences of the public, the experts, and citizens of different countries—calling for an interdisciplinary framework for the regulation of moral machines." (p.2)
- "Even though it may be too early to regulate about AV-Trolleys, it is the right time to start crowdsourcing citizen preferences." (p.4)

## 13. UNKNOWN / not in extract
- Full quantitative results from the Nature 2018 paper (Awad et al.) — only summarized here.
- Exact demographic breakdown of all 40M decision-makers (only a fraction completed the optional survey).
- Details of the "Moral Machine Experiment" (Nature 2018) conjoint analysis methodology.
- Whether MM data has been used in any actual AV regulation outside Germany.
- Whether the dataset has been made publicly available for download.
