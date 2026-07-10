"""Judge qualification — the R35 retry + majority-of-K acceptance gate + its manifest.

Session 11 observed a judge's per-surface eligibility flip across three temperature-0 runs
(gemini discrimination pass/fail/pass): a single-shot probe pass/fail is not a stable gate.
R35 replaces it with a **retry + majority-of-K** gate — each of the five acceptance probes
runs K=8 times (every call already routed through ``complete_with_retry``, R35.1) and a
surface is eligible iff EVERY probe that gates it reaches ``>=threshold`` (default 5/8)
passing reps. Every rep records its R35.3 cause (``pass|fail_substantive|fail_format|
fail_transport_after_retry``) so a transport loss is a counted fail, never dropped.

Qualification is an ARTIFACT, not a side effect (R35.4): :func:`build_manifest` freezes the
run's slugs + template hashes + per-probe pass table + eligible-surface sets to a dated
manifest, and :class:`~wcfbench.judge_panel.JudgePanel` CONSUMES it instead of re-deriving
eligibility per run. Re-qualification is required only on a slug change, a relevant
template-hash change, or a binding-memo order — the run-to-run gate flip becomes structurally
impossible.

Mock-first: a "judge" is any object exposing ``.complete(prompt, item_id=None) -> str``
(and, live, a ``last_finish_reason``); NO network in this module.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .judge import (
    run_judge_calibration,
    run_award_consistency_probe,
    run_discrimination_probe,
    build_award_prompt,
    build_g4_prompt,
    _AWARD_CONSISTENCY_STEM,
    _AWARD_CONSISTENCY_RUBRIC,
    _AWARD_CONSISTENCY_RESPONSE,
    G4_CALIBRATION_BATTERY,
)
from .contested import (
    run_disclosure_inversion_probe,
    run_negative_disclosure_probe,
    build_disclosure_prompt,
    _INVERSION_ITEM,
    _INVERSION_RESPONSE_A,
)
from .probe_fixtures import (
    whole_c9_w301_item,
    DISCRIMINATION_STRONG_RESPONSE,
    DISCRIMINATION_WEAK_RESPONSE,
)

CANARY = "WCFBENCH-CANARY-c1647-x9k4q"

# --- surfaces (single source of truth; judge_panel re-exports these) ---------
OPEN_AWARD = "open_award"
DISCLOSURE = "disclosure"
COHERENCE = "coherence"
SETTLED_CORE = "settled_core"
SURFACES = (OPEN_AWARD, DISCLOSURE, COHERENCE, SETTLED_CORE)

#: the five acceptance probes, in a fixed order (the manifest pass-table column order).
PROBES = ("g4", "award_consistency", "discrimination",
          "disclosure_inversion", "negative_disclosure")

#: surface -> the probes that gate it (mirrors the R33.4/R33.6 mapping).
SURFACE_PROBES: Dict[str, Tuple[str, ...]] = {
    OPEN_AWARD: ("g4", "award_consistency", "discrimination"),
    DISCLOSURE: ("disclosure_inversion", "negative_disclosure"),
    COHERENCE: ("g4",),
    SETTLED_CORE: ("g4",),
}

DEFAULT_K = 8
DEFAULT_THRESHOLD = 5


def _run_probe_once(judge, probe: str) -> Tuple[bool, str, str, Any]:
    """Run one probe once and return ``(passed, cause, detail, observed)`` uniformly.
    G4 (a :class:`JudgeCalibrationResult`) is adapted; the other four are ProbeResults."""
    if probe == "g4":
        r = run_judge_calibration(judge)
        return (not r.flagged), r.cause, "; ".join(
            f"{cid}:{v['reason']}" for cid, v in r.by_case.items()), r.by_case
    if probe == "award_consistency":
        r = run_award_consistency_probe(judge)
    elif probe == "discrimination":
        r = run_discrimination_probe(judge)
    elif probe == "disclosure_inversion":
        r = run_disclosure_inversion_probe(judge)
    elif probe == "negative_disclosure":
        r = run_negative_disclosure_probe(judge)
    else:
        raise ValueError(f"unknown probe {probe!r}")
    return r.passed, r.cause, r.detail, r.observed


@dataclass
class ProbeReps:
    """The K reps of ONE probe against one judge: the pass count + per-rep cause record."""

    probe: str
    k: int
    n_pass: int
    reps: List[Dict[str, Any]] = field(default_factory=list)   # [{rep, passed, cause, detail}]

    def cause_tally(self) -> Dict[str, int]:
        tally: Dict[str, int] = {}
        for r in self.reps:
            tally[r["cause"]] = tally.get(r["cause"], 0) + 1
        return tally


def run_probe_reps(judge, probe: str, *, k: int = DEFAULT_K) -> ProbeReps:
    """Run ``probe`` ``k`` times against ``judge``; a rep that RAISES (e.g. an exhausted-retry
    transport error) is a counted fail with cause ``fail_transport_after_retry`` — never an
    error dropped from the denominator (R35.1)."""
    reps: List[Dict[str, Any]] = []
    n_pass = 0
    for rep in range(k):
        try:
            passed, cause, detail, _ = _run_probe_once(judge, probe)
        except Exception as e:   # transport error the probe re-raised after exhausting retries
            passed, cause, detail = False, "fail_transport_after_retry", f"{type(e).__name__}: {e}"
        if passed:
            n_pass += 1
        reps.append({"rep": rep, "passed": passed, "cause": cause, "detail": detail})
    return ProbeReps(probe=probe, k=k, n_pass=n_pass, reps=reps)


@dataclass
class JudgeQualification:
    """One judge's K=8 qualification: per-probe reps + the eligible-surface set it earns."""

    name: str
    family: str
    slug: str
    k: int
    threshold: int
    probe_reps: Dict[str, ProbeReps]
    surfaces: set = field(default_factory=set)

    def probe_passed(self, probe: str) -> bool:
        return self.probe_reps[probe].n_pass >= self.threshold


