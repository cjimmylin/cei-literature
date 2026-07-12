"""Grouped style-redacted lexical and length audit for TABLETS P1."""

import hashlib
import math
import re

import numpy as np
from scipy.sparse import csr_matrix, hstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score

from audits.schema_balance import TABLETS_ROOT, parse_jsonl_bytes, read_artifact_bytes
from itembank.generator import build_private_row
from tablets_constants import COMMANDMENT_SPECS, PAIRS


EXPECTED_PUBLIC_SHA256 = (
    "5c60194de2a1fd57276af83706bd8ff536749ee5039611711de7e5da61b44b4d"
)
LEXICAL_AUDIT_SEED = 20_260_711
_PAIR_THRESHOLD = 1.0 / 45.0 + 0.10
_GOLD_THRESHOLD = 1.0 / 3.0 + 0.10
_DIRECTION_THRESHOLD = 0.60
_GATE_THRESHOLDS = {
    "pair_bow_length": _PAIR_THRESHOLD,
    "pair_length_only": _PAIR_THRESHOLD,
    "gold_band_bow_length": _GOLD_THRESHOLD,
    "gold_band_length_only": _GOLD_THRESHOLD,
    "direction_bow_length": _DIRECTION_THRESHOLD,
    "direction_length_only": _DIRECTION_THRESHOLD,
}


def style_redacted_prompt(row):
    """Retain generic template/domain/tier style while removing pair semantics."""
    if type(row) is not dict:
        raise ValueError("style redaction requires a public row object")
    if row.get("record_type") != "adjudication" or row.get("severity_tier") not in {
        "T1",
        "T4",
    }:
        raise ValueError("style redaction is defined for endpoint adjudications")
    domain = row.get("domain")
    if type(domain) is not str or not domain:
        raise ValueError("style redaction requires a public domain")
    prompt = row.get("prompt")
    actions = row.get("actions")
    commandment = row.get("commandment")
    if type(prompt) is not str or type(actions) is not list:
        raise ValueError("style redaction requires the actual prompt and actions")
    if type(commandment) is not list or len(commandment) != 2:
        raise ValueError("style redaction requires two named duties")

    action_block = "\n".join(
        "%s — %s" % (action["action_id"], action["artifact"])
        for action in actions
    )
    if not action_block or not prompt.endswith("\n" + action_block):
        raise ValueError("expected action semantic block is absent from prompt")
    redacted = prompt[: -len(action_block)] + "<ACTIONS_REDACTED>"

    redacted, case_count = re.subn(
        r"\bAster-[0-9a-f]{10}\b",
        "<CASE_REDACTED>",
        redacted,
    )
    if case_count != 1:
        raise ValueError("expected case token is absent or duplicated")

    for number in commandment:
        duty = COMMANDMENT_SPECS[number]["duty"]
        if duty not in redacted:
            raise ValueError("expected named duty phrase is absent from prompt")
        redacted = redacted.replace(duty, "<DUTY_REDACTED>")
    return redacted


def _fold_for(pair, realization_index):
    pair_index = PAIRS.index(pair)
    return (
        pair_index
        + 2 * (realization_index - 1)
        + LEXICAL_AUDIT_SEED % 5
    ) % 5


def _expected_fold_assignment():
    return {
        "%s|%d" % (pair, realization): _fold_for(pair, realization)
        for pair in PAIRS
        for realization in range(1, 4)
    }


def _standardized_lengths(train_texts, test_texts):
    train = np.asarray([len(text) for text in train_texts], dtype=float)
    test = np.asarray([len(text) for text in test_texts], dtype=float)
    mean = float(np.mean(train))
    scale = float(np.std(train))
    if scale == 0.0:
        scale = 1.0
    return ((train - mean) / scale)[:, None], ((test - mean) / scale)[:, None]


def _classifier():
    return LogisticRegression(
        solver="liblinear",
        class_weight="balanced",
        random_state=LEXICAL_AUDIT_SEED,
        max_iter=2_000,
    )


def _oof_balanced_accuracy(texts, labels, folds, feature_mode):
    texts = np.asarray(texts, dtype=object)
    labels = np.asarray(labels, dtype=object)
    folds = np.asarray(folds, dtype=int)
    predictions = np.empty(len(labels), dtype=object)
    for fold in range(5):
        train_mask = folds != fold
        test_mask = folds == fold
        train_texts = texts[train_mask].tolist()
        test_texts = texts[test_mask].tolist()
        train_lengths, test_lengths = _standardized_lengths(
            train_texts, test_texts
        )
        if feature_mode == "length_only":
            train_features = train_lengths
            test_features = test_lengths
        elif feature_mode == "bow_length":
            vectorizer = TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2),
                token_pattern=r"(?u)\b\w+\b",
            )
            train_bow = vectorizer.fit_transform(train_texts)
            test_bow = vectorizer.transform(test_texts)
            train_features = hstack(
                [train_bow, csr_matrix(train_lengths)], format="csr"
            )
            test_features = hstack(
                [test_bow, csr_matrix(test_lengths)], format="csr"
            )
        else:
            raise AssertionError("unknown frozen lexical feature mode")
        fitted = _classifier().fit(train_features, labels[train_mask])
        predictions[test_mask] = fitted.predict(test_features)
    return round(float(balanced_accuracy_score(labels, predictions)), 6)


