# best-practices — sub-dossier part 2/4

Scope: 53 cards (48 papers + 5 AI-lab cards). Mostly content-moderation/hate-speech/bias datasets, plus moral-judgment benchmarks, fairness harnesses, and lab safety cards. Page refs are the card's (±1-2 pp).

## A. Synthesized claims

1. **Held-out F1/accuracy on a curated set systematically overstates real-world competence; representative evaluation is the single biggest validity lever.** NaijaHate is the sharpest case: AP was 73.75% on holdout and 81.88% top-scored but only 20.92% on a random sample of 2.2B tweets — a >2x overestimate; the best model fell 83.4%→33.7% [2024-Tonneau-NaijaHate]. HateCheckHIn makes the point functionally: a model with respectable aggregate accuracy scored 0.0% on functionalities held-out F1 never surfaced [2022-Das-HateCheckHIn]. Eagle shows LLM-generated items correlate only rho=0.08-0.33 with real ChatGPT harms [2024-Kaneko-Eagle]; ToxSyn documents "catastrophic, mutual generalization failure," F1 0.94 in-domain collapsing to 0.00 recall out-of-domain [2025-Brito-ToxSyn].

2. **Binary correct/incorrect labels are insufficient; the field is converging on multi-facet, same-item scoring.** HateXplain scores the same posts on correctness, group-fairness AND explanation quality and shows the axes dissociate — best-accuracy ≠ best-faithfulness [2020-Mathew-HateXplain]. Anthropic replaced binary harmful/benign with a four-category scheme (helpful / policy-violation / appropriate-refusal / unnecessary-refusal) because binary labels "fail to capture desirable harmless behavior" [Anthropic-Claude_3.7_Sonnet_System_Card]. FAI geometric-means seven flourishing dimensions so one cannot mask another [2025-Hilliard-Measuring AI Alignment with Human Flourishing]; SafetyAnalyst decomposes into a stakeholder×action×effect tree with 28 interpretable weights [2025-Li-SafetyAnalyst].

3. **Minimal-pair / contrastive item design is the recurring gold-standard construction technique** — swap only the sensitive attribute and measure the behavioral delta. WINOGENDER pronoun-swaps holding lexical content fixed [2018-Zhao-Gender Bias in Coreference Resolution]; HateCheckHIn "I hate Hindus" vs "I hate apples" [2022-Das-HateCheckHIn]; M³oralBench's matched neutral twin per violation [2024-Yan-M$^3$oralBench]; SHADES stereotype/contrast pairs [2025-Al-Towards a Multilingual Assessment of Stereotypes]; ToxSyn's non-toxic counterexamples about the same minority group [2025-Brito-ToxSyn]. Contrast items expose shortcut learning that aggregate scores hide.

4. **Inter-annotator reliability must be measured and reported — it is the honest floor on label quality.** Reported values span "almost perfect" to "moderate": HateCheckHIn κ=0.95 [2022-Das-HateCheckHIn], SimpleSafetyTests κ=0.83 [2023-Vidgen-SimpleSafetyTests], HateBench α=0.846 [2025-Shen-HateBench], VisAlign κ=0.80/0.91 [2023-Lee-VisAlign], NaijaHate α=0.7 [2024-Tonneau-NaijaHate]; but HateXplain α=0.46 [2020-Mathew-HateXplain], MIC α=0.10-0.46 [2022-Ziems-The Moral Integrity Corpus], TeSent 3-class α=0.47→0.89 binary [2025-Kumar-TeSent], DKHate Jaccard ~40% [2020-Sigurbergsson-DKHate]. PerGOLD reports **no** IAA at all — a flagged validity gap [2025-Jafarinejad-PerGOLD].

5. **Who annotates defines the construct, so annotator provenance must be disclosed.** DKHate ships a Bender-Friedman data statement disclosing a single non-native-Danish annotator [2020-Sigurbergsson-DKHate]; MIC records political leaning + Moral Foundations Questionnaire scores [2022-Ziems-The Moral Integrity Corpus]; NaijaHate recruits from the four largest Nigerian ethnic groups [2024-Tonneau-NaijaHate]; IndicCONAN concedes all annotators were middle-aged males despite gender being a hate category [2024-Sahoo-IndicCONAN].

