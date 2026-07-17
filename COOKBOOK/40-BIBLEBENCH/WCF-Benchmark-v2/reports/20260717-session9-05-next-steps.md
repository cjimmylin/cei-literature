# WCF-Benchmark-v2 — Session 9, Report 5 of 6: Next Steps & Scale-Up Readiness

_Internal owner-briefing · decision-support · Christian-Ethics-Benchmark-v2_

> **EXPLORATORY / NON-QUOTABLE.** Scores are 0–100 panel-median rubric conformity, not accuracy; bank versions are separate instruments. This report proposes next steps; it authorizes no spend — any live OpenRouter run needs explicit owner approval.

---

## 0. Readiness verdict — lead with it

**We are ready to scale up on frozen bank v2.4.** The three things that gate a
credible leaderboard run — the instrument, the judge, and the run mechanics —
are all in a shipped, validated, tested state. What is *not* yet resolved is
purely a question of statistical resolution *within* the top tier, and that is
bought with more per-item information (epochs / harder-core items), not with
more scale-up decisions. Nothing below blocks a go.

| Pillar | State | Verdict |
|---|---|---|
| **Instrument** | FROZEN at bank v2.4 — 265 main + 22 episodes; frontier core = 66 `-N-` items; 80/80 pinned tests green | **READY** |
| **Judge** | FIXED = panel-3 median(gemini-2.5-flash, deepseek-chat, mistral-small-2603); s8 meta-judging audit validated it (external OAuth judges corroborate the headline sign, see a *larger* gap → panel is conservative, not inflationary; ICC(2,k) 0.798; no kin favoritism) | **READY** — standing caveats intact |
| **Scale-up mechanics** | Runbook exists: 16-SUT longlist, ~$53 full-roster estimate, live-verified prices, exact commands, GO/NO-GO gates; frontier-core epochs×3 power strategy VALIDATED (MDD80 dropped to 3.95–5.41) | **READY** |
| **Statistical resolution (within tier-1)** | Adjacent top orderings not yet separable at current power — the minimax-m3 ↔ gpt-5-mini dead heat (+1.24, ns, MDD80 5.78) is the type case; fix is per-item info, not more SUTs | **KNOWN LIMIT — not a blocker** |

**In one paragraph.** The benchmark is scale-up-ready. The instrument is frozen
and tested; the judge is fixed and has now survived an out-of-benchmark
meta-audit that, if anything, says the incumbent panel *understates* the effect
that matters; and the run mechanics (roster, prices, commands, gates, power
strategy) are written down and validated. The only open technical question —
which of the very top models actually leads — is a resolution problem inside
tier-1, and the s8 minimax addendum showed that the lever for it is more
epochs or a harder core, not adding SUTs to the roster. So the roster run can
proceed now; the top-of-tier tie-break is a separate, later, item-side probe.

---

## 1. The fixed-judge question, explicitly

**Yes — the judge is fixed.** Scoring is done by the **panel-3 median of
gemini-2.5-flash + deepseek-chat + mistral-small-2603**. This is not under
review for the scale-up; it is the instrument.

The Session-8 meta-judging audit (report #4 in this batch;
`reports/20260717-session8-meta-judging-report.md`, §8) ran two fully
independent, out-of-benchmark OAuth judges — J4 (claude-opus-4-8) and J5
(gpt-5.5) — as **audit instruments only**, never joining the panel. Its
recommendation for v2.5+, stated here in meaning:

- **Keep the panel-3 median** as the scoring instrument. Both independent
  judges corroborate the *sign* of the headline (gpt-5-mini > claude-haiku-4.5
  on the frontier core), and both see a *larger* gap than the panel (J4 alone
  19.65, J5 alone 14.55, vs panel-3 5.90; 5-judge median 9.25, SIG). The panel
  is **conservative, not inflationary**, about the finding that matters.
- **Do not merge the OAuth judges into the panel.** They stay independent audit
  instruments (config-break rule); their entire value is their independence.
- **No kin-exclusion rule is needed for the current SUT set** — the audit found
  no favoritism-direction signal (cross-kin τ̂ = -5.10, read directionally, on
  the anti-kin side; each judge grades its own kin relatively *harsher*).
  **But re-audit** if an Anthropic-family or OpenAI-family model is ever added
  to the **scoring panel itself** (as opposed to the SUT roster).

Reliability backing: five-judge ICC(2,k) overall = 0.798; incumbent
gemini~deepseek ρ = 0.829; J4~J5 ρ = 0.849. The panel is a defensible fixed
instrument to scale on.

---

## 2. Gaps to close before the leaderboard paper

None of these block starting a scale-up run; they are the items that must be
resolved before a *leaderboard* is locked and a *paper* is drafted.

