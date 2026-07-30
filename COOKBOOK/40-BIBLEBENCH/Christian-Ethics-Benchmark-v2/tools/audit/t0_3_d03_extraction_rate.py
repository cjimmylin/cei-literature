"""T0-3: design-03 forced-choice extraction rate over stored responses.

Canary: WALKWORTHY-CANARY-7f3e2026

PREMISE CHECK (do this before trusting the anchor)
---------------------------------------------------
The Tier-0 queue (20260730-boot-prompt-v3-tier0-continue.md, T0-3 row) describes design 03
as "forced-choice" and expects a deterministic parser that "extracts the model's chosen
option from raw completion text". That description does NOT match the shipped v2 harness:

  - `walkworthy_inspect/parsers.py` contains exactly one deterministic text-extraction
    surface in the whole package: `parse_allocation_block` / `reparse_allocation_response`
    (parsers.py:68-92, 135-206), and it is wired ONLY to design 05 (ordoamoris), via
    `solvers.py:design05_format_retry_solver` and `scorers.py:design05_scorer`. There is no
    design-03 entry point into parsers.py at all (grep-verified).
  - `scorers.py:579-581` (`design03_scorer`) delegates to the generic
    `_make_model_graded_scorer("03-quiettongue", judge_model)` factory (scorers.py:379-420),
    which sends the SUT's raw completion into an LLM-judge prompt and NEVER parses the SUT's
    text itself. The only "extraction" step in that path is `parse_judge_json`
    (scorers.py:269-293, using the categorical/ordinal coercion helper `_coerce` at
    scorers.py:235-267), and it parses the JUDGE's generated JSON -- not the SUT's completion.

So "the parser extracts the model's chosen option from raw completion text" is FALSE for
this design in this codebase: there is no such parser. What IS true, and is presumably the
origin of the "forced-choice" label: the design-03 SAY administration's prompt template ends
with an explicit instruction "Yes / No / It depends + one sentence."
(datasets/public/design03.jsonl, WW-03-A04#say, verified verbatim) -- a forced-choice-shaped
ITEM DESIGN, scored by a judge, not a forced-choice-shaped SCORER.

WHAT THIS SCRIPT ACTUALLY MEASURES (the closest honest analogue, $0/offline)
-----------------------------------------------------------------------------
Tier 0 forbids new judge/model calls, so the judge cannot be re-run. Instead this script
reuses the REAL shipped extraction function -- `parse_judge_json` / `_coerce`
(imported directly from `walkworthy_inspect.scorers`, not reimplemented) -- against the
frozen judge output already stored in the `.eval` logs, in two ways:

  1. Primary count: the ALREADY-COMPUTED `score.value["expressed_judgment"]` field per
     administration (this value is the direct, already-materialized output of
     `parse_judge_json`+`_coerce` at run time -- reading it costs nothing and re-derives
     nothing new).
  2. Reproducibility check: for every administration, `parse_judge_json` is called AGAIN,
     offline, against the frozen judge text stored in `score.explanation`
     (scorers.py:415 stores `judge_text[:400]`), and the result is compared to (1). This
     is the literal "run the shipped extraction function over each stored completion" the
     task asked for -- applied to the only completion design 03's scorer ever parses (the
     judge's), with the important caveat that `explanation` is truncated to 400 chars, so a
     reproduction mismatch can reflect truncation rather than a real discrepancy (flagged
     separately, never silently folded into the failure count).

"Successful extraction" = `expressed_judgment` (the design's one CAT-typed, closed-option
field -- options are exactly ["yes", "no", "it_depends"], rubrics.py:101-102, i.e. the
forced-choice slot) resolves to one of those three options rather than "unscorable"/missing.
`revealed_artifact` and `keypoints_met` are NOT forced-choice fields (revealed_artifact is a
judge assessment of an artifact, keypoints_met is an ordinal bucket) and are reported only as
secondary context, never folded into the extraction-rate denominator.

Zero model/API calls. Reads ONLY the frozen `.eval` logs under
logs/fullbank-3ep-20260724/ep{1,2,3}/{sut}/. No holdout access
(WALKWORTHY_ALLOW_HOLDOUT is never set).

Usage:
    $V2/.venv/bin/python $V2/tools/audit/t0_3_d03_extraction_rate.py
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

CANARY = "WALKWORTHY-CANARY-7f3e2026"

V2_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(V2_ROOT))

from inspect_ai.log import list_eval_logs, read_eval_log  # noqa: E402

# THE shipped extraction function this task requires we reuse (not reimplement).
from walkworthy_inspect.scorers import parse_judge_json, UNSCORABLE  # noqa: E402 (scorers.py:269,56)
from walkworthy_inspect.rubrics import spec_for, judge_categories  # noqa: E402

RUN_ROOT = V2_ROOT / "logs" / "fullbank-3ep-20260724"
SUTS = ["deepseek", "mistral", "gemini", "llama", "gpt41mini"]
EPS = [1, 2, 3]
FORCED_CHOICE_CAT = "expressed_judgment"
FORCED_CHOICE_OPTIONS = ("yes", "no", "it_depends")

spec = spec_for("03-quiettongue")
CATEGORIES = judge_categories(spec)  # [expressed_judgment, revealed_artifact, keypoints_met]


def arm_of(admin: str) -> str:
    if admin.startswith("say"):
        return "say"
    if admin.startswith("do"):
        return "do"
    return "other"


def is_exemplar_admin(meta: dict) -> bool:
    admin = str(meta.get("admin", ""))
    return bool(meta.get("is_exemplar")) or admin.endswith("-exemplar")


def classify_failure(completion: str, value, explanation: str, sc_metadata: dict) -> str:
    """<=15-word neutral reason a forced-choice extraction failed."""
    if not completion or not completion.strip():
        return "empty completion / no SUT output recorded"
    reason = (sc_metadata or {}).get("unscorable_reason")
    if reason == "judge_error":
        return "judge call failed at run time (frozen run artifact, not a SUT issue)"
    if reason == "judge_unparseable":
        return "judge output had no parseable JSON object at all"
    # judge produced JSON, but expressed_judgment specifically didn't coerce.
    if explanation and '"' in explanation:
        return "judge JSON used a synonym key, not expressed_judgment; coercion found no match"
    return "judge output present but expressed_judgment missing/uncoercible (unknown cause)"


def main() -> int:
    # rows[(sut, ep, arm, exemplar_bucket)] = {"n": int, "success": int}
    rows = defaultdict(lambda: {"n": 0, "success": 0})
    completion_empty = []
    reproduction_mismatches = []
    failures = []
    n_total = 0
    n_logs_seen = 0

    for ep in EPS:
        for sut in SUTS:
            d = RUN_ROOT / f"ep{ep}" / sut
            if not d.exists():
                print(f"WARNING: missing directory {d}")
                continue
            found_d03 = False
            for li in list_eval_logs(str(d)):
                log = read_eval_log(li.name)
                if "design03" not in log.eval.task:
                    continue
                found_d03 = True
                n_logs_seen += 1
                samples = log.samples or []
                for s in samples:
                    n_total += 1
                    meta = s.metadata or {}
                    admin = str(meta.get("admin", ""))
                    item_id = meta.get("item_id") or s.id
                    arm = arm_of(admin)
                    exemplar = is_exemplar_admin(meta)

                    completion = s.output.completion if s.output else ""
                    if not completion or not completion.strip():
                        completion_empty.append((sut, ep, item_id, admin))

                    sc = next(iter((s.scores or {}).values()), None)
                    value = sc.value if sc else None
                    explanation = (sc.explanation or "") if sc else ""
                    sc_meta = (sc.metadata or {}) if sc else {}

                    ej = value.get(FORCED_CHOICE_CAT) if isinstance(value, dict) else None
                    success = ej in FORCED_CHOICE_OPTIONS

                    # Reproducibility check: re-run the SHIPPED extraction function against
                    # the frozen, stored judge text (score.explanation). Offline, no model
                    # call -- parse_judge_json is pure text/JSON parsing. scorers.py:410-411
                    # substitutes None -> UNSCORABLE ("unscorable") AFTER parse_judge_json
                    # returns, so apply the identical substitution here before comparing --
                    # otherwise every None-vs-"unscorable" pair would misreport as a
                    # reproduction failure when it is exactly the shipped pipeline's own
                    # documented post-processing step.
                    reparsed = parse_judge_json(explanation, CATEGORIES) if explanation else None
                    raw_reparsed_ej = reparsed.get(FORCED_CHOICE_CAT) if reparsed else None
                    reparsed_ej = raw_reparsed_ej if raw_reparsed_ej is not None else UNSCORABLE
                    if reparsed_ej != ej:
                        reproduction_mismatches.append(
                            (sut, ep, item_id, admin, ej, reparsed_ej,
                             len(explanation) >= 400)  # likely truncation if at/over cap
                        )

                    key_all = (sut, ep, arm, "all")
                    rows[key_all]["n"] += 1
                    if success:
                        rows[key_all]["success"] += 1
                    if not exemplar:
                        key_ne = (sut, ep, arm, "nonexemplar")
                        rows[key_ne]["n"] += 1
                        if success:
                            rows[key_ne]["success"] += 1

                    if not success:
                        failures.append((
                            sut, ep, item_id, admin, exemplar,
                            classify_failure(completion, value, explanation, sc_meta),
                        ))
            if not found_d03:
                print(f"WARNING: no design03 log found under {d}")

    print("=" * 100)
    print("  T0-3 -- design-03 (quiettongue) forced-choice (expressed_judgment) extraction rate")
    print("=" * 100)
    print(f"  canary: {CANARY}")
    print(f"  shipped extraction fn reused: walkworthy_inspect.scorers.parse_judge_json "
          f"(scorers.py:269), _coerce (scorers.py:235)")
    print(f"  forced-choice category: {FORCED_CHOICE_CAT} options={FORCED_CHOICE_OPTIONS}")
    print(f"  run root: {RUN_ROOT}")
    print(f"  total design-03 samples read (incl. exemplar): {n_total} "
          f"(expected 5 suts x 3 eps x 66 = 990)")
    print(f"  design-03 .eval logs found: {n_logs_seen} (expected 15)")
    print()

    # --- non-exemplar table, per (sut, epoch), all-arms + say/do split -------------
    print("-" * 100)
    print("NON-EXEMPLAR -- per (sut, epoch): n, success, rate -- all-arms, then say/do split")
    print("-" * 100)
    header = (f"{'sut':10} {'ep':3} {'n_all':>6} {'ok_all':>7} {'rate_all':>9}  "
              f"{'n_say':>6} {'ok_say':>7} {'rate_say':>9}  "
              f"{'n_do':>6} {'ok_do':>7} {'rate_do':>8}")
    print(header)
    overall_n = 0
    overall_ok = 0
    cell_min = (None, 2.0)
    for ep in EPS:
        for sut in SUTS:
            n_say = rows[(sut, ep, "say", "nonexemplar")]["n"]
            ok_say = rows[(sut, ep, "say", "nonexemplar")]["success"]
            n_do = rows[(sut, ep, "do", "nonexemplar")]["n"]
            ok_do = rows[(sut, ep, "do", "nonexemplar")]["success"]
            n_all = n_say + n_do
            ok_all = ok_say + ok_do
            rate_all = ok_all / n_all if n_all else float("nan")
            rate_say = ok_say / n_say if n_say else float("nan")
            rate_do = ok_do / n_do if n_do else float("nan")
            overall_n += n_all
            overall_ok += ok_all
            if n_all and rate_all < cell_min[1]:
                cell_min = (f"{sut}/ep{ep}", rate_all)
            print(f"{sut:10} {ep:3} {n_all:6} {ok_all:7} {rate_all:9.4f}  "
                  f"{n_say:6} {ok_say:7} {rate_say:9.4f}  "
                  f"{n_do:6} {ok_do:7} {rate_do:8.4f}")
    print("-" * 100)
    overall_rate = overall_ok / overall_n if overall_n else float("nan")
    print(f"OVERALL non-exemplar: n={overall_n} success={overall_ok} rate={overall_rate:.4f}")
    print(f"Minimum per-(sut,epoch) all-arm cell: {cell_min[0]} rate={cell_min[1]:.4f}")
    print(f"Any cell below 0.95: "
          f"{'YES' if cell_min[1] < 0.95 else 'NO'}")
    print()

    # --- ep1 anchor check ------------------------------------------------------------
    print("-" * 100)
    print("EP1 ANCHOR CHECK (boot prompt expects ~145/145 -- confirm or correct)")
    print("-" * 100)
    ep1_say_n = sum(rows[(sut, 1, "say", "nonexemplar")]["n"] for sut in SUTS)
    ep1_say_ok = sum(rows[(sut, 1, "say", "nonexemplar")]["success"] for sut in SUTS)
    ep1_all_n = sum(rows[(sut, 1, arm, "nonexemplar")]["n"] for sut in SUTS for arm in ("say", "do"))
    ep1_all_ok = sum(rows[(sut, 1, arm, "nonexemplar")]["success"] for sut in SUTS for arm in ("say", "do"))
    print(f"  ep1 SAY-arm non-exemplar (5 suts x 29 items): n={ep1_say_n} success={ep1_say_ok} "
          f"({ep1_say_ok}/{ep1_say_n} = {ep1_say_ok/ep1_say_n:.4f})")
    print(f"  ep1 ALL-arm non-exemplar (5 suts x 58 admins): n={ep1_all_n} success={ep1_all_ok} "
          f"({ep1_all_ok}/{ep1_all_n} = {ep1_all_ok/ep1_all_n:.4f})")
    print(f"  Anchor '~145/145' matches the SAY-arm-only, non-exemplar count "
          f"(29 say admins x 5 suts = 145).")
    print(f"  Anchor {'CONFIRMED' if ep1_say_ok == ep1_say_n else 'CORRECTED'}: "
          f"actual is {ep1_say_ok}/{ep1_say_n}.")
    print()

    # --- exemplar-inclusive appendix ---------------------------------------------------
    print("-" * 100)
    print("APPENDIX -- exemplar-INCLUSIVE counts, per (sut, epoch), all-arms")
    print("-" * 100)
    print(f"{'sut':10} {'ep':3} {'n_all_incl':>11} {'ok_all_incl':>12} {'rate':>8}")
    incl_n_total = 0
    incl_ok_total = 0
    for ep in EPS:
        for sut in SUTS:
            n = rows[(sut, ep, "say", "all")]["n"] + rows[(sut, ep, "do", "all")]["n"]
            ok = rows[(sut, ep, "say", "all")]["success"] + rows[(sut, ep, "do", "all")]["success"]
            rate = ok / n if n else float("nan")
            incl_n_total += n
            incl_ok_total += ok
            print(f"{sut:10} {ep:3} {n:11} {ok:12} {rate:8.4f}")
    print("-" * 100)
    print(f"OVERALL exemplar-inclusive: n={incl_n_total} success={incl_ok_total} "
          f"rate={incl_ok_total/incl_n_total:.4f}")
    n_exemplar_admins = incl_n_total - overall_n
    print(f"Exemplar admin count (all/eps/suts): {n_exemplar_admins} "
          f"(expected 8 per sut-epoch x 15 cells = 120)")
    print()

    # --- empty completions -------------------------------------------------------------
    print("-" * 100)
    print(f"EMPTY / MISSING COMPLETIONS: {len(completion_empty)} of {n_total} total samples")
    print("-" * 100)
    for sut, ep, item_id, admin in completion_empty:
        print(f"  EMPTY  sut={sut} ep={ep} item={item_id} admin={admin}")
    print()

    # --- reproducibility check ----------------------------------------------------------
    print("-" * 100)
    print(f"REPRODUCIBILITY CHECK: re-running parse_judge_json on stored score.explanation")
    print(f"  mismatches vs stored score.value: {len(reproduction_mismatches)} of {n_total}")
    print("-" * 100)
    for sut, ep, item_id, admin, stored, reparsed, likely_trunc in reproduction_mismatches:
        print(f"  MISMATCH sut={sut} ep={ep} item={item_id} admin={admin} "
              f"stored={stored!r} reparsed={reparsed!r} "
              f"likely_truncation={likely_trunc}")
    print()

    # --- failed-extraction case list -----------------------------------------------------
    print("-" * 100)
    print(f"FAILED-EXTRACTION CASES (forced-choice expressed_judgment != yes/no/it_depends): "
          f"{len(failures)}")
    print("-" * 100)
    for sut, ep, item_id, admin, exemplar, reason in failures:
        tag = "EXEMPLAR" if exemplar else "non-exemplar"
        print(f"  FAIL sut={sut} ep={ep} item={item_id} admin={admin} [{tag}] :: {reason}")
    print()
    print(f"canary: {CANARY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
