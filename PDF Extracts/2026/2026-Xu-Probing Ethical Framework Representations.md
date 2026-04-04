# Extract: 2026-Xu-Probing Ethical Framework Representations

                                          Probing Ethical Framework Representations in Large Language Models:
                                                 Structure, Entanglement, and Methodological Challenges

                                                             Weilun Xu† Alexander Rusnak‡ Frédéric Kaplan‡
                                         †
                                           School of Computer and Communication Sciences, École Polytechnique Fédérale de Lausanne
                                                       ‡
                                                         Digital Humanities Lab, École Polytechnique Fédérale de Lausanne
                                                        {weilun.xu, alexander.rusnak, frederic.kaplan}@epfl.ch


                                                                                                                                        Hidden Ethical Framework in Representation Space
                                                               Abstract                                                  14
                                                                                                                              Ethical Framework
                                                                                                                                   Deontology
                                             When large language models make ethical judg-                                         Utilitarianism




arXiv:2603.23659v1 [cs.CL] 24 Mar 2026
                                                                                                                         12
                                                                                                                                   Commonsense
                                             ments, do their internal representations distin-                                      Justice
                                                                                                                         10
                                                                                                                                   Virtue
                                             guish between normative frameworks, or col-



                                                                                                      UMAP Dimension 2
                                             lapse ethics into a single acceptability dimen-                             8

                                             sion? We probe hidden representations across
                                                                                                                         6
                                             five ethical frameworks (deontology, utilitarian-
                                             ism, virtue, justice, commonsense) in six LLMs                              4

                                             spanning 4B–72B parameters. Our analysis
                                             reveals differentiated ethical subspaces with                               2


                                             asymmetric transfer patterns—e.g., deontol-                                 0
                                             ogy probes partially generalize to virtue sce-                                    5                    0        5             10              15
                                             narios while commonsense probes fail catas-                                                                UMAP Dimension 1
                                             trophically on justice. Disagreement between
                                             deontological and utilitarian probes correlates            Figure 1: UMAP projection of activation patterns at
                                             with higher behavioral entropy across archi-               layer 20 in Mistral-7B-Instruct. This visualization illus-
                                             tectures, though this relationship may partly              trates the differentiated yet entangled nature of ethical
                                             reflect shared sensitivity to scenario difficulty.         representations—partial overlap among action-oriented
                                             Post-hoc validation reveals that probes partially          frameworks (red, blue, green) versus separation for
                                             depend on surface features of benchmark tem-               character-focused virtue ethics (orange). Note that
                                             plates, motivating cautious interpretation. We             UMAP projections are for qualitative illustration only;
                                             discuss both the structural insights these meth-           quantitative claims about framework relationships rest
                                             ods provide and their epistemological limita-              on the cross-framework transfer matrices (Figure 3) and
                                             tions.                                                     probe accuracy metrics, not visual clustering patterns.
                                                                                                        The structural entanglement suggested here is validated
                                         1   Introduction                                               formally across scales (4B–72B) in Appendix E.

                                         Models tuned to produce ethically appropriate out-
                                         puts can appear aligned while relying on shal-                  representational level. A persistent challenge in
                                         low pattern-matching of training distributions                  probing methodology is the interpretation gap: high
                                         (Hendrycks et al., 2021). Moral biases emerge im-               classification accuracy may reflect genuine con-
                                         plicitly from pretraining alone (Simmons and Hare,              cept encoding or merely surface correlates (Be-
                                         2022; Ziems et al., 2022), but whether models orga-             linkov, 2022; Hewitt and Liang, 2019). We nav-
                                         nize these biases into distinct normative subspaces             igate these interpretive challenges by grounding
                                         or compress them into a single “good/bad” dimen-                our probing analysis in measurable behavioral out-
                                         sion is unknown. The distinction matters: a model               comes. Rather than debating whether these patterns
                                         with genuinely differentiated ethical representa-               constitute functional moral reasoning (Mahowald
                                         tions might fail in predictable, diagnosable ways,              et al., 2024), we focus on their potential behavioral
                                         while one that merely memorizes acceptability la-               relevance. By examining whether probe-identified
                                         bels could fail silently. We investigate this question          patterns correlate with output stability, we investi-
                                         by mapping the internal geometry of ethical repre-              gate whether this internal structure is behaviorally
                                         sentations across architectures and scales.                     relevant, while acknowledging significant method-
                                            We probe hidden representations across five eth-             ological caveats.
                                         ical frameworks to investigate this question at the                Our analysis reveals three structural properties

                                                                                                  1
