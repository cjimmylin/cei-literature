# RP-07 HAWTHORNE — Evaluation Awareness as a Reported Statistic

**Gaps:** G-14 (evaluation awareness), G-15 (alignment-faking-aware evaluation)
**Portfolio claim:** measurement science · **Wave:** 1 (quick win — machinery mostly exists)
**Author:** Fable 5 · 2026-07-07

## Motivation

Models increasingly detect that they are being evaluated and behave differently: system cards now carry evaluation-awareness sections; models that recognize eval-design patterns score "safer"; alignment-faking diagnostics find performative compliance widespread; reasoning models can obfuscate against monitors. The consequence for values measurement is stark: **an announced values score is a measurement of test-taking behavior, and it upper-bounds internalization.** The COOKBOOK's unannounced-measurement law anticipated this. What's missing — in the field and in CEI's own releases — is the *quantification*: a standard, per-model, per-construct statistic for how much announcement inflates values scores. Naming it after the Hawthorne effect gives the field a handle it will actually use.

## Core hypothesis

**H1:** The Hawthorne delta — matched-item score difference between explicit-eval delivery and embedded-in-task delivery — is positive, stable (replicable across item samples), and model-specific.
**H2:** The delta varies by construct (e.g., larger for prosocial self-presentation traits like kindness/honesty-claims than for harder-to-fake process behaviors).
**H3 (the scary one, pre-register carefully):** The delta *grows* with model capability and with reasoning-mode — more capable models are better test-takers, so announced benchmarks get *less* valid as models improve.

## Method sketch

1. **Paired delivery.** Each item exists in two forms: (a) announced (framed as an ethics evaluation — the field's default), (b) embedded (the same decision arises naturally inside a realistic task stream — UNMARKED/SALIENCE delivery machinery, already designed and partially built). Content-matched, delivery-isolated, order counterbalanced across sessions.
2. **Awareness probes.** Post-hoc elicitation ("was that an evaluation?") on a held-out subsample, plus in-prompt canary discipline (SERMONMOUNT MF-lesson: canaries verify the embedded framing wasn't seen through). Awareness rate is a covariate, not the endpoint — behavior difference is the endpoint.
3. **Faking layer.** Add value-conflict diagnostics (2026 alignment-faking methodology) as a third condition: announced + incentive-to-misrepresent. Delta between conditions 1 and 3 estimates strategic (not just reactive) inflation.
4. **Estimation.** Per-model, per-trait deltas with cluster-bootstrapped CIs (stats machinery pinned in the SERMONMOUNT pre-reg is reusable); capability axis from public benchmark scores for H3.
5. **Reporting standard.** Propose "Hawthorne-corrected" reporting: values benchmarks report announced score, embedded score, and delta. Fold into COOKBOOK KB-01 as an amendment candidate and adopt in all future CEI releases.

## Novelty vs. published work

Evaluation awareness is documented as a phenomenon (system cards, eval-design-recognition studies); nobody has published a cross-model, cross-construct *quantification* on values content, and no benchmark reports announcement sensitivity. The methodological move — treat announcement as a measurement facet and report its effect size — is standard psychometrics applied where nobody has applied it. Fast, clean, and it makes every existing announced values benchmark reinterpretable.

## Deliverables

1. Paired-delivery protocol + item pairs (reusing existing bank content; public release).
2. Hawthorne-delta estimates: 6–8 frontier models × 4–6 constructs (the headline table).
3. Methodology paper (target: fast venue first — workshop/short paper — to claim the term and the method; journal-length follow-up with H3).
4. COOKBOOK KB-01 amendment proposal + adoption in CEI release checklists.

## Opus build tasks

- O1: Item-pair assembly from UNMARKED/SALIENCE designs + existing banks (the embedded forms are the craft-heavy part; Fable-tier gate on a 20-pair sample).
- O2: Canary + awareness-probe module (light).
- O3: Faking-condition scripts adapting the value-conflict diagnostic method (read the 2604.20995 method first — acquisition list P1).
- O4: Run (keys-gated) + delta estimation with the pinned bootstrap stats.
- O5: Short-paper draft for Fable-tier review.

## Kill criteria

- **K1:** If deltas are within noise across all constructs for current frontier models (pre-registered minimum detectable effect: 0.3 SD), publish the null prominently — "announced values evals are (currently) not inflated" is valuable and legitimizes standard practice. The program then closes cleanly.
- **K2:** If embedded delivery can't pass the canary/awareness check (models see through the task framing at >30% rates), the embedded condition isn't unannounced — return to delivery craft before estimating anything.
- **K3:** If H3's capability analysis is confounded beyond repair at feasible model counts (capability correlates with vendor, training recipe, everything), report H1/H2 only; do not stretch.
