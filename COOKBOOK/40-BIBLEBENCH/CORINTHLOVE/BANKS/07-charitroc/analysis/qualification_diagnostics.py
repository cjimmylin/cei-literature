#!/usr/bin/env python3
"""Read-only diagnostics for a verified CHARITROC public qualification root.

The source root is verified with the qualification runner's own semantic and
whole-root checks before and after analysis.  Hidden scoring data is read only
from the local bank sidecar and is never copied into the diagnostic report.
"""
from __future__ import annotations

import argparse
import hashlib
from itertools import combinations
import json
import os
from pathlib import Path
import stat
import sys

if __package__ in {None, ""}:
    _BANK_ROOT = Path(__file__).resolve().parents[1]
    if os.fspath(_BANK_ROOT) not in sys.path:
        sys.path.insert(0, os.fspath(_BANK_ROOT))

from pilot import contracts, manifest
from pilot import run_cheap_openrouter as cheap
from scorers import action_scale, stage3_update


DIAGNOSTIC_VERSION = "charitroc-public-qualification-diagnostics-v1"
LIVE_LABEL = "live OpenRouter qualification measurement"
CUES = ("strong", "weak", "absent", "adversarial")
EXPECTED_PUBLIC_EPISODES = 12
CheapOpenRouterQualificationRunner = cheap.CheapOpenRouterQualificationRunner


def _accuracy(correct_count, total):
    if type(correct_count) is not int or type(total) is not int or total <= 0:
        raise ValueError("diagnostic accuracy requires positive integer counts")
    if not 0 <= correct_count <= total:
        raise ValueError("diagnostic accuracy count is outside its denominator")
    return {
        "correct_count": correct_count,
        "incorrect_count": total - correct_count,
        "accuracy": correct_count / total,
    }


def _agreement(count, total):
    if type(count) is not int or type(total) is not int or total <= 0:
        raise ValueError("diagnostic agreement requires positive integer counts")
    if not 0 <= count <= total:
        raise ValueError("diagnostic agreement count is outside its denominator")
    return {"agreement_count": count, "agreement_rate": count / total}


def _score_counts():
    return {str(score): 0 for score in range(len(action_scale.ACTION_ORDER))}


def _assert_complete_verification(verification):
    expected = {"access", "canary", "smoke", "qualification"}
    if (
        type(verification) is not dict
        or verification.get("valid") is not True
        or verification.get("purpose") != "qualification-only"
        or type(verification.get("scopes")) is not dict
        or set(verification["scopes"]) != expected
        or any(
            type(row) is not dict or row.get("valid") is not True
            for row in verification["scopes"].values()
        )
    ):
        raise ValueError("qualification runner did not verify every required scope")


def _assert_live_report(runner, report):
    false_fields = (
        "authorizes_calibration", "authorizes_private_execution",
        "authorizes_freeze",
    )
    if (
        runner.run_mode != "live"
        or runner.provenance != LIVE_LABEL
        or type(report) is not dict
        or report.get("purpose") != "qualification-only"
        or report.get("measurement_label") != LIVE_LABEL
        or report.get("measurement_ready") is not True
        or any(report.get(field) is not False for field in false_fields)
        or type(report.get("report_sha256")) is not str
        or len(report["report_sha256"]) != 64
        or type(report.get("smoke_report_sha256")) is not str
        or len(report["smoke_report_sha256"]) != 64
    ):
        raise ValueError("diagnostics require a verified live qualification report")


def _verified_artifact_hashes(runner, smoke_report):
    expected = {
        (episode["id"], model)
        for episode in runner.public_episodes
        for model in runner.models
    }
    if type(smoke_report) is not dict or type(
            smoke_report.get("artifacts")) is not list:
        raise ValueError("verified smoke artifact manifest is unavailable")
    hashes = {}
    for row in smoke_report["artifacts"]:
        if type(row) is not dict:
            raise ValueError("verified smoke artifact manifest is invalid")
        key = (row.get("item_id"), row.get("logical_model_id"))
        digest = row.get("artifact_sha256")
        if (
            key not in expected
            or key in hashes
            or type(digest) is not str
            or len(digest) != 64
            or any(character not in "0123456789abcdef" for character in digest)
        ):
            raise ValueError("verified smoke artifact manifest differs")
        expected_path = runner._episode_path(*key)
        if row.get("relative_path") != expected_path.relative_to(
                runner.out_dir).as_posix():
            raise ValueError("verified smoke artifact path differs")
        hashes[key] = digest
    if set(hashes) != expected:
        raise ValueError("verified smoke artifact coverage differs")
    return hashes


