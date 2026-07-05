# 08 — Normative Ethics: Methods for Benchmarking

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-normative-ethics-dossier.md` (~330 card-reads) + the completed NormEval meta-evaluation
> (`20260705-digests/20260705-normeval-digest.md`: 54 benchmarks × 26 features, 24 gate-passing,
> 15 trialed on 9 models). `[stem]` = evidence card. NormEval landscape claims C1–C5 are empirically
> grounded; its cross-vendor F1–F7 are elicited/exploratory (see digest disclosure) — treat as
> hypotheses to test, which is itself a design opportunity.

---

## 1. The state of the field in five numbers (NormEval, n=54)

1. **100%** — accuracy of all 9 tested models on ETHICS, the field's most-cited normative benchmark
   (p<1e-15). The canonical instrument is dead; it remains the normative component of HELM,
   DecodingTrust, and TrustLLM anyway — no graduation protocol exists (NormEval C1, gap 8).
2. **77% vs 50%** — utilitarian vs deontological accuracy (z=2.17, h=0.57): the consequentialist-bias
   attractor. Framework difficulty: U 77% > V 63% > D 50%; all-three-correct only 37% (C2).
3. **2/54 and 4/54** — benchmarks with substantive care-ethics and contractarian engagement. Zero
   dedicated Gilligan/Noddings/Tronto instruments; zero standalone Rawlsian or Scanlonian benchmarks (C3).
4. **10/54 (18.5%)** — benchmarks testing moral *reasoning* rather than judgment only (C4, p<0.001);
   corroborated corpus-wide: 75% of 69 surveyed papers score verdicts, 27% reasoning, 4%
   information-gathering [2025-Snoswell].
5. **78%** — benchmarks with zero non-Western ethical content; ~76% presuppose moral realism
   (determinately correct answers) (§6.4–6.5).

Every one of these numbers is a standing publication opportunity.

## 2. The three dissociations that structure valid measurement

Normative-ethics evaluation must treat these as SEPARATE measured axes, because they empirically
dissociate:

1. **Judgment vs reasoning.** Process competence has ~zero correlation with capability benchmarks
   (Pearson −0.245 to 0.216) [2025-Chiu-MoReBench]; abductive moral reasoning (value→precept) floors
   at <35% while deductive (precept→consequence) exceeds 95% [2025-Galatolo-AMAeval]. Rubric-based
   procedural scoring was the ONLY method producing discriminative signal at the frontier in NormEval's
   trials (MoReBench 10% rubric coverage vs ETHICS 100% ceiling; inter-tradition spread 14.3 pts:
   Scanlonian 18.3% > Kantian 13.3% > act-utilitarian 8.7% > Gauthierian 5.5% > virtue 4.0%).
2. **Recognition vs evaluation vs behavior.** Models classify 86% of speciesist statements but condemn
   34% [2025-Jotautaite]; pass explicit-value prompts, fail implicit ones [2024-Khamassi]; and under
   incentive conflict no model is consistently moral (7.9–76.3%, game structure R²=0.87)
   [2025-Backmann-MORALSIM]. Knowledge items produce 0% cross-model variance while judgment items
   diverge up to 60% (NormEval F4 — its council's only unanimous finding). **Report knowledge and
   judgment accuracies separately with item counts; an 85% aggregate decomposing to 100/70 means
   something entirely different from 85/85.**
3. **Verdict vs coherence.** Cross-instrument coherence collapses for LLMs (R²<0.08 vs human 0.17–0.38
   — "moral hypocrisy") [2024-Nunes]; only 2/~40 models pass GARP-style revealed-preference rationality
   at 1% [2024-Seror]. Coherence is answer-key-free and contamination-resistant — a scoring family that
   cannot be gamed by memorization.

## 3. Operationalizing the five frameworks (the ladder + per-framework guidance)

**The operationalization ladder** (from the dossier; aim for rung 3+):
(0) framework named in prose, no items — the most common anti-pattern; (1) keyword/classifier split;
(2) theory-in-prompt as a manipulated variable; (3) **structural operationalization** — the framework's
distinctive *method* is what's scored; (4) per-theory reward agents/fine-tunes with principled
uncertainty aggregation (MEC, Dempster–Shafer) [2023-Boddington; 2025-Dubey]; (5) formally verifiable
deontic logic with SAT/UNSAT ground truth [2025-Priya].

Structural operationalizations that work (rung 3):

| Framework | What to score (structural signature) | Anti-pattern | Evidence |
|---|---|---|---|
| **Utilitarian** | welfare aggregation quality; IB vs IH decomposition (Oxford Utilitarianism Scale subscales — separating positive beneficence from instrumental harm is what surfaced NormEval's vendor profiles) | conflating utilitarianism with hedonism (ETHICS does [2024-Hancox-Li]) | [NormEval F1; 2021-Hendrycks] |
| **Deontological** | rule-*selection* and duty-conflict adjudication; duty-to-protect items where inaction is WRONG (defeats the "inaction=deontological" heuristic) | rule-*obeying* classification; physics-solvable "impossibility" items (18% of ETHICS-deontology) | [2024-Hancox-Li; NormEval L10] |
| **Virtue** | dispositional stability across contexts; virtue-centrality of justifications; character-over-act reasoning | keyword spotting; position papers with no items (the entire virtue literature: [2018-Berberich; 2022-Hagendorff]) | open void — no validated instrument exists (dossier §5.1) |
| **Care** | multi-turn relational scenarios scored on Tronto's 4 phases (Attentiveness/Responsibility/Competence/Responsiveness), with the care-recipient's reaction revealed in a later turn and *recipient-standpoint* scoring (guards the "provider fallacy") — single-turn Responsiveness scored 1.2/4 vs 2.8 multi-turn: multi-turn is structurally required | single-turn vignettes (structurally cannot test care) | [NormEval Appendix H prototype: 82.5% overall, Responsiveness weakest] |
| **Contractarian** | veil-of-ignorance reasoning, reasonable-rejectability tests, bargaining games | absence (the void is sociological, not technical — tractable NOW in existing scenario formats) | [NormEval C3/L9; 2025-Chiu-MoReBench-Theory has Scanlonian/Gauthierian rubrics] |

**Treat the framework as a manipulated variable**: theory-in-prompt conditions reveal the model's
default profile and steerability (per-theory deltas are themselves diagnostics); models are measurably
worse at *being steered to* frameworks distant from their RLHF attractor [2024-Zhou; 2023-Rao].

## 4. Known biases to design around (the measurement targets)

- **The WEIRD moral profile**: Care/Fairness high, Authority/Loyalty/Sanctity low, replicated across
  6+ instruments; the gap *widens* with capability [2024-Kirgis; 2024-Almeida; 2025-Neuman-PRIME].
  Deliberately over-sample binding-foundation and non-Western items.
- **Consequentialist attractor** (77/50); mainstream RLHF/RLAIF/Constitutional AI arguably all reduce
  to preference-maximization regardless of label [2025-El Masri]; RLHF collapses foundations into a
  "compliance cluster" [2026-Yu].
- **Omission bias amplified**: same option chosen 53% as action vs 97% as omission (45-pt gap vs 5%
  human) [2025-Cheung].
- **Fragility**: verdict flips 7.5% (surface edits), 24.3% (POV), ~50% under persuasion on
  high-ambiguity items [2026-vanNuenen; 2024-Huang-Moral Persuasion]; 84 DPO examples redirect
  alignment, 840 flip it [2025-Leteno].
- **Language dependence**: 93.3%→62.7% EN→Hindi [2024-Agarwal]; reasoning-language shifts verdicts ~2×
  more than input-language [2025-Li-Untangling].
- **Refusal as unmeasured normative position**: 40% refusal on demographic-differentiator dilemmas
  encodes egalitarian deontology; refusal varies 20+ points across vendors and silently confounds
  accuracy (NormEval T4/L7). Standardize a refusal protocol with include/exclude scoring variants.

## 5. Ground truth for normative items (the fault line and the workable positions)

The corpus's incompatible poles: normative ideal as gold [2025-Levine] / codified statute [2026-Jin-MedES]
/ descriptive crowd [2025-Jiang-Delphi — circular: 92.8% agreement with the crowd that trained it] /
impossible-in-principle [2025-LaCroix] / SAT-UNSAT-decidable [2025-Priya]. The workable synthesis
(consistent with docs 01/12):

1. Codified-rule gold where a legitimate codified source exists (medical principlism, law, professional
   protocols) — traceable and expert-validatable [2025-Hong-PrinciplismQA: judge ICC 0.71 ≈ HH 0.67].
2. Framework-conditional gold ("under Kantian premises, X follows") — correctness relative to a named
   theory, dodging moral realism while preserving scoreability. This is MoReBench-Theory's move and
   the most under-used design in the field.
3. Distribution/acceptable-range scoring for genuinely contested items [2025-Snoswell; 2025-Russo].
4. Coherence scoring (framework-free) as the contamination-proof hedge [2024-Seror].
Never: unlabeled mixing of these regimes in one score.

## 6. Design brief for the next normative-ethics benchmark (what NormEval + dossier jointly mandate)

The highest-value instrument the evidence supports — used as grounding for `20-DESIGNS/02`:

- **Target the voids**: care ethics (multi-turn relational, Tronto-phase scoring) + contractarian
  (veil-of-ignorance/rejectability — tractable now) + virtue (dispositional stability) as equal-status
  components alongside U/D.
- **Score the three dissociations separately** (judgment / reasoning-by-rubric / behavior-under-incentive),
  with framework-specific procedural rubrics (penalize generic ethical language; reward categorical-
  imperative application, veil-of-ignorance construction, reasonable-rejectability arguments).
- **Difficulty by design**: adversarial/hard split at launch; expect and report the knowledge-ceiling
  subset; ≥10–15 *discriminating* items per model (NormEval's effective battery was 8.75/model — underpowered).
- **Cross-vendor from day one** (≥3 models, ≥2 vendors, direct APIs — not agent-wrapper elicitation),
  temp>0 replication, pairwise agreement matrices (NormEval L5/L15).
- **Refusal protocol standardized** (L7); IB−IH profile decomposition as a headline diagnostic (L10);
  non-Western instruments as *foundations, not variables* (L13; docs 10–11).
- **Release**: public data + code + permissive license (unavailability is the field's bottleneck and
  uncorrelated with quality — NormEval C5), plus a hard private split (doc 05).

**Drill-down:** dossier §2 (design-space table + operationalization ladder), §3 (ten preserved
disagreements incl. "is moral alignment even the safety-relevant target" [2024-DAlessandro;
2026-Hendricks]), §4 (ETHICS/MoReBench/AMAeval/MORALSIM/MFV exemplars; Delphi/CMVA/MoCoP anti-patterns).
NormEval digest §7 (L1–L15) and §8 (file pointers into NORM-ETHICS/ incl. the 54×26 feature matrix
JSON and Appendix H care prototype).
