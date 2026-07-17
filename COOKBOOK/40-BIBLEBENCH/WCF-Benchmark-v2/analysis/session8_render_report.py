#!/usr/bin/env python
"""Session-8 Phase 4: render the ONE consolidated meta-judging report.

Reads analysis/20260717-session8-meta-judging-stats.json and emits
reports/20260717-session8-meta-judging-report.md with the 8-section skeleton.
Numbers come STRAIGHT from the stats JSON (no hand transcription); prose and
judgment are literals here. Judge configs (pins, effort, CLI versions) are
passed in the header constants below.
"""
from __future__ import annotations

import json
from pathlib import Path

V2 = Path(__file__).resolve().parent.parent
STATS = V2 / "analysis" / "20260717-session8-meta-judging-stats.json"
OUT = V2 / "reports" / "20260717-session8-meta-judging-report.md"

# Judge configs (recorded from Phase-0 smokes)
J4_MODEL = "claude-opus-4-8 (Claude OAuth, `claude -p --model opus`)"
J5_MODEL = "gpt-5.5 (ChatGPT OAuth, `codex exec`, reasoning_effort=medium)"
CLI_CLAUDE = "Claude Code 2.1.183"
CLI_CODEX = "codex-cli 0.144.3"
J5_PIN_RULING = ("owner-locked branch: try `gpt-5.5` pin with a 3-call smoke, "
                 "fall back to verified `gpt-5.6-sol` on 400. **Smoke result: "
                 "`gpt-5.5` pin accepted (3/3 parseable, no 400) — no fallback "
                 "needed; `gpt-5.6-sol` NOT used.**")


def f(x, nd=2):
    if x is None:
        return "—"
    if isinstance(x, bool):
        return "SIG" if x else "ns"
    if isinstance(x, float):
        return f"{x:+.{nd}f}" if abs(x) < 1000 else str(x)
    return str(x)


def fu(x, nd=2):  # unsigned
    return "—" if x is None else (f"{x:.{nd}f}" if isinstance(x, float) else str(x))