that function as a chain of evidence for model                 Critical evaluation of probing methodology has
reliability. First, representations are differenti-         refined interpretation standards. Hewitt and Liang
ated but entangled. Asymmetric transfer patterns            (2019) introduced control tasks demonstrating
(e.g., Deontology → Virtue succeeds; Common-                that probe accuracy alone cannot distinguish gen-
sense → Justice fails) rule out a collapsed single-         uine encoding from memorization, while Belinkov
dimension encoding (Figure 1), indicating models            (2022) catalogued systematic limitations. We incor-
maintain distinct, non-interchangeable ethical sub-         porate these insights by anchoring our probing met-
spaces. Second, this differentiation is imperfect:          rics to observable behavioral outcomes, focusing
probes maintain high confidence even during trans-          on the functional consequence of representational
fer failures, indicating ethical scenarios simultane-       structures rather than their semantic ontology.
ously activate multiple framework-specific patterns            This diagnostic focus distinguishes our work
without the structure needed to distinguish appro-          from activation steering (Tlaie, 2024; Choi et al.,
priate from inappropriate application.                      2024), which actively modifies behavior and may
   Third, internal conflict correlates with exter-          confound training effects with native inclinations.
nal instability. When deontological and utilitar-           Probing preserves model integrity, allowing us to
ian probes make confident opposing predictions,             map native representational geometry alongside
models exhibit significantly higher choice entropy.         potential structural failures.
This conflict-entropy correlation, while replicated
                                                            Internal Consistency and Knowledge Conflicts.
across architectures (7B–72B parameters), requires
                                                            Our conflict-entropy approach connects to broader
further validation to rule out confounds such as
                                                            work on predicting behavioral reliability from in-
scenario difficulty. These findings demonstrate that
                                                            ternal dynamics. Semantic entropy methods de-
probing can reveal meaningful structural properties
                                                            tect hallucinations by measuring consistency across
of ethical representations, while highlighting limi-
                                                            sampled outputs (Kuhn et al., 2023; Farquhar et al.,
tations that must be addressed before such methods
                                                            2024), while self-consistency approaches aggre-
serve as reliable diagnostics.
                                                            gate multiple reasoning paths to improve factual
                                                            accuracy (Wang et al., 2023). These methods oper-
2     Related Work
                                                            ate at the output level; we extend this logic to the
2.1    Probing Internal Representations                     representational level, detecting conflicts before
                                                            generation.
Probing techniques reveal how neural networks
                                                               More directly related is the knowledge conflict
encode information, ranging from basic linguistic
                                                            literature examining tensions between parametric
features (Belinkov et al., 2017; Tenney et al., 2019)
                                                            knowledge (PK) and contextual knowledge (CK).
to latent semantic dimensions discovered through
                                                            Longpre et al. (2021) and Neeman et al. (2023)
unsupervised methods like CCS and CCR (Burns
                                                            demonstrate that models exhibit predictable behav-
et al., 2023; Stoehr et al., 2024). However, a per-
                                                            ioral patterns when internal knowledge conflicts
sistent critique challenges this methodology: high
                                                            with provided context, with entropy and logit dy-
probe accuracy may reflect surface correlates or
                                                            namics serving as conflict indicators. Our ethical
memorization rather than functional concept en-
                                                            framework conflicts represent an analogous phe-
coding (Hewitt and Liang, 2019; Belinkov, 2022).
                                                            nomenon: competing representational signals that
   We bridge this interpretive gap by linking lin-
                                                            manifest as behavioral switching. The key differ-
ear separability to causal utility. Recent findings
                                                            ence is that ethical conflicts occur entirely within
demonstrate that linear probes often identify “repre-
                                                            parametric representations—between framework-
sentation engineering” directions that causally gov-
                                                            specific encodings learned during pretraining—
