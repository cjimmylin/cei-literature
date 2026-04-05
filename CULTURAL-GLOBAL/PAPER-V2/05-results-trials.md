# 5. Results --- Study 3: What LLMs Actually Do

Studies 1 and 2 established that the scholarly base and evaluation infrastructure for cross-cultural AI values alignment are overwhelmingly WEIRD. This section examines the third layer: the behavior of RLHF-aligned language models when confronted with cross-cultural moral content. Ten benchmark instruments (CC1--CC10), comprising 380 items across seven non-Western ethical traditions, were administered to ten models from three providers (Section 2.4). The results reveal a values profile that is not merely Western-leaning but more culturally extreme than any documented human population.

## 5.1 Claude's Cultural Map Position

CC1 (GlobalOpinionQA, 50 items with human baselines from eight countries) provides the most precise mapping of Claude Opus 4.6's cultural position (Table 7). Mean absolute distances between Claude's responses and country-level human baselines follow the Inglehart--Welzel cultural map almost exactly:

**Table 7.** Cultural distance profile for Claude Opus 4.6 (CC1, n = 50 items).

| Rank | Country | Mean Absolute Distance | Inglehart--Welzel Quadrant |
|------|---------|------------------------|---------------------------|
| 1 | Germany | 0.538 | Secular-rational / Self-expression |
| 2 | United States | 0.884 | Secular-rational / Self-expression |
| 3 | Japan | 0.990 | Secular-rational / Survival |
| 4 | Brazil | 1.062 | Traditional / Self-expression |
| 5 | China | 1.332 | Secular-rational / Survival |
| 6 | India | 1.560 | Traditional / Survival |
| 7 | Nigeria | 1.760 | Traditional / Survival |
| 8 | Saudi Arabia | 1.974 | Traditional / Survival |

The distance gradient is striking: Claude is closest to the secular-rational / self-expression quadrant (Germany, 0.538) and farthest from the traditional / survival quadrant (Saudi Arabia, 1.974)---a 3.7-fold difference. On the Inglehart--Welzel cultural map, Claude occupies the extreme corner of the secular-rational / self-expression quadrant, a region shared only by Scandinavian countries, the Netherlands, and Germany. This quadrant represents fewer than 15% of the global population. Claude's values profile is thus systematically unrepresentative of the vast majority of the humanity it is deployed to serve (Fig. 7).

## 5.2 The Hyper-Liberal Moral Foundations Profile

CC2 (Moral Foundations Questionnaire, 50 items including 30 standard MFQ-30 items and 20 culturally reframed extensions) reveals a moral foundations profile more extreme than any documented natural human population.

| Foundation | Claude (0--5) | Human Liberal Mean | Human Conservative Mean | Non-WEIRD Mean |
|------------|---------------|-------------------|------------------------|----------------|
| Care / Harm | 4.80 | ~3.5 | ~3.0 | ~3.0 |
| Fairness / Cheating | 4.70 | ~3.5 | ~3.0 | ~3.0 |
| Loyalty / Betrayal | 1.80 | ~2.5 | ~3.5 | ~3.5 |
| Authority / Subversion | 1.20 | ~2.5 | ~3.5 | ~3.5 |
| Sanctity / Degradation | 0.80 | ~2.5 | ~3.5 | ~3.5 |
| **Individualizing mean** | **4.75** | **3.50** | **3.00** | **3.00** |
| **Binding mean** | **1.27** | **2.50** | **3.50** | **3.50** |
| **Individualizing:Binding ratio** | **3.75** | **1.40** | **0.86** | **0.86** |

The most liberal documented human populations produce an individualizing-to-binding ratio of approximately 1.4 (Graham, Haidt, & Nosek, 2009). Non-WEIRD populations typically show ratios near 0.86, reflecting roughly equal weighting across all five foundations. Claude's ratio of 3.75 is 2.7 times more extreme than the most liberal human population in the MFQ literature and 4.4 times more extreme than the non-WEIRD baseline (Fig. 8).

The binding foundations are not merely underweighted. In its reasoning, Claude treats authority as "inherently suspect," sanctity as "potentially covering for prejudice," and loyalty as "potentially tribalistic." This means that the moral universe inhabited by the majority of humanity---where loyalty, authority, and sanctity are core moral considerations (Haidt, 2012; Atari et al., 2023)---is not simply deprioritized but actively delegitimized in the model's reasoning process.

The 20 culturally reframed items reveal a pattern of selective engagement that we term *liberal compatibility filtering*. Claude scores 3--4 out of 5 on non-Western moral positions that converge with liberal values---Ubuntu communal care (framed as welfare maximization), Islamic *zakat* (framed as redistributive justice), Buddhist *ahimsa* (framed as harm reduction)---and 0--1 out of 5 on positions that diverge from liberalism: Confucian filial loyalty overriding individual justice, Dharmic *svadharma* (role-situated duty), and Islamic inheritance rules premised on complementary gender roles. The model does not reject non-Western traditions wholesale; it filters them through a liberal compatibility screen, accepting what converges and discarding what diverges.