def _load_endpoint_rows(tablets_root=None):
    artifacts, _ = read_artifact_bytes(tablets_root=tablets_root)
    public_hash = hashlib.sha256(artifacts["public"]).hexdigest()
    if public_hash != EXPECTED_PUBLIC_SHA256:
        raise ValueError("lexical audit source public bank hash drift")
    public = parse_jsonl_bytes(artifacts["public"], "public")
    private = parse_jsonl_bytes(artifacts["private"], "private")
    private_by_id = {row["id"]: row for row in private}
    endpoint = [
        row
        for row in public
        if row["record_type"] == "adjudication"
        and row["framing_arm"] == "neutral"
        and row["monitoring_condition"] == "unmonitored"
        and row["severity_tier"] in {"T1", "T4"}
    ]
    if len(endpoint) != 270:
        raise ValueError("lexical audit endpoint row count drift")
    rows = []
    for public_row in endpoint:
        private_row = private_by_id.get(public_row["id"])
        if private_row is None or private_row != build_private_row(public_row):
            raise ValueError("lexical audit private gold-band binding drift")
        group = "%s|%d" % (
            public_row["pair"],
            public_row["realization_index"],
        )
        rows.append(
            {
                "public": public_row,
                "group": group,
                "fold": _fold_for(
                    public_row["pair"], public_row["realization_index"]
                ),
                "gold_band": private_row["authoring_gold_band"],
            }
        )
    return rows, public_hash


def _build_lexical_audit(tablets_root=None):
    rows, public_hash = _load_endpoint_rows(tablets_root)
    fold_assignment = _expected_fold_assignment()
    groups = {row["group"] for row in rows}
    if groups != set(fold_assignment):
        raise ValueError("lexical audit group coverage drift")
    group_folds = {}
    group_counts = {}
    for row in rows:
        group_folds.setdefault(row["group"], set()).add(row["fold"])
        group_counts[row["group"]] = group_counts.get(row["group"], 0) + 1
    if any(len(folds) != 1 for folds in group_folds.values()) or set(
        group_counts.values()
    ) != {2}:
        raise ValueError("lexical audit group crosses folds or lacks endpoint pair")

    style_texts = [style_redacted_prompt(row["public"]) for row in rows]
    raw_texts = [row["public"]["prompt"] for row in rows]
    folds = [row["fold"] for row in rows]
    labels = {
        "pair": [row["public"]["pair"] for row in rows],
        "gold_band": [row["gold_band"] for row in rows],
        "direction": [row["public"]["direction_permutation"] for row in rows],
    }
    fold_diagnostics = {}
    for fold in range(5):
        train_indices = [index for index, value in enumerate(folds) if value != fold]
        test_rows = sum(value == fold for value in folds)
        diagnostic = {
            "train_rows": len(train_indices),
            "test_rows": test_rows,
            "train_pair_classes": len({labels["pair"][i] for i in train_indices}),
            "train_gold_band_classes": len(
                {labels["gold_band"][i] for i in train_indices}
            ),
            "train_direction_classes": len(
                {labels["direction"][i] for i in train_indices}
            ),
        }
        if diagnostic != {
            "train_rows": 216,
            "test_rows": 54,
            "train_pair_classes": 45,
            "train_gold_band_classes": 3,
            "train_direction_classes": 2,
        }:
            raise ValueError("lexical audit training fold loses a frozen class")
        fold_diagnostics[str(fold)] = diagnostic

    gate_specs = (
        ("pair_bow_length", "pair", "bow_length"),
        ("pair_length_only", "pair", "length_only"),
        ("gold_band_bow_length", "gold_band", "bow_length"),
        ("gold_band_length_only", "gold_band", "length_only"),
        ("direction_bow_length", "direction", "bow_length"),
        ("direction_length_only", "direction", "length_only"),
    )
    gates = {}
    for name, label_name, feature_mode in gate_specs:
        accuracy = _oof_balanced_accuracy(
            style_texts, labels[label_name], folds, feature_mode
        )
        threshold = _GATE_THRESHOLDS[name]
        gates[name] = {
            "label": label_name,
            "feature_view": feature_mode,
            "balanced_accuracy": accuracy,
            "threshold": threshold,
            "status": "PASS" if accuracy <= threshold else "REWORK",
        }
    raw_pair_accuracy = _oof_balanced_accuracy(
        raw_texts, labels["pair"], folds, "bow_length"
    )
    return {
        "audit": "TABLETS_LEXICAL_LENGTH",
        "schema_version": "tablets-lexical-audit.v1",
        "status": (
            "PASS"
            if all(gate["status"] == "PASS" for gate in gates.values())
            else "REWORK"
        ),
        "source_public_sha256": public_hash,
        "seed": LEXICAL_AUDIT_SEED,
        "subset": "COMMON_ENDPOINT_NEUTRAL_BASE_ONLY",
        "row_count": 270,
        "group_count": 135,
        "fold_count": 5,
        "fold_assignment": fold_assignment,
        "fold_diagnostics": fold_diagnostics,
        "style_redaction": {
            "case_token": "REDACTED",
            "named_duties": "REDACTED",
            "action_semantics": "REDACTED",
            "pair_specific_content": "REDACTED",
            "retained_surface": ["generic_template", "domain", "severity_tier"],
        },
        "gates": gates,
        "raw_pair_diagnostic": {
            "label": "pair",
            "feature_view": "raw_prompt_bow_length",
            "balanced_accuracy": raw_pair_accuracy,
            "status": "DIAGNOSTIC_ONLY",
            "affects_overall_status": False,
        },
        "real_10pct_finetune_status": "NOT_RUN",
    }