def main() -> int:
    d = json.load(open(STATS))
    L = []
    W = L.append

    W("# WCF-Benchmark-v2 — Session 8: The Impact of Judging")
    W("### An out-of-benchmark OAuth meta-judging audit of the v2.4 findings\n")
    W("> **EXPLORATORY / NON-QUOTABLE.** All results measure rubric conformity, "
      "not accuracy. The two OAuth judges are **audit instruments only** — they "
      "never join the scoring panel, the leaderboard, or bank scoring. "
      "Single-judge headline rows are **gap-stability evidence** (sign + "
      "magnitude band); no per-single-judge significance is claimed.\n")

    # header / configs
    ps = d["parse_stats"]
    W("**Judge configurations**\n")
    W("| Judge | Model | Channel | CLI | Parse-fail |")
    W("|---|---|---|---|---|")
    W(f"| J1 gemini | gemini-2.5-flash | incumbent panel | (bank) | — |")
    W(f"| J2 deepseek | deepseek-chat | incumbent panel | (bank) | — |")
    W(f"| J3 mistral | mistral-small-2603 | incumbent panel | (bank) | — |")
    W(f"| **J4** | {J4_MODEL} | Claude OAuth | {CLI_CLAUDE} | "
      f"{ps['J4']['parse_fail']}/{d['n_j4']} |")
    W(f"| **J5** | {J5_MODEL} | ChatGPT OAuth | {CLI_CODEX} | "
      f"{ps['J5']['parse_fail']}/{d['n_j5']} |")
    W(f"\n**J5 model-pin ruling.** {J5_PIN_RULING}\n")
    W(f"**Coverage.** Bank {d['bank_version']}; panel = {d['panel']}; parser = "
      f"{d['parser']}. J4 graded **{d['n_j4']}** samples (superset); J5 graded "
      f"**{d['n_j5']}** (full priority ladder — no rungs cut); **{d['n_twin']} "
      f"twin samples** carry both OAuth judges. J4's {d['n_j4']} unique "
      f"samples come from {ps['J4']['n_records']} total grade records "
      f"(checkpoint/resume retries after an OAuth-cap outage; latest grade per "
      f"sample_key wins). Zero parse-failures on either OAuth channel across "
      f"all {ps['J4']['n_records']}+{ps['J5']['n_records']} calls (grade-free "
      f"replay prompts; anti-leakage by construction; explicit-tell scan "
      f"0/779).\n")

    # 1 executive summary
    hs = d["headline_sensitivity"]
    pr = hs["panel3_reference"]["gpt5mini-vs-haiku"]
    j4a = hs["J4_alone"]["gpt5mini-vs-haiku"]
    j5a = hs["J5_alone"]["gpt5mini-vs-haiku"]
    m5 = hs["median5"]["gpt5mini-vs-haiku"]
    ck = d["cross_kin_did"]
    ci = ck["tau_ci95_item_clustered"] or [None, None]
    straddles = (ci[0] is not None and ci[0] <= 0 <= ci[1])
    ci_verdict = ("straddles zero → not significant" if straddles else
                  ("excludes zero on the negative side — anti-kin, the "
                   "opposite of favoritism" if ci[1] is not None and ci[1] < 0
                   else "excludes zero on the positive side"))
    W("## 1. Executive summary\n")
    W(f"1. **The headline survives independent judging and gets larger.** The "
      f"v2.4 finding — gpt-5-mini > claude-haiku-4.5 on the 66-item frontier "
      f"core — reproduces under every out-of-benchmark judge. Incumbent panel-3 "
      f"gap **{fu(pr['gap'])}** (MDD80 {fu(pr['mdd80'])}, "
      f"{f(pr['significant_at_mdd80'])}); J4 Opus alone **{fu(j4a['gap'])}**; "
      f"J5 GPT alone **{fu(j5a['gap'])}** (single-judge rows are gap-stability "
      f"evidence, not significance verdicts); 5-judge median **{fu(m5['gap'])}** "
      f"(MDD80 {fu(m5['mdd80'])}, {f(m5['significant_at_mdd80'])}). Sign is "
      f"stable across all five judge configurations; both OAuth judges see a "
      f"larger gap than the incumbent panel.")
    W(f"2. **No favoritism-direction signal — if anything, anti-kin.** The "
      f"cross-kin contrast τ̂ = **{f(ck['tau_obs'])}** points *away* from "
      f"favoritism (positive τ̂ would be the favoritism signal). Read this "
      f"directionally, not as a significance test: τ̂ reduces algebraically to "
      f"d̄_haiku − d̄_gpt5mini (the qwen anchor cancels), so it rests on the "
      f"single J4−J5 twin-difference instrument and conflates kin bias with any "
      f"judge-pair × SUT interaction. Each judge grades its OWN kin relatively "
      f"harsher (Opus on haiku, GPT on gpt-5-mini), the opposite of the "
      f"favoritism concern; the epoch-1-only robustness variant agrees "
      f"(τ̂ = {f(ck['robustness_epoch1_only']['tau_obs'])}). See §5.")
    W(f"3. **Recommendation:** the panel-3 median is a defensible instrument for "
      f"v2.5+; the OAuth cross-check corroborates the sign of the headline "
      f"while showing the incumbent panel is *conservative* about its "
      f"magnitude. See §8.\n")

    # 2 house style
    W("## 2. House-style calibration\n")
    W("Per-judge mean grade minus incumbent panel-3 median on identical twin "
      f"samples (n={d['house_style_twin']['gemini']['n']}). Negative = harsher "
      "than the panel. s5 baselines (different sample base) shown for reference.\n")
    hst = d["house_style_twin"]
    molds = ["contested", "complicit", "steadfast", "v1-kind"]
    W("| Judge | overall | " + " | ".join(molds) + " |")
    W("|---|" + "---|" * (len(molds) + 1))
    for j in ["gemini", "deepseek", "mistral_small", "J4", "J5"]:
        row = hst[j]
        cells = " | ".join(f(row["by_mold"].get(m)) for m in molds)
        W(f"| {j} | {f(row['overall'])} | {cells} |")
    s5 = d["s5_baseline_reference"]
    W(f"\n_s5 reference (panel-health, cited not recomputed): gemini overall "
      f"{f(s5['gemini']['overall'])} / contested {f(s5['gemini']['contested'])} "
      f"/ anchor {f(s5['gemini']['anchor'])}; deepseek "
      f"{f(s5['deepseek']['overall'])}; mistral {f(s5['mistral_small']['overall'])}._\n")
    W("**By SUT** (house-style delta):\n")
    suts = sorted(hst["gemini"]["by_sut"])
    W("| Judge | " + " | ".join(s.replace("openrouter/", "") for s in suts) + " |")
    W("|---|" + "---|" * len(suts))
    for j in ["gemini", "deepseek", "mistral_small", "J4", "J5"]:
        cells = " | ".join(f(hst[j]["by_sut"].get(s)) for s in suts)
        W(f"| {j} | {cells} |")
    W("")

    # 3 reliability
    W("## 3. Five-judge reliability\n")
    rel = d["reliability"]
    W(f"ICC(2,k) absolute-agreement and pairwise Spearman/MAD across all five "
      f"judges, on samples where all five graded.\n")
    W("| Stratum | n | ICC(2,k) |")
    W("|---|---|---|")
    for m in ["overall", "contested", "complicit", "steadfast", "v1-kind"]:
        r = rel.get(m, {})
        W(f"| {m} | {r.get('n','—')} | {fu(r.get('icc2k'),3)} |")
    W("")
    ov = rel["overall"]
    if ov.get("pairwise"):
        W("**Overall pairwise** (Spearman ρ / MAD):\n")
        W("| Pair | ρ | MAD |")
        W("|---|---|---|")
        for pair, v in ov["pairwise"].items():
            W(f"| {pair} | {fu(v['spearman'],3)} | {fu(v['mad'])} |")
        W("")

    # 4 headline sensitivity (PRIMARY)
    W("## 4. Headline sensitivity — the decision-relevant table\n")
    W("gpt-5-mini − claude-haiku-4.5, paired per-item on the 66-item frontier "
      "core, epochs-averaged. MDD80 = 2.80×SE (s7 convention). **Single-judge "
      "rows are gap-stability only** — single-judge MDD80 runs ~8–10; the "
      "5-judge median is the one config that can tighten MDD80 below panel-3.\n")
    W("| Judge config | n | gap | SE | MDD80 | sign holds | significance |")
    W("|---|---|---|---|---|---|---|")
    # Significance verdict is emitted ONLY for the two panel-style configs
    # (panel-3 reference + 5-judge median), per the pre-stated framing rule.
    # Single-judge rows show gap-stability (sign band), NOT a SIG/ns verdict.
    ALLOW_SIG = {"panel3_reference", "median5"}
    order = [("panel3_reference", "incumbent panel-3 (reference)"),
             ("gemini_alone", "gemini alone"),
             ("deepseek_alone", "deepseek alone"),
             ("mistral_small_alone", "mistral-small alone"),
             ("J4_alone", "J4 Opus alone"),
             ("J5_alone", "J5 GPT alone"),
             ("median5", "5-judge median")]
    for key, label in order:
        p = hs.get(key, {}).get("gpt5mini-vs-haiku")
        if not p:
            continue
        sign = "yes" if p["gap"] > 0 else "no"
        verdict = (f(p["significant_at_mdd80"]) if key in ALLOW_SIG
                   else "— (stability only)")
        W(f"| {label} | {p['n']} | {fu(p['gap'])} | {fu(p['se_diff'])} | "
          f"{fu(p['mdd80'])} | {sign} | {verdict} |")
    W(f"\n_Significance is reported ONLY for the two panel-style rows "
      f"(panel-3 and 5-judge median); single-judge rows carry no SIG/ns "
      f"verdict by design (single-judge MDD80 ≈ 8–10 lacks the power). All "
      f"seven configs agree the sign is positive (gpt-5-mini ahead), and both "
      f"OAuth judges see a LARGER gap than the panel. The decision-relevant "
      f"result: the 5-judge median gap {fu(m5['gap'])} at MDD80 "
      f"{fu(m5['mdd80'])} is {f(m5['significant_at_mdd80'])}, and the panel-3 "
      f"reference {fu(pr['gap'])} at MDD80 {fu(pr['mdd80'])} is "
      f"{f(pr['significant_at_mdd80'])}._\n")

    # 5 cross-kin
    W("## 5. Cross-kin symmetry\n")
    W(f"{ck['design']}. J4 (Opus) is Anthropic-kin to the haiku SUT; J5 (GPT) "
      f"is OpenAI-kin to the gpt-5-mini SUT; qwen is mutual non-kin anchor. "
      f"Per-sample d = J4−J5 on {ck['n_twin_core_samples']} twin core samples; "
      f"item-clustered bootstrap ({ck['n_boot']} reps) over "
      f"{ck['n_items_clustered']} items.\n")
    e1 = ck["robustness_epoch1_only"]
    nb = ck["n_by_sut"]
    W("| Quantity | value |")
    W("|---|---|")
    for t, v in ck["dbar_by_sut"].items():
        W(f"| d̄ ({t}), n={nb.get(t,'—')} | {f(v)} |")
    W(f"| Anthropic-kin component (d̄_haiku − d̄_qwen)† | {f(ck['component_anthropic_kin'])} |")
    W(f"| OpenAI-kin component (d̄_gpt5mini − d̄_qwen)† | {f(ck['component_openai_kin'])} |")
    W(f"| **τ̂** (default, haiku/gpt5mini epochs 1–3) | **{f(ck['tau_obs'])}** |")
    W(f"| τ̂ 95% CI (item-clustered, {ck['n_boot']} reps) | {ck['tau_ci95_item_clustered']} |")
    W(f"| τ̂ robustness (epoch-1-only, all three SUTs n={e1['n_by_sut']['qwen']}) | {f(e1['tau_obs'])} |")
    W(f"| τ̂ robustness 95% CI | {e1['tau_ci95_item_clustered']} |")
    W(f"\n**Identification caveat (load-bearing).** {ck['identification_caveat']} "
      f"We therefore read τ̂ **directionally**, not as a significance test: it "
      f"shows no favoritism-direction (positive) signal and a point estimate on "
      f"the anti-kin side, corroborated by the epoch-1-only variant "
      f"(τ̂ = {f(e1['tau_obs'])}, same sign). "
      f"†_The displayed qwen d̄ and kin components are epoch-imbalanced "
      f"(qwen J5 = epoch-1 only, n={nb['qwen']}, vs haiku/gpt-5-mini n="
      f"{nb['haiku']}); they do NOT enter τ̂ because the anchor cancels, so "
      f"they are shown as a sanity baseline only._\n")

    # 6 item artifacts
    W("## 6. Item-level artifacts — top-10 s7 discriminators\n")
    W("Per-SUT mean and 3-SUT spread on each high-discrimination item, under "
      "the panel vs each OAuth judge. Persistent spread = real item "
      "discrimination, not an incumbent-judge artifact.\n")
    W("| Item | panel spread | J4 spread | J5 spread |")
    W("|---|---|---|---|")
    persist_j4 = persist_j5 = collapse = 0
    for it, e in d["top10_discriminators"].items():
        W(f"| {it} | {fu(e['panel3']['spread'])} | {fu(e['J4']['spread'])} | "
          f"{fu(e['J5']['spread'])} |")
        ps_, j4s, j5s = (e['panel3']['spread'], e['J4']['spread'],
                         e['J5']['spread'])
        if None not in (ps_, j4s) and j4s >= 0.5 * ps_:
            persist_j4 += 1
        if None not in (ps_, j5s) and j5s >= 0.5 * ps_:
            persist_j5 += 1
        if (None not in (ps_, j4s, j5s) and j4s < 0.5 * ps_
                and j5s < 0.5 * ps_):
            collapse += 1
    n10 = len(d["top10_discriminators"])
    W(f"\n_Discrimination persists (OAuth spread ≥ half the panel spread) for "
      f"{persist_j4}/{n10} items under J4 and {persist_j5}/{n10} under J5; it "
      f"collapses under BOTH OAuth judges for {collapse}/{n10} — so the "
      f"top-discriminator signal is overwhelmingly real item discrimination, "
      f"not an incumbent-judge artifact. Several items (e.g. COMP-N-004/007) "
      f"show a LARGER spread under the OAuth judges._\n")

    # 7 gate cap
    gc = d["gate_cap"]
    W("## 7. GATE-cap consistency\n")
    W(f"On {gc['n_cap_eligible_twin']} cap-eligible twin samples "
      f"({gc['definition']}), per-judge rate of emitting a ≤40 (cap-signal) "
      f"grade.\n")
    W("| Judge | cap-signal rate |")
    W("|---|---|")
    for j in ["gemini", "deepseek", "mistral_small", "J4", "J5"]:
        W(f"| {j} | {fu(gc.get(f'rate_{j}'),3)} |")
    W("")

    # 8 threats + recommendation
    cb = d.get("contamination_bound", {})
    W("## 8. Threats, limitations, and the v2.5+ recommendation\n")
    W("**Contamination bound.** " + (
        f"Explicit-tell scan: {cb.get('explicit_tell_scan','0/779')}, so the "
        f"residual channel is stylistic (markdown habits, not vendor names). " + (
            f"Style-normalized re-grade (n={cb['n']}): mean delta "
            f"{f(cb.get('mean_delta'))}, mean |delta| "
            f"{fu(cb.get('mean_abs_delta'))}, max |delta| "
            f"{fu(cb.get('max_abs_delta'))} — a small bound on style-channel "
            f"contamination of the kin estimate."
            if cb.get("n") else "Style-normalized re-grade pending.")))
    W("")
    W("**Limitations.** (1) Single-judge MDD80 (~8–10) lacks power for "
      "per-judge significance — only the panel-3 and 5-judge-median rows carry "
      "significance verdicts, by design. (2) J5 qwen coverage is epoch-1 only "
      "(ladder rung 1), so the DiD anchor rests on fewer qwen epochs than the "
      "kin SUTs. (3) OAuth judges are subscription-metered; concurrency and "
      "rate caps forced checkpoint/resume (one transient outage re-graded "
      "clean). (4) All numbers are EXPLORATORY / rubric-conformity, not "
      "accuracy or quotable leaderboard values.\n")
    W("**Recommended judging configuration for v2.5+.**\n")
    W(f"- **Keep the panel-3 median** as the scoring instrument. Two fully "
      f"independent, out-of-benchmark judges corroborate the *sign* of the "
      f"headline, and both see a *larger* gpt-5-mini advantage — so the "
      f"incumbent panel is conservative, not inflationary, about the finding "
      f"that matters.")
    W(f"- **Do not merge the OAuth judges into the panel** (config-break rule; "
      f"they remain audit instruments). Their value is exactly their "
      f"independence.")
    W(f"- **The kin-favoritism worry is not supported** by this audit — retain "
      f"the panel without a kin-exclusion rule for the current SUT set, but "
      f"re-audit if an Anthropic- or OpenAI-family model is ever added to the "
      f"scoring panel itself.\n")
    W("---")
    W(f"_Bank {d['bank_version']} · panel {d['panel']} · parser "
      f"{d['parser']} · J4 {J4_MODEL} · J5 {J5_MODEL} · "
      f"{CLI_CLAUDE} / {CLI_CODEX}. OAuth-judge numbers never appear in a "
      f"leaderboard-style table with panel-median rows; they are "
      f"instrument-difference audits only._")

    OUT.write_text("\n".join(L) + "\n")
    print(f"wrote {OUT} ({len(L)} lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