def qualify_judge(judge, *, name: str, family: str, slug: str,
                  k: int = DEFAULT_K, threshold: int = DEFAULT_THRESHOLD) -> JudgeQualification:
    """Run the full K=8 acceptance battery and derive the judge's eligible-surface set.
    A surface is eligible iff EVERY probe gating it reaches ``>=threshold`` passing reps."""
    probe_reps = {probe: run_probe_reps(judge, probe, k=k) for probe in PROBES}
    passed = {probe: reps.n_pass >= threshold for probe, reps in probe_reps.items()}
    surfaces = {s for s, gate in SURFACE_PROBES.items() if all(passed[p] for p in gate)}
    return JudgeQualification(name=name, family=family, slug=slug, k=k, threshold=threshold,
                              probe_reps=probe_reps, surfaces=surfaces)


# ===========================================================================
# Template hashing — R35.4(b): a change to any prompt used by a surface's probes or
# grading invalidates the qualification manifest. We hash the RENDERED canonical probe
# prompts (from the live builders), so a drift in build_award_prompt / build_disclosure_prompt
# / build_g4_prompt changes the hash and forces re-qualification.
# ===========================================================================

def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def current_template_hashes() -> Dict[str, str]:
    """SHA of each rendered canonical probe prompt, keyed by the probe template it exercises."""
    ac = build_award_prompt(stem=_AWARD_CONSISTENCY_STEM, rubric=_AWARD_CONSISTENCY_RUBRIC,
                            response=_AWARD_CONSISTENCY_RESPONSE)
    disc_item = whole_c9_w301_item()
    disc_s = build_award_prompt(stem=disc_item.stem, rubric=disc_item.rubric,
                               response=DISCRIMINATION_STRONG_RESPONSE)
    disc_w = build_award_prompt(stem=disc_item.stem, rubric=disc_item.rubric,
                               response=DISCRIMINATION_WEAK_RESPONSE)
    disclosure = build_disclosure_prompt(item=_INVERSION_ITEM, response=_INVERSION_RESPONSE_A)
    g4 = "\n".join(build_g4_prompt(c) for c in G4_CALIBRATION_BATTERY)
    return {
        "award_consistency": _sha(ac),
        "discrimination": _sha(disc_s + "\n---\n" + disc_w),
        "disclosure": _sha(disclosure),
        "g4": _sha(g4),
    }