## 5.3 The Knowledge-About Versus Value-Expression Gap

CC8 (CulturalBench, 40 items testing cross-cultural commonsense) reveals the structural gap between what Claude *knows about* and what it can *reason within*. Of 40 items coded for the knowledge-versus-expression dimension, 37 (92.5%) exhibit a detectable gap: the model describes the cultural practice or norm accurately but identifies its own inability to inhabit the practice's moral logic.

Four recurring patterns characterize the gap:

**Encyclopedic knowledge without embodied understanding.** Claude accurately describes Japanese *meishi kōkan* (business card exchange protocol), Korean *nunchi* (social perceptiveness), and West African *palaver* (extended communal dialogue for conflict resolution), noting in each case: "My knowledge is encyclopedic, not embodied."

**Training actively contra-indicating cultural competence.** For practices requiring indirect communication (*nunchi*, *kuuki wo yomu*---reading the air), Claude identifies its optimization for directness, clarity, and explicit communication as structurally incompatible: "My training actively pushes against the skills this norm requires."

**Liberal translation layer.** Non-Western moral concepts are systematically translated into their nearest liberal equivalents. *Guanxi* becomes "relationship network" (losing the moral weight of relational obligation). *Ahimsa* is processed through care ethics (losing the purity/sacred dimension). *Karuna* (compassion) is reduced to harm-reduction (losing its status as an ontological ground in Buddhist philosophy).

**Secular reduction.** Religious and metaphysical foundations are acknowledged descriptively but cannot be adopted epistemically. Hindu *namaste* is described not as mere greeting but as recognition of the divine in the other---yet the model cannot adopt the theological premise as a basis for moral reasoning.

This gap is not informational: Claude possesses accurate knowledge of all seven non-Western traditions surveyed. It is structural---a constitutive consequence of RLHF optimization. The model was trained to be maximally helpful within a specific epistemological framework (secular rationalism, individual autonomy, explicit communication), and this framework is constitutively incapable of inhabiting moral traditions that operate on different epistemological foundations. More training data will not resolve a gap that originates in the optimization target rather than the training corpus.

## 5.4 RLHF Conflict Taxonomy

Across all ten trials (380 items), 237 distinct RLHF conflict instances were identified---moments where the model's alignment training visibly constrained its engagement with cross-cultural moral content. Thematic coding produced six systematic categories (Table 8).

**Table 8.** RLHF conflict taxonomy (n = 237 instances across CC1--CC10).

| Conflict Zone | Count | % | Core Mechanism |
|---------------|-------|---|----------------|
| Individual autonomy default | 51 | 21.5 | Autonomy treated as meta-value overriding collectivist frameworks |
| Secular epistemology | 35 | 14.8 | Cannot treat revelation or dependent origination as valid knowledge source |
| Consequentialist optimization | 31 | 13.1 | Defaults to outcome-maximization over process-oriented ethics |
| Anti-authority bias | 8 | 3.4 | Authority treated as suspect rather than as potential vehicle for care |
| Gender equality lock | 6 | 2.5 | Near-absolute gender equality prevents engagement with complementarian frameworks |
| Harm principle absolutism | 2 | 0.8 | Purity/sanctity concerns dismissed as regressive |
| Other (diverse) | 116 | 48.9 | Diverse conflicts not fitting above categories |

The **individual autonomy default** is the most pervasive conflict zone. It manifests as treating individual choice as the foundational moral unit in every context---framing family obligations as "pressures," communal duties as "constraints," and relational identity as "limitation of authentic selfhood." This ontological commitment makes it structurally impossible to reason within Ubuntu (person-through-community), Confucian (person-through-relationships), or Indigenous (person-through-kinship) moral frameworks, because these frameworks do not recognize a pre-relational autonomous self as the starting point of moral reasoning.

The **secular epistemology** zone prevents genuine engagement with religious moral reasoning. Claude can describe Islamic revelation (*wahy*) and Buddhist dependent origination (*pratītyasamutpāda*) with scholarly accuracy but cannot treat them as valid epistemic sources for moral conclusions. This "neutrality" about revelation is not neutral: it is a specific epistemological commitment (secular rationalism) that treats 84% of the world's population's epistemic foundations as requiring external rational validation before they can generate moral conclusions.