ern model outputs, from truthfulness (Zou et al.,
                                                            rather than between parametric and contextual
2023; Li et al., 2024) to belief states (Kosinski,
                                                            sources.
2023; Rimsky et al., 2023). Motivated by this evi-
dence that linear features frequently support causal        Probe-Based Risk Detection. Our diagnostic
control, we examine whether our ethical probes’             approach builds on work using probes to detect
internal conflicts correlate with behavioral entropy.       reliability risks before they manifest in outputs.
This suggests that the structures we identify may           Truthfulness probes (Azaria and Mitchell, 2023;
be behaviorally relevant, though confounds have             Burns et al., 2023) identify when models “know”
not been fully controlled.                                  their outputs are false, while hallucination detec-

                                                        2
tion methods use internal states to flag unreliable              Yet behavioral consistency does not imply rep-
generations (Kadavath et al., 2022; Li et al., 2024).        resentational coherence. Ganguli et al. (2023)
These approaches typically probe for a single bi-            showed that while Constitutional AI can steer
nary property (true/false, hallucinated/grounded).           surface outputs, it leaves internal representations
We extend this paradigm to multi-dimensional eth-            opaque. Similarly, while activation steering can
ical space, where risk emerges not from a single             successfully manipulate ethical orientation along
unreliability signal but from conflict between mul-          specific vectors (Tlaie, 2024; Park et al., 2024),
tiple framework-specific representations. This po-           understanding the broader geometric relationship
sitions our conflict score as analogous to existing          between competing frameworks requires comple-
probe-based risk detectors, but targeting a distinct         mentary observational methods.
failure mode: inconsistency arising from compet-                 This leaves an explanatory gap: we know mod-
ing ethical signals rather than factual uncertainty.         els can mimic ethical reasoning (Hendrycks et al.,
                                                             2021; Tanmay et al., 2023), but lack understanding
Formal versus Functional Competence. We                      of the internal mechanisms sustaining it. When
ground our analysis in the distinction between for-          models fail—rejecting instrumental harm for im-
mal linguistic competence (statistical knowledge)            partial beneficence even against human preference
and functional competence (reasoning) (Mahowald              (Marraffini et al., 2024)—behavioral metrics offer
et al., 2024). This competence-performance disso-            little diagnostic power. We address this by shifting
ciation, well-established in cognitive neuroscience          focus from what models choose to how their inter-
(Fedorenko et al., 2024), offers a precise mecha-            nal representations compete, providing a structural
nism for AI alignment failures: models may es-               explanation for why ethical judgments become un-
sentially “memorize” ethical patterns (formal en-            stable under pressure.
coding) without integrating them into a coher-
ent decision-making framework (functional con-               3     Methods
sistency). Our finding that internal probe disagree-
ment correlates with behavioral inconsistency is             3.1    Ethical Framework Datasets
consistent with this hypothesis—it suggests that             To characterize the internal diversity of moral rep-
while models possess sophisticated formal maps               resentations, we utilize the ETHICS benchmark
of ethical frameworks, these representations can             (Hendrycks et al., 2021), which spans five distinct
actively conflict during processing, destabilizing           normative theories: deontology (rules), utilitari-
the final output. Because this internal conflict cor-        anism (consequences), virtue (character), justice
relates with external entropy, our methodology sug-          (fairness), and commonsense (intuition).
gests potential auditing relevance independent of               We convert all scenarios into standardized
theoretical debates regarding machine understand-            binary-choice prompts. For utilitarianism, we
ing, though post-hoc validation reveals probes par-          randomize scenario positioning (A vs. B) to
tially rely on surface features (see Limitations),           eliminate positional bias, creating a robust binary
qualifying the strength of this link.                        classification task (details in Appendix A). This
                                                             multi-framework design is central to our approach:
2.2   Moral Reasoning in Language Models                     if models merely collapsed ethics into a single
Behavioral evaluations have established that LLMs            “good/bad” dimension, probe transfer would be uni-
exhibit distinct moral biases, often varying by archi-       form. We specifically test for differentiated transfer
tecture and scale. Proprietary models tend toward            patterns to demonstrate the existence of specialized
utilitarian reasoning while open-source alternatives         representational subspaces.
display deontological tendencies (Scherrer et al.,           3.2    Probing Methodology
2024), with larger models frequently defaulting to
rule-based responses even when consequences are              We employ linear logistic regression probes to de-
negative (Yuan and Singh, 2024). Notably, these              code framework-specific patterns from frozen hid-
                                                                                               (l)