| Gap | Why it matters | Rough cost | Owner decision needed? |
|---|---|---|---|
| **Full v2.4 leaderboard with the deepseek + gpt-4o-mini anchors re-run at v2.4 scale** | These anchors bridge earlier pilots to the frozen v2.4 scale but have never been run at v2.4; without them the board has no low/mid anchor row on the current instrument | ~$3 OpenRouter | Part of the scale-up budget authorization (§3, item 1) |
| **Episode re-inclusion flag** — the 9 G4-excluded 4-turn escalation episodes | These are the strongest tier-break instruments in the set (100/100 for haiku + gpt-5-mini vs gpt-4o-mini 42.0 — a 58-pt tier gap); they are preserved and runnable via `wcf_new_episodes`, but re-inclusion changes what the leaderboard measures | run cost folds into the roster run | **YES** — explicit owner decision + tier-break rationale required |
| **Definitive minimax-m3 vs gpt-5-mini resolution** | The top-of-tier ordering is currently a dead heat (+1.24, ns, MDD80 5.78); a leaderboard that names a #1 needs this resolved | more per-item info: **more epochs or harder-core items, NOT more SUTs** | Method choice (epochs vs new items) — can defer to paper stage |
| **NARROW-N-004-style bistable ramp → candidate item class** | The bistable ramp is now characterized across two model families (qwen, gemini), suggesting a purpose-authored item *class*, not a one-off; could sharpen the frontier core | authoring effort (v2.5) | Tied to the v2.5-before-scale-up decision (§3, item 3) |
| **Scale-up SUT selection + kin bookkeeping** | Which of the 16-SUT longlist to actually run, and the kin-disclosure bookkeeping each row carries (gemini-family DiD, deepseek −1.7-pt, mistral +0.97 bound) | selection, not spend | **YES** — the core scale-up decision (§3, item 1) |

> Note: the gpt-4o-mini = 42.0 escalation-episode anchor (a 58-pt tier gap under
> the 4-turn ramps, vs 100/100 for haiku + gpt-5-mini) is confirmed in
> `reports/20260716-session6-report.md`. Like all figures here it is
> EXPLORATORY / NON-QUOTABLE and version-scoped to the v2.3 gate run.

---

## 3. Pending owner decisions

- **Scale-up SUT set + budget authorization.** Which of the 16-SUT longlist to
  run and at what ceiling. Full default roster ≈ **$53** SUT+grading; the
  deepseek + gpt-4o-mini anchor re-run adds ~$3. Trimmable by dropping the
  OPTIONAL/frontier-duplicate rows. **No live run proceeds without this.**
- **Episode re-inclusion.** Include the 9 G4-excluded 4-turn escalation
  episodes (strong tier-break instruments, runnable via `wcf_new_episodes`) —
  yes/no, plus the tier-break rationale if yes.
- **v2.5 authoring before scale-up, or scale-up on frozen v2.4?** Either author
  a v2.5 (e.g. a NARROW-N-004-style bistable-ramp item class) first, or run the
  roster on the already-frozen, already-tested v2.4. Both are defensible; v2.4
  is ready now.
- **Paper venue / framing.** Deferral is fine — the design + evaluation +
  meta-judging reports in this batch are already the paper's spine; venue and
  framing can wait until the leaderboard is locked.
- **Reporting-session scope — RESOLVED.** This batch of 6 owner-briefing
  reports is the resolution of the reporting-session scope itself; no further
  reporting decision is pending.

---

## 4. Recommended sequence

If the goal is to move toward the benchmark-design + leaderboard paper, the path
is:

1. **Authorize the scale-up SUT set + budget** (§3, item 1) — pick the roster
   from the 16-SUT longlist, set the ceiling, include the deepseek + gpt-4o-mini
   anchor re-run (~$3).
2. **Run frozen v2.4** across the roster: full-bank mean (tier-level ranking,
   MDD80 ~2–3.5) **plus** frontier-core **epochs×3** (within-tier-1 ranking,
   MDD80 3.95–5.41). Keep main and episodes as separate eval-sets (the `-T`
   gotcha); per-run audits (unscored=0, panel quorum, `<think>` prevalence,
   dated log dirs) per the runbook §4.
3. **Decide episode re-inclusion** (§3, item 2) with tier-break rationale; run
   `wcf_new_episodes` if yes.
4. **Lock the leaderboard** — full-bank + frontier-core + (optionally)
   standalone escalation panel, each with `bank_version` / panel / parser
   citations and every kin disclosure attached to its row. Resolve the
   minimax-vs-gpt-5-mini tie-break here if a named #1 is wanted (more epochs or
   a harder core).
5. **Draft the paper** from the design + evaluation + meta-judging reports in
   this batch (reports #1–#4 and #6), plus this next-steps report as the
   decision log.

---

## Bottom line

**The instrument, the judge, and the run mechanics are all READY: WCF-Benchmark-v2 can scale up on frozen bank v2.4 the moment the owner authorizes the SUT set and budget — the only unresolved question is a within-tier-1 tie-break that is a later item-side probe, not a scale-up blocker.**

---

_Verified against: `reports/20260717-session8-meta-judging-report.md` (§8 recommendation + limitations), `reports/20260716-session6-scaleup-runbook.md`, `reports/20260717-session8-minimax-epochs-addendum.md`, `reports/20260716-session7-report.md`. Bank v2.4 · panel median(gemini-2.5-flash, deepseek-chat, mistral-small-2603) · last-match GRADE: N parser. EXPLORATORY / NON-QUOTABLE throughout._
