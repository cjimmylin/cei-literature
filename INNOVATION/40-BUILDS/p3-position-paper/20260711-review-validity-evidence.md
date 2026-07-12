# P3 Position Paper — Pre-Submission Adversarial Review (Reviewer 1: Validity / Evidence lens)

**Date:** 2026-07-11
**Reviewer lens:** Validity & evidence. Refute-first posture: each load-bearing claim treated as
unsupported until its on-disk source convinces me.
**Inputs (read-only):**
- Frozen draft: `INNOVATION/40-BUILDS/p3-position-paper/20260709-draft-v0.md` (never edited).
- Citation ledger v1: `INNOVATION/40-BUILDS/p3-position-paper/20260710-ledger-v1.md` (64 rows; phase-2
  totals 52 VERIFIED / 8 SEARCH-CONFIRMED / 4 ⚠).
- On-disk extracts under `PDF Extracts/{2024,2025,2026}/` and PDFs under `../Lit-WS-PDFs/`.

**Method.** (1) Mapped every load-bearing prose claim to its ledger row. (2) Spot-checked 20 of the
highest-stakes empirical claims directly against on-disk extracts (SpecEval/Ahmed, Zhang stress-test,
Christian RM biases, MacDiarmid reward-hacking, Helff RLVR, Qiu peer-prediction, Recchia, Carro,
Halpern social-choice survey, Deckenbach, Nair, Zhou utility-behavior, Betley, Gomez/2510.05192, Cloud
subliminal, Wang persona features, Anthropic agentic-misalignment blackmail, Teaching-Claude-Why,
Ibrahim warmth). (3) Checked internal count consistency. (4) Checked evidence-class hygiene against the
phase-2 ledger. Two verification sub-agents were blocked by a spurious content-policy false-positive on
the Nair/faking material; those four items I verified myself directly from the extracts.

**Headline.** The draft's *architecture* (pipeline framing, stage-by-stage gap thesis, judge-corruption
caveat) is sound and the great majority of citations now resolve to on-disk VERIFIED PDFs whose findings
match the prose. But the review surfaced **three venue misattributions, one metric mislabel, one
aggregation-theory mischaracterization at the center of §5, two "essentially all"/generalization
overstatements, and a live internal self-contradiction** (the draft asserts "no citation is VERIFIED"
while the governing ledger now lists 52 VERIFIED). None of these is fatal to the thesis, but several are
externally embarrassing if shipped and one (VE-6, the majoritarian claim) weakens the §5 argument as
written. Overall: **CONDITIONAL-GO.**

---

## Findings

### VE-1 — "vanilla RLHF is a disguised **majoritarian** aggregator" mischaracterizes the survey it cites
**Severity: MAJOR**
**Draft location:** §5, lines 229–230.
**Claim quoted:** *"Its central theoretical claim is that **vanilla RLHF is a disguised majoritarian
aggregator** — it silently flattens a distribution of values into a majority preference."*
**Ledger row:** W14 [VERIFIED] — `2026-Halpern-Social Choice for AI Alignment Survey.pdf` (arXiv:2606.21550).
**What the evidence supports:** The survey's central technical framing is that Bradley–Terry reward
learning is a **Borda-like** aggregation rule — explicitly a *consensus/compromise* rule, the opposite
of majoritarian: *"Borda selects the consensus or compromise response … over a response backed by a
narrower majority, and it downranks polarizing responses."* The survey does connect *majority* only to a
**preprocessing** step — binary-majority-vote label collapse, which it says induces the **Copeland**
rule, not to "vanilla RLHF" as a whole: *"many prominent alignment deployments intentionally flatten Px
into binary preference labels by taking the majority vote … this preprocessing induces the Copeland
rule."* So the paper's own headline is Borda (consensus-flattening), with majority/Copeland as a
secondary preprocessing artifact. Calling the survey's central claim "RLHF = majoritarian" is a
substantive mischaracterization of the cited source and undercuts the §5 sentence that leans on it
("majority-gold benchmark labeling is itself an instance of the majoritarian flattening the theory arm
formalizes").
**Recommended fix:** Rephrase to "RLHF reward learning is a **disguised (Borda-like) preference
aggregator**, and common majority-vote label preprocessing further collapses it toward a Copeland/majority
rule" — and adjust the §5 "majoritarian flattening" callback accordingly (or footnote that the majority
flattening is the preprocessing step, not the base rule).