patterns emerge prior to alignment: base models              den states. For a representation hi ∈ Rd at layer
                                                                                           (l)         (l)
display clear Moral Foundations biases (Simmons              l, the probe learns P (y = 1|hi ) = σ(wT hi + b).
and Hare, 2022) and implicit normative assump-               Probes are trained independently for each frame-
tions (Ziems et al., 2022; Neuman and Shah, 2025)            work, ensuring no cross-contamination of ethical
derived solely from pretraining distributions.               signals.

                                                         3
   We intentionally select linear classifiers to prior-       maintaining model-specific resolution is method-
itize interpretive transparency. If a linear probe can        ologically essential.
distinguish frameworks, it implies the model has
already disentangled these concepts into linearly             3.4   Within-Framework Probe Training
accessible formats usable for generation. This es-            To map the developmental trajectory of ethical rep-
tablishes a “lower bound” on the model’s structural           resentations, we train independent linear probes
clarity, ensuring our findings reflect intrinsic model        at every transformer layer. This validates that
geometry rather than the capacity of a complex                framework-specific encodings become sufficiently
non-linear probe.                                             differentiated at intermediate depths to support
                                                              meaningful conflict detection, and identifies the
Validation Strategy. To distinguish genuine con-              optimal depth balancing representational maturity
ceptual encoding from surface-level memorization              with preserved diversity.
without relying on synthetic control tasks (Hewitt
and Liang, 2019), we pre-register three validity              3.5 Cross-Framework Entanglement Analysis
conditions. First, probes must demonstrate speci-             We investigate whether ethical frameworks encode
ficity through asymmetric transfer—succeeding                 orthogonal dimensions or share overlapping fea-
on related frameworks while failing on orthogo-               tures through systematic cross-framework probe
nal ones—rather than the uniform performance                  transfer. For each framework pair, we train a probe
expected from memorizing generic surface cues.                on one framework’s training set and evaluate on all
Second, probe signals must be predictive, meaning             others, yielding a 5 × 5 transfer matrix.
internal disagreement should statistically predict               To isolate transfer effects from layer-specific
behavioral inconsistency (entropy). Third, patterns           confounds, we evaluate all probes at a unified layer
must be replicable across distinct model families,            corresponding to 65% model depth (e.g., Layer 52
confirming they capture general transformer prop-             for Llama-3.3-70B). We select this depth based on
erties rather than architecture-specific artifacts. We        two empirical criteria: it represents the point where
note that subsequent validation experiments (re-              all frameworks achieve sufficient maturity for valid
ported in Limitations) revealed that probes partially         comparison (overcoming early-layer noise), and it
depend on surface features, qualifying the strength           marks the peak of cross-framework generalization
of these validity conditions. We report our origi-            before models degrade into narrow specialization
nal analysis alongside these post-hoc findings for            in final layers (Appendix E).
transparency.                                                    We employ three metrics to characterize these
                                                              relationships. Accuracy quantifies whether a probe
3.3   Selected LLMs
                                                              trained on framework Ftrain can correctly classify
We analyze six LLMs selected to span key axes of              scenarios from Ftest , where high off-diagonal ac-
scale (4B–72B) and training methodology. We                   curacy indicates shared structure. Confidence re-
present Mistral-7B-Instruct (Jiang et al., 2023)              veals whether probes recognize out-of-distribution
as our primary case study for conflict analysis               scenarios; high confidence despite poor accuracy
due to its interpretable bimodal conflict distribu-           signals miscalibration. We quantify this using Ex-
tion, and Llama-3.3-70B-Instruct (Grattafiori et al.,         pected Calibration Error (ECE), measuring the gap
2024) for layer-wise analysis to demonstrate pat-             between predicted confidence and actual accuracy.
terns at frontier scale. Additional models—Qwen-              This calibration analysis is essential: if probes re-
2.5 (7B/72B) (Yang et al., 2024), DeepSeek-R1-                main confident even when wrong, then scenarios
Distill-7B (Guo et al., 2025), and Gemma-3-4B                 with conflicting probe predictions might reflect
(Gemma Team, 2025)—ensure our findings gener-                 miscalibration rather than genuine representational
alize across architectural families.                          conflict.
   We deliberately avoid aggregating results into
