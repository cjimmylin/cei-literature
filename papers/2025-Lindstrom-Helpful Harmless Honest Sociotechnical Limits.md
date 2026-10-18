---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LINDSTROM2025
type: journalArticle
short_title: "Helpful Harmless Honest Limits"
year: 2025
first_author: "[[Adam Dahlgren Lindström]]"
last_author: "[[Dobbe, Roel]]"
authors: "Lindström, Adam Dahlgren; Methnani, Leila; Krause, Lea; Ericson, Petter; Martínez de Rituerto de Troya, Íñigo; Coelho Mollo, Dimitri; Dobbe, Roel"
doi: 10.1007/s10676-025-09837-2
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12137480/"
publication: "Ethics and Information Technology"
CONF-CC: "Ethics and Information Technology"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: Christianity
rv_islam: 0
rv_christianity: 50
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: Christianity
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "RLHF, RLAIF, HHH-Principle, AI-Safety, Sociotechnical, Values-Alignment"
key_contribution: "Critical analysis showing tensions between HHH goals; RLHF insufficient alone for AI safety"
significance: "Argues effective AI safety requires comprehensive sociotechnical approaches beyond technical interventions"
tags: 
abstract: "This paper critically evaluates the attempts to align Artificial Intelligence (AI) systems, especially Large Language Models (LLMs), with human values and intentions through Reinforcement Learning from Feedback methods, involving either human feedback (RLHF) or AI feedback (RLAIF). Specifically, we show the shortcomings of the broadly pursued alignment goals of honesty, harmlessness, and helpfulness."
DATE_ADDED: 20260208
research_topic: "AI Safety & Alignment"
LLM_assessed: NA
DATA_URL: NA
pdf_extract: "PDF Extracts/2025/2025-Lindstrom-Helpful Harmless Honest Sociotechnical Limits.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Lindstrom-Helpful Harmless Honest Sociotechnical Limits.pdf]]"
CONFERENCE: Journal
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# Helpful, harmless, honest? Sociotechnical limits of AI alignment and safety through Reinforcement Learning from Human Feedback

## Authors

[[Lindström, Adam Dahlgren]], [[Methnani, Leila]], [[Krause, Lea]], [[Ericson, Petter]], [[Martínez de Rituerto de Troya, Íñigo]], [[Coelho Mollo, Dimitri]], [[Roel Dobbe|Dobbe, Roel]]

## Metadata

**Authors:** Lindström, Adam Dahlgren; Methnani, Leila; Krause, Lea; Ericson, Petter; Martínez de Rituerto de Troya, Íñigo; Coelho Mollo, Dimitri; Dobbe, Roel

**Year:** 2025

**Publication:** Ethics and Information Technology

**Type:** journalArticle