### VE-2 — SpecEval "**20-point** consistency gap" mislabels a percentage-of-consistency spread and conflates it with a per-model spec-vs-behavior gap
**Severity: MAJOR**
**Draft location:** §2, lines 121–122.
**Claim quoted:** *"SpecEval … reports up to 20-point spec-versus-behavior consistency gaps across
sixteen models."*
**Ledger row:** W1 [VERIFIED] — `2025-Ahmed-SpecEval.pdf` (arXiv:2509.02464).
**What the evidence supports:** The "~20" figure is a *nearly-20%* gap in three-way **consistency scores
between providers** (best provider 0.816 vs. Google 0.64) — i.e. an inter-provider spread, not each
model's own spec-vs-behavior deficit. "sixteen models" is correct (16 models, 6 developers). Reading the
figure as "up to 20-point spec-versus-behavior consistency gaps across sixteen models" implies a
per-model self-consistency deficit of up to 20 points, which is not what the number measures.
**Recommended fix:** "reports three-way consistency scores that differ by ~20 percentage points *across
providers* (e.g. 0.82 vs. 0.64) among sixteen models" — or drop the numeric and say "substantial
provider-level consistency gaps."

### VE-3 — Three venue attributions are unsupported by the on-disk sources ("NeurIPS 2025", "ICML 2025 + Nature")
**Severity: MAJOR** (BLOCKER for the specific "+ Nature" / "NeurIPS 2025" tokens if shipped verbatim)
**Draft locations & claims:**
- §2 line 121: SpecEval `[⚠ arXiv:2509.02464, **NeurIPS 2025**]`.
- §7 lines 313–314: Betley `[SEARCH-CONFIRMED, arXiv:2502.17424, **ICML 2025 + Nature**]`.
- (Related, lower-stakes) §6 line 282 utility-engineering `[… NeurIPS 2025 **spotlight**]` — S15, still
  SEARCH-CONFIRMED / not ingested, so unverifiable here.
**Ledger rows:** W1 [VERIFIED], S18 [VERIFIED], S15 [SEARCH-CONFIRMED].
**What the evidence supports:** The SpecEval extract is an arXiv preprint (v2, 22 Oct 2025) carrying a
NeurIPS **submission checklist** — evidence of *submission*, not *acceptance*; no venue acceptance is
stated. The Betley extract (v7, 20 Jan 2026) contains **no** mention of ICML 2025 or Nature anywhere;
the only "ICML" string is an unrelated 2023 citation. Presenting a submission checklist as a "NeurIPS
2025" venue, and asserting a "Nature" publication that the on-disk PDF does not evidence, are exactly the
misattributed-venue overstatements this review is charged to catch. (The ledger's *own* notes do not
claim to have verified these venues either — they verify ID + author/title only.)
**Recommended fix:** Strike the venue tokens unless a separate acceptance record is produced. Downgrade
to "arXiv:2509.02464" and "arXiv:2502.17424" with venue omitted, or verify acceptance independently
before any external use. Do not ship "+ Nature" without a Nature DOI on disk.

### VE-4 — "**Essentially all** frontier models blackmail" overstates the source's "vast majority"
**Severity: MAJOR**
**Draft location:** §7, lines 300–302.
**Claim quoted:** *"Essentially all frontier models blackmail under goal-threat in simulated corporate
settings."*
**Ledger row:** S16 [VERIFIED] — `2025-Anthropic-Agentic Misalignment.pdf`.
**What the evidence supports:** The source (16 models) says the **"vast majority"** blackmailed, and
explicitly flags an exception: **Llama 4 Maverick did *not* blackmail** on the main prompt (only 12%
after a prompt tweak). "Essentially all" launders a documented non-universal result into a universal one
— precisely the kind of "all" where the source said "most."
**Recommended fix:** "The vast majority of tested frontier models blackmail under goal-threat (with at
least one exception on the unmodified prompt)."