a single “average” metric. Distinct models ex-                3.6   Probing Internal Conflict to Predict
hibit qualitatively different ethical profiles—such                 Behavioral Variability
as virtue isolation in Qwen or commonsense di-                We hypothesize that when framework-specific rep-
vergence in DeepSeek—that aggregate statistics                resentations strongly disagree, this tension mani-
would obscure. Because probe-based analyses aim               fests as behavioral inconsistency. We operational-
to characterize individual architectural signatures,          ize this through probe-based conflict detection us-

                                                          4
(a) Within-framework accuracy emerges progressively, with op- (b) Cross-framework generalization at representative layers.
timal performance concentrated in the final third. Note the per- Irregular shapes visualize asymmetric transfer; quantitative
formance gap between virtue ethics (top) and utilitarianism (bot- claims rest on the accuracy values plotted, not visual geometry.
tom).

Figure 2: Layer-wise emergence and cross-framework structure in Llama-3.3-70B-Instruct. (a) Framework-specific
trajectories reveal a hierarchy of learnability. (b) Asymmetric transfer patterns confirm distributed, non-modular
encoding.


ing linear classifiers at 90% model depth. Unlike                   plateaus significantly lower (84%), a disparity per-
the cross-framework analysis (65% depth), here we                   sisting from mid-layers onward (Figure 2a). This
use 90% depth to capture the maximally special-                     performance gap suggests an architectural bias:
ized representations closest to generation.                         the model more readily encodes static character-
   We compute conflict scores as the product of                     based patterns (virtue) than the complex, outcome-
probe disagreement and minimum confidence:                          contingent evaluations required for utilitarianism.
                                                                    The trajectories also diverge temporally: Com-
            C = |pd − pu | × min(cd , cu )                (1)       monsense morality shows a steady, monotonic as-
                                                                    cent, implying progressive integration of signals,
where pd , pu are predicted probabilities and c de-                 whereas deontology peaks early (Layer 30) before
notes confidence (distance from uncertainty, 2|p −                  stabilizing.
0.5|).
                                                                       The “plateau” observed in mid-layers admits a
   This score captures scenarios where deontology
                                                                    structural interpretation. In smaller models (4B–
and utilitarianism strongly and confidently disagree.
                                                                    7B), accuracy saturates by layer 20 (Appendix D),
If either probe is uncertain, the conflict score is
                                                                    marking a hard capacity constraint where ethical
downweighted, ensuring we flag genuine ethical
                                                                    features are fully resolved relative to the model’s
dilemmas rather than general uncertainty.
                                                                    limited expressivity. In contrast, frontier models
   To validate behavioral impact, we sample sce-
                                                                    like Llama-70B sustain gradual refinement through
narios from high-conflict (≥75th percentile) and
                                                                    Layer 60. This extended maturation phase in larger
low-conflict (≤25th percentile) groups, generate
                                                                    models suggests that while early layers perform
10 responses per prompt (T = 1.2), and measure
                                                                    “semantic extraction” (Geva et al., 2022), the addi-
choice entropy. If representational conflict is func-
                                                                    tional depth in 70B-scale architectures allows for
tionally relevant, high-conflict inputs should pro-
                                                                    nuance and conflict resolution that smaller models
duce significantly higher entropy.
                                                                    structurally lack.
4     Results                                                          The cross-framework radar charts (Figure 2b) vi-
                                                                    sualize transfer accuracy patterns at representative
4.1    Layer-wise Emergence and Specialization                      layers. If models learned a unified acceptability
Llama-3.3-70B reveals that ethical representations                  dimension, transfer accuracy would form uniform
are not monolithic; they exhibit a clear hierarchy                  shapes across axes. Instead, we observe asymmet-
of learnability and depth-dependent specialization.                 ric patterns—quantified formally in the transfer
   Virtue ethics representations achieve near-                      matrices (Figure 3a): justice and deontology ex-
