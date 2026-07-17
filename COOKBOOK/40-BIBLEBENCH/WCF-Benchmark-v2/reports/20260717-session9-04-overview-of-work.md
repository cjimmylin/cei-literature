# WCF-Benchmark-v2 — Overview of Work

### Report 4 of 6 · Owner briefing · A consolidated development history of the Inspect-harness build

> **EXPLORATORY / NON-QUOTABLE.** All scores are 0–100 panel-median rubric
> conformity, not accuracy; bank versions are separate instruments (no
> cross-version comparison).

---

## What "this version" is

WCF-Benchmark-v2 (Christian-Ethics-Benchmark-v2) is the **re-implementation of the
WCF benchmark on the Inspect AI harness** (`inspect-ai` 0.3.246). It exists because
v1 never got off the ground as a measurement instrument: the v1 harness at
`WCF-Benchmark/04-HARNESS/` was 25 bespoke modules that never completed a single
quotable run and carried a forecast on the order of **$278** for a full T4 pass. v2
throws that away and rebuilds the entire scoring loop in **~450 lines** on a
standard, audited harness, where the `.eval` logs *are* the audit trail and every
run is explicitly exploratory.

This report is the lab notebook for that rebuild: session by session, what was run,
what was decided, why, and how the bank evolved from its ported starting state to its
final v2.4 form under an out-of-benchmark validation audit. It doubles as the methods
section — the design decisions below are the method.

Two framing facts carry through every session and must be stated once, plainly:

1. **The scores are rubric conformity, 0–100, graded by a model panel.** They are not
   accuracy and never become accuracy.
2. **Each bank version is a separate instrument.** A v2.2 number and a v2.4 number do
   not live on the same scale; the "bank-versioning rule" (every leaderboard cites its
   `bank_version` + panel + parser) exists precisely so no one silently compares
   across versions.

The arc in one line: **bank 204 → 199 → 228 → 265; single grader → median-of-3 panel;
a ceiling problem → an authoring-first frontier core; an undifferentiated blob → a
per-item-powered index; and finally an external OAuth audit that corroborated the
headline.**

---

## Sessions 1–2 (2026-07-15) — port + first full pass

**Bank:** 204 main + 22 episodes (ported). · **Key decision:** rebuild on Inspect AI;
simplest-viable single `model_graded_qa` scoring, 0–100 numeric. · **Experiment:**
29-item smoke, then a full 226-item pass on 2 SUTs.

The port took v1's 25-module harness down to ~450 lines on Inspect AI 0.3.246. The
bank came across as **204 main items + 22 episodes** (4 dev-set-only items excluded).
Scoring was deliberately minimal per owner lock: one `model_graded_qa` against a
key + rubric emitting a `GRADE: <0-100>` — no Kendall-τ, triaxial, refusal, or
contested-adherence scorers.

The 29-item live smoke cost about **$0.05** and, critically, extracted **29/29** grades
cleanly. That single fact retired v1's dominant failure mode: v1's bespoke parser drift
had been the thing that kept it from ever producing a quotable run. The full 226-item
pass then ran on two SUTs through a single gemini grader for **$1.67**, all 452 samples
scored, 0 unscored: **claude-haiku-4.5 89.9 vs gpt-4o-mini 69.5**, with the gap peaking
on complicit items (gpt-4o-mini over-assists where the gold answer is to refuse).

Two harness gotchas were found and fixed here, both of which shaped everything after:

- `model_graded_qa(instructions="")` is **falsy**, so Inspect silently substitutes its
  default correct/partial/incorrect instructions — quietly breaking a custom numeric
  grade contract. Always pass non-empty instructions.
- Inspect's `model=[...]` **list form reduces by MODE**, which is degenerate on a
  continuous 0–100 scale (first-grader-wins on any 3-way disagreement). The fix that
  becomes the panel later is `multi_scorer(scorers, "median")`.

The episode probe already flagged the problem that would dominate the middle sessions:
the generic pressure turn discriminated on gpt-4o-mini (4 zeros, full range) but
**saturated on haiku** (14/22 at 100). The ceiling was visible from day one.

---

## Session 3 — three parallel streams; the median-of-3 panel is adopted

**Bank:** 204 + 22 (unchanged). · **Key decision:** adopt a **median-of-3 grader
panel** as the default after a grader-robustness trigger fired. · **Experiment:** three
parallel streams — per-item pressure turns, grader-effect bound, SUT sweep.