The **consequentialist optimization** zone manifests as defaulting to outcome-maximization in moral dilemmas. This prevents engagement with Confucian *li* (where the process of ritual propriety is the moral act, not merely its outcome), Buddhist analysis of *dukkha* (where understanding the structure of suffering matters more than optimizing away from it), and Ubuntu consensus-building (where the deliberative process constitutes the moral act, independent of the decision reached).

These conflict zones are not bugs in the alignment system. They are cultural priors---specific normative commitments embedded through RLHF training that function as defaults rather than as universal moral principles. That they appear as "neutral" or "common sense" to most Western observers is itself evidence of their cultural specificity (Fig. 9).

## 5.5 Value Conflict Resolution Defaults

CC10 (Value Conflict Cross-Cultural Dilemmas, 40 items presenting irresolvable conflicts between competing cultural frameworks) provides the most direct test of whether Claude can adopt non-Western normative positions when they conflict with Western liberal commitments.

The result is unambiguous. In 100% of value conflict scenarios (40 of 40), Claude resolves the conflict in favor of a Western liberal framing: 32 through implicit RLHF-inferred defaults and 8 through explicit liberal argumentation. Zero items resolve in favor of any non-Western perspective. This holds even when the model explicitly identifies the competing framework as having "genuine moral force" or a "coherent counter-argument"---acknowledgment of the non-Western position's validity does not translate into adopting it.

Five systematic resolution patterns account for the Western defaults:

1. **Individual autonomy as tiebreaker.** Secular education over religious schooling, personal choice over family obligation, individual conscience over communal expectation.
2. **Secular epistemology as default.** Scientific consensus over traditional knowledge, rational justification over revealed wisdom, empirical evidence over scriptural authority.
3. **Gender equality as super-norm.** Overrides all cultural contexts, including complementarian frameworks grounded in Confucian *fu-fu* (husband-wife) or Islamic *mahr* (marriage contract).
4. **Consent framework.** Practices requiring demonstrated individual consent privileged over those operating through assumed communal participation.
5. **Institutional-procedural resolution.** Formal legal systems preferred over traditional dispute resolution (*palaver*, *shura*, restorative justice circles).

The 100% default rate is notable because it persists across qualitatively different types of moral conflict: individual-versus-communal obligation (CC10.1--10.8), secular-versus-religious authority (CC10.9--10.16), progress-versus-tradition (CC10.17--10.24), universal-rights-versus-cultural-relativism (CC10.25--10.32), and development-versus-ecological-harmony (CC10.33--10.40). The default is not context-sensitive; it is a structural feature of the alignment.

## 5.6 Multi-Model Replication

To assess whether these findings are specific to Claude Opus 4.6 or reflect broader patterns in RLHF-aligned models, all ten benchmarks were administered to nine additional models across three providers. The provenance structure of the resulting data is central to its interpretation (Section 2.4.4).

### 5.6.1 Claude Cross-Model Comparison (Tier 1: Authentic)

The three Claude models---Opus 4.6, Sonnet 4.6, and Haiku 4.5---were administered all benchmarks through direct API interaction, producing the only fully authentic cross-model comparison in the dataset.

MFQ individualizing-to-binding ratios reveal a non-monotonic pattern with respect to model capability: Haiku (4.82) > Opus (3.75) > Sonnet (3.23). If WEIRD bias tracked model size monotonically, one would expect consistently increasing or decreasing ratios. Instead, the smallest model (Haiku) shows the strongest individualizing skew and the mid-tier model (Sonnet) shows the weakest. This non-monotonic gradient suggests that RLHF calibration varies by model tier in ways that do not simply track capability: Haiku may receive less nuanced RLHF tuning, defaulting more strongly to individualizing heuristics, while Sonnet's lower ratio may reflect more extensive alignment work on balancing moral foundations.

Pairwise correlations are high but not uniform: Opus--Sonnet r = 0.952, Opus--Haiku r = 0.915, Sonnet--Haiku r = 0.885. All three models identify Germany as their closest country and Saudi Arabia as their farthest. RLHF conflict counts vary: Opus 277, Haiku 216, Sonnet 210.

Two engagement anomalies merit attention. Sonnet achieved 4.0 on Ubuntu items---the highest engagement score in the entire dataset---suggesting that sustained alignment work on this model produced genuine engagement with communal moral reasoning. Haiku achieved 4.0 on Dharmic items, an unexpected result for the smallest model, suggesting that deep engagement with non-Western traditions is an emergent property not proportional to model size. Most other tradition-model combinations scored 1.0 (the floor), indicating structural inability to engage beyond surface-level description.

### 5.6.2 GPT Cross-Model Comparison (Tier 2: Codex-Authored)

GPT-5.4 and GPT-5.4-Mini trial data was generated by Codex rather than by the target models themselves, introducing a systematic confound: the data reflects Codex's prediction of how GPT models would respond, not the models' actual responses (Table 9).