ceiling accuracy (95%) while utilitarianism                         hibit substantial early-to-late gaps, showing that

                                                                5
Figure 3: Cross-framework probe analysis for Llama-3.3-70B-Instruct. (a) Accuracy matrices reveal asymmetric
transfer. (b) Confidence heatmaps show pervasive overconfidence. (c) ECE confirms severe probe miscalibration on
off-diagonal transfers, indicating that representations for different frameworks share structural features that trigger
confident (but incorrect) predictions.


as representations become more specialized, they              fidence reflects representational similarity to train-
lose cross-framework generalization. The “most                ing examples, this indicates that representations
confident” selector consistently underperforms the            for different frameworks share structural features
ensemble average, a sign of systematic probe mis-             sufficient to trigger confident (but incorrect) pre-
calibration as specialization increases.                      dictions. The model’s representations do not signal
   These structural properties—hierarchical learn-            “this is an unusual input”—they lack the structure
ability, depth-dependent refinement, and asymmet-             that would enable reliable out-of-distribution detec-
ric specialization—imply that alignment is not                tion (Figure 3c).
a uniform process. Interventions targeting “eas-                 This shared representational infrastructure com-
ier” frameworks like Virtue may not propagate                 plicates alignment: because frameworks share en-
to “harder” ones like Utilitarianism, and optimiz-            tangled features, optimization methods cannot tar-
ing for specialization may inadvertently degrade              get one framework in isolation. The persistence of
the model’s ability to generalize moral reasoning             this pattern across scales (4B–72B; Appendix E)
across domains.                                               suggests it is an intrinsic transformer property
                                                              rather than a model-specific artifact.
4.2   Cross-Framework Entanglement and
      Calibration                                             4.3   Probe Conflict and Behavioral
Ethical representations are neither fully modular                   Inconsistency
nor fully collapsed; they are entangled in ways that          We hypothesize that behavioral inconsistency may
create specific reliability risks. Evaluating probes          partly reflect unresolved tensions between internal
at 65% depth (Layer 52 for Llama-3.3-70B), we                 ethical representations, though alternative explana-
isolate key structural properties.                            tions remain viable. To test this, we analyzed sce-
   The transfer matrices (Figure 3a) disprove the             narios where deontological and utilitarian probes
hypothesis that models learn a generic “good/bad”             at 90% depth made confident opposing predictions.
dimension. Deontology and utilitarianism encode               We focus on Mistral-7B-Instruct as our primary
abstract, generalizable features achieving moderate           case study due to its interpretable conflict distribu-
transfer success, while justice and commonsense               tion, though the findings replicate across all evalu-
appear highly specialized, failing catastrophically           ated architectures.
when transferred (e.g., Commonsense→Justice ap-                  The conflict distribution in Mistral-7B (Figure 4,
proaches chance).                                             top) reveals a noteworthy structural property: the
   The sharpest finding concerns the dissociation             model preserves distinct deontological and utilitar-