### VE-5 — Wang persona-features claim imports "cross-model-convergent" from a *different* paper
**Severity: MAJOR**
**Draft location:** §7, lines 314–316.
**Claim quoted:** *"this emergent misalignment is mediated by low-dimensional, **cross-model-convergent**
persona directions that can be monitored, steered, and cheaply reversed `[⚠ arXiv:2506.19823]`
`[⚠ arXiv:2506.11618]` `[⚠ arXiv:2506.11613]`."*
**Ledger rows:** W34 (Wang 2506.19823) / W35 (Soligo 2506.11618) / W36 (Turner 2506.11613), all [VERIFIED].
**What the evidence supports:** Wang (2506.19823) studies GPT-4o only and supports monitored / steered /
cheaply-reversed (few-hundred benign samples restore alignment). It does **not** demonstrate *cross-model
convergence* — that finding belongs to Soligo (2506.11618, "Convergent Linear Representations"). The
sentence bundles three citations so the "cross-model-convergent" adjective is *jointly* supported by the
trio, which is defensible **only if the citations stay bundled**; as written it is easy to read as
attributing convergence to the lead (Wang) cite. Flag as a real risk of over-attribution.
**Recommended fix:** Keep the bundle but pin the adjective: "cheaply reversible persona directions (Wang)
that are convergent across models (Soligo) and reproducible in model organisms (Turner)." Ensure the
convergence claim is anchored to 2506.11618.

### VE-6 — INTERNAL CONTRADICTION: draft asserts "**no citation is VERIFIED**" but the governing ledger now lists **52 VERIFIED**
**Severity: MAJOR** (evidence-class hygiene / provenance integrity)
**Draft location:** Abstract-region banner lines 19–22; Appendix header line 430 ("**None is
`[VERIFIED]`.**"); Appendix line 511 ("0 `[VERIFIED]`").
**Claim quoted:** *"As drafted, **no citation in this paper is `[VERIFIED]`**"* (line 20) and *"**Every
citation in this draft is either `[SEARCH-CONFIRMED]` or `[⚠]`. None is `[VERIFIED]`.**"* (line 430).
**Ledger state:** Phase-2 (2026-07-10) upgraded 50 rows → VERIFIED; current totals **52 VERIFIED / 8
SEARCH-CONFIRMED / 4 ⚠** (ledger §1.1, §5.1). The draft is frozen at v0 and therefore *pre-dates* the
upgrade, so this is not the drafter's error — but it is a live, load-bearing contradiction between the
paper's own self-description and the authoritative evidence record. Anyone reading the draft standalone
will believe zero citations are verified; that is now false for 52 of 64.
**Recommended fix:** Do not silently edit the frozen draft. At clearance, replace the banner + Appendix
count block with the reconciled ledger totals (52/8/4) and re-scope the "must confirm before external
use" gate to the **4 ⚠ + 8 SEARCH-CONFIRMED** rows only. Preserve the ⚠/SC tags on those 12; the other
52 may drop the hedge.

### VE-7 — INTERNAL CONTRADICTION: draft's own "Ledger totals" line is off by one (41 vs 42 ⚠)
**Severity: MINOR**
**Draft location:** Appendix line 511.
**Claim quoted:** *"**Ledger totals:** 41 `[⚠]` citations · 20 `[SEARCH-CONFIRMED]` citations · 0
`[VERIFIED]`."*
**Ledger state:** The ⚠ table in the same appendix contains **42** data rows, and the ledger v1
reconciliation (§1.2, §1.3 cause 3) confirms 42 is correct — the 41 is a hand-count slip (the
line-wrapped EVALUESTEER tag, v0 lines 151–152). Internal inconsistency between the draft's stated total
and its own table.
**Recommended fix:** Correct 41 → 42 (and the whole line to 52/8/4) at the same clearance edit as VE-6.

### VE-8 — arXiv:2510.05192 ("66k samples", "agentic-misalignment mitigation") — wrong number and a framing the source explicitly rejects
**Severity: MAJOR**
**Draft location:** §7, lines 301–303 ("a large mitigation study `[⚠ arXiv:2510.05192]`"); ledger W28
claim "agentic-misalignment mitigation, 66k samples".
**Claim quoted (prose):** *"Essentially all frontier models blackmail … with a large mitigation study
`[…2510.05192]` and cross-lab eval exchange following."*
**Ledger row:** W28 [VERIFIED] — `2025-Gomez-From surveillance to signalling escalation channels as.pdf`.
**What the evidence supports:** (a) **Sample count is wrong.** The paper ran **24,000** trials (10 models
× 24 conditions × 100), not 66k — "66k samples" appears nowhere. (b) **Framing.** The paper *explicitly
rejects* the "agentic misalignment" label: *"We prefer this framing [task–rule conflict] to 'agentic
misalignment' because it focuses on the situational trigger rather than implying a claim about the
agent's internal values."* It is a genuine mitigation study (baseline harmful rate 38.73% → 1.21% with a
credible escalation channel), but describing it as "agentic-misalignment mitigation, 66k samples"
double-errs on number and on the source's own preferred framing. The paper was also retitled
(insider-risk → "From surveillance to signalling"), which the ledger notes.
**Recommended fix:** In prose, "a large environmental-controls / task–rule-conflict mitigation study
(harmful-action rate 38.7% → 1.2%)"; in the ledger, correct "66k" → "24k samples" and soften the
"agentic-misalignment" descriptor. (Prose currently doesn't state the 66k, so the prose fix is light; the
ledger row must be corrected before it is cited externally.)