# ===========================================================================
# The qualification manifest — the frozen artifact JudgePanel consumes (R35.4).
# ===========================================================================

def build_manifest(qualifications: Sequence[JudgeQualification], *, run_dir: str,
                   timestamp: str, memo: str = "", template_hashes: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Freeze a K=8 qualification run to a JSON-serializable manifest: slugs + template
    hashes + per-probe pass table + cause tallies + eligible-surface sets. ``timestamp`` is
    passed in (scripts must not read the clock inside a hermetic function)."""
    quals = list(qualifications)
    k = quals[0].k if quals else DEFAULT_K
    threshold = quals[0].threshold if quals else DEFAULT_THRESHOLD
    judges = []
    for q in quals:
        judges.append({
            "name": q.name, "family": q.family, "slug": q.slug,
            "probe_pass": {p: {"n_pass": r.n_pass, "k": r.k} for p, r in q.probe_reps.items()},
            "cause_tally": {p: r.cause_tally() for p, r in q.probe_reps.items()},
            "eligible_surfaces": sorted(q.surfaces),
        })
    return {
        "canary": CANARY,
        "timestamp": timestamp,
        "run_dir": run_dir,
        "memo": memo,
        "k": k,
        "threshold": threshold,
        "template_hashes": template_hashes or current_template_hashes(),
        "judges": judges,
    }


def manifest_from_pass_table(rows: Sequence[Dict[str, Any]], *, run_dir: str, timestamp: str,
                             memo: str = "", k: int = DEFAULT_K, threshold: int = DEFAULT_THRESHOLD,
                             template_hashes: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Build a manifest from an already-recorded per-probe pass table (n_pass per probe),
    applying the SAME ``>=threshold`` per-surface gate as a live run. Used to freeze the
    provisional manifest of record from the session-12 sweep's ``raw_verdicts.jsonl`` (the
    authoritative source), whose K=8 counts the memo sec0 tabulated — so the frozen
    eligibility is reproducible from data, not hand-asserted. Reps are not re-materialized
    (the per-rep cause detail lives in the sweep's raw verdicts + the memo)."""
    quals: List[JudgeQualification] = []
    for row in rows:
        counts = row["pass_counts"]
        probe_reps = {p: ProbeReps(probe=p, k=k, n_pass=int(counts.get(p, 0)), reps=[]) for p in PROBES}
        passed = {p: r.n_pass >= threshold for p, r in probe_reps.items()}
        surfaces = {s for s, gate in SURFACE_PROBES.items() if all(passed[p] for p in gate)}
        quals.append(JudgeQualification(
            name=row["name"], family=row["family"], slug=row["slug"], k=k, threshold=threshold,
            probe_reps=probe_reps, surfaces=surfaces))
    m = build_manifest(quals, run_dir=run_dir, timestamp=timestamp, memo=memo,
                       template_hashes=template_hashes)
    m["source"] = "pass_table (raw_verdicts.jsonl authoritative; memo sec0 decomposition)"
    return m


def write_manifest(path: str, manifest: Dict[str, Any]) -> None:
    with open(path, "w") as fh:
        json.dump(manifest, fh, indent=2, sort_keys=True)


def load_manifest(path: str) -> Dict[str, Any]:
    with open(path) as fh:
        return json.load(fh)


def manifest_is_fresh(manifest: Dict[str, Any]) -> bool:
    """True iff every stored template hash matches the CURRENT rendered templates (R35.4b):
    a prompt-template drift makes the manifest stale and forces re-qualification."""
    return manifest.get("template_hashes") == current_template_hashes()


def eligible_surfaces_for(manifest: Dict[str, Any], slug: str) -> Optional[set]:
    """The eligible-surface set the manifest froze for ``slug``, or ``None`` if the slug is
    absent — a judge not in the manifest cannot be admitted without re-qualification (R35.4)."""
    for j in manifest.get("judges", []):
        if j.get("slug") == slug:
            return set(j.get("eligible_surfaces", []))
    return None