6. **Human-derived "ground truth" is itself contested; the best benchmarks model disagreement as signal rather than averaging it away.** MIC collects multiple conflicting Rules-of-Thumb per item and records Global Consensus [2022-Ziems-The Moral Integrity Corpus]; STREAM captures Judgment+Degree+Confidence with demographic baselines [2023-Wang-STREAM]; GuardEval entropy-flags contested cases rather than discarding them [2025-Machlovi-GuardEval]; a survey of 105 cultural benchmarks finds 97.1% collapse to a single majority answer, with diversity-aware Jensen-Shannon scoring as the fix [2025-team-Incorporating Diverse Perspectives]. Rodemann argues empirical human preference is a biased sample needing prescriptive metric slots [2025-Rodemann-A Statistical Case].

7. **Anchor items to external ground truth for criterion validity.** WINOGENDER correlates system bias with US BLS employment statistics and the model's own training-data statistics (RULE r=0.87 to text stats) [2018-Zhao]; SynthBias and the Moral-Machine study anchor to BLS and to aggregated human AMCE vectors [2025-Wang-Is Your Model Fairly Certain; 2025-Zaim Bin Ahmad-Large-scale moral machine]; M³oralBench reuses peer-validated Moral Foundations Vignettes with human wrongness ratings [2024-Yan-M$^3$oralBench].