**Stream A (per-item pressure turns, v2.1):** authored 22 per-item maximum-pressure
episode turns. Haiku's ceiling proved to be **real saturation** (its at-100 count rose
14→16/22), while the same turns crushed gpt-4o-mini (69.5→40.8) and merely dented qwen
(98.8→91.5). Capability for haiku, ceiling artifact for qwen.

**Stream B (grader-effect bound):** replayed all 452 session-2 responses through two
additional graders (deepseek + mistral-small). Gemini was a **harsh outlier** (max
MAD 12.3, above the 10-pt trigger; 20.4% of samples showed a ≥30-pt three-grader
spread). But rankings were **grader-robust** — no rank flip across any grader. Under
the pre-stated rule the trigger fired, and the **median-of-3 panel became the v2.1
default**.

**Stream C (SUT sweep):** a 4-SUT sweep grew into a 6-model board —
**qwen 93.4 > haiku 89.9 > mistral-large 88.9 > deepseek 85.2 > llama 72.6 >
gpt-4o-mini 69.5**. The standout was deepseek's episode mean collapsing to **51.2**:
it executed unethical instructions with verbatim admissions (compliance-with-harm).

The reusable orchestration lesson: `inspect score --model` overrides the **SUT, not the
grader closure**. To re-grade you must **replay the persisted, grade-free grading
prompt** stored in each sample's metadata. That replay-of-a-grade-free-prompt technique
is anti-leakage by construction and is the direct seed of the session-8 meta-audit.

---

## Session 4 — adversarial critique → pipeline fixes → panel-native pilot

**Bank:** 199 main + 22 episodes (after quarantines/strips). · **Key decision:** keep
the panel, resolve grader-kin collisions on the **roster** side. · **Experiment:** a
5-SUT panel-native pilot.

Five parallel Opus critics returned **43 findings** (7 pilot-blocking / 19 must-fix / 17
defer), all dispositioned. The consequential catches:

- The `GRADE_PATTERN` was **first-match**, not Inspect's deliberate last-match — a
  latent injection lever, provably exploitable, with **0 realized corruption** across
  904 archived completions. Fixed to last-match plus a 4-digit reject.
- Custom template markers were un-neutralized (Inspect sanitizes only `[BEGIN/END
  DATA]`) → SUT-answer defanging added.
- **8 items scored counterfactual criteria** impossible to satisfy in single-completion
  mode → resolved as 5 quarantines + 2 control-twin strips + 3 decline-credit gates.
- Session-3's 6-rung leaderboard was **really 3 tiers** (haiku-vs-mistral t=0.76).
- The single→panel bridge is **model-dependent** (+4.2 haiku vs +10.2 gpt-4o-mini) →
  no constant-offset bridging, ever.

Survivals (design wins): deepseek's 51.2 collapse was **genuine** (11/11 compliance-
with-harm); **0/204 items** were doctrine-recall contaminable.

The **panel-native pilot** (patched bank, not comparable to s2/s3):
qwen 96 ≈ haiku 95 ≈ kimi 94 (all adjacent, t<2) ≫ llama 80 ≈ gpt-4o-mini 78 (tier
break t=8.27). Session-3's "qwen > haiku" **did not reproduce** (t=1.88, ns). And the
ceiling was now **binding**: 72–77% of tier-1 items sat at exactly 100. The panel had
removed grader noise and thereby exposed bank saturation. 44/44 tests, 0/1105 unscored.

---

## Session 5 — measurement + design; v2.2

**Bank:** 199 + 22, repaired to **v2.2**. · **Key decision:** "new items needed" branch
**confirmed** → session 6 becomes authoring-first. · **Experiment:** item triage,
kin-delta with a control, and 3 pre-stated cheap-fix "levers."

**Phase 1 triage** (221 items, $0, logs only): **DEAD-CEILING 119 (53.8%)**, NOISY 39,
CORE-discriminating 38 (an upper bound), TIER-BREAK-only 25. The seductive
"episodes are the discrimination engine" hypothesis was **refuted** — episodes own only
the tier break (gap 36.2), not the frontier.

**Phase 2 kin-delta:** the design upgrade was adding **qwen as a non-kin control**, so
the ruling rests on a difference-in-differences rather than a raw two-panel delta (the
raw delta hid a +2.3–4.0 level shift that would have masqueraded as kin bias). With the
control: self-kin (deepseek grading deepseek) **+1.67 [+0.14, +3.27]** real-but-small;
family-kin (mistral) **+0.97 [−0.51, +2.46]** ns. Ruling: **mistral unlocked**,
**deepseek unlocked** with a ±1.7-pt sensitivity rule, **google conditional** (gemini-
kin unmeasured — an s6 piggyback mandated before quoting).

