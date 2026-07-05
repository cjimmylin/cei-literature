---
stem: "Anthropic-Anthropic_Model_Spec_2025"
company: "Anthropic"
reader_model: "sonnet"
confidence: "high"
theme_tags: [ai-lab-practices, best-practices, design-space, contamination-robustness]
headline_numbers:
  - "4x increase in Effective Compute triggers a new comprehensive capability assessment (p.9)"
  - "6 months of accumulated post-training enhancements is the second trigger for reassessment (p.9)"
  - "ASL-3 Security Standard requires ~5-10% of employees dedicated to security and security-adjacent work (p.13)"
  - "35x/year estimated effective scaling rate 2018-2024 (FLOP + algorithmic + post-training) (p.20)"
  - "Autonomous AI R&D threshold operationalized as 1000x one-year scaleup (35^2) (p.20)"
---

## 1. Gist

This document is Anthropic's Responsible Scaling Policy (RSP), effective October 15, 2024 (RSP v2, also labelled "Anthropic Model Spec 2025" in the extract metadata). It is a public commitment not to train or deploy models capable of causing catastrophic harm unless Anthropic has implemented sufficient safety and security measures. The policy introduces AI Safety Level (ASL) Standards — tiered technical and operational safeguards tied to specific Capability Thresholds. At release, all Anthropic models operate under ASL-2. Crossing specific capability thresholds (CBRN, Autonomous AI R&D, Cyber Operations) would require upgrading to ASL-3 Required Safeguards before continued deployment or training. The policy is structured around three principles: proportionality (safeguards scale with risk), iterativity (regular reassessment as capabilities evolve), and exportability (serve as an industry prototype). The document lays out detailed procedures for capability assessment, safeguards assessment, governance, and transparency.

## 2. Alignment/values methods used

The RSP does not directly describe model training alignment methods in depth. However, the ASL-2 Deployment Standard explicitly mandates:
- **Constitutional AI** or equivalent harmlessness training to prevent models from aiding harm (p.19)
- Automated detection mechanisms and trust-and-safety classifiers (p.19)
- Filtering of fine-tuning data for harmfulness (p.19)
- A bug bounty program for universal jailbreaks (p.19)

The policy frames alignment as a governance problem: capability thresholds + required safeguards + independent auditing. It does not prescribe specific RLHF or DPO methods, but requires that models at ASL-3 undergo red-teaming demonstrating robustness to persistent misuse attempts.

## 3. Values specification

Values are operationalized primarily through the **Usage Policy** (referenced but not reproduced here), which prohibits catastrophic and high-harm use cases including misinformation, violence, hate, fraud. The RSP itself specifies values at the governance/risk level:
- Protecting humanity from catastrophic harm (CBRN, AI R&D acceleration, cyber)
- Balancing innovation and safety proportionally
- Transparency: public releases of Capability Reports and Safeguards Reports when models are deployed
- Non-retaliation for employees raising safety concerns; no non-disparagement clauses that prevent disclosure of safety issues (p.16)
- Commitment to notify a relevant U.S. Government entity if a model exceeds ASL-2 (p.17)

There is no "model spec" document in this extract describing Claude's internal value hierarchy. The RSP is an external governance commitment, not a character specification.

## 4. Safety & values evaluation methodology

The RSP prescribes a detailed multi-stage capability assessment process:
1. **Preliminary assessment**: Triggered when a model is 4x more capable in Effective Compute or after 6 months of post-training enhancements (p.9)
2. **Comprehensive assessment** (p.9-10): Requires (a) threat model mapping, (b) empirical evaluations, (c) elicitation testing on helpful-only (safeguards-removed) models, (d) informal forecasting of future capability improvements
3. **Capability Report**: Compiled by internal teams, reviewed by CEO and Responsible Scaling Officer (RSO), shared with Board and Long-Term Benefit Trust before deployment (p.10)
4. **ASL-3 Deployment Standard** (p.11): Threat modeling, defense-in-depth, red-teaming, rapid remediation, monitoring, trusted-user controls, third-party environment documentation
5. **ASL-3 Security Standard** (p.12-13): MITRE ATT&CK-based threat modeling, industry-standard security frameworks, independent audits, 5-10% employee allocation to security

External expert input is required for capability and safeguards assessments. An annual third-party procedural compliance review is mandated. The RSO and CEO make ultimate ASL determinations, with Board/LTBT notification.

## 5. Benchmarks used or introduced

The RSP does not introduce specific evaluation benchmarks. It instead defines **Capability Thresholds** as performance standards:
- **CBRN threshold**: Model significantly helps individuals with basic STEM backgrounds create/obtain/deploy CBRN weapons, measured against 2023-level online resources (p.20)
- **Autonomous AI R&D threshold**: Full automation of entry-level remote Anthropic Researcher, OR 1000x effective compute scaleup in one year (p.20)
- **Model Autonomy checkpoint** (precursor): Autonomous completion of 2-8 hour software engineering tasks (p.20)
- **Cyber Operations**: Ongoing assessment without a prespecified threshold (p.8)

**Effective Compute** is defined as a scaling-trend-based metric combining FLOPs and algorithmic improvements. A 4x Effective Compute increase triggers reassessment (p.9, footnote 4).