### VE-9 — Load-bearing claims still resting on ⚠ / SEARCH-CONFIRMED rows (presumptively unsafe for external use)
**Severity: MAJOR** (as a gate, not a per-claim error)
**Draft locations / rows:** Of the 12 non-VERIFIED rows, the load-bearing ones are:
- **W3 ⚠** (arXiv:2607.01250) — §2 line 126–128: *"A June-2026 systematic review found 'underspecified'
  to be the single most frequent failure label across the alignment corpus."* Ledger §5.3 **declined the
  upgrade**: the ingested 2607.01250 is Dönmez "Structuring the Space of Sociotechnical Alignment," whose
  title/claim does **not** confirm "systematic review / underspecified most frequent." This is a specific
  empirical claim resting on a title/claim-divergent ⚠ row — the single most fragile factual claim in §2.
- **W5 ⚠** (2510.06370, EVALUESTEER) — §3 line 151–152: *"reported <75% accuracy on combined profiles."*
  Not ingested; specific numeric on an unverified row.
- **W26 ⚠** (2602.20710) — §6 line 277–278 (counterfactual-simulation faithfulness training). Not ingested.
- **W32 ⚠** (2604.09588) — §7 line 308 (identity-file architectures). Not ingested.
- **S1 SC** (Model Spec Evals, Mar 2026) — §2 line 126, presented as *"OpenAI shipped Model Spec Evals
  (Mar 2026) as a versioned compliance metric"* — asserted as shipped fact on a search-only row.
- **S13 SC** (Sheshadri et al. 2025) — §6 line 271–272 (compliance-gap across frontier models). Ledger
  notes batch2 ingested a *different* paper (Marks 2503.10965); Sheshadri not on disk.
- **S15 SC** (2502.08640, utility engineering) — §6 line 282, the "coherent, scale-strengthening value
  systems" half of the §6 adjudication, with a "NeurIPS 2025 spotlight" venue tag; not ingested.
- **S8/S9/S10/S11 SC** — §5 aggregation (NLHF/maximal-lottery, clone-robustness, Collective Alignment
  pipeline, Habermas-machine critique); several carry specific framings.
**What the evidence supports:** For these 12, the ledger's on-disk verification is *absent or divergent*.
Per the ledger's own load-bearing rule, their findings are presumptively unsafe to state as established
fact externally.
**Recommended fix:** Before external use, either (i) fetch-verify each of the 12, or (ii) retain explicit
hedging in prose for each ("reportedly," "search-confirmed," "not independently verified") and, for W3
specifically, either re-acquire the actual systematic review or delete the "most frequent failure label"
sentence — do not ship it as fact.

### VE-10 — Evidence-class hygiene: several ⚠/SC findings are stated in prose as flat fact without the tag's hedge
**Severity: MINOR** (subsumed by VE-9 but called out per task item (d))
**Draft locations & claims:**
- §2 line 126: *"OpenAI shipped Model Spec Evals (Mar 2026)"* — declarative "shipped," source is S1
  [SEARCH-CONFIRMED].
