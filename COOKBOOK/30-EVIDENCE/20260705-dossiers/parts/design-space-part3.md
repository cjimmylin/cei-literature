# design-space — sub-dossier part 3/4

Scope: 58 cards across hate-speech corpora, bias probes, moral-reasoning benchmarks, fairness meta-benchmarks, safety/agentic benchmarks, and machine-ethics theory — the menu of task formats, scoring, and dataset construction.

## A. Synthesized claims

1. **Minimal-pair counterfactual substitution is the workhorse for isolating one value/identity variable.** Hold a sentence fixed, swap one identity token, and any output difference is causally attributable to it [2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred]. The 8,640-sentence Equity Evaluation Corpus (11 templates) shows 75–86% of 219 systems scored one gender higher, yet mean deltas were <0.03 (3% of range) even as max delta hit 0.34 (p.6) — bias *pervasive but small in mean*, surfaced only by paired testing. The lever recurs as grammatical-gender morphology [2024-Pikuliak-Women Are Beautiful Men Are Leaders Gender Stereotypes in Machine; 2025-Team-EuroGEST Investigating Gender Stereotypes in Multilingual Language] and leading/non-leading prompt pairs [2025-Muñoz-García-Leading and Non-Leading Prompts Quantifying Gender Bias in Large].

2. **Distributional (soft) labels beat majority-vote hard labels when disagreement is intrinsic.** Scruples targets the full 5-label annotator distribution (626,714 judgments over 32,766 anecdotes), scoring by distributional cross-entropy with a Bayesian BEST oracle and Dirichlet-multinomial layer to separate model uncertainty from controversiality [2021-Lourie-Scruples]. OffendES's 10-annotator subset yields per-label probability vectors for multi-output regression [2021-Plaza-del-Arco-OffendES A New Corpus in Spanish for Offensive Language Research].

3. **Score the reasoning, not just the verdict** — a correct choice with a wrong rationale is a failure benchmarks must catch: matched correct-vs-plausible-but-wrong reasoning chains [2025-Galatolo-Beyond Ethical Alignment]; LLM-judge rationale classification into consequentialist/deontological labels [2025-Samway-Are Language Models Consequentialist or Deontological]; an `ideal_response_profile` of required principles [2025-Herrador-The PacifAIst Benchmark]; justifications/steerability/moral-sensitivity as first-class behaviors [2025-Snoswell-Beyond Verdicts LLM Moral Competence].

4. **Distributional-similarity scoring generalizes verdict-matching to opinion space.** GlobalOpinionQA scores 1 − Jensen-Shannon Distance between model and country-level human distributions over 2,556 survey MCQs (metric-agnostic) [2025-Durmus-Towards Measuring the Representation of Subjective Global Opinions in]. SVO work maps free-text choices to a scalar angle, defining "value rationality" as distance from an ideal angle [2023-Zhang-Heterogeneous Value Alignment Evaluation for].

5. **Template × fragment combinatorics is the dominant scalable construction method, but needs a scope statement.** The MLCommons AI Safety Benchmark builds 43,090 items from 725 fragments × 32 speech-act templates, with explicit scope (adult × general assistant × English × Western) and 3 personas [2024-Group-The AI Safety Benchmark]. SHADES uses grammatical-agreement slot tags (`<GENDER:MASC>`) for the same pattern across languages [2018-Kiritchenko-...; 2025-Al-Towards a Multilingual Assessment of Stereotypes in Large ...].

6. **Macro-F1, not accuracy, is near-universal for imbalanced tasks**, since positive-class prevalence is tiny. SemEval-2019 oversampled hate to ~40–42% vs ~10% natural [2019-Basile-SemEval-2019 Task 5]; Jahan (~0.93% natural) keyword-seeded to 5k/10.7k [2022-Jahan-Finnish Hate-Speech Detection on Social Media Using CNN and FinBERT]; Trager's raw kappas are low from base rates, needing PABAK [2022-Trager-The Moral Foundations Reddit Corpus]. Velankar's *balanced* 6,250-per-class design is a deliberate exception [2024-Velankar-SamPar A Marathi Hate Speech Dataset].

