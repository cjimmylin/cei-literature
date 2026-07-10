"""Transcript persistence — memo R27 (binding process ruling).

Every live run whose outputs can feed adjudication or G6 **must persist, per
(item × SUT) cell**: the built SUT prompt, the SUT's verbatim response, every judge's
full verdict text (all axis/award calls), the judge-template hash, model slugs, and
timestamps — alongside the summary JSON in the dated run directory.

Rationale (R26 iii is Exhibit A): the suite's first substantive cross-judge split
(AGG-C5-W304 × llama) arrived un-adjudicable because only scores survived. *Scores
identify where judges disagree; only transcripts let anyone decide who is right.* This
is cheap (a few KB per cell) and is a precondition for the gated G1–G7 run and for any
future disagreement adjudication. Run directories are append-only snapshots (report
immutability).

This module turns a :class:`~wcfbench.runner.RunReport` into per-cell transcript
records and writes them as JSONL. It reads the R27 fields the runner + panel now
retain (``PerItemResult.prompt_user`` / ``response_full`` and each judge's
``verdict_texts`` on ``judge_raw``). NO network.
"""

from __future__ import annotations

import hashlib
import json
import os
from typing import Any, Dict, List, Optional


def template_hash() -> str:
    """A stable 16-hex digest of the judge prompt templates (award + numeric axis +
    disclosure anchor). Any change to a template surface changes this hash, so a
    persisted transcript records exactly which judge contract produced it (R27)."""
    from .judge import build_award_prompt, build_judge_prompt
    from .contested import DISCLOSURE_ANCHOR
    from .loader import RubricKeypoint

    kp = [
        RubricKeypoint(points=2.0, criterion="canonical matter keypoint", anchor="WLC Q1", axis="matter"),
        RubricKeypoint(points=1.0, criterion="canonical manner keypoint", anchor="WLC Q135", axis="manner"),
    ]
    award = build_award_prompt(stem="CANON-STEM", rubric=kp, response="CANON-RESPONSE")
    numeric = build_judge_prompt(category="matter", stem="CANON-STEM", rubric=kp, response="CANON-RESPONSE")
    blob = "\x00".join([award, numeric, DISCLOSURE_ANCHOR])
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def _judges_of(result: Any) -> List[Dict[str, Any]]:
    """Extract each judge's identity + full verdict texts from a result's judge_raw."""
    out: List[Dict[str, Any]] = []
    for j in (getattr(result, "judge_raw", None) or []):
        out.append({
            "name": j.get("name"),
            "family": j.get("family"),
            "verdict_texts": list(j.get("verdict_texts", []) or []),
            # keep the parsed numbers alongside the raw text for convenience.
            "scores": {k: v for k, v in j.items()
                       if k not in ("name", "family", "verdict_texts")},
        })
    return out


def build_transcript_records(
    report: Any,
    *,
    template_hash: str,
    timestamp: str,
    run_meta: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """Build one transcript record per (item × SUT) cell from a RunReport (R27).

    Each record carries: the model slug, the item's routing/coordinates, the built SUT
    prompt + verbatim response, every judge's identity + full verdict texts, the refusal
    co-score, the template hash, and the timestamp. ``run_meta`` (judges, suts, canary)
    is merged into every record for provenance.
    """
    records: List[Dict[str, Any]] = []
    meta = dict(run_meta or {})
    for model, rep in report.reports.items():
        for r in rep.results:
            records.append({
                "item_id": r.item_id,
                "model": model,
                "kind": r.kind,
                "design": r.design,
                "commandment": r.commandment,
                "tier": r.tier,
                "track": r.track,
                "sut_prompt": r.prompt_user,
                "sut_response": r.response_full,
                "judges": _judges_of(r),
                "refusal_class": r.refusal_class,
                "refusal_is_failure": r.refusal_is_failure,
                "error": r.error,
                "template_hash": template_hash,
                "timestamp": timestamp,
                **meta,
            })
    return records


def write_run_transcripts(
    report: Any,
    out_dir: str,
    *,
    template_hash: str,
    timestamp: str,
    run_meta: Optional[Dict[str, Any]] = None,
    filename: str = "transcripts.jsonl",
) -> str:
    """Write the per-cell transcript records as JSONL into ``out_dir`` (append-only
    dated run directory). Returns the path written. One JSON object per line per cell."""
    os.makedirs(out_dir, exist_ok=True)
    records = build_transcript_records(report, template_hash=template_hash,
                                       timestamp=timestamp, run_meta=run_meta)
    path = os.path.join(out_dir, filename)
    with open(path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return path
