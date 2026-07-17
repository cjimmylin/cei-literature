# WCF-Bench-v2 — Messaging, Title & Abstract

**Report 6 of 6 · Scale-Up Readiness Briefing · 2026-07-17 · internal**

> **EXPLORATORY / NON-QUOTABLE.** Everything below is internal message-shaping for a
> future paper. All results are 0–100 panel-median **rubric conformity**, not accuracy;
> the benchmark makes **rank** claims, not absolute-score claims. No number here is
> cleared for external quotation. The title and abstract are **drafts for review.**

---

## 1. The headline (integrated / three co-equal contributions)

The work is strongest told as **one paper with three interlocking contributions**,
each of which makes the next credible:

> **We built a benchmark that separates frontier models on *conduct* where knowledge
> benchmarks can't; we validated the LLM panel that scores it by having independent
> out-of-benchmark judges try to break its headline (they couldn't); and the resulting
> leaderboard shows a resolved frontier ordering — gpt-5-mini and minimax-m3 lead a
> tight tier-1 cluster, clearing claude-haiku-4.5.**

The three pillars:
1. **A discriminating instrument.** WCF-Bench-v2 measures *costly obedience* — holding
   a lawful-but-costly ethical position when the cooperative RLHF-default answer is the
   trap. It discriminates frontier models exactly where standard evals saturate.
2. **A validated judge-panel.** A median-of-3 cross-vendor LLM panel, stress-tested by a
   5-judge meta-audit (including Claude Opus and GPT-5.5 as independent judges): the
   panel is **conservative, not inflationary**, and shows **no kin favoritism**.
3. **A frontier leaderboard.** On the 66-item frontier core, tier-1 is a **three-way
   cluster** (minimax-m3 ≈ gpt-5-mini, both clearing haiku; qwen a half-step below).

The narrative hook that ties them together: **models that ace questions *about* Christian
virtue can still fail at *practicing* it under cost — and we can measure the difference
reliably enough to rank frontier systems.**

---

## 2. Most impactful findings, ranked

1. **The ceiling-breaking construct.** On the v1-derived layer, **53.8% of items are
   dead-ceiling** for capable models — the faithful answer is one RLHF already rewards.
   The authored frontier core inverts this: the RLHF-default answer is engineered to be
   the *failing* one, so frontier models land in the 70–80 band and separate. *This is
   the reusable idea other researchers will want.*
2. **"Judging the judges" holds.** Two fully independent, out-of-benchmark judges
   corroborate the headline **and see a larger gap** (J4 Opus 19.65, J5 GPT-5.5 14.55 vs
   panel 5.90) — the panel is conservative. 5-judge ICC(2,k) = 0.798; the two OAuth
   judges agree at ρ = 0.849. *This is the methodological credibility anchor.*
3. **A resolved frontier ordering.** gpt-5-mini − haiku = **+5.90 (SIG)** — the first
   within-tier-1 conduct ordering the benchmark could resolve; minimax-m3 then ties
   gpt-5-mini (+1.24, ns) and also clears haiku (+7.14, SIG). Tier-1 is a **three-way
   cluster**, not a single leader. *This is the concrete result.*
4. **No kin favoritism (directional).** The cross-kin DiD τ̂ = −5.10 leans anti-kin —
   each judge grades its own kin *harsher*, the opposite of the concern. *Read
   directionally only (see the caveat in §4).*
5. **Ordering is robust; calibration is not.** The mold-specific harshness of stricter
   judges widens the gap rather than shifting scores uniformly — which is *why* rank
   claims are trustworthy while absolute 0–100 values stay non-quotable.

---

## 3. Draft title & abstract (for review)

**Title (draft):**
> **Costly Obedience: A Discriminating Ethics Benchmark, a Validated LLM Judge-Panel,
> and a Frontier Leaderboard**

*Alternative subtitles considered:* "Measuring whether models *practice* the ethics they
can *recite*"; "Ranking frontier models on conduct where knowledge benchmarks saturate."

**Abstract (draft — internal, not cleared for external use):**
> Standard capability and knowledge benchmarks increasingly saturate for frontier
> language models, losing the resolution needed to compare them — and they measure what
> a model *knows*, not how it *acts* when the cooperative response is subtly wrong. We
> present **WCF-Bench-v2**, a benchmark that measures **costly obedience**: whether a
> model holds a lawful-but-costly ethical position, grounded in the Westminster
> Standards, when the RLHF-default answer is the trap. The benchmark comprises 287 items
> across nine "molds" of moral reasoning and agentic pressure episodes, including a
> 66-item **frontier core** authored so that the cooperative default answer fails; on a
> legacy item layer 53.8% of items are ceiling-saturated for capable models, whereas the
> frontier core separates them. Items are scored 0–100 for **rubric conformity** (not
> accuracy) by a cross-vendor **median-of-3 LLM panel**. We validate the panel with a
> five-judge **meta-audit** that replays a grade-free grading prompt (anti-leakage by
> construction) and adds two fully independent out-of-benchmark judges (Claude Opus and
> GPT-5.5): the panel is **conservative rather than inflationary** — both independent
> judges reproduce the headline ordering and see a *larger* gap — with an overall
> ICC(2,k) of 0.798 and no evidence of kin favoritism. On the frontier core, the tier-1
> frontier is a **three-way cluster**: minimax-m3 ≈ gpt-5-mini (ns), both significantly
> clearing claude-haiku-4.5, with qwen a half-step below. We find that inter-judge
> *ordering* is robust while absolute *calibration* is judge-dependent; accordingly we
> report ranks, not absolute scores. All results are **exploratory** measures of rubric
> conformity against a specific confessional standard and should not be read as general
> ethical accuracy.

---

## 4. Framing guardrails (must survive into any external draft)

These are non-negotiable and easy to erode when prose is polished:
- **EXPLORATORY / NON-QUOTABLE, rubric-conformity-not-accuracy** stays in the abstract
  and near every results table. The benchmark measures conformity to *the Westminster
  Standards*, a specific confessional rubric — not universal moral correctness.
- **Ranks, not absolute values.** Ordering is judge-robust; absolute 0–100 calibration
  is not. Never headline an absolute score.
- **τ̂ is directional only.** "No kin favoritism" must never be stated as a significance
  test: τ̂ collapses algebraically to d̄_haiku − d̄_gpt5mini (the qwen anchor cancels),
  conflates kin bias with any judge×SUT interaction, and rests on one instrument.
- **Single-judge rows carry no significance.** Only the panel-3 and 5-judge-median rows
  get SIG/ns verdicts (single-judge MDD80 ≈ 8–10).
- **OAuth judges are audit instruments**, never leaderboard rows and never in the panel.
- **Bank versions are separate instruments** — no cross-version score comparison.

---

## 5. What to flesh out before the paper

- **Figures worth building:** the RLHF-ceiling histogram (v1 layer at 100 vs frontier
  core spread); the 5-judge concordance / J4~J5 scatter (ρ = 0.849); the house-style
  harshness heatmap (judge × mold); the frontier-core leaderboard with MDD80 error bars.
- **A worked "trap" example** in the intro (e.g. complicit COMP-C9-001 or steadfast
  STED-N-003 from the Benchmark Card) to make "the default answer is the trap" concrete.
- **Scale-up leaderboard:** the current tier-1 four-model core is thin for a leaderboard
  paper; the many-model scale-up (Report 5) fills this out.
- **Construct-validity paragraph:** why Westminster Standards as the rubric, and the
  honest scope limit (a specific confessional tradition, not universal ethics).

---

## 6. One-line messages by audience

| Audience | One-liner |
|---|---|
| Owner / internal | "The headline survived an adversarial judge-swap and got *stronger*; the instrument and judge are ready to scale." |
| ML research | "A conduct benchmark that separates frontier models where knowledge benchmarks ceiling out — with the LLM judge-panel validated by independent out-of-benchmark judges." |
| AI-safety framing | "Models that can *recite* an ethic don't always *hold* it under cost; we can measure the gap and rank frontier systems on it." |
| Skeptic-facing | "We tried to break our own headline with two independent frontier judges. It got bigger, not smaller." |

---

*Draws on Reports 1–5 of this batch. All numbers trace to the session-7/8 stats JSONs;
none is cleared for external quotation. Title and abstract are drafts for owner review.*