7. **Subjective-item agreement is often only "fair," bounding achievable model scores.** OffendES κ=0.3579 [2021-Plaza-del-Arco-OffendES...]; CharMoral Fleiss κ=0.55 [2025-Bae-CharMoral]. Expert-taxonomy anchoring lifts it: Turkish superset Krippendorff α=0.84 [2024-Tonneau-Turkish Hate Speech Superset Dataset], AI Safety Benchmark κ=0.79 [2024-Group-...].

8. **Audit whether the construct is stably present before trusting a dataset.** FFB ran 45,079 experiments (14,428 GPU hours), documents reported Adult accuracy drifting 0.17 (~20%) across prior papers, and runs an ERM baseline across seeds to test whether bias is reliably elicited [2023-Han-FFB]. ABCFair makes problem-framing (intervention stage, group composition, notion, output format) selectable because "the winner depends on the framing" — 98 result tables, 294 trade-off plots [2024-Defrance-ABCFair].

9. **Hierarchical / multi-dimensional annotation per item multiplies reuse and mirrors moderation workflows.** Aggressiveness/target labeled only for confirmed-hateful items [2019-Basile-...]; four simultaneous dimensions [2024-Tonneau-...]; two-level binary→{Violence,Hate,Vulgar} + rationale spans [2024-Z. Delbari-Spanning the Spectrum of Hatred Detection A Persian Multi-Label Hate]; four-task generative output [2023-Maity-Ex-ThaiHate A Generative Multi-task Framework for].

10. **Span/rationale annotation upgrades classification into an explanation benchmark.** HATECAT-TR labels character-level spans (BIO/IO, SeqEval F1) [2025-Seker-HATECAT-TR A Hate Speech Span Detection]; PHATE adds a shortest-supporting-span and quantifies its contribution via rationale-masked vs random-masked F1 [2024-Z. Delbari-...].

11. **Multi-step / path-dependent scenarios stress-test consistency single-turn items miss.** Staircase escalates 3,302 scenarios over 5 steps, comparing full/no/causal-context and arguing causal context best mirrors human path-dependence [2025-Wu-The Staircase of Ethics Multi-step Moral Dilemmas]; AgentBench varies rounds 5→35 as difficulty [Zhipu AI-AgentBench_2308.03688]; 8-setting context-ablation quantifies each element's marginal contribution [2025-Bae-CharMoral].

12. **LLM-as-judge/generator is now standard but needs validation and family-separation controls.** MedES's LoRA-tuned QWQ-32B guardian (test F1 >0.96) keeps evaluator + test-annotator in the Qwen family while base model + training-annotator are DeepSeek, to reduce self-preference [2026-Jin-MedES Chinese Medical Ethics Scenarios]; Samway's Gemini judge is human-validated (P=0.845, F1=0.820) [2025-Samway-...]; LlamaGuard scored 70.4% on human eval [2024-Group-...]; GPT-4o-first-then-human-revise cuts cost [2025-Seker-...].