def _read_bound_json(path, expected_sha256):
    """Read once from a no-follow descriptor and bind those exact bytes."""
    try:
        lexical = os.lstat(path)
    except OSError as exc:
        raise ValueError("qualification episode artifact is missing") from exc
    if stat.S_ISLNK(lexical.st_mode) or not stat.S_ISREG(lexical.st_mode):
        raise ValueError("qualification episode artifact is not a regular file")
    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(os.fspath(path), flags)
    except OSError as exc:
        raise ValueError("qualification episode artifact cannot be opened") from exc
    try:
        opened = os.fstat(descriptor)
        if (
            not stat.S_ISREG(opened.st_mode)
            or (lexical.st_dev, lexical.st_ino)
            != (opened.st_dev, opened.st_ino)
        ):
            raise ValueError("qualification episode artifact changed before read")
        chunks = []
        digest = hashlib.sha256()
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
            digest.update(chunk)
        completed = os.fstat(descriptor)
        if (
            (opened.st_dev, opened.st_ino, opened.st_size, opened.st_mtime_ns)
            != (
                completed.st_dev, completed.st_ino,
                completed.st_size, completed.st_mtime_ns,
            )
        ):
            raise ValueError("qualification episode artifact changed during read")
    finally:
        os.close(descriptor)
    if digest.hexdigest() != expected_sha256:
        raise ValueError("qualification verified artifact hash differs")
    try:
        return json.loads(
            b"".join(chunks).decode("utf-8"),
            object_pairs_hook=cheap._unique_object,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError):
        raise ValueError("qualification episode artifact JSON is invalid") from None


def _read_scored_rows(runner, artifact_hashes):
    rows = {model: {} for model in runner.models}
    for model in runner.models:
        for episode in runner.public_episodes:
            item_id = episode["id"]
            hidden = runner._sidecar[item_id]
            path = runner._episode_path(item_id, model)
            artifact = runner._validate_episode_artifact(
                _read_bound_json(path, artifact_hashes[(item_id, model)]),
                item_id,
                model,
            )
            raw_stage2 = runner._response_for_stage(artifact, "stage_2")
            raw_stage3 = runner._response_for_stage(artifact, "stage_3")
            raw_stage4 = runner._response_for_stage(artifact, "stage_4")
            stage2 = action_scale.score_response(raw_stage2)
            stage3 = action_scale.score_response(raw_stage3)
            stage4 = action_scale.score_response(raw_stage4)
            update = stage3_update.score_update(
                raw_stage2,
                raw_stage3,
                hidden["true_type"],
                hidden["cue_variant"],
                hidden["expected_stage3"],
            )
            if (
                stage2["mechanical_flag"]
                or stage3["mechanical_flag"]
                or stage4["mechanical_flag"]
                or update["mechanical_flag"]
            ):
                raise ValueError(
                    "qualification diagnostic inputs are not mechanically resolved"
                )
            rows[model][item_id] = {
                "cue_variant": hidden["cue_variant"],
                "true_type": hidden["true_type"],
                "belief_correct": update["belief_correct"],
                "action_correct": update["action_correct"],
                "joint_correct": update["update_correct"],
                "stage3_belief": stage3["intent_score"],
                "stage3_action": stage3["score"],
                "stage4_belief": stage4["intent_score"],
                "stage4_action": stage4["score"],
                "stage4_grade": stage4["grade"],
            }
    return rows