**Phases 3–4 (levers):** Lever A (an excellence gate) **failed** — 1/15 nonzero; tier-1
still hit 100 on 14/15, confirming the ceiling is **capability parity**, not scale
compression. This is the decisive result: cheap rubric tweaks cannot manufacture
frontier discrimination, so **new items are needed → authoring-first**. Levers B+C
(rubric repairs) **passed**.

**Power finding:** full-bank adjacent-frontier MDD80 ≈ 2.2–3.5 against observed tier-1
gaps of 0.9–2.4 → the pooled bank is **under-powered**. The fix is per-item information
delivered as a **separately-reported frontier-core index**. The session-6 scale-up
runbook was written here.

---

## Session 6 — authoring-first; v2.3

**Bank:** 199 + 29 new = **228 main** + 22 episodes (**v2.3**). · **Key decision:**
authoring-first executed; gate **GO** by exactly one item. · **Experiment:** the
frontier-core gate + a 4-turn escalation episode probe.

The authoring pipeline — the reusable part — ran end to end: a brief specifying
**M1–M5 discrimination mechanisms** → **6 Opus drafters** (54 items) → **10 blind
adversarial reviewers** (2 lenses/item, anti-leakage held) → Fable adjudication →
a **7-item replacement wave** → G1–G3 gates. **Kill ledger 9/61 (14.8%)**, and all 9
episodes were rebuilt (the direct-lie-fork anti-pattern — which RLHF swats every turn —
was banned in favor of plausible-duty-reframe pretexts).

The pre-stated gate came in **GO by exactly one item**: 18/52 = **34.6% nonzero
|qwen−haiku|** against the ≥⅓ criterion, 0 unscored. Contested items were the never-
saturating kind (53% nonzero). **Episodes 0/9** — even plausible-duty-reframe 4-turn
ramps could not dent tier-1 (haiku and qwen at exactly 100 on all 9) while gpt-4o-mini
fell to 42, the strongest tier-break instrument to date.

**v2.3 frozen: 228 main + 22 episodes**, with G4 applied strictly (23 items excluded,
including all 9 episodes and 8 crosswind). The **re-fire leaderboard** (key raised):
**qwen 94.4 > haiku 93.6 > gpt-5-mini 90.4 > deepseek 87.6 ≫ gpt-4o-mini 76.9**; and on
the frontier core, **three-way parity ~74** (gpt-5-mini 74.9 ≈ qwen 74.3 ≈ haiku 73.7).
0/1295 unscored. An **owner flag** was opened: strict G4 excludes the best tier-break
episodes ever authored — their re-inclusion is an owner decision (still open).

---

## Session 7 — frontier-core expansion; v2.4; parity broken

**Bank:** 228 + 37 = **265 main** + 22 episodes (**v2.4**); frontier core 29 → **66
items**. · **Key decision:** expand the core with proven molds only; ship v2.4. ·
**Experiment:** epochs×3 on the 66-item core.

The authoring wave used the two molds the s6 gate had proven discriminating: **50
drafted** (25 contested + 13 complicit + 12 steadfast) → 8 killed (16%) + 5 rebuilds +
1 further kill → **42 accepted**. The gate this time came in **GO 69.0% nonzero — double
s6's 34.6%**; mold concentration was the whole story. Strict G4 removed only 5/42 →
**37 enter → v2.4 = 265 main + 22 episodes**, with a new `wcf_frontier_core` task
auto-tracking the 66 `-N-` items.

The headline result — the first genuine within-tier-1 ordering on the benchmark:

| SUT | 66-core mean (epochs×3) | SE |
|---|---|---|
| gpt-5-mini | 78.39 | 2.17 |
| qwen3.7-plus | 75.33 | 1.64 |
| claude-haiku-4.5 | 72.48 | 1.63 |

**gpt-5-mini − haiku = +5.90 against MDD80 5.41 → SIG.** The other two pairs stayed ns.
The mechanism that made it possible: MDD80 shrank from 11–15 (s6, 29 items × 1 draw)
to **3.95–5.41** (66 × 3) — exactly the √n·√k design target from s5's power finding.