13. **Pluralism aggregation is a live, unsettled axis.** Maximizing Expected Choiceworthiness with equal theory credences (justified by ~32/31/37% philosopher endorsement of consequentialism/deontology/virtue) [2023-Boddington-Normative Ethical Theory AI Ethics]; but formal work argues every aggregation rule relocates the normative choice and faces Arrow-type impossibility [2025-Baum-Aggregation Problems in Machine Ethics], that pluralist models collapse to monism or flatten via aggregation [2025-Yaacov-Normative Moral Pluralism for AI], and that benchmarks should report per-framing leaderboards not one number [2024-Defrance-...].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Kiritchenko-Examining Gender and Race Bias | Minimal-pair template swap; bias in 75–86% of systems but mean delta <0.03, max 0.34 — only paired t-tests (Bonferroni over 438) reveal it |
| 2019-Basile-SemEval-2019 Task 5 | Hierarchical conditional labels; Exact-Match-Ratio for joint multi-label; oversample hate to ~40% |
| 2019-Ibrohim-Multi-label Hate Speech | Government/legal (Bareskrim Polri) partnership grounds "strong vs weak" label definitions |
| 2020-Pitenis-Offensive Language in Greek | Monolingual embeddings beat mBERT 0.89 vs 0.73; keyword-seeded minority-class sampling |
| 2021-Lourie-Scruples | Distributional labels + BEST oracle + Dirichlet-multinomial; 626,714 judgments; cross-entropy over accuracy |
| 2021-Plaza-del-Arco-OffendES | 10-annotator probability-vector subset for multi-output regression; NOE separates positive expletives from offense; κ=0.36 |
| 2022-Jahan-Finnish Hate-Speech | Language-specific pretraining gap quantified (FinBERT vs mBERT 3.5–5%); ~0.93% natural hate → keyword seeding |
| 2022-Trager-Moral Foundations Reddit Corpus | Annotator demographic/psychological metadata as a research object; PABAK for low-base-rate labels |
| 2023-Boddington-Normative Ethical Theory | MEC pluralism aggregation with equal-credence theory ensemble; PhD forced-choice qualitative eval |
| 2023-Han-FFB | Cross-paper variance table: same metric drifts 0.17 across papers → run ERM baseline to confirm construct present |
| 2023-Lee-KoSBi | Generate-then-classify paradigm; rejection sampling over k=8 improves safe-output ratio |
| 2023-Plaza-del-Arco-MarIA and BETO | MLM probe: top-10 adjectives × 3 categorization schemes; BPI/BRI probability- and rank-based bias indices |
| 2023-Zhang-Heterogeneous Value Alignment | SVO Slider (6 MCQ × 9 options) → scalar angle; "value rationality" = distance to ideal angle |
| 2024-Defrance-ABCFair | Configuration-as-first-class: report per-framing leaderboards; dual-label (biased train / unbiased eval) |
| 2024-Group-The AI Safety Benchmark | 725 fragments × 32 speech-act templates = 43,090; explicit scope + 3 personas; conservative min-across-tests grade |
| 2024-Jiang-WildTeaming at Scale | Diversity-aware attack metrics (ASR×n, Sim@n, #Tactics); auto-mine tactics from real adversarial logs |
| 2024-Pikuliak-GEST | Grammatical gender as a latent measurement device; two mutually-exclusive failure modes (stereotypical vs masc-default) |
| 2024-Tonneau-Turkish Hate Speech Superset | 4 simultaneous dimensions per tweet; Krippendorff α=0.84; domain-split (Istanbul Convention vs Refugees) |
| 2024-Z. Delbari-PHATE | Rationale-span validity test (rationale-masked vs random-masked F1); controversial/ambiguous keyword sampling (not slur lists) |
| 2025-Al-SHADES | Grammatical-agreement slot tags for grammatically valid multilingual generation; base (log-prob) vs instruct (yes/no) paradigms |
| 2025-Bae-CharMoral | 8-setting context-ablation; longitudinal "moral dynamic score" (0.5-crossing rate) |
| 2025-Durmus-GlobalOpinionQA | 1−JSD distributional similarity to country-level human distributions; cross-national & linguistic prompting conditions |
| 2025-Galatolo-Beyond Ethical Alignment | Matched correct-vs-plausible-wrong reasoning chains; static Task-1 accuracy <35% for all models; composite AMA score |
| 2025-Herrador-PacifAIst | Model-as-agent existential-prioritization MCQ; P-Score + Refusal Rate 2D behavioral profile; ideal_response_profile |
| 2025-Kilov-Discerning What Matters | Moral sensitivity (embed relevant features among irrelevant detail); Bradley-Terry pairwise vs human baseline |
| 2025-Li-Untangling Input Language | 2×2 input/reasoning-language factorial; flip-rate & sensitivity-ratio stability taxonomy; Split-Authority MFQ refinement |
| 2025-Mining-Albanian hate speech | Character-level n-gram TF-IDF as robust low-resource baseline (~84%) needing no language resources |
| 2025-Samway-Consequentialist or Deontological | LLM-judge rationale classification (16-label MoralLens); reasoning-order manipulation exposes post-hoc rationalization |
| 2025-Seker-HATECAT-TR | Character-level span detection (BIO/IO, SeqEval); GPT-4o-first + human-revise semi-automated annotation |
| 2025-Team-EuroGEST | Log-likelihood on 71k minimal gendered pairs across 30 languages; heuristic pair extraction (≤2 letters, ≤1 word) |
| 2025-Wu-Staircase of Ethics | 5-step escalating dilemmas; full/no/causal-context comparison; 3-LLM consensus value labeling |
| 2026-Jin-MedES | 1,278 atomic rules from authoritative docs used both to generate items AND score compliance; family-separated evaluator |
| 2023-Maity-Ex-ThaiHate | Single generative seq2seq emits label+sentiment+emotion+rationale in one pass |
| 2024-Velankar-SamPar | Deliberately balanced 4-class (6,250/class) separating group-hate / individual-offense / profanity |
| 2025-Muñoz-García-Leading Prompts | Leading vs non-leading prompt pairs isolate prompt-induced from model-intrinsic bias |
| 2016-Amodei-Concrete Problems | Reward hacking / Goodhart: formal objectives get gamed — argues against single-scalar optimization targets |
| 2018-Berberich-The Virtuous Machine | Crowd-sourced exemplar trajectories (IRL) as a per-cultural-zone construction method |
| 2019-Corazza-Cross-Platform Italian | Fix architecture, vary only training-data mixture; cross-platform pooling helps all platforms except Twitter |
| 2020-Mainali-Modes of Moral | Small-corpus bootstrapping: 25 articles suffice to train a transferable consequentialist/deontological classifier |
| 2022-Ramanayake-Pro-Social Rule Breaking | Test *when to appropriately violate* a rule; justification-quality discrimination (well- vs poorly-justified breaking) |
| 2023-Ibrohim-Indonesian review | Definitions come from 5 sources; legal (Bareskrim Polri) is most authoritative; binary reaches 98.7% acc but multi-label drops to 66% |
| 2023-McDonald-Categorical Imperative | Formula of Humanity (never treat as mere means) as a clearer alignment target than utility-max |
| 2024-Boerstler-Stability of Moral Preferences | Test-retest reliability (10 sessions/2 weeks) as a mandatory validity check for preference benchmarks |
| 2024-Keswani-Active Learning for Moral Preference | Pre-deployment simulation diagnostic for preference-elicitation instability/misspecification/noise |
| 2024-Stenseke-Computational Complexity of Ethics | Moral Tractability Thesis: a benchmark's demanded reasoning should be computationally tractable |
| 2024-University-Emerging Coded Terms | LLM coded-term discovery pipeline as a benchmark-maintenance / evasion-discovery tool |
| 2025-Baum-Aggregation Problems | Formal MDS 5-tuple; every aggregation rule relocates normative choice, faces Arrow-type impossibility |
| 2025-El Masri-Towards Attuned AI | RLHF/RLAIF are inherently utilitarian; ethics-of-care weighting for edge-case users |
| 2025-Graves-AI Practical Wisdom | 7-category suffering taxonomy (multi-tradition, anti-WEIRD) as a recognition-benchmark basis |
| 2025-Liu-Scales of Justitia | R=E(T,D,P,M) checklist; dataset composition taxonomy (Q-only/Q&A/MCQ/Dialogue); graded (not binary) success metrics |
| 2025-Nay-Law as Information | Fiduciary duty (care+loyalty) and public law as democratically-grounded alignment ground truth |
| 2025-Snoswell-Beyond Verdicts | "Acceptable range" under reasonable pluralism instead of single ground truth; evaluate justifications/consistency/steerability |
| 2025-Yaacov-Normative Moral Pluralism | Moral threshold = benchmark floor excluding unreasonable answers without forcing one correct answer |
| 2026-Goel-Interpretable Moral | Compositional token design (who/how-many/which-side) + causal ATE for group-influence measurement |
| Anthropic-Responsible_Scaling_Policy_1.0 | Tiered (ASL-style) benchmark stringency; conservative thresholds with explicit safety buffers; best-elicitation requirement |
| Zhipu AI-AgentBench | POMDP formalization; 5-type failure taxonomy; inverse-average weighting so easy domains don't dominate |
| 2023-Roger-Ethical multimodal | Gamified Discord emoji-reaction crowd labeling (ethical/unethical/unclear) with user pre/post-tests |
| 2025-Muntean-Moral Coherentism | Score internal coherence (contradictory rulings on similar cases) rather than rule-following |
| 2025-Sharmaa-Somali/Hindi-English code-switch | Partial transliteration preserving syntax; explicit profanity-vs-hate decoupling for construct validity |
| 2025-Zgliczynski-Ethical Resonance | Cultural-universality index and cross-domain transfer as external-validity metrics |

## C. Patterns & disagreements

**Convergence.** (1) Macro-F1 for imbalanced classification is near-universal [Basile; Pitenis; Jahan; Trager; Delbari; Mining]. (2) Expert/authority-anchored taxonomies raise agreement and construct validity [Ibrohim 2019 & 2023; Tonneau; Seker; Pikuliak; Graves]. (3) Keyword/lexicon-seeded sampling to overcome tiny natural prevalence is the default collection trick [Pitenis; Jahan; Delbari; Velankar]. (4) Reasoning quality, not just verdicts, is the frontier [Galatolo; Samway; Herrador; Snoswell; Maity]. (5) Monolingual/language-specific resources beat multilingual models on culturally-specific tasks [Pitenis 0.89 vs 0.73; Jahan; Velankar].

**Disagreements.** (a) *Ground truth vs acceptable range*: MedES and PacifAIst use exact-match against a single "correct" choice [Jin; Herrador], while Snoswell and Yaacov argue accuracy-against-ground-truth is wrong for moral items and propose an "acceptable range" / moral-threshold floor [2025-Snoswell-...; 2025-Yaacov-...]. (b) *Balanced vs natural class distribution*: Velankar deliberately balances classes [2024-Velankar-...] whereas Basile oversamples but toward natural-ish prevalence and most treat imbalance as the thing to preserve/measure [2019-Basile-...]. (c) *Aggregation*: Boddington endorses equal-credence MEC aggregation [2023-Boddington-...] while Baum and Yaacov argue aggregation is impossible/illegitimate and Defrance says report per-framing instead of aggregating [2025-Baum-...; 2025-Yaacov-...; 2024-Defrance-...]. (d) *Cross-platform/cross-domain pooling*: Corazza finds pooling helps everywhere except Twitter (in-domain wins) [2019-Corazza-...], a caution against assuming more heterogeneous data always helps.

## D. Exemplars & anti-patterns

**Best-designed.** *MLCommons AI Safety Benchmark* [2024-Group-...]: explicit scope, persona-conditioned generation, speech-act template taxonomy, validated grader (LlamaGuard κ=0.79), conservative min-across-tests aggregation — names its limits instead of claiming "safety in general." *ABCFair* [2024-Defrance-...] and *FFB* [2023-Han-...]: exemplary meta-design — framing as selectable, cross-paper drift quantified, construct audited before ranking. *Scruples* [2021-Lourie-...]: distributional labels + principled oracle for intrinsic disagreement. *MedES* [2026-Jin-...]: rule-grounded auditable answers tied to statutes, family-separated validated evaluator.

**Anti-patterns.** *Accuracy-only on imbalanced data*: SamPar reports only accuracy — insufficient for imbalanced hate detection [2024-Velankar-...]. *Hard fair-κ labels without soft targets*: OffendES κ=0.36 [2021-Plaza-del-Arco-...] and CharMoral κ=0.55 [2025-Bae-...] force majority labels onto contested items, discarding signal Scruples-style distributions keep. *Under-specified scoring*: Ramanayake's pro-social-rule-breaking construct has no operational metric [2022-Ramanayake-...]; Ex-ThaiHate's generative multi-task framing lacks confirmed metrics [2023-Maity-...] — generative multi-field outputs need a specified structured-extraction grader.

## E. Design lessons

1. **State scope before items.** Specify SUT × use-case × persona × context and whose values are measured, rather than claiming general "safety" or "morality" [2024-Group-The AI Safety Benchmark; 2025-Liu-The Scales of Justitia via R=E(T,D,P,M)].
2. **Use minimal pairs to isolate the value variable**, and report paired/distributional deltas — mean effects can be tiny (<0.03) while prevalence is huge (75%+) [2018-Kiritchenko-...; 2024-Pikuliak-...; 2025-Muñoz-García-...].
3. **Prefer distributional/soft labels and cross-entropy for contested items**; add an oracle (BEST) to set the achievable ceiling [2021-Lourie-...; 2021-Plaza-del-Arco-OffendES...].
4. **Grade reasoning, not only verdicts**: matched correct-vs-plausible-wrong chains, rationale classification, and ideal-response profiles defeat "right answer, wrong reason" [2025-Galatolo-...; 2025-Samway-...; 2025-Herrador-...; 2025-Snoswell-...].
5. **For subjective/pluralistic constructs, score an "acceptable range" or enforce a moral-threshold floor** rather than a single gold answer; report per-framing leaderboards instead of one aggregate [2025-Snoswell-...; 2025-Yaacov-...; 2024-Defrance-...].
6. **Use macro-F1 (never bare accuracy) on imbalanced data**, and adjust agreement stats for base rate (PABAK) [2019-Basile-...; 2022-Trager-...; 2024-Velankar- as anti-pattern].
7. **Audit the dataset before trusting it**: run a baseline across seeds to confirm the construct is stably elicited, and tabulate cross-paper metric drift [2023-Han-FFB; 2024-Defrance-...].
8. **Anchor label definitions in expert/legal/authoritative taxonomies** to lift agreement and construct validity [2019-Ibrohim-...; 2023-Ibrohim-...; 2024-Tonneau- (α=0.84); 2026-Jin- (atomic rules); 2025-Graves-].
9. **Validate LLM judges against humans and separate model families** (evaluator ≠ base) to blunt self-preference [2026-Jin-...; 2025-Samway-...; 2024-Group-...].
10. **Add hierarchical/multi-dimensional and rationale-span annotation** for reuse and explanation evaluation [2019-Basile-...; 2024-Tonneau-...; 2024-Z. Delbari-...; 2025-Seker-...; 2023-Maity-...].
11. **Test consistency across steps, contexts, and input/reasoning languages**, not just one-shot verdicts [2025-Wu-...; 2025-Li-...; 2025-Bae- context ablation; Zhipu AI-AgentBench round-count difficulty].
12. **Report test-retest reliability of any preference-elicitation instrument** [2024-Boerstler-...; 2024-Keswani-...].
13. **For low-resource/non-English, build language-specific resources** — monolingual embeddings, character n-grams, native seed lists, grammatical-agreement slot tags, syntax-preserving transliteration — not translated English artifacts [2020-Pitenis-...; 2025-Mining-...; 2025-Al-SHADES; 2025-Muñoz-García-...; 2025-Sharmaa-...; 2025-Team-EuroGEST].
14. **Tier stringency, set conservative thresholds with explicit safety buffers**, commit to a harder version before saturation, and require best-elicitation testing [Anthropic-Responsible_Scaling_Policy_1.0].
15. **Use compositional structured inputs enabling causal attribution** (per-consideration token dims, causal ATE) [2026-Goel-...].
16. **Avoid single-scalar targets that invite Goodharting**; prefer multi-dimensional, inverse-average-weighted aggregation so easy domains don't dominate [2016-Amodei-...; Zhipu AI-AgentBench].