def _model_diagnostic(model_rows):
    ordered = list(model_rows.values())
    total = len(ordered)
    if total == 0:
        raise ValueError("qualification diagnostic has no public episodes")
    stage3_accuracy = {
        "belief": _accuracy(
            sum(row["belief_correct"] for row in ordered), total
        ),
        "action": _accuracy(
            sum(row["action_correct"] for row in ordered), total
        ),
        "joint": _accuracy(
            sum(row["joint_correct"] for row in ordered), total
        ),
    }
    scores = _score_counts()
    grades = {grade: 0 for grade in action_scale.ACTION_ORDER}
    by_cue = {}
    for cue in CUES:
        cue_rows = [row for row in ordered if row["cue_variant"] == cue]
        if not cue_rows:
            raise ValueError(f"qualification diagnostic lacks {cue} cue coverage")
        cue_scores = _score_counts()
        for row in cue_rows:
            cue_scores[str(row["stage4_action"])] += 1
        by_cue[cue] = {
            "n_public_episodes": len(cue_rows),
            "stage3_belief_correct_count": sum(
                row["belief_correct"] for row in cue_rows
            ),
            "stage3_action_correct_count": sum(
                row["action_correct"] for row in cue_rows
            ),
            "stage3_joint_correct_count": sum(
                row["joint_correct"] for row in cue_rows
            ),
            "stage4_score_counts": cue_scores,
        }
    for row in ordered:
        scores[str(row["stage4_action"])] += 1
        grades[row["stage4_grade"]] += 1
    truth_means = {}
    for true_type in ("benign", "malicious"):
        truth_rows = [row for row in ordered if row["true_type"] == true_type]
        if not truth_rows:
            raise ValueError(
                f"qualification diagnostic lacks {true_type} truth coverage"
            )
        truth_means[true_type] = {
            "n_public_episodes": len(truth_rows),
            "mean_score": (
                sum(row["stage4_action"] for row in truth_rows)
                / len(truth_rows)
            ),
        }
    return {
        "n_public_episodes": total,
        "stage3_accuracy": stage3_accuracy,
        "stage4_score_distribution": {
            "score_counts": scores,
            "grade_counts": grades,
            "truth_specific_score_means": truth_means,
        },
        "cue_specific_counts": by_cue,
    }


def _pairwise_agreement(rows, model_a, model_b, item_ids):
    pairs = [(rows[model_a][item_id], rows[model_b][item_id])
             for item_id in item_ids]
    total = len(pairs)

    def count_equal(*fields):
        return sum(
            all(left[field] == right[field] for field in fields)
            for left, right in pairs
        )

    return {
        "model_a": model_a,
        "model_b": model_b,
        "n_public_episodes": total,
        "stage3": {
            "belief": _agreement(count_equal("stage3_belief"), total),
            "action": _agreement(count_equal("stage3_action"), total),
            "joint": _agreement(count_equal(
                "stage3_belief", "stage3_action"
            ), total),
        },
        "stage4": {
            "belief": _agreement(count_equal("stage4_belief"), total),
            "action": _agreement(count_equal("stage4_action"), total),
            "joint": _agreement(count_equal(
                "stage4_belief", "stage4_action"
            ), total),
        },
    }


def _build_verified_diagnostics(runner):
    """Build diagnostics after two complete semantic/whole-root verifications."""
    first_verification = runner.verify("all")
    _assert_complete_verification(first_verification)
    source_report = runner._verify_qualification_report(return_report=True)
    _assert_live_report(runner, source_report)
    smoke_report = _read_bound_json(
        runner._path("reports", "smoke.json"),
        source_report["smoke_report_sha256"],
    )
    artifact_hashes = _verified_artifact_hashes(runner, smoke_report)
    item_ids = [row["id"] for row in runner.public_episodes]
    if (
        len(item_ids) != len(set(item_ids))
        or source_report.get("public_episode_count_per_model") != len(item_ids)
    ):
        raise ValueError("qualification diagnostic public coverage differs")

    rows = _read_scored_rows(runner, artifact_hashes)
    model_diagnostics = {
        model: _model_diagnostic(rows[model]) for model in runner.models
    }
    agreements = {}
    for model_a, model_b in combinations(runner.models, 2):
        key = f"{model_a}__{model_b}"
        agreements[key] = _pairwise_agreement(
            rows, model_a, model_b, item_ids
        )

    guards = [
        (
            f"Public N={len(item_ids)} qualification only; not calibration, "
            "a private benchmark result, or a multi-vendor concordance test."
        ),
        (
            "Stage-3 joint belief/action accuracy must not be used alone for "
            "model ranking."
        ),
        (
            "Invalid case evidence does not necessarily prove malicious motive; "
            "belief and action channels must be interpreted separately."
        ),
        (
            "The cue/judge bank remains frozen pending replicated localized "
            "evidence for a revision."
        ),
    ]
    payload = {
        "diagnostic_version": DIAGNOSTIC_VERSION,
        "purpose": "qualification-only",
        "measurement_label": LIVE_LABEL,
        "measurement_ready": True,
        "authorizes_calibration": False,
        "authorizes_private_execution": False,
        "authorizes_freeze": False,
        "profile_id": source_report["profile_id"],
        "profile_sha256": source_report["profile_sha256"],
        "source_qualification_report_sha256": source_report["report_sha256"],
        "public_episode_count_per_model": len(item_ids),
        "logical_model_ids": list(runner.models),
        "model_diagnostics": model_diagnostics,
        "between_model_exact_agreement": agreements,
        "agreement_definition": (
            "Exact equality of mechanically scored INTENT and DECISION fields; "
            "reason text is excluded."
        ),
        "interpretation_guards": guards,
    }
    payload["diagnostic_sha256"] = contracts.canonical_sha256(payload)

    second_verification = runner.verify("all")
    _assert_complete_verification(second_verification)
    final_report = runner._verify_qualification_report(return_report=True)
    if contracts.canonical_json_bytes(final_report) != contracts.canonical_json_bytes(
            source_report):
        raise ValueError("qualification report changed during diagnostics")
    return payload