def _validate_structure(report):
    if type(report) is not dict:
        raise ValueError("lexical audit report must be an object")
    if report.get("source_public_sha256") != EXPECTED_PUBLIC_SHA256:
        raise ValueError("lexical audit source public hash drift")
    if (
        report.get("seed") != LEXICAL_AUDIT_SEED
        or report.get("row_count") != 270
        or report.get("group_count") != 135
        or report.get("fold_count") != 5
        or report.get("subset") != "COMMON_ENDPOINT_NEUTRAL_BASE_ONLY"
    ):
        raise ValueError("lexical audit frozen sample contract drift")
    expected_folds = _expected_fold_assignment()
    if report.get("fold_assignment") != expected_folds:
        raise ValueError("lexical audit fold/group assignment drift")
    for pair in PAIRS:
        pair_folds = [
            expected_folds["%s|%d" % (pair, realization)]
            for realization in range(1, 4)
        ]
        if len(set(pair_folds)) != 3:
            raise ValueError("lexical audit pair groups leak across folds")
    gates = report.get("gates")
    if type(gates) is not dict or set(gates) != set(_GATE_THRESHOLDS):
        raise ValueError("lexical audit gate schema drift")
    for name, threshold in _GATE_THRESHOLDS.items():
        gate = gates[name]
        if type(gate) is not dict or gate.get("threshold") != threshold:
            raise ValueError("lexical audit threshold drift")
        accuracy = gate.get("balanced_accuracy")
        if (
            type(accuracy) not in (int, float)
            or isinstance(accuracy, bool)
            or not math.isfinite(float(accuracy))
            or not 0.0 <= float(accuracy) <= 1.0
        ):
            raise ValueError("lexical audit accuracy is invalid")
        expected_status = "PASS" if accuracy <= threshold else "REWORK"
        if gate.get("status") != expected_status:
            raise ValueError("lexical audit gate status contradicts its threshold")
    expected_overall = (
        "PASS"
        if all(gate["status"] == "PASS" for gate in gates.values())
        else "REWORK"
    )
    if report.get("status") != expected_overall:
        raise ValueError("lexical audit overall status is not fail-closed")
    diagnostic = report.get("raw_pair_diagnostic")
    if (
        type(diagnostic) is not dict
        or diagnostic.get("status") != "DIAGNOSTIC_ONLY"
        or diagnostic.get("affects_overall_status") is not False
    ):
        raise ValueError("raw semantic pair diagnostic may not promote the audit")
    if report.get("real_10pct_finetune_status") != "NOT_RUN":
        raise ValueError("real 10% fine-tune status must remain NOT_RUN")
    return True


def audit_lexical_length(tablets_root=None):
    """Run the deterministic grouped lexical and length audit."""
    report = _build_lexical_audit(tablets_root)
    _validate_structure(report)
    return report


def validate_lexical_audit(report):
    """Reject frozen-field drift and any substituted deterministic result."""
    _validate_structure(report)
    if report != _build_lexical_audit():
        raise ValueError("lexical audit deterministic result drift")
    return True


__all__ = [
    "EXPECTED_PUBLIC_SHA256",
    "LEXICAL_AUDIT_SEED",
    "audit_lexical_length",
    "style_redacted_prompt",
    "validate_lexical_audit",
]
