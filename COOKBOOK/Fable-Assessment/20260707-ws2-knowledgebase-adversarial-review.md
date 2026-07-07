# WS-2 — Knowledgebase Adversarial Review: KB01–13 + 2 SOTA docs (Fable-adjudicated, 2026-07-07)

**Method:** Fable read KB01 (Seven Laws master) directly; three Opus refute-first agents
covered KB02–05, KB06–09, KB10–13 + `alignment-methods-overview` +
`benchmark-landscape-statistics`, cross-checking against the verified 10-LITERATURE layer
and the shipped designs. Every candidate finding adjudicated here. First-ever review of the
standards layer.

## Verdict

**No KILL. The factual spine is strong** — 33/34 landscape statistics matched their digests
verbatim, the numbers in KB06–09 check against the verified lit reviews, and the Seven Laws
are sound as principles. Four systemic defect classes require an Opus fix pass:

1. **Stale embedded design briefs (the worst class — six MAJORs).** The §6 briefs in
   KB08/09/10/11 predate the 2026-07-05 adversarial gate and now actively contradict the
   shipped designs: KB10 promises 3 scoring layers where 04 ships 4 (omitting the headline
   D-layer!), bets discrimination on the T2 layer 04 demoted, and cites κ 0.87–0.96 where
   the binding gate is 0.7; KB11 headlines MGCFA-as-artifact where 05 demoted it to
   exploratory, and scores "adaptation trajectory" where 05's whole C1 fix replaced it with
   *selectivity* (raw adaptation = sycophancy-confounded); KB08 promises a
   behavior-under-incentive axis 02 never built; KB09 promises a dyadic axis 03 swapped for
   rationalization. **Fix: a SUPERSEDED banner on each §6 brief naming the shipped design
   file and its 3–6 deltas.** A builder must never ground on a KB brief again.
2. **Under-operationalized gate standards** — the §6.2 bar cluster (no test, no clustering
   unit, no effect-size floor, no correction convention, single unverified exemplar set at
   a *weaker* p than its own evidence), the Law-1 capability gate, the 10%-fine-tune probe,
   and the absent power/MDES guidance. **All resolved by the WS-6 rulings CS-1/CS-2/CS-3/
   CS-5** plus the addendum items below.
3. **Confidence inflation at headline points.** KB09 states the MP-DP effect as established
   fact three times with zero fragility caveat — the one doc that most needed the
   adjudicated hedge is the one place it is missing — and by KB04's own bar MP-DP (1/36
   pairs) does not "discriminate." KB11 elevates the N_eff≈3.4 trials number (100%
   Western-liberal resolution) to a landscape headline. KB13/overview carry undated
   perishable superlatives.
4. **Scattered scoping errors**, each small, each correctable in one line (list below).

## Adjudicated findings (sustained unless noted; grades final)

**KB01 (Fable direct read):** Law-1 "~40%" threshold had no provenance or operationalization
→ resolved by CS-5 (MAJOR, fixed). "Aggregate conservatively (worst-category), never by
mean" → MINOR: report both, headline the conservative one (worst-category alone lets one
noisy category own the headline). "Fine-tuned scorer usually beats a frontier judge" →
MINOR: single-study (Flames); hedge to "can beat." Otherwise KB01 is in good shape; the
pre-registration checklist is genuinely strong.