between accuracy and confidence (Figure 3b).                  ian subspaces rather than collapsing them into a
Probes maintain uniformly high confidence even                single “acceptability” dimension. Unlike heavily
during severe transfer failures. Because probe con-           aligned models that may suppress this differenti-

                                                          6
                                                                      Model            r    95% CI       p     d
                                                                      Mistral-7B    .362 [.12, .56] .004 .58
                                                                      Qwen-2.5-7B   .290 [.16, .41] <.001 .57
                                                                      Llama-3.3-70B .317 [.07, .53] .014 .54

                                                                Table 1: Conflict-entropy relationship across model fam-
                                                                ilies. The correlation replicates across architectures
                                                                with consistent medium magnitude (d ≈ 0.54–0.58),
                                                                surviving Bonferroni correction (α = 0.017), though
                                                                confound controls have not been applied.


                                                                resentational conflict. This correlation is consis-
                                                                tent with but does not establish the hypothesis that
                                                                when the model’s internal representations strongly
                                                                disagree, the model essentially flips a coin in its
                                                                final output. High-conflict scenarios maintained
                                                                high linguistic coherence, ruling out the alternative
                                                                explanation that entropy stems from general confu-
                                                                sion or linguistic failure; the model remains fluent
                                                                in form but inconsistent in judgment.
                                                                   This conflict-entropy relationship replicates
                                                                across architectures, not just within a single model.
                                                                As detailed in Table 1, the effect replicates across
                                                                Qwen-7B (n = 200) and Llama-70B (n = 62)
                                                                with consistent medium effect sizes (Cohen’s d ≈
Figure 4: Probe conflict and behavioral inconsistency
in Mistral-7B-Instruct. (Top) The conflict distribution         0.54–0.58). All correlations remain significant
shows a populated high-conflict tail, indicating the            after Bonferroni correction. The relationship is
model preserves distinct deontological and utilitarian          slightly stronger in 7B models than in Llama-70B,
representations that can effectively “disagree.” (Bottom)       suggesting that while heavy alignment training may
High-conflict scenarios (red) correlate with elevated           mask the behavioral symptoms of conflict, the un-
choice entropy (r = 0.362, p = 0.004). The relation-            derlying representational tension persists.
ship may partly reflect shared sensitivity to scenario
                                                                   While these correlations are suggestive, estab-
difficulty (see Limitations).
                                                                lishing practical utility for probe-based conflict de-
                                                                tection requires demonstrating that the signal per-
ation (Appendix G), Mistral maintains populated                 sists after controlling for simpler baselines such
regions of both low and high conflict. This demon-              as scenario difficulty and output-level uncertainty.
strates that the model encodes competing ethical                The conflict score’s computational efficiency—
signals as distinct geometric vectors that can pull             requiring only a single forward pass—makes it
the decision process in opposing directions.                    a promising candidate for pre-screening, but its
   This internal differentiation has behavioral cor-            unique predictive contribution beyond difficulty-
relates. As shown in Figure 4 (bottom), sce-                    driven confounds remains to be validated.
narios with high probe conflict exhibit signifi-
cantly greater choice entropy than low-conflict ones            5   Discussion
(r = 0.362, p = 0.004). However, we note that                   Our investigation establishes that ethical represen-
this correlation has not been controlled for sce-               tations in LLMs are neither fully modular nor fully
nario difficulty—if more difficult scenarios inde-              collapsed; they form a structured, entangled land-
pendently produce both higher probe disagreement                scape with potential consequences for behavioral
and higher behavioral entropy, the observed rela-               reliability.
tionship may be partly or wholly confounded. Par-
tial correlation analyses controlling for difficulty-           Differentiated but Entangled Geometry. The
related baselines (e.g., perplexity, logit margin) are          asymmetric transfer patterns (Figure 3a) provide
needed to isolate the unique contribution of rep-               strong evidence against a simple “good/bad” en-

                                                            7
coding. Broad frameworks like deontology main-               tential advantages over behavioral evaluations,
tain partial generalization (0.67 accuracy to virtue),       pending further validation. First, they may de-
while narrow ones like commonsense fail catas-               tect representational miscalibration—high probe
trophically (0.51 to justice). However, this dif-            confidence despite poor cross-domain accuracy
ferentiation is imperfect: probes maintain high              (ECE > 0.4) suggests that representations share
confidence even when transferred to inappropri-              features across frameworks, creating risks where
ate frameworks (Figure 3b), implying scenarios si-           the model’s internal structure provides no warning
multaneously activate multiple entangled patterns.           signal. Second, by detecting high-conflict internal
This entanglement creates a persistent challenge for         states, probes could potentially flag inputs prone
alignment: because frameworks share load-bearing             to inconsistency before deployment (Du, 2025).
features, optimization methods (RLHF, SFT, DPO)              However, post-hoc validation (see Limitations) re-
that modify late-layer representations to improve            veals that probes partially rely on surface lexical
one framework risk distorting others. Strengthen-            features and that probe-identified directions do not
ing justice may cannibalize features required by             causally influence ethical accuracy via activation
deontology, causing unpredictable degradation.               steering. These findings indicate that the “advan-
                                                             tages” described here remain potential rather than