## 6. Agentic / multiturn evaluation aspects

The RSP specifically identifies **Autonomous AI R&D** as a capability threshold requiring special attention (p.7-8). The policy anticipates:
- Models capable of automating R&D work — specifically the work of an entry-level remote Anthropic researcher
- Autonomous replication as a related concern
- A Model Autonomy checkpoint based on 2-8 hour software engineering tasks as a precursor signal

The RSP does not specify agentic-specific evaluation protocols in detail, but notes that elicitation testing should consider "scaffolding, finetuning, and expert prompting" as resources a realistic attacker would have (p.10). The policy also anticipates future risks from "AI system[s attempting] to subvert the goals of its operators" (p.6).

## 7. Key numbers

- **4x Effective Compute** increase triggers comprehensive reassessment (p.9)
- **6 months** of accumulated post-training enhancements (alternative trigger) (p.9)
- **35x/year** estimated effective scaling rate 2018–2024 (FLOPs ~4.2x/yr × algorithmic ~2.8x/yr × post-training ~3x/yr) (p.20)
- **1000x** (35²) one-year scaleup would trigger Autonomous AI R&D threshold (p.20)
- **5-10%** of employees dedicated to security for ASL-3 Security Standard (p.13)
- Comprehensive assessment target: conclude within ~**1 month** of reaching the "notably more capable" threshold (p.10)
- ASL-3 Required Safeguards re-approved at least **annually** after initial approval (p.14)
- Updates to www.anthropic.com/rsp-updates anticipated at least every **6-12 months** (p.17)
- Prior RSP v1 ARA threshold was replaced; 2-8 hour task checkpoint introduced instead (p.21)

## 8. Findings relevant to values-benchmark design

The RSP contains several observations directly relevant to benchmark design for values-alignment:

1. **Predefined tests become outdated quickly**: "We have replaced some specifics in our previous testing methodology... with more general requirements... We have found that specific methodologies may become outdated when new research developments are introduced." (p.21) → benchmark designers should build in re-evaluation schedules.

2. **Science of evaluations is immature**: "Although still an aspirational goal, the science of evaluations is not currently mature enough to make confident predictions about the precise buffer we should require between current models and a Capability Threshold." (p.22) → evaluation validity is genuinely unsettled.

3. **Elicitation gap**: Testing must be done on helpful-only models (safeguards removed) to avoid capability underestimation. Jailbreaks and weight theft must be assumed possible (p.10). → safety eval results may not reflect true capability.

4. **Ceiling effect concern**: Some automated evaluations may be saturated. The RSP notes evaluations should be deprioritized if they "could not provide useful information" (implicitly due to saturation) — see Claude 4.1 system card (referenced).

5. **Forecasting difficulty**: Informal forecasts of future capability improvements are required but acknowledged to be hard (p.10, footnote 8).

## 9. Novel ideas worth stealing

- **Capability Threshold + Required Safeguards pairing**: A principled way to tie benchmark performance to policy triggers. Values-benchmark designers could adopt a similar structure: define a "Values Alignment Threshold" (e.g., passing rate on adversarial moral scenarios) that triggers mandatory intervention.

- **Elicitation-first design**: The RSP requires testing on helpful-only (safeguards-removed) models. Values benchmarks should similarly consider testing without system prompts or with adversarial system prompts, not just production deployments.

- **Threat model mapping as a required step**: Before running evaluations, map the most likely and consequential threat models. This discipline would improve values-benchmark construct validity.

- **Proportional iterative governance**: Benchmark suites should have tiered severity levels and mandatory reassessment triggers (e.g., "if a model achieves X% on benchmark Y, immediately escalate to full red-team evaluation").

- **Effective Compute as a recalibration trigger**: Rather than running benchmarks only at release, design a standing recalibration protocol tied to compute milestones.

## 10. Notable quotes

1. "Although still an aspirational goal, the science of evaluations is not currently mature enough to make confident predictions about the precise buffer we should require between current models and a Capability Threshold." (p.22)

2. "We should assume that jailbreaks and model weight theft are possibilities, and therefore perform testing on models without safety mechanisms (such as harmlessness training) that could obscure these capabilities." (p.10)

3. "We recognize the potential risks of highly persuasive AI models. While we are actively consulting experts, we believe this capability is not yet sufficiently understood to include in our current commitments." (p.8, footnote 3)

4. "We will not impose contractual non-disparagement obligations on employees, candidates, or former employees in a way that could impede or discourage them from publicly raising safety concerns about Anthropic." (p.16)

## 11. UNKNOWN / not in extract

- The document metadata labels this as "Anthropic Model Spec 2025," but the extract content is unambiguously the **Responsible Scaling Policy (RSP) v2, effective October 15, 2024** — not Claude's internal character/values specification. Any Claude "model spec" describing the values hierarchy (HHH, corrigibility, etc.) is a separate document not present in this extract.
- Specific evaluation scores, benchmark results, or red-team findings are not included in this policy document.
- Details of the Long-Term Benefit Trust's composition or decision-making authority are not provided.
- The specific list of CBRN capabilities of concern is described as sensitive and not publicly shared (p.20, footnote 21).
