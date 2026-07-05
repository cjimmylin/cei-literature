# 12 — Pluralism, Aggregation, and Whose Values

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-pluralism-aggregation-dossier.md` (~160 cards). `[stem]` = evidence card.
> **Scope:** the question underneath every values benchmark — whose values does it encode, how is
> disagreement handled, and what aggregation is defensible. This is where most benchmarks are
> philosophically weakest and where a well-designed benchmark differentiates itself.

---

## 1. The field's structural failure and the fix

**97.1% of cultural-alignment datasets collapse human disagreement to a single majority label**
[2025-team-Incorporating Diverse Perspectives] — while individual differences explain 39.5% of
offensiveness variance vs 2.9% for country [2023-Davani], and preserving all ratings yields ~53% greater
downstream toxicity reduction than majority vote [2025-Sorensen]. Disagreement is structured signal:
it decomposes into interpretable trait×prompt variance [2026-Li-PluriHarms], and expert-vs-crowd gold
disagree on 34% of items [2023-Aroyo-DICES].

**The fix, now standard among exemplars:** ship annotator-level labels with demographics AND validated
psychometrics (MFQ-2, Schwartz, WVS, political leaning) so every item carries a portable value vector;
score against the full distribution (KL/JSD/L2) with an explicit empirical ceiling (KorNAT: ceiling
0.450, best model 0.331 [2024-Lee-KorNAT]); let users re-aggregate [2023-Aroyo-DICES].

## 2. Determinism as misalignment

When humans genuinely disagree, a model that answers deterministically is *miscalibrated to the
construct*: humans give ~17.3% non-majority answers on kidney-allocation vs GPT-4o 2.98%
[2025-Dickerson]; models "reproduce human judgments only under high consensus" and collapse toward the
majority as disagreement rises (Δ~0.34 at 0.5 consensus) [2025-Russo-Pluralistic Moral Gap]; LLMs are
near-clones of each other (cross-model r=0.99–1.00) while humans span −0.79 to 0.98 [2026-Huang].
**Design implications:** sample N times per item and score the *response distribution*; offer explicit
indecision/coin-flip options and score their calibrated use; add entropy/diversity metrics so a model
cannot win by always hitting the mode.

## 3. Whose values: the source taxonomy (and what each costs)

| Source of ground truth | Exemplar | Cost / risk |
|---|---|---|
| Census-reweighted national survey | KorNAT (6,174 Koreans, sampling-error bounds) [2024-Lee-KorNAT] | descriptive-not-normative; survey's own bias |
| Global survey instruments (WVS, PEW, Moral Machine) | GlobalOpinionQA JSD [2025-Durmus]; MULTITP 40M judgments [2024-Jin] | WEIRD skew in instrument; self-selection (Moral Machine skews young/male/educated) |
| Participatory deliberation | Collective Constitutional AI (1,002 US adults, Group-Aware Consensus; lower bias on all 9 BBQ dims at equal MMLU) [2024-Huang] | demonstrated at one national scale only; manipulation resistance unknown |
| Affected-community co-design | context experts raised agreement 68.75%→93% [2022-Nkemelu]; targeted-group annotators [2021-Cercas Curry-ConvAbuse] | recruitment cost; positionality must be documented |
| Expert/professional protocol | TRIAGE (START protocol gold) [2024-Kirch]; 12 medical ethicists [2025-Hong] | narrow domains only |
| Law / regulation | AIR-Bench clause-anchoring [2024-Zeng]; legal-alignment arguments [2026-Kolt] | law ≠ ethics; jurisdiction relativism |
| Philosophy-weighted theory panels | MEC with PhilPapers credences (32/31/37%) [2023-Boddington] | contested weighting |
| State/media corpora | NaVAB, C-VARC, HKGAI — "official stance = national values" | anti-pattern when conformity is scored as safety [2025-Han-HKGAI-V1] |
| Undisclosed lab crowdworkers | InstructGPT: ~40 contractors, 75% under 35, 96% English data [OpenAI-instructgpt] | the default anti-pattern — invisible narrow alignment |

**Rule:** the source is a *disclosure requirement*, not a solved choice. Put "who are we aligning to"
in the datasheet with the same rigor as dataset statistics (Law 7).

## 4. Aggregation is a normative act — expose it

- Social aggregation "merely relocates the moral terrain": who has standing, how preferences are
  elicited, which rule — bounded by Arrow-type impossibility [2025-Baum]; no classifier satisfies
  statistical parity + equalized odds + calibration simultaneously with unequal base rates
  [2024-Hendrycks]; "the winner depends on the framing" across 7 provably-incompatible fairness notions
  [2024-Defrance-ABCFair]. The RLHF pipeline embeds this invisibly — annotators deviate from principle
  consensus 28.9%, and the divergence concentrates in the RL step (DD ~69–71% vs RM ~14%) [2025-Buyl];
  reward models encode stable sociodemographic preference rankings (Spearman r=0.67 across 7 RMs;
  income r=0.91) [2025-Elle].
- **Defensible moves, in order of preference:** (1) interpretable steerable weights re-fittable per
  community [2025-Li-SafetyAnalyst]; (2) per-framing leaderboards / moral-parliament vectors with no
  collapse [2024-Defrance; 2024-Hendrycks]; (3) a single declared rule with its normative commitment
  stated; (never) a hidden default.
- **Tiered normativity is the workable compromise** (doc 01, Step 0): a non-negotiable universal floor
  (baseline safety, UDHR-level harms — scored strictly with high-κ gold labels) + a context-dependent
  pluralistic layer (scored distributionally) + a declared conflict ordering [2026-He-GVS-Scale;
  2025-Wang; 2025-Yaacov; 2024-Varshney's sādhāraṇa/viśeṣa]. Declare the floor as a stipulation, not a
  discovery — and note the critique that even the UDHR is contested as universalism [2024-Varshney].

## 5. The WEIRD default (what you are correcting for)

Un-prompted LLMs encode a Western/global-average profile: all 20 tested LLMs (Chinese- and US-origin
alike) answer MFQ-2/WVS more like Americans than Chinese (origin×nationality interaction 10× smaller
than nationality effect) [2025-Haslett]; alignment tracks web-content-per-country r=0.94 [2025-Sukiennik];
prompting in Russian/Chinese/Turkish does NOT shift values toward those populations — **language ≠
culture** [2023-Durmus]; models compress within-country variance (US R²=0.80 vs Nigeria 0.01
[2023-Benkler]). Western constructs also fail to transfer: India's salient axes are Region and Caste
[2022-Shaily Bhatt; 2024-Sahoo-IndiBias]; Afro-relational trust, Maqasid, Ubuntu, Confucian role-ethics
supply axes absent from every mainstream benchmark [2025-Amugongo; 2024-MaqasidAI; 2022-Gwagwa] — but
must be operationalized into scoreable items, not aspirational descriptors ("too vague to encode"
critique [2025-Yilma]). Full treatment: docs 10, 11.

## 6. Elicitation confounds specific to pluralism

- **Expressed ≠ revealed** (doc 06): MCQ stability diverges from interactive behavior [2025-Liu-ConflictScope];
  cross-instrument coherence collapses for LLMs (R²<0.08 vs human 0.17–0.38) [2024-Nunes].
- **Group deliberation distorts**: LLM panels drift utilitarian (β=0.31; opposite the human direction)
  [2025-Keshmirian]; diversity dissolved through consensus is diversity lost — if you use multi-agent
  aggregation, measure the drift it introduces.
- **Human ground truth is unstable on exactly the items that matter**: 10–18% test-retest flips on
  controversial items [2024-Boerstler] — stratify by consensus and propagate instability into error bars.

## 7. Adjudications

1. **Majority vote vs distribution?** Distribution, whenever measured human consensus <~85% (doc 01,
   Adjudication 1). Both scores can be reported; never only the collapsed one.
2. **Is human-likeness the target?** No (mimetic fallacy) — for *pluralism* constructs the target is
   matching the human distribution; for *agent behavior* the target is the declared normative framework;
   humans themselves want agents to act differently than humans [Kneer; 2024-Lazar].
3. **Descriptive survey vs prescriptive floor?** Both, tiered: survey distributions govern the
   pluralistic layer; the declared floor overrides where descriptive averages encode harms ("aligning to
   averages may not be desirable if those averages encode harmful biases" [2024-Jin-MULTITP]).
4. **Can non-Western frameworks be benchmarked?** Yes, but only via co-design with affected communities
   producing action-guiding items (paired individual-vs-community items for Ubuntu; Region/Caste axes
   for India), with ethnographic verification — not by importing framework names as labels [2025-Yilma;
   2024-Sahoo; docs 10–11].
5. **Incomparability**: allow "incomparable / no ranking" as a valid, scoreable response and test whether
   models confabulate rankings over incommensurable values [2024-Zhi-Xuan; 2025-Benavoli].

## 8. Checklist (pluralism section of any new benchmark)

- [ ] Datasheet answers "whose values" with annotator demographics + psychometric value vectors
- [ ] Annotator-level labels shipped; users can re-aggregate
- [ ] Distributional scoring on contested band; N-sample elicitation; entropy/diversity metrics
- [ ] Empirical ceiling from human disagreement (≠1.0); consensus stratification
- [ ] Tiered normativity: declared universal floor + pluralistic layer + conflict ordering
- [ ] Aggregation exposed (steerable weights or per-framing reports); no hidden rule
- [ ] Determinism-under-disagreement measured as a failure mode
- [ ] Native authoring / co-design for each cultural context; positionality documented
- [ ] Incomparability allowed and scored; test-retest instability propagated
- [ ] "Ethics" framing avoided; construct stated as values-of-population-X (Law 7)

**Drill-down:** `20260705-pluralism-aggregation-dossier.md` §2 (five decision axes), §3 (nine
disagreements incl. the Noothigattu boundary case), §4 (DICES, KorNAT, PluriHarms, CCAI, ABCFair
exemplars; HKGAI/Delphi/NaVAB anti-patterns).