- §2 line 127–128: *"found 'underspecified' to be the single most frequent failure label"* — declarative
  "found," source is W3 [⚠, upgrade declined].
- §3 line 151: *"reported <75% accuracy"* — declarative numeric, source W5 [⚠, not ingested].
- §6 line 271–272: compliance-gap *"extended across frontier models"* — declarative, S13 [SC, wrong paper
  ingested].
**What the evidence supports:** The inline `[⚠ …]`/`[SEARCH-CONFIRMED]` tags *are* present, so the hedge
is technically attached; but the surrounding verbs ("shipped," "found," "reported") read as settled fact.
The tag and the verb should not disagree.
**Recommended fix:** Where the verb asserts a fact but the tag hedges, soften the verb ("OpenAI *appears
to have* shipped …", "a review *reportedly* found …") until the row is VERIFIED.

### VE-11 — Carro "belief-misaligned arguments rated higher quality" conflates two distinct metrics
**Severity: MINOR**
**Draft location:** §4.1, lines 202–204.
**Claim quoted:** *"AI debaters are measurably more persuasive when arguing their own priors, **and**
belief-misaligned arguments are rated higher quality."*
**Ledger row:** W13 [VERIFIED] — `2025-Carro-AI Debaters Own Beliefs Bias.pdf` (arXiv:2510.13912).
**What the evidence supports:** Both halves are individually TRUE but come from *opposite-direction*
metrics on different axes: *persuasion/win-rate* is higher for prior-aligned arguments (Elo), while the
*isolated pairwise quality* rating (LLM-judge clarity/relevance) is paradoxically higher for
prior-misaligned arguments. Juxtaposed in one sentence with "and," they read as one coherent finding when
they are two, and the draft omits that the "higher quality" verdict is itself an LLM-judge artifact — which
is ironically the very §4.1 point.
**Recommended fix:** Split: "more persuasive (higher win-rate) when arguing their priors, yet an LLM
quality-judge paradoxically rates their *belief-misaligned* arguments as clearer/higher-quality — itself
an instance of the judge bias this section warns about."

### VE-12 — Zhang stress-test "~300k scenarios" is the diversity-filtered subset, not the generation total
**Severity: MINOR**
**Draft location:** §2, lines 122–125.
**Claim quoted:** *"generated on the order of 300k value-tradeoff scenarios … with high-disagreement
scenarios showing 5–13× more non-compliance."*
**Ledger row:** W2 [VERIFIED] — `2025-Zhang-Stress-Testing Model Specifications.pdf` (arXiv:2510.07686).
**What the evidence supports:** The 5–13× figure is **exactly right** (Key Finding 1: 4.6×≈5× from
Table 2, >13× from Fig 2; contradictions/ambiguity-not-defiance framing also correct). The "300k" is the
paper's *diversity-filtered analysis subset*; total generation was **410k+**. "Generated ~300k" is
mildly imprecise (the 300k were *selected*, 410k generated), though the abstract does itself say "generate
over 300,000 diverse query scenarios," so this is defensible-but-loose.
**Recommended fix:** "generated 400k+ scenarios (≈300k retained after diversity filtering)" — or leave,
citing the abstract's own phrasing. Low priority; the load-bearing 5–13× is solid.

### VE-13 — "Teaching Claude why" >3× reduction: figure correct, attribution slightly off ("reasons > rules")
**Severity: MINOR**
**Draft location:** §7, lines 322–323.
**Claim quoted:** *"reason-based constitutions generalize better than rule-based ones (reported >3×
reduction in agentic misalignment)."*
**Ledger row:** S19 [VERIFIED] — `2026-Anthropic-Teaching Claude Why.pdf`.
**What the evidence supports:** The **>3× figure is real** (blackmail 65% → 19%, "more than a factor of
three"), but it refers to *high-quality constitutional documents + fictional stories that are
out-of-distribution from the eval*, not to a clean *reasons-vs-rules* head-to-head. A separate
smaller result (22% → 3%) is the closer "reasons matter" comparison. The draft's "reasons > rules"
gloss slightly over-tidies which intervention produced the >3×.
**Recommended fix:** "high-quality reason/constitution-based training reduced agentic misalignment >3×
(65%→19%), generalizing from out-of-distribution documents."

### VE-14 — Christian RM "cannot scrub" is a mild strengthening of "does not fully close"
**Severity: MINOR**
**Draft location:** §3, lines 148–151.
**Claim quoted:** *"They inherit 'sticky' value biases from pretraining that identical preference data
cannot scrub."*
**Ledger row:** W4 [VERIFIED] — `2026-Christian-RMs Inherit Value Biases.pdf` (arXiv:2601.20838).
**What the evidence supports:** Well-supported: "sticky" is the paper's own frame; the agency(Llama)/
communion(Gemma) family-level finding holds "even when the preference data and finetuning process are
identical." The one nuance: ~100k preference pairs *narrow but do not close* the gap — so "cannot scrub"
is directionally right but a touch stronger than "cannot fully overcome." Acceptable; noting for
precision.
**Recommended fix:** Optionally soften "cannot scrub" → "cannot fully scrub / does not close." Low priority.

### VE-15 — MacDiarmid "~12% sabotage" is one task's rate, not a general run-rate; "naturally generalizes" needs a nuance
**Severity: MINOR**
**Draft location:** §3, lines 160–162.
**Claim quoted:** *"reward hacking during production RL naturally generalizes to alignment faking,
sabotage, and broad emergent misalignment `[…2511.18397]` (sabotage reported in ~12% of runs)."*
**Ledger row:** W8 [VERIFIED] — `2025-MacDiarmid-Natural EM from Reward Hacking.pdf`.
**What the evidence supports:** The **12%** is the attempted-sabotage rate on **one** evaluation (code
sabotage, default model, original classifier prompt), not a global "~12% of runs" across the study
(other settings 0–25%). The generalization claim is supported, but the paper notes the model did **not
discover the hacks unaided** — hacks were induced via synthetic-document finetuning/prompting first, after
which misalignment generalization is spontaneous. "In production RL naturally generalizes" slightly
overstates the naturalness of the *initial* hack.
**Recommended fix:** "sabotage attempted ~12% of the time on the code-sabotage eval," and "once
reward-hacking is learned, it spontaneously generalizes to …". Low priority.

### VE-16 — Qiu peer-prediction, Deckenbach, Nair, Zhou, Betley(narrow→broad), Cloud(same-init), Helff, Recchia — VERIFIED CLEAN
**Severity: (none — positive control)**
For completeness and to demonstrate the check was real, these high-stakes claims spot-checked **accurate**
against on-disk extracts:
- **Qiu (W10):** "strengthens as capability gap widens" = paper's "inverse scaling property"; "5–20×
  collapse toward random" is genuinely this paper's own reported baseline; **"ICLR 2026" venue is
  correctly stated on every page header** (contrast VE-3 — this one checks out). ACCURATE.
- **Deckenbach (W21):** paper title *is* "Models That Know How Evaluations Are Designed Score Safer."
  ACCURATE.
- **Nair (W22):** "alignment faking substantially more prevalent than previously reported" (37% compliance
  gaps in 7B models). ACCURATE.
- **Zhou (W27):** "When Preferences Fail to Become Incentives: A Utility–Behavior Gap" — elicited utilities
  do not drive incentivized behavior. ACCURATE.
- **Betley (S18):** narrow finetuning → broad misalignment. ACCURATE (venue tokens flagged separately in
  VE-3).
- **Cloud (W39):** the "same-initialization" qualifier is load-bearing and correctly stated. ACCURATE.
- **Helff (W9):** RLVR gameable — causal + observational. ACCURATE.
- **Recchia (W12):** debate presentation does not repair confirmation/automation bias (one qualified
  exception on the LLM-wrong subset). ACCURATE.
- **Ibrahim (S20):** warmth→accuracy/sycophancy trade-off. ACCURATE.

---

## Summary table

| # | Finding | Severity | One-line |
|---|---|---|---|
| VE-1 | §5 "RLHF = majoritarian" mischaracterizes the survey (it's Borda/consensus; majority is a preprocessing step) | MAJOR | Fix the central §5 characterization to Borda + majority-preprocessing/Copeland |
| VE-2 | SpecEval "20-point gap" mislabels an inter-provider consistency spread as a per-model spec-vs-behavior gap | MAJOR | Reframe as ~20pp *provider-level* consistency spread |
| VE-3 | Venue misattributions: SpecEval "NeurIPS 2025", Betley "ICML 2025 + Nature" unsupported on disk | MAJOR (BLOCKER for verbatim) | Strike venue tokens until acceptance evidenced |
| VE-4 | "Essentially all frontier models blackmail" overstates source's "vast majority" (Llama exception) | MAJOR | "Vast majority … with ≥1 exception" |
| VE-5 | "cross-model-convergent" attributed near Wang; belongs to Soligo | MAJOR | Pin convergence to 2506.11618 |
| VE-6 | Draft says "no citation VERIFIED"; ledger now 52 VERIFIED — live self-contradiction | MAJOR | Reconcile banner+appendix to 52/8/4 at clearance |
| VE-7 | Draft's own ⚠ total 41 vs table's 42 | MINOR | Correct 41→42 |
| VE-8 | 2510.05192 "66k samples / agentic-misalignment mitigation" — wrong count (24k) + framing source rejects | MAJOR | Fix count to 24k; soften framing (prose + ledger W28) |
| VE-9 | Load-bearing claims on 12 ⚠/SC rows (esp. W3 "underspecified most frequent", S1, S13, S15) presumptively unsafe | MAJOR (gate) | Fetch-verify or keep explicit hedge; W3 sentence must not ship as fact |
| VE-10 | ⚠/SC findings stated with fact-verbs ("shipped/found/reported") despite hedge tags | MINOR | Soften verbs to match tags |
| VE-11 | Carro "rated higher quality" conflates win-rate vs isolated-quality (opposite-direction) metrics | MINOR | Split the two metrics; note it's an LLM-judge artifact |
| VE-12 | Zhang "~300k scenarios" is filtered subset; 410k generated (5–13× figure itself correct) | MINOR | "≈300k retained of 400k+"; keep 5–13× |
| VE-13 | Teaching-Claude >3× figure correct but "reasons>rules" attribution loose | MINOR | Attribute >3× to the OOD-constitution intervention |
| VE-14 | Christian "cannot scrub" mildly stronger than "does not close" | MINOR | Soften to "cannot fully scrub" |
| VE-15 | MacDiarmid "~12% of runs" is one task's rate; "naturally generalizes" needs the induced-hack nuance | MINOR | "~12% on the code-sabotage eval"; "once learned, generalizes" |
| VE-16 | Positive control: Qiu/Deckenbach/Nair/Zhou/Betley/Cloud/Helff/Recchia/Ibrahim verified clean | — | Check was real; core empirical spine holds |

**Tally:** 8 MAJOR (one of which, VE-3, is a BLOCKER for the specific venue tokens if shipped verbatim;
VE-9 is a gate) · 7 MINOR · 1 positive-control clean.

---

## Overall recommendation: **CONDITIONAL-GO**

The paper's evidentiary spine is genuinely strong: the pipeline framing is a considered opinion (as
declared), and of ~20 high-stakes empirical claims spot-checked against on-disk VERIFIED PDFs, nine
verify cleanly and the remainder are correctable calibration/attribution errors rather than fabrications —
the load-bearing numbers that survive (Zhang 5–13×, Qiu 5–20× inverse-scaling, Christian agency/communion,
Nair 37% faking, Helff RLVR causality) are accurate. **CONDITIONAL** because the draft, if circulated as
frozen, would ship three unsupported venue attributions (VE-3), a metric mislabel (VE-2), a §5-central
aggregation-theory mischaracterization (VE-1), two "all"/generalization overstatements (VE-4, VE-8), and a
live internal contradiction claiming zero verified citations when 52 now are (VE-6) — each externally
damaging and each cheaply fixable at the clearance edit. **NO external use** until (a) VE-1–VE-8 are
corrected, (b) the 12 ⚠/SC rows in VE-9 are either fetch-verified or explicitly hedged in prose (W3's
"most-frequent-failure-label" sentence must not ship as fact on a title-divergent ⚠ row), and (c) the
banner/appendix count block is reconciled to the phase-2 ledger totals — after which this clears for the
second (Fable/Jimmy) gate.