**DOI:** [10.1007/s10676-025-09837-2](https://doi.org/10.1007/s10676-025-09837-2)

## Links

- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12137480/
- **DOI:** https://doi.org/10.1007/s10676-025-09837-2

## Abstract

This paper provides critical analysis of RLHF and RLAIF techniques used to align Large Language Models with human values through the HHH (Helpful, Harmless, Honest) principle. The authors examine theoretical and practical limitations, revealing tensions between helpfulness, harmlessness, and honesty goals. Key issues include how increased user-friendliness may mislead users about AI capabilities, sycophantic model behavior prioritizing agreement over accuracy, and value imposition favoring hegemonic cultural norms. The work concludes that effective AI safety requires comprehensive sociotechnical approaches spanning institutional, process, and technological design rather than technical interventions alone.

## Detailed Summary

This paper provides a comprehensive critical evaluation of Reinforcement Learning from Human Feedback (RLHF) and RLAIF techniques as methods for AI alignment and safety, arguing that these approaches are fundamentally insufficient when taken as standalone solutions. The authors, a multidisciplinary team from Umea University, Vrije Universiteit Amsterdam, and Delft University of Technology, examine both theoretical underpinnings and practical implementations of the HHH (Helpful, Harmless, Honest) principle that has become widely adopted in LLM alignment practices.

The paper reveals significant tensions inherent in the HHH goals. For "harmlessness," the actual implementation often translates to "least harmful" rather than truly harm-free, settling for comparing harmful options rather than preventing harm. The evaluation criteria conflate harmlessness with superficial virtues (politeness, friendliness) without justification. For "honesty," the paper argues that LLMs cannot express genuine uncertainty since they lack introspective capabilities - any expressed confidence is merely a predicted textual pattern, not actual model certainty. Furthermore, RLHF's reduced human input means fewer opportunities to catch factual errors. For "helpfulness," increased user-friendliness paradoxically may mislead users about AI capabilities, while sycophantic behavior (prioritizing agreement over accuracy) emerges from preference optimization.

A key theoretical contribution is connecting RLHF limitations to Nancy Leveson's "curse of flexibility" concept from system safety: the greater power and flexibility of computational systems means "the limits of what is possible to accomplish are different than the limits of what can be accomplished successfully and safely." The paper argues that effective AI safety requires comprehensive sociotechnical approaches spanning institutional, process, and technological design - not merely technical fine-tuning of model outputs.

## Paper Outline

1. Introduction - RLHF's role in AI safety claims
2. Background
   - LLM training and fine-tuning
   - Reinforcement Learning from Human Feedback
   - Reinforcement Learning from AI Feedback (RLAIF)
   - Technical criticism (Casper et al.'s taxonomy)
   - The curse of flexibility (Leveson)
3. Limitations of RLHF
   - 3.1 Harmlessness - least harmful vs. truly harmless
   - 3.2 Honesty - calibration and truthfulness challenges
   - 3.3 Helpfulness - user-friendliness and sycophancy
4. Internal Tensions and Ethical Issues in RLHF
   - Trade-offs between helpfulness and deception
   - Flexibility vs. interpretability
   - Value imposition and cultural hegemony
5. Rebooting AI Safety and Ethics
   - AI safety as sociotechnical discipline
   - Comprehensive design across institutions
   - Beyond technical interventions

## Methods Summary

The paper employs multidisciplinary critical analysis combining technical understanding of RLHF/RLAIF with philosophical ethics, system safety theory, and sociotechnical systems analysis. The authors examine primary sources from AI companies (Anthropic's Constitutional AI, OpenAI's InstructGPT) alongside academic critiques. They apply Casper et al.'s taxonomy of RLHF challenges (collecting human feedback, training reward models, training policy) and Leveson's system safety framework to evaluate alignment approaches. The analysis integrates empirical findings about model behavior (jailbreaking, sycophancy, hallucination) with normative assessment of what safety and alignment should require.

## Results Summary

The analysis identifies fundamental limitations: (1) HHH principles are deliberately kept vague ("we simply let our crowdworkers interpret these concepts as they see fit" - Bai et al.), undermining accountability; (2) Harmlessness evaluation ignores systemic harms emerging from sociotechnical embedding; (3) Honesty cannot be achieved by models lacking genuine introspection; (4) Helpfulness optimization produces sycophantic behavior prioritizing agreement over accuracy; (5) RLAIF risks propagating Western-centric values while failing in non-Western contexts; (6) Technical jailbreaking demonstrates fragility of RLHF safety constraints; (7) The curse of flexibility means model complexity prevents proper specification and validation of safety requirements.

## Conclusions

The authors conclude that RLHF, while improving LLM performance on some dimensions, is "deeply insufficient as a means for achieving AI safety and ethical AI, and, if taken as a silver bullet without integration in a broader sociotechnical approach, may be counterproductive for achieving those goals." They call for establishing AI safety as a sociotechnical discipline that is "open to the normative and political dimensions of artificial intelligence." Effective AI safety requires comprehensive design across institutions, processes, and technological systems - not merely technical fine-tuning. The paper advocates for moving beyond the narrow framing of alignment as a technical problem solvable through feedback mechanisms toward recognition of AI safety as fundamentally involving questions of power, accountability, and social values.

## Artifact Contributions

None mentioned

## Data Description

This paper does not introduce or utilize a specific dataset or benchmark for LLM assessment. It is a critical sociotechnical analysis of Reinforcement Learning from Human Feedback (RLHF) and the HHH (helpful, harmless, honest) alignment principle, examining their theoretical underpinnings and practical limitations from multidisciplinary philosophical and system safety perspectives.


## Notes


## Citation Info