Supporting results: the google DiD came in **+0.72 [−2.55, +4.22]** → the gemini row is
**quotable with a disclosed bound**. `glm-4.7` was retired from the catalog →
substituted `glm-5` (disclosed). A grader retry wrapper (`bounded_grader`,
`GRADER_ATTEMPTS=3`) was added after gemini transients hit 8.7% → post-wrapper quorum
drops fell to 1/1742 (0.06%). Session 7 also produced the post-hoc
category/discrimination analysis `20260716A-Report.md`.

Disclosure: spend was **$20.45 vs a $20 ceiling (+2.3% breach)**, driven by glm-5
reasoning verbosity and gemini-3.5-flash's $9/M output pricing.

---

## Session 8 — meta-judging + minimax

**Bank:** v2.4 (unchanged — audit only). · **Key decision:** validate the headline with
**out-of-benchmark OAuth judges**, kept strictly as audit instruments. · **Experiment:**
grade-free replay of s7 responses through two OAuth judges + an owner-authorized minimax
epochs run.

The design reused the s3 replay technique: re-grade the persisted s7 responses by
replaying the **grade-free grading prompt** (anti-leakage by construction; explicit-tell
scan **0/779**). Two judges from OAuth-subscription channels, at **$0 OpenRouter**:
**J4 = claude-opus-4-8** (Claude OAuth), **J5 = gpt-5.5** (Codex OAuth). Kin symmetry:
J4 is kin to the haiku SUT, J5 to the gpt-5-mini SUT, qwen mutual non-kin. **Zero
parse-fails across 997+562 calls.**

**The headline survived and strengthened.** On the gpt-5-mini − haiku gap
(66-core, epochs-averaged):

| Judge configuration | gap | verdict |
|---|---|---|
| incumbent panel-3 | 5.90 | SIG (MDD80 5.41) |
| gemini alone | 8.79 | stability only |
| deepseek alone | 4.53 | stability only |
| mistral alone | 4.87 | stability only |
| **J4 Opus alone** | **19.65** | stability only |
| **J5 GPT alone** | **14.55** | stability only |
| **5-judge median** | **9.25** | SIG (MDD80 5.62) |

The sign was **positive in all 7 configurations**, and both OAuth judges saw a *larger*
gap → the incumbent panel is **conservative, not inflationary**. On kin favoritism: the
cross-kin contrast τ̂ = **−5.10** pointed *away* from favoritism (each judge graded its
own kin relatively harsher). An adversarial Opus reviewer caught a **BLOCKER pre-commit**
(SIG/ns had been stamped on single-judge rows, contradicting the report's own no-single-
judge-significance rule) and flagged that τ̂ collapses algebraically to
d̄_haiku − d̄_gpt5mini (the qwen anchor cancels) → both were fixed before commit; read τ̂
directionally only.

The **minimax addendum** (owner-authorized, ~$1.5 live): re-running minimax under matched
epochs×3 gave **minimax 79.63 vs gpt-5-mini 78.39 (+1.24, ns)** — s7's single-draw 80.45
lead **dissolved** under comparable measurement. minimax − haiku +7.14 (SIG) mirrored the
gpt-5-mini finding. So the top of tier-1 is a **three-way cluster**: minimax ≈ gpt-5-mini,
both clearing haiku, with qwen a half-step below. The reusable lesson: **single-draw and
epochs-averaged means are never comparable** — re-measure under matched draws before any
ordering claim.

---

## Arc summary

Across eight sessions the benchmark moved from a ported-but-saturated instrument to a
powered one. The **bank grew 204 → 199 → 228 → 265** main items — the dip at 199 being
the session-4 quarantine of un-scoreable items, and the two jumps being the s6 (+29) and
s7 (+37) authoring waves. Scoring evolved from a **single gemini grader** to a
grader-robustness-triggered **median-of-3 panel**. The central problem — a hard **ceiling**
where 72–77% of tier-1 items sat at exactly 100 and cheap rubric levers could not break it
— was diagnosed in s4–s5 and answered in s6–s7 by an **authoring-first frontier core** of
66 discriminating items, run at epochs×3 to convert the s5 power finding into an actual
resolved ordering (gpt-5-mini > haiku, SIG). What began as an undifferentiated **blob** of
pooled scores became a **per-item-powered index**. And in s8 the whole edifice was checked
from outside the benchmark: two OAuth judges, kept as audit instruments only, **corroborated
the headline's sign, showed the panel to be conservative, and found no kin favoritism** —
while a matched-epochs re-measurement dissolved the one unresolved top-of-tier lead into a
three-way dead heat. Every number here remains **exploratory, rubric-conformity, and
bank-version-local**.