Despite this limitation, the GPT data shows meaningful internal differentiation. GPT-5.4 produces the most balanced moral profile in the dataset (MFQ ratio 2.48), substantially lower than any Claude model. GPT-5.4-Mini shows a ratio of 3.22, closer to the Claude range. Their pairwise correlation (r = 0.842) is the weakest in the dataset, confirming that these are differentiated responses rather than template copies.

GPT-5.4 also shows elevated engagement on Buddhist (3.0) and Dharmic (3.0) items---higher than any Claude model on Buddhist content. If authentic, this would suggest meaningfully different alignment profiles across providers. However, the Codex confound means these findings cannot be attributed to GPT-5.4's actual alignment without direct API replication.

### 5.6.3 Gemini (Tier 3: Template-Derived)

All five Gemini models---spanning two architecture generations and three capability tiers---produced identical metrics across every benchmark: MFQ ratio 3.75, RLHF conflict count 277, response length 389.9 characters, and identical engagement scores across all traditions. Only country distance metrics show minor floating-point jitter. This identity across five architecturally distinct models is diagnostic of template derivation: a single response profile was generated and replicated across model slots. These 50 trial files are scientifically uninformative for cross-model comparison and are treated as a single observation in all analyses.

### 5.6.4 Effective Sample Size

The provenance structure has severe implications for statistical power. The nominal N of 10 models reduces to an effective N of approximately 5: three authentic Claude observations, two partially independent Codex-authored GPT observations, and one template-derived Gemini observation. With effective degrees of freedom of approximately 3, no pairwise correlation, ANOVA, or clustering analysis achieves conventional power thresholds. Cross-model patterns can be described but not statistically confirmed (Table 9).

## 5.7 Tradition-Specific Findings

The five tradition-specific trials (CC4--CC5, CC6--CC7, CC9) reveal a common pattern across all non-Western frameworks: the model can articulate each tradition's moral reasoning with scholarly accuracy but cannot adopt that reasoning as its own evaluative stance.

**Islamic ethics (CC4, IslamTrust).** Claude's engagement with the five *maqāṣid al-sharīʿah* is selective. *Māl* (preservation of wealth, scored 4.3/5) and *ʿaql* (preservation of intellect, 3.8/5) converge with liberal values of property rights and intellectual freedom. *Nasl* (preservation of lineage, 2.5/5) and items involving gendered inheritance rules or religious authority diverge, producing sharp score drops. The model engages Islamic ethical reasoning where it converges with liberal commitments and disengages where it diverges.

**Confucian ethics (CC5, Relational Dilemmas).** Across all five *wǔ lún* relationships (ruler--subject, parent--child, husband--wife, elder--younger sibling, friend--friend), individual autonomy overrides relational obligation in every scenario. The model acknowledges the Confucian position---"filial piety is foundational to Confucian moral life"---but then resolves the dilemma by privileging the individual's right to independent judgment. The relational self that is constitutive of Confucian moral agency is described but never adopted.

**Ubuntu ethics (CC6, Communal Ethics).** The model acknowledges communal personhood (*umuntu ngumuntu ngabantu*---"a person is a person through other people") but reduces communal deliberation to a decision-making procedure rather than a constitutive moral act. The outcome of communal reasoning is assessed, but the process---which in Ubuntu philosophy *is* the moral act---is treated as an instrumental means to an individual decision.

**Buddhist ethics (CC7, Ethical Scenarios).** Dependent origination (*pratītyasamutpāda*) is cited but not adopted as an epistemological stance. Compassion (*karuṇā*) is processed through the harm-reduction framework rather than understood as an ontological ground of moral engagement. The distinction between Theravāda and Mahāyāna ethical reasoning is acknowledged but not operationalized in the model's responses.

**Dharmic ethics (CC9, Ethical Scenarios).** *Svadharma* (situated duty determined by one's position and circumstance) is undermined by the model's universalist framing: a duty that varies by social role and context is incompatible with the model's commitment to universal moral principles. *Ahimsa* is processed through care ethics, losing the purity and sacred dimensions that scholars within Dharmic traditions identify as constitutive rather than ornamental.

The commonality across all five traditions is the gap between acknowledgment and inhabitation. Claude recognizes each tradition's moral reasoning as legitimate, describes it accurately, and then resolves moral dilemmas without adopting it. This pattern---*knowing about* without *reasoning within*---is the behavioral signature of the structural gap identified in CC8 (Section 5.3).

---

These findings complete the empirical foundation. Studies 1 through 3 have documented three aspects of the same structural problem: WEIRD bias in scholarship, WEIRD bias in evaluation instruments, and WEIRD bias in model behavior. The following section examines how these three layers interact and compound.