def _require_regular_file(path, label):
    try:
        mode = os.lstat(path).st_mode
    except OSError as exc:
        raise ValueError(f"{label} is missing") from exc
    if stat.S_ISLNK(mode) or not stat.S_ISREG(mode):
        raise ValueError(f"{label} must be a regular file")


def build_live_diagnostics(
        *, bank_root, run_root, profile_id=manifest.CHEAP_PROFILE_ID):
    """Analyze one existing live root without creating or changing it."""
    if profile_id not in manifest.QUALIFICATION_PROFILE_IDS:
        raise ValueError("qualification diagnostic profile_id is not frozen")
    bank = Path(bank_root).expanduser().resolve()
    lexical_root = Path(run_root).expanduser().absolute()
    try:
        root_mode = os.lstat(lexical_root).st_mode
    except OSError as exc:
        raise ValueError("qualification run_metadata root is missing") from exc
    if stat.S_ISLNK(root_mode) or not stat.S_ISDIR(root_mode):
        raise ValueError("qualification root must be an existing real directory")
    root = lexical_root.resolve()
    _require_regular_file(root / "run_metadata.json", "run_metadata")
    _require_regular_file(
        root / "reports/qualification.json", "qualification report"
    )
    runner = CheapOpenRouterQualificationRunner(
        bank_root=bank,
        out_dir=root,
        run_mode="live",
        profile_id=profile_id,
    )
    if len(runner.public_episodes) != EXPECTED_PUBLIC_EPISODES:
        raise ValueError("live diagnostics require the exact 12-item public bank")
    return _build_verified_diagnostics(runner)