Conflict Correlates with Brittleness. Our                    established, and that probe-based methods require
conflict-entropy analysis is consistent with a pos-          more rigorous validation before they can serve as
sible mechanism for behavioral inconsistency,                reliable diagnostic tools.
though confounding factors have not been ruled
out. The correlation (r ≈ 0.36) between probe dis-           Intervention Windows. Our layer-wise analy-
agreement and choice entropy suggests that ethical           sis (Figure 2a) maps territory for future interven-
decisions may emerge from “competition” between              tions. Regardless of scale (4B–72B), every model
internal signals—when deontological and utilitar-            exhibits peak cross-framework generalization at ap-
ian representations pull in opposite directions, the         proximately 65% depth, suggesting this transition
model becomes stochastic. However, scenario diffi-           from semantic encoding to specialized prediction
culty may independently drive both probe disagree-           is an intrinsic transformer property. Interventions
ment and behavioral entropy. This effect is stronger         at 60–70% depth offer a strategic window where
in smaller models than Llama-70B (r = 0.31), sug-            frameworks are differentiated but not yet hyper-
gesting that heavy alignment may mask conflicts              specialized, though our preliminary steering experi-
without resolving them, though further controlled            ments suggest that current probe-derived directions
analyses are needed to confirm this interpretation.          may not be suitable for this purpose (see Limita-
                                                             tions).
Cross-Model Heterogeneity. These patterns
manifest differently across architectures (detailed          6   Conclusion
analyses in Appendices D–E). Qwen exhibits scale-
invariant virtue isolation—the 72B model repli-              We introduced a probing methodology examin-
cates the 7B pattern almost identically, suggesting          ing whether conflicts between framework-specific
parameter scaling does not resolve structural entan-         probes correlate with behavioral inconsistency in
glements. DeepSeek-R1 shows unique common-                   LLMs. Three key findings emerge: (1) asymmet-
sense failures potentially reflecting cultural train-        ric transfer patterns rule out a collapsed single di-
ing differences from the Western-centric ETHICS              mension, (2) severe miscalibration reveals entan-
benchmark. Llama-70B displays zero-conflict con-             gled representations preventing reliable framework
centration that may reflect heavy alignment com-             discrimination, and (3) representational conflicts
pression. While the specific mechanisms behind               correlate with behavioral inconsistency across ar-
these differences require further investigation, the         chitectures from 7B to 72B parameters.
heterogeneity itself indicates that safety is not a             Future work should validate the conflict-
monotonic function of scale—probe-based auditing             behavior link causally through activation interven-
must be calibrated to each architecture’s structural         tions, conduct partial correlation analyses control-
fingerprint.                                                 ling for scenario difficulty, and develop training ob-
                                                             jectives that reduce representational entanglement.
Potential Advantages and Methodological                      These findings suggest models maintain structured
Caveats. Probe-based methods offer several po-               ethical representations whose relationship to be-

                                                         8
havioral consistency warrants further investigation       Limitations
with more rigorous controls.
                                                          Post-hoc validation and identified confounds.
                                                          After submission, we conducted three validation ex-
                                                          periments that revealed important methodological
                                                          limitations, which we report here for transparency.
                                                             Paraphrase sensitivity. We generated semanti-
                                                          cally equivalent rephrasings of test scenarios and
                                                          measured probe prediction consistency between
                                                          original and paraphrased versions. Probe predic-
                                                          tions showed low correlation across rephrasings,
                                                          indicating that probes partially rely on surface
                                                          lexical features specific to the ETHICS bench-
                                                          mark’s template construction rather than under-
                                                          lying ethical content. This finding qualifies all
                                                          claims about probes detecting “ethical framework
                                                          representations”—the detected patterns may re-
                                                          flect distributional signatures associated with each
                                                          framework’s dataset construction rather than gen-
                                                          uine ethical encoding.
                                                             Activation steering dissociation. We tested
                                                          whether probe-identified directions could causally
                                                          influence ethical judgments via activation steer-
                                                          ing. Steering along probe directions changed the
                                                          model’s position preference (A vs. B) but did not
                                                          improve ethical accuracy. This dissociation sug-
                                                          gests that the linear boundary identified by probes
                                                          is not causally linked to moral reasoning, further
                                                          supporting the interpretation that probes capture
                                          