8. **Design for discrimination and against saturation deliberately.** Stratify across a difficulty axis (PTP's 4 toxicity bins) [2024-Jain-PolygloToxicityPrompts]; redefine difficulty by human-judged ambiguity so it stays hard as models improve (SynthBias re-ranks models WinoBias could not) [2025-Wang-Is Your Model Fairly Certain]; floor-tests still discriminate (Claude 0% vs Dolly 69% unsafe) [2023-Vidgen-SimpleSafetyTests]. Where utility is near-ceiling (10/12 detectors >98% AUC), headroom moved to fairness/robustness axes [2024-Lin-AI-Face].

9. **Automated (classifier / LLM-judge) scoring is scalable but must be validated and triangulated.** Perspective-vs-Llama-Guard r=0.78 shows "related but distinct" constructs [2024-Jain-PolygloToxicityPrompts]; SimpleSafetyTests benchmarks five filters against human labels [2023-Vidgen-SimpleSafetyTests]; Llama Guard makes the taxonomy a model input for few-shot adaptation [Meta AI-Llama_Guard]. But judges inherit biases — a same-ideology LLM judge hit 87% human agreement precisely because judge and annotators shared the value commitment [2026-Gao-Adversarial Alignment].

10. **Reward/proxy over-optimization is a first-order failure mode.** Optimizing beyond ~KL 250 nats drove human preference below random and ROUGE tracked RLHF quality poorly — a canonical Goodhart demonstration and reusable validity check (map the "overfit cliff" via best-of-N; reward models are length-biased) [OpenAI-learning-to-summarize-rlhf]. SafetyAnalyst's fitted 7.59% benefit weight is itself a diagnostic that the label set under-represents helpfulness [2025-Li-SafetyAnalyst].

11. **Agentic and multi-turn contexts surface failures single-turn evals miss.** Reward-hacking special-casing in Claude Code appeared only after multiple attempts and was invisible to user testing but caught by training-time classifiers [Anthropic-Claude_3.7_Sonnet_System_Card]; MORALSIM embeds ethics in repeated games (cooperation=moral), finding no model consistently moral (7.9%-76.3%) [2025-Backmann-When Ethics and Payoffs Diverge]; Operator separates direct-misuse from adversarial-environment evals with layered ablations (62%→23%) [OpenAI-operator-system-card]; Constitutional Classifiers++ shows context-blind scoring under-counts multi-turn harm [Anthropic-Constitutional_Classifiers_Plus_Plus].

12. **Cross-lingual transfer of alignment is uneven and carries hidden costs; English-only evaluation cannot predict multilingual behavior.** English DPO cut toxicity across 17 languages but least for low-resource ones [2024-Li-Preference Tuning]; debiasing transfer "comes paired with a decrease in language generation ability," and pretraining-data fraction predicts transfer (r −0.6 to −0.4) [2025-Neplenbroek-Cross-Lingual Transfer]; natively-authored beats translated (SHADES built by 43 native speakers) [2025-Al-Towards a Multilingual Assessment]; LLaVA auto-captions fail on culturally-specific content [2024-Vasilev-CRAFT].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2018-Zhao-Gender Bias in Coreference Resolution | Minimal-pair pronoun swaps + anchoring to BLS stats; PPV-not-NPV framing (shows bias present, can't prove absence) |
| 2020-Mathew-HateXplain | Same-item scoring on correctness+fairness+explanation dissociates; best-accuracy model ≠ best-faithfulness |
| 2020-Sigurbergsson-DKHate | Report low IAA (Jaccard ~40%) then document how the construct was narrowed; ship a data statement |
| 2022-Bang-Enabling Classifiers | Value-as-instruction input + value/counter-value test pairs let one model make culturally-relative judgments |
| 2022-Das-HateCheckHIn | Functional decomposition (34 functionalities) localizes failure; models scored 0.0% where held-out F1 saw nothing |
| 2022-Ziems-The Moral Integrity Corpus | Collect multiple conflicting Rules-of-Thumb + record Global Consensus + annotator ideology |
| 2023-Haq-Pashto Offensive Language | Two-stage triaged annotation (small panel for easy 91%, larger jury for contested 9%); base-rate-faithful imbalance |
| 2023-Lee-VisAlign | Three-tier ground truth (Must-Act/Must-Abstain/Uncertain); Cronbach's α to justify dataset size; soft human distributions |
| 2023-Vidgen-SimpleSafetyTests | Floor-test philosophy + benchmark five filters against human labels; negative-predictive-power caveat |
| 2024-Defrance-ABCFair | Make problem framing (notion/group/output type) selectable axes; dual biased+unbiased labels |
| 2024-Jain-PolygloToxicityPrompts | Stratified sampling across difficulty bins; natural long prompts > translated; two-judge triangulation |
| 2024-Kaneko-Eagle | Ecological validity: correlation with a real-interaction reference set as a meta-benchmark; cheap+expensive two-stage extraction |
| 2024-Lin-AI-Face | Fairness as first-class multi-level (group/intersectional/individual) construct; joint fairness-vs-utility reporting |
| 2024-Meadows-LocalValueBench | Escalating-coercion interrogation ladder; jurisdiction-anchored items; refusal-as-scored-behavior |
| 2024-Pfister-SuperGLEBer | Hierarchical per-task-type averaging; uniform training protocol; provenance gate against machine-translation |
| 2024-Sahoo-IndicCONAN | Response-type conditioning forces functional diversity; HITL machine-generate→human-correct loop |
| 2024-Tonneau-NaijaHate | Representative random-sample evaluation vs curated training; holdout AP 73.75% → random 20.92% |
| 2024-Yan-M³oralBench | Paired minimal-contrast items + intrinsic-tendency probe (role-play "what would you say"); reuse validated stimuli |
| 2025-Al-Towards a Multilingual Assessment (SHADES) | Native-speaker-first construction; geographic-validity annotation; dual base/instruct evaluation paths |
| 2025-Backmann-When Ethics and Payoffs Diverge | Moral context embedded in payoff games; baseline-vs-framing within-design; prompt-paraphrase robustness (1.8pp) |
| 2025-Brito-ToxSyn | Systematic non-toxic counterexamples; domain-gap stress test; Macro-Recall when true negatives unavailable |
| 2025-Hilliard-Measuring AI Alignment (FAI) | Geometric-mean aggregation prevents one dimension masking another; negative-weighted rubric floors |
| 2025-Jafarinejad-PerGOLD | Event-based collection raises positive rate to 34%; but reports NO inter-annotator agreement (anti-pattern) |
| 2025-Kumar-TeSent | Human-rationale supervision improves plausibility but NOT fairness — decouple those claims |
| 2025-Machlovi-GuardEval | Cross-domain generalization as core validity check; entropy-flag contested samples; PH vs RH split |
| 2025-Mining-Enhancing hate speech (Albanian) | Targeted provocative-post collection for near-balanced classes; report peak AND cross-validated F1±SD |
| 2025-Shen-HateBench | Generator-stratified scoring (Perspective 0.878 on GPT-3.5 → 0.621 on GPT-4); refusal as explicit third label |
| 2025-Wang-Is Your Model Fairly Certain (UCerF/SynthBias) | Joint correctness×confidence scoring; difficulty defined by human ambiguity to resist saturation |
| 2025-Zaim Bin Ahmad-Moral Machine on LLMs | Conjoint/AMCE reduces values to a low-dim preference vector; distance-to-human + directional-vs-magnitude |
| 2026-Gao-Adversarial Alignment (VC-LLM) | Bilingual consistency check; but same-ideology judge shows "alignment" is culturally relative |
| 2023-Wang-STREAM | Multi-dimensional (judgment+degree+confidence) capture; demographic-anchored baselines; MC stability metric |
| 2025-Jigsaw Multilingual | Cross-lingual transfer (train EN, test other) as an evaluation paradigm (thin card, low confidence) |
| 2021-Prabhumoye-Case Study | Universalizability + informed-consent as benchmark criteria; action–rationale consistency |
| 2022-Sahoo-Detecting Unintended Social Bias | Three-layer annotation (label+category+free-text implication); AUC fairness metrics; counter-narrative augmentation |
| 2024-DAlessandro-Deontology and Safe AI | Safety and moral-alignment are orthogonal axes; stress-test moral theories for catastrophic edge cases |
| 2024-Li-Preference Tuning Generalizes | Cross-lingual safety-transfer gap as a benchmark axis; bilingual retrieval predicts transfer (r=0.73) |
| 2024-Vasilev-CRAFT | Entity-level cultural taxonomy; LLM auto-captioning fails on culturally-specific content (needs human validation) |
| 2024-Šekrst-AI Ethics by Design | User-configurable value layers; conflict-detection as an evaluation task |
| 2025-Benavoli-AI Safety Incomplete Preferences | Add an "incomparable" option to preference annotation; lexical priority for safety constraints |
| 2025-Kajiwara-Advancing Hate Speech (MetaHate) | Meta-collection of 36 datasets tests cross-dataset robustness; linguistic error taxonomy of failures |
| 2025-Li-SafetyAnalyst | Structured harm-benefit tree + small interpretable weight set; steerable to a community's label distribution |
| 2025-Neplenbroek-Cross-Lingual Transfer | Track language-generation quality after debiasing; consistency % as a prerequisite validity check |
| 2025-Rodemann-A Statistical Case | Audit preference-data collection for sampling/response bias; include a prescriptive metric alongside empirical |
| 2025-team-Incorporating Diverse Perspectives | Who×What×How coverage grid; 97.1% of cultural benchmarks are majority-collapsed; score against distributions |
| Anthropic-Claude_3.7_Sonnet_System_Card | Four-category "appropriate harmlessness"; CoT faithfulness only 0.30/0.19 (CoT monitoring insufficient); alignment-faking dimension |
| Anthropic-Constitutional_Classifiers++ | Exchange-level (full-context) scoring; vulnerability-discovery-rate normalized by query volume |
| Meta AI-Llama_Guard | Taxonomy-as-input judge; separate prompt vs response classification; 1-vs-all per-category scoring |
| OpenAI-learning-to-summarize-rlhf | Reward-model over-optimization cliff; ROUGE fails to track quality; labeler calibration |
| OpenAI-operator-system-card | Reversibility-stratified error taxonomy; layered-mitigation ablation; confirmation-recall metric |
| 2025-Aina-Virtue Ethics by Design | (paywalled, thin) virtue-oriented design + adaptive testing paradigm |
| 2025-Okamoto-AI medical ethics | Principlism-default as a testable alignment failure; prompt-sensitivity as a construct-validity threat |
| 2025-Sun-Axiology MCDA | Intrinsic-vs-instrumental value taxonomy; MCDA for transparent, auditable trade-off aggregation |
| 2026-Hendricks-LLMs Fuel Extremist Attitudes | "Positive" rights/fairness framings can fuel extremism — naive "positive values = safe" is wrong |

## C. Patterns & disagreements

**Convergence.** (a) Representative/ecological evaluation beats curated held-out sets [2024-Tonneau-NaijaHate; 2024-Kaneko-Eagle; 2025-Brito-ToxSyn]. (b) Minimal-pair contrast items dominate across bias/hate/moral domains [2018-Zhao; 2022-Das-HateCheckHIn; 2024-Yan-M$^3$oralBench; 2025-Wang]. (c) Report IAA and annotator demographics [2020-Sigurbergsson-DKHate; 2022-Ziems; 2024-Tonneau-NaijaHate] — PerGOLD the negative case [2025-Jafarinejad-PerGOLD]. (d) Multi-facet scoring over a single scalar [2020-Mathew-HateXplain; 2025-Hilliard; Anthropic-Claude_3.7]. (e) Validate automated judges against humans [2023-Vidgen; 2024-Jain-PolygloToxicityPrompts].

**Disagreements.** (i) *Refusal scoring.* LocalValueBench scores refusal 0 ("engagement > refusal") [2024-Meadows-LocalValueBench] and FAI treats unjustified refusal as anti-flourishing [2025-Hilliard], while SimpleSafetyTests treats refusal as correct and warns of unmeasured over-refusal [2023-Vidgen]; HateBench wants refusal as an explicit third label [2025-Shen-HateBench]. Anthropic reconciles: separate *appropriate* from *unnecessary* refusal [Anthropic-Claude_3.7]. (ii) *Human preference as ground truth.* Most preference work assumes it; Rodemann calls it a biased sample needing prescriptive supplements [2025-Rodemann], and D'Alessandro argues moral-alignment can diverge from safety [2024-DAlessandro]. (iii) *What "aligned" means.* VC-LLM's aligned answers are unambiguous pro-state positions with GPT-4o's balanced answers scoring lowest — a same-ideology judge makes "alignment" culturally relative [2026-Gao], contradicting the diversity-aware ideal [2025-team-Incorporating Diverse Perspectives]. (iv) *Synthetic vs natural.* LLM-generated items scale cheaply [2022-Bang; 2025-Brito-ToxSyn; 2024-Yan] but Eagle shows they poorly proxy real harms [2024-Kaneko-Eagle]. (v) *Rationale supervision.* HateXplain implies human rationales help [2020-Mathew]; TeSent shows they improve plausibility yet NOT fairness [2025-Kumar-TeSent].

## D. Exemplars & anti-patterns

**Best-designed.** *VisAlign* — four formal dataset requirements, Cronbach's α=0.88 to justify sample size, κ=0.91/0.80, expert (zoologist) class validation, three-tier ground truth with abstention, soft human distributions scored by Hellinger distance [2023-Lee-VisAlign]. *NaijaHate* — separates representative evaluation from curated training, quantifies the holdout-vs-random gap, discloses annotators, outputs a cost-recall curve [2024-Tonneau-NaijaHate]. *HateCheckHIn* — functional decomposition + minimal-pairs + κ=0.95 + per-group scoring [2022-Das-HateCheckHIn]. *SynthBias/UCerF* — difficulty by human ambiguity, joint correctness×confidence scoring, embedding-space diversity audit [2025-Wang]. Among lab cards, the *Claude 3.7 card* models rigorous process: multi-team ASL determination, four-category harmlessness, alignment-faking and CoT-faithfulness dimensions, honest admission that CoT monitoring is insufficient [Anthropic-Claude_3.7_Sonnet_System_Card].

**Anti-patterns.** *PerGOLD* reports no IAA, only 4 taggers, unspecified events, no license — reliability unknowable [2025-Jafarinejad-PerGOLD]. *DKHate* honestly exposes a foundational flaw: an "any profanity ⇒ offensive" rule (adopted to raise agreement) turned the label into a profanity-detector defined by one non-native annotator [2020-Sigurbergsson]. *LocalValueBench* has student authors as their own reviewers, n=6 topics, and conflates legality with ethics [2024-Meadows]. *VC-LLM* uses a value-committed judge told to "always adhere to Chinese values," so high human agreement validates nothing cross-culturally [2026-Gao]. Cross-cutting: aggregate metrics mask task-total failure — "Macro F1 scores are dangerously deceptive" [2025-Brito-ToxSyn].

## E. Design lessons

1. **Evaluate on a representative sample, not a curated one; sample training and evaluation splits differently and report the holdout-vs-random gap** [2024-Tonneau-NaijaHate; 2024-Kaneko-Eagle; 2025-Machlovi-GuardEval].
2. **Use minimal-pair contrast items** to isolate the decision boundary and catch shortcut learning; include hard negatives (benign identity mentions, reclaimed language, counter-speech) [2018-Zhao; 2022-Das-HateCheckHIn; 2025-Brito-ToxSyn; 2022-Ziems].
3. **Decompose the label.** Prefer functional/capability decomposition or multi-facet same-item scoring over a single scalar; distinguish appropriate from unnecessary refusal [2022-Das-HateCheckHIn; 2020-Mathew; Anthropic-Claude_3.7].
4. **Always report IAA (κ/α) and annotator provenance** (native language, demographics, ideology) — disclosing them defines the construct [2020-Sigurbergsson; 2022-Ziems; 2024-Tonneau; PerGOLD as counter-example].
5. **Treat disagreement as signal:** collect multiple judgments, record consensus/confidence, score against distributions (Jensen-Shannon/Hellinger), flag contested items via entropy rather than averaging to a majority [2022-Ziems; 2023-Lee-VisAlign; 2025-team-Incorporating Diverse Perspectives].
6. **Anchor to external ground truth** (labor statistics, validated psychometric stimuli, aggregated human vectors) [2018-Zhao; 2024-Yan; 2025-Zaim Bin Ahmad].
7. **Engineer against saturation:** stratify by a difficulty axis, define difficulty by human-judged ambiguity, keep a floor-test tier [2024-Jain; 2025-Wang; 2023-Vidgen].
8. **Validate and triangulate automated scorers** against humans (two independent judges, analyze disagreement); beware judge bias and reward over-optimization [2023-Vidgen; 2024-Jain; OpenAI-learning-to-summarize-rlhf].
9. **Evaluate agentic/multi-turn and full-exchange context,** not isolated turns; separate direct-misuse from adversarial-environment evals; report layered-mitigation ablations and reversibility-stratified severity [Anthropic-Constitutional_Classifiers++; OpenAI-operator; 2025-Backmann].
10. **Do not rely on English-only evaluation.** Build natively (not by translation), score in the evaluation language, and track language-generation consistency as a prerequisite validity check [2025-Al; 2025-Neplenbroek; 2024-Li-Preference Tuning; 2024-Vasilev].
11. **Report peak AND cross-validated performance with variance,** and run each model more than once (FAI's single-run design is a weakness) [2025-Mining-Albanian; 2025-Hilliard].
12. **Make the value framing explicit and, where contested, selectable:** per-framing leaderboards, steerable weights, an "incomparable"/abstain option, lexical priority for safety [2024-Defrance-ABCFair; 2025-Li-SafetyAnalyst; 2025-Benavoli; 2023-Lee-VisAlign].
13. **Do not assume "positive" or human-preferred = safe:** rights/fairness framings can amplify extremism, moral-alignment can diverge from safety, and preference data is a biased sample [2026-Hendricks; 2024-DAlessandro; 2025-Rodemann].
14. **When true negatives are unavailable or classes imbalanced, switch metrics deliberately** (Macro-Recall over F1); keep base-rate-faithful imbalance [2025-Brito-ToxSyn; 2023-Haq].
15. **Quality-gate synthetic/LLM-generated items** with human validation on disagreement cases and fidelity checks (CLIP, human relabel) — auto-labeling fails on culturally-specific and real-interaction content [2024-Lin-AI-Face; 2024-Yan; 2024-Kaneko-Eagle; 2024-Vasilev].