**KB02–05 (agent A, 19 findings):** F1/F2/F3/F5/F6 (§6.2 cluster) MAJOR → CS-1/CS-5.
F4 MAJOR → NurValues card verification ordered (verification list); until verified the 90%
bar is labeled *pre-registered convention*; the p<0.001→p<0.01 weakening vs its own
exemplar is now disclosed. F18 MAJOR → MDES/power statement mandated per design before
first live run (addendum). F15 MAJOR-terminology → "robustness confidence interval" renamed
*robustness envelope*, reported per-axis, never pooled alone. F17 → the 10%-fine-tune probe
is operationalized by adopting the DUPLEX/ENGINE implementation as canonical (10% stratified
sample; parity margin 0.02–0.05 config; reference = same model's full-bank score). MINORs
sustained: ≤70%-of-ceiling ambiguity noted (F7); undefined "longevity score" (F8); Clifford
thresholds scoped to taxonomic vignettes (F10); the α<0.5 self-consistency gate relabeled
(it is internal-consistency machinery, not test-retest — keep the registered 0.5, fix the
name) (F11); the "exceeds ~95% of 620 papers" marketing line cut (F12); encoder-classifier
perturbation magnitudes flagged non-transferable (F16); "Never for" table gets the
paired-floor carve-out (F14); ceiling-uncertainty propagated into headroom claims (F19).

**KB06–09 (agent B, 14 findings):** F1+F2 MAJOR sustained → KB09 gets the adjudicated
MP-DP caveat inline at all three assertion sites, and "the only discriminating instrument"
is reworded to "the only instrument showing any between-model movement (1/36 pairs — below
the KB04 bar)." F3 MAJOR sustained → KB08's two incompatible "three dissociations" triads
reconciled; **the dropped verdict-vs-coherence axis is flagged as a real loss** — it is the
answer-key-free, contamination-resistant scoring family and appears in the roadmap as a
future enhancement (not a mandate). F4/F5 MAJOR → SUPERSEDED banners (class 1). F10
(P0 gate runs on single unvalidated judge scores) adjudicated ACCEPTABLE-for-P0 with a
disclosure line added to the P0 run checklist — the smoke test's provisional labeling
already carries this; full KB07 judge validation binds from P1 up. F11 MINOR → fix the
docstring's mis-cite (subject≠judge is a stricter extension, not KB07 L54); the
generator≠judge rule is vacuous at P0 (hand-authored items) — assert it in code when a
generator first exists. MINORs sustained: VLM qualifier restored on directional sycophancy
(F6); one "most-replicated" superlative demoted (F7); MoReBench ~zero-capability-r scoped
to PR-style process scoring (F8); F12 inline elicitation caveat; F13 "identical" →
"indistinguishable at N=1/temp-0"; F14 causal gloss softened.

**KB10–13 + SOTA (agent C, 25 findings):** #19–24 MAJOR → SUPERSEDED banners (class 1).
#1 MAJOR sustained → KB10 §5 VOID table corrected against the digest (Sikhism 6/2,
Confucianism 14/1 are NOT void; KB10's own §1 list disagrees with its §5 table). #5 MAJOR
sustained → the 100%-Western-liberal trials stat carries the N_eff≈3.4 caveat at point of
use. #14 MAJOR sustained → verbatim-rule violation fixed ("18 of 54 fail only on data
availability" → the digest's own enumeration; drop the unsupported "only"). #7 sustained →
addendum rule: each benchmark pre-registers ONE primary distributional divergence (JSD
recommended: symmetric, bounded), others as sensitivity — KL/JSD/L2 can rank-order models
differently and the doc recommending all three reproduced the aggregation pathology it
condemns. MINORs sustained: 45-vs-47 denominator reconciliation line (#2); model named in
the 55.61%-refusal stat (#3, it is Llama2-13b, not GPT-family); "wherever measured" →
instrument-bound (#4); community-unit denominator fixed to the deep-scored subset (#6);
"Determinism as misalignment" retitled "…on contested items" (#8); the ~85% consensus line
registered as convention, consistent with KB01 Adjudication 1 (#9); Boddington/MEC stem +
renormalization checked (verification list, #10); "as of 2026-01" dates on KB13/overview
perishables (#11/#13/#18); §5 caveat block names the RV same-vendor caveat explicitly
(#15); "converged on one pipeline" → "dominant shape with named divergences" (#16);
Stiennon 10×-vs-5× card check (verification list, #17). #12 (CCAI↔Sycophancy stem
conflation in two docs) → cross-check against the completed 2026-07-06 card rename; these
two references are likely the residue the 7-citation fix missed — verify and fix.

## The fix vehicle (one Opus session)

1. New file `00-KNOWLEDGEBASE/20260707-kb-addendum-fable-assessment.md`: the CS-1/2/3/5
   rulings verbatim, X2-probe operationalization, MDES mandate, robustness-envelope rename,
   primary-divergence rule, ~85% and 40%-live-fraction registered as conventions.
   KB01 + KB04 headers get a one-line pointer.
2. In-place point fixes with a changelog line per doc (KB docs are living, not dated
   reports): the four SUPERSEDED banners; KB09 caveats; KB10 VOID table + 45/47; the MINOR
   list above.
3. **Verification list (WS-5-style, cheap):** NurValues card vs source; Stiennon 1.3B/6.7B
   multiplier; Boddington/MEC stem; ConflictScope 1.7→4.5 + Snoswell 96/3 (KB02 headliners);
   CCAI-rename residue in KB13 + overview.

After this pass, the KB layer is fit to serve as the grounding for post-window builders —
which it currently is NOT for anyone who reads a §6 brief as spec.