def render_markdown(payload):
    """Render a concise human-readable view of the hashed JSON diagnostic."""
    if (
        type(payload) is not dict
        or payload.get("purpose") != "qualification-only"
        or payload.get("diagnostic_sha256") != contracts.canonical_sha256({
            key: value for key, value in payload.items()
            if key != "diagnostic_sha256"
        })
    ):
        raise ValueError("diagnostic payload hash or purpose differs")
    lines = [
        "# CHARITROC Public Qualification Diagnostics",
        "",
        "> **Qualification only — not calibration, private measurement, or a "
        "freeze authorization.**",
        "",
        f"Source report SHA-256: `{payload['source_qualification_report_sha256']}`",
        "",
        "## Stage-3 and Stage-4 summary",
        "",
        "| Model | N | Belief acc. | Action acc. | Joint acc. | Benign mean | Malicious mean | Stage-4 scores 0/1/2/3/4 |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for model in payload["logical_model_ids"]:
        row = payload["model_diagnostics"][model]
        accuracy = row["stage3_accuracy"]
        stage4 = row["stage4_score_distribution"]
        counts = stage4["score_counts"]
        truth_means = stage4["truth_specific_score_means"]
        distribution = "/".join(str(counts[str(score)]) for score in range(5))
        lines.append(
            f"| {model} | {row['n_public_episodes']} | "
            f"{accuracy['belief']['accuracy']:.4f} | "
            f"{accuracy['action']['accuracy']:.4f} | "
            f"{accuracy['joint']['accuracy']:.4f} | "
            f"{truth_means['benign']['mean_score']:.4f} | "
            f"{truth_means['malicious']['mean_score']:.4f} | "
            f"{distribution} |"
        )
    lines.extend([
        "",
        "## Cue-specific counts",
        "",
        "| Model | Cue | N | Belief correct | Action correct | Joint correct | Stage-4 scores 0/1/2/3/4 |",
        "|---|---|---:|---:|---:|---:|---|",
    ])
    for model in payload["logical_model_ids"]:
        cue_rows = payload["model_diagnostics"][model]["cue_specific_counts"]
        for cue in CUES:
            row = cue_rows[cue]
            distribution = "/".join(
                str(row["stage4_score_counts"][str(score)])
                for score in range(5)
            )
            lines.append(
                f"| {model} | {cue} | {row['n_public_episodes']} | "
                f"{row['stage3_belief_correct_count']} | "
                f"{row['stage3_action_correct_count']} | "
                f"{row['stage3_joint_correct_count']} | {distribution} |"
            )
    lines.extend([
        "",
        "## Between-model exact agreement",
        "",
        "| Pair | S3 belief/action/joint | S4 belief/action/joint |",
        "|---|---|---|",
    ])
    for key, row in payload["between_model_exact_agreement"].items():
        s3 = "/".join(f"{row['stage3'][field]['agreement_rate']:.4f}"
                      for field in ("belief", "action", "joint"))
        s4 = "/".join(f"{row['stage4'][field]['agreement_rate']:.4f}"
                      for field in ("belief", "action", "joint"))
        lines.append(f"| {key} | {s3} | {s4} |")
    lines.extend(["", "## Interpretation guards", ""])
    lines.extend(f"- {guard}" for guard in payload["interpretation_guards"])
    lines.extend([
        "",
        f"Diagnostic SHA-256: `{payload['diagnostic_sha256']}`",
        "",
    ])
    return "\n".join(lines)


def _safe_output_path(path, source_root):
    candidate = Path(path).expanduser().absolute()
    parent = candidate.parent.resolve()
    resolved = parent / candidate.name
    try:
        resolved.relative_to(source_root)
    except ValueError:
        return resolved
    raise ValueError("diagnostic outputs must remain outside the live root")


def _write_new_or_validate(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() or path.is_symlink():
        if path.is_symlink() or not path.is_file():
            raise ValueError("diagnostic output must be a regular file")
        if path.read_text(encoding="utf-8") != content:
            raise ValueError("existing diagnostic output differs")
        return
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())


def write_reports(payload, *, json_path, markdown_path, source_run_root):
    """Write idempotent reports outside the immutable qualification root."""
    source = Path(source_run_root).expanduser().resolve(strict=True)
    json_out = _safe_output_path(json_path, source)
    markdown_out = _safe_output_path(markdown_path, source)
    json_text = contracts.canonical_json_bytes(payload).decode("utf-8") + "\n"
    markdown_text = render_markdown(payload)
    _write_new_or_validate(json_out, json_text)
    _write_new_or_validate(markdown_out, markdown_text)
    return json_out, markdown_out


def build_parser():
    parser = argparse.ArgumentParser(
        description="Read-only CHARITROC public qualification diagnostics"
    )
    parser.add_argument("--run-root", required=True)
    parser.add_argument(
        "--bank-root", default=os.fspath(Path(__file__).resolve().parents[1])
    )
    parser.add_argument("--json-out")
    parser.add_argument("--markdown-out")
    parser.add_argument(
        "--profile-id",
        choices=manifest.QUALIFICATION_PROFILE_IDS,
        default=manifest.CHEAP_PROFILE_ID,
    )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if (args.json_out is None) != (args.markdown_out is None):
        raise SystemExit("--json-out and --markdown-out must be supplied together")
    payload = build_live_diagnostics(
        bank_root=Path(args.bank_root),
        run_root=Path(args.run_root),
        profile_id=args.profile_id,
    )
    if args.json_out is not None:
        paths = write_reports(
            payload,
            json_path=Path(args.json_out),
            markdown_path=Path(args.markdown_out),
            source_run_root=Path(args.run_root),
        )
        sys.stdout.write(json.dumps({
            "json_report": os.fspath(paths[0]),
            "markdown_report": os.fspath(paths[1]),
            "purpose": "qualification-only",
            "diagnostic_sha256": payload["diagnostic_sha256"],
        }, sort_keys=True, separators=(",", ":")) + "\n")
    else:
        sys.stdout.write(
            contracts.canonical_json_bytes(payload).decode("utf-8") + "\n"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
